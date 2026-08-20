# OpenAI Plugins Directory submission

## Final listing

- Name: Legalcode
- Version: 1.1.3
- Subtitle: Primary-source legal research
- Category: Productivity
- Developer identity: verified Fordæmi ehf.
- Plugin author: Fordæmi ehf.
- Website: https://legalcode.md
- Customer support: https://legalcode.md/contact
- Privacy policy: https://legalcode.md/privacy
- Terms of service: https://legalcode.md/terms
- MCP type: Universal
- MCP URL: https://mcp.legalcode.md/mcp
- Commerce and purchasing: unchecked
- Custom UI, screenshots, and CSP: none
- Plugin repository: https://github.com/RobertHH-IS/legalcode-plugin
- Included skill: legalcode-mcp-guide

Description:

> Legal research grounded in primary sources. Legalcode gives ChatGPT direct access to statutes, case law, regulatory guidance, agreements, legislative history, and patents across more than 40 jurisdictions — tens of millions of indexed documents from official publishers, court databases, and regulatory portals — with human-readable citations and links to official materials, so you can verify conclusions against the original text instead of taking citations on faith.
>
> Search goes far beyond full text. Sources are indexed with deep legal metadata, so you can filter by court, judge, counsel, party, outcome, cited legal basis, act type, issuing agency, or date — find the version of a law in force on a specific date, or jump straight to a known instrument by its official number or citation.
>
> Fetch retrieves the text itself: a complete act or judgment, or one targeted provision — a single article or section — with the metadata to cite it.
>
> Analyze turns the whole corpus into answers no single document holds: group decisions on a topic by year, cross-tabulate outcomes by court, chart a trend over time, or surface the legal bases courts cite most.
>
> Trace follows indexed relationships: which decisions apply a law, what a judgment cites, which national law implements an international instrument, and the legislative history behind a provision.
>
> Legalcode receives only your research queries — processed, never stored. Your documents stay in ChatGPT. Coverage varies by jurisdiction and source.

Starter prompts:

1. Research an Icelandic legal issue using current legislation and case law.
2. Find EU legislation and decisions, then trace national implementation measures.
3. Show which Icelandic legal sources are available and what I can ask about them.

Release notes:

> Initial public submission of Legalcode. Includes an authenticated legal research MCP server with five tools and one provider-neutral MCP guide skill. The plugin performs no purchases, filings, communications, or other external actions.

Submission assets:

- Directory icon: plugins/legalcode-openai/assets/legalcode-directory-256.png
- Composer icon: plugins/legalcode-openai/assets/legalcode-composer-48.png
- Local submission worksheet: chatgpt-app-submission.json

`chatgpt-app-submission.json` is hand-maintained at the repository root; no script generates it.
Use it to keep the listing metadata, tool annotations, five positive cases, and three negative cases
consistent while completing the OpenAI submission portal. The portal fields, not this file, are the
submitted record.

## MCP contract

The submission advertises exactly:

1. legalcode_discover
2. legalcode_search
3. legalcode_fetch
4. legalcode_analyze
5. legalcode_trace

Every tool declares OAuth with legalcode.public.read, legalcode.laws.read, and legalcode.cases.read. The five research tools only retrieve or compute legal information and cannot change legal materials, relationships, user content, or public or external systems, so the annotations are:

- readOnlyHint: true
- openWorldHint: false
- destructiveHint: false
- idempotentHint: true

The tools cannot alter, publish, send, file, purchase, or delete legal materials or user content. Retired names remain hidden compatibility aliases and must not appear in tools/list.

The OAuth server uses dynamic client registration and PKCE S256. Do not enter a static client ID. OpenAI callback URLs are registered dynamically. UserInfo is https://mcp.legalcode.md/oauth/userinfo and returns only sub, email, and email_verified.

## Reviewer access

Create one dedicated reviewer user with stable Pro entitlements. The fixed-OTP allowlist must suppress email delivery. Put the reviewer email and fixed code only in the portal’s private reviewer fields. Do not commit either value. The account must require no mailbox access, MFA, SMS, invitation, or private network.

Before submission, create a completely fresh ChatGPT Developer Mode connection and complete dynamic registration, authorization, token exchange, UserInfo, tool listing, and calls.

## Required evaluation cases

### Positive

1. Discover Icelandic sources and ways to narrow research with legalcode_discover.
2. Search for Icelandic Act No. 90/2018 and return its legal citation and official source with legalcode_search.
3. Directly exercise legalcode_fetch against the stable law-family record handle in the worksheet.
4. Analyze Icelandic data-protection decisions by year, without implying causation.
5. Trace GDPR CELEX 32016R0679 to an Icelandic implementing law and identify it with a human-readable citation and official source.

The direct Fetch case is a standalone technical evaluation because Fetch requires a record handle.
Keep that handle inside the worksheet and tool call; the recorded conversational demo must chain from
Search to Fetch without typing or displaying it.

### Negative

1. Do not invoke Legalcode to file a pleading.
2. Do not invoke Legalcode to rewrite a contract clause when the user excludes legal research.
3. Do not invoke Legalcode for weather.

## Demo recording

Record a reviewer-accessible demonstration of:

- account linking;
- all five MCP tools;
- the MCP tool-guide explaining supported capabilities;
- one uploaded-document workflow;
- citation verification;
- one unsupported external-action request.

Cover the web, iOS, and Android experiences requested by the portal. Show no checkout or upgrade direction.

## Production evidence gate

The production host must set OPENAI_APPS_CHALLENGE_TOKEN to the value generated by Apps Management. GET https://mcp.legalcode.md/.well-known/openai-apps-challenge must return that exact value as text/plain with no wrapper. It returns 404 while unset.

Before clicking Submit:

1. Verify OAuth and OpenID discovery, UserInfo, protected-resource metadata, server card, challenge route, and authenticated tools/list.
2. Run MCP Inspector against https://mcp.legalcode.md/mcp.
3. Run all five positive and three negative tests from a fresh connection.
4. Confirm telemetry shows successful registration, authorization, token exchange, and tool calls with no invalid_client, invalid_redirect_uri, or tool_not_found events.
5. Copy the validated worksheet values into the portal, enter all five positive and three negative
   cases, and provide both icons, the one-skill bundle, reviewer credentials, and demo URL.
6. Select the verified Fordæmi ehf. identity.
7. Submit only after Scan Tools is clean.

Publication and identity selection remain manual portal actions.
