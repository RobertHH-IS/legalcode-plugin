# Legalcode Plugins

Public plugin distribution for Legalcode.

Legalcode gives AI agents primary legal source lookup and reusable legal workflows. This repository ships free and Pro plugin bundles for Codex and Claude Code.

Website: https://legalcode.md

## Plugins

| Plugin | Target | MCP endpoint | Skills | CLI |
|---|---|---|---:|---|
| `legalcode-codex` | Codex | Public MCP | 10 | No |
| `legalcode-claude-code` | Claude Code | Public MCP | 10 | No |
| `legalcode-pro-codex` | Codex | Pro MCP | 12 | Install helper |
| `legalcode-pro-claude-code` | Claude Code | Pro MCP | 12 | Install helper |

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

## Additional Pro Skills

Pro plugins ship the 10 free skills above plus these two Pro-only skills that depend on the Pro MCP's pre-law trace and case-law-by-law trace surfaces:

11. `legalcode-anti-gold-plating-is` — Icelandic gold-plating (gullhúðun) analysis for EEA-implementation acts. Section-by-section detection of *innleiðing umfram lágmark*, traced through the Alþingi pre-law record (frumvarp, greinargerð, umsagnir, nefndarálit, breytingartillögur), with per-finding impact retrieval via targeted MCP searches. Applies the Davidson Five + Pattern G30 framework, runs Iron Law 7 counter-argument stress tests on every HIGH/CRITICAL finding, and produces a full *Gullhúðunarskýrsla* plus an optional remediation *breytingafrumvarp* — both rendered as standalone Word documents.
12. `legalcode-docx-render` — Self-contained DOCX renderer with Icelandic legal typography (Arial 10pt body, sized headings, 1-inch margins), thin horizontal borders between table rows, and a mandatory standalone-document audit so the output opens in Word, LibreOffice, or Pages with zero update prompts. Pandoc-backed with a post-render Python helper for table-border injection. Acts as the rendering back end for `legalcode-anti-gold-plating-is` but works as a general-purpose Icelandic-legal DOCX renderer for any markdown source.

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
