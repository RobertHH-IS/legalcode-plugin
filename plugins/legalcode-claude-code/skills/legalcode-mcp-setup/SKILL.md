---
name: legalcode-mcp-setup
description: >
  Connect Legalcode MCP to an AI agent and choose the correct authenticated endpoint.
  Use when setting up Legalcode in Claude, Claude Code, ChatGPT, Codex, Cursor,
  Windsurf, or another MCP-compatible client, or when repairing stale connector tools.
---

# Legalcode MCP Setup

Use this skill to connect an agent to Legalcode or repair an existing connection.

## Exact endpoints

Public:

```text
https://mcp.legalcode.md/mcp
```

Pro:

```text
https://mcppro.legalcode.md/mcp
```

Both endpoints require the client to complete OAuth. Do not configure the hostname root;
the Streamable HTTP endpoint is `/mcp`.

## Current tool contract

Legalcode advertises exactly five tools:

- `legalcode_discover` — jurisdictions, source profiles, facets, query syntax, and help
- `legalcode_search` — ranked or exact source search
- `legalcode_fetch` — metadata, excerpts, sections, and full-document fallback
- `legalcode_analyze` — aggregate analysis
- `legalcode_trace` — indexed relationships between laws, cases, and pre-law material

Never invent a source-specific tool name. Start with
`legalcode_discover({ mode: "jurisdictions" })`, then use the exact fields and values
returned by discovery. Search accepts one `jurisdiction` string and a `sourceTypes`
array.

## Public or Pro

Use Public for authenticated free-tier law and case-law research. Use Pro when the
account needs the Pro corpus or entitlements, including guidance, agreements, downloads,
and higher-throughput workflows. Treat returned `usage` and structured limit responses
as authoritative; do not hard-code quota numbers in agent instructions.

## Setup flow

1. Open the client's plugin, connector, or MCP settings.
2. Add Legalcode as a remote Streamable HTTP MCP server using the exact `/mcp` URL.
3. Complete OAuth when prompted.
4. Start a new chat so the client loads the current tool catalog.
5. Call `legalcode_discover({ mode: "jurisdictions" })` to verify the connection.

## Repair stale ChatGPT connector tools

If ChatGPT reports `Tool ... not found` and names a tool other than the five listed
above, its installed plugin or connector catalog is stale:

1. Update or reinstall the Legalcode plugin from its current GitHub source.
2. Remove and reconnect the Legalcode connector if its tool catalog is still stale.
3. Complete OAuth again if requested.
4. Test in a new chat with `legalcode_discover({ mode: "jurisdictions" })`.

Do not work around a stale catalog by guessing tool names.

## Privacy boundary

The agent keeps user documents and matter context. Send only legal-source lookup
arguments to Legalcode; do not upload client documents through search calls.

## Links

- Legalcode: https://legalcode.md
- Install docs: https://legalcode.md/docs/install
- Public MCP: https://mcp.legalcode.md/mcp
- Pro MCP: https://mcppro.legalcode.md/mcp
- More Legalcode skills: https://github.com/RobertHH-IS/legalcode-plugin/tree/main/more-skills
