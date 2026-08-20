# Legalcode OpenAI Plugin

This repository contains the submission package for the Legalcode OpenAI plugin.

Legalcode gives OpenAI products authenticated access to primary legal sources through the hosted
MCP endpoint:

```text
https://mcp.legalcode.md/mcp
```

## Submission package

The uploadable package is [`plugins/legalcode-openai`](plugins/legalcode-openai). It contains:

- the OpenAI plugin manifest;
- Legalcode brand assets and notices; and
- one provider-neutral skill: `legalcode-mcp-guide`.

The package deliberately contains no CLI, local MCP server, scripts, hooks, custom app, or
client-specific Claude/Codex bundles. Specialized legal workflow skills are maintained and
distributed separately so users can add only the workflows they need.

The hosted MCP connection is declared in the package's `.mcp.json` and entered again in the OpenAI
submission portal. Reviewer credentials remain only in the portal's private fields.
[`chatgpt-app-submission.json`](chatgpt-app-submission.json) is the checked-in worksheet for the
listing, tool annotations, and submission test cases.

## Validate

Run the pinned Python 3.11+ validation environment with `uv`:

```bash
uv run --python 3.13 --with-requirements requirements-dev.txt \
  python scripts/validate_openai_submission.py
```

The validator checks the exact one-skill inventory, MCP dependency metadata, package boundaries,
manifest assets, routing cases, and submission worksheet.
