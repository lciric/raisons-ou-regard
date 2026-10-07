#!/usr/bin/env python3
"""Groupe 5 (volet 7, tranches B_et_D et A_et_C) : construit corrections_groupe_5.json
à partir des lignes exactes de la v3.6, puis vérifie :
  1. chaque « ancien » est une ligne entière d'insertion v3.6, présente une seule fois dans la v3.6 ;
  2. aucun « ancien » ne figure dans la v3.5 (on ne touche que du texte ajouté) ;
  3. chaque « ancien » reste unique après application simulée des corrections des groupes 1 à 4 ;
  4. aucune citation (entre « » ou "…") n'atteint quinze mots dans les nouveaux textes ;
  5. le JSON écrit est valide et se relit.
"""
import glob, json, os, re, sys

W = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
V36 = {'FR': f'{W}/livrable/COURS_Alignment_v3.6_FR_2026-10-02.md', 'EN': f'{W}/livrable/COURS_Alignment_v3.6_EN_2026-10-02.md'}
V35 = {'FR': f'{W}/source/COURS_Alignment_v3.5_FR_2026-09-27.md', 'EN': f'{W}/source/COURS_Alignment_v3.5_EN_2026-09-27.md'}
OUT = f'{W}/travail/corrections_groupe_5.json'

txt36 = {k: open(v, encoding='utf8').read() for k, v in V36.items()}
txt35 = {k: open(v, encoding='utf8').read() for k, v in V35.items()}
lines36 = {k: v.split('\n') for k, v in txt36.items()}

# (fichier, début exact de la ligne d'insertion, [(sous-chaîne à remplacer, remplacement)], étiquette)
EDITS = [
    # 1 — volet 7, F·25 (B_et_D n° 9 / 10) : « plus faiblement » prêté aussi au volet 5, §3, qui dit « aussi forts »
    ('FR', "> ⚠ *(v3.6)* Le résultat interne rappelé ici vient du pilotage, et c'est un appui faible",
     [("bougent le comportement dans le même sens, plus faiblement, et chaque direction",
       "bougent le comportement dans le même sens — plus faiblement dans la carte système d'Opus 4.8, aussi fort dans une reproduction externe sur un modèle à poids ouverts —, et chaque direction")],
     'F·25'),
    ('EN', "> ⚠ *(v3.6)* The internal result recalled here comes from steering, and it is weak support",
     [("move behaviour in the same direction, more weakly, and every steered direction",
       "move behaviour in the same direction — more weakly in the Opus 4.8 system card, just as strongly in an external reproduction on an open-weights model —, and every steered direction")],
     'F·25'),
    # 2 — volet 7, F·31 (B_et_D n° 29 / 30) : le « pilotage loin d'une persona » n'est pas le pilotage préventif du papier
    ('FR', "> ⚠ *(v3.6)* Le lien entre déplacement et trait est corrélationnel",
     [("Et piloter loin d'une persona pendant l'entraînement aurait doublé",
       "Et piloter loin d'une persona pendant l'entraînement — l'inverse du pilotage préventif de ce papier, qui pousse vers le trait (fiche 8) — aurait doublé")],
     'F·31 a'),
    ('EN', "> ⚠ *(v3.6)* The shift-to-trait link is correlational",
     [("And steering away from a persona during training reportedly doubled",
       "And steering away from a persona during training — the opposite of this paper's preventative steering, which pushes toward the trait (reading sheet 8) — reportedly doubled")],
     'F·31 a'),
    # 3 — volet 7, F·31 (B_et_D n° 31 / 32) : « comme toute direction témoin » efface la condition « à norme égale » de la doctrine
    ('FR', "> ⚠ *(v3.6)* « MMLU préservé » n'écarte le dommage que sur ce composite",
     [("n'est, comme toute direction témoin, qu'un nul de spécificité",
       "n'est, comme toute direction témoin comparée à norme égale, qu'un nul de spécificité")],
     'F·31 b'),
    ('EN', "> ⚠ *(v3.6)* \"MMLU preserved\" rules out damage only on that composite",
     [("is, like any control direction, only a specificity null",
       "is, like any control direction compared at equal norm, only a specificity null")],
     'F·31 b'),
    # 4 — volet 7, F·36 (B_et_D n° 51 / 52) : la borne sans cas connu (doctrine)
    ('FR', "> ⚠ *(v3.6)* Le masquage sélectif des gradients n'est montré que sur de petits modèles *(source : cours, volet 2, §I, JB10)* ; et ton test par sondes",
     [("la ré-élicitation à budget fixé d'avance contre une référence jamais entraînée, rapportée comme une borne ; pour la taille des modèles, aucune parade connue ; on le dit *(source : cours, volet 10, Łucki et al. ; cours, volet 2, §I, JB10 ; cours, volet M, M7)*.",
       "la ré-élicitation à budget fixé d'avance, contre une référence jamais entraînée et, comme cas connu, un modèle connu pour masquer, rapportée comme une borne : sans ce cas connu, le budget est aveugle ; pour la taille des modèles, aucune parade connue ; on le dit *(source : cours, volet 10, Łucki et al. ; fiches, partie C ; cours, volet 2, §I, JB10 ; cours, volet M, M4 et M7)*.")],
     'F·36'),
    ('EN', "> ⚠ *(v3.6)* Selective gradient masking is shown only on small models *(source: course, Part 2, §I, JB10)*; and your probe test",
     [("re-elicitation at a budget fixed in advance against a never-trained reference, reported as a bound; for model size, none known; say so *(source: course, Part 10, Łucki et al.; course, Part 2, §I, JB10; course, Part M, M7)*.",
       "re-elicitation at a budget fixed in advance, against a never-trained reference and, as the known case, a model known to mask, reported as a bound: without that known case, the budget is blind; for model size, none known; say so *(source: course, Part 10, Łucki et al.; reading sheets, part C; course, Part 2, §I, JB10; course, Part M, M4 and M7)*.")],
     'F·36'),
    # 5 — volet 7, F·5 (A_et_C n° 17 / 18) : « jamais par l'exactitude de lecture » contredit le choix de couche par AUROC (programme ; encadré)
    ('FR', "> ⚠ *(v3.6)* La direction qui lit le mieux n'est pas forcément celle qui agit : chez RepE, la direction de la régression logistique",
     [("Parade : choisir une direction, ou un site, par son effet causal mesuré",
       "Parade : pour agir, retenir une direction, ou un site, sur son effet causal mesuré"),
      ("—, jamais par l'exactitude de lecture (passation, §5.2 ; cours, volet M, M4 ; README du dépôt).",
       "—, jamais sur sa seule exactitude de lecture : celle-ci choisit la couche d'une sonde, elle ne prouve pas que la direction agit (passation, §5.2 ; cours, volet M, M4 ; README du dépôt ; programme, partie 3).")],
     'F·5'),
    ('EN', "> ⚠ *(v3.6)* The direction that reads best is not necessarily the one that acts: in RepE, the logistic-regression direction",
     [("Workaround: choose a direction, or a site, by its measured causal effect",
       "Workaround: to act, retain a direction, or a site, on its measured causal effect"),
      ("— never by reading accuracy (handover, §5.2; course, Part M, M4; repository README).",
       "— never on its reading accuracy alone: that accuracy picks a probe's layer, it does not prove that the direction acts (handover, §5.2; course, Part M, M4; repository README; programme, part 3).")],
     'F·5'),
    # 6 — volet 7, F·7 (A_et_C n° 23 / 24) : « aucune parade connue » contre l'artefact de polarité, alors que M4 en donne
    ('FR', "> ⚠ *(v3.6)* Ce nul de rang un est dit sans son cas connu",
     [("; contre l'artefact de polarité, aucune parade connue ; on le dit.",
       "; contre l'artefact de polarité, des paires qui ne diffèrent que par le trait, vérifiées par un classifieur qui ne lit que la surface, une direction de polarité construite comme concept rival, au même endroit et à dégradation appariée, et le témoin sans pression (cours, volet M, M4).")],
     'F·7'),
    ('EN', "> ⚠ *(v3.6)* This rank-one null is stated without its known case",
     [("; against the polarity artefact, none known; say so.",
       "; against the polarity artefact, pairs that differ only in the trait, checked by a classifier that reads only the surface, a polarity direction built as a rival concept, at the same place and at matched degradation, and the no-pressure control arm (course, Part M, M4).")],
     'F·7'),
    # 7 — volet 7, F·13 (A_et_C n° 53 / 54) : « aucune parade connue » contredit l'extension du volet 4, reprise juste dessous
    ('FR', "> ⚠ *(v3.6)* Que l'interprétabilité « aide » n'est pas chiffré",
     [("; contre un organisme trop facile, aucune parade connue ; on le dit.",
       "; contre un organisme trop facile, le durcir — un objectif plus profondément caché — et mesurer quelles méthodes tiennent encore (cours, volet 4, Auditing Hidden Objectives, repris ci-dessous) ; contre l'écart entre l'implanté et le naturel, aucune parade connue ; on le dit (cours, volet M, M5).")],
     'F·13'),
    ('EN', "> ⚠ *(v3.6)* That interpretability \"helps\" is not quantified",
     [("; against an organism that is too easy, none known; say so.",
       "; against an organism that is too easy, harden it — a more deeply hidden objective — and measure which methods still hold (course, Part 4, Auditing Hidden Objectives, reproduced below); against the gap between implanted and natural, none known; say so (course, Part M, M5).")],
     'F·13'),
    # 8 — volet 7, F·17 (A_et_C n° 61 / 62) : « pour les capacités, aucune parade connue » contredit la parade donnée (JB10)
    ('FR', "> ⚠ *(v3.6)* Ce « 7× » compare des méthodes de désapprentissage entre elles",
     [("pour dire une borne, pas une certification (cours, volet 2, §I, JB10) ; pour l'échelle et pour les capacités, aucune parade connue ; on le dit.",
       "pour dire une borne, pas une certification ; la référence jamais entraînée, qui écarte un fine-tuning qui enseigne au lieu de réveiller, étend ce test aux capacités (cours, volet 2, §I, JB10 ; cours, volet M, M4) ; pour l'échelle, aucune parade connue ; on le dit.")],
     'F·17'),
    ('EN', "> ⚠ *(v3.6)* This \"7×\" compares unlearning methods with each other",
     [("to state a bound, not a certification (course, Part 2, §I, JB10); for scale and for capabilities, none known; say so.",
       "to state a bound, not a certification; the never-trained reference, which rules out a fine-tune that teaches instead of reawakening, extends this test to capabilities (course, Part 2, §I, JB10; course, Part M, M4); for scale, none known; say so.")],
     'F·17'),
    # 9 — volet 7, F·54 (A_et_C n° 83 / 84) : le 0,844 de TRACE n'est pas dit rappel de campagne
    ('FR', "> ⚠ *(v3.6)* Un rappel de 0,844 ne se lit qu'avec son taux de faux positifs",
     [("Un rappel de 0,844 ne se lit qu'avec son taux de faux positifs et le ratio de trafic bénin : un rappel de campagne dépend du taux de base (cours, volet 6, §6).",
       "Un rappel de 0,844 ne se lit qu'avec son taux de faux positifs, que la fiche ne donne pas ; et un rappel de campagne dépend en plus du ratio de trafic bénin : celui de Brown tombe quand ce ratio monte (cours, volet 6, §6).")],
     'F·54'),
    ('EN', "> ⚠ *(v3.6)* A recall of 0.844 reads only with its false-positive rate",
     [("A recall of 0.844 reads only with its false-positive rate and the benign-traffic ratio: a campaign recall depends on the base rate (course, Part 6, §6).",
       "A recall of 0.844 reads only with its false-positive rate, which the sheet does not give; and a campaign recall also depends on the benign-traffic ratio: Brown's drops as that ratio rises (course, Part 6, §6).")],
     'F·54'),
]

def find_line(fi, prefix):
    idx = [i for i, l in enumerate(lines36[fi]) if l.startswith(prefix)]
    if len(idx) != 1:
        sys.exit(f'ERREUR : préfixe trouvé {len(idx)} fois ({fi}) : {prefix[:80]}')
    return idx[0]

corrections = []
for fi, prefix, subs, tag in EDITS:
    i = find_line(fi, prefix)
    old = lines36[fi][i]
    new = old
    for a, b in subs:
        if new.count(a) != 1:
            sys.exit(f'ERREUR : sous-chaîne trouvée {new.count(a)} fois ({fi}, {tag}) : {a[:80]}')
        new = new.replace(a, b)
    assert new != old
    corrections.append({'fichier': fi, 'ancien': old, 'nouveau': new, '_ligne': i + 1, '_tag': tag})

# 1 et 2 : unicité dans la v3.6, absence dans la v3.5
for c in corrections:
    fi, a = c['fichier'], c['ancien']
    assert txt36[fi].count(a) == 1, (fi, c['_tag'], 'non unique en v3.6')
    assert a not in txt35[fi], (fi, c['_tag'], 'présent en v3.5')
    assert '(v3.6' in a and a.startswith('> ⚠'), (fi, c['_tag'], 'pas une ligne d insertion')

# 3 : application simulée des groupes 1 à 4, puis des nôtres
sim = dict(txt36)
for f in sorted(glob.glob(f'{W}/travail/corrections_groupe_[1-4].json')):
    d = json.load(open(f, encoding='utf8'))
    for c in d['corrections']:
        if sim[c['fichier']].count(c['ancien']) == 1:
            sim[c['fichier']] = sim[c['fichier']].replace(c['ancien'], c['nouveau'])
for c in corrections:
    assert sim[c['fichier']].count(c['ancien']) == 1, (c['_tag'], 'touché par un autre groupe')
    sim[c['fichier']] = sim[c['fichier']].replace(c['ancien'], c['nouveau'])

# 4 : citations de moins de quinze mots dans les nouveaux textes
quote_re = re.compile(r'«\s*([^»]*?)\s*»|"([^"]*?)"')
for c in corrections:
    for m in quote_re.finditer(c['nouveau']):
        q = m.group(1) or m.group(2) or ''
        assert len(q.split()) < 15, (c['_tag'], q)

# 5 : écrire et relire
out = {'corrections': [{k: v for k, v in c.items() if not k.startswith('_')} for c in corrections]}
json.dump(out, open(OUT, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
back = json.load(open(OUT, encoding='utf8'))
assert len(back['corrections']) == len(corrections)
for c in corrections:
    print(f"{c['fichier']} l.{c['_ligne']:>5}  {c['_tag']:<7} OK")
print(f'{len(corrections)} corrections écrites dans {OUT} ; JSON valide ; toutes les vérifications passent.')
