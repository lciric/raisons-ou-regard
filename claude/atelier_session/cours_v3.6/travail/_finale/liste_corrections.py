#!/usr/bin/env python3
"""Liste des corrections appliquées : groupe, n°, langue, ligne d'arrivée dans la v3.6 corrigée, nature, tranche, extrait (lecture seule)."""
import json, glob, os, re, sys
sys.path.insert(0, '/tmp/claude-0/-home-user-sycophancy-construct-validity/332d478c-da90-5795-bb10-27657d88c4d0/scratchpad/cours_v36/outils')
import appliquer as A
txt = {k: open(v, encoding='utf8').read() for k, v in A.OUT.items()}
cmp = json.load(open(f'{A.TRAV}/_finale/comptes_par_tranche.json'))
import subprocess
def tranche_map(fi):
    a = open(A.SRC[fi], encoding='utf8').read().split('\n')
    out = subprocess.run(['diff', A.SRC[fi], A.OUT[fi]], capture_output=True, text=True).stdout
    m = {}
    for g in re.finditer(r'(?m)^(\d+)a(\d+)(?:,(\d+))?$', out):
        na, s, e = int(g.group(1)), int(g.group(2)), int(g.group(3) or g.group(2))
        i = na - 1
        while i >= 0 and not a[i].strip(): i -= 1
        t = next(t for t, d in A.TRANCHES.items() if d[fi][0] - 1 <= i <= d[fi][1] - 1)
        for k in range(s, e + 1): m[k] = t
    return m
TM = {fi: tranche_map(fi) for fi in ('FR', 'EN')}
def nature(l):
    if re.match(r'^> \*\*⚠ ', l) or re.match(r'^>\s*(- \*\*(Limite :|Limit:)|\s+\*\*(Parade :|Workaround:))', l): return 'encadré'
    if re.match(r'^> ⚠ \*\*', l): return 'renvoi'
    if re.match(r'^> ⚠ \*\(v3\.6\)\*', l): return 'avertissement'
    return 'autre'
rows = []
for f in sorted(glob.glob(f'{A.TRAV}/corrections_*.json')):
    d = json.load(open(f, encoding='utf8'))
    for n, c in enumerate(d['corrections'], 1):
        fi, nou = c['fichier'], c['nouveau']
        pos = txt[fi].index(nou)
        line = txt[fi].count('\n', 0, pos) + 1
        first = nou.split('\n')[0]
        L = txt[fi].split('\n')
        # nature : de la ligne d'arrivée ; si ligne de corps d'encadré, encadré
        nat = nature(L[line - 1])
        if nat == 'autre':
            # morceau de l'encadré du 2 octobre ou note d'ouverture ?
            k = line - 1
            while k > 0 and L[k].startswith('>') and '★' not in L[k] and 'ce qui s\'ajoute' not in L[k] and 'what is added' not in L[k]: k -= 1
            nat = 'morceau du 2 octobre' if '★' in L[k] else ('note d\'ouverture' if line < 40 else 'autre')
        rows.append((os.path.basename(f).replace('corrections_', '').replace('.json', ''), n, fi, line, TM[fi].get(line, '?'), nat, re.sub(r'\s+', ' ', first)[:95]))
import collections
print(collections.Counter((r[5]) for r in rows))
print(collections.Counter((r[0], r[2]) for r in rows))
json.dump(rows, open(f'{A.TRAV}/_finale/corrections_appliquees.json', 'w'), ensure_ascii=False, indent=0)
for r in rows[:6]: print(r)
