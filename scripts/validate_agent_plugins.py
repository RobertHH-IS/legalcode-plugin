#!/usr/bin/env python3
"""Validate Legalcode's portable and client-specific plugin package contracts."""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from jsonschema.validators import validator_for


REPO_ROOT = Path(__file__).resolve().parents[1]
PLUGIN_VERSION = "1.1.0"
REPOSITORY_URL = "https://github.com/RobertHH-IS/legalcode-plugin"
MORE_SKILLS_URL = f"{REPOSITORY_URL}/tree/main/more-skills"
PLUGIN_SCHEMA_URL = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
MCP_SCHEMA_URL = "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json"
PUBLIC_MCP_URL = "https://mcp.legalcode.md/mcp"
PRO_MCP_URL = "https://mcppro.legalcode.md/mcp"
RETIRED_MCP_TOOL_NAMES = {
    "analyze_cases",
    "analyze_pre_laws",
    "fetch_source",
    "find_cases_for_law",
    "find_laws_for_case",
    "get_facets",
    "list_jurisdictions",
    "search_agreements",
    "search_cases",
    "search_guidance",
    "search_laws",
    "search_patents",
    "search_pre_laws",
}

EXPECTED_SKILLS = {
    "legalcode-case-timeline-builder",
    "legalcode-contract-review",
    "legalcode-document-qa",
    "legalcode-dpia-generator",
    "legalcode-legal-memorandum",
    "legalcode-mcp-tool-guide",
    "legalcode-nda-triage",
    "legalcode-public-search",
    "legalcode-statute-analysis",
    "legalcode-tabular-review",
}
ADDITIONAL_SKILLS = {
    "business-legal-radar-private-agent-watch",
    "legalcode-anti-gold-plating-is",
    "legalcode-docx-render",
    "legalcode-mcp-setup",
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
    legacy_cli_helper_path = bundle_root / "scripts" / "install-legalcode-cli.sh"

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
        not legacy_cli_helper_path.exists(),
        f"{prefix} must not ship the unpublished Legalcode CLI install helper",
        failures,
    )
    for manifest_path, manifest in (
        (portable_manifest_path, portable_manifest),
        (vendor_manifest_path, vendor_manifest),
    ):
        require(
            "CLI install helper" not in json.dumps(manifest),
            f"{manifest_path.relative_to(REPO_ROOT)} must not advertise a Legalcode CLI helper",
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
        portable_server == {"type": "streamable-http", "url": bundle.endpoint},
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
        f"{prefix}/skills inventory differs from the expected 10 skills",
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
            entry.get("source") == {"source": "local", "path": f"./plugins/{name}"},
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


def validate_openai_bundle(
    plugin_schema: dict[str, Any], failures: list[str]
) -> list[Path]:
    bundle_root = REPO_ROOT / "plugins" / "legalcode-openai"
    portable_path = bundle_root / "plugin.json"
    vendor_path = bundle_root / ".codex-plugin" / "plugin.json"
    portable = load_json(portable_path)
    vendor = load_json(vendor_path)
    validate_against_schema(portable_path, portable, plugin_schema, failures)

    require(
        portable.get("name") == "legalcode",
        "OpenAI portable name must be legalcode",
        failures,
    )
    require(
        vendor.get("name") == "legalcode",
        "OpenAI vendor name must be legalcode",
        failures,
    )
    require(
        portable.get("version") == PLUGIN_VERSION,
        "OpenAI portable version drifted",
        failures,
    )
    require(
        vendor.get("version") == PLUGIN_VERSION,
        "OpenAI vendor version drifted",
        failures,
    )
    require(
        vendor.get("description") == "Primary-source legal research",
        "OpenAI subtitle drifted",
        failures,
    )
    require(
        vendor.get("author", {}).get("name") == "Fordæmi ehf.",
        "OpenAI author must be Fordæmi ehf.",
        failures,
    )
    require(
        vendor.get("repository") == REPOSITORY_URL,
        "OpenAI repository URL drifted",
        failures,
    )

    for required_path in (
        bundle_root / "README.md",
        bundle_root / "LICENSE",
        bundle_root / "THIRD_PARTY_NOTICES.md",
        bundle_root / "assets" / "legalcode-directory-512.png",
        bundle_root / "assets" / "legalcode-composer-48.png",
    ):
        require(
            required_path.is_file(),
            f"{required_path.relative_to(REPO_ROOT)} is required",
            failures,
        )

    for forbidden_path in (
        bundle_root / ".mcp.json",
        bundle_root / "mcp.json",
        bundle_root / "scripts",
        bundle_root / "hooks",
        bundle_root / "apps",
        bundle_root / "app.json",
    ):
        require(
            not forbidden_path.exists(),
            f"{forbidden_path.relative_to(REPO_ROOT)} must not ship",
            failures,
        )

    skills_root = bundle_root / "skills"
    skill_directories = {
        path.name: path
        for path in skills_root.iterdir()
        if path.is_dir() and (path / "SKILL.md").is_file()
    }
    require(
        set(skill_directories) == EXPECTED_SKILLS,
        "OpenAI bundle must contain the exact ten skills",
        failures,
    )
    expected_dependency = (
        "dependencies:\n"
        "  tools:\n"
        "    - type: mcp\n"
        "      value: legalcode\n"
        "      description: Search, retrieve, analyze, and trace primary legal sources\n"
        "      transport: streamable_http\n"
        f"      url: {PUBLIC_MCP_URL}\n"
    )
    for name, directory in skill_directories.items():
        dependency_path = directory / "agents" / "openai.yaml"
        require(
            dependency_path.is_file(),
            f"OpenAI skill {name} lacks agents/openai.yaml",
            failures,
        )
        if dependency_path.is_file():
            require(
                dependency_path.read_text(encoding="utf-8").endswith(
                    expected_dependency
                ),
                f"OpenAI skill {name} has invalid MCP dependency",
                failures,
            )

    return list(skill_directories.values())


def validate_openai_routing_cases(failures: list[str]) -> None:
    cases_path = REPO_ROOT / "tests" / "openai-skill-routing.json"
    document = load_json(cases_path)
    cases = document.get("cases", [])
    require(
        document.get("schema_version") == 1,
        "OpenAI routing test schema drifted",
        failures,
    )
    require(
        isinstance(cases, list) and len(cases) >= 7,
        "OpenAI routing tests must cover activation, non-activation, selection, and sequencing",
        failures,
    )
    case_ids = {case.get("id") for case in cases if isinstance(case, dict)}
    require(
        {
            "activate_capabilities",
            "activate_aggregate_workflow",
            "activate_bad_filter_recovery",
            "select_exact_authority",
            "select_implementation_trace",
            "nonactivation_weather",
            "nonactivation_contract_specific",
        }.issubset(case_ids),
        "OpenAI routing test inventory is incomplete",
        failures,
    )
    for case in cases:
        if not isinstance(case, dict):
            failures.append("OpenAI routing test case must be an object")
            continue
        sequence = case.get("expected_sequence", [])
        require(
            isinstance(sequence, list)
            and all(
                tool
                in {
                    "legalcode_discover",
                    "legalcode_search",
                    "legalcode_fetch",
                    "legalcode_analyze",
                    "legalcode_trace",
                }
                for tool in sequence
            ),
            f"OpenAI routing case {case.get('id')} has an invalid tool sequence",
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
        for markdown_path in skill_directory.rglob("*.md"):
            content = markdown_path.read_text(encoding="utf-8")
            relative_path = markdown_path.relative_to(REPO_ROOT)
            for tool_name in sorted(RETIRED_MCP_TOOL_NAMES):
                if re.search(rf"\b{re.escape(tool_name)}\b", content):
                    failures.append(
                        f"{relative_path} references retired MCP tool {tool_name}"
                    )
            if re.search(r"`guide`", content):
                failures.append(f"{relative_path} references retired MCP tool guide")
            if re.search(
                r"https://mcp(?:pro)?\.legalcode\.md(?!/mcp)",
                content,
            ):
                failures.append(
                    f"{relative_path} uses a Legalcode MCP hostname without /mcp"
                )
            if re.search(r'["\']jurisdictions["\']\s*:', content):
                failures.append(
                    f"{relative_path} uses plural jurisdictions in an MCP call"
                )
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
        skill_directories.extend(validate_openai_bundle(plugin_schema, failures))
        validate_openai_routing_cases(failures)
        validate_marketplaces(failures)
        root_readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        additional_skills_root = REPO_ROOT / "more-skills"
        additional_skill_directories = {
            path.name: path
            for path in additional_skills_root.iterdir()
            if path.is_dir() and (path / "SKILL.md").is_file()
        }
        require(
            set(additional_skill_directories) == ADDITIONAL_SKILLS,
            "more-skills inventory differs from the expected additional skills",
            failures,
        )
        require(
            (additional_skills_root / "README.md").is_file(),
            "more-skills/README.md must explain the optional skill inventory",
            failures,
        )
        skill_directories.extend(additional_skill_directories.values())
        require(
            MORE_SKILLS_URL in root_readme,
            "README.md must link to the additional skills directory",
            failures,
        )
        for bundle in BUNDLES:
            bundle_root = REPO_ROOT / "plugins" / bundle.name
            for reference_path in (
                bundle_root / "README.md",
                bundle_root / "skills" / "legalcode-mcp-tool-guide" / "SKILL.md",
            ):
                require(
                    MORE_SKILLS_URL in reference_path.read_text(encoding="utf-8"),
                    f"{reference_path.relative_to(REPO_ROOT)} must link to more skills",
                    failures,
                )
        for retired_cli_instruction in (
            "install-legalcode-cli.sh",
            "npm install -g legalcode",
            "CLI install helper",
        ):
            require(
                retired_cli_instruction not in root_readme,
                f"README.md must not advertise {retired_cli_instruction}",
                failures,
            )
        validate_skills(skill_directories, failures)

        core_skill_roots = [
            REPO_ROOT / "plugins" / bundle.name / "skills" for bundle in BUNDLES
        ] + [REPO_ROOT / "plugins" / "legalcode-openai" / "skills"]
        forbidden_core_patterns = {
            "provider-specific model or client instruction": r"\b(?:Claude|Codex|Sonnet|Opus|Haiku)\b",
            "shell or CLI requirement": r"(?:allowed-tools:|claude -p|Bash\(|\bCLI\b|\bPandoc\b|\bOCR\b|\bpython\b)",
            "checkout or sales link": r"https?://[^\s)]+(?:checkout|pricing|subscribe|upgrade)",
        }
        for root in core_skill_roots:
            for markdown_path in root.rglob("*.md"):
                content = markdown_path.read_text(encoding="utf-8")
                for label, pattern in forbidden_core_patterns.items():
                    require(
                        re.search(pattern, content, re.IGNORECASE) is None,
                        f"{markdown_path.relative_to(REPO_ROOT)} contains a {label}",
                        failures,
                    )
    except (
        Exception
    ) as error:  # Surface malformed files and unavailable schemas clearly.
        failures.append(str(error))

    if failures:
        print("Agent Plugins conformance failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(
        f"Agent Plugins conformance passed: {len(BUNDLES) + 1} bundles, "
        f"{(len(BUNDLES) + 1) * len(EXPECTED_SKILLS)} bundled skills, "
        f"{len(ADDITIONAL_SKILLS)} additional skills."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
