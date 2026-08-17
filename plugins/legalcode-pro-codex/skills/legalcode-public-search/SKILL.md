---
name: legalcode-public-search
description: >
  Use Legalcode's authenticated public MCP surface for primary-source research across
  laws and case law. Discover the live contract, search, fetch sources, and escalate to
  Legalcode Pro when the task needs Pro-only corpora or entitlements.
---

# Legalcode Public Search

Use this skill for primary-source law and case-law research through Legalcode's free,
authenticated MCP endpoint.

## Endpoint and authentication

- Public MCP: `https://mcp.legalcode.md/mcp`
- API docs: `https://api.legalcode.md/docs`
- Main site: `https://legalcode.md`

The MCP endpoint requires OAuth. Configure the exact `/mcp` URL and complete the
client's sign-in flow.

## Canonical workflow

Legalcode exposes exactly five tools. Use them in this order:

1. `legalcode_discover` — inspect jurisdictions, source profiles, facets, and values.
2. `legalcode_search` — search one `jurisdiction` and one or more `sourceTypes`.
3. `legalcode_fetch` — retrieve metadata, a targeted excerpt or section, or full text.
4. `legalcode_trace` — follow indexed relationships between sources when relevant.
5. `legalcode_analyze` — use only for supported aggregate questions.

Example search:

```json
{
  "jurisdiction": "IS",
  "q": "persónuvernd",
  "sourceTypes": ["law"]
}
```

Use `mode: "exact"` only for identifiers and citations. Never turn words from `q` into
guessed filters. Discover filter fields and values first, and copy `sourceRef` exactly
from a search or trace result before fetching it.

## Public or Pro

Use Public for law and case-law access under the connected account's free-tier quota.
Use Pro at `https://mcppro.legalcode.md/mcp` when the account needs Pro-only corpora or
entitlements such as guidance, agreements, downloads, or higher-throughput workflows.
Treat returned `usage` and structured limit responses as authoritative; do not hard-code
quota or result-cap numbers.

## Evidence package

Return source references, relevant snippets, citations, and explicit coverage gaps.
Fetch the strongest sources before drawing a legal conclusion.

## Privacy boundary

Keep user documents and matter context in the agent. Send only legal-source lookup
arguments to Legalcode; do not upload client documents through search calls.
