#!/usr/bin/env python3
"""Rend le programme (Markdown à blocs HTML : couverture, sommaire, parties) en PDF A4.

Usage : python3 programme_vers_pdf.py <entree.md> <sortie.pdf>

Deux passes : la première trouve, par pdftotext, la page où commence chaque partie ;
la seconde remplit le sommaire (@@P1@@ … @@P12@@, @@PA@@). Pied de page numéroté.
"""
import html, os, re, subprocess, sys, tempfile

from markdown_it import MarkdownIt

ICI = os.path.dirname(os.path.abspath(__file__))

CSS = """
@page { size: A4; margin: 17mm 16mm 18mm 16mm; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: 'DejaVu Serif', Georgia, serif; font-size: 10pt; line-height: 1.42; color: #111; }
h1 { font-size: 18pt; margin: 0 0 10pt; color: #1a2a44; }
h2 { font-size: 13pt; margin: 16pt 0 6pt; border-bottom: 1px solid #9aa6b8; padding-bottom: 2pt; color: #1a2a44; page-break-after: avoid; }
h3 { font-size: 11pt; margin: 12pt 0 4pt; page-break-after: avoid; }
p, li { orphans: 3; widows: 3; }
p { margin: 4pt 0 6pt; }
ul, ol { margin: 2pt 0 6pt 0; padding-left: 17pt; }
li { margin: 1pt 0; }
li > p { margin: 2pt 0; }
table { border-collapse: collapse; margin: 6pt 0 10pt; font-size: 8.6pt; line-height: 1.32; width: 100%; page-break-inside: auto; }
th, td { border: 1px solid #8a94a6; padding: 3pt 4pt; vertical-align: top; text-align: left; }
th { background: #e8edf5; }
tr { page-break-inside: avoid; }
code { font-family: 'DejaVu Sans Mono', monospace; font-size: 8.4pt; background: #f1f3f6; padding: 0 2pt; word-break: break-word; }
blockquote { border-left: 3px solid #9aa6b8; margin: 6pt 0; padding: 3pt 9pt; color: #222; font-size: 9.2pt; background: #f7f8fa; }
sup { font-size: 70%; }
.cover { page-break-after: always; }
.cover h1 { font-size: 30pt; margin: 4pt 0 6pt; }
.kicker { font-family: 'DejaVu Sans', sans-serif; font-size: 9pt; letter-spacing: 0.06em; text-transform: uppercase; color: #4a5a78; margin: 0; }
.subtitle { font-style: italic; font-size: 11pt; color: #2b3a55; margin: 0 0 12pt; }
.covbox { border: 1px solid #9aa6b8; background: #f6f8fb; padding: 8pt 11pt; font-size: 9.3pt; line-height: 1.36; }
.covbox p { margin: 3pt 0 5pt; }
.toc { page-break-after: always; }
.toc table { font-size: 10pt; }
.toc td:first-child { width: 7%; text-align: center; }
.toc td:last-child { width: 8%; text-align: right; }
.toc p { font-size: 9.3pt; }
section.partie { page-break-before: always; }
.phrase { border-left: 4px solid #1a2a44; background: #f3f6fa; padding: 6pt 10pt; margin: 8pt 0 10pt; }
.alerte { border: 1px solid #b4532a; background: #fbf3ee; padding: 6pt 10pt; margin: 8pt 0 10pt; }
"""

def pied(mention):
    return ('<div style="font-family: DejaVu Sans, sans-serif; font-size: 7.5px; color: #555; width: 100%; '
            'padding: 0 16mm; display: flex; justify-content: space-between;">'
            f'<span>Raisons ou regard ? · {html.escape(mention)}</span>'
            '<span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>')

TITRES = [
    ('P1', '1 · Antériorité'), ('P2', '2 · Questions et lectures'), ('P3', '3 · Matériel'),
    ('P4', '4 · Les phases de l'), ('P5', '5 · L'), ('P6', '6 · Prédictions et règles'),
    ('P7', '7 · Dégradation appariée'), ('P8', '8 · Menaces'), ('P9', '9 · Ressources'),
    ('P10', '10 · Le papier'), ('P11', '11 · Ce qui reste'), ('P12', '12 · Les décisions'),
    ('PA', 'Annexe · La table'),
]


def page_html(texte, titre):
    # CommonMark (markdown-it-py) : une liste peut suivre un paragraphe, et les listes
    # imbriquées s'alignent sur le texte de l'élément parent, comme sur GitHub.
    corps = MarkdownIt('commonmark').enable('table').render(texte)
    return (f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>{html.escape(titre)}</title>'
            f'<style>{CSS}</style></head><body>{corps}</body></html>')


def imprimer(html_path, pdf_path, mention):
    subprocess.run(['node', os.path.join(ICI, 'imprimer_pdf.js'), html_path, pdf_path, pied(mention)],
                   check=True, timeout=600)


def pages_des_parties(pdf_path):
    n = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', pdf_path], capture_output=True, text=True).stdout).group(1))
    trouve, sommaire = {}, None
    for p in range(1, n + 1):
        t = subprocess.run(['pdftotext', '-f', str(p), '-l', str(p), '-layout', pdf_path, '-'],
                           capture_output=True, text=True).stdout
        tete = [l.strip() for l in t.splitlines() if l.strip()][:4]
        if sommaire is None:
            if any(l.startswith('Sommaire') for l in tete):
                sommaire = p
            continue
        for cle, debut in TITRES:
            if cle not in trouve and any(l.startswith(debut) for l in tete):
                trouve[cle] = p
    return trouve, n


def main():
    src, out = sys.argv[1], sys.argv[2]
    texte = open(src, encoding='utf8').read()
    m = re.search(r'<p class="kicker">(.*?)</p>', texte)
    mention = m.group(1) if m else os.path.basename(src)
    titre = 'Raisons ou regard ? — ' + mention
    with tempfile.TemporaryDirectory() as d:
        h = os.path.join(d, 'page.html')
        brouillon = re.sub(r'@@P[0-9A]+@@', '00', texte)
        open(h, 'w', encoding='utf8').write(page_html(brouillon, titre))
        imprimer(h, out, mention)
        trouve, n = pages_des_parties(out)
        manquants = [c for c, _ in TITRES if c not in trouve]
        if manquants:
            sys.exit(f'parties introuvables dans le PDF : {manquants}')
        final = texte
        for cle, p in trouve.items():
            final = final.replace(f'@@{cle}@@', str(p))
        open(h, 'w', encoding='utf8').write(page_html(final, titre))
        imprimer(h, out, mention)
        trouve2, n2 = pages_des_parties(out)
        if trouve2 != trouve:
            sys.exit(f'la pagination a bougé entre les passes : {trouve} / {trouve2}')
    print(out, os.path.getsize(out), 'octets,', n2, 'pages ;', trouve)


if __name__ == '__main__':
    main()
