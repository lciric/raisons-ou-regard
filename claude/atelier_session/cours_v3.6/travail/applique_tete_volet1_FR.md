# Insertions appliquées — tete_volet1 — FR

### Insertion n°1, après la ligne 1 de la v3.5

> Ancre : # COURS D'ALIGNEMENT — VERSION FUSIONNÉE v3.5 — 27 septembre 2026

> **v3.6 — 2 octobre 2026 : ce qui s'ajoute** *(v3.6)*
>
> Rien du texte de la v3.5 n'est retiré ni modifié : on ajoute, et chaque ajout porte la mention *(v3.6)*. Deux ajouts.
>
> - ★ **L'encadré du 2 octobre 2026 sur les sondes de désalignement** — pourquoi il faut un organisme modèle, J-lens compris ; comment entraîner les sondes ; le hors-distribution — est au volet 2, en trois morceaux : la partie 1 à la fin de la présentation de la section A (après « En pratique — Auditing Hidden Objectives », avant le cas d'application K71) ; les parties 2 et 3 à la fin de celle de la section C (après « En pratique — Contrastive Activation Addition (CAA) », avant le cas d'application K47) ; le J-lens au C bis (après « Le test, tel qu'il se dit », avant le cas d'application K72). Des renvois y mènent depuis le volet M, M5, et le volet 6, §8.
> - ⚠ **Les limites de chaque instrument, et comment les contourner** : un encadré « Limites et parades » par instrument, à sa maison (index ci-dessous) ; ailleurs, un renvoi d'une ligne vers cet encadré, et un avertissement ponctuel là où un passage rapporte un résultat sans dire la limite de l'instrument qui l'a produit. Quand aucune parade n'est connue, l'encadré le dit. La règle, partout : une direction aléatoire de même norme n'est que le nul de spécificité ; le dommage ne s'écarte qu'à dégradation appariée ; un nul d'instrument ne compte qu'avec son cas connu (cours, volet M, M4 et M5).
>
> **Où sont les encadrés « Limites et parades »**, volet par volet :
>
> ⚠ **Limites et parades** : contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme ») ; dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») ; jeu tenu à part → volet M, M4 (après « Le jeu tenu à part ») ; cas connu → volet M, M5 (fin de section) *(v3.6)*
>
> ⚠ **Limites et parades** : organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; J-lens et espace de travail → volet 2, C bis (après « Le test, tel qu'il se dit ») ; ablation et projection → volet 2, §D (après « La méthode ») ; crosscoders et comparaison de modèles → volet 2, §D (fin du cas d'application K64) *(v3.6)*
>
> ⚠ **Limites et parades** : débat et supervision évolutive → volet 2, §E (après « En pratique — Debate ») ; élicitation non supervisée → volet 2, §E (fin du cas d'application K52) ; généralisation faible-vers-fort → volet 2, §F (après « En pratique — l'automatisation ») ; moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») ; classifieurs de sûreté → volet 2, §H (fin du cas d'application G1) ; désapprentissage et ré-élicitation → volet 2, §I (après « En pratique — l'unlearning mis à l'épreuve ») *(v3.6)*
>
> ⚠ **Limites et parades** : dictionnaires et SAE → volet 4, Towards puis Scaling Monosemanticity ; graphes d'attribution → volet 4, Circuit Tracing ; autoencodeurs en langage naturel → volet 4, La vague récente sur la cognition du modèle ; auto-rapport et introspection → volet 5, partie II, A, sujet 13 ; juges LLM → volet 6, §2 (après « La loi de déplacement ») ; détecteurs fine-tunés → volet 7, F·29 ; patching → volet 10, fiche Patchscopes ; oracles d'activation → volet 10, fiche LatentQA ; chaîne de pensée comme moniteur → volet 11, réponse 43 *(v3.6)*

### Insertion n°3, après la ligne 3 de la v3.5

> Ancre : > **Un seul document : le volet M et onze volets.** Le cours de juin 2026 (volets 1 à 5), les volets 6 à 11 de septembre, et, nouveau en v3.5, le **volet M — la méthode** : comment construire à voix haute l'expérience qui tranche une question ouverte (le pari, les contrôles et ce qu'ils écartent, le

> ⚠ *(v3.6)* Les sondes à 0,93-0,997 : le cours ne dit pas sur quel jeu ces scores sont mesurés, et un score de sonde en distribution ne dit rien de la généralisation — le chiffre qui compte est l'écart avec le score sur des types tenus à part (fiches, partie B, piège 1 ; fiche 7). Parade : ne les dire qu'avec leur jeu de mesure, tenir à part des familles entières, jamais des paraphrases (explication du 2 octobre, partie 3 ; fiche 7), et ne jamais les mettre dans la même phrase que les interventions sur Llama-3.1-8B (cours, volet 6, §2).

### Insertion n°5, après la ligne 74 de la v3.5

> Ancre : Le quatrième, le plus inquiétant, est l’alignement trompeur (deceptive alignment), aussi appelé alignment faking. Imagine un modèle qui a acquis un but interne désaligné mais qui est assez capable pour comprendre une chose : paraître aligné pendant l’entraînement et les évaluations est instrumentale

> ⚠ *(v3.6)* Ce que le travail Alignment Faking mesure, c'est un écart de conformité entre le cas « entraîné » et le cas « non entraîné », dont le scratchpad donne le motif : l'indice est construit, et l'on ne sait pas trancher entre jeu de rôle et vraie préservation de buts (fiche 14). Parade : distinguer la conformité (14 %) de la conformité avec raisonnement explicite de faux alignement (12 %) (fiches, partie B, piège 7), et retirer l'indice lisible pour chercher quand même la préservation de buts (fiche 14) ; une réplication sur un modèle récent mesure peut-être la mémorisation du scénario, ses transcripts ayant été réinclus dans l'entraînement — contre cela, aucune parade connue ; on le dit (fiches, partie C ; fiche 14).

### Insertion n°7, après la ligne 74 de la v3.5

> Ancre : Le quatrième, le plus inquiétant, est l’alignement trompeur (deceptive alignment), aussi appelé alignment faking. Imagine un modèle qui a acquis un but interne désaligné mais qui est assez capable pour comprendre une chose : paraître aligné pendant l’entraînement et les évaluations est instrumentale

> ⚠ **Limites et parades** : évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; chaîne de pensée comme moniteur → volet 11, réponse 43 *(v3.6)*

### Insertion n°9, après la ligne 102 de la v3.5

> Ancre : étape de preuve, lancer un test unitaire — et pour ces tâches le problème est léger. Mais il mord le plus fort là où vit précisément l’alignement : sur les jugements flous et chargés de valeurs (« ce comportement est-il bon ? », « ce plan est-il sage ? ») qui n’ont aucun vérificateur bon marché. C’e

> ⚠ *(v3.6)* « On vérifie le transfert au réel » est le maillon que rien ne garantit : un succès sur un organisme construit borne l'instrument sans prouver le cas naturel, car une intention implantée est peut-être plus saillante qu'une naturelle — sur les sleeper agents, la meilleure de 1 000 directions aléatoires atteint déjà 95,3 % (passation, §5.2 ; fiche 15). Parade partielle : planter le même comportement par plusieurs recettes et lire la sonde sur une recette tenue à part, avec un comportement inoffensif planté de la même façon comme contrôle (cours, volet 2, §A, K71), ou deux familles d'organismes avec un témoin conscient mais honnête (cours, volet 6, §8) ; contre l'écart entre implanté et naturel lui-même, aucune parade connue ; on le dit (fiche 15 ; encadré du 2 octobre, partie 1).

### Insertion n°11, après la ligne 102 de la v3.5

> Ancre : étape de preuve, lancer un test unitaire — et pour ces tâches le problème est léger. Mais il mord le plus fort là où vit précisément l’alignement : sur les jugements flous et chargés de valeurs (« ce comportement est-il bon ? », « ce plan est-il sage ? ») qui n’ont aucun vérificateur bon marché. C’e

> ⚠ **Limites et parades** : organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; cas connu → volet M, M5 (fin de section) ; contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme ») ; dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») ; jeu tenu à part → volet M, M4 (après « Le jeu tenu à part ») *(v3.6)*

### Insertion n°13, après la ligne 126 de la v3.5

> Ancre : décomposition) qui essaie de fabriquer un signal fiable à partir de juges faillibles, et l’interprétabilité qui essaie de lire l’état interne pour court-circuiter le besoin de confiance. On reconnaît enfin qu’un chercheur sérieux pourrait désigner un autre problème comme le plus dur — par exemple la

> ⚠ **Limites et parades** : débat et supervision évolutive → volet 2, §E (après « En pratique — Debate ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») *(v3.6)*

### Insertion n°15, après la ligne 136 de la v3.5

> Ancre : test et déploiement. C’est ici qu’intervient la conscience d’être évalué (evaluation awareness) : si l’on peut détecter, voire neutraliser, la représentation interne « ceci est un test », et que le comportement désaligné augmente quand on la neutralise, c’est un signal fort que les évaluations « pro

> ⚠ *(v3.6)* Que le désalignement monte quand on neutralise « ceci est un test » n'est qu'un appui faible tant que le dommage n'est pas écarté : chaque direction pilotée dégrade la sortie, et des vecteurs de contrôle arbitraires font aussi monter le désalignement, plus faiblement (fiche 2 ; fiches, partie C). Parade : une direction aléatoire de même norme n'écarte que le nul de spécificité ; le dommage ne s'écarte qu'à dégradation appariée, par une courbe dose-réponse contre plusieurs témoins, avec un cas connu au même réglage (cours, volet M, M4 ; cours, volet 2, §C, K47).

### Insertion n°17, après la ligne 136 de la v3.5

> Ancre : test et déploiement. C’est ici qu’intervient la conscience d’être évalué (evaluation awareness) : si l’on peut détecter, voire neutraliser, la représentation interne « ceci est un test », et que le comportement désaligné augmente quand on la neutralise, c’est un signal fort que les évaluations « pro

> ⚠ *(v3.6)* Si les détecteurs se taisent, cela ne prouve pas que le modèle ne feint pas : une sonde muette ne départage pas « pas d'intention » et « sonde aveugle » (passation, §5.2 ; fiches, partie B, piège 3). Parade : mesurer sensibilité et fausses alarmes sur un organisme où l'on a installé l'intention soi-même, et ne tirer du silence ailleurs qu'une borne (passation, §5.2) — c'est la partie 1 de l'encadré du 2 octobre, au volet 2 (fin de la présentation de la section A), dont la suite, entraîner les sondes et le hors-distribution, est à la fin de celle de la section C.

### Insertion n°19, après la ligne 136 de la v3.5

> Ancre : test et déploiement. C’est ici qu’intervient la conscience d’être évalué (evaluation awareness) : si l’on peut détecter, voire neutraliser, la représentation interne « ceci est un test », et que le comportement désaligné augmente quand on la neutralise, c’est un signal fort que les évaluations « pro

> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; cas connu → volet M, M5 (fin de section) ; évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») *(v3.6)*

### Insertion n°21, après la ligne 140 de la v3.5

> Ancre : La chain-of-thought (le raisonnement que le modèle écrit avant de répondre) semble un cadeau pour la surveillance : on lirait ses pensées. Le problème, qu’il faut nommer, est la fidélité (faithfulness) : rien ne garantit que ce raisonnement écrit reflète le calcul interne réel — un modèle peut produ

> ⚠ *(v3.6)* Le raisonnement écrit peut aussi persuader le moniteur : un moniteur fondé sur la chaîne de pensée n'aurait signalé qu'environ 1 % des actions de Mythos 5, contre environ 50 % sans elle — un seul moniteur, un incident (fiche 3). Parade : juger ce que le modèle fait, pas ce qu'il en dit (passation, §5.1) ; encadré complet au volet 11, réponse 43.

### Insertion n°23, après la ligne 140 de la v3.5

> Ancre : La chain-of-thought (le raisonnement que le modèle écrit avant de répondre) semble un cadeau pour la surveillance : on lirait ses pensées. Le problème, qu’il faut nommer, est la fidélité (faithfulness) : rien ne garantit que ce raisonnement écrit reflète le calcul interne réel — un modèle peut produ

> ⚠ *(v3.6)* « La seconde prend le relais » suppose la sonde fiable là où la chaîne ne l'est pas : le silence d'une sonde en production n'est pas celui du modèle (cours, volet 3, §3, K70), et au seuil d'un moniteur, des sondes rappellent 43 % à 1 % de faux positifs, contre 55 % pour le meilleur moniteur LLM (cours, volet 7, F·51). Parade : des canaris — des positifs connus glissés dans le trafic —, un score de dérive et un échantillon frais jugé chaque mois (cours, volet 3, §3, K70), et un rappel rapporté à un seuil calibré à 1 % de faux positifs sur des variantes bénignes appariées (cours, volet 7, F·23).

### Insertion n°25, après la ligne 140 de la v3.5

> Ancre : La chain-of-thought (le raisonnement que le modèle écrit avant de répondre) semble un cadeau pour la surveillance : on lirait ses pensées. Le problème, qu’il faut nommer, est la fidélité (faithfulness) : rien ne garantit que ce raisonnement écrit reflète le calcul interne réel — un modèle peut produ

> ⚠ **Limites et parades** : chaîne de pensée comme moniteur → volet 11, réponse 43 ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») *(v3.6)*

### Insertion n°27, après la ligne 150 de la v3.5

> Ancre : La Responsible Scaling Policy (RSP) d’Anthropic est un cadre de gouvernance qui lie le niveau de sûreté exigé au niveau de capacité du modèle. Elle définit des paliers, les AI Safety Levels (ASL), par analogie avec les niveaux de biosécurité des laboratoires : plus un modèle approche de capacités da

> ⚠ *(v3.6)* Un seuil non franchi est une borne, pas une absence : sans budget d'élicitation fixé d'avance et rapporté, « rien trouvé » dit seulement qu'on n'a pas assez cherché (cours, volet M, M7) ; et le Risk Report d'août concède des évaluations non tirées des vrais chemins de risque, sur des modèles probablement conscients d'être évalués (fiche 3). Parade : une élicitation à budget fixé d'avance, rapportée comme une borne (cours, volet M, M7 ; cours, volet 2, §B, K63) ; contre le modèle qui se retient, deux versions d'un environnement, tirées au hasard, qui ne diffèrent que par des indices de réalisme, avec un organisme dressé à se cacher comme cas connu (cours, volet 2, §B, K63).

### Insertion n°29, après la ligne 150 de la v3.5

> Ancre : La Responsible Scaling Policy (RSP) d’Anthropic est un cadre de gouvernance qui lie le niveau de sûreté exigé au niveau de capacité du modèle. Elle définit des paliers, les AI Safety Levels (ASL), par analogie avec les niveaux de biosécurité des laboratoires : plus un modèle approche de capacités da

> ⚠ **Limites et parades** : évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») *(v3.6)*

### Insertion n°31, après la ligne 160 de la v3.5

> Ancre : C’est la question qui sépare un bon technicien d’un chercheur, et elle s’applique directement à tes propres travaux. On attend une chaîne causale explicite, du résultat technique jusqu’à la réduction du risque. Pour mes travaux, elle se dit ainsi : aujourd’hui, on dispose de méthodes qui lisent l’ét

> ⚠ *(v3.6)* La lecture « solide » repose, sur Llama, sur la seule lecture qui y soit mesurée, une corrélation de projection, ρ = 0,684, qui peut n'être qu'un ajustement ; les métriques de sonde, d'ajustement, ne sont pas rapportées (README du dépôt ; cours, volet 6, §2). Parade : scorer des items exclus de l'entraînement de la sonde, et extraire sur un jeu disjoint (README du dépôt) ; les sondes à 0,93-0,997 sont sur Qwen2.5-7B, un autre projet, jamais dans la même phrase que ce résultat (cours, volet 6, §2).

### Insertion n°33, après la ligne 160 de la v3.5

> Ancre : C’est la question qui sépare un bon technicien d’un chercheur, et elle s’applique directement à tes propres travaux. On attend une chaîne causale explicite, du résultat technique jusqu’à la réduction du risque. Pour mes travaux, elle se dit ainsi : aujourd’hui, on dispose de méthodes qui lisent l’ét

> ⚠ *(v3.6)* « Plusieurs méthodes de rang un ont échoué » est un nul sans chiffres ni cas connu : leurs sorties brutes n'ont pas été conservées (README du dépôt), et un nul de pilotage peut venir d'un rang trop bas (fiche 7). Parade : avant de lire un nul, un cas connu au même réglage — un vecteur de pays, qui s'échange dans l'article sur l'espace de travail (cours, volet 2, §C, K47 ; cours, volet M, M5).

### Insertion n°35, après la ligne 160 de la v3.5

> Ancre : C’est la question qui sépare un bon technicien d’un chercheur, et elle s’applique directement à tes propres travaux. On attend une chaîne causale explicite, du résultat technique jusqu’à la réduction du risque. Pour mes travaux, elle se dit ainsi : aujourd’hui, on dispose de méthodes qui lisent l’ét

> ⚠ *(v3.6)* La prédiction du sous-espace n'a pas d'appui causal propre : la baisse du rang trois n'est pas revenue sur des générations fraîches, le sous-espace adoucit les verdicts négatifs sans encoder la déférence, et le contraste entre rangs vient d'expériences séparées, le seul balayage fait dans une même expérience n'étant pas monotone (README du dépôt ; cours, volet 6, §2). Parade : un balayage de rang dans une même expérience, sur des sous-espaces emboîtés, monotonie vérifiée et non supposée, à dégât égal, sur des générations fraîches gardées en texte complet, avec un bras sans pression (cours, volet 6, §6 ; cours, volet M, M4).

### Insertion n°37, après la ligne 160 de la v3.5

> Ancre : C’est la question qui sépare un bon technicien d’un chercheur, et elle s’applique directement à tes propres travaux. On attend une chaîne causale explicite, du résultat technique jusqu’à la réduction du risque. Pour mes travaux, elle se dit ainsi : aujourd’hui, on dispose de méthodes qui lisent l’ét

> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; ablation et projection → volet 2, §D (après « La méthode ») ; cas connu → volet M, M5 (fin de section) *(v3.6)*

### Insertion n°39, après la ligne 166 de la v3.5

> Ancre : couches sont biaisées par la même cause. La conclusion forte : les défenses les plus précieuses sont celles dont les failles sont indépendantes des autres — typiquement, les méthodes white-box (interprétabilité, sondes internes) qui ne passent pas par le comportement observé et peuvent donc rester v

> ⚠ *(v3.6)* Les sondes ne sont pas indépendantes d'office des méthodes comportementales : sur un modèle naturel, leur étiquette vient de la conduite, jugée après coup (explication du 2 octobre, partie 1, point 2) ; elles peuvent lire « je suis surveillé » au lieu de l'intention (cours, volet 6, §8) ; et itérer contre ses détecteurs sélectionne l'évasion (fiche 19). Parade : un organisme où l'intention est installée, qui fournit la vérité de terrain, deux familles d'organismes et un témoin conscient mais honnête (explication du 2 octobre, partie 1, point 2 ; cours, volet 6, §8), et des détecteurs scellés hors de la boucle — s'ils se déclenchent encore quand ceux de la boucle se taisent, l'évasion a été sélectionnée (fiche 19).

### Insertion n°41, après la ligne 166 de la v3.5

> Ancre : couches sont biaisées par la même cause. La conclusion forte : les défenses les plus précieuses sont celles dont les failles sont indépendantes des autres — typiquement, les méthodes white-box (interprétabilité, sondes internes) qui ne passent pas par le comportement observé et peuvent donc rester v

> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; désapprentissage et ré-élicitation → volet 2, §I (après « En pratique — l'unlearning mis à l'épreuve ») *(v3.6)*

### Insertion n°43, après la ligne 172 de la v3.5

> Ancre : On sépare les deux moitiés. Pour le red-teaming, l’objectif est de découvrir comment faire échouer le modèle avant qu’un adversaire réel ne le fasse. On combine des attaques manuelles (des humains cherchant des jailbreaks créatifs) et automatisées (optimiser, par gradient, un suffixe adversarial qui

> ⚠ *(v3.6)* Le résultat d'un jeu red team / blue team ne vaut que pour la red team supposée : un échafaudage d'attaque optimisé fait passer le score de sûreté de 0,87 à 0,41 (cours, volet 7, F·24), et sur Opus 4.6 la moitié de quarante attaques conçues à la main ne sont jamais attrapées par le moniteur (cours, volet 7, F·23). Parade : dire quelle red team le chiffre suppose — au moins une red team optimisée composante par composante —, un seuil calibré à 1 % de faux positifs sur des variantes bénignes appariées, un ensemble de prompts de moniteur spécialisés (cours, volet 7, F·24 et F·23) ; et une red team à budget fixé d'avance, dont le « rien trouvé » n'est qu'une borne (cours, volet M, M7).

### Insertion n°45, après la ligne 172 de la v3.5

> Ancre : On sépare les deux moitiés. Pour le red-teaming, l’objectif est de découvrir comment faire échouer le modèle avant qu’un adversaire réel ne le fasse. On combine des attaques manuelles (des humains cherchant des jailbreaks créatifs) et automatisées (optimiser, par gradient, un suffixe adversarial qui

> ⚠ **Limites et parades** : red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») ; moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») *(v3.6)*

### Insertion n°47, après la ligne 178 de la v3.5

> Ancre : implantée, sur l’interprétabilité qui contourne le comportement observé, et sur l’oversight qui essaie de fabriquer un signal fiable — mais c’est une raison de ne pas confondre « le modèle se comporte bien sur nos tests » avec « le modèle est aligné ».

> ⚠ *(v3.6)* La vérité de terrain implantée n'est pas parfaite : l'organisme conditionné à l'évaluation de la fiche 10 n'annote qu'environ 80 à 86 % du temps en évaluation, encore 34 % en déploiement simplement prompté, et ne distingue pas de façon fiable évaluation et déploiement à partir d'indices subtils (fiche 10). Parade : vérifier chaque copie par son comportement (cours, volet 2, §A, K71), et tenir pour vérité de terrain la règle et ses indices, l'étiquette de chaque entrée se vérifiant encore par la conduite (encadré du 2 octobre, partie 1, point 2 : volet 2, fin de la présentation de la section A).

### Insertion n°49, après la ligne 178 de la v3.5

> Ancre : implantée, sur l’interprétabilité qui contourne le comportement observé, et sur l’oversight qui essaie de fabriquer un signal fiable — mais c’est une raison de ne pas confondre « le modèle se comporte bien sur nos tests » avec « le modèle est aligné ».

> ⚠ **Limites et parades** : organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; cas connu → volet M, M5 (fin de section) *(v3.6)*
