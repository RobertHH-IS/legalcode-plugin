# Legalcode Plugins

Public plugin distribution for Legalcode.

Legalcode gives AI agents primary legal source lookup and reusable legal workflows. This repository ships free and Pro plugin bundles for Codex and Claude Code.

Website: https://legalcode.md

## Plugins

| Plugin | Target | MCP endpoint | Skills | CLI |
|---|---|---|---:|---|
| `legalcode-codex` | Codex | Public MCP | 10 | No |
| `legalcode-claude-code` | Claude Code | Public MCP | 10 | No |
| `legalcode-pro-codex` | Codex | Pro MCP | 10 | Install helper |
| `legalcode-pro-claude-code` | Claude Code | Pro MCP | 10 | Install helper |

## Included Free Skills

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

Each skill explains when to use public MCP and when to use Pro MCP.

## Public vs Pro

Public MCP:

```text
https://mcp.legalcode.md/mcp
```

Use public MCP for anonymous laws and case law lookup. It is rate limited and returns the top 5 results per query.

Pro MCP:

```text
https://mcppro.legalcode.md/mcp
```

Use Pro MCP for stronger search, AND/OR search, up to 20 results per query, guidance, agreements, downloads, and authenticated higher-throughput access.

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

## Pro CLI Helper

The Pro plugins include:

```text
scripts/install-legalcode-cli.sh
```

That helper runs:

```bash
npm install -g legalcode
```

The npm package must be published separately before this command works for external users.

## Notes

Your agent keeps your documents and matter context. Legalcode provides source lookup through MCP.
