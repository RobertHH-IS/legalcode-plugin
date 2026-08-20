# Legalcode for OpenAI

Legalcode provides authenticated primary-source legal research through the universal hosted MCP endpoint:

https://mcp.legalcode.md/mcp

This is the complete OpenAI submission bundle. It contains one provider-neutral skill,
`legalcode-mcp-guide`, which explains when and how to combine Legalcode's five MCP tools.
Specialized legal workflow skills are intentionally distributed separately and are not part of
the plugin submission.

The bundle contains no command-line program, local server, hook, script, app manifest, or custom
UI. It bundles the hosted MCP connection in `.mcp.json`; the OpenAI submission portal also receives
the same endpoint through its **With MCP** submission flow.

## Included skill

- `legalcode-mcp-guide`

## MCP capabilities

The canonical tool surface is legalcode_discover, legalcode_search, legalcode_fetch, legalcode_analyze, and legalcode_trace. The tools only retrieve or compute legal information. They cannot alter, publish, send, file, purchase, or delete legal materials, relationships, user content, or public or external systems.

Coverage varies by jurisdiction and source. Important conclusions should be checked against the returned legal citations, official links, and underlying primary materials.

## Submission metadata

- Name: Legalcode
- Version: 1.1.3
- Developer: Fordæmi ehf.
- Category: Productivity
- Website: https://legalcode.md
- Support: https://legalcode.md/contact
- Privacy: https://legalcode.md/privacy
- Terms: https://legalcode.md/terms
- Repository: https://github.com/RobertHH-IS/legalcode-plugin
