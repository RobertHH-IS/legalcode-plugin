---
name: legalcode-public-search
description: >
  Research primary legal materials with Legalcode using Discover, Search, Fetch,
  Analyze, and Trace. Use for laws, cases, guidance, agreements, legislative
  history, patents, citations, implementation links, and source verification.
---

# Legalcode Primary-Source Search

Use the hosted Legalcode MCP at https://mcp.legalcode.md/mcp through the connected account.

## Workflow

1. Frame the jurisdiction, source family, issue, date or version, and requested output.
2. Call legalcode_discover when fields, facets, source codes, analytics, or trace coverage are not confirmed.
3. Call legalcode_search with explicit filters. Keep free text in q; never convert it silently into a structured filter.
4. Copy returned sourceRef values exactly.
5. Call legalcode_fetch for metadata, provisions, excerpts, or paginated text.
6. Use legalcode_trace only for deterministic indexed relationships.
7. Use legalcode_analyze only for capabilities confirmed by Discover, then verify examples through Search and Fetch.

Prefer primary materials and official publisher URLs. Preserve citations, sourceRef, applied filters, version status, and uncertainty. Distinguish no match from unsupported or incomplete coverage. Never invent a sourceRef, citation, field, sourceCode, or relationship. If a capability returns subscription_required, explain the limitation neutrally and continue with available evidence. Do not provide purchase or upgrade directions.

Legalcode researches sources. It does not file documents, communicate with third parties, or take legal action.
