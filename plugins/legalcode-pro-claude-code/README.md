# Legalcode Pro Claude Code Plugin

Pro Legalcode plugin bundle for Claude Code.

Includes:

- Pro Legalcode MCP endpoint: `https://mcppro.legalcode.md/mcp`
- 13 Legalcode skills for setup, public/pro search, contract review, privacy, legal research, litigation chronology, tabular review, **private Business Legal Radar monitoring**, **Icelandic gold-plating (gullhúðun) analysis**, and **DOCX rendering**

This directory is an Agent Plugins v1.0.0 package. Portable clients load `plugin.json`, `skills/`, and `mcp.json`; Claude Code continues to load `.claude-plugin/plugin.json` and `.mcp.json`. Authentication is client-managed and is not stored in either MCP configuration file.

## Skills

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
11. `business-legal-radar-private-agent-watch` — Privacy-first local legal radar monitoring with client-owned watch state and Codex/Claude Code automation
12. `legalcode-anti-gold-plating-is` — Icelandic gold-plating analysis for EEA-implementation acts; produces a _Gullhúðunarskýrsla_ and optional remediation _breytingafrumvarp_ as Word documents
13. `legalcode-docx-render` — Companion DOCX renderer with Icelandic legal typography and table-border post-processing

Install from the marketplace:

```text
/plugin marketplace add RobertHH-IS/legalcode-plugin
/plugin install legalcode-pro-claude-code@legalcode
```
