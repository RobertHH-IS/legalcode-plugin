#!/usr/bin/env python3
"""Post-render helper: inject thin horizontal borders into every w:tbl in a .docx.

Pandoc renders markdown tables without any visible borders by default. For a long
legal report with many tables, the lack of horizontal row separators makes the
tables visually fuse into surrounding prose and forces the reader to count cells.
This helper adds the OOXML equivalent of a single 0.5pt grey line between rows
(insideH) and on the top/bottom edge of each table.

Usage: python3 add-table-borders.py <input.docx> [<output.docx>]
       (if output is omitted, the file is edited in place via a temp swap)

The helper is idempotent: tables that already have a w:tblBorders element are
left unchanged.
"""
import re
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

BORDER_XML = (
    '<w:tblBorders>'
    '<w:top w:val="single" w:sz="4" w:space="0" w:color="999999"/>'
    '<w:left w:val="nil"/>'
    '<w:bottom w:val="single" w:sz="4" w:space="0" w:color="999999"/>'
    '<w:right w:val="nil"/>'
    '<w:insideH w:val="single" w:sz="4" w:space="0" w:color="999999"/>'
    '<w:insideV w:val="nil"/>'
    '</w:tblBorders>'
)

# w:sz is in eighths of a point. 4 = 0.5pt = the thinnest visible single line.
# Color #999999 is a soft grey — visible but not dominating.

# Pattern: find <w:tblPr>...</w:tblPr> blocks that lack <w:tblBorders>, and
# inject BORDER_XML before the closing </w:tblPr>.
TBLPR_PATTERN = re.compile(
    r'(<w:tblPr>(?:(?!</w:tblPr>).)*?)(</w:tblPr>)',
    re.DOTALL,
)


def add_borders_to_tblpr(match: re.Match) -> str:
    body, close = match.group(1), match.group(2)
    if 'tblBorders' in body:
        return match.group(0)
    return body + BORDER_XML + close


def process(in_path: Path, out_path: Path) -> tuple[int, int]:
    """Returns (tables_touched, tables_total)."""
    with tempfile.NamedTemporaryFile(suffix='.docx', delete=False) as tmp:
        tmp_path = Path(tmp.name)

    tables_touched = 0
    tables_total = 0

    with zipfile.ZipFile(in_path, 'r') as zin, zipfile.ZipFile(
        tmp_path, 'w', zipfile.ZIP_DEFLATED
    ) as zout:
        for item in zin.namelist():
            data = zin.read(item)
            if item == 'word/document.xml':
                text = data.decode('utf-8')
                tables_total = len(TBLPR_PATTERN.findall(text))
                new_text, count = TBLPR_PATTERN.subn(add_borders_to_tblpr, text)
                # subn counts every match; we want how many were actually changed.
                tables_touched = sum(
                    1
                    for m in TBLPR_PATTERN.finditer(text)
                    if 'tblBorders' not in m.group(1)
                )
                data = new_text.encode('utf-8')
            zout.writestr(item, data)

    shutil.move(str(tmp_path), str(out_path))
    return tables_touched, tables_total


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    in_path = Path(sys.argv[1])
    out_path = Path(sys.argv[2]) if len(sys.argv) > 2 else in_path
    if not in_path.exists():
        print(f'error: {in_path} not found', file=sys.stderr)
        return 1
    touched, total = process(in_path, out_path)
    print(f'{in_path.name}: borders added to {touched} of {total} tables')
    return 0


if __name__ == '__main__':
    sys.exit(main())
