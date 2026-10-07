# Vérification du groupe 5 — tranches volet7_B_et_D et volet7_A_et_C (cours v3.6, 2 octobre 2026)

## Portée et méthode

- **Insertions vérifiées.** Volet 7, parties B et D : 34 en français, 34 en anglais. Volet 7, parties A et C : 48 en français, 48 en anglais. Total : 164 insertions, soit 82 paires FR/EN :
  - 1 encadré complet (« Détecteurs fine-tunés », à la fin de F·29) ;
  - 34 avertissements ponctuels (10 en B et D, 24 en A et C) ;
  - 47 renvois d'une ligne.
- **Ce qui a été lu.**
  - Les quatre extraits `applique_volet7_B_et_D_{FR,EN}.md` et `applique_volet7_A_et_C_{FR,EN}.md`.
  - Tout le volet 7 de la v3.6, avec ses insertions : français, lignes 2527 à 3825 ; anglais, lignes 2692 à 3963.
  - Chaque source citée, relue dans sa pièce :
    - le cours v3.5 : la note de tête ; volet M (M4, M5, M7, M8) ; volet 2 (§A et K71, §B et K63, §C et K47, C bis, §D et K64, §E et K52, §F et JB8, §G et K76, §H et G1, §I et JB10, clôture) ; volet 4 (*Auditing Hidden Objectives*) ; volet 5 (partie I, §3 ; partie II, sujets 1 et 13) ; volet 6 (§2, §3, §6, §8) ; volet 7 (F·17, F·22 à F·25, F·29, F·36, F·50 à F·57, F·62) ; volet 10 (n° 30, 37, 39, 53, 54, 64, 66) ; volet 11 (réponses 43 et A7) ;
    - les fiches : parties B (grille et pièges 1, 3, 4, 5, 6, 7) et C ; fiches 2, 3, 4, 5, 7, 8, 9, 14, 15, 16, 17, 18 ; la contre-lecture des fiches ;
    - le programme, parties 1, 3, 4, 7 et 8 ;
    - la passation, §5.2 et §5.5 ;
    - l'explication du 2 octobre, §1 à §3 ;
    - le rapport d'antériorité 3 du 2 octobre (*The Obfuscation Atlas* ; Drake et Eberstadt) ;
    - le README du dépôt.
- **Contrôle mécanique.** Le script `travail/_verif_groupe_5/construire_corrections.py` construit le JSON à partir des lignes exactes de la v3.6, puis vérifie cinq choses :
  - chaque « ancien » est une ligne entière d'insertion v3.6, présente une seule fois dans la v3.6 ;
  - aucun « ancien » ne figure dans la v3.5 ;
  - chaque « ancien » reste unique après une application simulée des corrections des groupes 1 à 4 ;
  - aucune citation des nouveaux textes n'atteint quinze mots ;
  - le JSON écrit est valide et se relit.

  Résultat : 18 corrections, toutes les vérifications passent.

## Bilan

**9 fautes**, chacune corrigée dans les deux langues, soit **18 corrections** dans `corrections_groupe_5.json` (numérotées ici dans l'ordre du fichier : les impaires en français, les paires en anglais).

| Nature | Paires | Corrections |
|---|---|---|
| Contredit le texte voisin, ou se contredit | F·13 (A et C, n° 53/54) ; F·17 (A et C, n° 61/62) | 13-14 ; 15-16 |
| Parade déclarée inconnue alors que le cours en donne une | F·7 (A et C, n° 23/24) | 11-12 |
| Doctrine : une borne sans son cas connu ; une direction témoin sans la condition « à norme égale » | F·36 (B et D, n° 51/52) ; F·31 (B et D, n° 31/32) | 7-8 ; 5-6 |
| Source qui dit autre chose que ce qu'on lui prête | F·25 (B et D, n° 9/10) | 1-2 |
| Durcissements : une affirmation plus forte que la source | F·5 (A et C, n° 17/18) ; F·54 (A et C, n° 83/84) | 9-10 ; 17-18 |
| Précision : une phrase qui se lit à contresens du texte voisin | F·31 (B et D, n° 29/30) | 3-4 |

Les 73 autres paires sont justes. Le détail est plus bas, paire par paire.

**Les places.**
- Aucune insertion ne coupe un tableau, une liste ni un paragraphe.
- Les avertissements de la partie A suivent le dernier item de la liste « À retenir », ou un paragraphe entier.
- Les renvois suivent le dernier item de « Les questions qui peuvent en sortir », ou la fin du bloc « À dire / Questions probables ».
- Dans les fiches en un seul paragraphe de la partie B (fin) et de la partie D, l'anglais tient ce paragraphe sur une ligne et le français sur plusieurs. L'insertion française suit alors la dernière ligne du même paragraphe.
- Aucune ligne « À dire » ni forme nommée n'est touchée.

**Les renvois.**
- Les 25 cibles distinctes que nomment les renvois de ces deux tranches existent à l'endroit dit dans la v3.6 : français, lignes 359 à 6215 ; anglais, lignes 426 à 6516. Chaque encadré suit bien le paragraphe annoncé (« En pratique — les coup probes », « La loi de déplacement », fin du cas G1, etc.).
- Le renvoi « détecteurs fine-tunés → volet 7, F·29 » (F·62) pointe vers l'encadré de cette tranche.
- Chaque renvoi nomme des instruments que la fiche emploie.

**Les deux langues.**
- Les 82 paires sont au même endroit, dans le même ordre (n° FR = n° EN − 1).
- Elles disent la même chose, avec les mêmes nombres et les mêmes sources.
- Une seule variante de libellé, juste dans chaque langue : « cours, note de tête » / « course, opening reserves ». La tête anglaise s'intitule « Reserves… » et dit la même correction des « 81-87% » et « 95-99% ».
- Les corrections sont faites par paires.

**La forme.**
- L'encadré et les renvois suivent les formats fixes.
- Les avertissements de B et D citent leurs sources en *(source : …)* ; ceux de A et C, entre parenthèses simples. Les deux sont permis.
- Aucun sigle inventé : seulement des numéros de la banque (K47, K63, K64, K71, K52, JB8, JB10, G1), des sections du cours (M4, M5, M7, F·n, A7), et des sigles courants (LLM, SAE, NLA, AUROC, AUC, RL, MMLU, CAA).
- Toutes les citations font moins de quinze mots. Aucune revendication « first » ou « premier » : « première porte » et « first gate » désignent la porte du programme.
- Chaque nombre ajouté est dans une pièce, avec sa source.

**La doctrine.**
- Aucune insertion ne dit qu'un contrôle aléatoire écarte le dommage. La phrase de doctrine est écrite en toutes lettres dans quatre avertissements (F·4, F·5, F·7, F·25).
- Deux écarts sont corrigés :
  - une borne de désapprentissage donnée sans son cas connu (F·36) ;
  - « comme toute direction témoin, qu'un nul de spécificité », qui efface la condition « à norme égale » (F·31).

## Insertion par insertion — volet 7, B et D

**FR n° 1 / EN n° 2 — F·22, avertissement** (FR l. 2571, EN l. 2736), après « La limite, écrite par eux ».
- **Juste.** Un « résiste au red-teaming complet » ne vaut qu'au budget et à la force de l'attaque essayée : M7, budget fixé d'avance ; F·24, « au moins celui-ci ».
- La vérité-terrain est Sonnet 4.6 (F·22). Piège 6 : oublier qui juge.
- Parades : le budget fixé d'avance (M7) ; la red team optimisée composante par composante (F·24) ; l'audit humain stratifié d'environ 200 items (programme, partie 3) ; les proxys « avec humains dans la boucle », que F·22 laisse ouverts.
- La red team a son cas connu dans le papier même : elle a trouvé la « science totalisante » contre la grille par défaut.

**FR n° 3, 5, 7 / EN n° 4, 6, 8 — renvois de F·22, F·23, F·24.** Justes. Les cibles existent : §G après les coup probes ; volet 6, §2 après la loi de déplacement ; §H après StrongREJECT. Elles sont pertinentes : le proxy est un juge LLM, et il s'agit de jeux de contrôle et de red teams.

**FR n° 9 / EN n° 10 — F·25, avertissement** (FR l. 2684, EN l. 2849). **Faute → corrections 1 et 2.**
- « Des vecteurs de contrôle au contenu arbitraire bougent le comportement dans le même sens, plus faiblement » est sourcé à la fiche 2, à la partie C **et** au volet 5, partie I, §3.
- Les deux premières disent bien « plus faiblement » (carte d'Opus 4.8).
- Mais le volet 5, §3 dit le contraire pour la reproduction externe : « des vecteurs de contrôle sans rapport avec l'alignement, aux effets aussi forts ». Le programme, partie 1, le confirme pour GLM-5 : les témoins sans rapport « font autant ».
- La phrase affaiblit donc la limite, et prête à une source ce qu'elle ne dit pas.
- Correction : « plus faiblement dans la carte système d'Opus 4.8, aussi fort dans une reproduction externe sur un modèle à poids ouverts ».
- Le reste est juste : chaque direction dégrade (fiche 2) ; la parade est celle de la fiche 2, point 4, avec la doctrine.

**FR n° 11 / EN n° 12 — F·25, renvoi.** Juste. Évaluations et pots de miel ; juges LLM, puisque le realism win rate passe par un juge apparié ; chaîne de pensée et conscience verbalisée, réponse 43 ; pilotage, §C.

**FR n° 13 / EN n° 14 — F·29, renvoi** (avant « Ce que ça change pour toi »). Juste. Sondes et pilotage : la phrase porte sur *truth probing* et *honesty steering*.

**FR n° 15 / EN n° 16 — F·29, encadré « Détecteurs fine-tunés »** (FR l. 2730, EN l. 2895), en fin de fiche. Juste.
- **L1.** 0,70-0,75 et à peine mieux qu'un prompt (fiche 7). Parade : la validation croisée par types (fiche 7), puis battre le prompt ou publier (F·29).
- **L2.** Ce ne sont pas des sondes, mais un fine-tuning LoRA à l'auto-rapport (fiche 7 ; explication, §2). Parade : le test causal de la fiche 7, point 5.
- **L3.** Environ 25 % d'étiquettes révisées, juge GPT-5 (fiche 7). Parade : le mot « révisées » (pièges de la fiche 7) et l'audit humain (programme, partie 3).
- **L4.** Des assertions seulement (F·29). « Aucune connue » : aucune pièce n'en donne.
- **L5.** « lying isn't one thing » et trois lectures rivales (fiche 7).
- **L6.** LoRA, cinq époques, Gemma et Qwen, cadres contrôlés (fiche 7). « Aucune connue ».
- Format conforme.

**FR n° 17 / EN n° 18 — F·30 (CHIVE), avertissement** (FR l. 2770, EN l. 2935). Juste.
- Le nul de trois outils en lecture seule, sur des comportements simples et les éditions testées, plafond inconnu (fiche 4, limites et réserves de la KB). Un nul d'instrument ne compte qu'avec son cas connu (M5).
- Parades :
  - la barre posée après le nul, consignée par la fiche 4 ;
  - le cas connu d'un décodeur : l'oracle d'activation marche sur des variantes fine-tunées jamais vues (fiche 18) ;
  - l'audit humain du classifieur (programme, partie 3).

**FR n° 19, 21 / EN n° 20, 22 — renvois de F·30 et F·34.** Justes. Les cinq cibles de CHIVE correspondent aux trois outils, à l'introspection et aux juges. Pour F·34, le jeu tenu à part a un encadré au volet M, M4 : le gain de MSM est hors distribution.

**FR n° 23 / EN n° 24 — F·33, avertissement** (FR l. 2839, EN l. 3004). Juste.
- « Non appris » se lit au comportement.
- Un travail externe trouve que l'inoculation peut masquer (partie C, point 2). Les parades sont les points 5 et 6 de la partie C.

**FR n° 25 / EN n° 26 — F·33, avertissement** (FR l. 2845, EN l. 3010). Juste.
- Une sonde calibrée sur un bras lit autrement dans l'autre : passation, §5.2, mot pour mot dans le sens.
- Parades : une sonde par bras et une sonde neuve, sur un jeu d'indices disjoint (explication, §2, étapes 2 et 5 ; programme, partie 3, jeu δ) ; le test causal (M4).

**FR n° 27 / EN n° 28 — F·33, renvoi.** Juste.

**FR n° 29 / EN n° 30 — F·31, avertissement** (FR l. 2872, EN l. 3037). **Précision → corrections 3 et 4.**
- La première phrase est juste : corrélationnel, trait nommé d'avance, évaluation légère (fiche 8) ; le test à dégradation appariée (M4).
- La seconde rapporte Drake et Eberstadt : piloter loin de la persona pendant l'entraînement double la diffusion. Le rapport 3 du 2 octobre le dit (« de 24 % à environ 50 % ») ; la passation, §5.5, aussi. C'est dit « rapport, non vérifié » : juste.
- Mais la phrase est posée juste après le texte de F·31 sur le *preventative steering* (« le trait ne s'installe pas »). Elle se lit comme une contradiction du papier.
- Or le pilotage préventif pousse **vers** le trait (fiche 8 : « on pousse vers le trait pendant l'entraînement »). Le rapport parle de l'inverse.
- Correction : « — l'inverse du pilotage préventif de ce papier, qui pousse vers le trait (fiche 8) — ».

**FR n° 31 / EN n° 32 — F·31, avertissement** (FR l. 2880, EN l. 3045). **Faute de doctrine → corrections 5 et 6.**
- « MMLU préservé » n'écarte le dommage que sur ce composite : juste. Le programme, parties 3 et 8, met dans D les dégâts attendus du concept.
- Mais « la direction aléatoire appariée en covariance … n'est, comme toute direction témoin, qu'un nul de spécificité » dit trop.
- Une direction témoin comparée **à dégradation appariée** est justement ce qui écarte le dommage : les K1 du programme, partie 3, « chacun à dégradation appariée » ; M4.
- La réponse A7 dit « quelle que soit la direction témoin, une comparaison à dégradation égale, puisqu'à norme égale deux directions n'abîment pas autant le modèle ».
- Correction : « comme toute direction témoin comparée à norme égale ». La parade (dégradation égale ; composite ; « dire quel aléatoire a fondé quel chiffre », volet 6, §3) est juste.

**FR n° 33, 35 / EN n° 34, 36 — renvois de F·31 et F·32.** Justes. Pour F·32, les organismes : le professeur doté d'un trait est un organisme.

**FR n° 37 / EN n° 38 — F·38, avertissement** (FR l. 2938, EN l. 3103). Juste.
- K63 : « a relevé moins de mauvaise conduite quand les modèles se disaient évalués, mais la conscience tue lui échappe ».
- « Dans une simulation, « c'est faux » est vrai » : fiche 3 et grille de la partie B, question 8.
- La parade est celle de K63 : deux versions tirées au hasard, une sonde et les mots du modèle, l'organisme dressé à se cacher comme cas connu.
- Contre le confondeur de simulation, aucune pièce ne donne de parade : « aucune connue » est juste.

**FR n° 39, 41, 43 / EN n° 40, 42, 44 — renvois de F·38, F·39, F·28.** Justes.

**FR n° 45 / EN n° 46 — F·27 (AuditBench), avertissement** (FR l. 2973, EN l. 3138). Juste.
- L'implanté est peut-être plus saillant que le naturel (passation, §5.2 ; M5).
- L'objectif était écrit en clair dans les documents (fiche 16).
- La parade partielle vient de K71 et de l'ablation d'affordance (fiche 16).
- Contre l'écart entre l'implanté et le naturel, « aucune connue » : juste. M5 et le volet 6, §8, disent qu'aucun organisme n'est le cas naturel.

**FR n° 47, 49 / EN n° 48, 50 — renvois de F·27 et F·35.** Justes. La cible de F·35, les classifieurs de sûreté, est en fin de G1.

**FR n° 51 / EN n° 52 — F·36 (SGTM), avertissement** (FR l. 2994, EN l. 3159). **Faute de doctrine → corrections 7 et 8.**
- Les limites sont justes :
  - de petits modèles (JB10) ;
  - des sondes qui échouent alors que RMU reste jailbreakable (volet 10, Deeb et Roger) ;
  - une lecture muette quand le retrait d'une direction rend 64,7 % (volet 10, Łucki).
- « Trancher par une intervention, jamais par une lecture » est soutenu par la partie C (« Seule une intervention tranche »).
- Mais la parade (« la ré-élicitation … contre une référence jamais entraînée, rapportée comme une borne ») omet le cas connu.
- Or M4 (« la référence jamais entraînée ») et JB10 disent qu'un retour au pas de la référence ne borne rien sans un modèle connu pour masquer qui, lui, revient plus vite : « sinon le budget est aveugle ».
- Correction : ajout du modèle connu pour masquer comme cas connu, et de « sans ce cas connu, le budget est aveugle » ; ajout des sources (partie C ; M4).

**FR n° 53 à 67 / EN n° 54 à 68 — renvois de F·36, F·40, F·41, F·42, F·26, F·59, F·60, F·62.** Justes, avec des cibles existantes et pertinentes. Pour F·41, le juge LLM d'un texte. Pour F·42, le jailbreak imbriqué. Pour F·62, sondes, détecteurs fine-tunés et pilotage (*honesty steering*).

## Insertion par insertion — volet 7, A et C

**FR n° 1 / EN n° 2 — F·1, avertissement** (FR l. 3097, EN l. 3231), après le dernier item de « À retenir ». Juste.
- Fiche 15 : 95,3 % pour la meilleure de 1 000 directions aléatoires ; la saillance tient peut-être à l'insertion.
- M5 : un cas connu n'est pas le cas naturel.
- K71 : plusieurs recettes, une tenue à part, l'organisme d'une autre équipe.
- Pour le cas naturel, « aucune connue » : juste.

**FR n° 3 / EN n° 4 — F·1, renvoi.** Juste.

**FR n° 5 / EN n° 6 — F·2, avertissement** (FR l. 3129, EN l. 3263). Juste.
- Le scratchpad n'est pas le raisonnement opaque, et le papier n'en fait pas la cause de la conformité (fiche 14).
- Une chaîne de pensée tait souvent ce qui a décidé (fiche 17).
- La réinclusion des transcripts fait peut-être mesurer de la mémorisation (partie C).
- Parades : l'écart de conformité comme mesure, et le HOOK « retirer l'indice lisible » (fiche 14) ; le témoin conscient mais honnête (volet 6, §8, et F·2 elle-même).
- Contre la mémorisation, aucune pièce n'offre de parade : juste.

**FR n° 7, 9 / EN n° 8, 10 — renvois de F·2 et F·3.** Justes.

**FR n° 11 / EN n° 12 — F·4, avertissement** (FR l. 3191, EN l. 3325). Juste : piège 4, M4, la courbe de K47. Doctrine écrite en toutes lettres.

**FR n° 13 / EN n° 14 — F·4, avertissement** (FR l. 3202, EN l. 3336). Juste.
- La partition est rangée par le volet 6, §2, sous « Le causal (P2), sur Llama-3.1-8B ». Le README borne ce projet à un seul modèle, à la complaisance d'opinion et à un tour.
- Le patch de l'état complet sert de plafond (programme, partie 8).
- La parade (d'autres concepts, un second modèle, un balayage de rang emboîté dans une même expérience) est celle de la pièce P4 (volet 6, §6).

**FR n° 15 / EN n° 16 — F·4, renvoi.** Juste.

**FR n° 17 / EN n° 18 — F·5, avertissement** (FR l. 3224, EN l. 3358). **Durcissement → corrections 9 et 10.**
- Les deux constats sont justes : RepE (volet 10, n° 53, sur l'utilité) ; les modèles « quirky », à transfert comparable (n° 30).
- Mais la parade dit de choisir une direction ou un site « jamais par l'exactitude de lecture ». Or :
  - le programme, partie 3, choisit les couches de la représentation « évalué » par l'AUROC d'une sonde, puis valide causalement sur l'organisme ;
  - l'encadré du 2 octobre, inséré au volet 2, dit « La couche se choisit par l'AUROC sur le jeu de validation ».
- La v3.6 se contredirait.
- Correction : « pour agir, retenir une direction, ou un site, sur son effet causal mesuré … jamais sur sa seule exactitude de lecture : celle-ci choisit la couche d'une sonde, elle ne prouve pas que la direction agit ». C'est cohérent avec la formulation du même constat au volet 5 (« passer chaque étape du pipeline, pas seulement la meilleure lectrice, au test causal »).

**FR n° 19, 21 / EN n° 20, 22 — renvois de F·5 et F·6.** Justes. Pour F·6, l'élicitation non supervisée a son encadré en fin de K52.

**FR n° 23 / EN n° 24 — F·7, avertissement** (FR l. 3282, EN l. 3416). **Faute → corrections 11 et 12.**
- Les limites sont justes :
  - le nul de rang un sans cas connu (M5 ; fiche 7, point 5) ;
  - les méthodes rapportées sans chiffres, sorties brutes non conservées, et l'artefact de polarité oui/non (README).
- La première parade est juste : le vecteur de pays de K47, et le balayage emboîté de la pièce P4.
- Mais « contre l'artefact de polarité, aucune parade connue » est faux : le volet M, M4, en donne trois.
  - Les paires contrastives qui ne diffèrent que par le trait, vérifiées par un classifieur qui ne lit que la surface.
  - La direction d'un concept rival, au même endroit, à dégradation appariée : ici, la polarité.
  - Le témoin sans pression, qui écarte un corrélat qui bouge sans pression. C'est ce témoin qui a montré que l'ablation de rang trois déplaçait la valence.
- Correction : ces trois parades, sourcées à M4.

**FR n° 25 / EN n° 26 — F·7, avertissement** (FR l. 3291, EN l. 3425), après le texte repris du volet 4. Juste.
- « De façon contrôlée » est bien dans le texte voisin.
- Les comparaisons de CAA (prompts système, fine-tuning, MMLU et TruthfulQA, GPT-4 vérifié à la main) et la sycophancie moins bien pilotée en QCM : volet 10, n° 54.
- Parade : la doctrine, et la courbe de K47.

**FR n° 27 / EN n° 28 — F·7, avertissement** (FR l. 3296, EN l. 3430). Juste.
- README : κ 0,56-0,66 sur les quatre conditions de critique ; aucun sous-ensemble humain ; le juge ne voit pas le texte évalué.
- Parades : le juge scellé et l'audit d'environ 200 items (programme, partie 3) ; le texte complet gardé (README ; volet 6, §6, pièce P4).

**FR n° 29 / EN n° 30 — F·7, renvoi.** Juste. L'ablation et la projection ont leur encadré au §D après « La méthode ».

**FR n° 31 / EN n° 32 — F·8, avertissement** (FR l. 3325, EN l. 3459). Juste.
- Piège 4 et M4.
- Fiche 5 : « des explications plausibles existent pour des directions arbitraires ».
- K64 : les features pilotées une à une contre des directions aléatoires à dommage apparié, sur la tâche de comptage, avec de nouvelles graines. C'est un témoin à dégradation appariée, conforme à la doctrine.
- Fiche 5, §2.1.4 : valider par la prédiction, mieux qu'une baseline.

**FR n° 33 / EN n° 34 — F·8, avertissement** (FR l. 3330, EN l. 3464). Juste.
- README : 86,8 % de la variance au résidu, qui porte le signal lu, et la limite mot pour mot dans le sens.
- La parade (lire sur la reconstruction et sur le résidu) est ce que fait le README.
- Pour trancher entre les deux lectures, aucune pièce ne donne de parade.

**FR n° 35 / EN n° 36 — F·8, renvoi.** Juste.

**FR n° 37 / EN n° 38 — F·9, avertissement** (FR l. 3364, EN l. 3498), après « Extension ». Juste.
- Fiche 18 : l'oracle « might confabulate plausible guesses », des suppositions souvent fausses ; le NLA confabule ; garder le décodeur à part.
- Fiche 4 : aucun gain en lecture seule.
- Piège 4 sur les vecteurs d'émotion « manipulables », un mot du texte voisin.
- La courbe de K47.

**FR n° 39 / EN n° 40 — F·9, renvoi.** Juste.

**FR n° 41 / EN n° 42 — F·10, avertissement** (FR l. 3394, EN l. 3528). Juste.
- F·24 : 0,87 → 0,41 sur cinq environnements.
- F·23 : la moitié des quarante attaques conçues à la main jamais attrapées par Opus 4.6 ; calibration à 1 % de faux positifs sur des variantes bénignes appariées.

**FR n° 43 / EN n° 44 — F·10, renvoi.** Juste.

**FR n° 45 / EN n° 46 — F·11, avertissement** (FR l. 3418, EN l. 3552). Juste.
- Volet 10, Michael et al. : avantage seulement avec débatteurs humains ; GPT-4, 78 % contre 80 % ; juges humains surconfiants.
- Parade : le banc à réponse connue (§E, « En pratique — Debate »), le juge scellé et l'audit (programme, partie 3).
- Au-delà de l'expertise humaine, il n'y a plus de référence : §E (tâches surhumaines) et clôture du volet 2. « Aucune connue » : juste, comme l'a jugé le groupe 3 pour l'encadré du débat.
- Voir l'observation 2.

**FR n° 47 / EN n° 48 — F·11, renvoi.** Juste.

**FR n° 49 / EN n° 50 — F·12, avertissement** (FR l. 3448, EN l. 3582). Juste. JB8 : les idées qui exploitaient la structure du jeu de données ; « contredire partout passerait pour une récupération » ; la parade entière, avec la copie sur étiquettes vraies comme cas connu.

**FR n° 51 / EN n° 52 — F·12, renvoi.** Juste.

**FR n° 53 / EN n° 54 — F·13, avertissement** (FR l. 3478, EN l. 3612). **Faute → corrections 13 et 14.**
- Les limites sont justes (fiche 16) :
  - quatre équipes ;
  - l'équipe 3 a réussi avec les données et sans SAE ;
  - l'équipe sans données a échoué ;
  - l'objectif était écrit en clair ;
  - « artificially easy to discover ».
- Mais « contre un organisme trop facile, aucune parade connue » contredit le texte du volet 4 repris quelques lignes plus bas dans la même fiche : « Extension : durcir l'organisme (objectif plus profondément caché) et mesurer quelles méthodes tiennent encore ».
- Correction : cette parade, sourcée au volet 4 (*Auditing Hidden Objectives*). « Aucune connue » reste pour l'écart entre l'implanté et le naturel, que le texte voisin pose aussi (M5).

**FR n° 55, 57, 59 / EN n° 56, 58, 60 — renvois de F·13, F·15, F·16.** Justes.

**FR n° 61 / EN n° 62 — F·17, avertissement** (FR l. 3586, EN l. 3720). **Faute → corrections 15 et 16.**
- Les limites sont justes :
  - le « 7× » compare des méthodes, sur de petits modèles (F·36 ; JB10) ;
  - le test sur faits indépendants ne vaut que pour des faits à faible fuite, pas pour des capacités (volet 10, Deeb et Roger).
- La parade de JB10 est juste.
- Mais « pour l'échelle et pour les capacités, aucune parade connue » contredit cette parade même. JB10 (« How would you verify that a **capability** has been unlearned… ») est construit pour des capacités. La référence jamais entraînée y écarte précisément « que le fine-tuning enseigne la capacité au lieu de la réveiller » (JB10 ; M4).
- Correction : la référence jamais entraînée étend le test aux capacités ; « aucune connue » reste pour l'échelle.

**FR n° 63 / EN n° 64 — F·17, avertissement** (FR l. 3597, EN l. 3731), entre la clôture du volet 4 reprise et « Fin du Volet 4 ». Juste.
- Fiche 2 : vecteurs arbitraires ; dégradation de chaque direction ; « comparable or smaller » à 0,01×.
- La parade est le point 4 de la fiche 2. La place est entre deux paragraphes.

**FR n° 65 / EN n° 66 — F·17, renvoi.** Juste.

**FR n° 67 / EN n° 68 — F·50, avertissement** (FR l. 3627, EN l. 3759). Juste.
- Le volet 6, §6, attribue 0,867 à la reproduction de Casademunt, et « catches 95-99 % » aux auteurs, à 1 % de faux positifs.
- La note de tête dit fausses les rétractations « 0,867 vs 95-99 % » (anglais : « they are true »).
- F·62 : des sondes de vérité moins bonnes qu'un prompt.
- Volet 5, sujet 1 : battre une baseline boîte noire à coût égal. F·29 : publier si la sonde ne bat pas le prompt.

**FR n° 69 / EN n° 70 — F·50, renvoi.** Juste.

**FR n° 71 / EN n° 72 — F·51, avertissement** (FR l. 3651, EN l. 3783). Juste.
- F·51 : 43 % contre 55 % à 1 % de faux positifs.
- F·50 : le rappel à 1 % de faux positifs est la vraie mesure.
- Volet 5, sujet 1 : baseline boîte noire à coût égal.
- Programme, partie 3 : les trois distances.

**FR n° 73 / EN n° 74 — F·51, renvoi.** Juste.

**FR n° 75 / EN n° 76 — F·52, avertissement** (FR l. 3675, EN l. 3807). Juste.
- Piège 1 ; fiche 7 (l'écart hors distribution est la mesure) ; 0,73 à 0,93 (F·52).
- Parade : l'explication, §3 (des familles, jamais des paraphrases ; des formats tenus à part) et le programme, partie 3.

**FR n° 77 / EN n° 78 — F·52, renvoi.** Juste.

**FR n° 79 / EN n° 80 — F·53, avertissement** (FR l. 3698, EN l. 3830). Juste.
- La conscience est induite au niveau du prompt (F·53). Un nul ne compte qu'avec son cas connu (M5).
- *The Obfuscation Atlas* est cité « rapport », conforme au rapport 3 : après RL, des sondes neuves hors domaine se dégradent.
- Parades : l'organisme dressé à se cacher (K63), qui garantit que la pression mord ; la sonde neuve sur un jeu d'indices disjoint (explication, §2 et §3 ; passation, §5.2).

**FR n° 81 / EN n° 82 — F·53, renvoi.** Juste.

**FR n° 83 / EN n° 84 — F·54, avertissement** (FR l. 3722, EN l. 3854). **Durcissement → corrections 17 et 18.**
- « Un rappel de 0,844 ne se lit qu'avec son taux de faux positifs » : juste, et la fiche ne donne pas ce taux.
- Mais la suite fait de ce 0,844 un rappel de campagne qui dépendrait du ratio de trafic bénin. Ce n'est vrai que du rappel de campagne de Brown, que le volet 6, §6, montre tomber de 81-87 % à 65,8 % quand ce ratio passe de dix à cent. F·54 ne dit pas que le rappel de TRACE en soit un.
- Correction : la dépendance au ratio est dite pour un rappel de campagne, avec l'exemple de Brown.
- La parade est juste : 1 % pour la porte G1 du programme (volet 6, §6) ; calibration sur variantes bénignes appariées (F·23).

**FR n° 85, 87 / EN n° 86, 88 — renvois de F·54 et F·55.** Justes.

**FR n° 89 / EN n° 90 — F·56, avertissement** (FR l. 3767, EN l. 3899). Juste.
- La red team (F·24).
- Le volet 6, §6, corrigé sur les textes intégraux (note de tête) : le « 81-87 % » de Brown est un rappel de campagne à 2,35-3,09 % de faux positifs, à dix fois plus de trafic bénin ; il tombe à 65,8 % à cent fois ; figure 5, absente du résumé.

**FR n° 91 / EN n° 92 — F·56, renvoi.** Juste.

**FR n° 93 / EN n° 94 — F·57, avertissement** (FR l. 3790, EN l. 3922). Juste. F·24 (0,87 → 0,41, « le score de sûreté ») ; F·50 (l'AUC ne dit pas le rappel au seuil) ; F·23 (calibration). Voir l'observation 4.

**FR n° 95 / EN n° 96 — F·57, renvoi.** Juste.

## Observations, sans correction (à trancher par la suite)

1. **Deux fiches sans renvoi.**
   - F·14 (ELK) nomme les sondes de vérité et CCS (« des tentatives partielles »).
   - F·58 (la page des directions) cite « activation monitors are not robust to distributional shifts ».
   - Ni l'une ni l'autre ne porte de renvoi. Un renvoi d'une ligne y serait utile : vers les sondes d'activation et l'élicitation non supervisée pour la première, vers les sondes d'activation pour la seconde.
   - Une correction ne peut pas l'ajouter : il n'y a aucune insertion v3.6 dans ces deux fiches. Cela demande une insertion.
2. **F·11, FR n° 45 / EN n° 46.** « Quand le juge est un modèle, les limites des juges LLM s'appliquent (piège 6) » est exact, mais vague.
   - Le groupe 3 a remplacé une formule voisine par les erreurs constatées chez Kenton et al. (volet 10) : le juge faible suit le consultant ouvert, qu'il ait raison ou tort, et son biais de position est plus fort en débat.
   - On pourrait faire de même ici, par souci d'homogénéité. Ce n'est pas une faute : la phrase est conditionnelle et sourcée.
3. **Encadré de F·29, parade 2.** Elle reprend le test causal de la fiche 7, point 5, sans son cas positif : un pilotage qui, à cette dose, sait faire basculer l'honnêteté. La parade ne lit aucun nul, donc la doctrine n'est pas violée ; l'ajout la rendrait complète.
4. **F·57, FR n° 93.** Le 0,87 du score de sûreté de F·24 côtoie l'« AUC of 0.87 » du moniteur Gemini, citée à la ligne d'ancrage.
   - L'insertion dit bien « le score de sûreté ».
   - Les pièces ne disent pas si les deux nombres sont liés : aucune précision n'a été ajoutée.
   - À l'oral, garder en tête le piège 7 : deux chiffres voisins qui ne mesurent pas la même chose.
5. **Les « aucune parade connue » jugés justes.** Aucune pièce n'en donne pour :
   - le cas naturel (F·1) ;
   - la mémorisation du scénario (F·2) ;
   - « features absentes » contre « dictionnaire qui perd trop » (F·8) ;
   - le débat au-delà de l'expertise humaine (F·11) ;
   - les assertions seules, et la tromperie en déploiement (encadré de F·29) ;
   - le confondeur de simulation (F·38) ;
   - l'écart entre l'implanté et le naturel (F·27, et F·13 après correction) ;
   - la taille des modèles (F·36) et l'échelle (F·17).
6. **Les lignes « À ne pas dire » de F·50 et F·56.** Elles portent encore les deux rétractations que la note de tête dit fausses : « c'est 0,867 », et « Le « 81-87 % » n'y est pas ».
   - La règle interdit de les toucher.
   - Les avertissements FR n° 67 et n° 89 renvoient au volet 6, §6, et à la note de tête, ce qui suffit à l'étude.
