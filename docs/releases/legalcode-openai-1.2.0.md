# Legalcode OpenAI package 1.2.0

Prepared on 2026-09-30. The upload file is `dist/legalcode-openai-1.2.0.zip`.

This release preserves the `legalcode` package name, publisher, existing manifest format and
`https://mcp.legalcode.md/mcp` connection. It updates the included guide for all six tools, dedicated
patent search and retrieval, parliamentary event and participation assignments, exact versions,
historical dates, counting units and body availability. It adds the missing support URL, five
positive and three negative review scenarios, and release notes. Country targeting and the saved
demo URL are omitted to preserve their existing portal values. Credentials are excluded.

## Validation

- Source-package conformance and the pinned skill-reference validator passed.
- All 12 packaged examples passed the current MCP input schemas. Binding markers are test
  fixtures that must be replaced by returned handles before execution; these are not live results.
- The extracted ZIP passed the same conformance checks, ZIP integrity and source-file hash parity.
- All three PNG assets satisfy the documented square-icon dimensions and size limits.
- The package passed the configured secret-pattern scan and excludes generated system files.
- Both public and Pro server cards advertise six tools; only Patents advertises open-world access.
- Both plugin packages and the Claude marketplace declare version 1.2.0; shared guide and example
  parity are checked by the conformance gate. CI builds and saves the upload ZIP with its evidence.

The checksum and file inventory are recorded next to the ZIP in its `.zip.sha256` and
`.validation.json` files. This checks package contents, not every possible secret pattern or every
hosted research scenario. Fresh reviewer-session scenarios and portal approval are separate.

## Upload

1. Open the existing Legalcode plugin in OpenAI's plugin management dashboard.
2. Select **Upload plugin to make changes** and choose `legalcode-openai-1.2.0.zip`.
3. Confirm version 1.2.0 under **Metadata & Skills** and inspect the automated findings.
4. Keep reviewer credentials and the demonstration video in the secure portal fields.
5. Complete the applicable review and publish the approved package version.

For hosted Search or Analyze updates, inspect **MCPs → Issues → Live definition / Held update**.
Rescan or appeal the held definitions separately. Uploading this ZIP does not approve those tools.

Official references:

- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/plugins/deploy/submission
