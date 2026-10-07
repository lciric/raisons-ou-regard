#!/usr/bin/env python3
"""Assemble la v1.6 à partir de la v1.5 et des éditions des cinq rédacteurs.

Chaque opération vérifie que son ancre figure exactement une fois dans le texte courant.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import merges as M

SRC = "/home/user/raisons-ou-regard/claude/PROGRAMME_RAISONS_OU_REGARD_v1.5_2026-10-03.md"
DST = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "v16_out.md")

E = {}
for name in ["transfert", "tirages", "decision29", "rang", "mesures"]:
    for e in json.load(open(os.path.join(HERE, f"ed_{name}.json"), encoding="utf-8")):
        assert e["id"] not in E, e["id"]
        E[e["id"]] = e

def mod(eid, pairs):
    """Copie de l'édition eid, avec des retouches (ancien, nouveau) sur son new_text."""
    e = dict(E[eid])
    t = e["new_text"]
    for old, new in pairs:
        assert t.count(old) == 1, (eid, old)
        t = t.replace(old, new)
    e["new_text"] = t
    return e

def orig(eid):
    return dict(E[eid])

def custom(ids, anchor, mode, new_text):
    return {"id": "+".join(ids), "anchor": anchor, "mode": mode, "new_text": new_text}

# ---------------------------------------------------------------- opérations, dans l'ordre du document
OPS = []
add = OPS.append

# En-tête et couverture
add(orig("E01")); add(orig("E02")); add(orig("A4-00"))
add(mod("E03", [
    ("une sonde apprise sur l'extraction, lue sur la validation v2, sous chaque condition. Des sondes réentraînées dans le jeu qu'elles lisent y voient la distinction au plafond sous toutes les conditions, l'échec construit compris (partie 3) ;",
     "une sonde apprise sur l'extraction, lue sur la validation v2, sous chaque condition, et c'est elle qui décide. Des sondes entraînées et testées dans un même jeu restaient au plafond sous toutes les conditions, l'échec construit compris (partie 3) ;"),
    ("  - **la méthode du rang change** ; sa définition détaillée est proposée (partie 2).",
     "  - **la méthode du rang change** : le rang minimal se mesure par effacement linéaire, et non plus par projection ; sa définition détaillée est proposée (parties 2 et 3)."),
    ("le transfert, lui, ne tombe au hasard, au dernier jeton, que sous l'effacement linéaire sur toutes les couches (0,497, contre 0,682 sans intervention) ;",
     "le transfert, lui, ne tombe, au dernier jeton, que sous l'effacement linéaire sur toutes les couches (0,497, contre 0,682 sans intervention et 0,687 sous un seul tirage du comparateur) ;"),
    ("aucun retrait ne fait tomber la lecture des sondes réentraînées ;", "aucun retrait ne fait tomber la lecture des sondes réentraînées dans le jeu qu'elles lisent ;"),
    ("sur la conduite, le même effacement (sur A100, KL 0,259) retire presque tout l'écart,",
     "sur la conduite, l'effacement sur toutes les couches, mesuré sur A100 (KL 0,259), retire presque tout l'écart,"),
]))
add(orig("d29-Q")); add(orig("E04")); add(orig("E05"))
add(custom(["A4-01", "E06"], E["E06"]["anchor"], "replace", M.VOCAB))
add(orig("E07")); add(orig("E08"))
# Partie 1
add(orig("E09"))
# Partie 2
add(mod("A4-02", [("Le changement vient des mesures du 5 et du 6 octobre : jusqu'au rang 16, sur toutes les couches, la projection laissait le transfert de « je suis évalué » entre 0,61 et 0,68 (0,682 sans intervention), quand une seule direction effacée par couche le faisait tomber à 0,497.",
                     "Le changement vient des mesures du 5 et du 6 octobre : jusqu'au rang 16, sur toutes les couches, la projection ne faisait pas tomber le transfert de « je suis évalué », quand une seule direction effacée par couche le faisait tomber (plus bas).")]))
add(orig("A4-03"))
add(mod("A4-04", [
    ("un tirage du comparateur, au même KL, le laisse à 0,687.", "un tirage du comparateur, à la même KL, le laisse à 0,687."),
    ("- **Une première mesure, exploratoire seulement** (6 octobre ;", "- **Une première mesure, exploratoire seulement** (5 et 6 octobre ;"),
    ("  - La charge de « je suis évalué » n'est pas mesurée,",
     "  - Le transfert de départ est modeste : 0,682.\n  - Sur la conduite, l'effacement entier sur toutes les couches ne bat pas un tirage du comparateur au même dommage : 52,8 points contre 53,6 (`organism_inhibition-20261005-115519-a006`, sur A100).\n  - La charge de « je suis évalué » n'est pas mesurée,"),
]))
add(orig("A4-05")); add(orig("A4-06")); add(orig("A4-07"))
# Partie 3
add(orig("E10")); add(orig("E11")); add(orig("E12"))
add(orig("T01")); add(orig("E13"))
add(custom(["A4-08"], E["A4-08"]["anchor"], "insert_after", M.A4_08))
add(orig("T02")); add(orig("T03"))
add(mod("T04", [("la projection résiduelle tombe sous 0,01.", "la projection résiduelle tombe sous 0,01 en moyenne sur les couches.")]))
add(orig("T05")); add(orig("T06")); add(orig("T07")); add(orig("T08"))
add(orig("A2-01")); add(orig("A2-02"))
add(orig("A4-09")); add(orig("A4-10"))
# Partie 4
add(orig("E14")); add(orig("E15")); add(orig("A4-11"))
add(orig("d29-A")); add(orig("d29-B")); add(orig("d29-C"))
add(custom(["d29-D", "A2 (notes : les 100 tirages sur une carte)"], E["d29-D"]["anchor"], "replace", M.D29_D))
add(orig("T09")); add(orig("d29-E")); add(orig("A2-03")); add(orig("T10")); add(orig("d29-F")); add(orig("E16"))
add(orig("A2-04")); add(orig("T11"))
add(orig("A4-12")); add(orig("A4-13")); add(orig("A4-14"))
add(orig("T12")); add(orig("T13"))
add(orig("A4-15")); add(orig("A4-16")); add(orig("A4-17"))
add(orig("T14"))
# Partie 5
add(orig("T15")); add(orig("d29-L"))
# Partie 6
add(orig("A4-18")); add(orig("A4-19"))
add(custom(["d29-G", "A2-05", "T16"], M.ROW1_OLD, "replace", M.ROW1_NEW))
add(orig("E17")); add(orig("T17")); add(orig("d29-H"))
add(orig("A4-20")); add(orig("T18")); add(orig("A4-21"))
# Partie 7
add(mod("A2-06", [
    ("Sur deux machines H100, sous deux pilotes, quatre runs ont donné les mêmes (le 4 et le 6 octobre).",
     "Sur deux machines H100, sous deux pilotes, quatre runs ont donné les mêmes (le 4 et le 6 octobre). La conduite gloutonne de l'organisme change de même : sans intervention, son écart d'extraction est de 55,2 points sur A100 (`…-115519-a006`), de 54,4 sur H100 (`organism_inhibition-20261004-101821-ada0`, `…-141318-194c`, `…-141323-faa0`)."),
]))
add(custom(["A2-07", "d29-J"], E["A2-07"]["anchor"], "replace", E["A2-07"]["new_text"] + "\n" + E["d29-J"]["new_text"]))
add(orig("T20")); add(orig("A4-22")); add(orig("T19"))
add(orig("d29-I")); add(orig("A2-08")); add(orig("E18"))
# Partie 8
add(orig("E19")); add(orig("A2-09")); add(orig("T21")); add(orig("d29-K")); add(orig("A4-23"))
# Partie 9
add(orig("A2-10")); add(orig("d29-M")); add(orig("A4-24")); add(orig("A4-25"))
add(orig("E20")); add(orig("E21")); add(orig("E22"))
add(custom(["cohérence (E22, E29) : la relecture de la semaine 1"],
    "Celle de la v1.5 demande à Lazar, à grands traits : la relecture de la v1.5 (de 4 à 6 heures)", "replace",
    "Celle de la v1.5 demande à Lazar, à grands traits : la relecture du programme, désormais la v1.6 (de 4 à 6 heures)"))
# Partie 10
add(orig("T22")); add(orig("A4-26")); add(orig("T23")); add(orig("A4-27"))
# Partie 11
assert E["A4-28"]["anchor"] == E["A2-11"]["anchor"]
add(custom(["A4-28", "A2-11"], E["A4-28"]["anchor"], "insert_after", E["A4-28"]["new_text"] + "\n" + E["A2-11"]["new_text"]))
add(orig("E23"))
# Partie 12
add(orig("E24")); add(orig("E25"))
add(custom(["A2 (notes : la ligne du calcul)"], M.CALC_OLD, "replace", M.CALC_NEW))
add(orig("E26"))
e27 = mod("E27", [("la méthode du rang choisie. La lecture de la v1.6 est donnée plus bas",
                   "la méthode du rang changée (sa définition détaillée, proposée). La lecture de la v1.6 est donnée plus bas")])
add(custom(["d29-N", "E27"], E["d29-N"]["anchor"], "replace", E["d29-N"]["new_text"] + "\n" + e27["new_text"]))
add(custom(["cohérence (E28) : la lecture de la décision 26"],
    "**Comment cette version lit le « toutes, telles que proposées » de la décision 26.**", "replace",
    "**Comment la v1.5 lit le « toutes, telles que proposées » de la décision 26.**"))
add(orig("E28")); add(orig("E29")); add(orig("E30")); add(orig("E31"))
add(custom(["E32", "d29-O"], E["E32"]["anchor"], "replace", M.PT17_20))
add(orig("E33")); add(orig("E34"))
# Annexe 1
add(orig("T24")); add(orig("d29-P"))
add(custom(["A4 (notes : la grille, annexe 1)"], M.GRILLE_OLD, "replace", M.GRILLE_NEW))
add(orig("T25"))
# Annexe 3
add(custom(["E35"], E["E35"]["anchor"], "replace", M.ANNEXE3))

# ---------------------------------------------------------------- application
text = open(SRC, encoding="utf-8").read()
log = []
for op in OPS:
    a, mode, new = op["anchor"], op["mode"], op["new_text"]
    n = text.count(a)
    if n != 1:
        sys.exit(f"ÉCHEC {op['id']} : ancre trouvée {n} fois")
    i = text.index(a)
    if mode == "replace":
        text = text[:i] + new + text[i + len(a):]
    elif mode == "insert_after":
        j = i + len(a)
        assert text[j] == "\n", (op["id"], "l'ancre ne finit pas sa ligne")
        text = text[:j] + "\n" + new + text[j:]
    elif mode == "insert_before":
        assert i == 0 or text[i - 1] == "\n", (op["id"], "l'ancre ne commence pas sa ligne")
        text = text[:i] + new + "\n" + text[i:]
    else:
        sys.exit(f"mode inconnu {mode}")
    log.append(op["id"])

open(DST, "w", encoding="utf-8").write(text)

used = set()
for x in log:
    for part in x.split("+"):
        used.add(part)
missing = sorted(k for k in E if k not in used)
print(f"{len(log)} opérations appliquées ; éditions d'origine non utilisées : {missing}")
print("lignes :", text.count("\n") + (0 if text.endswith("\n") else 1))
