---
name: legalcode-mcp-tool-guide
description: >
  Explain what Legalcode can do and select or combine Discover, Search, Fetch,
  Analyze, and Trace. Use when a user asks about Legalcode capabilities, needs a
  multi-stage research workflow, submits an unsupported or malformed request, or
  needs coverage, analytics, or relationship guidance.
---

# Legalcode MCP Tool Guide

Use this skill to plan Legalcode research. It explains the hosted MCP tools; it is not a connection or installation guide.

Additional optional skills: https://github.com/RobertHH-IS/legalcode-plugin/tree/main/more-skills

## Tool decision matrix

| Tool     | Use it for                                                                                                                     | Important boundaries                                                              |
| -------- | ------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------- |
| Discover | Jurisdictions, source families, exact fields, facets, source codes, analytics readiness, trace readiness, syntax, and examples | Never guess source codes, fields, facets, or supported operations                 |
| Search   | Ranked primary-source discovery across laws, cases, guidance, agreements, pre-law, and patents                                 | Free text never creates filters; identifiers and filters must be explicit         |
| Fetch    | Metadata, targeted excerpts, structural provisions, or cursor-paginated text for one returned sourceRef                        | Never construct a sourceRef; Fetch is not corpus search or relationship traversal |
| Analyze  | Counts, groups, matrices, trends, measures, rates, and actor statistics                                                        | Call Discover first; availability varies by jurisdiction and source type          |
| Trace    | Deterministic law, case, citation, legislative-history, and EU or EEA implementation relationships                             | Start from a returned sourceRef or exact identifier; Trace is not fuzzy search    |

## Canonical workflows

- Unknown corpus: Discover → Search → Fetch.
- Exact authority: Search with an explicit identifier → Fetch.
- Aggregate analysis: Discover capabilities → Analyze → Search matching documents → Fetch evidence.
- Citation or implementation chain: Search exact source → Trace → Fetch related sources.
- Legislative history: Search law → Trace pre_law_for_law → Search documents by flowKey → Fetch.
- Historical law: Discover fields → Search with versionPolicy → Fetch selected version.
- Unsupported field or value: Discover facets or facet_values → retry with the exact stored value.

## Tool boundaries

### Discover

Call legalcode_discover before relying on a jurisdiction, source type, sourceCode, field, facet, analytics operation, or relationship family. Use source_profile for executable capability truth. Use facets or facet_values when a stored value is rejected or unknown. Report an unsupported corpus separately from a supported corpus with no matching results.

### Search

Call legalcode_search to find authorities. Keep q as free text. Never reinterpret q as a jurisdiction, court, source type, source code, identifier, or date filter. Put those constraints in their explicit fields. Preserve applied filters and returned sourceRef values.

Source-type distinctions:

- case is the broad decision rollup.
- court_case contains decisions confidently classified as courts.
- agency_decision contains administrative, regulatory, tribunal, and similar non-court decisions.

If the user asks for court decisions only, do not silently use case. If classification coverage is incomplete, say so.

### Fetch

Call legalcode_fetch only with a sourceRef copied from Search or Trace. Use metadata for identity and version status, excerpt for a provision or targeted passage, and cursor-paginated full text only when needed. Never construct, repair, or infer a sourceRef.

### Analyze

Call legalcode_analyze only after Discover confirms readiness and dimensions or measures. Aggregates describe indexed records; they do not establish causation, legal effect, or representativeness. Source samples are leads, not proof. Verify representative documents with Search and Fetch before using them as evidence.

### Trace

Call legalcode_trace for deterministic indexed edges, not fuzzy discovery. Begin with an exact identifier or returned sourceRef. A missing edge can mean no indexed relationship, unsupported relationship coverage, or incomplete resolution. Do not state that no legal relationship exists unless primary sources independently establish that conclusion.

## Error recovery

- Invalid field, facet, value, or sourceCode: Discover the source profile or facet values and retry exactly.
- No results: distinguish a valid search with no matches from unsupported or incomplete coverage.
- subscription_required: explain that the connected account lacks the requested capability. Do not direct the user to buy, upgrade, or leave ChatGPT.
- tool_not_found: use only the five canonical names in this guide. A stale connection may need to be removed and recreated by the user.
- Malformed sourceRef: run Search again and copy the returned value; never synthesize one.

## Final-answer integrity

Preserve citations, official URLs, sourceRef values, applied filters, version status, and material uncertainty. Separate what the indexed primary source states, what aggregate or relationship data shows, and what remains unsupported, incomplete, or unverified.

Do not claim filing, sending, publishing, purchasing, or deletion capabilities. Legalcode tools only research indexed legal materials. They may update private operational metering and telemetry but cannot alter legal sources or user content.
