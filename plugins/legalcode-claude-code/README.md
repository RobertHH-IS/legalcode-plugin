# Legalcode Claude Code Plugin

Free Legalcode plugin bundle for Claude Code.

Includes:

- public Legalcode MCP endpoint: `https://mcp.legalcode.md/mcp`
- 13 Legalcode skills for setup, public search, contract review, privacy, legal research, litigation chronology, tabular review, private Business Legal Radar monitoring, Icelandic gold-plating analysis, and DOCX rendering

This directory is an Agent Plugins v1.0.0 package. Portable clients load `plugin.json`, `skills/`, and `mcp.json`; Claude Code continues to load `.claude-plugin/plugin.json` and `.mcp.json`. Authentication is client-managed and is not stored in either MCP configuration file.

Install from the marketplace after this repo is public:

```text
/plugin marketplace add RobertHH-IS/legalcode-plugin
/plugin install legalcode-claude-code@legalcode
```

Use Pro when you need guidance, agreements, stronger search, more results per query, downloads, or CLI workflows.
