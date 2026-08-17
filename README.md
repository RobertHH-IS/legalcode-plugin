# Legalcode Plugins

Public plugin distribution for Legalcode.

Legalcode gives AI agents primary legal source lookup and reusable legal workflows. This repository ships OpenAI, Codex, and Claude Code plugin bundles.

Website: https://legalcode.md

## Plugins

| Plugin                      | Target      | MCP endpoint  | Skills |
| --------------------------- | ----------- | ------------- | -----: |
| `legalcode-codex`           | Codex       | Public MCP    |     10 |
| `legalcode-claude-code`     | Claude Code | Public MCP    |     10 |
| `legalcode-pro-codex`       | Codex       | Pro MCP       |     10 |
| `legalcode-pro-claude-code` | Claude Code | Pro MCP       |     10 |
| `legalcode-openai`          | OpenAI      | Universal MCP |     10 |

## Included Skills

1. `legalcode-mcp-tool-guide`
2. `legalcode-public-search`
3. `legalcode-contract-review`
4. `legalcode-nda-triage`
5. `legalcode-dpia-generator`
6. `legalcode-document-qa`
7. `legalcode-legal-memorandum`
8. `legalcode-statute-analysis`
9. `legalcode-case-timeline-builder`
10. `legalcode-tabular-review`

All five bundles ship these 10 provider-neutral core skills. The OpenAI submission package contains no MCP manifest or local executable because the universal hosted MCP endpoint is configured separately in the OpenAI submission portal.

## More Skills

Additional Legalcode skills are available in the public repository:

https://github.com/RobertHH-IS/legalcode-plugin/tree/main/more-skills

## Agent Plugins v1

The four Codex and Claude Code bundles implement the portable [Agent Plugins v1.0.0](https://agent-plugins.org/specification) package layout:

- `plugin.json` declares portable identity and metadata.
- `skills/*/SKILL.md` contains Agent Skills.
- `mcp.json` declares the hosted Streamable HTTP MCP server.

The OpenAI package keeps `plugin.json` and the ten skills but deliberately omits `mcp.json`; its universal MCP URL is submitted in the OpenAI portal. The existing `.codex-plugin/plugin.json`, `.claude-plugin/plugin.json`, and `.mcp.json` files remain in place for the other client-specific and legacy bundles.

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

## Conformance

Run the pinned Python 3.11+ validation environment with `uv`:

```bash
uv run --python 3.13 --with-requirements requirements-dev.txt \
  python scripts/validate_agent_plugins.py
```

Alternatively, install `requirements-dev.txt` into any Python 3.11+ virtual environment and run `python scripts/validate_agent_plugins.py`.

## Notes

Your agent keeps your documents and matter context. Legalcode provides source lookup through MCP.
