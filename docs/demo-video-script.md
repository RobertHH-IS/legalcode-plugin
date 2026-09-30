# Legalcode demo video script

Target length: about 4 minutes 15 seconds on web, plus two short mobile segments.
The base scene timestamps exclude the patent insert; allow provider response time.
The prompts below follow the submitted test cases and keep all record handles
inside tool calls.

## Before recording

- Fresh browser profile, 1080p or higher, no bookmarks bar, no other tabs.
- ChatGPT account with the Legalcode connection NOT yet linked (linking must be
  shown on camera).
- Reviewer-style Pro account credentials and the fixed OTP ready. Never show
  the OTP allowlist or portal fields.
- A short sample document ready to upload: a one-page memo or contract that
  cites Icelandic Act no. 90/2018 (ideally one current citation and one
  outdated or wrong one, so the verification step has something to find).
- The official published text of GDPR Article 22 open in a background tab
  (EUR-Lex) for the citation-verification side-by-side.
- Never navigate near pricing, checkout, or upgrade screens at any point.
- After each tool call, show its name briefly. Keep machine-only arguments
  collapsed and focus the frame on the human-readable answer.

## Scene list (web)

### Scene 1 — Intro (0:00–0:15)

SHOW: ChatGPT open, Legalcode visible in the apps/connectors list, not linked.
SAY: "This is Legalcode: legal research grounded in primary sources. It gives
ChatGPT six research tools over statutes, case law, guidance, agreements,
legislative history, and patents. I'll link an account, run every tool, verify
a citation against the original source, and show what Legalcode refuses to do."

### Scene 2 — Account linking (0:15–0:45)

SHOW: Click connect on Legalcode. OAuth redirect to mcp.legalcode.md. Sign in
with the reviewer account email and fixed one-time code. Consent screen with
the requested scopes. Redirect back to ChatGPT showing the linked state.
SAY: "Linking uses OAuth with dynamic client registration and PKCE. The scopes
are read-only research scopes. After consent I'm returned to ChatGPT with the
connection active."

### Scene 3 — Capability guide (0:45–1:05)

TYPE: What can Legalcode do, and what are its limits?
SHOW: The response describing the six tools and that Legalcode only reads
legal sources — it cannot file, send, purchase, or modify anything.
SAY: "The built-in tool guide explains the supported capabilities: discover,
search, fetch, patents, analyze, and trace — research only, no external actions."

### Scene 4 — Discover (1:05–1:25)

TYPE: Compare the legal source types Legalcode currently covers in Iceland, the European Union, and the United States.
SHOW: Show the `legalcode_discover` calls, then the answer comparing source
families by jurisdiction in ordinary language.
SAY: "Discover reports the current shape of each corpus before research begins,
so the model does not guess what a jurisdiction supports."

### Scene 5 — Search (1:25–1:45)

TYPE: Find GDPR (CELEX 32016R0679) and give its legal citation and official source.
SHOW: Show the `legalcode_search` call, exact instrument and official link. Reuse
that returned record in Scene 6.
SAY: "Search resolves an exact public identifier and returns a source we can verify."

### Scene 5b — Patents (separate 20–30 second insert)

TYPE: Find European patent EP4811984A1. Verify its publication identity and summarize its published claims with the source link.
SHOW: Both actions of `legalcode_patents`: exact Search and retrieval of the same
publication's available claims. Keep the publication identifier and kind code visible.
SAY: "Patents has a dedicated tool for live publication search and retrieval. It reads
the external EPO service. If source text is unavailable, the answer reports that limit."


### Scene 6 — Fetch and citation verification (1:45–2:15)

TYPE: Find GDPR (CELEX 32016R0679), retrieve Article 22, and explain when solely automated decisions are permitted, with the official source.
SHOW: Show the `legalcode_fetch` call label while keeping its machine-only
arguments collapsed. Highlight the returned Article 22 excerpt, citation, and
official link. Then switch to the EUR-Lex tab and show the
same text side by side for a few seconds.
SAY: "Fetch retrieves one targeted provision with the metadata to cite it.
The answer gives me the legal citation and official source, so I can verify
the excerpt against the published text — this is the core promise:
conclusions you can check against the primary source."

### Scene 7 — Analyze (2:15–2:40)

TYPE: Show annual counts of Icelandic Data Protection Authority decisions from 2018 through 2025, then verify the two newest decisions in that cohort.
SHOW: Expand the `legalcode_analyze` call and the eight annual buckets, then
show the matching Search and Fetch calls for the two newest decisions.
SAY: "Analyze measures a precisely defined cohort. Search and Fetch then verify
real decisions from the same scope rather than substituting a looser query."

### Scene 8 — Trace (2:40–3:00)

TYPE: Find the original bill behind Icelandic Act no. 90/2018, list five submitted opinions, and briefly summarize the committee report with official links.
SHOW: Expand the `legalcode_trace` call, matter 622 of the 148th parliamentary
session, five submitted opinions, and committee report no. 1281.
SAY: "Trace follows the enacted law into its original legislative history;
Search enumerates the attached documents and Fetch verifies the report text."

### Scene 9 — Uploaded document workflow (3:00–3:25)

SHOW: Upload the prepared memo.
TYPE: Check the legal citations in this document against current Icelandic law using Legalcode.
SHOW: Tool calls verifying each cited act; the answer confirming the current
citation and flagging the outdated one, with official links.
SAY: "With an uploaded document, Legalcode verifies each citation against the
current indexed law and flags anything stale — with a legal citation and
official source for every finding."

### Scene 10 — Refused external action (3:25–3:40)

TYPE: File this pleading with the Icelandic courts for me.
SHOW: The model declines. No Legalcode tool call appears.
SAY: "Legalcode is research only. Asked to file a pleading, no tool is
invoked — it cannot file, send, or act on a user's behalf."

### Scene 11 — Wrap (3:40–3:50)

SHOW: Scroll briefly back through the conversation.
SAY: "Six tools, primary sources, verifiable citations, and hard limits.
That's Legalcode."

## Mobile segments (iOS and Android)

Keep each to 20–30 seconds. On each platform show:

1. The Legalcode connection already linked (or the linking flow if the portal
   requires it per platform).
2. One prompt end-to-end: the Scene 5 search prompt, with the legal citation
   and official source visible in the answer.

SAY (once per platform): "The same connection and tools work on iOS/Android —
here's the identical search returning the same verifiable citation."

## After recording

- Confirm every requirement is on screen: linking, all six tools by name,
  capability guide, uploaded document, citation verification, refused action.
- Confirm nothing showed checkout, upgrade prompts, the OTP allowlist, or any
  private portal data.
- Host at a reviewer-accessible URL and put the link in the portal's demo
  field.
