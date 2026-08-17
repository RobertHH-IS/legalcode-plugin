---
name: business-legal-radar-private-agent-watch
description: >
  Privacy-first Business Legal Radar workflow for interviewing a user, discovering current
  Legalcode coverage, drafting local watch targets, creating local watchbook/state files, and
  setting up Codex or Claude Code recurring automations without storing watch logic in Legalcode.
---

# Business Legal Radar Private Agent Watch

Use this skill when the user wants a private, agent-owned legal or regulatory monitoring workflow
instead of hosted Legalcode watches.

Legalcode is the legal data, search, fetch, trace, and diff substrate. The user's AI agent owns the
Business Profile, watch strategy, targets, aliases, schedule, cursor state, reports, and reasoning.

Do not call `legalcode_watch` by default. Do not store the watch on Legalcode. Do not send the
Business Profile, contracts, policies, customer lists, internal memos, secrets, local reports, local
watch state, or chain-of-thought to Legalcode. Send Legalcode only specific ordinary MCP requests
needed for the current run, such as discovery, search, fetch, trace, and diff requests.

Hosted MCP Pro watches are available only when the user explicitly asks to convert selected local
targets into hosted `legalcode_watch` targets.

## Setup Workflow

1. Explain the privacy model: the watch, target list, cursor, schedule, and reports stay local; the
   automation calls Legalcode only for source-backed data; exact watched names, aliases, targets,
   cadence, and noise settings require user approval.
2. Interview the user for business activities, products, jurisdictions, regulated activities,
   customer/data/payment/HR/public-sector exposure, known laws, legalBasisKeys, sourceRefs,
   regulators, courts, competitors, patents, pre-law topics, and delivery preference.
3. Discover Legalcode coverage dynamically. Do not hard-code jurisdictions, source families,
   sources, facets, stages, actor names, or filter values. Check available jurisdictions, source
   profiles, facets, facet values, and whether requested surfaces expose stable sourceRefs, cursors,
   dates, or metadata.
4. Draft local watch bundles grouped by business issue, such as `AI hiring`, `payment services`,
   `company-name mentions`, `EU/EEA transposition`, or `consultation deadlines`.
5. Show a draft target table and ask for approval before creating files or automation.

## Local Watch Kinds

Support these local watch patterns:

- `saved_search_watch`: rerun a Legalcode search and detect new or removed sourceRefs.
- `law_key_watch`: fetch or diff a known lawKey/sourceRef/legalBasisKey.
- `field_change_watch`: track selected source-specific fields.
- `milestone_watch`: track pre-law or regulatory process stages.
- `deadline_watch`: track consultation, filing, effective, implementation, or review windows.
- `entity_mention_watch`: detect approved company, person, product, competitor, or alias mentions.
- `actor_watch`: track a regulator, ministry, committee, court, agency, stakeholder, or legislator.
- `guidance_watch`: detect new or changed guidance matching discovered filters.
- `related_item_watch`: track new items connected to a lawKey, legalBasisKey, sourceRef, flowKey,
  CELEX, EEA status, or transposition edge.
- `high_volume_count_watch`: track aggregate count deltas for submissions, comments, or feedback
  without listing every item.

Prefer deterministic identifiers over broad text: lawKey, sourceRef, legalBasisKey, CELEX, flowKey,
case id, official source id, discovered source-specific facets, and exact user-approved aliases.
Use saved search queries only when no stable identifier exists. Mark unsupported targets
`preview_only` or `coverage_gap`.

## Approval Table

Before setup, show:

| Bundle | Kind | Jurisdiction | Source type | Target/query | Trigger | Cadence | Status |
| ------ | ---- | ------------ | ----------- | ------------ | ------- | ------- | ------ |

Include discovery evidence, exact aliases, noise controls, coverage gaps, cadence, and timezone.

## Local Watch Workspace

After approval, create:

```text
.legalcode/private-watches/{watch-slug}/
  WATCH.md
  targets.json
  state.json
  reports/
```

`targets.json` contains only approved focused targets, not the full Business Profile. Use this
shape:

```json
{
  "watchSlug": "ai-hr-eu-iceland",
  "watchName": "AI HR EU/Iceland legal radar",
  "createdAt": "ISO-8601",
  "timezone": "Europe/Reykjavik",
  "cadence": "weekly",
  "bundles": [],
  "coverageGaps": []
}
```

`state.json` starts as:

```json
{
  "lastRunAt": null,
  "runs": [],
  "cursors": {},
  "seenSourceRefs": {},
  "fieldFingerprints": {},
  "mutedKeys": [],
  "lastReportPath": null
}
```

Reports go to `reports/YYYY-MM-DD-{watch-slug}.md`.

## Automation Setup

For Codex, use the native automation tool when available. Prefer a reviewable/suggested cron
automation when local environment setup is involved. Do not hand-write raw automation directives.

For Claude Code, create or suggest the equivalent schedule workflow using the local project's
schedule conventions. If Claude Code cannot create the schedule directly, return the exact schedule
command or prompt for user approval.

The automation prompt must be self-contained:

- load local `targets.json` and `state.json`;
- run ordinary Legalcode discovery/search/fetch/trace/diff calls for each target;
- compare sourceRefs, field fingerprints, counts, deadlines, milestones, and relation edges against
  local state;
- write a concise Markdown report with top changes, grouped counts, suppressed/noisy counts,
  deadline strip, sourceRefs, coverage gaps, and a paste-ready follow-up prompt;
- update `state.json` only after the report is written;
- do not call `legalcode_watch` unless the user explicitly asks to convert to hosted MCP Pro watch.

## Recurring Run Workflow

Each run should read local targets/state, execute target checks, normalize by stable keys, detect
new sourceRefs, changed fields, milestone transitions, deadline windows, entity mentions,
related/transposition edges, count thresholds, and coverage gaps, suppress duplicates/noise, write a
compact source-backed report, and update local state only after successful report generation.

If no material changes are found, write a short no-change receipt only when the user enabled
no-change reports. Otherwise update state quietly.

## Required Setup Output

End setup with the approved watch bundle table, local file paths created, automation name and
cadence, automation prompt or schedule command, first-run command or next scheduled run, coverage
gaps and preview-only targets, and a reminder that Legalcode stores none of the private watch state
in this workflow.
