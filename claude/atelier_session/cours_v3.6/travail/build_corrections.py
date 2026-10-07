import json, sys
W='/tmp/claude-0/-home-user-sycophancy-construct-validity/332d478c-da90-5795-bb10-27657d88c4d0/scratchpad/cours_v36'
V36={'FR':open(f'{W}/livrable/COURS_Alignment_v3.6_FR_2026-10-02.md',encoding='utf8').read(),
     'EN':open(f'{W}/livrable/COURS_Alignment_v3.6_EN_2026-10-02.md',encoding='utf8').read()}
V35={'FR':open(f'{W}/source/COURS_Alignment_v3.5_FR_2026-09-27.md',encoding='utf8').read(),
     'EN':open(f'{W}/source/COURS_Alignment_v3.5_EN_2026-09-27.md',encoding='utf8').read()}

def line_with(fi, key):
    ls=[l for l in V36[fi].split('\n') if key in l]
    assert len(ls)==1, (fi,key,len(ls))
    return ls[0]

C=[]
def corr(fi, key, subs):
    old=line_with(fi,key)
    new=old
    for a,b in subs:
        assert new.count(a)==1, (fi,key,a,new.count(a))
        new=new.replace(a,b)
    assert new!=old
    C.append({'fichier':fi,'ancien':old,'nouveau':new})

# 1. Note d'ouverture : les morceaux de l'encadré du 2 octobre ne portent pas *(v3.6)*
corr('FR',"Rien du texte de la v3.5 n'est retiré ni modifié",
     [("chaque ajout porte la mention *(v3.6)*. Deux ajouts.",
       "chaque ajout porte la mention *(v3.6)* ou, pour les morceaux de l'encadré du 2 octobre, sa date. Deux ajouts.")])
corr('EN',"No text of v3.5 is removed or changed",
     [("every addition carries the mark *(v3.6)*. Two additions.",
       "every addition carries the mark *(v3.6)* or, for the pieces of the box of 2 October, its date. Two additions.")])

# 2. Q4 : dommage et spécificité confondus
corr('FR',"n'est qu'un appui faible tant que le dommage n'est pas écarté :",
     [("tant que le dommage n'est pas écarté :","tant que le dommage n'est pas écarté et la spécificité pas établie :"),
      ("le dommage ne s'écarte qu'à dégradation appariée, par une courbe dose-réponse contre plusieurs témoins, avec un cas connu au même réglage (cours, volet M, M4 ; cours, volet 2, §C, K47).",
       "le dommage ne s'écarte qu'à dégradation appariée, et la spécificité s'établit par une courbe dose-réponse contre plusieurs témoins, celle du concept au-dessus à chaque niveau de dommage, avec un cas connu au même réglage (cours, volet M, M4 ; cours, volet 2, §C, K47 ; fiche 2).")])
corr('EN',"is only weak support as long as damage has not been ruled out:",
     [("as long as damage has not been ruled out:","as long as damage has not been ruled out and specificity not established:"),
      ("damage is ruled out only at matched degradation, by a dose-response curve against several controls, with a known case at the same setting (course, Part M, M4; course, Part 2, §C, K47).",
       "damage is ruled out only at matched degradation, and specificity is established by a dose-response curve against several controls, the concept's curve above theirs at every level of damage, with a known case at the same setting (course, Part M, M4; course, Part 2, §C, K47; reading sheet 2).")])

# 3. Q5 : chiffres de F·51, fiche non relue aux sources
corr('FR',"« La seconde prend le relais » suppose",
     [("contre 55 % pour le meilleur moniteur LLM (cours, volet 7, F·51).",
       "contre 55 % pour le meilleur moniteur LLM (cours, volet 7, F·51 : fiche de première version, non relue aux sources).")])
corr('EN',"\"The second takes over\" assumes",
     [("against 55% for the best LLM monitor (course, Part 7, F·51).",
       "against 55% for the best LLM monitor (course, Part 7, F·51: a first-version sheet, not checked against the sources).")])

# 4. Q9 : le nul de rang un — la limite citée était la lecture même de la réponse
corr('FR',"« Plusieurs méthodes de rang un ont échoué » est un nul",
     [("et un nul de pilotage peut venir d'un rang trop bas (fiche 7).",
       "et, sans cas connu au même réglage, ce nul ne sépare pas « il faut plus d'une direction » d'un instrument aveugle à cette dose (cours, volet M, M5 ; fiche 7).")])
corr('EN',"\"Several rank-one methods failed\" is a null",
     [("and a steering null can come from too low a rank (reading sheet 7).",
       "and, without a known case at the same setting, that null does not separate \"more than one direction is needed\" from an instrument blind at that dose (course, Part M, M5; reading sheet 7).")])

# 5. Q9 : le mot que M8 interdit, même pour le nier
corr('FR',"sans encoder la déférence",
     [("le sous-espace adoucit les verdicts négatifs sans encoder la déférence, et",
       "le sous-espace adoucit les verdicts négatifs, avec ou sans pression, et")])
corr('EN',"without encoding deference",
     [("the subspace softens negative verdicts without encoding deference, and",
       "the subspace softens negative verdicts with or without pressure, and")])

# 6. Q11 : le « rien trouvé » d'une red team ne borne qu'avec un cas connu
corr('FR',"Le résultat d'un jeu red team / blue team ne vaut que",
     [("dont le « rien trouvé » n'est qu'une borne (cours, volet M, M7).",
       "dont le « rien trouvé » n'est qu'une borne, et seulement si la même red team réussit là où l'on sait qu'elle doit réussir (cours, volet M, M5 et M7).")])
corr('EN',"The result of a red team / blue team game holds only",
     [("whose \"found nothing\" is only a bound (course, Part M, M7).",
       "whose \"found nothing\" is only a bound, and only if the same red team succeeds where it is known that it should (course, Part M, M5 and M7).")])

# 7. Encadré « Contrôles aléatoires », limite 2 : la source dit « l'aléatoire seul »
corr('FR',"Un tirage aléatoire seul est un contrôle faible",
     [("**Limite :** Un tirage aléatoire seul est un contrôle faible :","**Limite :** L'aléatoire seul est un contrôle faible :")])
corr('EN',"A single random draw is a weak control",
     [("**Limit:** A single random draw is a weak control:","**Limit:** Random alone is a weak control:")])

# 8. Encadré « Contrôles aléatoires », limite 4 : trois contrôles, pas deux
corr('FR',"sont deux contrôles différents ; leur confusion",
     [("sont deux contrôles différents ; leur confusion a coûté une journée de corrections,",
       "sont deux des trois contrôles de ton dossier, dont la confusion a coûté une journée entière de corrections,")])
corr('EN',"are two different controls; confusing them",
     [("are two different controls; confusing them cost a full day of corrections,",
       "are two of the three controls in your dossier, whose confusion cost a full day of corrections,")])

# 9. Encadré « Jeu tenu à part », limite 3 : sources de la couche et du seuil
corr('FR',"Choisir la couche, le seuil ou le prédicteur sur le jeu de test",
     [("*(source : cours, volet 2, C bis ; README du dépôt)*",
       "*(source : cours, volet M, M4 ; cours, volet 2, C bis ; programme, partie 3 ; README du dépôt)*")])
corr('EN',"Choosing the layer, threshold or predictor on the test set",
     [("*(source: course, Part 2, C bis; repository README)*",
       "*(source: course, Part M, M4; course, Part 2, C bis; programme, part 3; repository README)*")])

# 10. Volet M, M9 : le nul d'une chasse ne borne qu'avec un cas connu
corr('FR',"« Aucun contournement universel dans sa chasse » est le nul",
     [("une borne à son budget, pas une absence, et une chasse",
       "une borne à son budget, pas une absence, qui ne vaut que si la même chasse trouve là où l'on sait qu'il y a à trouver, et une chasse")])
corr('EN',"\"No universal jailbreak in its hunt\" is the null",
     [("a bound at its budget, not an absence, and a hunt",
       "a bound at its budget, not an absence, which holds only if the same hunt finds something where it is known there is something to find, and a hunt")])

# 11. EN seul : renvoi de M5 (paragraphe, fiche, anglais) et encadré « Known case »
corr('EN',"The rule of this section, applied to misalignment probes",
     [("The rule of this section,","The rule of this paragraph,"),
      ("section A; sheet 15);","section A; reading sheet 15);"),
      ("an organism trained to the action by reflex","an organism trained to act by reflex")])
corr('EN',"two different manufactures of the same behaviour",
     [("two different manufactures of the same behaviour","two different ways of installing the same behaviour")])

# Contrôles : unicité dans la v3.6, absence de la v3.5 (texte ajouté seulement)
for c in C:
    fi=c['fichier']
    assert V36[fi].count(c['ancien'])==1, c['ancien'][:80]
    assert c['ancien'] not in V35[fi], c['ancien'][:80]
    # chaque ligne de l'ancien est absente de la v3.5 (ligne ajoutée)
    for l in c['ancien'].split('\n'):
        assert l not in V35[fi].split('\n'), l[:80]
out=f'{W}/travail/corrections_groupe_1.json'
json.dump({'corrections':C}, open(out,'w',encoding='utf8'), ensure_ascii=False, indent=1)
print(len(C),'corrections écrites dans',out)
