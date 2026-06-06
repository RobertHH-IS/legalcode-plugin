#!/usr/bin/env python3
"""Build the reference docx that pandoc uses for Icelandic-legal typography.

One-time setup helper. Generates a Word document whose styles encode the
typography table from the legalcode-docx-render SKILL.md:

- Normal/body: Arial 10pt
- Heading 1:   Arial 14pt bold
- Heading 2:   Arial 12pt bold
- Heading 3:   Arial 10pt bold
- Heading 4:   Arial 10pt bold italic
- Margins:     1 inch on all sides

Pandoc's --reference-doc flag picks up the styles and applies them to every
generated document. Table-cell typography is set by the body Normal style;
cell-level overrides are applied by the post-render helper if needed.

Usage: python3 build-reference-docx.py <output.docx>
       (defaults to ./reference-is.docx if no path is given)
"""
import sys
from pathlib import Path

try:
    from docx import Document
    from docx.shared import Pt, Inches
except ImportError:
    print(
        'error: python-docx not installed. Install with: pip install python-docx',
        file=sys.stderr,
    )
    sys.exit(2)


def build(out_path: Path) -> None:
    doc = Document()
    styles = doc.styles

    # Body / default
    normal = styles['Normal']
    normal.font.name = 'Arial'
    normal.font.size = Pt(10)

    # Headings
    for name, size, italic in [
        ('Heading 1', 14, False),
        ('Heading 2', 12, False),
        ('Heading 3', 10, False),
        ('Heading 4', 10, True),
    ]:
        s = styles[name]
        s.font.name = 'Arial'
        s.font.size = Pt(size)
        s.font.bold = True
        s.font.italic = italic

    # Margins
    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)

    doc.save(out_path)


def main() -> int:
    out_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('reference-is.docx')
    out_path.parent.mkdir(parents=True, exist_ok=True)
    build(out_path)
    print(f'reference docx written to {out_path}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
