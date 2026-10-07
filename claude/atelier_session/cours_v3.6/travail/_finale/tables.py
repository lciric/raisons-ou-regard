#!/usr/bin/env python3
"""Fabrique les tableaux du bilan final (lecture seule sur le livrable ; écrit tables.md dans _finale)."""
import json, re, sys
sys.path.insert(0, '/tmp/claude-0/-home-user-sycophancy-construct-validity/332d478c-da90-5795-bb10-27657d88c4d0/scratchpad/cours_v36/outils')
import appliquer as A
F = '/tmp/claude-0/-home-user-sycophancy-construct-validity/332d478c-da90-5795-bb10-27657d88c4d0/scratchpad/cours_v36/travail/_finale'
enc = json.load(open(f'{F}/encadres.json'))
cpt = json.load(open(f'{F}/comptes_par_tranche.json'))
cor = json.load(open(f'{F}/corrections_appliquees.json'))
L = {fi: open(A.OUT[fi], encoding='utf8').read().split('\n') for fi in ('FR', 'EN')}
# index de la note d'ouverture (FR) : instrument court -> endroit
idx = []
for l in L['FR'][:40]:
    m = re.match(r'^> ⚠ \*\*Limites et parades\*\* : (.*?) \*\(v3\.6\)\*\s*$', l)
    if m:
        for e in m.group(1).split(' ; '):
            a, b = e.split(' → ', 1); idx.append((a.strip(), b.strip()))
assert len(idx) == 27
DEMANDE = {1, 5, 6, 7, 8, 9, 10, 11, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27}
partiel = {}
for fi, pat_start, pat_any in (('FR', r'\*\*Parade :\*\* aucune connue', r'aucune (parade )?(complète )?connue'),):
    for k, b in enumerate(enc[fi]):
        partiel[k] = sum(1 for j in range(b['ligne'], b['fin']) if re.search(pat_any, L[fi][j]) and not re.search(pat_start, L[fi][j]))
out = []
out.append('| # | Instrument (FR) | Instrument (EN) | Maison (d\'après l\'index de la note d\'ouverture) | Ligne v3.6 FR | Ligne v3.6 EN | Limites | Parade « aucune connue » | Parade partielle, reste sans parade | Nommé dans la demande |')
out.append('|---|---|---|---|---|---|---|---|---|---|')
for k, (f, e) in enumerate(zip(enc['FR'], enc['EN'])):
    out.append(f"| {k + 1} | {f['instrument']} | {e['instrument']} | {idx[k][1]} | {f['ligne']} | {e['ligne']} | {f['limites']} | {f['aucune']} | {partiel[k]} | {'oui' if k + 1 in DEMANDE else 'non (ajouté)'} |")
tot_l = sum(b['limites'] for b in enc['FR']); tot_n = sum(b['aucune'] for b in enc['FR']); tot_p = sum(partiel.values())
out.append(f'| | **Total** | | | | | **{tot_l}** | **{tot_n}** | **{tot_p}** | 20 nommés + 7 ajoutés |')
open(f'{F}/table_instruments.md', 'w', encoding='utf8').write('\n'.join(out) + '\n')
# sans parade : liste par instrument
out = []
for k, b in enumerate(enc['FR']):
    if b['aucune']:
        e = enc['EN'][k]
        out.append(f"- **{b['instrument']}** (FR l. {b['ligne']}, EN l. {e['ligne']}) — {b['aucune']} limite(s) :")
        for s in b['sans_parade']:
            out.append(f'  - {s}')
open(f'{F}/liste_sans_parade.md', 'w', encoding='utf8').write('\n'.join(out) + '\n')
# annexe des corrections
out = ['| Fichier | N° | Langue | Ligne v3.6 | Tranche | Nature de la ligne corrigée | Début du texte corrigé |', '|---|---|---|---|---|---|---|']
for g, n, fi, line, tr, nat, ex in cor:
    ex = ex.replace('|', '\\|')
    out.append(f'| {g} | {n} | {fi} | {line} | {tr} | {nat} | {ex} |')
open(f'{F}/annexe_corrections.md', 'w', encoding='utf8').write('\n'.join(out) + '\n')
print(open(f'{F}/table_instruments.md', encoding='utf8').read())
print(open(f'{F}/liste_sans_parade.md', encoding='utf8').read()[:3000])
