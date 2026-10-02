#!/usr/bin/env python3
"""Rend un fichier Markdown en PDF A4 avec Chromium (Playwright), pied de page numéroté.

Usage : python3 md_vers_pdf.py <entree.md> <sortie.pdf>

Le Markdown est lu en CommonMark (markdown-it-py), comme sur GitHub : une liste peut
suivre un paragraphe sans ligne vide, et une liste imbriquée s'aligne sur le texte de
l'élément parent. (La première version, avec Python-Markdown, aplatissait ces listes.)
"""
import html, os, subprocess, sys, tempfile

from markdown_it import MarkdownIt

ICI = os.path.dirname(os.path.abspath(__file__))

CSS = """
@page { size: A4; margin: 17mm 16mm 18mm 16mm; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: 'DejaVu Serif', Georgia, serif; font-size: 10.3pt; line-height: 1.44; color: #111; }
h1 { font-size: 17pt; margin: 0 0 10pt; color: #1a2a44; }
h2 { font-size: 13.5pt; margin: 18pt 0 6pt; border-bottom: 1px solid #9aa6b8; padding-bottom: 2pt; color: #1a2a44; page-break-after: avoid; }
h3 { font-size: 11.5pt; margin: 12pt 0 4pt; page-break-after: avoid; }
h4 { font-size: 10.5pt; margin: 10pt 0 3pt; page-break-after: avoid; }
p, li { orphans: 3; widows: 3; }
p { margin: 4pt 0 6pt; }
ul, ol { margin: 2pt 0 6pt 0; padding-left: 18pt; }
li { margin: 1pt 0; }
li > p { margin: 2pt 0; }
table { border-collapse: collapse; margin: 6pt 0 10pt; font-size: 8.8pt; line-height: 1.32; width: 100%; page-break-inside: auto; }
th, td { border: 1px solid #8a94a6; padding: 3pt 4pt; vertical-align: top; text-align: left; }
th { background: #e8edf5; }
tr { page-break-inside: avoid; }
code { font-family: 'DejaVu Sans Mono', monospace; font-size: 8.6pt; background: #f1f3f6; padding: 0 2pt; word-break: break-word; }
pre { background: #f1f3f6; padding: 6pt; font-size: 8.4pt; white-space: pre-wrap; word-break: break-word; }
blockquote { border-left: 3px solid #9aa6b8; margin: 6pt 0; padding: 3pt 9pt; color: #222; background: #f7f8fa; }
hr { border: 0; border-top: 1px solid #bbb; margin: 12pt 0; }
sup { font-size: 70%; }
"""


def main():
    src, out = sys.argv[1], sys.argv[2]
    texte = open(src, encoding='utf8').read()
    corps = MarkdownIt('commonmark').enable('table').render(texte)
    nom = html.escape(os.path.basename(src))
    page = (f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>{nom}</title>'
            f'<style>{CSS}</style></head><body>{corps}</body></html>')
    pied = ('<div style="font-family: DejaVu Sans, sans-serif; font-size: 7.5px; color: #555; width: 100%; '
            'padding: 0 16mm; display: flex; justify-content: space-between;">'
            f'<span>{nom}</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>')
    with tempfile.TemporaryDirectory() as d:
        h = os.path.join(d, 'page.html')
        open(h, 'w', encoding='utf8').write(page)
        subprocess.run(['node', os.path.join(ICI, 'imprimer_pdf.js'), h, out, pied], check=True, timeout=600)
    print(out, os.path.getsize(out))


if __name__ == '__main__':
    main()
