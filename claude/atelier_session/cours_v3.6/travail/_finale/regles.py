#!/usr/bin/env python3
"""Contrôles mécaniques des règles sur le seul texte ajouté de la v3.6 corrigée (lecture seule)."""
import re, sys, subprocess, collections
sys.path.insert(0, '/tmp/claude-0/-home-user-sycophancy-construct-validity/332d478c-da90-5795-bb10-27657d88c4d0/scratchpad/cours_v36/outils')
import appliquer as A
ALLOW = {'SFT', 'RL', 'DPO', 'LORA', 'LoRA', 'GPU', 'AUROC', 'SAE', 'SAEs', 'CoT', 'NLA', 'NLAs'}
for fi in ('FR', 'EN'):
    a = open(A.SRC[fi], encoding='utf8').read()
    b = open(A.OUT[fi], encoding='utf8').read().split('\n')
    out = subprocess.run(['diff', A.SRC[fi], A.OUT[fi]], capture_output=True, text=True).stdout
    blocks = []
    for m in re.finditer(r'(?m)^(\d+)a(\d+)(?:,(\d+))?$', out):
        s, e = int(m.group(2)), int(m.group(3) or m.group(2))
        blocks.append((s, e))
    # un bloc de diff peut contenir plusieurs insertions (même ancre) : on découpe sur les lignes vides
    units = []
    for s, e in blocks:
        cur = []
        for k in range(s - 1, e):
            if b[k].strip(): cur.append(k)
            elif cur: units.append(cur); cur = []
        if cur: units.append(cur)
    # regroupe les paragraphes d'un même bloc de citation : une unité = suite de lignes '>' contiguës hors lignes vides
    print(f'== {fi} : {len(blocks)} blocs ajoutés, {len(units)} paragraphes ajoutés')
    # 1. mention de version ou date, par bloc de diff
    sans = []
    for s, e in blocks:
        t = '\n'.join(b[s - 1:e])
        if '(v3.6' not in t and '2 octobre 2026' not in t and '2 October 2026' not in t:
            sans.append((s, b[s][:80] if s < len(b) else ''))
    print('  blocs sans « (v3.6 » ni date :', len(sans), sans[:5])
    added = [(k, b[k]) for s, e in blocks for k in range(s - 1, e)]
    # 2. revendications de priorité
    pri = [(k + 1, l[:160]) for k, l in added if re.search(r'\bfirst\b|\bpremi(er|ère)s?\b', l, re.I)]
    print('  lignes avec « first » / « premier » :', len(pri))
    for x in pri: print('    ', x)
    # 3. citations de quinze mots ou plus
    longq = []
    for k, l in added:
        for q in re.findall(r'«\s*([^»]+?)\s*»|“([^”]+)”|"([^"]+)"', l):
            q = next(x for x in q if x)
            n = len(re.findall(r"[\w’'-]+", q))
            if n >= 15: longq.append((k + 1, n, q[:120]))
    print('  citations de 15 mots ou plus :', len(longq))
    for x in longq[:30]: print('    ', x)
    # 4. aléatoire / random sans « même norme » dans la ligne
    rnd = [(k + 1, l[:200]) for k, l in added if re.search(r'aléatoire|\brandom', l, re.I) and not re.search(r'même norme|matched[- ]norm|same norm|norme égale|equal norm', l, re.I)]
    print('  lignes « aléatoire/random » sans « même norme » :', len(rnd))
    json_out = open(f'{A.TRAV}/_finale/aleatoire_{fi}.txt', 'w', encoding='utf8'); json_out.write('\n'.join(f'{k}: {l}' for k, l in rnd)); json_out.close()
    # 5. sigles absents de la v3.5 et de la liste permise
    sig = collections.Counter()
    for k, l in added:
        for w in re.findall(r'\b[A-Z][A-Z0-9]{1,6}s?\b', l):
            if w in ALLOW or re.search(r'\b' + re.escape(w) + r'\b', a): continue
            sig[w] += 1
    print('  sigles absents de la v3.5 (hors liste permise) :', dict(sig))
