#!/usr/bin/env python3
"""Contrôle des renvois sur la v3.6 corrigée (lecture seule) : chaque entrée « instrument → endroit » doit donner l'endroit
de l'index de la note d'ouverture pour cet instrument ; libellés précisés (« dont… », encadré du 2 octobre) signalés à part."""
import re, sys, collections
sys.path.insert(0, '/tmp/claude-0/-home-user-sycophancy-construct-validity/332d478c-da90-5795-bb10-27657d88c4d0/scratchpad/cours_v36/outils')
import appliquer as A
CFG = {'FR': (r'^> ⚠ \*\*Limites et parades\*\* : (.*?) \*\(v3\.6\)\*\s*$', ' ; ', ' → '),
       'EN': (r'^> ⚠ \*\*Limits and workarounds\*\*: (.*?) \*\(v3\.6\)\*\s*$', '; ', ' → ')}
for fi in ('FR', 'EN'):
    L = open(A.OUT[fi], encoding='utf8').read().split('\n')
    rx, sep, arr = CFG[fi]
    lines = [(i, re.match(rx, l)) for i, l in enumerate(L) if re.match(r'^> ⚠ \*\*(Limites et parades\*\* :|Limits and workarounds\*\*:)', l)]
    bad_format = [i + 1 for i, m in lines if not m]
    # l'index = les 4 premières lignes (note d'ouverture)
    idx = {}
    for i, m in lines[:4]:
        for e in m.group(1).split(sep):
            ins, loc = e.split(arr, 1); idx[ins.strip()] = loc.strip()
    n_entries = 0; mism = []; labelled = collections.Counter(); unknown = []
    for i, m in lines[4:]:
        if not m: continue
        # découpe : sur le séparateur, puis on recolle à la précédente toute pièce sans flèche
        parts = []
        for piece in m.group(1).split(sep):
            if parts and arr not in piece: parts[-1] += sep + piece
            else: parts.append(piece)
        for e in parts:
            n_entries += 1
            if arr not in e: unknown.append((i + 1, e[:100])); continue
            ins, loc = e.split(arr, 1); ins, loc = ins.strip(), loc.strip()
            if ins in idx:
                if loc != idx[ins]: mism.append((i + 1, ins, loc[:90], idx[ins][:90]))
            else:
                base = next((k2 for k2 in sorted(idx, key=len, reverse=True) if ins.startswith(k2)), None)
                labelled[ins] += 1
                if base and not loc.startswith(idx[base].split(' (')[0]):
                    mism.append((i + 1, ins, loc[:90], idx[base][:90]))
    print(f'== {fi} : {len(lines)} lignes au format de renvoi (dont 4 lignes d’index) ; {len(idx)} instruments dans l’index ; {n_entries} entrées hors index')
    print('   format non conforme :', bad_format or 'aucun')
    print('   endroit différent de l’index :', len(mism)); [print('    ', x) for x in mism[:15]]
    print('   entrées sans flèche :', unknown[:5] or 'aucune')
    print('   libellés précisés (hors index) :', sum(labelled.values()))
    for k2, v in labelled.most_common(): print(f'     {v} × {k2[:110]}')
