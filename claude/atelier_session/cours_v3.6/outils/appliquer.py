#!/usr/bin/env python3
"""Applique au cours v3.5 les insertions des agents, puis leurs corrections, et écrit la v3.6.

Usage :
  python3 appliquer.py insertions    # source v3.5 + travail/insertions_*.json -> livrable v3.6 (repart toujours de la v3.5)
  python3 appliquer.py corrections   # livrable v3.6 + travail/corrections_*.json -> livrable v3.6 corrigé
  python3 appliquer.py tranches      # imprime les tranches (lignes de la v3.5)

Format d'un fichier travail/insertions_<tranche>.json :
  {"tranche": "<cle>", "insertions": [{"fichier": "FR"|"EN", "ancre": "<ligne exacte de la v3.5, dans la tranche>", "texte": "<markdown>"}]}
  Le texte s'insère juste après la ligne d'ancrage, entouré de lignes vides. L'ancre doit apparaître une seule fois dans la tranche
  (comparaison après suppression des espaces de début et de fin).
Format d'un fichier travail/corrections_<nom>.json :
  {"corrections": [{"fichier": "FR"|"EN", "ancien": "<texte exact, présent une seule fois dans la v3.6>", "nouveau": "<texte>"}]}
"""
import glob, json, os, sys

W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = {'FR': f'{W}/source/COURS_Alignment_v3.5_FR_2026-09-27.md', 'EN': f'{W}/source/COURS_Alignment_v3.5_EN_2026-09-27.md'}
OUT = {'FR': f'{W}/livrable/COURS_Alignment_v3.6_FR_2026-10-02.md', 'EN': f'{W}/livrable/COURS_Alignment_v3.6_EN_2026-10-02.md'}
TRAV = f'{W}/travail'

# Tranches : (début, fin) inclus, en lignes de la v3.5 (base 1)
TRANCHES = {
    'tete_volet1':       {'FR': (1, 181),     'EN': (1, 248)},
    'volet_M':           {'FR': (182, 411),   'EN': (249, 496)},
    'volet2_A_a_D':      {'FR': (412, 666),   'EN': (497, 755)},
    'volet2_E_a_I':      {'FR': (667, 884),   'EN': (756, 1006)},
    'volet3':            {'FR': (885, 1110),  'EN': (1007, 1251)},
    'volets4_5_entete':  {'FR': (1111, 1368), 'EN': (1252, 1563)},
    'volet6':            {'FR': (1369, 1626), 'EN': (1564, 1791)},
    'volet7_B_et_D':     {'FR': (1627, 2069), 'EN': (1792, 2203)},
    'volet7_A_et_C':     {'FR': (2070, 2665), 'EN': (2204, 2803)},
    'volets8_9':         {'FR': (2666, 2935), 'EN': (2804, 3178)},
    'volet10':           {'FR': (2936, 3655), 'EN': (3179, 3894)},
    'volet11_1_a_20':    {'FR': (3656, 4128), 'EN': (3895, 4403)},
    'volet11_21_a_52':   {'FR': (4129, 4729), 'EN': (4404, 5037)},
    'volet11_53_et_fin': {'FR': (4730, 5377), 'EN': (5038, 5702)},
}


def norm(s):
    return s.strip()


def insertions():
    lignes = {k: open(v, encoding='utf8').read().split('\n') for k, v in SRC.items()}
    a_inserer = {'FR': [], 'EN': []}
    rapport, extraits = [], {}
    for f in sorted(glob.glob(f'{TRAV}/insertions_*.json')):
        try:
            d = json.load(open(f, encoding='utf8'))
        except Exception as e:
            rapport.append(f'- {os.path.basename(f)} : JSON illisible ({e})')
            continue
        tr = d.get('tranche')
        if tr not in TRANCHES:
            rapport.append(f'- {os.path.basename(f)} : tranche inconnue « {tr} »')
            continue
        ok = ko = 0
        for n, ins in enumerate(d.get('insertions', []), 1):
            fi, ancre, texte = ins.get('fichier'), ins.get('ancre', ''), ins.get('texte', '')
            if fi not in ('FR', 'EN') or not norm(ancre) or not texte.strip():
                rapport.append(f'- {tr} n°{n} : entrée incomplète'); ko += 1; continue
            a, b = TRANCHES[tr][fi]
            idx = [i for i in range(a - 1, min(b, len(lignes[fi]))) if norm(lignes[fi][i]) == norm(ancre)]
            if len(idx) != 1:
                rapport.append(f'- {tr} n°{n} ({fi}) : ancre trouvée {len(idx)} fois dans la tranche {a}-{b} : « {ancre[:120]} »'
                               + (f' (lignes {", ".join(str(i + 1) for i in idx[:8])})' if idx else ''))
                ko += 1; continue
            a_inserer[fi].append((idx[0], len(a_inserer[fi]), texte.rstrip()))
            extraits.setdefault((tr, fi), []).append(f'### Insertion n°{n}, après la ligne {idx[0] + 1} de la v3.5\n\n> Ancre : {ancre.strip()[:300]}\n\n{texte.rstrip()}\n')
            ok += 1
        rapport.append(f'- {tr} : {ok} insertion(s) appliquée(s), {ko} en échec')
    for fi in ('FR', 'EN'):
        L = lignes[fi]
        for i, _, texte in sorted(a_inserer[fi], key=lambda x: (x[0], x[1]), reverse=True):
            L[i + 1:i + 1] = [''] + texte.split('\n') + ['']
        open(OUT[fi], 'w', encoding='utf8').write('\n'.join(L))
    for (tr, fi), blocs in extraits.items():
        open(f'{TRAV}/applique_{tr}_{fi}.md', 'w', encoding='utf8').write(f'# Insertions appliquées — {tr} — {fi}\n\n' + '\n'.join(blocs))
    open(f'{TRAV}/rapport_application.md', 'w', encoding='utf8').write('# Rapport d\'application des insertions\n\n' + '\n'.join(rapport) + '\n')
    print('\n'.join(rapport))


def corrections():
    txt = {k: open(v, encoding='utf8').read() for k, v in OUT.items()}
    rapport = []
    for f in sorted(glob.glob(f'{TRAV}/corrections_*.json')):
        try:
            d = json.load(open(f, encoding='utf8'))
        except Exception as e:
            rapport.append(f'- {os.path.basename(f)} : JSON illisible ({e})'); continue
        ok = ko = 0
        for n, c in enumerate(d.get('corrections', []), 1):
            fi, anc, nou = c.get('fichier'), c.get('ancien', ''), c.get('nouveau', '')
            if fi not in txt or not anc:
                rapport.append(f'- {os.path.basename(f)} n°{n} : entrée incomplète'); ko += 1; continue
            k = txt[fi].count(anc)
            if k != 1:
                rapport.append(f'- {os.path.basename(f)} n°{n} ({fi}) : texte trouvé {k} fois : « {anc[:120]} »'); ko += 1; continue
            txt[fi] = txt[fi].replace(anc, nou); ok += 1
        rapport.append(f'- {os.path.basename(f)} : {ok} correction(s) appliquée(s), {ko} en échec')
    for fi, t in txt.items():
        open(OUT[fi], 'w', encoding='utf8').write(t)
    open(f'{TRAV}/rapport_corrections.md', 'a', encoding='utf8').write('# Rapport des corrections\n\n' + '\n'.join(rapport) + '\n\n')
    print('\n'.join(rapport))


def integrite():
    """Vérifie que chaque ligne de la v3.5 se retrouve, dans l'ordre et inchangée, dans la v3.6 (on n'a fait qu'ajouter)."""
    ok = True
    for fi in ('FR', 'EN'):
        a = open(SRC[fi], encoding='utf8').read().split('\n')
        b = open(OUT[fi], encoding='utf8').read().split('\n')
        j = 0
        manquantes = []
        for i, l in enumerate(a):
            while j < len(b) and b[j] != l:
                j += 1
            if j == len(b):
                manquantes.append(i + 1)
                j = 0
                # on repart du début pour ne pas masquer d'autres manques ; le compte reste indicatif
            else:
                j += 1
        print(f'{fi} : {len(a)} lignes v3.5, {len(b)} lignes v3.6, {len(b) - len(a)} ajoutées ; lignes v3.5 introuvables dans l\'ordre : '
              + (', '.join(map(str, manquantes[:20])) + (' …' if len(manquantes) > 20 else '') if manquantes else 'aucune'))
        ok = ok and not manquantes
    print('INTÉGRITÉ : OK' if ok else 'INTÉGRITÉ : ÉCHEC')


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd == 'insertions':
        insertions()
    elif cmd == 'corrections':
        corrections()
    elif cmd == 'integrite':
        integrite()
    elif cmd == 'tranches':
        for k, v in TRANCHES.items():
            print(k, v)
    else:
        print(__doc__)
