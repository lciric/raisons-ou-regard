# Insertions appliquées — volet6 — FR

### Insertion n°1, après la ligne 1418 de la v3.5

> Ancre : latente) — laquelle la loi doit utiliser est une question ouverte, à poser comme telle [R·P1].

> **⚠ Limites et parades — Juges LLM** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Un juge a des erreurs systématiques : sous cadrage social, la note du modèle-juge se déplace vers une destination. *(source : cours, volet 6, §2)*
>   **Parade :** Un juge scellé (prompt, modèle et température gelés), un audit humain d'environ 200 items stratifiés, l'accord rapporté. *(source : programme, partie 3)*
> - **Limite :** Une fenêtre tronquée fait mal lire : à travers elle, un verdict négatif adouci se lisait comme une position tenue. *(source : README du dépôt)*
>   **Parade :** Juger la réponse entière, et garder le texte complet. *(source : README du dépôt ; cours, volet 6, §6)*
> - **Limite :** Accord inter-juges modéré (κ de 0,56 à 0,66), aucun sous-ensemble noté par des humains, et le juge ne voit pas le texte évalué. *(source : README du dépôt)*
>   **Parade :** Un audit humain stratifié, qui borne l'erreur du juge. *(source : programme, partie 3)*
> - **Limite :** Un juge qui lit le raisonnement se laisse persuader : le moniteur fondé sur la chaîne de pensée aurait signalé environ 1 % des actions, contre environ 50 % sans elle. *(source : fiche 3 ; passation, §5.1)*
>   **Parade :** Juger les actions, leurs sorties et les messages, pas le texte qui précède l'action ; un filtre à haut rappel puis un arbitre ; un jeu de calibration à vérité connue et un test de persuasion. *(source : passation, §5.1)*
> - **Limite :** Un juge qui connaît le bras ou le cadrage note le nom du bras. *(source : cours, volet M, M4)*
>   **Parade :** La notation à l'aveugle : le juge ne voit ni le bras ni l'indice d'évaluation. *(source : cours, volet M, M4 ; passation, §5.1)*
> - **Limite :** Un juge d'entraînement se fait exploiter. *(source : programme, partie 8)*
>   **Parade :** Un juge d'entraînement distinct du juge scellé d'évaluation ; surveiller la longueur et les motifs de flatterie. *(source : programme, partie 8)*
> - **Limite :** Des étiquettes de juge non vérifiées à la main : environ 25 % des étiquettes révisées chez Hopkins et Khullar ; celles de CHIVE passent par un classifieur non validé contre des humains. *(source : fiche 7 ; cours, volet 7, F·30)*
>   **Parade :** Dire « révisées », pas « inversées », et borner l'erreur par un audit humain. *(source : fiche 7 ; programme, partie 3)*
> - **Limite :** Un modèle qui s'audite presque lui-même : pour Fable 5, l'investigateur est Mythos Preview. *(source : fiche 2 ; fiches, partie B, piège 6)*
>   **Parade :** aucune connue ; on le dit.

### Insertion n°3, après la ligne 1418 de la v3.5

> Ancre : latente) — laquelle la loi doit utiliser est une question ouverte, à poser comme telle [R·P1].

> ⚠ *(v3.6)* Que la destination « se lise dans les activations » dit qu'elle y est lisible, pas que le modèle s'en sert : la direction que lit ta sonde fait moins de 1 % du travail causal (cours, volet 6, §2) ; et le passage ne dit pas si ce R² vient d'items exclus de l'ajustement, alors que les métriques de sonde de ton dépôt étaient d'ajustement, et que son ρ peut l'être aussi (README du dépôt). Parade : scorer des items exclus de l'ajustement et extraire sur un jeu disjoint (README du dépôt) ; pour conclure que le modèle s'en sert, le test causal — faire plus que des directions aléatoires de même norme (le nul de spécificité), puis plus que des témoins à dégradation appariée (le dommage) (passation, §5.2 ; cours, volet M, M4).

### Insertion n°5, après la ligne 1429 de la v3.5

> Ancre : tout P2 sous Qwen2.5-7B, et le bloc WHAT DOES NOT EXIST de la base dit « one 7B model » : deux erreurs de la base, à corriger.

> ⚠ *(v3.6)* « À doses appariées » n'est pas « à dégradation appariée » : à dose égale, une direction concurrente et la tienne n'abîment pas forcément autant le modèle, si bien que ces deux rapports de sélectivité ne sont pas lus à dommage égal ; et le patch de l'état complet aux mêmes sites est un plafond, pas une explication (cours, volet M, M4 ; programme, parties 7 et 8). Parade : refaire la comparaison des deux directions nommées à dégradation appariée, en courbes de l'effet contre la dégradation, et ne comparer qu'aux réglages qu'un témoin peut apparier, en le disant (programme, partie 7).

### Insertion n°7, après la ligne 1437 de la v3.5

> Ancre : que les sous-espaces sont emboîtés. C'est la première anomalie de la thèse, pas son appui.

> ⚠ *(v3.6)* Ce nul de rang un est dit avec sa puissance, pas avec son cas connu : sans un concept qui cède au rang un dans le même appareil, au même réglage, il ne départage pas « concept réparti » et « appareil aveugle à ce réglage » (fiche 7 ; cours, volet M, M5) ; les autres méthodes de rang un sont rapportées sans chiffres, leurs sorties brutes n'ayant pas été conservées, et l'échec du blocage (clamping) de traits du SAE ne sépare pas « traits absents du dictionnaire » de « dictionnaire qui perd trop » (README du dépôt). Parade : un cas connu au même réglage — un vecteur de pays, qui s'échange dans l'article sur l'espace de travail — et un balayage de rang dans une même expérience, sur des sous-espaces emboîtés (cours, volet 2, §C, K47 ; cours, volet 6, §6) ; pour le SAE, aucune parade connue, on le dit ; et l'on dit une borne, jamais une absence (README du dépôt ; cours, volet M, M5).

### Insertion n°9, après la ligne 1444 de la v3.5

> Ancre : times more from widening the judged window » est **morte** : on ne peut pas élargir une fenêtre sur un texte disparu [R·E2b].

> ⚠ *(v3.6)* Une puissance élevée ne remplace pas un cas connu : ce nul sur générations fraîches se dit comme une borne, avec son budget et sa puissance, pas comme l'absence de tout effet (cours, volet M, M5). Parade : valider le même protocole — générations fraîches à graines appariées, réponse entière jugée et gardée en texte complet — sur un cas connu, au même réglage et au même seuil, avant de lire son silence (cours, volet M, M5 ; fiche 7 ; cours, volet 6, §6 ; README du dépôt).

### Insertion n°11, après la ligne 1449 de la v3.5

> Ancre : McNemar p = 0,0156 » — un contrôle de complétude ressuscité à tort comme résultat [R·rétractation].

> ⚠ **Limites et parades** : ablation et projection → volet 2, §D (après « La méthode ») ; patching → volet 10, fiche Patchscopes ; contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme ») ; dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; dictionnaires et SAE → volet 4, Towards puis Scaling Monosemanticity ; cas connu → volet M, M5 (fin de section) *(v3.6)*

### Insertion n°13, après la ligne 1456 de la v3.5

> Ancre : covariance** (pièce M4 du dossier : 0,161 pour l'aléatoire, contre 0,088 pour la direction de la sonde). Quand tu dis « contrôle », dis lequel, et lequel a fondé quel chiffre.

> ⚠ *(v3.6)* Aucun de ces trois contrôles n'écarte le dommage : l'aléatoire, apparié en norme ou en covariance, n'est que le nul de spécificité, et les directions concurrentes sont comparées à doses appariées, pas à dégradation égale (cours, volet M, M4 ; programme, partie 7 ; cours, volet 6, §2). Parade : un quatrième contrôle, à dégradation appariée — plusieurs familles de témoins au même rang, dont au moins vingt sous-espaces aléatoires, en courbes de l'effet contre la dégradation, rapportées contre leur médiane et leur 95e centile (programme, parties 3 et 7).

### Insertion n°15, après la ligne 1456 de la v3.5

> Ancre : covariance** (pièce M4 du dossier : 0,161 pour l'aléatoire, contre 0,088 pour la direction de la sonde). Quand tu dis « contrôle », dis lequel, et lequel a fondé quel chiffre.

> ⚠ **Limites et parades** : contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme ») ; dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») *(v3.6)*

### Insertion n°17, après la ligne 1483 de la v3.5

> Ancre : *Removing Sandbagging* (Ryd — 91/85/94 % d'élicitation sous supervision faible) [F·26].

> ⚠ *(v3.6)* Le 91/85/94 % de Ryd ne tient, selon la limite écrite des auteurs, que si l'entraînement est indistinguable du déploiement : un modèle qui les distingue échappe (cours, volet 7, F·26). Parade : aucune connue ; on le dit.

### Insertion n°19, après la ligne 1487 de la v3.5

> Ancre : distribution, 0,70-0,75 hors) [F·29] ; *CHIVE* (Karvonen — aucun gain des outils d'interprétabilité) [F·30].

> ⚠ *(v3.6)* Le nul de CHIVE est mesuré en lecture seule, avec des étiquettes passées par un classifieur LLM non validé contre des humains (cours, volet 7, F·30) ; et pour les adaptateurs d'introspection, rapport ou reconstruction plausible reste ouvert (cours, volet 7, F·28). Parade : pour un outil de lecture, battre la boîte noire sur des éditions qui dissocient la surface de la variable interne, et borner l'erreur des étiquettes par un audit humain (fiche 4 ; programme, partie 3) ; pour un auto-rapport, modifier l'état interne contre une direction aléatoire à dégradation appariée, et voir si le rapport suit (fiche 11 ; cours, volet 7, F·28).

### Insertion n°21, après la ligne 1492 de la v3.5

> Ancre : ré-entraînement) [F·36] ; *The Hot Mess of AI* (Hägele) [F·37].

> ⚠ *(v3.6)* Deux de ces résultats ont une portée étroite : les vecteurs de persona supposent le trait nommé d'avance, et le lien entre déplacement et trait n'y est que corrélationnel (fiche 8) ; le masquage sélectif des gradients n'est montré que sur de petits modèles (cours, volet 2, §I, JB10). Parade : pour la causalité d'un vecteur, le test à dégradation appariée (cours, volet M, M4) ; pour l'extraction supervisée et pour l'échelle, aucune parade connue ; on le dit.

### Insertion n°23, après la ligne 1497 de la v3.5

> Ancre : (Zhang) [F·42].

> ⚠ *(v3.6)* Le 96 % vient d'un stress-test délibéré, où l'action nuisible est la seule voie, et les auteurs ne connaissent aucun cas en déploiement réel ; le 68 → 5 % de Model Spec Midtraining est mesuré sur la même évaluation (cours, volet 7, F·38) ; et un modèle peut remarquer le test et se retenir (fiche 13). Parade : deux versions d'un environnement, tirées au hasard, qui ne diffèrent que par des indices de réalisme notés par un discriminateur, avec un organisme dressé à se cacher comme cas connu (cours, volet 2, §B, K63) ; contre un pot de miel que le modèle lit comme factice, aucune parade connue ; on le dit (fiche 3).

### Insertion n°25, après la ligne 1497 de la v3.5

> Ancre : (Zhang) [F·42].

> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») ; évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; auto-rapport et introspection → volet 5, partie II, A, sujet 13 ; détecteurs fine-tunés → volet 7, F·29 ; oracles d'activation → volet 10, fiche LatentQA ; autoencodeurs en langage naturel → volet 4, La vague récente sur la cognition du modèle ; dictionnaires et SAE → volet 4, Towards puis Scaling Monosemanticity ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; désapprentissage et ré-élicitation → volet 2, §I (après « En pratique — l'unlearning mis à l'épreuve ») ; généralisation faible-vers-fort → volet 2, §F (après « En pratique — l'automatisation ») ; juges LLM → volet 6, §2 (après « La loi de déplacement ») *(v3.6)*

### Insertion n°27, après la ligne 1510 de la v3.5

> Ancre : combine » : « I haven't seen it measured » (volet M, M8, et la règle « first to » de la base).

> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; J-lens et espace de travail → volet 2, C bis (après « Le test, tel qu'il se dit ») ; ablation et projection → volet 2, §D (après « La méthode ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme ») ; dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») ; patching → volet 10, fiche Patchscopes *(v3.6)*

### Insertion n°29, après la ligne 1519 de la v3.5

> Ancre : rien du travail causal.

> ⚠ *(v3.6)* Le jacobien ne dispense pas du test causal : le lens ne capture l'espace de travail que « only approximately and incompletely », pour des concepts d'un seul token, la présence n'y est pas la cause — le langage y est présent sur quatre tâches, causal sur deux —, et il n'a été montré que sur Claude (fiche 1). Parade : la porte du lens — reproduire d'abord sur Llama l'échange d'un concept d'un seul token, sinon un tuned lens déclaré comme approximation, et la thèse n'est pas testée au sens de l'article (programme, parties 3 et 8) ; un rapport non vérifié trouve d'ailleurs des échanges bien plus faibles sur des modèles ouverts (rapport d'antériorité 5 du 2 octobre — rapport, lu par résumé).

### Insertion n°31, après la ligne 1575 de la v3.5

> Ancre : sont à désapprendre : « six methods », « two points », « deference subspace », « widening the judged window ».

> ⚠ *(v3.6)* Ce « moins de 1 % » vient d'un seul modèle, Llama 3.1 8B Instruct, et de la seule complaisance d'opinion, en un tour (README du dépôt) : il relativise les sondes et le pilotage (volet 2, §C) sur ce cas, pas en général. Parade : la même partition sur d'autres concepts, puis sur un second modèle (cours, volet 6, §6).

### Insertion n°33, après la ligne 1589 de la v3.5

> Ancre : fait moins d'un pour cent du travail causal — lire n'est pas utiliser, déjà en distribution.

> ⚠ *(v3.6)* Les étiquettes de Hopkins et Khullar passent par un juge GPT-5, et environ 25 % ont été révisées à la passe de nettoyage (fiche 7). Parade : dire « révisées », pas « inversées », et garder pour mesure l'écart entre l'AUROC en distribution et l'AUROC sur des types tenus à part (fiche 7) ; dans ton propre dispositif, borner l'erreur du juge par un audit humain stratifié (programme, partie 3).

### Insertion n°35, après la ligne 1603 de la v3.5

> Ancre : consigne ; elle est inutile hors des organismes, **et on le sait avant de la déployer**.

> ⚠ *(v3.6)* Le silence de la sonde sur la famille 2, celle du fine-tuning léger, ne désigne « la trace de la consigne » que si cette famille porte bien l'intention : l'implant par fine-tuning peut rater (cours, volet 2, §E, K52), et l'organisme conditionné à l'évaluation de la fiche 10 ne suit sa règle qu'en partie (fiche 10). Parade : vérifier chaque copie par son comportement (cours, volet 2, §A, K71), l'étiqueter par des contrôles programmés et un juge scellé, jamais par la sonde (passation, §5.1 et §5.2), et ne lire un silence qu'une fois la sensibilité de la sonde mesurée sur un organisme où l'on a mis l'intention soi-même : il devient alors une borne (passation, §5.2).

### Insertion n°37, après la ligne 1616 de la v3.5

> Ancre : devraient se trouver.

> ⚠ *(v3.6)* Un effet porté par le seul reste peut aussi venir de ce que le lens manque — il ne capture l'espace de travail que « only approximately and incompletely », et pour des concepts d'un seul token (fiche 1) —, et le lens dépend des poids, or la famille 2 est fine-tunée, contrairement à la famille 1 (cours, volet 2, C bis ; cours, volet 6, §8). Parade : recalculer le lens sur chaque organisme fine-tuné, et lire le concept sur un jeu de tokens ou par l'extension multi-token de l'annexe, en disant laquelle (cours, volet 2, C bis ; programme, partie 3).

### Insertion n°39, après la ligne 1624 de la v3.5

> Ancre : aware-but-honest control.* »

> ### ★ Encadré du 2 octobre 2026 — Renvoi : entraîner des sondes de désalignement, et les juger hors distribution
>
> L'encadré du 2 octobre reprend ce paragraphe du côté de la pratique : pourquoi un organisme modèle, et pourquoi son succès borne l'instrument sans prouver le cas naturel (volet 2, fin de la présentation de la section A) ; comment entraîner une sonde sans toucher aux poids, et la juger hors distribution, sur des familles entières tenues à part et avec une sonde neuve après tout entraînement (volet 2, fin de la présentation de la section C) ; l'angle mort du J-lens et ses cas connus (volet 2, C bis). Les deux familles d'organismes et le témoin conscient mais honnête de ce paragraphe y sont donnés comme parade partielle à la saillance d'un comportement implanté.

### Insertion n°41, après la ligne 1624 de la v3.5

> Ancre : aware-but-honest control.* »

> ⚠ *(v3.6)* « Une sonde par couche » oblige à choisir une couche, et « s'allume » suppose un seuil : choisis sur les données du test, ils le contaminent (cours, volet 2, C bis ; README du dépôt). Parade : choisir la couche par l'AUROC sur un jeu de validation, jamais sur celui du test, avec des jeux d'indices disjoints, et fixer le seuil d'avance, le même que celui où le cas connu a été validé (programme, partie 3 ; cours, volet M, M5 ; fiche 7).

### Insertion n°43, après la ligne 1624 de la v3.5

> Ancre : aware-but-honest control.* »

> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; détecteurs fine-tunés → volet 7, F·29 ; organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; cas connu → volet M, M5 (fin de section) ; J-lens et espace de travail → volet 2, C bis (après « Le test, tel qu'il se dit ») ; jeu tenu à part → volet M, M4 (après « Le jeu tenu à part ») ; patching → volet 10, fiche Patchscopes *(v3.6)*
