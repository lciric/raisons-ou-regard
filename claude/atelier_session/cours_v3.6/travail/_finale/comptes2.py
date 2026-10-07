#!/usr/bin/env python3
"""Recoupement des comptes par tranche (lecture seule).
(1) Dans la v3.6 corrigée, par un alignement exact : les lignes non vides de la v3.5 sont placées gloutonnement, puis on vérifie
    que chacune est à une position où le contenu est unique OU cohérente avec le diff ; les lignes vides de la v3.5 sont placées
    sur les dernières lignes vides de chaque intervalle (l'outil insère juste après l'ancre).
(2) Dans les fichiers insertions_*.json, par tranche (texte d'avant les corrections)."""
import re, sys, json, glob, subprocess
sys.path.insert(0, '/tmp/claude-0/-home-user-sycophancy-construct-validity/332d478c-da90-5795-bb10-27657d88c4d0/scratchpad/cours_v36/outils')
import appliquer as A
PAT = {
 'FR': [('encadre', r'^> \*\*⚠ Limites et parades — '), ('renvoi', r'^> ⚠ \*\*Limites et parades\*\* : '), ('avert', r'^> ⚠ \*\(v3\.6\)\* '), ('morceau', r'★ Encadré du 2 octobre 2026')],
 'EN': [('encadre', r'^> \*\*⚠ Limits and workarounds — '), ('renvoi', r'^> ⚠ \*\*Limits and workarounds\*\*: '), ('avert', r'^> ⚠ \*\(v3\.6\)\* '), ('morceau', r'★ Box of 2 October 2026')]}
NAT = ['encadre', 'renvoi', 'avert', 'morceau']
def tranche_of(fi, i):
    for t, d in A.TRANCHES.items():
        x, y = d[fi]
        if x - 1 <= i <= y - 1: return t
    return None
res1, res2 = {}, {}
for fi in ('FR', 'EN'):
    a = open(A.SRC[fi], encoding='utf8').read().split('\n')
    b = open(A.OUT[fi], encoding='utf8').read().split('\n')
    # alignement par diff (LCS) : lignes de b qui viennent de a
    out = subprocess.run(['diff', A.SRC[fi], A.OUT[fi]], capture_output=True, text=True).stdout
    added = set()  # indices 0-based dans b
    ins_after = {}  # indice b -> ligne a (1-based) après laquelle le bloc est ajouté
    for m in re.finditer(r'(?m)^(\d+)a(\d+)(?:,(\d+))?$', out):
        na, s, e = int(m.group(1)), int(m.group(2)), int(m.group(3) or m.group(2))
        for k in range(s, e + 1):
            added.add(k - 1); ins_after[k - 1] = na
    assert not re.search(r'(?m)^\d+(,\d+)?[cd]\d', out), 'diff contient des modifications ou suppressions'
    assert len(added) == len(b) - len(a), (len(added), len(b), len(a))
    # tranche de chaque ligne ajoutée : celle de la dernière ligne NON VIDE de a qui précède le bloc (ancre)
    c = {t: dict.fromkeys(NAT + ['lignes'], 0) for t in A.TRANCHES}
    for k in sorted(added):
        na = ins_after[k]  # 1-based ; le bloc vient après la ligne na de a
        i = na - 1
        while i >= 0 and not a[i].strip(): i -= 1
        t = tranche_of(fi, i)
        c[t]['lignes'] += 1
        for nat, p in PAT[fi]:
            if re.search(p, b[k]): c[t][nat] += 1
    res1[fi] = c
    # (2) insertions_*.json
    c2 = {t: dict.fromkeys(NAT + ['insertions'], 0) for t in A.TRANCHES}
    for f in glob.glob(f'{A.TRAV}/insertions_*.json'):
        d = json.load(open(f, encoding='utf8'))
        for ins in d['insertions']:
            if ins['fichier'] != fi: continue
            c2[d['tranche']]['insertions'] += 1
            for l in ins['texte'].split('\n'):
                for nat, p in PAT[fi]:
                    if re.search(p, l): c2[d['tranche']][nat] += 1
    res2[fi] = c2
ok = True
for t in A.TRANCHES:
    for fi in ('FR', 'EN'):
        for nat in NAT:
            if res1[fi][t][nat] != res2[fi][t][nat]:
                ok = False; print('DIFFÉRENCE', t, fi, nat, res1[fi][t][nat], res2[fi][t][nat])
print('recoupement diff / insertions_*.json :', 'identique' if ok else 'ÉCARTS')
print('\n| Tranche | Insertions FR / EN | Encadrés FR / EN | Renvois FR / EN | Avertissements FR / EN | Morceaux du 2 oct. FR / EN | Lignes ajoutées FR / EN |')
print('|---|---|---|---|---|---|---|')
T = {fi: dict.fromkeys(NAT + ['lignes', 'insertions'], 0) for fi in ('FR', 'EN')}
for t in A.TRANCHES:
    f, e = res1['FR'][t], res1['EN'][t]
    fi2, ei2 = res2['FR'][t]['insertions'], res2['EN'][t]['insertions']
    for fi, r in (('FR', f), ('EN', e)):
        for n in NAT + ['lignes']: T[fi][n] += r[n]
    T['FR']['insertions'] += fi2; T['EN']['insertions'] += ei2
    print(f"| {t} | {fi2} / {ei2} | {f['encadre']} / {e['encadre']} | {f['renvoi']} / {e['renvoi']} | {f['avert']} / {e['avert']} | {f['morceau']} / {e['morceau']} | {f['lignes']} / {e['lignes']} |")
f, e = T['FR'], T['EN']
print(f"| **Total** | **{f['insertions']} / {e['insertions']}** | **{f['encadre']} / {e['encadre']}** | **{f['renvoi']} / {e['renvoi']}** | **{f['avert']} / {e['avert']}** | **{f['morceau']} / {e['morceau']}** | **{f['lignes']} / {e['lignes']}** |")
json.dump({'diff': res1, 'insertions': res2}, open(f'{A.TRAV}/_finale/comptes_par_tranche.json', 'w'), ensure_ascii=False, indent=1)
