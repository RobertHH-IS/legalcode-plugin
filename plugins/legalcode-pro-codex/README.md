# Legalcode Pro Codex Plugin

Pro Legalcode plugin bundle for Codex.

Includes:

- Pro Legalcode MCP endpoint: `https://mcppro.legalcode.md/mcp`
- 10 core Legalcode skills for MCP tool selection, primary-source search, contract review, privacy, legal research, litigation chronology, and tabular review

This directory is an Agent Plugins v1.0.0 package. Portable clients load `plugin.json`, `skills/`, and `mcp.json`; Codex continues to use `.codex-plugin/plugin.json` for presentation metadata. Authentication is client-managed and is not stored in either MCP configuration file.

## Skills

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

Find additional Legalcode skills at https://github.com/RobertHH-IS/legalcode-plugin/tree/main/more-skills.
