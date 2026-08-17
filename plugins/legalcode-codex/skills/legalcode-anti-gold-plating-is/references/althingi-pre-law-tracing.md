# Alþingi pre-law tracing with the current Legalcode MCP contract

Use this reference to retrieve Icelandic legislative history for an enacted act. The
Legalcode MCP endpoint is `https://mcppro.legalcode.md/mcp` and requires OAuth.

## Tool surface

Legalcode advertises exactly five tools:

- `legalcode_discover`
- `legalcode_search`
- `legalcode_fetch`
- `legalcode_analyze`
- `legalcode_trace`

Do not invent source-specific tool names. Search accepts one `jurisdiction` string and a
`sourceTypes` array.

## 1. Discover the live pre-law profile

```json
{
  "jurisdiction": "IS",
  "mode": "source_profile",
  "sourceType": "pre_law"
}
```

Then inspect facets before applying document-role, submitter, or status filters:

```json
{
  "jurisdiction": "IS",
  "mode": "facets",
  "sourceType": "pre_law"
}
```

Use `mode: "facet_values"` with the exact facet key returned by discovery when you need
stored values. Do not guess role or submitter values.

## 2. Resolve the enacted law

For a known Icelandic act number, use exact mode with a structured `lawKey` filter:

```json
{
  "jurisdiction": "IS",
  "mode": "exact",
  "sourceTypes": ["law"],
  "filters": [
    { "field": "lawKey", "op": "eq", "value": "90/2018" }
  ],
  "page": { "limit": 5 }
}
```

Record the canonical `lawKey` and `sourceRef` returned by Legalcode.

## 3. Trace the legislative flow

Prefer the indexed relationship over ranked text search:

```json
{
  "relationship": "pre_law_for_law",
  "jurisdiction": "IS",
  "lawKey": "IS|LAW|90/2018"
}
```

Record the returned `flowKey`. If the canonical law key is unavailable, discovery may
show that `relatedNumberYear` is supported for the pre-law corpus; apply it only as an
explicit filter after confirming the live profile.

## 4. Enumerate every attached document

```json
{
  "jurisdiction": "IS",
  "sourceTypes": ["pre_law"],
  "resultLevel": "document",
  "filters": [
    { "field": "flowKey", "op": "eq", "value": "<flowKey>" }
  ],
  "page": { "limit": 20 }
}
```

Follow `nextCursor` until `hasMore` is false. Keep every returned `sourceRef`, role,
sender or submitter, document number, date, format, and download URL. The full inventory
is required before claiming that the legislative record is complete.

Typical materials include the original bill and greinargerð, committee reports,
amendment proposals, submitted opinions, parliamentary documents, summaries, and the
final enacted text. Use the exact role values returned by discovery and results.

## 5. Narrow within the flow

Examples below assume discovery confirmed the fields and values.

Original bill:

```json
{
  "jurisdiction": "IS",
  "sourceTypes": ["pre_law"],
  "resultLevel": "document",
  "filters": [
    { "field": "flowKey", "op": "eq", "value": "<flowKey>" },
    { "field": "role", "op": "eq", "value": "ORIGINAL_BILL" }
  ]
}
```

Submitted opinions mentioning a phrase:

```json
{
  "jurisdiction": "IS",
  "sourceTypes": ["pre_law"],
  "resultLevel": "document",
  "filters": [
    { "field": "flowKey", "op": "eq", "value": "<flowKey>" },
    { "field": "role", "op": "eq", "value": "SUBMITTED_OPINION" },
    { "field": "documentText", "op": "text", "value": "umfram lágmark" }
  ],
  "page": { "limit": 20 }
}
```

Use the returned `downloadUrl` for bulk document collection. Use `legalcode_fetch` with
an exact `sourceRef` when you need metadata, a targeted excerpt or section, or paginated
full-text fallback.

## 6. Trace and fetch connected authority

- Use `legalcode_trace` with `relationship: "cases_for_law"` for decisions applying the
  enacted Icelandic law.
- Use `legalcode_search` with `jurisdiction: "EU"`, the correct `sourceTypes`, and exact
  identifier filters for the underlying EU instrument.
- Use `legalcode_trace` for supported EEA and implementation relationships after reading
  `legalcode_discover({ "mode": "help" })`.
- Use `legalcode_search` with `sourceTypes: ["guidance"]` only after discovery confirms
  the owning jurisdiction and source profile for ESA or other guidance.

## 7. Coverage and provenance

For every item, record:

- exact title and document role
- `sourceRef`, `flowKey`, and law key where present
- issuing body or submitter
- source date
- retrieval time
- direct source URL or Legalcode download URL
- whether content was fetched through Legalcode or a documented residual web fallback

If a document expected from the Alþingi matter page is absent, log the gap explicitly and
use the official Alþingi or Samráðsgátt page as a residual fallback. Never describe a
partial first page as the complete legislative record.
