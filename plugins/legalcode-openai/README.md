# Legalcode for OpenAI

Legalcode provides authenticated primary-source legal research through the universal hosted MCP endpoint:

https://mcp.legalcode.md/mcp

This OpenAI submission bundle contains no command-line program, local server, hook, script, app manifest, or custom UI. OpenAI connects the MCP endpoint separately through the submission portal.

## Included skills

1. legalcode-mcp-tool-guide
2. legalcode-public-search
3. legalcode-contract-review
4. legalcode-nda-triage
5. legalcode-dpia-generator
6. legalcode-document-qa
7. legalcode-legal-memorandum
8. legalcode-statute-analysis
9. legalcode-case-timeline-builder
10. legalcode-tabular-review

Additional optional skills are available at:

https://github.com/RobertHH-IS/legalcode-plugin/tree/main/more-skills

## MCP capabilities

The canonical tool surface is legalcode_discover, legalcode_search, legalcode_fetch, legalcode_analyze, and legalcode_trace. The tools search indexed legal sources and may update private operational metering and telemetry. They cannot alter, publish, send, file, purchase, or delete legal materials or user content.

Coverage varies by jurisdiction and source. Important conclusions should be checked against the returned source references and underlying primary materials.

## Submission metadata

- Name: Legalcode
- Version: 1.1.0
- Developer: Fordæmi ehf.
- Category: Productivity
- Website: https://legalcode.md
- Support: https://legalcode.md/contact
- Privacy: https://legalcode.md/privacy
- Terms: https://legalcode.md/terms
- Repository: https://github.com/RobertHH-IS/legalcode-plugin
