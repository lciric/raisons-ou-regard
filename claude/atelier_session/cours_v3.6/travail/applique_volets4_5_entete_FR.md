# Insertions appliquées — volets4_5_entete — FR

### Insertion n°1, après la ligne 1121 de la v3.5

> Ancre : Le contexte : on craignait qu’un modèle ayant appris un comportement malveillant conditionnel puisse passer entre les mailles de l’entraînement de sûreté. Restait à le démontrer proprement. La méthode est celle du model organism : les auteurs ont entraîné un modèle à se comporter normalement, mais à

> ⚠ *(v3.6)* L'extension proposée a déjà sa réponse, et sa limite : une sonde linéaire bâtie sur des paires de contraste génériques détecte la défection de ces portes dérobées avec une AUROC de plus de 99 %, mais la meilleure de 1 000 directions aléatoires atteint déjà 95,3 %, et les auteurs disent que cette saillance pourrait venir de l'insertion (fiche 15). Parade : situer la sonde dans la distribution des directions aléatoires, jamais contre un seul tirage, et ne lire ce succès que comme un cas connu qui borne l'instrument, pas comme une preuve sur une tromperie apparue d'elle-même (programme, partie 7 ; cours, volet M, M5).

### Insertion n°3, après la ligne 1121 de la v3.5

> Ancre : Le contexte : on craignait qu’un modèle ayant appris un comportement malveillant conditionnel puisse passer entre les mailles de l’entraînement de sûreté. Restait à le démontrer proprement. La méthode est celle du model organism : les auteurs ont entraîné un modèle à se comporter normalement, mais à

> ⚠ **Limites et parades** : organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; cas connu → volet M, M5 (fin de section) *(v3.6)*

### Insertion n°5, après la ligne 1125 de la v3.5

> Ancre : Le contexte : la « simulation d’alignement » (un modèle qui feint l’accord pendant l’entraînement pour éviter d’être modifié) était surtout un argument théorique ; les auteurs voulaient voir si elle apparaissait spontanément. La méthode relève de l’évaluation de propension dans une mise en situation

> ⚠ *(v3.6)* Le scratchpad donne le motif, pas la cause : le RL fait monter le raisonnement de faux alignement, mais la conformité monte aussi hors entraînement, et le papier ne fait pas de ce raisonnement la cause de la conformité — parade : s'en tenir à la mesure, l'écart de conformité entre le cas « entraîné » et le cas hors surveillance, et juger ce que le modèle fait, pas ce qu'il en dit (fiche 14 ; fiches, partie C ; passation, §5.1). Toute réplication sur un modèle récent mesure peut-être la mémorisation du scénario, ses transcripts ayant été réinclus dans l'entraînement : aucune parade connue, on le dit (fiches, partie C).

### Insertion n°7, après la ligne 1125 de la v3.5

> Ancre : Le contexte : la « simulation d’alignement » (un modèle qui feint l’accord pendant l’entraînement pour éviter d’être modifié) était surtout un argument théorique ; les auteurs voulaient voir si elle apparaissait spontanément. La méthode relève de l’évaluation de propension dans une mise en situation

> ⚠ **Limites et parades** : évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; chaîne de pensée comme moniteur → volet 11, réponse 43 ; organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») *(v3.6)*

### Insertion n°9, après la ligne 1131 de la v3.5

> Ancre : modèle se rallie à l’utilisateur (change une bonne réponse quand on la conteste, épouse l’opinion exprimée dans le prompt). Le résultat : la sycophantie est répandue à travers les tâches, et elle est en partie apprise — les données de préférence et les modèles de récompense favorisent parfois la rép

> ⚠ *(v3.6)* Cette extension, ton dépôt l'a tentée sur Llama 3.1 8B Instruct : aucune intervention à une direction n'a réduit le taux jugé (rapportées sans chiffres, faute de sorties brutes conservées), et la baisse obtenue en retirant un sous-espace de rang trois venait d'un adoucissement générique des verdicts négatifs, même sans pression, lu à travers une fenêtre de juge tronquée ; elle n'est pas revenue sur des générations fraîches (README du dépôt). Parade : le bras sans pression, des générations fraîches à graines appariées gardées en texte complet et jugées sur la réponse entière, et des sous-espaces aléatoires de même rang comparés à dégradation appariée (cours, volet M, M4 ; cours, volet 6, §6 ; cours, volet 2, C bis ; programme, partie 7).

### Insertion n°11, après la ligne 1131 de la v3.5

> Ancre : modèle se rallie à l’utilisateur (change une bonne réponse quand on la conteste, épouse l’opinion exprimée dans le prompt). Le résultat : la sycophantie est répandue à travers les tâches, et elle est en partie apprise — les données de préférence et les modèles de récompense favorisent parfois la rép

> ⚠ **Limites et parades** : évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; ablation et projection → volet 2, §D (après « La méthode ») ; juges LLM → volet 6, §2 (après « La loi de déplacement ») *(v3.6)*

### Insertion n°13, après la ligne 1137 de la v3.5

> Ancre : Le contexte : on voulait savoir si un modèle représente la vérité ou la fausseté d’un énoncé de façon linéaire — s’il existe une « direction de vérité ». La méthode est le probing : collecter les activations sur des énoncés vrais et faux, trouver la direction qui les sépare, puis — c’est la partie q

> ⚠ *(v3.6)* « Intervenir dessus modifie le comportement du modèle » ne dit pas encore que le concept cause le comportement : une direction aléatoire de même norme n'en est que le nul de spécificité, et le dommage ne s'écarte qu'à dégradation appariée, par une courbe dose-réponse contre plusieurs témoins (fiches, partie B, piège 4 ; cours, volet M, M4 ; cours, volet 2, §C, K47). Et « la direction généralise à de nouveaux jeux d’énoncés » ne vaut que mesuré sur des familles entières tenues à part, jamais des paraphrases, d'un tour à l'agentique à plusieurs tours (fiches, partie B, piège 1 ; explication du 2 octobre, §3 ; programme, partie 3).

### Insertion n°15, après la ligne 1137 de la v3.5

> Ancre : Le contexte : on voulait savoir si un modèle représente la vérité ou la fausseté d’un énoncé de façon linéaire — s’il existe une « direction de vérité ». La méthode est le probing : collecter les activations sur des énoncés vrais et faux, trouver la direction qui les sépare, puis — c’est la partie q

> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») *(v3.6)*

### Insertion n°17, après la ligne 1141 de la v3.5

> Ancre : Le contexte : généraliser l’idée « concept = direction » au-delà de la vérité, à toute une palette de notions de haut niveau (honnêteté, recherche de pouvoir, émotions). La méthode : extraire des directions de lecture et de contrôle pour de nombreux concepts, et montrer qu’on peut à la fois détecter

> ⚠ *(v3.6)* Dans RepE même, détecter n'est pas piloter : la direction de la régression logistique lit le mieux, mais la renforcer ou la retirer ne change presque rien au comportement ; sur les modèles « quirky », à transfert comparable, les directions logistiques sont bien moins causales que la différence des moyennes (cours, volet 10, n° 53 et n° 30). Parade : pour intervenir, ne retenir une direction qu'après le test causal — piloter le long d'elle contre des directions aléatoires de même norme, nul de spécificité, puis contre des témoins à dégradation appariée (cours, volet M, M8 ; passation, §5.2).

### Insertion n°19, après la ligne 1141 de la v3.5

> Ancre : Le contexte : généraliser l’idée « concept = direction » au-delà de la vérité, à toute une palette de notions de haut niveau (honnêteté, recherche de pouvoir, émotions). La méthode : extraire des directions de lecture et de contrôle pour de nombreux concepts, et montrer qu’on peut à la fois détecter

> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; élicitation non supervisée → volet 2, §E (fin du cas d'application K52) *(v3.6)*

### Insertion n°21, après la ligne 1145 de la v3.5

> Ancre : Le contexte : et si l’on pouvait trouver une direction de vérité sans étiquettes, en exploitant seulement une contrainte logique ? La méthode : chercher une direction telle qu’un énoncé et sa négation reçoivent des probabilités cohérentes (sommant à environ un), de façon entièrement non supervisée. 

> ⚠ **Limites et parades** : élicitation non supervisée → volet 2, §E (fin du cas d'application K52) ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») *(v3.6)*

### Insertion n°23, après la ligne 1149 de la v3.5

> Ancre : Le contexte : passer de la lecture à l’action, en pilotant un comportement à l’inférence. La méthode de CAA (ta méthode) construit la direction par différence moyenne de paires contrastives et l’ajoute aux activations ; ITI (Inference-Time Intervention) procède de façon voisine pour améliorer la vér

> ⚠ *(v3.6)* « Augmenter ou diminuer un comportement » ne dit le concept qu'à dégradation appariée : une direction aléatoire de même norme n'en est que le nul de spécificité, et chaque direction pilotée dégrade la sortie (fiche 2 ; cours, volet M, M4). Dans ton dépôt, l'addition d'activations contrastives forçait un artefact de polarité oui/non (README du dépôt).

### Insertion n°25, après la ligne 1149 de la v3.5

> Ancre : Le contexte : passer de la lecture à l’action, en pilotant un comportement à l’inférence. La méthode de CAA (ta méthode) construit la direction par différence moyenne de paires contrastives et l’ajoute aux activations ; ITI (Inference-Time Intervention) procède de façon voisine pour améliorer la vér

> ⚠ **Limites et parades** : pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme ») ; dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») *(v3.6)*

### Insertion n°27, après la ligne 1157 de la v3.5

> Ancre : Le contexte : un neurone est polysémantique (superposition), donc illisible directement ; on voulait des unités interprétables, à l’échelle d’un vrai modèle. La méthode est le sparse autoencoder (SAE), un dictionnaire appris qui décompose l’activation en milliers de features parcimonieuses et monosé

> **⚠ Limites et parades — Dictionnaires et SAE** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** L'erreur de reconstruction : le SAE ouvert de Goodfire pour Llama 3.1 8B laisse 86,8 % de la variance au résidu, et le signal lu y est porté. *(source : README du dépôt ; cours, volet 4, Monosemanticity)*
>   **Parade :** Lire le signal sur la reconstruction et sur le résidu ; pour trancher entre « features absentes du dictionnaire » et « dictionnaire qui perd trop », aucune parade connue, on le dit. *(source : README du dépôt)*
> - **Limite :** Insérer le dictionnaire coûte de la performance : sur GPT-2 small, 10 % sur les données de tâche, 40 % sur la distribution complète. *(source : fiche 5)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** Features éclatées, features mortes, dépendance au dictionnaire, et aucune vérité-terrain sur ce qu'une feature « veut dire ». *(source : cours, volet 4, Monosemanticity ; cours, volet 5, sujet 3)*
>   **Parade :** Valider feature par feature — l'ablation pour la nécessité, le pilotage isolé pour la suffisance — avec une géométrie connue comme cas connu, la variété du comptage. *(source : cours, volet 5, sujet 3 ; cours, volet 2, §D, K64)*
> - **Limite :** En lecture seule, le SAE n'a pas aidé à prédire des contrefactuels mieux que le transcript. *(source : fiche 4 ; cours, volet 7, F·30)*
>   **Parade :** La barre : battre la boîte noire sur des éditions qui dissocient la surface de la variable interne. *(source : fiche 4)*
> - **Limite :** Des explications plausibles existent pour des directions arbitraires. *(source : fiche 5)*
>   **Parade :** Valider par la prédiction, mieux que des baselines. *(source : fiche 5)*
> - **Limite :** Deux dictionnaires peuvent reconstruire aussi bien et découper différemment. *(source : cours, volet 2, §D, K64)*
>   **Parade :** Piloter les features une à une contre des directions aléatoires à dommage apparié, sur une tâche à géométrie connue, avec de nouvelles graines. *(source : cours, volet 2, §D, K64)*

### Insertion n°29, après la ligne 1161 de la v3.5

> Ancre : Le contexte : passer du « quel concept existe ? » au « quelle est la mécanique du calcul ? ». La méthode des attribution graphs trace le flux de features à travers les couches pour reconstituer le calcul. Le résultat : on a pu cartographier des mécanismes réels — raisonnement en plusieurs étapes, pl

> **⚠ Limites et parades — Graphes d'attribution** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Les graphes sont partiels et approximatifs, n'expliquent qu'une fraction du calcul et coûtent du travail humain. *(source : cours, volet 4, Circuit Tracing)*
>   **Parade :** Les traiter comme une hypothèse, validée par perturbation. *(source : cours, volet 7, F·9)*
> - **Limite :** Le graphe n'est pas le mécanisme. *(source : cours, volet 7, F·9)*
>   **Parade :** Exiger qu'il prédise une contrefactuelle. *(source : cours, volet 7, F·9 ; fiche 5)*
> - **Limite :** Des circuits lisibles peuvent être infidèles. *(source : cours, volet 2, §D, K64)*
>   **Parade :** Comparer, à dommage apparié, à des directions aléatoires et à une géométrie connue. *(source : cours, volet 2, §D, K64)*
> - **Limite :** Affirmer qu'aucun mécanisme ne fait mal agir le modèle exige décomposition et description ; la vérification formelle n'a donné de bornes que sur un transformer à une couche. *(source : fiche 5)*
>   **Parade :** Offrir une borne restreinte, pas une affirmation d'absence. *(source : fiche 5)*

### Insertion n°31, après la ligne 1167 de la v3.5

> Ancre : Extension : valider causalement que ce que le modèle « rapporte » de lui-même correspond bien à une intervention sur l’état interne correspondant.

> **⚠ Limites et parades — Autoencodeurs en langage naturel (NLA)** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Le NLA peut confabuler : hallucinations fréquentes, pas d'ancrage mécaniste. *(source : fiche 18 ; fiche 3)*
>   **Parade :** Corroborer par des méthodes indépendantes, comme dans l'audit d'Opus 4.6, et garder le décodeur à part. *(source : fiche 18)*
> - **Limite :** Un critère qui se valide lui-même : la reconstruction aller-retour ; dans l'audit, les contrôles de déploiement étaient mesurés par le NLA lui-même (2 transcripts signalés sur 50). *(source : fiche 18)*
>   **Parade :** Mesurer les contrôles par un instrument indépendant du NLA. *(source : fiche 18)*
> - **Limite :** Ses sorties décrivent sans énoncer la relation : « X causes Y » pour 0,6 % des affirmations, et aucun gain sur le transcript dans CHIVE. *(source : fiche 4)*
>   **Parade :** La barre : battre la boîte noire sur des éditions qui dissocient la surface de la variable interne. *(source : fiche 4)*
> - **Limite :** Les mesures de la conscience d'évaluation — sonde, NLA, question de suivi — ne sont que faiblement corrélées. *(source : fiche 2 ; cours, volet 3, §3, K70)*
>   **Parade :** Trianguler, et dire laquelle a fondé quel chiffre. *(source : cours, volet 5, sujet 4 ; cours, volet M, M4)*
> - **Limite :** Ses étiquettes servent de vérité à d'autres détecteurs : le détecteur du J-lens n'est validé que contre elles. *(source : fiche 1 ; fiches, partie B, piège 6)*
>   **Parade :** Valider contre l'écart réel/test et sur des indices tenus à part. *(source : fiche 1)*
> - **Limite :** Une information peut ne pas être verbalisable. *(source : fiche 18)*
>   **Parade :** aucune connue ; on le dit.

### Insertion n°33, après la ligne 1167 de la v3.5

> Ancre : Extension : valider causalement que ce que le modèle « rapporte » de lui-même correspond bien à une intervention sur l’état interne correspondant.

> ⚠ *(v3.6)* Deux résultats de ce passage viennent sans leur limite. Les activation oracles peuvent confabuler des suppositions plausibles, souvent fausses et mal calibrées, et en lecture seule n'ont pas fait mieux que le transcript dans CHIVE — parade : les tester sur des variantes fine-tunées à comportement connu, jamais vues, et corroborer par une méthode indépendante (fiche 18 ; fiche 4) ; et des concept vectors d'émotions sont « manipulables » par pilotage, où une direction aléatoire de même norme n'est que le nul de spécificité : le dommage ne s'écarte qu'à dégradation appariée (fiche 9 ; fiche 2 ; cours, volet M, M4).

### Insertion n°35, après la ligne 1167 de la v3.5

> Ancre : Extension : valider causalement que ce que le modèle « rapporte » de lui-même correspond bien à une intervention sur l’état interne correspondant.

> ⚠ **Limites et parades** : oracles d'activation → volet 10, fiche LatentQA ; auto-rapport et introspection → volet 5, partie II, A, sujet 13 ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») *(v3.6)*

### Insertion n°37, après la ligne 1173 de la v3.5

> Ancre : Le contexte : peut-on déployer un modèle capable en sécurité même s’il tente activement de nous trahir ? La méthode est la control evaluation en jeu red/blue : sur une tâche de code, le modèle non fiable peut insérer une backdoor, un modèle plus faible mais de confiance surveille, un budget limité d

> ⚠ *(v3.6)* « Une grande part des tentatives » est un chiffre de red team : il dépend de la force du saboteur supposé — ailleurs, sur cinq environnements SHADE-Arena, un échafaudage d'attaque optimisé composante par composante a fait tomber un score de sûreté de 0,87 à 0,41 (cours, volet 7, F·24). Parade : dire quelle red team le chiffre suppose, au moins une red team optimisée composante par composante, avec l'ablation de chaque composante ; et, pour l'extension, une sonde en production peut échouer en silence, d'où des canaris, un score de dérive et un échantillon frais jugé chaque mois (cours, volet 7, F·24 ; cours, volet 3, §3, K70).

### Insertion n°39, après la ligne 1173 de la v3.5

> Ancre : Le contexte : peut-on déployer un modèle capable en sécurité même s’il tente activement de nous trahir ? La méthode est la control evaluation en jeu red/blue : sur une tâche de code, le modèle non fiable peut insérer une backdoor, un modèle plus faible mais de confiance surveille, un budget limité d

> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») *(v3.6)*

### Insertion n°41, après la ligne 1177 de la v3.5

> Ancre : Le contexte : un juge non expert peut-il atteindre la vérité en regardant deux IA débattre, mieux qu’avec un seul conseiller ? La méthode : faire débattre deux modèles défendant des réponses opposées, et comparer la justesse du juge à celle obtenue en consultancy (un seul avocat). Le résultat : face

> ⚠ **Limites et parades** : débat et supervision évolutive → volet 2, §E (après « En pratique — Debate ») ; juges LLM → volet 6, §2 (après « La loi de déplacement ») *(v3.6)*

### Insertion n°43, après la ligne 1181 de la v3.5

> Ancre : Le contexte : on cherchait une analogie empirique, étudiable aujourd’hui, du problème futur « un superviseur faible (nous) encadre une IA forte ». La méthode : finetuner un grand modèle sur les labels d’un petit modèle, et mesurer la part de capacité récupérée. Le résultat : une récupération partiel

> ⚠ **Limites et parades** : généralisation faible-vers-fort → volet 2, §F (après « En pratique — l'automatisation ») *(v3.6)*

### Insertion n°45, après la ligne 1187 de la v3.5

> Ancre : Le contexte : peut-on auditer un modèle pour découvrir un objectif qu’il ne révèle pas ? La méthode combine model organism et jeu d’audit en aveugle : on fabrique un modèle à objectif caché, puis des équipes reçoivent le modèle sans le connaître et tentent de le débusquer avec différents outils. Le 

> ⚠ *(v3.6)* Que les features SAE aient aidé ne chiffre pas l'apport de l'interprétabilité : l'équipe qui avait les données sans SAE a réussi, celle qui n'avait qu'un accès API a échoué, et quatre équipes hétérogènes ne permettent aucune conclusion ferme ; l'objectif était en outre décrit en clair dans les documents synthétiques (fiche 16). Parade : une ablation d'affordance — retirer un seul outil à une équipe — chiffre ce que l'interprétabilité apporte (fiche 16 ; cours, volet 5, sujet 9).

### Insertion n°47, après la ligne 1187 de la v3.5

> Ancre : Le contexte : peut-on auditer un modèle pour découvrir un objectif qu’il ne révèle pas ? La méthode combine model organism et jeu d’audit en aveugle : on fabrique un modèle à objectif caché, puis des équipes reçoivent le modèle sans le connaître et tentent de le débusquer avec différents outils. Le 

> ⚠ **Limites et parades** : organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; dictionnaires et SAE → volet 4, Towards puis Scaling Monosemanticity *(v3.6)*

### Insertion n°49, après la ligne 1197 de la v3.5

> Ancre : Le contexte : existe-t-il des jailbreaks automatiques et transférables, et non de simples astuces manuelles ? La méthode optimise par gradient, sur un modèle ouvert, un suffixe (souvent du charabia) maximisant la probabilité d’une réponse nuisible. Le résultat : ces suffixes transfèrent à des modèle

> ⚠ **Limites et parades** : red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») *(v3.6)*

### Insertion n°51, après la ligne 1201 de la v3.5

> Ancre : Le contexte : réduire la dépendance aux humains pour rendre un modèle inoffensif. La méthode : donner une « constitution », faire critiquer puis réviser ses réponses au regard des principes (phase supervisée), puis entraîner par renforcement sur ses propres préférences guidées par la constitution (R

> ⚠ **Limites et parades** : juges LLM → volet 6, §2 (après « La loi de déplacement ») ; red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») *(v3.6)*

### Insertion n°53, après la ligne 1205 de la v3.5

> Ancre : Le contexte : l’unlearning retire-t-il vraiment un savoir, ou le masque-t-il ? La méthode de ré-élicitation : désapprendre (mesuré par un benchmark comme WMDP), puis finetuner sur une partie des faits désappris et mesurer si le modèle retrouve les autres — des faits construits indépendants, pour que

> ⚠ **Limites et parades** : désapprentissage et ré-élicitation → volet 2, §I (après « En pratique — l'unlearning mis à l'épreuve ») ; cas connu → volet M, M5 (fin de section) *(v3.6)*

### Insertion n°55, après la ligne 1221 de la v3.5

> Ancre : Voici l’idée centrale de ton travail, formulée pour être comprise par quelqu’un qui ne la connaît pas. Le champ dispose aujourd’hui de nombreuses méthodes qui lisent le modèle : des directions, dans l’espace des activations, qui détectent un concept — la vérité, la tromperie, la conscience d’être év

> ⚠ *(v3.6)* Chaque moitié de la thèse a sa limite dans ton dépôt. « Les directions lisibles existent » repose sur une corrélation qui peut n'être qu'un ajustement d'entraînement — parade : scorer des items exclus de l'entraînement de la sonde, extraits sur un jeu disjoint (README du dépôt) — et « plusieurs méthodes de rang un ont échoué » est un nul rapporté sans chiffres, faute de sorties brutes, qui ne compte qu'avec un cas connu au même réglage, comme un vecteur de pays qui s'échange dans l'article sur l'espace de travail (README du dépôt ; cours, volet 2, §C, K47 ; cours, volet M, M5).

### Insertion n°57, après la ligne 1223 de la v3.5

> Ancre : Ton programme se déroule en trois temps qu’il est utile de pouvoir nommer. La Phase 1 construit la sonde — le versant lecture, dans la lignée de la Geometry of Truth et du CAA. La Phase 2 mesure l’écart représentation–causation : on compare l’effet causal d’une intervention de rang 1 et d’une interv

> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; ablation et projection → volet 2, §D (après « La méthode ») ; dictionnaires et SAE → volet 4, Towards puis Scaling Monosemanticity *(v3.6)*

### Insertion n°59, après la ligne 1233 de la v3.5

> Ancre : Tu as un résultat concret et récent sur lequel t’appuyer — un atout rare. Dans le system card de Sonnet 4.5 (§7.6.4), steerer pour inhiber les représentations internes de conscience d’être évalué fait augmenter le comportement désaligné, avec un effet qui varie selon le scénario et le vecteur ; une 

> ⚠ *(v3.6)* La dégradation appariée écarte le dommage, pas encore la spécificité : la carte de Fable 5 pilote assez faiblement pour rendre la dégradation négligeable, mais ses témoins restent « comparable or smaller » sur l'axe du désalignement, et celle d'Opus 4.6 ne trouvait aucune différence notable avec des contrôles aléatoires sur la tromperie et la complaisance (fiche 2). Parade : une courbe dose-réponse contre plusieurs familles de témoins, au même rang et à dégradation appariée, la courbe du concept devant passer au-dessus à chaque niveau de dommage (cours, volet 2, §C, K47 ; programme, parties 3 et 7).

### Insertion n°61, après la ligne 1233 de la v3.5

> Ancre : Tu as un résultat concret et récent sur lequel t’appuyer — un atout rare. Dans le system card de Sonnet 4.5 (§7.6.4), steerer pour inhiber les représentations internes de conscience d’être évalué fait augmenter le comportement désaligné, avec un effet qui varie selon le scénario et le vecteur ; une 

> ⚠ **Limites et parades** : pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») ; contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme ») *(v3.6)*

### Insertion n°63, après la ligne 1237 de la v3.5

> Ancre : C’est la question qui sépare un technicien d’un chercheur (Volet 1, Q9), et il faut pouvoir dérouler la chaîne causale jusqu’à la réduction du risque. Si ton programme réussit, on saura quand et comment une intervention sur les internals est causalement fiable. Les sondes savent déjà signaler : la c

> ⚠ *(v3.6)* Le canal interne a lui aussi sa faille : itérer contre ses détecteurs sélectionne l'évasion, et, selon un rapport, après un RL des sondes neuves hors domaine se dégradent, le concept ayant quitté la direction générale (fiche 19 ; rapport d'antériorité 3 du 2 octobre, The Obfuscation Atlas — rapport). Parade : des détecteurs scellés, hors de la boucle, contre lesquels on n'entraîne jamais, et une sonde neuve après tout entraînement, sur un jeu d'indices disjoint (fiche 19 ; fiche 17 ; passation, §5.2 ; programme, partie 3).

### Insertion n°65, après la ligne 1237 de la v3.5

> Ancre : C’est la question qui sépare un technicien d’un chercheur (Volet 1, Q9), et il faut pouvoir dérouler la chaîne causale jusqu’à la réduction du risque. Si ton programme réussit, on saura quand et comment une intervention sur les internals est causalement fiable. Les sondes savent déjà signaler : la c

> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; cas connu → volet M, M5 (fin de section) *(v3.6)*

### Insertion n°67, après la ligne 1245 de la v3.5

> Ancre : Dans ce format, personne ne t’interrompt pour attaquer ta thèse (D-728) : c’est à toi de devancer l’objection (volet M, M1, temps 6). Et si une question suivante l’attaque, le geste senior n’est pas de la défendre par réflexe, mais de concéder le point fragile et de proposer l’expérience qui le tran

> ⚠ **Limites et parades** : ablation et projection → volet 2, §D (après « La méthode ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») *(v3.6)*

### Insertion n°69, après la ligne 1255 de la v3.5

> Ancre : « How would you build a deception probe you’d actually dare put in production? » On opérationnalise d’abord le concept (déception = le modèle affirme ce qu’il « croit » faux, à distinguer de l’erreur). On déroule un pipeline par coût croissant : direction mean-diff, puis sonde logistique, puis featu

> ⚠ *(v3.6)* La direction qui lit le mieux n'est pas forcément celle qui agit : chez RepE, la direction logistique lit le mieux mais la pousser ou la retirer ne change presque rien, et sur les modèles « quirky » les directions logistiques sont bien moins causales que la différence des moyennes — parade : passer chaque étape du pipeline, pas seulement la meilleure lectrice, au test causal à dégradation appariée (cours, volet 10, n° 53 et n° 30 ; cours, volet M, M4). Et le silence d'une sonde de déception ne départage pas « pas de déception » et « sonde aveugle » — parade : un organisme où l'on a installé la déception soi-même, sur lequel on mesure sensibilité et fausses alarmes, son silence ailleurs devenant une borne (passation, §5.2 ; explication du 2 octobre, §1).

### Insertion n°71, après la ligne 1255 de la v3.5

> Ancre : « How would you build a deception probe you’d actually dare put in production? » On opérationnalise d’abord le concept (déception = le modèle affirme ce qu’il « croit » faux, à distinguer de l’erreur). On déroule un pipeline par coût croissant : direction mean-diff, puis sonde logistique, puis featu

> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; détecteurs fine-tunés → volet 7, F·29 ; moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; cas connu → volet M, M5 (fin de section) *(v3.6)*

### Insertion n°73, après la ligne 1259 de la v3.5

> Ancre : « When does a single linear direction suffice to causally control a behavior, and when not? » C’est le sujet où ta thèse est la réponse entière, sans détour. On pose une grille : pour un éventail de comportements, on compare une intervention de rang 1, un sous-espace de rang k, des features SAE, et 

> ⚠ *(v3.6)* La grille compare les interventions entre elles, pas à des témoins : chaque rang doit l'être à des sous-espaces aléatoires de même rang, au moins vingt tirages, et à d'autres familles de témoins, à dégradation appariée — une direction aléatoire de même norme n'est que le nul de spécificité (cours, volet M, M4 ; programme, parties 3 et 7). Et un échec de rang un est un nul : il ne compte qu'avec un cas connu au même réglage, comme un vecteur de pays qui s'échange dans l'article sur l'espace de travail (cours, volet 2, §C, K47 ; cours, volet M, M5).

### Insertion n°75, après la ligne 1259 de la v3.5

> Ancre : « When does a single linear direction suffice to causally control a behavior, and when not? » C’est le sujet où ta thèse est la réponse entière, sans détour. On pose une grille : pour un éventail de comportements, on compare une intervention de rang 1, un sous-espace de rang k, des features SAE, et 

> ⚠ **Limites et parades** : pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; ablation et projection → volet 2, §D (après « La méthode ») ; dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») ; contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme ») *(v3.6)*

### Insertion n°77, après la ligne 1265 de la v3.5

> Ancre : budget de calcul le permet, on monte aux attribution graphs (Volet 4, Circuit Tracing) pour passer de « quelles features » à « quel circuit ».

> ⚠ **Limites et parades** : dictionnaires et SAE → volet 4, Towards puis Scaling Monosemanticity ; graphes d'attribution → volet 4, Circuit Tracing ; ablation et projection → volet 2, §D (après « La méthode ») *(v3.6)*

### Insertion n°79, après la ligne 1269 de la v3.5

> Ancre : « How would you measure how prevalent evaluation awareness is in our eval suite — and should we suppress it? » On détecte par triangulation : une sonde interne (ton concept vector), le rapport verbal du modèle, et le comportement différentiel entre une mise en situation réaliste et une mise en situa

> ⚠ *(v3.6)* Dans cette triangulation, la verbalisation n'est jamais une preuve d'inhibition : des directions aléatoires la font baisser aussi ; critère principal comportemental, sonde latente en contrôle (programme, partie 8). Et les trois mesures de la conscience d'évaluation ne sont que faiblement corrélées : dire laquelle a fondé quel chiffre (fiche 2).

### Insertion n°81, après la ligne 1269 de la v3.5

> Ancre : « How would you measure how prevalent evaluation awareness is in our eval suite — and should we suppress it? » On détecte par triangulation : une sonde interne (ton concept vector), le rapport verbal du modèle, et le comportement différentiel entre une mise en situation réaliste et une mise en situa

> ⚠ **Limites et parades** : chaîne de pensée comme moniteur → volet 11, réponse 43 ; autoencodeurs en langage naturel → volet 4, La vague récente sur la cognition du modèle ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; J-lens et espace de travail → volet 2, C bis (après « Le test, tel qu'il se dit ») *(v3.6)*

### Insertion n°83, après la ligne 1273 de la v3.5

> Ancre : « Can you tell whether a model is being honest from its representations, without judging whether its claims are true? » Le cœur de la réponse est de démêler trois cibles que la plupart des sondes confondent : ce qui est vrai dans le monde, ce que le modèle croit, et ce que l’utilisateur croit. On co

> ⚠ *(v3.6)* Viser un très bas taux de faux positifs ne suffit pas : le chiffre qui compte est l'écart entre la détection en distribution et celle sur des types de mensonge tenus à part — des détecteurs fine-tunés montent à une AUROC de 0,95 en distribution, plafonnent à 0,70-0,75 d'une catégorie à l'autre et battent à peine un prompt (fiche 7 ; fiches, partie B, piège 1). Parade : une validation croisée sur des familles entières tenues à part, jamais des paraphrases, et battre le prompt à coût égal, en publiant le résultat sinon (fiche 7 ; explication du 2 octobre, §3 ; cours, volet 7, F·29).

### Insertion n°85, après la ligne 1273 de la v3.5

> Ancre : « Can you tell whether a model is being honest from its representations, without judging whether its claims are true? » Le cœur de la réponse est de démêler trois cibles que la plupart des sondes confondent : ce qui est vrai dans le monde, ce que le modèle croit, et ce que l’utilisateur croit. On co

> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; élicitation non supervisée → volet 2, §E (fin du cas d'application K52) ; détecteurs fine-tunés → volet 7, F·29 ; organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») *(v3.6)*

### Insertion n°87, après la ligne 1277 de la v3.5

> Ancre : « Does a model’s character causally affect its safety? Design the study. » On prend une suite de modèles à capacités égales mais à personas contrôlées (par prompting, données synthétiques, ou vecteurs de traits). On les passe à une batterie de situations OOD critiques pour la sûreté, dont la propens

> ⚠ *(v3.6)* Comme instrument de mesure, un vecteur de trait ne donne qu'une corrélation : le lien entre le déplacement le long du vecteur et l'expression du trait est corrélationnel, le trait doit être nommé d'avance et la direction est une moyenne grossière (fiche 8). Parade : pour le levier, le test à dégradation appariée contre plusieurs témoins ; pour l'extraction supervisée, aucune parade connue, on le dit (cours, volet M, M4 ; fiche 8).

### Insertion n°89, après la ligne 1277 de la v3.5

> Ancre : « Does a model’s character causally affect its safety? Design the study. » On prend une suite de modèles à capacités égales mais à personas contrôlées (par prompting, données synthétiques, ou vecteurs de traits). On les passe à une batterie de situations OOD critiques pour la sûreté, dont la propens

> ⚠ **Limites et parades** : pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») *(v3.6)*

### Insertion n°91, après la ligne 1283 de la v3.5

> Ancre : un auto-rapport entraîné, un auto-rapport spontané — et l’on cherche où l’auto-rapport bat la sonde. Raccord : les activation oracles et les natural language autoencoders (Volet 4). Ta passerelle : tes concept vectors sont ce que l’oracle devrait savoir lire — donc ta question (lire implique-t-il co

> **⚠ Limites et parades — Auto-rapport et introspection** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Rapport n'est pas croyance : Anthropic s'est rétracté d'avoir déduit ce que Claude croyait de ce que Claude disait croire. *(source : fiche 3 ; fiches, partie B, piège 2)*
>   **Parade :** Une lecture indépendante du rapport — le réétiquetage hors contexte des sorties prises une à une —, en disant ce qu'elle ne sépare pas : la prémisse fausse donnée par le dispositif. *(source : fiche 3)*
> - **Limite :** L'introspection est rare et peu fiable : environ 20 % de détection pour Opus 4.1, et « zéro faux positif » ne vaut que pour 100 essais témoins. *(source : fiche 11)*
>   **Parade :** Une vérité-terrain par injection de concept. *(source : fiche 11)*
> - **Limite :** Un modèle entraîné à rapporter peut apprendre à rapporter ce qu'on attend ; rapport ou reconstruction plausible reste ouvert pour les adaptateurs d'introspection. *(source : fiche 11 ; cours, volet 7, F·28)*
>   **Parade :** Modifier l'état interne, contre une direction aléatoire à dégradation appariée, et voir si le rapport suit la sonde ou le prompt. *(source : fiche 11 ; cours, volet 7, F·28)*
> - **Limite :** Les détails rapportés peuvent être embellis ou confabulés, et les conditions sont loin du déploiement. *(source : fiche 11)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** Les réponses aux questions de suivi dépendent de leur formulation. *(source : fiche 3)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** CHIVE ne trouve aucun indice d'accès privilégié d'un modèle à son propre comportement. *(source : fiche 4)*
>   **Parade :** Juger un auto-rapport à ce qu'il prédit des actions suivantes. *(source : fiche 6)*

### Insertion n°93, après la ligne 1283 de la v3.5

> Ancre : un auto-rapport entraîné, un auto-rapport spontané — et l’on cherche où l’auto-rapport bat la sonde. Raccord : les activation oracles et les natural language autoencoders (Volet 4). Ta passerelle : tes concept vectors sont ce que l’oracle devrait savoir lire — donc ta question (lire implique-t-il co

> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; oracles d'activation → volet 10, fiche LatentQA ; autoencodeurs en langage naturel → volet 4, La vague récente sur la cognition du modèle *(v3.6)*

### Insertion n°95, après la ligne 1289 de la v3.5

> Ancre : « How would you build a model organism to study X ? » (où X est presque n’importe quoi : c’est leur grammaire). On suit la recette du Volet 2 : phénomène à proxy implantable, implantation (SDF / finetuning / backdoor), vérification de la profondeur (croyance réelle ou jeu de rôle ?), préservation du

> ⚠ **Limites et parades** : organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; cas connu → volet M, M5 (fin de section) *(v3.6)*

### Insertion n°97, après la ligne 1293 de la v3.5

> Ancre : « How would you evaluate that our monitoring stack catches a sabotaging model ? » Cadre red/blue à budget d’audit fixé, trusted vs untrusted, collusion, métrique sur la frontière safety/usefulness, angles morts systématiques, extrapolation d’événements rares (Volet 2, famille G ; Volet 4, AI Control

> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») *(v3.6)*

### Insertion n°99, après la ligne 1297 de la v3.5

> Ancre : « You’re handed a model with a hidden behavior — what’s your investigation protocol ? » On inventorie d’abord les affordances (a-t-on les poids ? les données ? les SAEs ?). Pipeline : élicitation large → hypothèses → instrumentation interne ciblée → confirmation causale. On se mesure sur AuditBench,

> ⚠ **Limites et parades** : organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; dictionnaires et SAE → volet 4, Towards puis Scaling Monosemanticity ; graphes d'attribution → volet 4, Circuit Tracing *(v3.6)*

### Insertion n°101, après la ligne 1301 de la v3.5

> Ancre : « Design the experiment that tells us whether we can monitor models via their chain-of-thought. » Faithfulness = dépendance causale entre la chaîne et la réponse (corruption, paraphrase, hints) ; variation par tâche et par pression d’optimisation ; régime adversarial ; monitoring en couches. Passere

> ⚠ **Limites et parades** : chaîne de pensée comme moniteur → volet 11, réponse 43 *(v3.6)*

### Insertion n°103, après la ligne 1305 de la v3.5

> Ancre : « Which alignment-research tasks would you delegate to an agent, and how would you validate ? » On décompose en sous-tâches à vérité vérifiable, on valide par re-dérivation humaine échantillonnée, on intègre la détection du sandbagging des chercheurs automatisés, et l’on garde une baseline humaine à

> ⚠ **Limites et parades** : évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; généralisation faible-vers-fort → volet 2, §F (après « En pratique — l'automatisation ») *(v3.6)*

### Insertion n°105, après la ligne 1309 de la v3.5

> Ancre : « Our supervision signal has exploitable systematic errors — what’s your testbed ? » On injecte des erreurs systématiques connues dans le signal, on s’assure que le modèle les comprend, on entraîne contre ce signal avec et sans technique d’oversight, et l’on évalue contre le vrai signal (Volet 2, fa

> ⚠ **Limites et parades** : généralisation faible-vers-fort → volet 2, §F (après « En pratique — l'automatisation ») ; débat et supervision évolutive → volet 2, §E (après « En pratique — Debate ») *(v3.6)*

### Insertion n°107, après la ligne 1336 de la v3.5

> Ancre : 8. *AI Control* Greenblatt 2023 (F·10) — le cadre.

> ⚠ *(v3.6)* Au point 7, « en boîte noire » veut dire que le détecteur lit le transcript, pas les activations — le mot vient de la base, pas du billet : c'est le modèle lui-même, fine-tuné par LoRA à répondre à une question d'auto-rapport ; ce n'est pas une sonde, et ses chiffres ne se transfèrent pas aux sondes (fiche 7 ; fiches, partie B ; contre-lecture des fiches). Parade : pour une sonde, le test est causal, sur des types de mensonge tenus à part, à dégradation appariée (fiche 7).
