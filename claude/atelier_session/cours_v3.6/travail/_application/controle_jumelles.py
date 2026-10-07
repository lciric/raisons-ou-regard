#!/usr/bin/env python3
"""Contrôle des jumelles FR/EN et de l'emplacement des insertions (lecture seule : ne modifie rien)."""
import json, glob, os, re, sys, collections
W = '/tmp/claude-0/-home-user-sycophancy-construct-validity/332d478c-da90-5795-bb10-27657d88c4d0/scratchpad/cours_v36'
sys.path.insert(0, f'{W}/outils')
import importlib.util
spec = importlib.util.spec_from_file_location('appliquer', f'{W}/outils/appliquer.py')
ap = importlib.util.module_from_spec(spec); spec.loader.exec_module(ap)
TR = ap.TRANCHES
L = {k: open(v, encoding='utf8').read().split('\n') for k, v in ap.SRC.items()}

def kind(line):
    s = line.strip()
    if not s: return 'blank'
    if s.startswith('```'): return 'fence'
    if s.startswith('#'): return 'heading'
    if s.startswith('|'): return 'table'
    if s.startswith('>'): return 'quote'
    if re.match(r'^\s*([-*+]|\d+[.)])\s', line): return 'list'
    if re.match(r'^\s{2,}\S', line): return 'indent'
    if re.match(r'^(-{3,}|\*{3,}|_{3,})$', s): return 'rule'
    return 'text'

def typ(t, fi):
    first = t.strip().split('\n')[0]
    if '★' in first: return 'encadre_2oct'
    if fi == 'FR':
        if first.startswith('> **⚠ Limites et parades —'): return 'encadre_limites'
        if first.startswith('> ⚠ **Limites et parades**'): return 'renvoi'
        if first.startswith('> ⚠ *(v3.6)*'): return 'ponctuel'
    else:
        if first.startswith('> **⚠ Limits and workarounds —'): return 'encadre_limites'
        if first.startswith('> ⚠ **Limits and workarounds**'): return 'renvoi'
        if first.startswith('> ⚠ *(v3.6)*'): return 'ponctuel'
    return 'autre:' + first[:60]

def nums(t, fi):
    t = t.replace(' ', ' ').replace(' ', ' ')
    if fi == 'FR':
        t = re.sub(r'(?<=\d) (?=\d{3}\b)', '', t)          # 1 000 -> 1000
        t = re.sub(r'(?<=\d),(?=\d)', '.', t)              # 0,62 -> 0.62
    else:
        t = re.sub(r'(?<=\d),(?=\d{3}\b)', '', t)          # 1,000 -> 1000
    return sorted(re.findall(r'\d+(?:\.\d+)?', t))

def heading_ctx(fi, i):
    # titre le plus proche au-dessus, et ses identifiants
    for j in range(i, -1, -1):
        if L[fi][j].startswith('#'):
            h = L[fi][j]
            ids = re.findall(r'F·\d+|Q\d+|M\d+|§\s?\w+|\b[A-I]\b(?= ·|\.| bis)|C bis|\b\d+\b', h)
            return j + 1, h, ids
    return 0, '', []

def para_start(fi, i):
    j = i
    while j > 0 and L[fi][j - 1].strip():
        j -= 1
    return j

out = []
alerts = []
total = collections.Counter()
for f in sorted(glob.glob(f'{W}/travail/insertions_*.json')):
    d = json.load(open(f, encoding='utf8'))
    tr = d['tranche']
    per = {'FR': [], 'EN': []}
    for n, ins in enumerate(d['insertions'], 1):
        fi = ins['fichier']; a, b = TR[tr][fi]
        idx = [i for i in range(a - 1, min(b, len(L[fi]))) if L[fi][i].strip() == ins['ancre'].strip()]
        assert len(idx) == 1, (tr, n)
        i = idx[0]
        t = ins['texte']
        # emplacement
        anc_k = kind(L[fi][i]); nxt = L[fi][i + 1] if i + 1 < len(L[fi]) else ''
        nxt_k = kind(nxt)
        fences = sum(1 for x in L[fi][:i + 1] if x.strip().startswith('```'))
        place = []
        if fences % 2 == 1: place.append('DANS_BLOC_CODE')
        if anc_k != 'blank' and nxt_k not in ('blank', 'heading'):
            place.append(f'COUPE_{anc_k}->{nxt_k}')
        ps = para_start(fi, i)
        head = L[fi][ps].strip()
        dire = ('**À dire' in head or '**À ne pas dire' in head) if fi == 'FR' else ('**What to say' in head or '**What not to say' in head)
        if dire:
            place.append('APRES_A_DIRE' if nxt_k in ('blank', 'heading') else 'DANS_A_DIRE')
        hl, h, ids = heading_ctx(fi, i)
        per[fi].append(dict(n=n, line=i + 1, rel=(i + 1 - a) / max(1, b - a), typ=typ(t, fi), nl=len(t.rstrip().split('\n')),
                            lim=len(re.findall(r'\*\*Limite ?:\*\*' if fi == 'FR' else r'\*\*Limit:\*\*', t)),
                            par=len(re.findall(r'\*\*Parade ?:\*\*' if fi == 'FR' else r'\*\*Workaround:\*\*', t)),
                            none=len(re.findall(r'aucune (?:parade )?connue' if fi == 'FR' else r'none known|no workaround(?: is)? known|no known workaround', t)),
                            nums=nums(t, fi), place=place, hl=hl, h=h, ids=ids, first=t.strip().split('\n')[0]))
        total[(tr, fi)] += 1
    nF, nE = len(per['FR']), len(per['EN'])
    out.append(f'## {tr} : FR {nF}, EN {nE}')
    for k in range(max(nF, nE)):
        F = per['FR'][k] if k < nF else None
        E = per['EN'][k] if k < nE else None
        if not F or not E:
            alerts.append(f'{tr} paire {k+1}: jumelle manquante'); continue
        pb = []
        if F['typ'] != E['typ']: pb.append(f"type {F['typ']} / {E['typ']}")
        if F['nl'] != E['nl']: pb.append(f"lignes {F['nl']} / {E['nl']}")
        if (F['lim'], F['par'], F['none']) != (E['lim'], E['par'], E['none']): pb.append(f"limites/parades/aucune {F['lim']},{F['par']},{F['none']} / {E['lim']},{E['par']},{E['none']}")
        if F['nums'] != E['nums']:
            cf, ce = collections.Counter(F['nums']), collections.Counter(E['nums'])
            pb.append(f"nombres FR-seulement {sorted((cf-ce).elements())} EN-seulement {sorted((ce-cf).elements())}")
        if abs(F['rel'] - E['rel']) > 0.08: pb.append(f"position relative {F['rel']:.2f} / {E['rel']:.2f}")
        idsF = [x for x in F['ids'] if not x.isdigit()]; idsE = [x for x in E['ids'] if not x.isdigit()]
        if idsF != idsE: pb.append(f"identifiants du titre {idsF} / {idsE}")
        for P, lab in ((F, 'FR'), (E, 'EN')):
            if P['place']: pb.append(f"emplacement {lab} {P['place']}")
        line = f"- paire {k+1} (n°{F['n']} FR l.{F['line']} / n°{E['n']} EN l.{E['line']}) [{F['typ']}] titre FR l.{F['hl']} « {F['h'][:70]} » / EN l.{E['hl']} « {E['h'][:70]} »"
        if pb:
            line += '\n    ' + '\n    '.join(pb)
            alerts.append(f'{tr} paire {k+1} (FR l.{F["line"]}, EN l.{E["line"]}): ' + ' ; '.join(pb))
        out.append(line)
open(f'{W}/travail/_application/controle_jumelles.txt', 'w', encoding='utf8').write('\n'.join(out) + '\n')
open(f'{W}/travail/_application/controle_alertes.txt', 'w', encoding='utf8').write('\n'.join(alerts) + '\n')
print('paires examinées, alertes :', len(alerts))
c = collections.Counter()
for a_ in alerts:
    for key in ('type', 'lignes', 'limites/parades', 'nombres', 'position relative', 'identifiants', 'COUPE', 'DANS_BLOC_CODE', 'A_DIRE', 'manquante'):
        if key in a_: c[key] += 1
print(c)
