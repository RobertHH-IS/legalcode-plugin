---
name: legalcode-mcp-guide
description: >
  Coordinate Legalcode's Discover, Search, Fetch, Analyze, and Trace tools for
  primary-source research. Use for capability questions, current source
  discovery, multi-tool research, aggregate analysis, relationship tracing,
  verified source text, or recovery from a rejected Legalcode call. Not for
  connection or installation setup.
---

# Legalcode MCP Guide

Use the connected schemas and the current `legalcode_discover` response as the contract for
parameters, fields, values, limits, and readiness. This guide adds only the cross-tool workflow and
handoffs that individual tool descriptions cannot express.

## Tool roles

| Tool | Purpose | What it hands to the next tool |
| --- | --- | --- |
| `legalcode_discover` | Learn the current shape of a jurisdiction and source family | searchable and filterable fields, facets, source codes, sorts, analytics readiness, and relationship coverage |
| `legalcode_search` | Find and rank candidate records | `sourceRef`, citation metadata, official URLs, snippets, and sometimes `downloadUrl` |
| `legalcode_fetch` | Verify one known record or provision | source metadata and the text needed to support a conclusion |
| `legalcode_analyze` | Count or group a defined indexed cohort | buckets, measures, and document handles when that profile permits them |
| `legalcode_trace` | Follow a persisted legal relationship | related-record handles and, for legislative history, flow handles |

Search discovers records; Fetch verifies their text; Analyze measures a cohort; Trace follows known
edges. Do not use Search-result counts as analytics or Trace edges as a substitute for reading the
underlying source.

## Discover the shape first

For each new jurisdiction and source family in a research task, call Discover `source_profile`
before the first Search, Analyze, or Trace. It establishes what the current corpus actually
supports. Use `facet_values` when an exact stored filter value is needed. Never guess a
`sourceCode`, field, facet value, analytics dimension, measure, or relationship capability.

Reuse a current profile already present in the conversation; do not repeat Discover for every call
within the same scope. Fetching a returned `sourceRef` and continuing a cursor-paginated call do not
need another discovery step.

## Search from most specific to least specific

1. Use an exact identifier or identifier filter when the authority is known.
2. Add structured filters advertised by Discover when the requested scope is known.
3. Use phrase mode when every meaningful term must occur together.
4. Use source-language keyword text for open-ended topic discovery.

Free text never creates jurisdiction, source-type, court, date, or other structured constraints.
Put those in explicit parameters. If a filter is rejected, correct it through Discover rather than
silently dropping it and broadening the question.

## Cross-tool handoffs

- **Candidate to evidence:** Discover → Search → Fetch. Copy the returned `sourceRef` exactly;
  never construct or decode it.
- **Aggregate to documents:** Discover → Analyze → Search → Fetch. Search the same jurisdiction,
  `q`, and every filter that Discover marks valid for Search; do not replace the analyzed cohort
  with a looser paraphrase.
- **Authority to related authorities:** Discover first. Then Search to resolve an uncertain
  authority, or pass a certain exact identifier directly to Trace. Fetch material targets. Trace
  starting inputs are relationship-specific; follow the connected schema rather than assuming one
  identifier works for every relationship.
- **Legislative history:** Discover → Search the enacted law → Trace its pre-law relationship →
  use each returned `flowKey` in a document-level pre-law Search → Fetch or download the relevant
  documents.
- **Complete text:** Prefer a returned `downloadUrl`; otherwise use Fetch full-text pagination and
  keep the source, mode, and cursor scope unchanged.
- **Cross-jurisdiction work:** repeat Discover and research separately for each jurisdiction, then
  normalize the comparison in the answer.

## Trace starting points

Trace inputs depend on the selected relationship:

| Relationship | Valid starting point |
| --- | --- |
| `cases_for_law` | `lawKey`, `legalBasisKey`, citation, or law `sourceRef` |
| `laws_for_case` | case `sourceRef` |
| `cited_cases` | case `sourceRef` |
| `citing_cases` | case `sourceRef` or citation |
| `pre_law_for_law` | `lawKey`, `legalBasisKey`, `relatedNumberYear`, or law `sourceRef` |
| `related_pre_law_flows` | `lawKey`, law `sourceRef`, `flowKey`, or EU pre-law `sourceRef` |
| `eea_incorporation_for_law` | EU `lawKey`, `legalBasisKey`, citation or CELEX, or `sourceRef` |
| `implementing_laws_for_eu_law` | the same EU identifiers plus the required national `jurisdiction` |
| `eu_law_for_implementing_law` | national `lawKey`, `legalBasisKey`, citation, or `sourceRef`; add national `jurisdiction` when it cannot be inferred |

## Evidence and reader-facing output

Search snippets identify candidates, not proof. Fetch the relevant provision or passage before
making a material legal claim. Analyze reports indexed counts under the applied scope; Trace reports
indexed relationships. Neither establishes causation, legal effect, or complete real-world
coverage, so preserve material coverage warnings.

Keep `sourceRef`, `lawKey`, `flowKey`, `sourceCode`, relationship names, metric keys, and field names
inside tool calls. In ordinary answers, use titles, legal citations, decision numbers, courts or
issuing bodies, dates, provision locators, and official URLs. Show raw machine vocabulary only when
the user explicitly asks for technical or machine-readable output.
