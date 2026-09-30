#!/usr/bin/env python3
"""Build and validate the complete Legalcode OpenAI upload ZIP."""

from __future__ import annotations

import hashlib
import json
import re
import struct
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "plugins" / "legalcode-openai"
VALIDATOR = ROOT / "scripts" / "validate_openai_submission.py"


def validate(path: Path) -> None:
    subprocess.run([sys.executable, str(VALIDATOR), "--package-root", str(path)],
                   cwd=ROOT, check=True)


def main() -> None:
    validate(PACKAGE)
    manifest = json.loads((PACKAGE / ".codex-plugin/plugin.json").read_text())
    version = manifest["version"]
    files = sorted(path for path in PACKAGE.rglob("*")
                   if path.is_file() and path.name != ".DS_Store")
    secret_pattern = re.compile(
        rb"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|"
        rb"\b(?:sk-[A-Za-z0-9_-]{20,}|ghp_[A-Za-z0-9]{30,})\b|"
        rb'"(?:access_token|refresh_token|client_secret|password)"\s*:\s*"[^"\s]+"'
    )
    for path in files:
        if path.is_symlink():
            raise ValueError(f"Symlink cannot be packaged: {path.relative_to(PACKAGE)}")
        if secret_pattern.search(path.read_bytes()):
            raise ValueError(f"Possible secret in {path.relative_to(PACKAGE)}")
    assets = {}
    for path in files:
        if path.suffix == ".png":
            data = path.read_bytes()
            if data[:8] != b"\x89PNG\r\n\x1a\n":
                raise ValueError(f"Invalid PNG: {path.name}")
            width, height = struct.unpack(">II", data[16:24])
            if width != height or not 48 <= width <= 4096 or len(data) > 5 * 1024 * 1024:
                raise ValueError(f"Invalid submission icon size: {path.name}")
            assets[str(path.relative_to(PACKAGE))] = {"width": width, "height": height}
    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    output = dist / f"legalcode-openai-{version}.zip"
    with tempfile.TemporaryDirectory(prefix="legalcode-plugin-package-") as temporary:
        archive_path = Path(temporary) / output.name
        with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for path in files:
                name = path.relative_to(PACKAGE).as_posix()
                entry = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
                entry.create_system = 3
                entry.external_attr = 0o100644 << 16
                entry.compress_type = zipfile.ZIP_DEFLATED
                archive.writestr(entry, path.read_bytes())
        extracted = Path(temporary) / "extracted"
        with zipfile.ZipFile(archive_path) as archive:
            if archive.testzip() is not None:
                raise ValueError("ZIP integrity check failed")
            archive.extractall(extracted)
        validate(extracted)
        file_hashes = {str(path.relative_to(PACKAGE)): hashlib.sha256(path.read_bytes()).hexdigest()
                       for path in files}
        for name, digest in file_hashes.items():
            if hashlib.sha256((extracted / name).read_bytes()).hexdigest() != digest:
                raise ValueError(f"Extracted file differs from source: {name}")
        data = archive_path.read_bytes()
        output.write_bytes(data)
    digest = hashlib.sha256(data).hexdigest()
    output.with_suffix(".zip.sha256").write_text(f"{digest}  {output.name}\n")
    report = {
        "version": version,
        "archive": output.name,
        "bytes": len(data),
        "sha256": digest,
        "files": file_hashes,
        "assets": assets,
        "validation": {
            "source_conformance": "passed", "extracted_archive_conformance": "passed",
            "skill_reference": "passed", "zip_integrity": "passed",
            "source_extracted_hash_parity": "passed", "secret_pattern_scan": "passed",
        },
        "limits": ["Package validation is separate from hosted tool approval and live reviewer scenarios."],
    }
    output.with_suffix(".validation.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"archive": str(output), "bytes": len(data), "files": len(files),
                      "sha256": digest}, indent=2))


if __name__ == "__main__":
    main()
