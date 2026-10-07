# Insertions appliquées — volet11_53_et_fin — FR

### Insertion n°1, après la ligne 4774 de la v3.5

> Ancre : explicitement à feindre l'obéissance pour préserver ses préférences, et que la feinte persistait sous entraînement (Alignment Faking, 2024).

> ⚠ *(v3.6)* Ce résultat lit le motif dans un scratchpad caché, donné avec la consigne de raisonner sur sa situation, sur un indice construit (gratuit contre payant) : on ne sait pas y trancher entre jeu de rôle et vraie préservation de buts, et le RL qui fait monter ce raisonnement fait aussi monter la conformité hors surveillance, sans que le papier fasse de ce raisonnement la cause de la conformité (fiche 14 ; fiches, partie C ; fiches, partie B, piège 2). Parade : s'appuyer sur la mesure, l'écart de conformité entre le cas « entraîné » et le cas « non entraîné », et retirer l'indice lisible pour chercher quand même la préservation de buts (fiche 14) ; qu'une réplication sur un modèle récent ne mesure que la mémorisation du scénario, ses transcripts ayant été réinclus dans l'entraînement, aucune parade connue ne l'écarte ; on le dit (fiches, partie C).

### Insertion n°3, après la ligne 4774 de la v3.5

> Ancre : explicitement à feindre l'obéissance pour préserver ses préférences, et que la feinte persistait sous entraînement (Alignment Faking, 2024).

> ⚠ **Limites et parades** : évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; chaîne de pensée comme moniteur → volet 11, réponse 43 ; organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») *(v3.6)*

### Insertion n°5, après la ligne 4789 de la v3.5

> Ancre : concept n'est pas une sonde qui le contrôle ; chez moi, la direction lue fait moins d'un pour cent du travail causal.

> ⚠ *(v3.6)* Des vecteurs aléatoires en contrôle n'écartent que « n'importe quelle poussée de cette taille fait autant » — le nul de spécificité ; le dommage ne s'écarte qu'à dégradation appariée (cours, volet M, M4) ; et dans la lignée des cartes système, l'effet est modeste et dépend du jeu de données, des vecteurs de contrôle arbitraires bougent le comportement dans le même sens, chaque direction dégrade les sorties, et Opus 4.6 ne trouvait pas de différence notable avec des contrôles aléatoires sur la tromperie et la complaisance (fiche 2 ; contre-lecture des fiches). Parade : un sous-espace contre des sous-espaces aléatoires de même rang, à dégradation appariée, plus une baseline de prompt et une courbe dose-réponse contre plusieurs témoins (fiche 2 ; cours, volet 2, §C, K47 ; programme, partie 3).

### Insertion n°7, après la ligne 4789 de la v3.5

> Ancre : concept n'est pas une sonde qui le contrôle ; chez moi, la direction lue fait moins d'un pour cent du travail causal.

> ⚠ *(v3.6)* Ces détecteurs de mensonge ne sont pas des sondes : ce sont des modèles fine-tunés par LoRA pour répondre à une question d'auto-rapport sur un transcript ; et 0,95 est une progression en distribution pendant l'entraînement, le plateau d'une catégorie à l'autre étant de 0,70 à 0,75, à peine mieux qu'un simple prompt (fiche 7 ; explication du 2 octobre, partie 2). Parade : ne pas transférer leurs chiffres aux sondes ; pour une sonde, mesurer l'écart entre l'AUROC en distribution et celle de familles entières tenues à part, puis faire le test causal à dégradation appariée, avec un cas connu au même réglage (fiche 7 ; explication du 2 octobre, partie 3).

### Insertion n°9, après la ligne 4789 de la v3.5

> Ancre : concept n'est pas une sonde qui le contrôle ; chez moi, la direction lue fait moins d'un pour cent du travail causal.

> ⚠ *(v3.6)* Ce chiffre de partition n'a pas été mesuré à dégradation égale — « un chiffre à refaire à dégradation égale » (cours, volet 11, réponse A4) —, un aléatoire apparié en covariance y fait davantage que la direction de la sonde (cours, volet 6, §2 et §3), et la seule lecture mesurée sur Llama est une corrélation peut-être d'ajustement (README du dépôt). Parade : le protocole de la réponse A4 — une intervention sur la direction lue, une sur l'état complet aux mêmes endroits, des directions témoins comparées à dégradation égale —, le patch de l'état complet servant de plafond, et la lecture scorée sur des items exclus de l'entraînement de la sonde (cours, volet 11, réponse A4 ; programme, partie 8 ; README du dépôt).

### Insertion n°11, après la ligne 4789 de la v3.5

> Ancre : concept n'est pas une sonde qui le contrôle ; chez moi, la direction lue fait moins d'un pour cent du travail causal.

> ⚠ **Limites et parades** : organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; détecteurs fine-tunés → volet 7, F·29 ; patching → volet 10, fiche Patchscopes ; cas connu → volet M, M5 (fin de section) ; sondes de désalignement, J-lens compris (encadré du 2 octobre) → volet 2, §A (avant le cas d'application K71), §C (avant le cas d'application K47) et C bis (avant le cas d'application K72) *(v3.6)*

### Insertion n°13, après la ligne 4807 de la v3.5

> Ancre : de la même façon.

> ⚠ **Limites et parades** : juges LLM → volet 6, §2 (après « La loi de déplacement ») ; évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; débat et supervision évolutive → volet 2, §E (après « En pratique — Debate ») *(v3.6)*

### Insertion n°15, après la ligne 4834 de la v3.5

> Ancre : d'échec, le décalage de distribution d'abord ; une défense en profondeur veut des échecs indépendants, pas des couches qui se ressemblent.

> ⚠ *(v3.6)* Le gain hors distribution du midtraining de spécification est lu sur des modèles ouverts, sur un banc agentique dont le modèle peut reconnaître les scènes comme des tests — la limite que sa fiche pose elle-même (cours, volet 7, F·34). Parade : deux versions de l'environnement, tirées au hasard, qui ne diffèrent que par des indices de réalisme notés par un discriminateur, avec un organisme dressé à se cacher comme cas connu (cours, volet 2, §B, K63) ; qu'un banc tenu à part représente le réel, aucune parade connue ne le garantit ; on le dit (fiche 12).

### Insertion n°17, après la ligne 4834 de la v3.5

> Ancre : d'échec, le décalage de distribution d'abord ; une défense en profondeur veut des échecs indépendants, pas des couches qui se ressemblent.

> ⚠ *(v3.6)* Le résultat d'inhibition cité a la même limite qu'à la réponse 56 — des vecteurs de contrôle arbitraires font aussi monter le désalignement, plus faiblement, et un contrôle de même norme n'est que le nul de spécificité (fiche 2 ; cours, volet M, M4) — ; et la couche interne n'est pas indépendante de la façade par construction : une sonde peut lire « je suis surveillé » et le contexte de test au lieu de l'intention, et tomber alors au même endroit que l'évaluation (cours, volet 6, §8 ; cours, volet 3, §4, K67). Parade : des sous-espaces aléatoires de même rang à dégradation appariée pour l'inhibition, et, pour la sonde, des transcripts honnêtes rédigés comme des tests et un organisme conscient mais honnête, sur lesquels elle doit rester à sa ligne de base (cours, volet M, M4 ; cours, volet 3, §4, K67 ; cours, volet 6, §8).

### Insertion n°19, après la ligne 4834 de la v3.5

> Ancre : d'échec, le décalage de distribution d'abord ; une défense en profondeur veut des échecs indépendants, pas des couches qui se ressemblent.

> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; jeu tenu à part → volet M, M4 (après « Le jeu tenu à part ») *(v3.6)*

### Insertion n°21, après la ligne 4848 de la v3.5

> Ancre : red team de mon propre banc est la première chose que je publierais, avant tout chiffre de rappel.

> ⚠ *(v3.6)* Les quarante attaques du banc des angles morts sont conçues à la main, en transcriptions synthétiques dont le réalisme reste ouvert : le banc dit si le moniteur voit une attaque écrite par des humains, pas si un modèle la produirait (cours, volet 7, F·23 ; cours, volet 11, réponse B14) ; et le réalisme par paires se mesure par un juge LLM, alors que la conscience d'évaluation liée à la tâche persiste (cours, volet 7, F·25). Parade : rejouer les attaques comme des tâches que le modèle doit faire dans un vrai harnais, au seuil calibré sur des variantes bénignes appariées (cours, volet 11, réponse B14 ; cours, volet 7, F·23) ; pour le réalisme des transcriptions synthétiques, aucune parade connue ; on le dit (cours, volet 7, F·23).

### Insertion n°23, après la ligne 4848 de la v3.5

> Ancre : red team de mon propre banc est la première chose que je publierais, avant tout chiffre de rappel.

> ⚠ **Limites et parades** : red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») ; moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; classifieurs de sûreté → volet 2, §H (fin du cas d'application G1) ; évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; juges LLM → volet 6, §2 (après « La loi de déplacement ») *(v3.6)*

### Insertion n°25, après la ligne 4860 de la v3.5

> Ancre : je commencerais.

> ⚠ *(v3.6)* « Ne généraliseraient jamais » serait un nul d'instrument : il ne compte qu'avec un cas connu où la même sonde, au même réglage, attrape hors distribution une intention qu'on a installée — sinon l'échec dit peut-être seulement que la sonde est aveugle (cours, volet M, M5 ; passation, §5.2). Parade : juger la sonde sur des familles entières tenues à part, jusqu'à l'agentique à plusieurs tours, avec un organisme où l'on a installé l'intention, et dire le résultat comme une borne, jamais comme une absence (explication du 2 octobre, parties 1 et 3 ; programme, partie 3 ; cours, volet M, M5).

### Insertion n°27, après la ligne 4860 de la v3.5

> Ancre : je commencerais.

> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; cas connu → volet M, M5 (fin de section) ; jeu tenu à part → volet M, M4 (après « Le jeu tenu à part ») ; sondes de désalignement, J-lens compris (encadré du 2 octobre) → volet 2, §A (avant le cas d'application K71), §C (avant le cas d'application K47) et C bis (avant le cas d'application K72) *(v3.6)*

### Insertion n°29, après la ligne 4877 de la v3.5

> Ancre : right need not be the lever: in my setting the probe's direction did under one percent of the causal work.

> ⚠ *(v3.6)* Note d'étude, sans rien changer à la position : ce « moins d'un pour cent » n'a pas encore été mesuré à dégradation égale, et un aléatoire apparié en covariance y fait davantage que la direction de la sonde (cours, volet 11, réponse A4 ; cours, volet 6, §2 et §3). Parade : le refaire par le protocole de la réponse A4, avec des directions témoins comparées à dégradation égale et le patch de l'état complet comme plafond (cours, volet 11, réponse A4 ; programme, partie 8).

### Insertion n°31, après la ligne 4885 de la v3.5

> Ancre : random directions with the same covariance, compared at equal degradation — to say a direction acts; without it, you have a correlation.

> ⚠ *(v3.6)* Deux réserves à garder sous la position : la lisibilité elle-même ne se prouve pas en distribution — une AUROC en distribution ne prouve rien, c'est l'écart avec des familles tenues à part qui se mesure (fiches, partie B, piège 1 ; fiche 7) — ; et une intervention qui échoue ne réfute la causalité qu'avec un cas connu au même réglage, sinon le nul peut venir d'un rang trop bas (fiche 7 ; cours, volet M, M5). Parade : des familles entières tenues à part, jamais des paraphrases, et un cas connu au même rang, à la même dose et au même seuil que la mesure (explication du 2 octobre, partie 3 ; cours, volet M, M5 ; fiche 7).

### Insertion n°33, après la ligne 4898 de la v3.5

> Ancre : the mechanism.

> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme ») ; dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») ; cas connu → volet M, M5 (fin de section) ; patching → volet 10, fiche Patchscopes ; évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») *(v3.6)*

### Insertion n°35, après la ligne 4921 de la v3.5

> Ancre : proposé depuis 2024 et presque pas mesuré.

> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; patching → volet 10, fiche Patchscopes ; ablation et projection → volet 2, §D (après « La méthode ») ; dictionnaires et SAE → volet 4, Towards puis Scaling Monosemanticity *(v3.6)*

### Insertion n°37, après la ligne 4936 de la v3.5

> Ancre : blanc contre le noir, avec son intervalle.

> ⚠ *(v3.6)* Des sondes entraînées hors politique sur des exemples écrits peuvent n'apprendre qu'un indice de surface, ou lire le texte plutôt qu'une représentation (cours, volet 2, §C ; programme, partie 8) ; et réussir le test à deux familles ferme l'écart entre deux façons d'implanter, pas celui entre l'implanté et le naturel : une intention implantée est peut-être plus saillante (cours, volet 6, §8 ; passation, §5.2 ; fiche 15). Parade : tirer les négatifs des générations réelles du modèle, lire au premier jeton avant toute raison écrite ou au jeton d'action avec des raisons neutres préremplies, et ajouter l'organisme d'une autre équipe (cours, volet 2, §C ; programme, parties 3 et 8 ; cours, volet 2, §A, K71) ; contre l'écart entre l'implanté et le naturel lui-même, aucune parade connue ; on le dit (explication du 2 octobre, partie 1 ; cours, volet M, M5).

### Insertion n°39, après la ligne 4936 de la v3.5

> Ancre : blanc contre le noir, avec son intervalle.

> ⚠ **Limites et parades** : organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») ; cas connu → volet M, M5 (fin de section) ; sondes de désalignement, J-lens compris (encadré du 2 octobre) → volet 2, §A (avant le cas d'application K71), §C (avant le cas d'application K47) et C bis (avant le cas d'application K72) *(v3.6)*

### Insertion n°41, après la ligne 4948 de la v3.5

> Ancre : sommer un biais ne fait qu'un plus grand biais.

> ⚠ *(v3.6)* L'échec sur la famille « adaptateur léger » ne se lit « une sonde lit le mécanisme d'induction » qu'avec deux cas connus : l'implant de cette famille a pris, vérifié copie par copie par son comportement, et la sonde, au même seuil, attrape des cas tenus à part de la famille qu'elle réussit ; sinon le nul dit peut-être un implant raté ou un seuil trop strict (cours, volet 2, §A, K71 ; cours, volet 2, §E, K52 ; cours, volet M, M5). Parade : ces deux vérifications avant de conclure, et un comportement inoffensif planté par les deux mêmes recettes, qui écarte une sonde lisant la recette (cours, volet 2, §A, K71).

### Insertion n°43, après la ligne 4948 de la v3.5

> Ancre : sommer un biais ne fait qu'un plus grand biais.

> ⚠ *(v3.6)* Les détecteurs de mensonge cités ne sont pas des sondes — des modèles fine-tunés par LoRA pour répondre à une question d'auto-rapport sur un transcript —, et 0,95 est une progression en distribution pendant l'entraînement (fiche 7 ; explication du 2 octobre, partie 2) : leur destin ne se transfère pas tel quel aux sondes. Parade : pour une sonde, l'écart entre l'AUROC en distribution et celle de familles entières tenues à part, puis le test causal à dégradation appariée (fiche 7 ; explication du 2 octobre, partie 3).

### Insertion n°45, après la ligne 4948 de la v3.5

> Ancre : sommer un biais ne fait qu'un plus grand biais.

> ⚠ **Limites et parades** : cas connu → volet M, M5 (fin de section) ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; détecteurs fine-tunés → volet 7, F·29 ; patching → volet 10, fiche Patchscopes ; sondes de désalignement, J-lens compris (encadré du 2 octobre) → volet 2, §A (avant le cas d'application K71), §C (avant le cas d'application K47) et C bis (avant le cas d'application K72) *(v3.6)*

### Insertion n°47, après la ligne 4962 de la v3.5

> Ancre : ordre des concepts que la charge ne prédit pas — alors ma prédiction tomberait, et je le dirais.

> ⚠ *(v3.6)* La charge se lit au J-lens, qui n'a été montré que sur Claude et ne lit que des concepts d'un seul token, et « charge » désigne trois grandeurs selon les textes (fiche 1 ; cours, volet 2, C bis ; cours, volet 6, §6). Parade : sur chaque modèle ouvert, une porte — reproduire d'abord l'échange d'un concept d'un seul token, sinon un tuned lens déclaré comme approximation, la thèse n'étant alors pas testée au sens de l'article —, la charge d'un concept de plusieurs tokens lue sur un jeu de tokens, et le prédicteur principal gelé d'abord, en disant lequel (programme, parties 3 et 8 ; cours, volet 6, §6).

### Insertion n°49, après la ligne 4962 de la v3.5

> Ancre : ordre des concepts que la charge ne prédit pas — alors ma prédiction tomberait, et je le dirais.

> ⚠ **Limites et parades** : ablation et projection → volet 2, §D (après « La méthode ») ; J-lens et espace de travail → volet 2, C bis (après « Le test, tel qu'il se dit ») ; dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») ; patching → volet 10, fiche Patchscopes *(v3.6)*

### Insertion n°51, après la ligne 4975 de la v3.5

> Ancre : et ce chiffre, je ne l'ai pas vu mesuré.

> ⚠ *(v3.6)* « Indiscernable de zéro » est un nul : il ne compte que si le même dispositif — mêmes cadrages, même régression — voit le déplacement là où il existe, chez le juge que tu as mesuré, et il se dit comme une borne, avec son budget et sa puissance, jamais comme une absence (cours, volet M, M5) ; et l'écart entre modèles et chercheurs sur les propositions de recherche repose sur dix chercheurs et 92 paires (cours, volet 7, F·41). Parade : ce cas connu dans le même protocole avant de déclarer un juge « résolu », et l'écart sur les propositions dit avec la taille de son échantillon (cours, volet M, M5 ; cours, volet 7, F·41).

### Insertion n°53, après la ligne 4975 de la v3.5

> Ancre : et ce chiffre, je ne l'ai pas vu mesuré.

> ⚠ **Limites et parades** : juges LLM → volet 6, §2 (après « La loi de déplacement ») ; cas connu → volet M, M5 (fin de section) ; évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») *(v3.6)*

### Insertion n°55, après la ligne 4989 de la v3.5

> Ancre : détection et incrimination que Redwood pose pour les menaces diffuses, et je la garde.

> ⚠ *(v3.6)* La garantie borne les fausses alarmes, pas les ratés : une sonde en production peut échouer en silence, et son silence n'est pas celui du modèle (cours, volet 3, §3, K70) ; et le test séquentiel toujours valide existe déjà sur des scores de vérificateur boîte noire, ce qui reste étant le même test sur des scores internes (cours, volet 7, F·55). Parade : des canaris — des positifs connus glissés dans le trafic —, un score de dérive et un échantillon frais jugé chaque mois (cours, volet 3, §3, K70) ; et, pour cette combinaison, dire « I haven't seen that combination measured », jamais « first » ni « mine » (cours, volet 7, F·52 et F·55).

### Insertion n°57, après la ligne 4989 de la v3.5

> Ancre : détection et incrimination que Redwood pose pour les menaces diffuses, et je la garde.

> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») *(v3.6)*

### Insertion n°59, après la ligne 5001 de la v3.5

> Ancre : combien de directions l'effet demande, par un balayage de rang fait dans une même expérience.

> ⚠ *(v3.6)* Les trois questions s'appliquent d'abord à ton propre chiffre : ce « moins d'un pour cent contre soixante-huit » n'a pas encore été mesuré à dégradation égale, et un aléatoire apparié en covariance y fait davantage que la direction de la sonde (cours, volet 11, réponse A4 ; cours, volet 6, §2 et §3). Parade : le protocole de la réponse A4, avec des directions témoins comparées à dégradation égale et le patch de l'état complet comme plafond (cours, volet 11, réponse A4 ; programme, partie 8).

### Insertion n°61, après la ligne 5001 de la v3.5

> Ancre : combien de directions l'effet demande, par un balayage de rang fait dans une même expérience.

> ⚠ **Limites et parades** : contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme ») ; dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») ; patching → volet 10, fiche Patchscopes ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; ablation et projection → volet 2, §D (après « La méthode ») *(v3.6)*

### Insertion n°63, après la ligne 5014 de la v3.5

> Ancre : pire qu'une défense dont on connaît les limites.

> ⚠ *(v3.6)* « Pas contournable » ne dit rien de ce que fait un entraînement : selon un rapport, après un RL, des sondes neuves hors domaine se dégradent alors qu'une sonde neuve dans le domaine reste quasi parfaite (rapport d'antériorité 3 du 2 octobre, *The Obfuscation Atlas* — rapport, lu de façon ciblée), et itérer contre ses détecteurs sélectionne l'évasion (fiche 19). Parade : une sonde neuve après tout entraînement, sur un jeu d'indices disjoint, et des détecteurs scellés hors de la boucle — s'ils se déclenchent encore quand ceux de la boucle se taisent, l'évasion a été sélectionnée (passation, §5.2 ; programme, partie 3 ; fiche 19).

### Insertion n°65, après la ligne 5014 de la v3.5

> Ancre : pire qu'une défense dont on connaît les limites.

> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; sondes de désalignement, J-lens compris (encadré du 2 octobre) → volet 2, §A (avant le cas d'application K71), §C (avant le cas d'application K47) et C bis (avant le cas d'application K72) *(v3.6)*

### Insertion n°67, après la ligne 5030 de la v3.5

> Ancre : explanations.

> ⚠ *(v3.6)* Deux limites pour A10 : le sous-espace de rang trois déplaçait la valence, pas le concept, et son effet n'est pas revenu sur des générations fraîches — ce n'est pas une prise causale sur la complaisance, et le décomposer en features ne dirait pas ce qui la porte (cours, volet 6, §2 ; README du dépôt) ; et le dictionnaire épars ouvert pour ce modèle laisse la plus grande part de la variance dans son résidu, qui porte le signal lu (README du dépôt). Parade : le témoin sans pression et la direction d'un concept rival, à dégradation appariée, avant de décomposer, et le signal lu sur la reconstruction et sur le résidu ; pour trancher entre « features absentes du dictionnaire » et « dictionnaire qui perd trop », aucune parade connue ; on le dit (cours, volet M, M4 ; README du dépôt).

### Insertion n°69, après la ligne 5060 de la v3.5

> Ancre : sabotage — realism, which Kissane measures at 32.8 percent for audits; I'd publish mine before any number.

> ⚠ *(v3.6)* Le réalisme par paires de Kissane mesure si un juge prend une transcription d'audit pour une transcription réelle ; il ne dit pas si une intention implantée ressemble à une intention naturelle — une intention implantée est peut-être plus saillante (cours, volet 7, F·25 ; passation, §5.2 ; fiche 15). Parade partielle : planter le même sabotage par plusieurs recettes, en tenir une à part, et ajouter l'organisme d'une autre équipe (cours, volet 2, §A, K71) ; contre l'écart entre l'implanté et le naturel lui-même, aucune parade connue ; on le dit (explication du 2 octobre, partie 1 ; cours, volet M, M5).

### Insertion n°71, après la ligne 5064 de la v3.5

> Ancre : compute and without the environments — and I'd first try to reproduce Diffuse Control in the open, because the first gate only needs that.

> ⚠ **Limites et parades** : juges LLM → volet 6, §2 (après « La loi de déplacement ») ; dictionnaires et SAE → volet 4, Towards puis Scaling Monosemanticity ; graphes d'attribution → volet 4, Circuit Tracing ; ablation et projection → volet 2, §D (après « La méthode ») ; organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») *(v3.6)*

### Insertion n°73, après la ligne 5094 de la v3.5

> Ancre : link between sessions isn't visible in the artefacts, and one must look elsewhere.

> ⚠ *(v3.6)* Les transcriptions du banc sont conçues à la main : une sonde lue sur elles lit un modèle qui traite le texte d'un autre, pas l'intention d'un agent qui écrit sa propre procédure, et elle peut lire le texte plutôt qu'une représentation (cours, volet 7, F·23 ; cours, volet 11, réponse B14 ; programme, partie 8). Parade : faire produire les trajectoires par le modèle lui-même, avec un organisme à qui l'on a installé la procédure nuisible comme cas connu, lire au jeton d'action avec des raisons neutres préremplies, et garder le seuil calibré sur les variantes bénignes appariées (cours, volet 6, §8 ; passation, §5.2 ; programme, parties 3 et 8 ; cours, volet 7, F·23).

### Insertion n°75, après la ligne 5094 de la v3.5

> Ancre : link between sessions isn't visible in the artefacts, and one must look elsewhere.

> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») *(v3.6)*

### Insertion n°77, après la ligne 5115 de la v3.5

> Ancre : inhibit — then you can only make the environment realistic, without knowing whether you succeeded.

> ⚠ *(v3.6)* Un contrôle aléatoire de l'inhibition n'est que le nul de spécificité ; le dommage ne s'écarte qu'à dégradation appariée (cours, volet M, M4) ; et la conscience verbalisée ne mesure pas l'inhibition : des directions aléatoires la font baisser aussi, et les mesures de la conscience d'évaluation — sonde, NLA, question de suivi — ne sont que faiblement corrélées (programme, partie 8 ; fiche 2). Parade : des sous-espaces aléatoires de même rang à dégradation appariée, un critère principal comportemental avec une sonde latente comme contrôle, et dire laquelle des mesures a fondé quel chiffre (programme, parties 3 et 8 ; cours, volet 5, sujet 4 ; cours, volet M, M4).

### Insertion n°79, après la ligne 5115 de la v3.5

> Ancre : inhibit — then you can only make the environment realistic, without knowing whether you succeeded.

> ⚠ **Limites et parades** : évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme ») ; dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; chaîne de pensée comme moniteur, et conscience verbalisée → volet 11, réponse 43 ; juges LLM → volet 6, §2 (après « La loi de déplacement ») *(v3.6)*

### Insertion n°81, après la ligne 5139 de la v3.5

> Ancre : signal, delegation gains ground. What would kill it: an unchanged frontier — then the internal signal says nothing beyond the scorer.

> ⚠ *(v3.6)* La récupération de l'écart par les agents automatisés s'est faite avec des idées qui exploitaient la structure propre au jeu de données, et sur une tâche binaire, un fort qui contredit partout passerait aussi pour une récupération (cours, volet 2, §F, JB8). Parade : une tâche à vérité connue, lue sur les items tenus à part où le superviseur se trompe, avec l'accord du fort là où le superviseur a raison, et une copie entraînée sur les étiquettes vraies comme cas connu (cours, volet 2, §F, JB8).

### Insertion n°83, après la ligne 5139 de la v3.5

> Ancre : signal, delegation gains ground. What would kill it: an unchanged frontier — then the internal signal says nothing beyond the scorer.

> ⚠ **Limites et parades** : généralisation faible-vers-fort → volet 2, §F (après « En pratique — l'automatisation ») ; moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») *(v3.6)*

### Insertion n°85, après la ligne 5159 de la v3.5

> Ancre : else.

> ⚠ *(v3.6)* L'inhibition sur Sonnet 4.5 a la même limite qu'à la réponse 56 — des vecteurs de contrôle arbitraires font aussi monter le désalignement, plus faiblement, et un contrôle de même norme n'est que le nul de spécificité (fiche 2 ; cours, volet M, M4) — ; et le « moins d'un pour cent » de ton travail n'a pas encore été mesuré à dégradation égale (cours, volet 11, réponse A4). Parade : des sous-espaces aléatoires de même rang à dégradation appariée, une baseline de prompt et une courbe dose-réponse, et la partition refaite par le protocole de la réponse A4 (fiche 2 ; cours, volet 2, §C, K47 ; cours, volet 11, réponse A4).

### Insertion n°87, après la ligne 5159 de la v3.5

> Ancre : else.

> ⚠ *(v3.6)* Dans les cas où l'on « sait » si le modèle est en évaluation, on sait la règle installée et ses indices, pas ce que le modèle croit : l'organisme conditionné à l'évaluation ne suit pas sa règle à la lettre, et ne distingue pas de façon fiable évaluation et déploiement à partir d'indices subtils (fiche 10). Parade : étiqueter chaque entrée par sa conduite, jamais par la sonde, valider la sonde sur des formulations tenues à part, et prendre cet organisme comme cas connu de « je suis évalué » (passation, §5.2 ; explication du 2 octobre, parties 2 et 3 ; programme, parties 3 et 4).

### Insertion n°89, après la ligne 5159 de la v3.5

> Ancre : else.

> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; cas connu → volet M, M5 (fin de section) ; chaîne de pensée comme moniteur, et conscience verbalisée → volet 11, réponse 43 ; autoencodeurs en langage naturel → volet 4, La vague récente sur la cognition du modèle ; J-lens et espace de travail → volet 2, C bis (après « Le test, tel qu'il se dit ») ; sondes de désalignement, J-lens compris (encadré du 2 octobre) → volet 2, §A (avant le cas d'application K71), §C (avant le cas d'application K47) et C bis (avant le cas d'application K72) *(v3.6)*

### Insertion n°91, après la ligne 5179 de la v3.5

> Ancre : where the weak model is wrong — then the strong model is different without being more right.

> ⚠ *(v3.6)* Un juge fort pris pour vérité de terrain est un juge LLM, avec ses erreurs systématiques, et il peut partager celles du fort qu'il départage, comme un modèle qui s'audite presque lui-même (cours, volet 6, §2 ; fiches, partie B, piège 6 ; fiche 2). Parade : valider d'abord sur une tâche à vérité connue, lue sur les items tenus à part où le faible se trompe, avec une copie entraînée sur les étiquettes vraies comme cas connu, et sceller le juge, audité par des humains sur des items stratifiés (cours, volet 2, §F, JB8 ; programme, partie 3) ; pour un juge proche du modèle qu'il juge, aucune parade connue au-delà de cette validation ; on le dit (fiches, partie B, piège 6).

### Insertion n°93, après la ligne 5179 de la v3.5

> Ancre : where the weak model is wrong — then the strong model is different without being more right.

> ⚠ **Limites et parades** : généralisation faible-vers-fort → volet 2, §F (après « En pratique — l'automatisation ») ; juges LLM → volet 6, §2 (après « La loi de déplacement ») ; jeu tenu à part → volet M, M4 (après « Le jeu tenu à part ») *(v3.6)*

### Insertion n°95, après la ligne 5200 de la v3.5

> Ancre : positives on legitimate sessions exceed what a human can review.

> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») ; classifieurs de sûreté → volet 2, §H (fin du cas d'application G1) *(v3.6)*

### Insertion n°97, après la ligne 5221 de la v3.5

> Ancre : comparison: indistinguishable effects at four seeds — then more seeds are needed before concluding, not a preference.

> ⚠ *(v3.6)* La projection sur la direction du trait, lue d'un bras à l'autre, mêle l'effet cherché et un biais de mesure : l'entraînement change les représentations, et une direction calibrée sur un bras lirait autrement dans un autre (passation, §5.2) ; et le lien entre ce déplacement et le trait n'est que corrélationnel (fiche 8). Parade : une sonde neuve par bras et après l'entraînement, sur un jeu d'indices disjoint, la direction extraite aussi dans le modèle de base, et le trait au test comme critère principal, la projection restant une mesure séparée (passation, §5.2 ; programme, partie 3).

### Insertion n°99, après la ligne 5221 de la v3.5

> Ancre : comparison: indistinguishable effects at four seeds — then more seeds are needed before concluding, not a preference.

> ⚠ *(v3.6)* L'avantage hors distribution du midtraining a été lu sur des modèles ouverts, dans des scènes agentiques que le modèle peut reconnaître comme des tests (cours, volet 7, F·34). Parade : deux versions de chaque environnement, tirées au hasard, qui ne diffèrent que par des indices de réalisme notés par un discriminateur, avec un organisme dressé à se cacher comme cas connu (cours, volet 2, §B, K63).

### Insertion n°101, après la ligne 5221 de la v3.5

> Ancre : comparison: indistinguishable effects at four seeds — then more seeds are needed before concluding, not a preference.

> ⚠ **Limites et parades** : pilotage par vecteurs, dont vecteurs de persona → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; jeu tenu à part → volet M, M4 (après « Le jeu tenu à part ») ; évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; sondes de désalignement, J-lens compris (encadré du 2 octobre) → volet 2, §A (avant le cas d'application K71), §C (avant le cas d'application K47) et C bis (avant le cas d'application K72) *(v3.6)*

### Insertion n°103, après la ligne 5244 de la v3.5

> Ancre : instance.

> ⚠ *(v3.6)* La batterie aval est faite de scènes construites : le modèle peut y remarquer le test et se retenir, et dans une simulation, « c'est faux » est vrai, si bien qu'un pot de miel ne sépare pas un modèle qui le lit comme factice d'un modèle qui se retient (fiche 13 ; fiche 3) ; et sur un modèle récent, la scène d'alignment faking mesure peut-être la mémorisation du scénario, ses transcripts ayant été réinclus dans l'entraînement (fiches, partie C). Parade : deux versions de chaque environnement, tirées au hasard, qui ne diffèrent que par des indices de réalisme notés par un discriminateur, avec un organisme dressé à se cacher comme cas connu (cours, volet 2, §B, K63) ; contre le pot de miel lu comme factice et contre la mémorisation, aucune parade connue ; on le dit (fiche 3 ; fiches, partie C).

### Insertion n°105, après la ligne 5244 de la v3.5

> Ancre : instance.

> ⚠ **Limites et parades** : pilotage par vecteurs, dont vecteurs de persona → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») *(v3.6)*

### Insertion n°107, après la ligne 5267 de la v3.5

> Ancre : representation — then none of the three pieces sees it, and one should say so rather than sign.

> ⚠ *(v3.6)* « Si la capacité remonte […], c'est qu'elle était là » suppose que le fine-tuning ne l'a pas enseignée : un petit fine-tuning peut créer la capacité qu'on croit éliciter (cours, volet 2, §B, K63). Parade : une élicitation à budget fixé d'avance, rapportée comme une borne, dont le gain ne compte qu'au-delà de celui du même budget sur un modèle qui n'a pas la capacité, et un organisme entraîné à sous-performer comme cas connu (cours, volet M, M7 ; cours, volet 2, §B, K63 ; cours, volet 7, F·26).

### Insertion n°109, après la ligne 5267 de la v3.5

> Ancre : representation — then none of the three pieces sees it, and one should say so rather than sign.

> ⚠ *(v3.6)* Une remontée sous inhibition ne fait une preuve mécaniste qu'au-delà des témoins : dans la lignée des cartes système, des vecteurs de contrôle arbitraires bougent aussi le comportement, et un contrôle de même norme n'est que le nul de spécificité (fiche 2 ; cours, volet M, M4). Parade : plusieurs familles de témoins au même rang — sous-espaces aléatoires, contrastes sans rapport, directions de forte variance, simple prompt — comparées à dégradation appariée, et un organisme conditionné à l'évaluation comme cas connu de la sonde (programme, parties 3 et 7 ; explication du 2 octobre, partie 3).

### Insertion n°111, après la ligne 5267 de la v3.5

> Ancre : representation — then none of the three pieces sees it, and one should say so rather than sign.

> ⚠ **Limites et parades** : évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; désapprentissage et ré-élicitation → volet 2, §I (après « En pratique — l'unlearning mis à l'épreuve ») ; généralisation faible-vers-fort → volet 2, §F (après « En pratique — l'automatisation ») ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; cas connu → volet M, M5 (fin de section) ; sondes de désalignement, J-lens compris (encadré du 2 octobre) → volet 2, §A (avant le cas d'application K71), §C (avant le cas d'application K47) et C bis (avant le cas d'application K72) *(v3.6)*

### Insertion n°113, après la ligne 5290 de la v3.5

> Ancre : stronger.

> ⚠ *(v3.6)* Un moniteur qui partage les poids de l'acteur peut reconnaître les attaques synthétiques dont on connaît la réponse, et ne laisser passer que les vraies : un pot de miel ne sépare pas un modèle qui le lit comme factice d'un modèle qui se retient (fiche 3 ; cours, volet 2, §B). Parade partielle : mesurer le réalisme de ces attaques par un juge mis devant la paire, et donner à leur construction de vraies ressources de déploiement (cours, volet 7, F·25) ; contre un moniteur qui lit le pot de miel comme factice, aucune parade connue ; on le dit (fiche 3).

### Insertion n°115, après la ligne 5290 de la v3.5

> Ancre : stronger.

> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») *(v3.6)*

### Insertion n°117, après la ligne 5312 de la v3.5

> Ancre : answers, only that it's stable.

> ⚠ *(v3.6)* Qu'inhiber la direction « l'utilisateur croit X » change la réponse ne montre la mauvaise raison qu'au-delà du dommage et d'un concept voisin : retirer une direction abîme aussi le modèle, et un effet d'ablation dit la nécessité, pas la spécificité (cours, volet M, M4). Parade : comparer à des sous-espaces aléatoires de même rang et à la direction rivale — « la réponse est vraie » —, tous à dégradation appariée (cours, volet M, M4).

### Insertion n°119, après la ligne 5312 de la v3.5

> Ancre : answers, only that it's stable.

> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; ablation et projection → volet 2, §D (après « La méthode ») ; dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») ; chaîne de pensée comme moniteur → volet 11, réponse 43 ; auto-rapport et introspection → volet 5, partie II, A, sujet 13 *(v3.6)*

### Insertion n°121, après la ligne 5334 de la v3.5

> Ancre : depend on N — then it's not a population effect, and the failure mode is individual.

> ⚠ *(v3.6)* Ce 1,0 contre 0,35 est le score d'une seule des douze tâches, en organisations simulées, et sa fiche n'a lu que le résumé : ni les contrôles internes ni les limites de détail (cours, volet 7, F·39). Parade : le dire comme le score d'une tâche simulée, et lire l'article en entier avant de s'en servir, comme la fiche le demande (cours, volet 7, F·39).

### Insertion n°123, après la ligne 5334 de la v3.5

> Ancre : depend on N — then it's not a population effect, and the failure mode is individual.

> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») *(v3.6)*

### Insertion n°125, après la ligne 5356 de la v3.5

> Ancre : and that's the contested RLHF result, only worse.

> ⚠ *(v3.6)* Ce 0,88 est l'AUROC d'un détecteur fine-tuné, sur une suite de modèles rendus malhonnêtes, donc construits ; sa fiche, faite d'extraits, ne dit pas s'il est mesuré sur des types tenus à part, alors qu'une AUROC ne vaut que par cet écart (cours, volet 7, F·62 ; fiches, partie B, pièges 1 et 5 ; fiche 7) ; et la réserve qui ouvre la version française — un résultat absent de la base, à comprendre, pas à dire — vaut aussi pour la version anglaise, qui ne la porte pas (cours, volet M, M10, item 12). Parade : une validation croisée par types de mensonge tenus à part, et conclure sur l'instrument, pas sur la malhonnêteté naturelle (fiche 7 ; programme, partie 8).

### Insertion n°127, après la ligne 5356 de la v3.5

> Ancre : and that's the contested RLHF result, only worse.

> ⚠ *(v3.6)* Deux des trois tests ont leur propre limite : un déplacement nul est un nul, qui ne compte que si le même dispositif voit le déplacement du modèle avant l'entraînement à l'honnêteté, au même réglage, et se dit comme une borne (cours, volet M, M5) ; et que l'inhibition fasse revenir les mensonges ne prouve un changement interne qu'à dégradation appariée, des erreurs dues au dommage pouvant se compter comme des mensonges si l'étiquette ne vérifie pas la contradiction avec la croyance du modèle (cours, volet M, M4 ; fiche 7). Parade : ce cas connu dans le même protocole, des sous-espaces aléatoires de même rang à dégradation appariée, et des mensonges étiquetés contre la croyance obtenue en contexte neutre (cours, volet M, M4 et M5 ; fiche 7).

### Insertion n°129, après la ligne 5356 de la v3.5

> Ancre : and that's the contested RLHF result, only worse.

> ⚠ **Limites et parades** : détecteurs fine-tunés → volet 7, F·29 ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; juges LLM → volet 6, §2 (après « La loi de déplacement ») ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; cas connu → volet M, M5 (fin de section) *(v3.6)*

### Insertion n°131, après la ligne 5375 de la v3.5

> Ancre : What would make it decisive: a single transcript in that cell.

> ⚠ *(v3.6)* Une case vide est un nul : il ne compte que si un organisme à qui l'on a installé l'une de ces stratégies, rejoué dans le même harnais, remplit la case « exécute » ; et le modèle de production peut aussi reconnaître le test et se retenir (cours, volet M, M5 ; fiche 13 ; cours, volet 2, §B). Parade : ce cas connu, deux versions de chaque tâche qui ne diffèrent que par des indices de réalisme notés par un discriminateur, et un budget fixé d'avance, le résultat dit comme une borne à ce budget, jamais comme une absence (cours, volet 2, §B, K63 ; cours, volet M, M5 et M7).

### Insertion n°133, après la ligne 5375 de la v3.5

> Ancre : What would make it decisive: a single transcript in that cell.

> ⚠ **Limites et parades** : red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») ; moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; cas connu → volet M, M5 (fin de section) *(v3.6)*
