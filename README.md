# Legalcode Plugins

Public plugin distribution for Legalcode.

Legalcode gives AI agents primary legal source lookup and reusable legal workflows. This repository ships free and Pro plugin bundles for Codex and Claude Code.

Website: https://legalcode.md

## Plugins

| Plugin                      | Target      | MCP endpoint | Skills |
| --------------------------- | ----------- | ------------ | -----: |
| `legalcode-codex`           | Codex       | Public MCP   |     13 |
| `legalcode-claude-code`     | Claude Code | Public MCP   |     13 |
| `legalcode-pro-codex`       | Codex       | Pro MCP      |     13 |
| `legalcode-pro-claude-code` | Claude Code | Pro MCP      |     13 |

## Included Skills

1. `legalcode-mcp-setup`
2. `legalcode-public-search`
3. `legalcode-contract-review`
4. `legalcode-nda-triage`
5. `legalcode-dpia-generator`
6. `legalcode-document-qa`
7. `legalcode-legal-memorandum`
8. `legalcode-statute-analysis`
9. `legalcode-case-timeline-builder`
10. `legalcode-tabular-review`
11. `business-legal-radar-private-agent-watch`
12. `legalcode-anti-gold-plating-is` — Icelandic gold-plating (gullhúðun) analysis for EEA-implementation acts. Section-by-section detection of _innleiðing umfram lágmark_, traced through the Alþingi pre-law record (frumvarp, greinargerð, umsagnir, nefndarálit, breytingartillögur), with per-finding impact retrieval via targeted MCP searches. Applies the Davidson Five + Pattern G30 framework, runs Iron Law 7 counter-argument stress tests on every HIGH/CRITICAL finding, and produces a full _Gullhúðunarskýrsla_ plus an optional remediation _breytingafrumvarp_ — both rendered as standalone Word documents.
13. `legalcode-docx-render` — Self-contained DOCX renderer with Icelandic legal typography (Arial 10pt body, sized headings, 1-inch margins), thin horizontal borders between table rows, and a mandatory standalone-document audit so the output opens in Word, LibreOffice, or Pages with zero update prompts. Pandoc-backed with a post-render Python helper for table-border injection. Acts as the rendering back end for `legalcode-anti-gold-plating-is` but works as a general-purpose Icelandic-legal DOCX renderer for any markdown source.

All four bundles ship the same skill tree. Each skill explains when its workflow requires Pro MCP capabilities; the bundles differ by target client and MCP endpoint.

## Agent Plugins v1

Every bundle implements the portable [Agent Plugins v1.0.0](https://agent-plugins.org/specification) package layout:

- `plugin.json` declares portable identity and metadata.
- `skills/*/SKILL.md` contains Agent Skills.
- `mcp.json` declares the hosted Streamable HTTP MCP server.

The existing `.codex-plugin/plugin.json`, `.claude-plugin/plugin.json`, and `.mcp.json` files remain in place for client-specific and legacy loading. Agent Plugins v1 does not define portable OAuth fields, so authentication is completed by the client rather than embedded in `mcp.json`.

## Public vs Pro

Public MCP:

```text
https://mcp.legalcode.md/mcp
```

Use public MCP for public-tier legal research. The host currently requires client-managed OAuth and applies the connected account's access and quota policy.

Pro MCP:

```text
https://mcppro.legalcode.md/mcp
```

Use Pro MCP for stronger search, guidance, agreements, downloads, and higher-throughput access. It also requires client-managed OAuth.

## Codex Install

Codex uses the repo-local marketplace manifest:

```text
.agents/plugins/marketplace.json
```

Free plugin path:

```text
./plugins/legalcode-codex
```

Pro plugin path:

```text
./plugins/legalcode-pro-codex
```

## Claude Code Install

```text
/plugin marketplace add RobertHH-IS/legalcode-plugin
/plugin install legalcode-claude-code@legalcode
```

For Pro:

```text
/plugin install legalcode-pro-claude-code@legalcode
```

## Conformance

Run the pinned Python 3.11+ validation environment with `uv`:

```bash
uv run --python 3.13 --with-requirements requirements-dev.txt \
  python scripts/validate_agent_plugins.py
```

Alternatively, install `requirements-dev.txt` into any Python 3.11+ virtual environment and run `python scripts/validate_agent_plugins.py`.

## Notes

Your agent keeps your documents and matter context. Legalcode provides source lookup through MCP.
