---
name: legalcode-docx-render
description: >
  Use to render a finalised Markdown file to a self-contained Word document
  suitable for filing with Alþingi committees, ESA, regulated clients, or
  external counsel. Triggers on "render this markdown to docx", "convert to
  Word", or "produce a .docx with Icelandic legal typography". Applies Arial
  10pt body, sized headings, 1-inch margins; injects thin (0.5pt grey)
  horizontal borders between table rows; and runs a mandatory standalone-
  document audit so opening the file in Word, LibreOffice, or Pages produces
  zero update prompts (no TOC field codes, no attached templates, no file-
  system external relationships). Designed as the rendering back end for the
  legalcode-anti-gold-plating-is skill but works as a general-purpose
  Icelandic-legal DOCX renderer. Use after the substantive markdown is
  frozen — this skill does not edit prose; it only renders.
allowed-tools: Read, Write, Bash
---

# Legalcode DOCX Renderer (Icelandic legal typography)

## When to use

After a substantive markdown deliverable is frozen — typically the end of the
*legalcode-anti-gold-plating-is* skill's Stage 9e or Stage 10e — render to a
self-contained `.docx` that is fit for delivery to lawyers, Alþingi
committees, ESA, or regulated parties.

Do not use this skill for drafts under active substantive editing. The pipeline
freezes content before rendering; if content is still changing, render later.

## Typography

| Element | Point size | docx-js size (half-points) | Notes |
|---|---|---|---|
| Body / default | 10pt | 20 | Arial; tight leading |
| Heading 1 | 14pt | 28 | bold |
| Heading 2 | 12pt | 24 | bold |
| Heading 3 | 10pt | 20 | bold |
| Heading 4 | 10pt | 20 | bold italic |
| Tables (cell text) | 9pt | 18 | one step below body |
| Footnotes / captions | 8pt | 16 | |

Page: US Letter or A4 with 1-inch (1440 DXA) margins. Line spacing: single.
Paragraph spacing: 0pt before, 6pt after. Heading paragraph spacing: 12pt
before, 4pt after.

## Standalone-document requirement

The `.docx` must produce **zero prompts** when opened in Word, LibreOffice, or
Pages. Three failure modes are explicitly forbidden:

- **No Word `{ TOC \o ... }` field codes.** The skill renders any *Efnisyfirlit*
  section as ordinary headings and bullets in the markdown source; pandoc must
  be invoked **without** `--toc`.
- **No `<w:attachedTemplate>` references** in `word/settings.xml`. The
  reference document used for typography must not propagate as an attached
  template.
- **No file-system `TargetMode="External"` relationships** in
  `word/_rels/document.xml.rels`. Web URLs (`http://`, `https://`) to
  althingi.is, EUR-Lex, domstolar.is etc. are permitted because they do not
  trigger an open-time prompt; `file://`, drive letters, and relative paths
  are not.

## Table borders (mandatory)

Pandoc renders markdown tables with no `tblBorders` element by default —
every `<w:tbl>` inherits the bare *„Table"* style and the result on screen is
a grid of text floating in white space. For a long legal document with many
tables this fuses the rows visually and forces the reader to count cells.

**Every `<w:tbl>` in the delivered `.docx` must carry a `tblBorders` element
with at minimum a thin (0.5pt, soft grey `#999999`) horizontal line between
rows (`w:insideH`) and on the top and bottom edges of the table (`w:top` /
`w:bottom`). Left, right, and inside-vertical borders must remain blank** —
only horizontal rules between rows are needed.

The post-render helper `scripts/add-table-borders.py` injects these into every
table that lacks them. It is idempotent.

## Render protocol

### Step 1 — Generate the reference docx (one-time setup)

```bash
python3 scripts/build-reference-docx.py /tmp/reference-is.docx
```

This produces a reference document with the typography table above baked in.
Reusable across renders.

### Step 2 — Render with pandoc

```bash
pandoc -f gfm+smart -t docx \
  --metadata title="{Document title}" \
  --metadata lang=is \
  --reference-doc=/tmp/reference-is.docx \
  -o "{output}.docx" \
  "{input}.md"
```

**Do NOT pass `--toc`.** Any table of contents must be hand-written in the
markdown source.

### Step 3 — Inject table borders (mandatory)

```bash
python3 scripts/add-table-borders.py "{output}.docx"
```

Idempotent — re-running on a document that already has borders is a no-op.

### Step 4 — Audit (mandatory)

```bash
F="{output}.docx"
echo "Container valid:    $(unzip -l "$F" | grep -q word/document.xml && echo ✓ || echo ✗)"
echo "Tables w/ borders:  $(unzip -p "$F" word/document.xml | grep -oc 'tblBorders') of $(unzip -p "$F" word/document.xml | grep -oc '<w:tbl>')"
echo "instrText:          $(unzip -p "$F" word/document.xml | grep -c '<w:instrText')"
echo "fldChar:            $(unzip -p "$F" word/document.xml | grep -c '<w:fldChar')"
echo "fldSimple:          $(unzip -p "$F" word/document.xml | grep -c '<w:fldSimple')"
echo "attachedTpl:        $(unzip -p "$F" word/settings.xml 2>/dev/null | grep -c 'attachedTemplate')"
echo "Local-fs ext rels:  $(unzip -p "$F" word/_rels/document.xml.rels 2>/dev/null | grep -E 'TargetMode="External"[^>]*Target="(file:|[A-Z]:|\\.)' | wc -l)"
```

Required output:

- Container valid: ✓
- Tables with borders == count of `<w:tbl>` (1:1)
- instrText, fldChar, fldSimple: all 0
- attachedTpl: 0
- Local-fs ext rels: 0

Any deviation is a hard fail. Repair the docx before delivery — either by
re-rendering without the offending feature or by post-processing the OOXML
directly (`unzip` → edit `word/settings.xml` or
`word/_rels/document.xml.rels` → `zip -X` re-pack).

## Icelandic character preservation

After rendering, confirm Icelandic characters survive:

```bash
pandoc -f docx -t plain "{output}.docx" | head -40 | grep -oE "[þðæöÞÐÆÖ]" | sort -u
```

Expected: at least one of `þ`, `ð`, `æ`, `ö` visible. If any are mangled, the
renderer is misconfigured — re-run with explicit `--metadata lang=is`.

## What this skill does NOT do

- Does not edit the markdown source. If the prose needs work, fix it upstream.
- Does not generate a Table of Contents — the markdown must contain a static
  *Efnisyfirlit* section.
- Does not bundle the Anthropic docx skill. If that skill is available in your
  runtime, use it directly with the typography brief in the parent skill; this
  renderer is the fallback when it is not.

## Provenance

- Created: 2026-05-27
- License: Proprietary (Legalcode)
- Dependencies: pandoc ≥ 3.0, python3 ≥ 3.10, python-docx (for reference-docx
  generation only)
