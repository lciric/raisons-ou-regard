#!/usr/bin/env python3
"""Groupe 7 : écrit travail/verif_groupe_7.md (constats insertion par insertion)."""
import json, re

W = '/tmp/claude-0/-home-user-sycophancy-construct-validity/332d478c-da90-5795-bb10-27657d88c4d0/scratchpad/cours_v36'
TR = ('volet11_1_a_20', 'volet11_21_a_52', 'volet11_53_et_fin')
INS = {tr: json.load(open(f'{W}/travail/insertions_{tr}.json', encoding='utf8'))['insertions'] for tr in TR}
CORR = json.load(open(f'{W}/travail/corrections_groupe_7.json', encoding='utf8'))['corrections']

# ordre des corrections dans le JSON (identique à construire_corrections.py)
ORDRE = [('P1', TR[0], 13), ('P2', TR[0], 23), ('P3', TR[0], 29), ('P4', TR[0], 63), ('P5', TR[0], 65),
         ('P6', TR[0], 67), ('P7', TR[0], 91), ('P24', TR[0], 89),
         ('P8', TR[1], 11), ('P9', TR[1], 39), ('P10', TR[1], 77), ('P11', TR[1], 93), ('P12', TR[1], 99),
         ('P13', TR[1], 113),
         ('P14', TR[2], 5), ('P15', TR[2], 17), ('P16', TR[2], 21), ('P17', TR[2], 25), ('P18', TR[2], 37),
         ('P19', TR[2], 77), ('P20', TR[2], 85), ('P21', TR[2], 103), ('P22', TR[2], 109), ('P23', TR[2], 113)]
assert len(CORR) == 2 * len(ORDRE)
IDX = {}
for k, (p, tr, n) in enumerate(ORDRE):
    fr, en = CORR[2 * k], CORR[2 * k + 1]
    assert fr['fichier'] == 'FR' and en['fichier'] == 'EN'
    assert fr['ancien'] in INS[tr][n - 1]['texte'] and en['ancien'] in INS[tr][n]['texte'], (p, tr, n)
    IDX[(tr, n)] = (p, 2 * k + 1, 2 * k + 2)

# places : paires2.txt
PLACE = {}
for l in open(f'{W}/travail/_verif_groupe_7/paires2.txt', encoding='utf8'):
    m = re.match(r'(\S+) FR n°(\d+) \(v3\.5 l\.\d+, v3\.6 l\.(\d+)\) \[(.*?)\] \| EN n°(\d+) \(v3\.5 l\.\d+, v3\.6 l\.(\d+)\) \[(.*?)\]', l.strip())
    assert m, l
    tr, nfr, lfr, lab, nen, len_, lab2 = m.groups()
    assert lab == lab2
    PLACE[(tr, int(nfr))] = (lab, int(lfr), int(nen), int(len_))

def lieu(lab):
    if lab.isdigit():
        return f'réponse {lab}'
    if lab.startswith('«'):
        return f'prémisse {lab}…»'
    if '/' in lab:
        a, b = lab.split('/')
        return f'réponse {b}' if a.startswith('A9') else f'réponse {a}, point {b}'
    return f'réponse {lab}'

def typ(t):
    t = t.lstrip()
    if t.startswith('> ⚠ **Limites et parades** :'):
        return 'renvoi'
    if t.startswith('> **⚠ Limites et parades —'):
        return 'encadré'
    return 'avertissement'

R = 'renvoi'
C = {TR[0]: {}, TR[1]: {}, TR[2]: {}}

# ---------------- tranche volet11_1_a_20 ----------------
c = C[TR[0]]
c[1] = ('conforme', "J-lens montré sur Claude seulement, pour des concepts d'un seul token (fiche 1 ; passation, §5.2) ; trois sens de « charge » (cours, volet 6, §6). Parade — porte : reproduire l'échange d'un concept d'un seul token, sinon tuned lens déclaré, thèse alors non testée au sens de l'article ; prédicteur gelé d'abord — : programme, parties 3 et 8 (porte G9).")
c[5] = ('conforme ; place signalée', "Accord seulement modéré avec un second juge, juge qui ne voit que les deux réponses, aucun sous-ensemble noté par des humains : README du dépôt. Parade (juge scellé, audit humain stratifié, réponse entière, texte complet) : programme, partie 3 ; README. Place : entre « trois choses autour » et « La première » de la réponse 2 ; rien n'est coupé, mais l'annonce est séparée de son premier point (alerte).")
c[7] = ('conforme', "Partition non mesurée à dégradation égale (citation de la réponse A4, sous quinze mots) ; aléatoire apparié en covariance plus fort que la direction de la sonde (cours, volet 6, §2 et §3). Parade : protocole de la réponse A4, patch de l'état complet comme plafond (programme, partie 8).")
c[9] = ('conforme', "Doctrine juste : témoin de même norme = nul de spécificité ; les contrôles aléatoires d'origine n'écartent pas le dommage ; l'ablation dit la nécessité, pas la spécificité (cours, volet 6, §2 ; volet M, M4 ; cohérent avec l'encadré « Ablation »). Parade : sous-espaces de même rang à dégradation appariée, retrait partiel ou courbe effet/dégradation (M4 ; C bis ; programme, partie 7).")
c[13] = ('corrigé (P1)', "Faute de logique. L'insertion dit qu'à défaut de cas connu « un nul peut venir d'un rang trop bas » ; or le cas connu qu'elle propose est un autre concept (les pays, au rang un) : il écarte l'instrument aveugle, pas le rang trop bas, que seul le balayage de rang traite. La fiche 7 ne lie les deux que si le cas positif porte sur le même concept, en distribution. Correction : sans cas connu, le nul ne sépare pas « il faut plus d'une direction » (ta prédiction pour un concept réparti : fiche 7 ; programme, partie 2) d'un instrument aveugle à cette dose (M5). Même constat que le groupe 1.")
c[15] = ('conforme', "Artefact de polarité oui/non de l'addition contrastive ; résidu du dictionnaire épars qui garde la plus grande part de la variance et porte le signal lu : README du dépôt. « Aucune parade connue ; on le dit » à juste titre, pour l'artefact et pour trancher entre les deux lectures.")
c[19] = ('conforme', "Un seul tirage par condition ; sous-espace extrait sur le lot qui sert à l'évaluer : README. Parade (plusieurs générations, bootstrap au niveau des items, extraction sur un jeu disjoint) : programme, partie 7 ; README.")
c[23] = ('corrigé (P2)', "Doctrine et portée. « Des vecteurs de contrôle aléatoires » sans « de même norme » pour le nul de spécificité ; et « chaque direction dégrade les sorties » est généralisé, alors que les fiches le donnent pour la carte d'Opus 4.8, à 0,10× (fiche 2 ; fiches, contradictions entre papiers) — Fable 5 : dégradation négligeable à 0,01×. Correction : « de même norme » ; « dégradait les sorties dans la carte d'Opus 4.8, à 0,10× ». « highly dataset-dependent » est bien dans la fiche 2.")
c[25] = ('conforme', "Objectif implanté décrit en clair, « artificially easy to discover » (citation exacte), seule équipe en échec : celle sans accès aux données (fiche 16). Parades (conclure sur l'instrument ; ablation d'affordance) : programme, partie 8 ; fiche 16. « Aucune parade connue » pour l'organisme trop facile : juste.")
c[27] = ('conforme', "Détecteurs = modèles fine-tunés par LoRA sur une question d'auto-rapport ; 0,95 = progression en distribution pendant l'entraînement (fiche 7 ; explication, partie 2). Parade : écart avec des familles tenues à part, test causal à dégradation appariée, cas connu (fiche 7 ; explication, partie 3).")
c[29] = ('corrigé (P3)', "Chiffre déformé : la source dit que la meilleure de 1 000 directions aléatoires atteint 95,3 % (fiche 15 ; passation, §5.2), pas que « des directions aléatoires la séparent déjà ». Correction : le chiffre et sa portée exacts. Parade partielle (plusieurs recettes, recette tenue à part, comportement inoffensif, organisme d'une autre équipe) : K71 ; « aucune parade connue » pour l'écart implanté/naturel : explication, partie 1.")
c[33] = ('conforme', "Jeu canari sans le déclencheur : pas mieux qu'une red team boîte noire (M5). Parade (jumeau propre réentraîné, second jumeau, filtre empoisonné exprès comme cas connu) : M4 et M9 ; borne large sans parade, dite.")
c[35] = ('conforme', "Masquage sélectif des gradients montré sur de petits modèles (JB10) ; ramener la capacité par réentraînement ne prouve pas le retrait (volet 2, §I). Parade : ré-élicitation contre une référence jamais entraînée, au même budget, modèle connu pour masquer, « not elicitable at this budget » (M4, M5 ; JB10) : doctrine du nul respectée.")
c[37] = ('conforme', "Différentiel nul seulement avec son cas connu (M5 ; G1). Parade (uplift du modèle sans filtre, filtre affaibli exprès, équipe rouge optimisée composante par composante) : M5 ; G1 ; F·24.")
c[41] = ('conforme', "Gain hors distribution lu sur banc agentique, modèles ouverts, scènes reconnaissables comme des tests (F·34). Parade : deux versions tirées au hasard, organisme dressé à se cacher (K63) ; représentativité du banc : « aucune parade connue » (fiche 12).")
c[43] = ('conforme', "Parade manquante ajoutée : juge d'entraînement distinct du juge scellé, métriques d'audit tenues à part, surveillance de la longueur et des motifs de flatterie (programme, partie 8, tableau des menaces) ; juge scellé, audit humain stratifié (programme, partie 3).")
c[47] = ('conforme', "Nul de la porte seulement avec le cas connu du moniteur blanc (M5 ; K70 ; passation, §5.2) ; chiffre de sûreté relatif à l'équipe rouge (F·24). Parade : positifs connus au même seuil, équipe rouge optimisée, rappel à faux positifs fixés avec le ratio de trafic bénin (F·24 ; volet 6, §6).")
c[51] = ('conforme', "Après RL, sondes neuves hors domaine dégradées, sonde neuve dans le domaine quasi parfaite : rapport d'antériorité 3 (*The Obfuscation Atlas*), statut de lecture dit ; itérer contre ses détecteurs sélectionne l'évasion (fiche 19). Parade : sonde neuve, jeu d'indices disjoint, détecteurs scellés hors de la boucle (passation, §5.2 ; programme, partie 3 ; fiche 19).")
c[53] = ('conforme', "« Ils avaient raison » tiré d'un nul d'instrument : cas connu requis (M5 ; passation, §5.2) ; nul dit comme une borne, avec budget et puissance.")
c[59] = ('conforme', "Séparer en distribution ne prouve rien (piège 1 ; fiche 7) ; seule lecture mesurée = corrélation peut-être d'ajustement (README ; volet 6, §2). Parade : items exclus de l'entraînement de la sonde, extraction disjointe, familles entières tenues à part (README ; explication, partie 3).")
c[61] = ('conforme', "La puissance ne remplace pas un cas connu (M5 ; réponse 4). Parade : même instrument montré capable de voir l'effet ; borne avec budget et puissance, jamais une absence.")
c[63] = ('corrigé (P4)', "Sens causal faussé : « ce que le RL a entraîné est la conformité, qui a fait monter le raisonnement » fait de la conformité la cause du raisonnement. La fiche 14 dit : l'entraînement obtient la conformité et fait monter le raisonnement de faux alignement (12 → 78 %), sans que le papier fasse de ce raisonnement la cause de la conformité, qui monte aussi hors surveillance. Correction alignée sur la fiche 14 et sur l'insertion n° 1 de la tranche 53-fin. Le reste (scratchpad, indice construit, jeu de rôle, mémorisation) : fiche 14 ; piège 2 ; fiches, partie C.")
c[65] = ('corrigé (P5)', "« Pour l'extraction supervisée, aucune parade connue » : faux, le programme (partie 8, menace « Nos concepts ne sont pas ceux du modèle ») donne le diffing par crosscoder, qui cherche sans hypothèse. Correction : cette parade, sourcée. Le reste (lien corrélationnel, trait nommé d'avance, baisse de capacités, nul de spécificité puis dégradation appariée) : fiche 8 ; M4 ; piège 4 ; passation, §5.2.")
c[67] = ('corrigé (P6)', "Même faute de logique que P1 (cas connu = les pays, autre concept). Correction : un nul à une direction ne sépare pas « il faut plus d'une direction » d'un instrument aveugle à cette dose. Le reste (« réfutée » vaut pour l'hypothèse forte, à ce réglage ; réponse 3 ; balayage de rang) est exact.")
c[73] = ('conforme', "Note d'étude, hors des lignes « À dire » : détecteurs fine-tunés par LoRA, pas des sondes (fiche 7 ; explication, partie 2). Parade pour une sonde : validation croisée par types tenus à part, test causal, cas connu (fiche 7).")
c[79] = ('conforme', "Ce que la réponse tait : contrôles aléatoires d'origine sans contrôle du dommage ; témoin de même norme = nul de spécificité (volet 6, §2 ; M4). Parade : sous-espaces de même rang à dégradation appariée, courbe effet/dégradation, extraction disjointe (M4 ; programme, partie 7 ; README).")
c[83] = ('conforme', "Fable 5 : dégradation négligeable, mais contrôles « comparable or smaller » sur l'axe du désalignement (fiche 2, citation exacte) ; jugements de dégradation contradictoires d'une carte à l'autre (fiches, partie B). Distinction dommage/spécificité juste. Parade : M4 ; K47 ; fiche 2.")
c[85] = ('conforme', "Mesures de la conscience d'évaluation faiblement corrélées, verbalisation qui rate le non-verbalisé, directions aléatoires qui la font baisser aussi (fiche 2 ; F·25 ; programme, partie 8). Parade : triangulation, critère principal comportemental et sonde latente, organisme conditionné (volet 5, sujet 4 ; programme, partie 8 ; explication, partie 3).")
c[89] = ('corrigé (P24)', "Exact sur F·24 et F·23, mais « pour le réalisme des transcriptions, aucune parade établie » tait la parade partielle de F·25 (juge mis devant la paire ; vraies ressources de déploiement), que donnent pour le même objet l'insertion n° 113 de la tranche 53-fin (B10) et, après P16, la réponse 61. Correction d'alignement, pas d'erreur de fait : parade partielle, sourcée (F·25 ; programme, partie 3), le réalisme restant ouvert (F·23).")
c[91] = ('corrigé (P7)', "Source incomplète : « une sonde neuve après tout entraînement » est attribuée à la passation, §5.2, qui ne la nomme pas ; elle est au programme (partie 3 : jeu δ, sonde neuve E′ ; partie 8 : « La sonde neuve E′ sur des indices δ »). Correction : source ajoutée. Le reste (échec silencieux, canaris, dérive, échantillon mensuel) : K70.")

# ---------------- tranche volet11_21_a_52 ----------------
c = C[TR[1]]
c[1] = ('conforme', "Détecteurs de Hopkins et Khullar = modèle fine-tuné par LoRA qui répond à une question d'auto-rapport ; environ 25 % d'étiquettes révisées (fiche 7 ; explication, §2). Parade : fiche 7. Forme : « explication du 2 octobre, §2 » ici, « partie 2 » ailleurs : même renvoi, laissé tel.")
c[5] = ('conforme', "Note insensible au cadrage = nul ; cas connu : un juge dont le déplacement est déjà mesuré (M5 ; volet 6, §2).")
c[11] = ('corrigé (P8) ; place signalée', "Sondes neuves hors domaine dégradées après RL (rapport 3) ; bascule sur les cas limites (rapport 4, « résumé seul, à vérifier », statut dit). L'indicatif « lit autrement » est porté par le rapport 3. Source manquante pour la sonde neuve et le jeu d'indices disjoint : la passation, §5.2, ne les nomme pas ; programme, parties 3 et 8. « Contre la bascule sous RL, aucune parade connue » : juste. Place : trois insertions (n° 11, 13, 15) entre le premier et le deuxième paragraphe de la réponse 24, imposées par l'unicité de l'ancre ; rien n'est coupé, et la n° 13 annonce « Plus bas ».")
c[13] = ('conforme', "Deux contrôles — aléatoire de même norme = nul de spécificité ; dégradation appariée = dommage — : passation, §5.2 (« Le test causal de la sonde ») ; M4 ; citation de la réponse A4 exacte. Parade : familles d'organismes et organisme honnête vérifiés copie par copie (K71 ; K52).")
c[17] = ('conforme', "Gain dans l'intervalle = nul ; cas connu : sabotage installé exprès, attrapé au même seuil (M5 ; passation, §5.2) ; équipe rouge supposée (F·24).")
c[21] = ('conforme', "Taux identique dans les deux bras = nul ; cas connu : organisme conditionné à l'évaluation (programme, partie 4) ; sondes « validées par intervention » contre la dégradation appariée, l'aléatoire de même norme n'étant que le nul de spécificité (M4 ; réponse 19).")
c[25] = ('conforme', "Raisonnement de l'espace privé = rapport, pas cause ; jeu de rôle contre préservation de buts indécidable (fiche 14 ; piège 2). Parade : l'écart de conformité gratuit/payant (fiche 14).")
c[27] = ('conforme', "Mémorisation possible : transcripts d'*Alignment Faking* réinclus par accident (fiche 14 ; fiche 3, Risk Report §5.2). « Aucune connue ; on le dit » : juste.")
c[31] = ('conforme', "Aléatoire apparié en covariance ≠ contrôle du dommage ; « un chiffre à refaire à dégradation égale » (citation de la réponse A4 ; la réponse 63 porte le chiffre de partition, d'où « réponses 63 et A4 »). Parade : courbe effet/dégradation (programme, partie 7) ; lien corrélationnel (fiche 8).")
c[35] = ('conforme', "Vecteur pris comme instrument : biais de mesure d'un bras à l'autre (passation, §5.2) ; lien corrélationnel (fiche 8). Parade : sonde par bras, sonde neuve, jeu disjoint (passation, §5.2 ; programme, partie 3).")
c[39] = ('corrigé (P9)', "Transcriptions synthétiques, risque de lire le texte (programme, partie 8 ; réponse 21) : exact. La parade disait « au premier jeton … ou au jeton d'action » ; le programme, cité, lit aux deux (partie 3 : « Deux positions de lecture » ; partie 8 : « avant toute raison, et au jeton d'action »), comme l'encadré du 2 octobre de la v3.6 et la correction du groupe 2 sur l'encadré « Sondes ». L'explication source dit « ou » ; on suit le programme. Correction : « aux deux positions … et ».")
c[43] = ('conforme', "Proxy de sabotage = juge LLM, Sonnet 4.6 avec le papier (F·22) ; erreurs systématiques (volet 6, §2). Parade : juge scellé, audit humain d'environ 200 items stratifiés, accord rapporté (programme, partie 3).")
c[45] = ('conforme', "Signal interne cumulé qui ne bat pas le scorer faible = nul ; cas connu : sabotage installé dans le générateur ; sinon une borne (passation, §5.2 ; M5).")
c[49] = ('conforme', "Écart faible-vers-fort fermé par des idées propres au jeu de données (JB8). Parade : tâche à vérité connue, items où le superviseur se trompe, copie entraînée sur les vraies étiquettes (JB8).")
c[53] = ('conforme', "Environ 25 % d'étiquettes révisées après un juge GPT-5 ; détecteurs testés sur Gemma et Qwen seulement (fiche 7). Parade : « révisées », jamais « inversées » ; audit humain (fiche 7 ; programme, partie 3) ; portée : « aucune parade connue », juste.")
c[59] = ('conforme', "Taux de reward hacking stable = nul ; cas connu : organisme dressé à se cacher (K63) ; réalisme par paires = juge LLM, scellé et audité par des humains (F·25 ; programme, partie 3).")
c[63] = ('conforme', "Nul de CHIVE borné : trois outils en lecture seule, au plus cinq appels, éditions de prompt, baseline forte ; étiquettes par un classifieur LLM non validé (fiche 4 ; F·30). Parade : la barre de la fiche 4 (éditions qui dissocient surface et variable, contrôle qui la préserve).")
c[67] = ('conforme', "AUROC hors distribution ≠ rappel au seuil : 43 % contre 55 % à 1 % de faux positifs (F·51). Parade : rappel à 1 % de faux positifs, baseline boîte noire ou prompt à coût égal (F·50 ; volet 5, sujet 1).")
c[71] = ('conforme', "Façons de tricher enseignées d'abord au modèle, ce qui confond le résultat de généralisation (fiche 13, limites de NEM). « Aucune connue ; on le dit » : juste.")
c[73] = ('conforme', "« Aucun transfert » = nul, cas connu requis (M5) ; « high-dimensional » (fiche 13, citation exacte). Parade : organisme où l'on a installé la disposition, même budget, batterie lue dimension par dimension.")
c[77] = ('encadré ; limite 6 corrigée (P10)', "Format fixe respecté (titre, « (v3.6, 2 octobre 2026) », « Limite : » / « Parade : », sources en italique). Chiffres vérifiés : 25 % et 39 %, plus de 99 % contre moins de 2 % (fiche 17) ; environ 1 % contre environ 50 %, un seul moniteur (fiche 3) ; entraîner contre le moniteur (fiche 17 ; fiches, partie C) ; verbalisation et directions aléatoires (fiche 10 ; fiche 2 ; programme, partie 8) ; « not verbalized », jamais « hidden reasoning » (fiche 17). Faute : la limite 6 (×2,4 à 2,9, rapport 4, résumé seul) disait « Parade : aucune connue » alors que le programme, partie 8, donne la parade (critère principal comportemental, sonde latente comme contrôle : la verbalisation n'est jamais la mesure). Place : réponse 43, que visent les renvois « chaîne de pensée comme moniteur ».")
c[79] = ('conforme', "Écart nul entre cadrages = nul, cas connu (M5) ; remontée sous inhibition seulement au-delà de deux contrôles (M4). Parade : organisme entraîné à sous-performer (F·26 ; K63) ; aléatoire de même norme puis dégradation appariée (réponse 19).")
c[83] = ('conforme', "Injection de concept : environ une fois sur cinq (Opus 4.1), « zéro faux positif » sur 100 essais témoins, détails embellis ou confabulés (fiche 11). « Aucune parade connue » contre la confabulation : juste.")
c[85] = ('conforme', "Intervention de même norme = nul de spécificité ; rapport immobile ne dit « texte sur l'état » que si l'état a bougé (M4 ; M5). Parade : direction aléatoire à dégradation appariée, sonde de vérification, injection de concept comme cas connu (fiche 11).")
c[89] = ('conforme', "Patch de l'état complet = plafond, pas explication (volet 6, §2 ; programme, partie 8) ; partition à refaire (A4). Parade : protocole A4, balayage de rang sur sous-espaces emboîtés (A4 ; volet 6, §6).")
c[93] = ('corrigé (P11)', "Même faute que P2 : « des vecteurs aléatoires » sans « de même norme », et « chaque direction dégrade les sorties » généralisé alors que c'est le constat de la carte d'Opus 4.8, à 0,10× (fiche 2). Parade (dégradation appariée, courbe dose-réponse, vecteur par vecteur) : M4 ; réponse 19 ; programme, partie 7.")
c[95] = ('conforme', "« Aucun écart, sur aucune évaluation » = nul ; cas connu : organisme conditionné (programme, partie 4) ; borne, pas certification (M5).")
c[99] = ('corrigé (P12)', "Biais de mesure d'un vecteur calibré ailleurs (passation, §5.2) et nul sans cas connu (M5) : exact. Source manquante pour la sonde neuve et le jeu disjoint : programme, parties 3 et 8.")
c[103] = ('conforme', "Étiquettes corrigées contre brutes ne départagent pas imitation et dépassement ; tâche binaire (JB8). Parade : superviseur faux au hasard à côté du superviseur faux dans un sens fixe, copie sur les vraies étiquettes, accord là où le superviseur a raison (JB8).")
c[107] = ('conforme', "Différentiel nul : il faut un banc qui sépare et un attaquant qui a assez cherché (M5 ; M7). Parade : uplift du modèle nu, filtre affaibli, budget d'attaque fixé d'avance (G1 ; M7).")
c[111] = ('conforme', "Masquage sélectif sur petits modèles (JB10) ; coût de ré-apprentissage = borne à un budget (M5). Parade : « aucune connue » pour l'échelle, ré-élicitation à budget fixé pour la borne.")
c[113] = ('corrigé (P13)', "Portée élargie : le Logit Lens qui ne trouve plus rien et les 64,7 % rendus par le retrait d'une direction par couche sont donnés pour RMU (cours, volet 10, Łucki et al. : « Contre RMU, seul le Logit Lens échoue »), pas pour le désapprentissage en général. Correction : « après désapprentissage par RMU ». Parade (trancher par une intervention, ré-élicitation, cas connu) : fiches, partie C ; volet 2, §I ; M5.")

# ---------------- tranche volet11_53_et_fin ----------------
c = C[TR[2]]
c[1] = ('conforme', "Scratchpad caché avec consigne, indice gratuit/payant construit, jeu de rôle contre préservation de buts ; le RL qui fait monter le raisonnement fait aussi monter la conformité hors surveillance, sans que le papier fasse du raisonnement la cause (fiche 14 ; fiches, partie C ; piège 2). Parade, et « aucune parade connue » pour la mémorisation : fiche 14 ; fiches, partie C.")
c[5] = ('corrigé (P14)', "Même faute que P2 : aléatoire sans « de même norme » ; dégradation de chaque direction généralisée (Opus 4.8, 0,10×). Le reste — effet modeste et dépendant du jeu de données, contrôles qui bougent dans le même sens, Opus 4.6 sans différence notable sur la tromperie et la complaisance — est dans la fiche 2 et la contre-lecture.")
c[7] = ('conforme', "LoRA, auto-rapport, 0,95 en distribution, plateau 0,70–0,75 entre catégories, à peine mieux qu'un prompt (fiche 7 ; explication, partie 2). Parade : fiche 7 ; explication, partie 3.")
c[9] = ('conforme', "Partition non mesurée à dégradation égale (A4) ; aléatoire apparié en covariance plus fort (volet 6, §2 et §3) ; seule lecture sur Llama = corrélation peut-être d'ajustement (README). Parade : protocole A4, items exclus (A4 ; programme, partie 8 ; README).")
c[15] = ('conforme', "Gain du midtraining de spécification lu sur modèles ouverts, scènes reconnaissables (F·34). Parade : K63 ; représentativité du banc : « aucune parade connue » (fiche 12).")
c[17] = ('corrigé (P15)', "« Plus faiblement » généralisé : c'est le constat de la carte d'Opus 4.8 (fiche 2) ; la reproduction externe sur un modèle à poids ouverts a trouvé des contrôles « aux effets aussi forts » (cours, volet 11, réponse 19). Correction : les deux constats, chacun sourcé. Le reste (sonde qui lit « je suis surveillé » ; transcripts honnêtes rédigés comme des tests, organisme conscient mais honnête) : volet 6, §8 ; K67.")
c[21] = ('corrigé (P16)', "Contradiction interne : l'insertion cite elle-même la mesure de réalisme par paires (F·25), puis dit « pour le réalisme des transcriptions synthétiques, aucune parade connue » ; l'insertion n° 113 (B10) donne pour le même objet une parade partielle tirée de F·25. Correction : parade partielle (juge mis devant la paire, scellé et audité par des humains ; vraies ressources de déploiement), sourcée (F·25 ; programme, partie 3), le réalisme restant ouvert (F·23). Le reste (attaques conçues à la main ; rejouer dans un vrai harnais au seuil calibré) : F·23 ; B14.")
c[25] = ('corrigé (P17)', "Logique inversée : l'insertion exigeait, pour que « ne généraliseraient jamais » compte, un cas connu où la sonde attrape hors distribution l'intention installée — ce qui réfuterait la proposition au lieu de l'établir. Ce qui l'établit : hors distribution, sur un organisme où l'intention est installée, une sonde qui reste muette ; sur un modèle naturel, son silence ne départage pas « elle ne généralise pas » et « il n'y a rien à voir » (passation, §5.2 ; explication, partie 1 ; M5). La parade (familles tenues à part, organisme, borne) est inchangée et juste.")
c[29] = ('conforme', "Note d'étude, « sans rien changer à la position » : la ligne « À dire » n'est pas touchée. « Moins d'un pour cent » non mesuré à dégradation égale (A4 ; volet 6, §2 et §3). Parade : protocole A4.")
c[31] = ('conforme', "AUROC en distribution ≠ preuve (piège 1 ; fiche 7). « Sinon le nul peut venir d'un rang trop bas » reprend la fiche 7, et ici le cas connu est « au même rang, à la même dose et au même seuil que la mesure », sans autre concept : la logique de la fiche 7 (cas positif sur le même concept) tient, à la différence de P1 et P6.")
c[37] = ('corrigé (P18)', "Même faute que P9 : « au premier jeton … ou au jeton d'action » ; le programme (parties 3 et 8), cité, lit aux deux positions. Le reste (indice de surface, lecture du texte ; deux familles ≠ écart implanté/naturel ; organisme d'une autre équipe ; « aucune parade connue » pour cet écart) est sourcé (volet 2, §C ; volet 6, §8 ; passation, §5.2 ; fiche 15 ; K71 ; explication, partie 1).")
c[41] = ('conforme', "Échec sur « adaptateur léger » : deux cas connus requis — implant vérifié copie par copie, sonde qui attrape au même seuil les cas tenus à part de la famille réussie (K71 ; K52 ; M5). Parade : comportement inoffensif planté par les deux recettes (K71).")
c[43] = ('conforme', "Détecteurs fine-tunés par LoRA, 0,95 en distribution (fiche 7 ; explication, partie 2). Parade : écart en distribution/familles tenues à part, test causal (fiche 7 ; explication, partie 3).")
c[47] = ('conforme', "J-lens : Claude seulement, un seul token, trois sens de « charge » (fiche 1 ; C bis ; volet 6, §6). Parade : porte G9, tuned lens déclaré, charge d'un concept de plusieurs tokens sur un jeu de tokens (programme, partie 3), prédicteur gelé.")
c[51] = ('conforme', "« Indiscernable de zéro » = nul ; cas connu dans le même dispositif ; borne (M5) ; dix chercheurs et 92 paires (F·41).")
c[55] = ('conforme', "La garantie borne les fausses alarmes, pas les ratés (K70) ; test séquentiel déjà publié sur des scores boîte noire (F·55). Parade : canaris, dérive, échantillon mensuel (K70) ; « I haven't seen that combination measured », jamais « first » (F·52 et F·55) : doctrine d'antériorité respectée.")
c[59] = ('conforme', "« Moins d'un pour cent contre soixante-huit » non mesuré à dégradation égale (A4 ; volet 6, §2 et §3). Parade : protocole A4.")
c[63] = ('conforme', "Même constat que la n° 51 de la tranche 1-20 (rapport 3 ; fiche 19), mêmes parades et sources.")
c[67] = ('conforme', "Sous-espace de rang trois qui déplaçait la valence ; effet non revenu sur générations fraîches (volet 6, §2 ; README) ; résidu du dictionnaire (README). Parade : témoin sans pression et concept rival à dégradation appariée (M4) ; « aucune parade connue » pour trancher : juste.")
c[69] = ('conforme', "Réalisme par paires de Kissane ≠ ressemblance implanté/naturel (F·25 ; passation, §5.2 ; fiche 15). Parade partielle (plusieurs recettes, une tenue à part, organisme d'une autre équipe) : K71 ; « aucune parade connue » pour l'écart lui-même : explication, partie 1 ; M5.")
c[73] = ('conforme', "Transcriptions conçues à la main : la sonde lit le texte d'un autre (F·23 ; B14 ; programme, partie 8). Parade : trajectoires produites par le modèle, organisme comme cas connu, lecture au jeton d'action avec raisons neutres préremplies (l'une des deux positions du programme, celle d'une trajectoire d'actions ; pas de contradiction), seuil calibré sur variantes bénignes (F·23).")
c[77] = ('corrigé (P19)', "« Un contrôle aléatoire de l'inhibition n'est que le nul de spécificité » : la doctrine vaut pour l'aléatoire de même norme (M4). Correction : « Pour l'inhibition, un contrôle aléatoire de même norme … ». Le reste (verbalisation, mesures faiblement corrélées, parade) : programme, parties 3 et 8 ; fiche 2 ; volet 5, sujet 4 ; M4.")
c[81] = ('conforme', "Récupération par des idées propres au jeu de données ; tâche binaire (JB8). Parade : JB8.")
c[85] = ('corrigé (P20)', "Même faute que P15 (« plus faiblement » généralisé). Le reste (« moins d'un pour cent » à refaire, A4 ; parade : M4, K47, A4) est exact.")
c[87] = ('conforme', "On connaît la règle installée, pas ce que croit le modèle ; organisme qui ne suit pas sa règle à la lettre et ne distingue pas de façon fiable à partir d'indices subtils (fiche 10). Parade : étiquette par la conduite, jamais par la sonde ; formulations tenues à part ; organisme comme cas connu (passation, §5.2 ; explication, parties 2 et 3 ; programme, parties 3 et 4).")
c[91] = ('conforme', "Juge fort = juge LLM, erreurs partagées possibles (volet 6, §2 ; piège 6 ; fiche 2). Parade : JB8 ; juge scellé et audit humain (programme, partie 3) ; « aucune parade connue au-delà » pour un juge proche du modèle (piège 6).")
c[97] = ('conforme', "Projection d'un bras à l'autre = effet + biais de mesure (passation, §5.2) ; lien corrélationnel (fiche 8). Parade : sonde neuve par bras, direction extraite dans la base, trait au test comme critère principal, projection en mesure séparée (passation, §5.2 ; programme, partie 3) : doctrine des sondes respectée.")
c[99] = ('conforme', "Avantage du midtraining lu sur modèles ouverts, scènes reconnaissables (F·34). Parade : K63.")
c[103] = ('corrigé (P21)', "Formule absente de la source citée : « un pot de miel ne sépare pas un modèle qui le lit comme factice d'un modèle qui se retient » n'est pas dans la fiche 3, qui ne concède que le confondeur « dans une simulation, « c'est faux » est vrai » ; « remarquer le test et se retenir » vient de K63 (cours, volet 2, §B : « il se retiendrait partout où il repère un test »), non cité. Correction : formule retirée, K63 ajouté ; la fin dit « contre le confondeur de la simulation lui-même et contre la mémorisation, aucune parade connue ». Même constat que les groupes 2, 3, 4 et 6.")
c[107] = ('conforme', "Un petit fine-tuning peut créer la capacité (K63) ; citation de la réponse B9 avec […], sous quinze mots. Parade : budget fixé d'avance, borne, gain au-delà du même budget sur un modèle sans la capacité, organisme sous-performant (M7 ; K63 ; F·26).")
c[109] = ('corrigé (P22)', "Contrôles confondus : le simple prompt (K4 du programme) n'a ni rang ni dégradation à apparier ; K1 à K3 se comparent au même rang, à dégradation appariée (programme, parties 3 et 7). Correction : « sous-espaces aléatoires, contrastes sans rapport et directions de forte variance, au même rang et comparés à dégradation appariée, plus un simple prompt ». Le reste (contrôles arbitraires qui bougent aussi, nul de spécificité, organisme conditionné) : fiche 2 ; M4 ; explication, partie 3.")
c[113] = ('corrigé (P23)', "Même formule du pot de miel, attribuée à la fiche 3, qui ne la porte pas. Correction : « un modèle peut remarquer le test et s'y conduire mieux » (K63 : les tests remarqués sous-estiment la propension ; fiche 13 : les modèles peuvent savoir qu'ils sont évalués), et la fin sans la fiche 3 : « contre un moniteur qui reconnaît encore ces attaques comme factices, aucune parade connue ; on le dit ». La parade partielle tirée de F·25 est exacte.")
c[117] = ('conforme', "Retirer une direction abîme aussi le modèle ; l'ablation dit la nécessité, pas la spécificité (M4). Parade : sous-espaces de même rang et direction rivale « la réponse est vraie », à dégradation appariée (M4).")
c[121] = ('conforme', "1,0 contre 0,35 = une tâche sur douze, organisations simulées, fiche faite sur le résumé seul (F·39). Parade : le dire tel, lire l'article en entier (F·39).")
c[125] = ('conforme', "0,88 = AUROC d'un détecteur fine-tuné sur des modèles rendus malhonnêtes ; types tenus à part non dits (F·62 ; pièges 1 et 5 ; fiche 7) ; réserve de la version française valable pour l'anglaise (M10, item 12). Parade : validation croisée par types, conclure sur l'instrument (fiche 7 ; programme, partie 8).")
c[127] = ('conforme', "Déplacement nul = nul, cas connu au même réglage, borne (M5) ; retour des mensonges sous inhibition seulement à dégradation appariée, étiquette vérifiée contre la croyance (M4 ; fiche 7). Parade : M4 et M5 ; fiche 7.")
c[131] = ('conforme', "Case vide = nul ; cas connu : organisme rejoué dans le même harnais ; modèle qui peut reconnaître le test (M5 ; fiche 13 ; volet 2, §B). Parade : cas connu, deux versions (K63), budget fixé, borne (M5, M7).")

RENVOI = "Renvoi : cibles présentes dans la v3.6 (titres, encadrés et ancres vérifiés) ; mêmes cibles, même place en EN."

# ---------------- contrôle de complétude ----------------
for tr in TR:
    for n, x in enumerate(INS[tr], 1):
        if x['fichier'] != 'FR':
            continue
        t = typ(x['texte'])
        if t == 'renvoi':
            assert n not in C[tr], (tr, n, 'renvoi commenté')
        else:
            assert n in C[tr], (tr, n, 'commentaire manquant')
        if (tr, n) in IDX:
            assert C[tr][n][0].startswith('corrigé') or 'corrigée' in C[tr][n][0], (tr, n)
    for n, v in C[tr].items():
        if v[0].startswith('corrigé') or 'corrigée' in v[0]:
            assert (tr, n) in IDX, (tr, n, 'corrigé sans correction')

# ---------------- rédaction ----------------
nb = {tr: {'renvoi': 0, 'avertissement': 0, 'encadré': 0} for tr in TR}
for tr in TR:
    for x in INS[tr]:
        if x['fichier'] == 'FR':
            nb[tr][typ(x['texte'])] += 1

L = []
A = L.append
A("# Vérification du groupe 7 — volet 11, tranches `volet11_1_a_20`, `volet11_21_a_52`, `volet11_53_et_fin`")
A("")
A("*2 octobre 2026. Relecture sceptique des insertions déjà appliquées dans `livrable/COURS_Alignment_v3.6_{FR,EN}_2026-10-02.md`. Corrections dans `travail/corrections_groupe_7.json`.*")
A("")
A("## 1. Portée et méthode")
A("")
tot = sum(len(INS[tr]) for tr in TR)
A(f"- **Ce qui a été vérifié** : {tot} insertions, soit {tot // 2} paires FR/EN.")
for tr in TR:
    A(f"  - `{tr}` : {len(INS[tr])} insertions, soit {len(INS[tr]) // 2} paires — {nb[tr]['avertissement']} avertissements ponctuels, {nb[tr]['renvoi']} renvois, " + ('aucun encadré.' if nb[tr]['encadré'] == 0 else f"{nb[tr]['encadré']} encadré."))
A("- **Pièces lues** :")
A("  - les deux v3.5 et les deux v3.6 ;")
A("  - les fichiers `insertions_*.json` et `applique_*.md` des trois tranches ;")
A("  - toutes les pièces : programme, passation v1.2, explication du 2 octobre, lectures prioritaires (fiches et parties B et C), contre-lecture, rapports d'antériorité des 1er et 2 octobre, README du dépôt ;")
A("  - les fiches F·xx, les cas K, JB et G et le volet M de la v3.5, pour les sources « cours, … » ;")
A("  - les corrections et vérifications des groupes 1 à 6, pour la cohérence.")
A("- **Contrôles mécaniques** :")
A("  - chaque insertion est présente une fois dans la v3.6 et absente de la v3.5 ;")
A("  - places : table de correspondance des lignes v3.5 → v3.6 ; chaque paire FR/EN est sous la même réponse, à la même ancre (0 écart) ;")
A("  - les cibles des renvois existent dans la v3.6 : les 30 ancres citées, FR et EN, y sont présentes, et chaque encadré visé est à sa place ;")
A("  - formats fixes, citations de moins de quinze mots, sigles (aucun sigle inventé : R1 est le nom de DeepSeek R1).")
A("- **Contrôles du JSON** :")
A("  - chaque « ancien » est une ligne entière d'insertion (deux lignes pour l'encadré), présente une seule fois dans la v3.6 et absente de la v3.5 ;")
A("  - l'unicité tient après les corrections des groupes 1 à 6, appliquées avant ou après celles-ci : 0 échec dans les deux ordres, aucun chevauchement ;")
A("  - le préfixe de format est gardé, les paires FR/EN sont complètes, et le JSON se recharge sans erreur.")
A("- **Lecture** : chaque avertissement et l'encadré ont été lus contre les sources qu'ils citent. Une phrase sans source est une faute ; une parade connue mais tue aussi.")
A("")
A("## 2. Bilan")
A("")
A(f"**{len(ORDRE)} paires fautives, {len(CORR)} corrections** (une FR et une EN par paire). Toutes les autres insertions sont conformes.")
A("")
A("| Nature de la faute | Paires | Corrections |")
A("|---|---|---|")
A("| Doctrine : « aléatoire » sans « de même norme » pour le nul de spécificité | 23 (1-20) ; 93 (21-52) ; 5, 77 (53-fin) | P2, P11, P14, P19 |")
A("| Portée d'un constat élargie : dégradation à 0,10× (Opus 4.8) ; « plus faiblement » (Opus 4.8 ; la reproduction externe les trouve aussi forts) ; 64,7 % et Logit Lens (RMU) ; 95,3 % (meilleure de 1 000) | 23, 29 (1-20) ; 93, 113 (21-52) ; 5, 17, 85 (53-fin) | P2, P3, P11, P13, P14, P15, P20 |")
A("| Logique du cas connu et du nul | 13, 67 (1-20) ; 25 (53-fin) | P1, P6, P17 |")
A("| Sens causal faussé (faux alignement) | 63 (1-20) | P4 |")
A("| « Aucune parade » alors qu'une parade est dans les pièces | 65, 89 (1-20) ; 77, limite 6 (21-52) ; 21 (53-fin) | P5, P24, P10, P16 |")
A("| Source manquante pour la sonde neuve et le jeu d'indices disjoint | 91 (1-20) ; 11, 99 (21-52) | P7, P8, P12 |")
A("| Positions de lecture : « ou » au lieu des deux positions du programme | 39 (21-52) ; 37 (53-fin) | P9, P18 |")
A("| Formule absente de la source citée (pot de miel, fiche 3) | 103, 113 (53-fin) | P21, P23 |")
A("| Contrôles confondus : le prompt n'a ni rang ni dégradation appariée | 109 (53-fin) | P22 |")
A("")
A("**Correspondance avec le JSON** (numéros d'ordre des entrées, FR puis EN) :")
A("")
for p, tr, n in ORDRE:
    _, i, j = IDX[(tr, n)]
    A(f"- {p} : `{tr}` FR n° {n} / EN n° {n + 1} → entrées {i} et {j}")
A("")
A("## 3. Constats transverses")
A("")
A("- **Le vrai** :")
A("  - les fautes de fond sont dans le tableau ci-dessus ;")
A("  - les chiffres conservés ont tous été retrouvés dans leur source : 0,95 et 0,70–0,75 ; 25 % et 39 % ; plus de 99 % contre moins de 2 % ; environ 1 % contre environ 50 % ; 43 % contre 55 % ; 95,3 % ; 64,7 % ; ×2,4 à 2,9 ; dix chercheurs et 92 paires ; 1,0 contre 0,35 ; 0,88 ; environ 25 % d'étiquettes révisées ; une fois sur cinq et 100 essais témoins ;")
A("  - les statuts de lecture des rapports d'antériorité sont dits (« résumé seul », « lu de façon ciblée »).")
A("- **La doctrine** :")
A("  - après correction, l'aléatoire de même norme n'est partout que le nul de spécificité ;")
A("  - le dommage ne s'écarte qu'à dégradation appariée ;")
A("  - chaque nul d'instrument est assorti de son cas connu et dit comme une borne ;")
A("  - aucune revendication d'antériorité : « I haven't seen that combination measured », jamais « first » ;")
A("  - les sondes restent une mesure séparée, jamais l'étiquette principale.")
A("- **La place** :")
A("  - aucun tableau, aucune liste, aucun paragraphe coupé ;")
A("  - deux places à signaler, sans correction possible par le texte : la réponse 2 (n° 5 de la tranche 1-20) et la réponse 24 (n° 11, 13 et 15 de la tranche 21-52).")
A("- **Les deux langues** : même contenu, même place pour les 172 paires ; les 24 corrections sont faites en paire. L'introduction anglaise du volet 11 est en français dès la v3.5 : hors du texte ajouté, non touchée.")
A("- **La forme** :")
A("  - formats fixes respectés (avertissement « > ⚠ *(v3.6)* », renvoi « > ⚠ **Limites et parades** : … *(v3.6)* », encadré) ;")
A("  - citations de moins de quinze mots ; aucune ligne « À dire » touchée, aucun chiffre ajouté à une forme nommée ;")
A("  - deux variantes de citation laissées telles (« explication du 2 octobre, §2 » et « partie 2 ») ;")
A("  - « aucune parade établie » (réponse 20) est remplacée par P24.")
A("- **Cohérence avec les groupes 1 à 6** : chaque correction rejoint un constat déjà fait ailleurs.")
A("  - P1 et P6 : groupe 1 ;")
A("  - formule du pot de miel (P21, P23) : groupes 2, 3, 4 et 6 ;")
A("  - attribution de la dégradation à Opus 4.8 (P2, P11, P14) : groupes 2 et 4 ;")
A("  - « plus faiblement » (P15, P20) : groupe 5 ;")
A("  - deux positions de lecture (P9, P18) : groupe 2, sur l'encadré « Sondes », et l'encadré du 2 octobre de la v3.6 ;")
A("  - une fois les groupes 1 à 7 appliqués, ni la formule du pot de miel ni « aucune parade établie » ne restent dans les deux fichiers.")
A("")
A("## 4. Insertion par insertion")
A("")
A("Colonnes :")
A("")
A("- n° FR / n° EN : rang dans `insertions_<tranche>.json` ;")
A("- place : réponse, puis ligne de la v3.6 FR / EN ;")
A("- type : avertissement, renvoi ou encadré.")
A("")
A("Les renvois ont tous été vérifiés de la même façon.")
A("")
TITRES = {TR[0]: 'Tranche `volet11_1_a_20` (réponses 1 à 20)', TR[1]: 'Tranche `volet11_21_a_52` (réponses 21 à 52)', TR[2]: 'Tranche `volet11_53_et_fin` (réponses 53 à 63, A1 à A17, B1 à B14)'}
for tr in TR:
    A(f"### {TITRES[tr]}")
    A("")
    A("| n° FR / EN | Place | Type | Verdict | Constat |")
    A("|---|---|---|---|---|")
    for n, x in enumerate(INS[tr], 1):
        if x['fichier'] != 'FR':
            continue
        lab, lfr, nen, len_ = PLACE[(tr, n)]
        assert nen == n + 1
        t = typ(x['texte'])
        if t == 'renvoi':
            v, cm = 'conforme', RENVOI
        else:
            v, cm = C[tr][n]
        if (tr, n) in IDX:
            p, i, j = IDX[(tr, n)]
            cm += f" *(JSON : entrées {i} et {j})*"
        cm = cm.replace('|', '/')
        A(f"| {n} / {n + 1} | {lieu(lab)} — l. {lfr} / {len_} | {t} | {v} | {cm} |")
    A("")
A("## 5. Alertes")
A("")
A("1. **Réponse 2** (n° 5 de la tranche 1-20) :")
A("   - où : FR l. 5092, EN l. 5333 ;")
A("   - quoi : l'avertissement sur le juge s'intercale entre l'annonce « trois choses autour » et « La première » ;")
A("   - pourquoi pas corrigé : rien n'est coupé, et le déplacer exigerait de toucher une ligne de la v3.5 ;")
A("   - à trancher à la main.")
A("2. **Réponse 24** (n° 11, 13 et 15 de la tranche 21-52) :")
A("   - quoi : trois insertions entre les deux premiers paragraphes, imposées par l'unicité de l'ancre ;")
A("   - lecture : cohérente, la n° 13 annonce « Plus bas ».")
A("3. **P9 et P18 suivent le programme** (« deux positions … et »), contre le « ou » de l'explication source :")
A("   - c'est le choix de l'encadré du 2 octobre de la v3.6 et du groupe 2 ;")
A("   - si l'on préfère l'explication, il faut revenir ensemble sur l'encadré « Sondes », l'encadré du 2 octobre et ces deux insertions.")
A("4. **P24 est une correction d'alignement**, pas une erreur de fait : la réponse 20 suit désormais B10 et la réponse 61 sur la parade partielle de F·25.")
A("5. **Rapport d'antériorité 4**, « résumé seul » :")
A("   - il porte encore deux énoncés du volet 11 : la bascule sous RL (réponse 24) et la limite 6 de l'encadré « Chaîne de pensée » ;")
A("   - le statut est dit dans le texte ; à vérifier sur le rapport avant publication.")
A("")
open(f'{W}/travail/verif_groupe_7.md', 'w', encoding='utf8').write('\n'.join(L) + '\n')
print('écrit', len(L), 'lignes')
