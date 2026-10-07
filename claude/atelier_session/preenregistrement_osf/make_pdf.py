"""The filing text, Markdown to HTML for Chromium's print: lists that python-markdown would miss are fixed (a blank
line before a list that follows a paragraph; nested items indented by 4 spaces)."""
import re
import sys
from pathlib import Path

import markdown

src, out_html = Path(sys.argv[1]), Path(sys.argv[2])
LIST = re.compile(r"^\s*(?:[-*]|\d+\.)\s")
lines, prev = [], ""
for line in src.read_text(encoding="utf-8").splitlines():
    n = len(line) - len(line.lstrip(" "))
    fixed = " " * (2 * n) + line.lstrip(" ") if n and not line.lstrip().startswith("|") else line
    if LIST.match(fixed) and prev.strip() and not LIST.match(prev) and not prev.startswith(" ") and not prev.startswith("|"):
        lines.append("")
    lines.append(fixed)
    prev = fixed
html = markdown.markdown("\n".join(lines), extensions=["tables"])
css = """
@page { size: A4; margin: 18mm 16mm; }
body { font-family: 'DejaVu Serif', Georgia, serif; font-size: 10pt; line-height: 1.38; color: #111; }
h1 { font-size: 17pt; margin: 0 0 4pt; } h2 { font-size: 13pt; margin: 16pt 0 5pt; border-bottom: 1px solid #999; padding-bottom: 2pt; }
h3 { font-size: 11pt; margin: 12pt 0 4pt; } p, li { margin: 3pt 0; } ul, ol { margin: 3pt 0 3pt 16pt; padding-left: 6pt; }
table { border-collapse: collapse; width: 100%; margin: 6pt 0; font-size: 8.6pt; page-break-inside: auto; }
th, td { border: 1px solid #aaa; padding: 3pt 4pt; vertical-align: top; text-align: left; } tr { page-break-inside: avoid; }
th { background: #eee; } code { font-family: 'DejaVu Sans Mono', monospace; font-size: 7.6pt; word-break: break-all; }
hr { border: 0; border-top: 1px solid #999; margin: 12pt 0; }
"""
out_html.write_text(f"<!doctype html><html><head><meta charset='utf-8'><title>Preregistration, stage 1</title><style>{css}</style></head><body>{html}</body></html>", encoding="utf-8")
