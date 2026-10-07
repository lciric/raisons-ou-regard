#!/usr/bin/env python3
"""Convertit la carte des angles (markdown) en HTML autonome, pour l'export PDF (Chromium de Playwright, html_vers_pdf.js).

Usage : python3 md_vers_html.py <carte.md> <sortie.html>

Python-Markdown attend des sous-listes indentées de quatre espaces et une ligne vide
avant une liste ou un tableau : le texte est normalisé en ce sens, sans toucher au contenu.
"""
import re
import sys

import markdown

LIST_RE = re.compile(r"^( *)([-*]|\d+\.) ")


def normaliser(texte: str) -> str:
    lignes = texte.split("\n")
    sortie = []
    precedente = ""
    type_haut = None  # type de la dernière liste de premier niveau : "ol" ou "ul"
    for ligne in lignes:
        m = LIST_RE.match(ligne)
        if m and 1 <= len(m.group(1)) <= 4:
            # Sous-liste (un seul niveau dans la carte) : quatre espaces.
            ligne = "    " + ligne.lstrip(" ")
        elif m and m.group(1) == "":
            type_ligne = "ol" if m.group(2)[0].isdigit() else "ul"
            if type_haut is not None and type_ligne != type_haut and precedente.strip() != "":
                # Changement de type de liste sans ligne vide : on sépare les deux listes.
                sortie.extend(["", "<!-- fin de liste -->", ""])
                precedente = ""
            type_haut = type_ligne
        elif ligne.strip() == "" or not ligne.startswith(" "):
            if not m and ligne.strip() != "":
                type_haut = None
        est_liste = bool(LIST_RE.match(ligne))
        est_tableau = ligne.startswith("|")
        prec_liste = bool(LIST_RE.match(precedente))
        prec_tableau = precedente.startswith("|")
        prec_vide = precedente.strip() == ""
        if est_liste and not prec_vide and not prec_liste and not precedente.startswith("    "):
            sortie.append("")
        if est_tableau and not prec_vide and not prec_tableau:
            sortie.append("")
        sortie.append(ligne)
        precedente = ligne
    return "\n".join(sortie)


CSS = """
body { font-family: 'DejaVu Sans', sans-serif; font-size: 9pt; line-height: 1.35; }
h1 { font-size: 17pt; margin-bottom: 4pt; }
h2 { font-size: 13.5pt; margin-top: 16pt; }
h3 { font-size: 11pt; margin-top: 12pt; }
h1, h2, h3 { break-after: avoid; }
p, li { font-size: 9pt; }
table { border-collapse: collapse; width: 100%; }
th, td { font-size: 7.5pt; vertical-align: top; padding: 2pt 3pt; border: 0.5pt solid #888888; }
th { background: #e8e8e8; }
tr { break-inside: auto; }
td { overflow-wrap: break-word; }
code { font-family: 'DejaVu Sans Mono', monospace; font-size: 8pt; }
td code { font-size: 7pt; overflow-wrap: anywhere; word-break: break-all; }
"""


def main() -> None:
    source, cible = sys.argv[1], sys.argv[2]
    with open(source, encoding="utf-8") as f:
        texte = f.read()
    corps = markdown.markdown(
        normaliser(texte), extensions=["tables", "sane_lists"], output_format="html5"
    )
    corps = corps.replace("<table>", '<table border="1" cellspacing="0" cellpadding="3" width="100%">')
    # Typographie française à l'impression seulement : espaces insécables autour des guillemets
    # et avant les ponctuations hautes, pour qu'aucune ligne ne commence par « », :, ;, ? ou !.
    nbsp = " "
    for avant, apres in (("« ", "«" + nbsp), (" »", nbsp + "»"), (" :", nbsp + ":"),
                         (" ;", nbsp + ";"), (" ?", nbsp + "?"), (" !", nbsp + "!")):
        corps = corps.replace(avant, apres)
    html = (
        "<!DOCTYPE html>\n<html lang=\"fr\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<title>La carte des angles déjà pris — programme « Raisons ou regard ? »</title>\n"
        f"<style>{CSS}</style>\n</head>\n<body>\n{corps}\n</body>\n</html>\n"
    )
    with open(cible, "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == "__main__":
    main()
