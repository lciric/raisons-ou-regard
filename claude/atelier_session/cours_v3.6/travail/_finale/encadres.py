#!/usr/bin/env python3
"""Inventaire des 27 encadrés « Limites et parades » (lecture seule) : titre, ligne, section, limites, parades, « aucune connue »."""
import re, json, sys
sys.path.insert(0, '/tmp/claude-0/-home-user-sycophancy-construct-validity/332d478c-da90-5795-bb10-27657d88c4d0/scratchpad/cours_v36/outils')
import appliquer as A
T = {'FR': (r'^> \*\*⚠ Limites et parades — (.*?)\*\* \*\((.*?)\)\*\s*$', r'^>\s*- \*\*Limite :\*\*', r'^>\s+\*\*Parade :\*\*', r'\*\*Parade :\*\* aucune connue'),
     'EN': (r'^> \*\*⚠ Limits and workarounds — (.*?)\*\* \*\((.*?)\)\*\s*$', r'^>\s*- \*\*Limit:\*\*', r'^>\s+\*\*Workaround:\*\*', r'\*\*Workaround:\*\* none known')}
out = {}
for fi in ('FR', 'EN'):
    L = open(A.OUT[fi], encoding='utf8').read().split('\n')
    tit, lim, par, none = (re.compile(x) for x in T[fi])
    boxes = []
    for i, l in enumerate(L):
        m = tit.match(l)
        if not m: continue
        j = i + 1; body = []
        while j < len(L) and L[j].startswith('>'):
            body.append(L[j]); j += 1
        # section : dernier titre markdown qui précède
        h = next((L[k] for k in range(i - 1, -1, -1) if re.match(r'^#{1,4} ', L[k])), '')
        nl = sum(1 for b in body if lim.match(b)); npar = sum(1 for b in body if par.match(b)); nn = sum(1 for b in body if none.search(b))
        # limites dont la parade est « aucune connue » : texte de la limite (début)
        sans = []
        for k, b in enumerate(body):
            if none.search(b):
                prev = next((body[x] for x in range(k, -1, -1) if lim.match(body[x])), '')
                sans.append(re.sub(r'^>\s*- \*\*(Limite :|Limit:)\*\*\s*', '', prev)[:160])
        # lignes du corps hors format (ni vide, ni Limite, ni Parade)
        hors = [b for b in body if b.strip() not in ('>',) and not lim.match(b) and not par.match(b)]
        boxes.append({'ligne': i + 1, 'instrument': m.group(1), 'date': m.group(2), 'section': h[:110], 'limites': nl, 'parades': npar, 'aucune': nn, 'sans_parade': sans, 'hors_format': hors[:3], 'fin': j})
    out[fi] = boxes
    print(f'== {fi} : {len(boxes)} encadrés')
    for b in boxes:
        print(f"{b['ligne']:>5} | {b['instrument'][:55]:<55} | L{b['limites']} P{b['parades']} N{b['aucune']} | {b['date']} | {b['section'][:70]}")
        for h in b['hors_format']: print('        hors format :', h[:140])
json.dump(out, open('/tmp/claude-0/-home-user-sycophancy-construct-validity/332d478c-da90-5795-bb10-27657d88c4d0/scratchpad/cours_v36/travail/_finale/encadres.json', 'w'), ensure_ascii=False, indent=1)
print('\n== parité FR/EN, encadré par encadré (même rang)')
for k, (f, e) in enumerate(zip(out['FR'], out['EN']), 1):
    flag = '' if (f['limites'], f['parades'], f['aucune']) == (e['limites'], e['parades'], e['aucune']) else '  <-- ÉCART'
    print(f"{k:>2}. {f['instrument'][:45]:<45} / {e['instrument'][:45]:<45} L{f['limites']}/{e['limites']} P{f['parades']}/{e['parades']} N{f['aucune']}/{e['aucune']}{flag}")
