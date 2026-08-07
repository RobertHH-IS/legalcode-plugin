#!/usr/bin/env python3
"""Validate Legalcode's portable and client-specific plugin package contracts."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from jsonschema.validators import validator_for


REPO_ROOT = Path(__file__).resolve().parents[1]
PLUGIN_VERSION = "1.0.0"
REPOSITORY_URL = "https://github.com/RobertHH-IS/legalcode-plugin"
PLUGIN_SCHEMA_URL = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
MCP_SCHEMA_URL = "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json"
PUBLIC_MCP_URL = "https://mcp.legalcode.md/mcp"
PRO_MCP_URL = "https://mcppro.legalcode.md/mcp"

EXPECTED_SKILLS = {
    "business-legal-radar-private-agent-watch",
    "legalcode-anti-gold-plating-is",
    "legalcode-case-timeline-builder",
    "legalcode-contract-review",
    "legalcode-document-qa",
    "legalcode-docx-render",
    "legalcode-dpia-generator",
    "legalcode-legal-memorandum",
    "legalcode-mcp-setup",
    "legalcode-nda-triage",
    "legalcode-public-search",
    "legalcode-statute-analysis",
    "legalcode-tabular-review",
}


@dataclass(frozen=True)
class Bundle:
    name: str
    vendor_manifest: str
    endpoint: str


BUNDLES = (
    Bundle("legalcode-codex", ".codex-plugin/plugin.json", PUBLIC_MCP_URL),
    Bundle(
        "legalcode-claude-code",
        ".claude-plugin/plugin.json",
        PUBLIC_MCP_URL,
    ),
    Bundle("legalcode-pro-codex", ".codex-plugin/plugin.json", PRO_MCP_URL),
    Bundle(
        "legalcode-pro-claude-code",
        ".claude-plugin/plugin.json",
        PRO_MCP_URL,
    ),
)


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path.relative_to(REPO_ROOT)} must contain a JSON object")
    return value


def fetch_schema(url: str) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "legalcode-plugin-conformance/1.0"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        value = json.load(response)
    if not isinstance(value, dict):
        raise ValueError(f"canonical schema at {url} is not a JSON object")
    return value


def json_path(parts: list[Any]) -> str:
    rendered = "$"
    for part in parts:
        rendered += f"[{part}]" if isinstance(part, int) else f".{part}"
    return rendered


def validate_against_schema(
    path: Path,
    document: dict[str, Any],
    schema: dict[str, Any],
    failures: list[str],
) -> None:
    validator_class = validator_for(schema)
    validator_class.check_schema(schema)
    validator = validator_class(schema)
    for error in sorted(
        validator.iter_errors(document),
        key=lambda item: list(item.absolute_path),
    ):
        failures.append(
            f"{path.relative_to(REPO_ROOT)} {json_path(list(error.absolute_path))}: "
            f"{error.message}"
        )


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def validate_bundle(
    bundle: Bundle,
    plugin_schema: dict[str, Any],
    mcp_schema: dict[str, Any],
    failures: list[str],
) -> list[Path]:
    bundle_root = REPO_ROOT / "plugins" / bundle.name
    portable_manifest_path = bundle_root / "plugin.json"
    portable_mcp_path = bundle_root / "mcp.json"
    vendor_manifest_path = bundle_root / bundle.vendor_manifest
    legacy_mcp_path = bundle_root / ".mcp.json"

    portable_manifest = load_json(portable_manifest_path)
    portable_mcp = load_json(portable_mcp_path)
    vendor_manifest = load_json(vendor_manifest_path)
    legacy_mcp = load_json(legacy_mcp_path)

    validate_against_schema(
        portable_manifest_path,
        portable_manifest,
        plugin_schema,
        failures,
    )
    validate_against_schema(portable_mcp_path, portable_mcp, mcp_schema, failures)

    prefix = f"plugins/{bundle.name}"
    require(
        portable_manifest.get("name") == bundle.name,
        f"{prefix}/plugin.json name must match its bundle directory",
        failures,
    )
    require(
        vendor_manifest.get("name") == bundle.name,
        f"{prefix}/{bundle.vendor_manifest} name must match its bundle directory",
        failures,
    )
    require(
        portable_manifest.get("version") == PLUGIN_VERSION,
        f"{prefix}/plugin.json version must be {PLUGIN_VERSION}",
        failures,
    )
    require(
        vendor_manifest.get("version") == PLUGIN_VERSION,
        f"{prefix}/{bundle.vendor_manifest} version must be {PLUGIN_VERSION}",
        failures,
    )
    require(
        portable_manifest.get("description") == vendor_manifest.get("description"),
        f"{prefix} portable and vendor descriptions must match",
        failures,
    )
    require(
        portable_manifest.get("keywords") == vendor_manifest.get("keywords"),
        f"{prefix} portable and vendor keywords must match",
        failures,
    )
    require(
        portable_manifest.get("repository") == REPOSITORY_URL,
        f"{prefix}/plugin.json repository must be {REPOSITORY_URL}",
        failures,
    )

    portable_server = portable_mcp.get("mcpServers", {}).get("legalcode", {})
    legacy_server = legacy_mcp.get("mcpServers", {}).get("legalcode", {})
    require(
        set(portable_mcp.get("mcpServers", {})) == {"legalcode"},
        f"{prefix}/mcp.json must declare exactly the legalcode server",
        failures,
    )
    require(
        portable_server
        == {"type": "streamable-http", "url": bundle.endpoint},
        f"{prefix}/mcp.json must map legalcode to {bundle.endpoint} via streamable-http",
        failures,
    )
    require(
        legacy_server == {"url": bundle.endpoint},
        f"{prefix}/.mcp.json must map legalcode to {bundle.endpoint}",
        failures,
    )

    skills_root = bundle_root / "skills"
    skill_directories = {
        path.name
        for path in skills_root.iterdir()
        if path.is_dir() and (path / "SKILL.md").is_file()
    }
    require(
        skill_directories == EXPECTED_SKILLS,
        f"{prefix}/skills inventory differs from the expected 13 skills",
        failures,
    )
    return [skills_root / name for name in sorted(skill_directories)]


def validate_marketplaces(failures: list[str]) -> None:
    codex_marketplace = load_json(REPO_ROOT / ".agents/plugins/marketplace.json")
    codex_entries = codex_marketplace.get("plugins", [])
    expected_codex_names = ["legalcode-codex", "legalcode-pro-codex"]
    require(
        [entry.get("name") for entry in codex_entries] == expected_codex_names,
        "Codex marketplace plugin names or ordering changed",
        failures,
    )
    for entry in codex_entries:
        name = entry.get("name")
        require(
            entry.get("source")
            == {"source": "local", "path": f"./plugins/{name}"},
            f"Codex marketplace source for {name} must remain repo-local",
            failures,
        )
        require(
            entry.get("policy")
            == {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
            f"Codex marketplace policy for {name} changed",
            failures,
        )

    claude_marketplace = load_json(REPO_ROOT / ".claude-plugin/marketplace.json")
    require(
        claude_marketplace.get("metadata", {}).get("version") == PLUGIN_VERSION,
        f"Claude marketplace metadata version must be {PLUGIN_VERSION}",
        failures,
    )
    claude_entries = claude_marketplace.get("plugins", [])
    expected_claude_names = [
        "legalcode-claude-code",
        "legalcode-pro-claude-code",
    ]
    require(
        [entry.get("name") for entry in claude_entries] == expected_claude_names,
        "Claude marketplace plugin names or ordering changed",
        failures,
    )
    for entry in claude_entries:
        name = entry.get("name")
        require(
            entry.get("source") == f"./plugins/{name}",
            f"Claude marketplace source for {name} must remain repo-local",
            failures,
        )
        require(
            entry.get("version") == PLUGIN_VERSION,
            f"Claude marketplace version for {name} must be {PLUGIN_VERSION}",
            failures,
        )


def validate_skills(skill_directories: list[Path], failures: list[str]) -> None:
    executable = shutil.which("skills-ref")
    if executable is None:
        failures.append(
            "skills-ref is unavailable; install the pinned requirements-dev.txt dependencies"
        )
        return
    for skill_directory in skill_directories:
        result = subprocess.run(
            [executable, "validate", str(skill_directory)],
            check=False,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            details = (result.stdout + result.stderr).strip()
            failures.append(
                f"{skill_directory.relative_to(REPO_ROOT)} failed skills-ref validation: "
                f"{details or 'no diagnostic output'}"
            )


def main() -> int:
    failures: list[str] = []
    try:
        plugin_schema = fetch_schema(PLUGIN_SCHEMA_URL)
        mcp_schema = fetch_schema(MCP_SCHEMA_URL)
        skill_directories: list[Path] = []
        for bundle in BUNDLES:
            skill_directories.extend(
                validate_bundle(bundle, plugin_schema, mcp_schema, failures)
            )
        validate_marketplaces(failures)
        validate_skills(skill_directories, failures)
    except Exception as error:  # Surface malformed files and unavailable schemas clearly.
        failures.append(str(error))

    if failures:
        print("Agent Plugins conformance failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(
        f"Agent Plugins conformance passed: {len(BUNDLES)} bundles, "
        f"{len(BUNDLES) * len(EXPECTED_SKILLS)} skills."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
