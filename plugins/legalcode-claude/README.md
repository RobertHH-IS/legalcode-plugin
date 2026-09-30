# Legalcode for Claude

Legalcode connects Claude to primary legal sources through the hosted MCP endpoint at
`https://mcp.legalcode.md/mcp`.

The plugin includes one skill, `legalcode-mcp-guide`, that coordinates Legalcode's six read-only
research tools: Discover, Search, Fetch, Patents, Analyze, and Trace. It helps Claude inspect current source
coverage, find legal authorities, verify source text, analyze indexed cohorts, and follow legal
relationships while keeping conclusions tied to citations and official-source links. Dedicated Patents
searches the external EPO service; generic Search and Fetch use the Legalcode corpus. Structured
parliamentary workflows preserve document versions, event identities, dated roles and counting units.

Coverage varies by jurisdiction and source. Important conclusions should be checked against the
returned citations, official links, and underlying primary materials.

## Publisher

- Fordæmi ehf.
- Website: https://legalcode.md
- Support: https://legalcode.md/contact
- Privacy: https://legalcode.md/privacy
- Terms: https://legalcode.md/terms
