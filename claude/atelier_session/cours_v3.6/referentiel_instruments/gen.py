# -*- coding: utf-8 -*-
import re, json, sys
sys.path.insert(0, '/tmp/claude-0/-home-user-sycophancy-construct-validity/332d478c-da90-5795-bb10-27657d88c4d0/scratchpad/ref')
from data import I
from reco import R, P

W = '/tmp/claude-0/-home-user-sycophancy-construct-validity/332d478c-da90-5795-bb10-27657d88c4d0/scratchpad/cours_v36'
SRC = {'FR': f'{W}/source/COURS_Alignment_v3.5_FR_2026-09-27.md', 'EN': f'{W}/source/COURS_Alignment_v3.5_EN_2026-09-27.md'}
TR = {
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
L = {k: open(v, encoding='utf8').read().split('\n') for k, v in SRC.items()}
ERR = []

def tranche_of(fi, n):
    for k, v in TR.items():
        a, b = v[fi]
        if a <= n <= b:
            return k

def check_anchor(fi, tr, n):
    line = L[fi][n - 1]
    a, b = TR[tr][fi]
    if not line.strip():
        ERR.append(f'{fi} {tr} ligne {n} vide'); return line
    idx = [i + 1 for i in range(a - 1, b) if L[fi][i].strip() == line.strip()]
    if idx != [n]:
        ERR.append(f'{fi} {tr} ligne {n} : ancre non unique {idx[:6]}')
    if tranche_of(fi, n) != tr:
        ERR.append(f'{fi} ligne {n} hors tranche {tr}')
    return line

def heading_of(fi, n):
    for i in range(n - 1, -1, -1):
        s = L[fi][i]
        if s.startswith('#'):
            return i + 1, s
    return 0, ''

def box(it, lang):
    if lang == 'FR':
        out = [f"> **⚠ Limites et parades — {it['nom_fr']}** *(v3.6, 2 octobre 2026)*", ">"]
        for (l, s, p, ps, *_rest) in it['L']:
            out.append(f"> - **Limite :** {l}. *(source : {s})*")
            if p is None:
                out.append(">   **Parade :** aucune connue ; on le dit.")
            else:
                out.append(f">   **Parade :** {p[0].upper() + p[1:]}. *(source : {ps})*")
    else:
        out = [f"> **⚠ Limits and workarounds — {it['nom_en']}** *(v3.6, 2 October 2026)*", ">"]
        for (_a, _b, _c, _d, l, s, p, ps) in it['L']:
            out.append(f"> - **Limit:** {l}. *(source: {s})*")
            if p is None:
                out.append(">   **Workaround:** none known; say so.")
            else:
                out.append(f">   **Workaround:** {p[0].upper() + p[1:]}. *(source: {ps})*")
    return '\n'.join(out)

BYID = {it['id']: it for it in I}

def renvoi(ids, lang):
    if lang == 'FR':
        parts = [f"{BYID[i]['court_fr']} → {BYID[i]['ou_fr']}" for i in ids]
        return "> ⚠ **Limites et parades** : " + ' ; '.join(parts) + " *(v3.6)*"
    parts = [f"{BYID[i]['court_en']} → {BYID[i]['ou_en']}" for i in ids]
    return "> ⚠ **Limits and workarounds**: " + '; '.join(parts) + " *(v3.6)*"

def occurrences(fi, pat):
    r = re.compile(pat, re.I)
    res = {}
    for i, l in enumerate(L[fi]):
        if r.search(l):
            t = tranche_of(fi, i + 1)
            hn, h = heading_of(fi, i + 1)
            res.setdefault(t, {}).setdefault((hn, h), []).append(i + 1)
    return res

def find_en_heading(tr, pat):
    a, b = TR[tr]['EN']
    r = re.compile(pat)
    hits = [i + 1 for i in range(a - 1, b) if r.search(L['EN'][i])]
    if len(hits) != 1:
        ERR.append(f'EN {tr} : en-tête « {pat} » trouvé {len(hits)} fois {hits[:4]}')
    return hits[0] if hits else 0

def nb(it):
    return len(it['L']), sum(1 for x in it['L'] if x[2] is not None)

def clip(s, n=110):
    s = s.strip()
    return s if len(s) <= n else s[:n] + '…'

# ------------------------------------------------------------------ vérifications et données
for it in I:
    it['anc_fr'] = check_anchor('FR', it['tranche'], it['fr_line'])
    it['anc_en'] = check_anchor('EN', it['tranche'], it['en_line'])
    # citations : pas de guillemets de plus de 14 mots
    for tup in it['L']:
        for txt in tup:
            if not txt: continue
            for q in re.findall(r'«([^»]*)»', txt) + re.findall(r'"([^"]*)"', txt):
                if len(q.split()) >= 15:
                    ERR.append(f"{it['id']} : citation trop longue « {q[:60]} »")
for p in P:
    tr = p[0]
    check_anchor('FR', tr, p[1]); check_anchor('EN', tr, p[2])
RECO = []
for (tr, frl, enpat, ids) in R:
    hn, h = (frl, L['FR'][frl - 1])
    if tranche_of('FR', frl) != tr:
        ERR.append(f'reco FR {frl} hors tranche {tr}')
    enl = find_en_heading(tr, enpat)
    RECO.append(dict(tranche=tr, fr_line=frl, fr_head=h, en_line=enl, en_head=L['EN'][enl - 1] if enl else '', ids=ids))

# ------------------------------------------------------------------ écriture du référentiel
TORD = list(TR.keys())
out = []
w = out.append
w("# Référentiel des instruments — cours d'alignement v3.6 (2 octobre 2026)")
w("")
w("*Pour les quatorze rédacteurs de la v3.6, un par tranche. Écrit le 2 octobre 2026 à partir des seules pièces du dossier : les deux sources v3.5, l'explication source du 2 octobre, les fiches de lecture prioritaires (partie B et fiches 1 à 19) et leur contre-lecture, le programme « Raisons ou regard ? » (parties 3, 7 et 8), la passation v1.2 (§5.1 et §5.2), les rapports d'antériorité du 1er et du 2 octobre (cités comme rapports) et le README du dépôt.*")
w("")
w("## Mode d'emploi")
w("")
w("- **Ce que contient chaque fiche d'instrument** : son nom (FR et EN), sa maison (tranche, section, ligne d'ancrage exacte dans chaque langue, recopiée telle quelle de la v3.5), le texte complet de son encadré en français et en anglais au format fixe, son renvoi d'une ligne dans les deux langues, et les endroits où il revient.")
w("- **L'encadré complet** s'insère juste après la ligne d'ancrage de sa maison (outil `appliquer.py`, format `travail/insertions_<tranche>.json`). Chaque ancre a été vérifiée : présente une seule fois dans sa tranche (après suppression des espaces de début et de fin), dans les deux langues. Les textes des encadrés sont donnés dans des blocs `~~~` : les recopier sans les clôtures.")
w("- **Le renvoi d'une ligne** se pose dans les sections où l'instrument revient. La partie « Par tranche », en fin de document, donne pour chaque tranche les sections où un renvoi est conseillé, avec le texte du renvoi prêt dans les deux langues ; le rédacteur choisit lui-même la ligne d'ancrage dans la section (une ligne unique dans sa tranche, en fin de passage, jamais au milieu d'une phrase coupée).")
w("- **Les avertissements ponctuels** prêts (neuf) sont donnés avec leur ancre vérifiée. Le rédacteur peut en ajouter d'autres, au format fixe, quand un passage de sa tranche rapporte un résultat obtenu avec un instrument sans dire sa limite ; il prend alors la limite et la parade, avec leurs sources, dans l'encadré de l'instrument.")
w("- **La doctrine, partout** : une direction aléatoire de même norme n'est que le nul de spécificité ; le dommage ne s'écarte qu'à dégradation appariée ; un nul d'instrument ne compte qu'avec son cas connu ; « to our knowledge », jamais « first ». Aucun ajout ne touche une ligne « À dire » ni une forme nommée, ni ne leur ajoute de chiffre.")
w("- **Les sources** : « cours, volet … » renvoie à la v3.5 ; « fiche n » aux fiches de lecture prioritaires du 1er octobre ; « fiches, partie B » à leur méthode de lecture (les sept pièges) ; « fiches, partie C » à leur fil rouge ; « contre-lecture des fiches » à la contre-lecture du 1er octobre ; « programme, partie n » au programme « Raisons ou regard ? » ; « passation » à la passation v1.2 ; « explication du 2 octobre » au texte source de l'encadré sur les sondes de désalignement ; « rapport d'antériorité n du 2 octobre » aux rapports bruts, toujours dits « rapport » ; « README du dépôt » au dépôt sycophancy-construct-validity. En anglais : course, Part …; reading sheet n; reading sheets, part B / part C; counter-reading of the sheets; programme, part n; handover; explanation of 2 October; prior-art report n of 2 October — report; repository README.")
w("")
w("## Table des instruments")
w("")
w("| # | Instrument | Maison (tranche, section) | Limites | Parades |")
w("|---|---|---|---|---|")
tl = tp = 0
for k, it in enumerate(I, 1):
    a, b = nb(it); tl += a; tp += b
    w(f"| {k} | {it['nom_fr']} / *{it['nom_en']}* | `{it['tranche']}` — {it['section_fr']} | {a} | {b} |")
w(f"| | **Total : {len(I)} instruments** | | **{tl}** | **{tp}** |")
w("")
w("« Parades » compte les limites qui ont une parade, même partielle ; les autres portent « aucune connue ; on le dit ».")
w("")
w("## Les contrôles et dispositifs : ce qui a un encadré, ce qui est fondu ailleurs")
w("")
w("- **La direction aléatoire de même norme, la dégradation appariée, le cas connu, le jeu tenu à part** ont chacun des limites propres (une dégradation appariée ne vaut que sur le composite choisi ; un cas connu est nécessaire, pas suffisant ; etc.) : ils ont donc leur encadré, au volet M (M4 et M5).")
w("- **La dose-réponse** est fondue dans l'encadré « Dégradation appariée et dose-réponse ».")
w("- **Les paires contrastives** (volet M, M4) sont fondues dans l'encadré « Sondes d'activation » : leur limite (une paire qui porte un style) et sa parade (un classifieur de la seule surface au hasard) y sont.")
w("- **Le jumeau propre et le jeu canari** (volet M, M4 et M5) sont fondus dans l'encadré « Classifieurs de sûreté » ; **la référence jamais entraînée** dans « Désapprentissage et ré-élicitation » ; **la notation à l'aveugle** dans « Juges LLM » ; **le bras de référence réaliste** dans « Évaluations comportementales » et « Red-teaming ».")
w("- **Le témoin sans pression et la direction d'un concept rival** n'ont pas de limite propre dans les pièces au-delà de ce que M4 dit déjà ; ils apparaissent comme parades dans « Dégradation appariée » et « Ablation et projection ».")
w("- **Les vecteurs de persona** sont dans « Pilotage par vecteurs » ; **l'agrégation de scores de sondes et les moniteurs à état** dans « Moniteurs du contrôle » ; **le logit lens et le tuned lens** dans « J-lens » (comme proxy déclaré) et « Désapprentissage » (une lecture qui ne voit rien).")
w("- **L'encadré sur les sondes de désalignement** (texte source du 2 octobre, à reprendre en entier) n'est pas un encadré d'instrument : il traite le cas connu, l'entraînement et le hors-distribution des sondes. Les encadrés « Sondes d'activation », « J-lens », « Organismes modèles », « Cas connu » et « Détecteurs fine-tunés » en reprennent les limites avec leurs sources propres ; là où il sera placé, un renvoi vers ces cinq encadrés est conseillé (texte prêt dans la partie « Par tranche », volet 6, §8).")
w("")
w("---")
w("")
w("# Partie 1 — Les instruments, un par un")
w("")
for k, it in enumerate(I, 1):
    a, b = nb(it)
    w(f"## {k}. {it['nom_fr']} — *{it['nom_en']}*")
    w("")
    w(f"- **Maison** : tranche `{it['tranche']}` ; FR : {it['section_fr']} ; EN : {it['section_en']}.")
    w(f"- **Limites** : {a} ; **parades** : {b}.")
    w(f"- **Ancre FR** (ligne {it['fr_line']} de la v3.5 FR ; l'encadré s'insère juste après) :")
    w("")
    w("~~~text"); w(it['anc_fr']); w("~~~")
    w("")
    w(f"- **Ancre EN** (ligne {it['en_line']} de la v3.5 EN) :")
    w("")
    w("~~~text"); w(it['anc_en']); w("~~~")
    w("")
    w("**Encadré complet, français :**")
    w("")
    w("~~~markdown"); w(box(it, 'FR')); w("~~~")
    w("")
    w("**Encadré complet, anglais :**")
    w("")
    w("~~~markdown"); w(box(it, 'EN')); w("~~~")
    w("")
    w("**Renvoi d'une ligne :**")
    w("")
    w("~~~markdown"); w(renvoi([it['id']], 'FR')); w(renvoi([it['id']], 'EN')); w("~~~")
    w("")
    # où il revient (conseillé)
    recs = [r for r in RECO if it['id'] in r['ids']]
    pon = [p for p in P if it['id'] in p[3]]
    w("**Où un renvoi ou un avertissement ponctuel est conseillé :**")
    w("")
    if recs:
        for r in recs:
            w(f"- `{r['tranche']}` — FR l. {r['fr_line']} : {clip(r['fr_head'].lstrip('# '), 90)} · EN l. {r['en_line']} : {clip(r['en_head'].lstrip('# '), 90)} — renvoi.")
    for p in pon:
        w(f"- `{p[0]}` — avertissement ponctuel prêt, après FR l. {p[1]} / EN l. {p[2]} (texte dans la partie « Par tranche »).")
    if not recs and not pon:
        w("- (aucun au-delà de sa maison)")
    w("")
    # occurrences automatiques
    w(f"**Où il revient** (relevé automatique, motifs FR `{it['re_fr']}` / EN `{it['re_en']}` ; sections, avec le nombre de lignes touchées) :")
    w("")
    ofr = occurrences('FR', it['re_fr']); oen = occurrences('EN', it['re_en'])
    for t in TORD:
        if t not in ofr and t not in oen:
            continue
        sfr = ofr.get(t, {}); sen = oen.get(t, {})
        def fmt(d):
            items = sorted(d.items(), key=lambda x: x[0][0])
            s = ' ; '.join(f"l. {hn} {clip(h.lstrip('# '), 48)} ({len(v)})" for (hn, h), v in items[:10])
            if len(items) > 10:
                s += f" ; … (+{len(items) - 10} sections)"
            return s or '—'
        w(f"- `{t}` — FR : {fmt(sfr)}")
        w(f"  — EN : {fmt(sen)}")
    w("")
    w("---")
    w("")

w("# Partie 2 — Par tranche")
w("")
w("Pour chaque tranche : les encadrés complets dont elle est la maison (ancre et renvoi à l'encadré de la partie 1), les avertissements ponctuels prêts, puis les renvois conseillés, section par section, texte prêt.")
w("")
for t in TORD:
    homes = [it for it in I if it['tranche'] == t]
    pons = [p for p in P if p[0] == t]
    recs = [r for r in RECO if r['tranche'] == t]
    a, b = TR[t]['FR']; c, d = TR[t]['EN']
    w(f"## `{t}` (FR l. {a}-{b} ; EN l. {c}-{d})")
    w("")
    w("**Encadrés complets à insérer (maison dans cette tranche) :**")
    w("")
    if homes:
        for it in homes:
            n = I.index(it) + 1
            w(f"- n° {n}, {it['nom_fr']} — après FR l. {it['fr_line']} « {clip(it['anc_fr'], 70)} » / EN l. {it['en_line']} « {clip(it['anc_en'], 70)} ».")
    else:
        w("- aucun.")
    w("")
    w("**Avertissements ponctuels prêts :**")
    w("")
    if pons:
        for p in pons:
            w(f"- Après FR l. {p[1]} / EN l. {p[2]} (instruments : {', '.join(BYID[i]['court_fr'] for i in p[3])}).")
            w("")
            w("  Ancre FR :")
            w("")
            w("~~~text"); w(L['FR'][p[1] - 1]); w("~~~")
            w("")
            w("  Ancre EN :")
            w("")
            w("~~~text"); w(L['EN'][p[2] - 1]); w("~~~")
            w("")
            w("~~~markdown"); w(p[4]); w(p[5]); w("~~~")
            w("")
    else:
        w("- aucun ; le rédacteur en ajoute s'il trouve un résultat d'instrument rapporté sans sa limite.")
    w("")
    w("**Renvois conseillés (le rédacteur choisit l'ancre dans la section) :**")
    w("")
    if t == 'volet6':
        w("- Là où sera placé l'encadré sur les sondes de désalignement (texte source du 2 octobre), un renvoi vers les cinq encadrés qui en reprennent les limites :")
        w("")
        w("~~~markdown"); w(renvoi(['sonde', 'jlens', 'orga', 'cas', 'det'], 'FR')); w(renvoi(['sonde', 'jlens', 'orga', 'cas', 'det'], 'EN')); w("~~~")
        w("")
    if recs:
        for r in recs:
            w(f"- FR l. {r['fr_line']} : {clip(r['fr_head'].lstrip('# '), 100)}")
            w(f"  EN l. {r['en_line']} : {clip(r['en_head'].lstrip('# '), 100)}")
            w("")
            w("~~~markdown"); w(renvoi(r['ids'], 'FR')); w(renvoi(r['ids'], 'EN')); w("~~~")
            w("")
    else:
        w("- aucun.")
    w("")

open(f'{W}/travail/referentiel_instruments.md', 'w', encoding='utf8').write('\n'.join(out) + '\n')

# aide machine : les encadrés et les ponctuels, au format de appliquer.py, par tranche
helper = {}
for it in I:
    helper.setdefault(it['tranche'], []).extend([
        {'fichier': 'FR', 'ancre': it['anc_fr'], 'texte': box(it, 'FR'), 'instrument': it['id'], 'nature': 'encadré'},
        {'fichier': 'EN', 'ancre': it['anc_en'], 'texte': box(it, 'EN'), 'instrument': it['id'], 'nature': 'encadré'}])
for p in P:
    helper.setdefault(p[0], []).extend([
        {'fichier': 'FR', 'ancre': L['FR'][p[1] - 1], 'texte': p[4], 'instrument': ','.join(p[3]), 'nature': 'ponctuel'},
        {'fichier': 'EN', 'ancre': L['EN'][p[2] - 1], 'texte': p[5], 'instrument': ','.join(p[3]), 'nature': 'ponctuel'}])
renv = {}
for r in RECO:
    renv.setdefault(r['tranche'], []).append({'section_fr': r['fr_head'], 'ligne_fr': r['fr_line'], 'section_en': r['en_head'], 'ligne_en': r['en_line'],
                                               'renvoi_fr': renvoi(r['ids'], 'FR'), 'renvoi_en': renvoi(r['ids'], 'EN')})
json.dump({'note': "Aide machine du référentiel : encadrés et ponctuels prêts au format de appliquer.py (clés fichier/ancre/texte), renvois par section (ancre à choisir).",
           'insertions_pretes': helper, 'renvois_conseilles': renv},
          open(f'{W}/travail/referentiel_instruments.json', 'w', encoding='utf8'), ensure_ascii=False, indent=1)

print('instruments', len(I), 'limites', tl, 'parades', tp, 'renvois', len(RECO), 'ponctuels', len(P))
print('\n'.join(ERR) if ERR else 'aucune erreur')
