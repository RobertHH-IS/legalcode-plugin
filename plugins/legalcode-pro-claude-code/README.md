# Legalcode Pro Claude Code Plugin

Pro Legalcode plugin bundle for Claude Code.

Includes:

- Pro Legalcode MCP endpoint: `https://mcppro.legalcode.md/mcp`
- 12 Legalcode skills for setup, public/pro search, contract review, privacy, legal research, litigation chronology, tabular review, **Icelandic gold-plating (gullhúðun) analysis**, and **DOCX rendering**
- CLI install helper at `scripts/install-legalcode-cli.sh`

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
11. `legalcode-anti-gold-plating-is` — Icelandic gold-plating analysis for EEA-implementation acts; produces a *Gullhúðunarskýrsla* and optional remediation *breytingafrumvarp* as Word documents
12. `legalcode-docx-render` — Companion DOCX renderer with Icelandic legal typography and table-border post-processing

Install from the marketplace after this repo is public:

```text
/plugin marketplace add RobertHH-IS/legalcode-plugin
/plugin install legalcode-pro-claude-code@legalcode
```

The CLI helper runs:

```bash
npm install -g legalcode
```

The npm package must be published separately before external users can install the CLI from npm.
