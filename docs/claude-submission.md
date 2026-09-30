# Claude Plugin Directory submission

Prepared on 2026-09-11. Submission requires an authenticated Claude Console session.

## Submission route

- Console: https://platform.claude.com/plugins/submit
- Team/Enterprise organization: https://claude.ai/admin-settings/directory/submissions/plugins/new
- Official requirements: https://claude.com/docs/plugins/submit

Console requires a Developer, Admin, or Owner role. The Claude.ai route requires directory management access. The public plugin repository must pass `claude plugin validate`. This application is for the Plugin Directory; MCP connector listings have a separate submission process.

## Listing copy

- Display name: Legalcode
- Publisher: Fordæmi ehf.
- Repository: https://github.com/RobertHH-IS/legalcode-plugin
- Plugin directory: https://github.com/RobertHH-IS/legalcode-plugin/tree/main/plugins/legalcode-claude
- Plugin path: `plugins/legalcode-claude`
- Website: https://legalcode.md
- Support: https://legalcode.md/contact
- Privacy: https://legalcode.md/privacy
- Terms: https://legalcode.md/terms
- Short description: Primary-source legal research

Description:

Legalcode connects Claude to primary legal materials through an authenticated, read-only MCP server. Search legal sources, retrieve source metadata and excerpts, analyze aggregate patterns, and trace relationships among laws, decisions, citations, and legislative history. The included research guide helps Claude combine these capabilities and keep conclusions tied to verifiable sources.

## Reviewer setup

The bundled remote MCP endpoint is `https://mcp.legalcode.md/mcp`. Complete the client-managed authentication flow with a Legalcode account. Provide any reviewer credentials only through private submission fields, never in this repository.

Example prompts:

1. Show which Icelandic legal sources are available and what I can ask about them.
2. Research an Icelandic legal issue using current legislation and case law.
3. Find EU legislation and decisions, then trace national implementation measures.

## Validation

```sh
claude plugin validate plugins/legalcode-claude
claude plugin validate .claude-plugin/marketplace.json
```

The OpenAI submission files are separate from this Claude package. Submission and acceptance must be confirmed in the authenticated portal; repository validation alone does not establish either.

## Version 1.2.0 update

The Claude guide and call examples now match the OpenAI package and all six MCP tools.
Patents uses the dedicated live EPO tool; parliamentary workflows preserve exact entries,
versions, temporal bounds and count semantics. The hosted endpoint and authentication are unchanged.
