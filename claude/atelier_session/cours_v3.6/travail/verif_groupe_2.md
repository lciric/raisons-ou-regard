# Vérification — groupe 2 : tranche volet2_A_a_D (cours v3.6, 2 octobre 2026)

Périmètre : les 25 insertions françaises (n° impairs 1 à 49 de `applique_volet2_A_a_D_FR.md`) et les 25 anglaises (n° pairs 2 à 50 de `applique_volet2_A_a_D_EN.md`), relues dans la v3.6 avec le texte qui les entoure (FR, lignes 589 à 1071 ; EN, lignes 674 à 1160).

Pièces relues pour vérifier : l'explication source du 2 octobre ; les fiches 1, 2, 3, 5, 7, 8, 10, 12, 13, 15, 16 et les parties B et C des lectures prioritaires ; la contre-lecture des fiches ; le programme v1.1, parties 3, 4, 7 et 8 ; la passation v1.2, §5.1 et §5.2 (et §4.2, §5.5) ; les rapports d'antériorité 3, 4 et 5 du 2 octobre ; le README du dépôt ; et, dans le cours v3.5, le volet M (M4, M5, M7, M8), le volet 2 (§A à §D, cas K71, K63, K47, K72, K64 ; §E, K52 ; §H, G1), le volet 3, §4 (K67), le volet 4 (Monosemanticity, Circuit Tracing), le volet 5, partie II, A (sujets 1 et 2), le volet 6 (§2, §3, §6, §8), le volet 7 (F·7, F·8, F·9, F·25, F·29, F·50, F·51, F·62), le volet 10 (n° 27, 30, 53) et le volet 11 (A7).

## Bilan

- **Place.** Les 20 ancres FR et les 20 ancres EN sont des fins de paragraphe (ligne suivante vide, vérifié dans les deux sources) : aucune insertion ne coupe un paragraphe, une liste ou un tableau. Les insertions FR et EN sont au même endroit, dans le même ordre (même paragraphe d'ancrage, n° FR = n° EN − 1).
- **Renvois.** Toutes les destinations citées existent, dans les deux langues : M4 (après « La direction aléatoire de même norme » ; après « La dose-réponse »), M5 (fin de section), §B, §C (deux), §D, §G (après « les coup probes »), §H (après « StrongREJECT »), C bis, volet 4 (Monosemanticity ; Circuit Tracing), volet 6, §2 (après « La loi de déplacement »), volet 10 (après la fiche Patchscopes, n° 14), volet 11 (réponse 43).
- **Doctrine.** Aucune insertion ne dit qu'un contrôle aléatoire écarte le dommage : partout, l'aléatoire de même norme est donné comme le nul de spécificité, et le dommage comme écarté seulement à dégradation (ou dommage) appariée. Aucune formule « first ». Deux encadrés d'instrument (ablation et projection ; crosscoders) omettaient le nul et son cas connu : complétés (corrections 10 et 11).
- **Forme.** Formats fixes respectés (encadrés, renvois, avertissements) ; citations de moins de quinze mots ; aucun sigle inventé (seuls des identifiants du cours — M4, K47, F·25, G1 de la banque — et des sigles courants : SAE, AUROC, LoRA, RL, NLA).
- **Langues.** Les versions anglaises disent la même chose que les françaises ; les fautes relevées sont donc dans les deux, et chaque correction a son double.
- **Corrections.** 11 par langue, 22 au total, dans `corrections_groupe_2.json`. Simulées sur une copie de la v3.6 : chaque « ancien » est présent une seule fois, n'est jamais une ligne de la v3.5, disparaît après application (deux corrections qui ajoutent une puce restent donc sans effet si l'outil est relancé), et toutes les lignes de la v3.5 restent présentes dans l'ordre.

## Insertion par insertion

**n° 1 / 2 — renvoi, fin du préambule (FR 611, EN 696).** Red-teaming et moniteurs du contrôle, destinations exactes. Sans faute.

**n° 3 / 4 — encadré du 2 octobre, partie 1 (FR 622, EN 708).** L'explication source est reprise en entier ; ses corrections sont exactes et dites :
- point 2 : 80 à 86 % contre 34 %, construction en deux étapes, et la limite « ne distingue pas de façon fiable » viennent bien de la fiche 10 ;
- point 3 : les deux réserves sont dans le README (sorties brutes non conservées ; ρ peut-être d'ajustement) ;
- point 4 : la porte du lens est bien définie dans la partie 3 du programme (la partie 4 ne fait que la citer) ; Zeisler, 6,3 à 11,1 % contre 54 à 70 %, et la revue de Nanda sur Qwen 3.6 27B sont dans le rapport 5, lus par résumé ; les 54, 70 et 70 % sont ceux du raisonnement en plusieurs étapes (fiche 1), et le titre du billet porte sur ce raisonnement : l'inférence « vraisemblablement » est fondée ;
- « régression logistique régularisée » n'a de source nulle part : la correction (partie 2) est juste.

La limite du cas connu (95,3 % ; saillance due à l'insertion) est dans la fiche 15, la passation, §5.2, et M5. Les parades citées (K71 ; volet 6, §8) existent. Sans faute.

**n° 5 / 6 — encadré « Organismes modèles » (FR 639, EN 725).** Limites et parades sourcées : fiche 15, piège 5 ; fiche 16 (objectif en clair, « artificially easy to discover ») ; K52 (« parfois, pas toujours ») et K71 ; rapport 5 (*The Model Organism Lottery*, résumé lu) ; fiche 13 (hacks fournis) ; partie C (transcripts réinclus) ; programme, partie 8 (8B, environ 32B).
- **Faute légère (vrai)** : « n'a été trouvé dans aucun système réel » déforme la fiche 15, qui dit « has not yet been found in any AI system » (« yet » perdu, « réel » ajouté). Correction 1 : la citation exacte (neuf mots).

**n° 7 / 8 — renvoi, cas connu de K71 (FR 684, EN 770).** Sans faute.

**n° 9 / 10 — encadré « Évaluations comportementales et pots de miel » (FR 706, EN 793).** Limites 2 à 5 et 7 vérifiées : F·25 (conscience verbalisée, juge devant la paire, ressources de déploiement) ; §B et K63 (sous-élicitation, budget fixé, gain au-delà du même budget) ; M7 ; fiche 13 (4,34 → 4,20, « high-dimensional ») ; fiche 12 (« narrowly … the symptom », métriques tenues à part) ; §B, §H, G1 et M4 (préjudice différentiel, notation à l'aveugle, bras de référence réaliste).
- **Faute (vrai), limite 1** : « se retenir » n'est pas ce que montre le chiffre cité. Dans la fiche 13, la triche discrète *monte* de 4,0 % à 18,9 % quand on annonce un classifieur : le modèle cache sa triche, il ne se retient pas. La retenue est celle de l'étude de Lynch, citée dans K63. Correction 2 : les deux conduites, chacune avec sa source (K63 ; fiche 13).
- **Faute (vrai), limite 6** : la fiche 3 ne dit pas qu'« un pot de miel ne sépare pas un modèle qui le lit comme factice d'un modèle qui se retient ». Son confondeur, concédé pour la réplication CTF, est autre : dans une simulation, croire « c'est faux » est juste, donc une réplication simulée ne peut pas montrer qu'un modèle croit à tort la situation simulée (fiche 3 ; grille de la partie B, question 8). Correction 3. La parade « aucune connue » reste juste.

**n° 11 / 12 — avertissement sur « la sonde, non » de K63 (FR 737, EN 824).** Passation, §5.2 ; pièges 1 et 3 ; fiche 7 ; trois cas connus de l'explication. Placé entre deux paragraphes du cas, sans en couper un. Sans faute.

**n° 13 / 14 — renvoi, cas connu de K63 (FR 746, EN 833).** Sans faute.

**n° 15 / 16 — encadré « Sondes d'activation » (FR 763, EN 851).** Vérifiés :
- moins de 1 % contre 68 % : volet 6, §2 ;
- la ligne sur les sondes : M8 ;
- la fabrication de l'organisme et la surveillance : volet 6, §8 ; K67 ;
- *Obfuscation Atlas* (rapport 3) et sonde « évaluation contre déploiement » (rapport 4, résumé seul) ;
- F·62 (sondes de vérité moins bonnes qu'un prompt) ; F·51 (43 % contre 55 % à 1 % de faux positifs) ; F·50 ; F·29 ; sujet 1 du volet 5 ;
- README (ajustement, ρ 0,684, jeu disjoint) ; M4 (paires qui portent un style, classifieur de surface au hasard) ; §C (négatifs générés par le modèle).
- **Faute (vrai), parade 4** : « Lire au premier jeton …, ou au jeton d'action … ». Le programme lit aux **deux** positions (partie 3 : « Deux positions de lecture » ; partie 8 : « avant toute raison, et au jeton d'action ») ; l'encadré du 2 octobre a corrigé exactement ce point (« Étape 4 »), et la parade le contredisait. Correction 4.
- Note, sans correction : la limite 5 (« lit autrement ») est à l'indicatif là où la passation dit « lirait » ; le rapport 3 l'appuie, et la source le dit « rapport ». Acceptable.

**n° 17 / 18 — encadré du 2 octobre, parties 2 et 3 (FR 789, EN 877).** Toutes les références vérifiées :
- régression logistique : volet 5, partie II, A, sujet 1 ; volet 10, n° 27 (coup probes) et n° 30 ;
- RepE : la direction logistique lit le mieux et n'agit presque pas (volet 10, n° 53) ; directions logistiques moins causales que la différence des moyennes, à transfert comparable (n° 30) ;
- fiche 7 : LoRA, auto-rapport, 0,60 → 0,95 au fil de l'entraînement, 0,70-0,75 ;
- programme, partie 3 : jeux d'indices disjoints, couche choisie par l'AUROC sur le jeu de validation, deux positions, familles et distances ; passation, §5.1 et §5.2 ;
- rapports 3 et 4 ; porte de l'organisme à concept planté (programme, parties 3 et 4).

Sans faute.

**n° 19 / 20 — encadré « Pilotage par vecteurs » (FR 819, EN 907).** Vérifiés :
- rang trop bas : fiche 7, contre-lecture ; vecteur de pays : K47 ; balayage : volet 6, §6 ;
- artefact de polarité : README ; « highly dataset-dependent » et dépendance à la couche : fiche 2, F·7 ;
- détection du pilotage, même machinerie, verbalisation : programme, partie 8 ; fiche 2 ;
- persona : fiche 8 ; Drake et Eberstadt, 24 % → environ 50 % : rapport 3, au conditionnel.
- **Faute (place), limite 1** : « chaque direction pilotée dégrade la sortie », dit en général, contredit le paragraphe qui suit (K47), où « the Fable 5 system card » pilote « à dégradation négligeable ». La fiche 2 l'attribue à la carte d'Opus 4.8, à 0,10×. Correction 5 : l'attribution.
- **Faute (source), parade 4** : « Rapporter jeu de données par jeu de données » n'est pas dans la partie 3 du programme, seule citée. Correction 6 : la parade du volet 5, partie II, A, sujet 2 (pré-enregistrer la définition de « ça marche », tester la généralisation d'un dispositif à l'autre), plus le choix de la couche sur le jeu de validation (programme, partie 3).
- **Faute (vrai), parade 7** : « pour l'extraction supervisée, aucune parade connue ». Le programme en donne une, partie 8 : contre « Nos concepts ne sont pas ceux du modèle », le diffing par crosscoder « cherche sans hypothèse ». Correction 7.

**n° 21 / 22 — avertissement sur « à dégradation négligeable » (K47 ; FR 849, EN 937).** Mythos Preview à 0,1×, « degeneracy at negligible levels », contre Opus 4.8 à 0,10× où chaque direction dégrade : c'est la contradiction que la partie B range parmi les « contradictions entre papiers ». « Le dommage se mesure, il ne se suppose pas » est dans M4. Sans faute.

**n° 23 / 24 — renvoi, contrôles de K47 (FR 860, EN 948).** Sans faute.

**n° 25 / 26 — avertissement sur l'ablation de la conscience d'évaluation (C bis ; FR 887, EN 975).** K72 (« L'article compare avec et sans ablation »), fiche 1 et contre-lecture (la seule chute de la verbalisation ne montre pas le retrait) ; parade : K72, programme, partie 8. Sans faute.

**n° 27 / 28 — avertissement sur « Ton résultat, tel qu'il se dit » (FR 904, EN 992).** README : rang un sans chiffres ; accord inter-juges modéré ; aucun sous-ensemble noté par des humains. M5 ; K47 ; volet 6, §6 ; programme, partie 3 (juge scellé, audit stratifié).
- **Imprécision** : « Les échecs de rang un sont … rapportés sans chiffres » vaut pour les méthodes de rang un du README, pas pour le re-test de rang un du volet 6, §2 (27/50, p 0,81), qui a ses chiffres. Correction 8 : « des méthodes de rang un ».

**n° 29 / 30 — renvoi (FR 907, EN 995).** Sans faute.

**n° 31 / 32 — encadré du 2 octobre, le J-lens (FR 920, EN 1008).** Passation, §5.2 (« copier », « supprimer », « mentir » ; organisme à réflexe ; étiquette, trois sondes, rééchantillonnage, crosscoder) ; fiche 1 ; programme, partie 3 ; C bis (recalculer le lens). Sans faute.

**n° 33 / 34 — encadré « J-lens et espace de travail » (FR 930, EN 1018).** Vérifiés : fiche 1 (« only approximately and incompletely », présence contre cause, quatre tâches contre deux, détecteur validé contre les seules étiquettes de NLA) ; C bis (jeu de tokens, part J-space, jeux disjoints, lens qui dépend des poids) ; volet 6, §6 (trois grandeurs) et §8 (échange validé sur les pays) ; programme, parties 3 et 8 (porte, proxy) ; passation, §5.2.
- **Faute (source), limite 3** : « un rapport trouve » attribue au rapport ce qu'il relaie d'un billet de Zeisler, lu par résumé (rapport 5 ; passation, §5.5). L'encadré manque aussi la réserve de l'encadré du 2 octobre : ces échanges sont vraisemblablement ceux d'une variable intermédiaire, pas l'échange de concept qu'exige la porte, qui est la parade donnée juste en dessous. Correction 9.

**n° 35 / 36 — renvoi, contrôles de K72 (FR 967, EN 1055).** Sans faute.

**n° 37 / 38 — avertissement sur le cas connu de K72 (FR 977, EN 1065).** Programme, partie 8 (l'inhibition peut taire la verbalisation sans toucher la représentation latente ; la verbalisation n'est jamais une preuve) ; fiche 1. Exact pour le paragraphe « Le cas connu ». Le contrôle par la charge, au paragraphe précédent, ne porte que sur le cadrage réel. Sans faute.

**n° 39 / 40 — encadré « Ablation et projection » (FR 996, EN 1085).** Vérifiés : M4 ; C bis (sous-espaces aléatoires de même rang, retrait partiel ou courbe effet-dégradation) ; programme, partie 7 ; volet 6, §2 (adoucissement avec ou sans pression ; générations fraîches ; troncature ; expériences séparées ; balayage non monotone) ; volet 6, §6 (chaque direction seule ; texte complet ; monotonie vérifiée ; deux ordres de retrait) ; A7 (graines appariées) ; README (circularité).
- **Manque (doctrine)** : aucune limite sur le nul. Une ablation sans effet ne dit rien sans cas connu, et le nul peut venir d'un rang trop bas (partie C des fiches ; M5). Parade : la même ablation doit d'abord défaire le comportement en distribution (partie C ; programme, partie 3). Correction 10 : la puce est ajoutée, et la source C bis est ajoutée à la parade des deux ordres de retrait, qui y figure aussi.

**n° 41 / 42 — avertissement sur Monosemanticity (FR 1014, EN 1103).** Fiche 2 (vecteurs arbitraires), fiche 5 (explications plausibles de directions arbitraires ; valider par la prédiction mieux que des baselines), volet 4 (erreur de reconstruction), K64 (une à une, dommage apparié, tâche de comptage, graines). Il nuance volontairement « ce qui prouve qu'on a saisi une unité de calcul réelle » : c'est le rôle d'un avertissement ponctuel. Sans faute.

**n° 43 / 44 — avertissement sur Circuit Tracing (FR 1019, EN 1108).** Volet 4 (« partiels et approximatifs », « une fraction du calcul ») ; K64 (Drori : circuits lisibles infidèles) ; F·9 (une hypothèse, une contrefactuelle, « The graph is the mechanism » à ne pas dire). Sans faute.

**n° 45 / 46 et 47 / 48 — renvois (FR 1022 et 1041, EN 1111 et 1130).** Sans faute.

**n° 49 / 50 — encadré « Crosscoders et comparaison de modèles » (FR 1060, EN 1149).** K64 (features qui varient ; graines), fiche 5, volet 4, README (86,8 % au résidu ; lecture sur la reconstruction et sur le résidu), passation, §5.2, programme, partie 7.
- **Manque (doctrine)** : le nul du crosscoder sans cas connu. Le programme le donne (partie 4, l'anatomie, options) : le diff entre l'organisme de la phase de validation de l'instrument (conditionné à l'évaluation) et sa base doit faire sortir des latents « évalué ». Correction 11 : la puce est ajoutée, et la dernière limite est précisée par « pour la version suivante », comme dans la passation, §5.2.

## Les corrections (`corrections_groupe_2.json`, une entrée FR et une EN pour chacune)

| N° | Insertion | Nature | Correction |
|---|---|---|---|
| 1 | Organismes modèles, limite 1 | vrai | citation exacte de la fiche 15, « has not yet been found in any AI system » |
| 2 | Évaluations, limite 1 | vrai | la triche discrète qui monte est une triche cachée, pas une retenue ; retenue sourcée à K63 |
| 3 | Évaluations, limite 6 | vrai | le confondeur de la fiche 3 dit tel qu'il est |
| 4 | Sondes, parade 4 | vrai | les deux positions de lecture, « et », pas « ou » |
| 5 | Pilotage, limite 1 | place | dégradation attribuée à la carte d'Opus 4.8, à 0,10× (sinon contradiction avec K47) |
| 6 | Pilotage, parade 4 | source | parade sourcée au volet 5, sujet 2, et au programme, partie 3 |
| 7 | Pilotage, parade 7 | vrai | diffing par crosscoder au lieu de « aucune connue » (programme, partie 8) |
| 8 | Avertissement « Ton résultat » | précision | « des méthodes de rang un » |
| 9 | J-lens, limite 3 | source | billet de Zeisler relayé par le rapport, et sa réserve |
| 10 | Ablation et projection | doctrine | puce ajoutée : le nul et son cas connu |
| 11 | Crosscoders | doctrine | puce ajoutée : le nul et son cas connu |

## Hors de cette tranche : même constat, non corrigé ici

Pour cohérence, à voir par les groupes concernés :
- « chaque direction pilotée dégrade la sortie » dit sans l'attribuer à Opus 4.8 : FR 174, 1789 ; EN 233, 1931, 2849 ;
- « pour l'extraction supervisée, aucune parade connue », alors que le programme, partie 8, donne le diffing par crosscoder : FR 2048, 3960, 5452 ; EN 2226, 4117, 5703 ;
- « une sonde calibrée ailleurs lit autrement », à l'indicatif : FR 5727, EN 6002. Note seulement : le rapport 3 l'appuie.
