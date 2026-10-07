#!/usr/bin/env python3
"""Simulation à blanc des corrections (lecture seule) : même ordre que appliquer.py, sur une copie en mémoire."""
import glob, json, os, sys
W = '/tmp/claude-0/-home-user-sycophancy-construct-validity/332d478c-da90-5795-bb10-27657d88c4d0/scratchpad/cours_v36'
SRC = {'FR': f'{W}/source/COURS_Alignment_v3.5_FR_2026-09-27.md', 'EN': f'{W}/source/COURS_Alignment_v3.5_EN_2026-09-27.md'}
OUT = {'FR': f'{W}/livrable/COURS_Alignment_v3.6_FR_2026-10-02.md', 'EN': f'{W}/livrable/COURS_Alignment_v3.6_EN_2026-10-02.md'}
base = sys.argv[1] if len(sys.argv) > 1 else None
txt = {k: open(base.replace('XX', k) if base else v, encoding='utf8').read() for k, v in OUT.items()}
src = {k: open(v, encoding='utf8').read() for k, v in SRC.items()}
srclines = {k: set(v.split('\n')) for k, v in src.items()}
pattern = sys.argv[2] if len(sys.argv) > 2 else f'{W}/travail/corrections_*.json'
for f in sorted(glob.glob(pattern)):
    d = json.load(open(f, encoding='utf8'))
    ok = ko = 0
    for n, c in enumerate(d.get('corrections', []), 1):
        fi, anc, nou = c.get('fichier'), c.get('ancien', ''), c.get('nouveau', '')
        k = txt[fi].count(anc)
        insrc = src[fi].count(anc)
        # lignes de la v3.5 touchées : une ligne entière de l'ancien qui est une ligne de la v3.5 et disparaît
        touche = [l for l in anc.split('\n') if l.strip() and l in srclines[fi] and l not in nou.split('\n')]
        flag = ''
        if insrc: flag += f' [ancien présent {insrc} fois dans la v3.5]'
        if touche: flag += f' [lignes v3.5 retirées : {len(touche)}]'
        if k != 1:
            print(f'ÉCHEC {os.path.basename(f)} n°{n} ({fi}) : trouvé {k} fois : « {anc[:150]} »{flag}'); ko += 1; continue
        txt[fi] = txt[fi].replace(anc, nou); ok += 1
        if flag: print(f'ALERTE {os.path.basename(f)} n°{n} ({fi}){flag}')
    print(f'- {os.path.basename(f)} : {ok} appliquée(s), {ko} en échec')
for fi in ('FR', 'EN'):
    a = src[fi].split('\n'); b = txt[fi].split('\n'); j = 0; man = []
    for i, l in enumerate(a):
        while j < len(b) and b[j] != l: j += 1
        if j == len(b): man.append(i + 1); j = 0
        else: j += 1
    print(f'{fi} : {len(a)} lignes v3.5, {len(b)} lignes simulées ; manquantes : {man[:20] if man else "aucune"}')
