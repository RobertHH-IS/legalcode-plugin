---
name: legalcode-mcp-setup
description: >
  Connect or reconnect the hosted Legalcode MCP endpoint in a client that
  supports remote Streamable HTTP servers and OAuth.
---

# Legalcode MCP Setup

Use the client’s graphical connector or MCP settings. Add this universal remote endpoint exactly:

https://mcp.legalcode.md/mcp

Choose Streamable HTTP if the client asks for a transport. Start OAuth account linking without entering a static client ID or client secret: Legalcode supports dynamic client registration and PKCE S256.

If a connection reports tool_not_found or advertises tools other than legalcode_discover, legalcode_search, legalcode_fetch, legalcode_analyze, and legalcode_trace, remove the stale connection and create a fresh one. If OAuth reports invalid_redirect_uri, record the exact callback URL shown by the client and contact https://legalcode.md/contact; do not substitute a static client ID.

This guide does not require a local server, command-line program, script, or downloaded credential.
