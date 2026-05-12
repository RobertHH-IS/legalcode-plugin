# Legalcode Pro Claude Code Plugin

Pro Legalcode plugin bundle for Claude Code.

Includes:

- Pro Legalcode MCP endpoint: `https://mcppro.legalcode.md/mcp`
- 10 Legalcode skills for setup, public/pro search, contract review, privacy, legal research, litigation chronology, and tabular review
- CLI install helper at `scripts/install-legalcode-cli.sh`

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
