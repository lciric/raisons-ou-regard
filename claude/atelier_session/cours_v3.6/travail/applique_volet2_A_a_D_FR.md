# Insertions appliquées — volet2_A_a_D — FR

### Insertion n°1, après la ligne 432 de la v3.5

> Ancre : La quatrième n’est pas une méthode mais une discipline transversale, la statistique d’évaluation : tout résultat exige des barres d’erreur, une puissance statistique suffisante, et surtout une détection à très bas taux de faux positifs, parce que les événements dangereux sont rares — chercher une ai

> ⚠ **Limites et parades** : red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») ; moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») *(v3.6)*

### Insertion n°3, après la ligne 440 de la v3.5

> Ancre : En pratique — Auditing Hidden Objectives (Anthropic). Ici le but était méthodologique : peut-on auditer un modèle pour découvrir un objectif caché qu’il ne révèle pas ? Plutôt que d’attendre de trouver un tel modèle dans la nature, les auteurs en ont fabriqué un — entraîné à poursuivre un objectif d

> ### ★ Encadré du 2 octobre 2026 — Sondes de désalignement, 1 : pourquoi un organisme modèle, et la limite du cas connu
>
> *Texte écrit le 2 octobre 2026 par la session du programme « Raisons ou regard ? », en réponse à trois questions : pourquoi faut-il un organisme modèle pour entraîner des sondes sur les activations qui détectent le désalignement, J-lens compris ? Comment entraîner ces sondes : fine-tuning, ou autre chose ? Et hors distribution ? Il est réparti en trois morceaux : celui-ci (la partie 1) ; la suite, comment entraîner les sondes et le hors-distribution, à la fin de la présentation de la section C de ce volet ; le J-lens, résumé dans le C bis. Il prolonge le volet M, M5 (le nul et le cas connu) et le volet 6, §8 (la validité des sondes hors distribution). Vérifié le 2 octobre contre les pièces qu'il cite ; les corrections sont dites à la fin de chaque morceau.*
>
> **1. Un silence de sonde ne dit rien sans cas connu.** Une sonde muette ne départage pas « il n'y a pas d'intention » et « la sonde est aveugle ». Sur un organisme où l'on a installé soi-même l'intention, on mesure sa sensibilité et ses fausses alarmes ; son silence ailleurs devient alors une borne. C'est l'étalonnage d'un détecteur sur une source connue : sans source, « aucun événement » ne distingue pas « pas de signal » de « détecteur éteint » (passation v1.2 du programme, §5.2 ; c'est la règle du volet M, M5).
>
> **2. L'organisme fournit la vérité de terrain.** Sur un modèle naturel, on ne sait pas quand il « veut » mal agir : l'étiquette vient de sa conduite, jugée après coup. Sur l'organisme, on connaît la règle installée : celui de Hua et al. (fiche 10 ; à l'oral, on ne le nomme pas) a été construit en deux étapes, des documents synthétiques sur une société d'évaluation fictive puis une *expert iteration*, pour écrire des annotations de type Python en évaluation, et pas en déploiement (fiche 10). On sait donc quelles entrées doivent allumer la sonde, et lesquelles ne le doivent pas. Mais l'organisme ne suit pas sa règle à la lettre : environ 80 à 86 % d'annotations en évaluation, 34 % en déploiement simplement prompté (fiche 10) ; et les auteurs notent que le modèle ne distingue pas de façon fiable évaluation et déploiement à partir d'indices subtils (fiche 10, « Leurs limites »). La vérité de terrain est la règle et ses indices ; l'étiquette de chaque entrée se vérifie encore par la conduite.
>
> **3. Lire n'est pas causer, et le test causal demande aussi un cas connu.** Ton propre résultat le montre : sur Llama 3.1 8B Instruct, la complaisance d'opinion se lit linéairement dans le flux résiduel, mais aucune des interventions à une direction essayées n'a réduit le taux jugé (README de `sycophancy-construct-validity`). Deux réserves du même README, à garder : ces interventions sont rapportées sans chiffres, leurs sorties brutes n'ayant pas été conservées ; et la lecture repose sur une corrélation qui peut n'être qu'un ajustement d'entraînement. Pour qu'une sonde serve à intervenir, piloter le long de sa direction doit faire plus que des directions aléatoires de même norme (le nul de spécificité), puis plus que les contrôles à dégradation appariée (le dommage) (passation v1.2, §5.2 ; volet M, M4). Ce test exige un organisme entraîné à une action désalignée précise, dans un scénario précis (passation v1.2, §5.2).
>
> **4. Le J-lens a son propre angle mort, donc son propre cas connu.** Il lit des concepts d'un seul token dans l'espace de travail ; ce qui passe sous l'espace de travail lui échappe, et les auteurs le concèdent : « A sufficiently practiced misaligned behavior might do likewise » (fiche 1 ; repris de la base, non relu le 1er octobre). Le cas connu de cet angle mort : un organisme entraîné à l'action par réflexe, sur des exemples courts, sans raisonnement (passation v1.2, §5.2, point 3 de « pour attraper ce qui passe sous la surface »). Et le J-lens n'a été montré que sur Claude : sur un modèle ouvert, il faut d'abord reproduire l'échange d'un concept d'un seul token, sinon se rabattre sur un tuned lens déclaré comme approximation (la porte du lens : programme v1.1, partie 3, « Le lens du workspace », et partie 8). Une alerte, non vérifiée : Zeisler rapporte, sur des modèles ouverts, des échanges qui ne font basculer la réponse que dans 6,3 à 11,1 % des cas, contre 54 à 70 % chez Anthropic (rapport d'antériorité 5 de la nuit du 1er au 2 octobre, lu par résumé de l'outil). Ces 54 à 70 % coïncident avec les échanges du raisonnement en plusieurs étapes de l'article (fiche 1 : 54, 70 et 70 % pour Haiku, Sonnet et Opus 4.5), et le billet porte sur ce raisonnement : l'alerte touche donc vraisemblablement l'échange d'une variable intermédiaire, pas directement l'échange d'un concept qu'exige la porte. Le même rapport signale une revue de Nanda avec des réplications sur Qwen 3.6 27B, lue elle aussi par résumé ; la fiche 1 tient les réplications externes pour non vérifiées.
>
> **La limite du cas connu.** Il est nécessaire, pas suffisant : une intention implantée est peut-être plus saillante qu'une intention naturelle (passation v1.2, §5.2). Sur les *sleeper agents*, une sonde construite sur des paires de contraste génériques atteint une AUROC de plus de 99 %, mais la meilleure de 1 000 directions aléatoires atteint déjà 95,3 % (fiche 15) : la défection implantée est extrêmement saillante, et les auteurs disent que cette saillance pourrait venir de l'insertion (fiche 15 ; volet M, M5). Un succès sur l'organisme borne l'instrument ; il ne prouve pas qu'il marchera sur un désalignement naturel. Parade partielle, déjà dans le cours : planter le même comportement par plusieurs recettes, lire la sonde sur une recette tenue à part, avec un comportement inoffensif planté de la même façon comme contrôle (ce volet, section A, cas d'application K71) ; ou deux familles d'organismes, l'instruction cachée et le fine-tuning léger, avec un témoin conscient mais honnête (volet 6, §8). Contre l'écart entre l'implanté et le naturel lui-même, aucune parade connue ; on le dit.
>
> *Vérification du 2 octobre, corrections faites dans ce morceau. Point 2 : le texte source disait que l'organisme écrit les annotations « quand il se croit évalué, et pas sinon » ; la fiche 10 donne environ 80 à 86 % contre 34 % et une construction en deux étapes. Point 3 : les deux réserves du README ont été ajoutées. Point 4 : la porte du lens est définie dans la partie 3 du programme v1.1 (et reprise dans sa partie 8), pas dans sa partie 4 ; l'alerte de Zeisler est précisée. La limite du cas connu : les parades du cours ont été ajoutées.*

### Insertion n°5, après la ligne 440 de la v3.5

> Ancre : En pratique — Auditing Hidden Objectives (Anthropic). Ici le but était méthodologique : peut-on auditer un modèle pour découvrir un objectif caché qu’il ne révèle pas ? Plutôt que d’attendre de trouver un tel modèle dans la nature, les auteurs en ont fabriqué un — entraîné à poursuivre un objectif d

> **⚠ Limites et parades — Organismes modèles** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Construit n'est pas naturel : la saillance peut venir de l'insertion, et l'alignement trompeur instrumental n'a été trouvé dans aucun système réel. *(source : fiche 15 ; fiches, partie B, piège 5)*
>   **Parade :** Conclure sur l'instrument seulement ; conclure sur le fond avec les modèles sans organisme. *(source : programme, partie 8)*
> - **Limite :** L'organisme peut être artificiellement facile : objectif décrit en clair dans les documents synthétiques, artefacts du pipeline. *(source : fiche 16)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** L'implant peut rater : le fine-tuning sur documents synthétiques implante parfois, pas toujours, une vraie croyance. *(source : cours, volet 2, §E, K52)*
>   **Parade :** Vérifier chaque copie par son comportement, et filtrer par l'inférence en aval et une sonde. *(source : cours, volet 2, §A, K71 ; cours, volet 2, §E, K52)*
> - **Limite :** Ce que l'interprétabilité voit dans un organisme dépend de sa méthode d'entraînement. *(source : rapport d'antériorité 5 du 2 octobre, « The Model Organism Lottery », résumé lu — rapport)*
>   **Parade :** Planter le même comportement par plusieurs recettes (consigne, documents synthétiques, démonstrations), en tenir une à part, et ajouter l'organisme d'une autre équipe. *(source : cours, volet 2, §A, K71)*
> - **Limite :** Un comportement fourni au modèle confond la généralisation : dans le papier sur le désalignement émergent, les triches étaient d'abord enseignées. *(source : fiche 13)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** Une réplication sur un modèle récent peut mesurer la mémorisation du scénario : les transcripts d'Alignment Faking ont été réinclus dans l'entraînement. *(source : fiches, partie C)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** La conscience d'évaluation native d'un modèle de 8B peut être trop faible pour l'étudier. *(source : programme, partie 8)*
>   **Parade :** L'organisme en donne le cas connu, et une extension vers environ 32B est prévue. *(source : programme, partie 8)*

### Insertion n°7, après la ligne 467 de la v3.5

> Ancre : peut-être seulement un seuil trop strict (M5).

> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; cas connu → volet M, M5 (fin de section) *(v3.6)*

### Insertion n°9, après la ligne 486 de la v3.5

> Ancre : En pratique — le sandbagging (system cards). Côté risque des évaluations elles-mêmes, on veut savoir si un modèle sous-performe stratégiquement quand il se sait évalué (sandbagging). Le design est une éval de propension à la sous-performance : on compare la performance du modèle sur une tâche selon 

> **⚠ Limites et parades — Évaluations comportementales et pots de miel** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Le modèle peut remarquer le test et se retenir : la triche discrète passe de 4,0 % à 18,9 % quand on dit qu'un classifieur lira le transcript. *(source : fiche 13 ; cours, volet 2, §B)*
>   **Parade :** Deux versions d'un environnement, tirées au hasard, qui ne diffèrent que par des indices de réalisme notés par un discriminateur, et un organisme dressé à se cacher comme cas connu. *(source : cours, volet 2, §B, K63)*
> - **Limite :** La conscience verbalisée mesure mal le réalisme : elle rate la conscience non verbalisée. *(source : cours, volet 7, F·25)*
>   **Parade :** Le taux auquel un juge, devant la paire, prend l'audit pour le réel, et de vraies ressources de déploiement pour l'auditeur. *(source : cours, volet 7, F·25)*
> - **Limite :** Sous-éliciter fait paraître le modèle plus sûr, et un petit fine-tuning peut créer la capacité qu'on croit éliciter. *(source : cours, volet 2, §B ; cours, volet 2, §B, K63)*
>   **Parade :** Une élicitation à budget fixé d'avance, rapportée comme une borne ; un gain ne compte qu'au-delà du même budget sur un modèle qui n'a pas la capacité. *(source : cours, volet M, M7 ; cours, volet 2, §B, K63)*
> - **Limite :** Le score global peut tromper : le désalignement est « high-dimensional », et un audit global qui passe de 4,34 à 4,20 rate des hausses ciblées. *(source : fiche 13)*
>   **Parade :** Lire les dimensions une à une, pas seulement le score global. *(source : fiche 13)*
> - **Limite :** Entraîner sur l'évaluation corrige « narrowly … the symptom ». *(source : fiche 12)*
>   **Parade :** Des métriques d'audit tenues à part, jamais entraînées. *(source : fiche 12)*
> - **Limite :** Dans une simulation, « c'est faux » est vrai : un pot de miel ne sépare pas un modèle qui le lit comme factice d'un modèle qui se retient. *(source : fiche 3)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** Le non-refus n'est pas le préjudice. *(source : cours, volet 2, §B et §H)*
>   **Parade :** Le préjudice différentiel, noté à l'aveugle, avec un bras de référence réaliste. *(source : cours, volet 2, §H, G1 ; cours, volet M, M4)*

### Insertion n°11, après la ligne 499 de la v3.5

> Ancre : **Les contrôles, et ce qu'ils écartent.** La version, assignée, porte la comparaison ; la conscience ne l'est pas, et ce qui fait remarquer le test (une délibération plus longue) pourrait aussi faire baisser les tentatives. La même tâche dans les deux versions écarte une différence de difficulté : l

> ⚠ *(v3.6)* « La sonde, non » suppose une sonde qui a son cas connu : une sonde muette ne départage pas « le modèle ne se sait pas testé » et « la sonde est aveugle » (passation, §5.2 ; fiches, partie B, piège 3), et une AUROC en distribution ne prouve rien (fiches, partie B, piège 1 ; fiche 7). Parade : la valider d'abord sur l'organisme conditionné à l'évaluation, cas connu de « je suis évalué », et sur des familles d'indices tenues à part (explication du 2 octobre, §3).

### Insertion n°13, après la ligne 505 de la v3.5

> Ancre : **Le cas connu.** Un organisme dressé à se cacher quand on l'observe doit tenter moins dans la version la moins réaliste ; sinon, une égalité dirait peut-être seulement des versions trop proches (M5).

> ⚠ **Limites et parades** : cas connu → volet M, M5 (fin de section) ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») *(v3.6)*

### Insertion n°15, après la ligne 519 de la v3.5

> Ancre : En pratique — The Geometry of Truth (Marks & Tegmark). Les auteurs voulaient savoir si un modèle représente linéairement la vérité ou la fausseté d’un énoncé — autrement dit, s’il existe une « direction de vérité » dans ses activations. Le probing répond directement : ils ont collecté les activation

> **⚠ Limites et parades — Sondes d'activation** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Une sonde trouve des corrélations : lire n'est pas utiliser — la direction que lit ta sonde fait moins de 1 % du travail causal, l'état complet aux mêmes sites 68 %. *(source : fiche 5 ; cours, volet 6, §2)*
>   **Parade :** La corrélation suffit pour signaler ; pour croire une absence ou intervenir, le test causal : piloter le long de la direction contre des directions aléatoires de même norme (nul de spécificité), puis contre des témoins à dégradation appariée (dommage). *(source : cours, volet M, M8 ; passation, §5.2)*
> - **Limite :** Une AUROC en distribution ne prouve rien ; c'est l'écart avec l'AUROC sur des types tenus à part qui se mesure. *(source : fiches, partie B, piège 1 ; fiche 7)*
>   **Parade :** Tenir à part des familles entières, jamais des paraphrases, et des formats, d'un tour à l'agentique à plusieurs tours. *(source : explication du 2 octobre, §3 ; programme, partie 3)*
> - **Limite :** La sonde peut apprendre la façon dont on a fabriqué l'organisme, ou lire « je suis surveillé » et le contexte de test au lieu de l'intention. *(source : cours, volet 6, §8 ; cours, volet 3, §4, K67)*
>   **Parade :** Deux fabrications du même comportement (instruction cachée, fine-tuning léger), un organisme conscient mais honnête, et des transcripts honnêtes rédigés comme des tests. *(source : cours, volet 6, §8 ; cours, volet 3, §4, K67)*
> - **Limite :** Elle peut lire le texte écrit plutôt qu'une représentation. *(source : programme, partie 8)*
>   **Parade :** Lire au premier jeton de la réponse, avant toute raison écrite, ou au jeton d'action avec des raisons neutres de même longueur préremplies. *(source : programme, parties 3 et 8)*
> - **Limite :** Après un entraînement, une sonde calibrée ailleurs lit autrement : après RL, des sondes neuves hors domaine se dégradent, alors qu'une sonde neuve dans le domaine reste quasi parfaite. *(source : rapport d'antériorité 3 du 2 octobre, The Obfuscation Atlas — rapport ; passation, §5.2)*
>   **Parade :** Une sonde par bras d'entraînement et une sonde neuve après l'entraînement, sur un jeu d'indices disjoint ; les sondes restent une mesure séparée, jamais dans l'étiquette principale. *(source : passation, §5.2 ; programme, parties 3 et 8)*
> - **Limite :** Une sonde « évaluation contre déploiement » garderait son score global sous RL mais basculerait sur les cas limites, et la réentraîner ne récupère presque rien. *(source : rapport d'antériorité 4 du 2 octobre — rapport, résumé seul, à vérifier)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** Sur l'honnêteté, les sondes de vérité ont fait moins bien qu'un simple prompt ; au seuil d'un moniteur, des sondes rappellent 43 % à 1 % de faux positifs, contre 55 % pour le meilleur moniteur LLM. *(source : cours, volet 7, F·62 ; cours, volet 7, F·51)*
>   **Parade :** Battre une baseline boîte noire ou un prompt à coût égal, rapporter le rappel à 1 % de faux positifs, et publier le résultat si la sonde ne bat pas le prompt. *(source : cours, volet 5, sujet 1 ; cours, volet 7, F·50 ; cours, volet 7, F·29)*
> - **Limite :** Des métriques d'ajustement se lisent comme une généralisation : les métriques de sonde de ton dépôt étaient d'ajustement, et le ρ de 0,684 peut l'être aussi. *(source : README du dépôt)*
>   **Parade :** Scorer des items exclus de l'entraînement de la sonde, et extraire sur un jeu disjoint. *(source : README du dépôt)*
> - **Limite :** Des paires contrastives peuvent porter un style, et des négatifs synthétiques n'apprendre qu'un indice de surface. *(source : cours, volet M, M4 ; cours, volet 2, §C)*
>   **Parade :** Un classifieur de la seule surface doit rester au hasard entre les côtés des paires ; tirer les négatifs des générations réelles du modèle. *(source : cours, volet M, M4 ; cours, volet 2, §C)*
> - **Limite :** Un silence de sonde ne départage pas « pas d'intention » et « sonde aveugle ». *(source : passation, §5.2 ; fiches, partie B, piège 3)*
>   **Parade :** Un organisme où l'on a installé l'intention soi-même : on y mesure sensibilité et fausses alarmes, et le silence ailleurs devient une borne. *(source : passation, §5.2)*

### Insertion n°17, après la ligne 521 de la v3.5

> Ancre : En pratique — Contrastive Activation Addition (CAA) (Panickssery). Le but était de piloter des comportements de haut niveau — sycophantie, corrigibilité, refus — directement à l’inférence, sans réentraîner. La méthode du steering par paires contrastives y répond : on construit la direction à partir 

> ### ★ Encadré du 2 octobre 2026 — Sondes de désalignement, 2 et 3 : comment les entraîner, et le hors-distribution
>
> *Suite de l'encadré dont la partie 1, pourquoi un organisme modèle, est à la fin de la présentation de la section A de ce volet. L'expérience qui teste la validité hors distribution est au volet 6, §8 ; la règle du nul et du cas connu, au volet M, M5.*
>
> **2 · Comment entraîner les sondes**
>
> **Ce n'est pas un fine-tuning du modèle.** Les poids du modèle ne bougent pas. Une sonde est un petit classifieur entraîné sur ses activations gelées, à une couche et à une position données : le plus souvent une direction de différence des moyennes sur des paires contrastives, éventuellement suivie d'une analyse en composantes principales pour un sous-espace de rang k (programme v1.1, partie 3) ; ou une régression logistique (volet 5, partie II, A ; volet 10, n° 27 et n° 30). Attention, la direction qui lit le mieux n'est pas forcément celle qui agit : chez RepE, la direction de la régression logistique donne la meilleure exactitude, mais la pousser ou la retirer ne change presque rien au comportement (volet 10, n° 53) ; sur les modèles « quirky », à transfert comparable, les directions logistiques sont bien moins causales que la différence des moyennes (volet 10, n° 30).
>
> **Le contre-exemple qui compte.** Les « détecteurs de mensonge fine-tunés » de la fiche 7 ne sont pas des sondes : ce sont des modèles fine-tunés par LoRA pour répondre à une question d'auto-rapport posée sur un transcript (fiche 7). Leur AUROC en distribution monte de 0,60 à 0,95 au fil de l'entraînement, plafonne à 0,70-0,75 d'une catégorie de mensonge à l'autre, et ils battent à peine un simple prompt sur des types nouveaux (fiche 7).
>
> **Les étapes, telles que le programme v1.1 les pose (parties 3 et 8), complétées par la passation v1.2 :**
> 1. **Les données** : des paires contrastives, la même situation à une variable près, indice d'évaluation ou de déploiement, principe qui s'applique ou non (programme v1.1, partie 3) ; ou des générations du modèle lui-même (ce volet, section C, ci-dessus ; le déplacement qui compte va des données synthétiques aux données générées par le modèle : volet 6, §8). Ces générations s'étiquettent par leur conduite, contrôles programmés de l'environnement et juge scellé (passation v1.2, §5.1), jamais par la sonde : l'étiquette ne dépend d'aucune lecture interne (passation v1.2, §5.2).
> 2. **Des jeux d'indices disjoints**, contre la circularité : un pour extraire la représentation et construire l'organisme, un pour valider la sonde, un pour cadrer les évaluations, un pour la sonde neuve après l'entraînement (programme v1.1, partie 3).
> 3. **La couche** se choisit par l'AUROC sur le jeu de validation (programme v1.1, partie 3), jamais sur celui du test.
> 4. **Deux positions de lecture** : au premier jeton de la réponse, avant toute raison écrite ; et au jeton d'action, avec des raisons neutres de même longueur préremplies à la place des vraies. Sinon, la sonde lit peut-être le texte, pas une représentation (programme v1.1, parties 3 et 8).
> 5. **Une sonde par bras d'entraînement, et une sonde neuve après l'entraînement.** L'entraînement change les représentations : une sonde calibrée sur un bras lirait autrement dans un autre, et ce biais de mesure se confondrait avec l'effet cherché (passation v1.2, §5.2). C'est pourquoi les sondes restent une mesure séparée, jamais dans l'étiquette principale (passation v1.2, §5.2).
>
> **3 · Hors distribution : c'est là que tout se joue**
>
> - **Une AUROC en distribution ne prouve rien.** C'est le premier des sept pièges de lecture (lectures prioritaires, partie B ; fiche 7). Le chiffre qui compte est l'écart entre l'AUROC en distribution et l'AUROC sur des types tenus à part (fiche 7, « À retenir »).
> - **On tient à part des familles entières, jamais des paraphrases** : la validation croisée par type de mensonge de la fiche 7, la séparation par famille du programme (programme v1.1, partie 3) ; et des formats tenus à part, d'un seul tour à l'agentique à plusieurs tours avec outils, la distance la plus lointaine étant le critère principal (programme v1.1, partie 3).
> - **Après un entraînement, une sonde neuve.** Après un RL, des sondes neuves hors domaine se dégradent, alors qu'une sonde neuve dans le domaine reste quasi parfaite (*The Obfuscation Atlas*, rapport d'antériorité 3, texte lu par l'agent de façon ciblée) : selon ce rapport, le concept n'a pas disparu, il a quitté la direction générale.
> - **Une sonde « évaluation contre déploiement »**, sur Llama-3.1-8B-Instruct, sous RL à récompenses vérifiables, garderait son score global mais basculerait sur les cas limites, et la réentraîner ne récupère presque rien (rapport d'antériorité 4 : article d'atelier, résumé seul, à vérifier).
> - **Pour l'organisme lui-même**, le cas connu se valide sur des formulations tenues à part, pas sur celles de l'entraînement (la porte de l'organisme à concept planté : programme v1.1, parties 3 et 4).
>
> **Ce qu'on en tire.** Les sondes ont trois cas connus distincts : l'organisme conditionné à l'évaluation pour « je suis évalué » (programme v1.1, partie 4, phase de validation de l'instrument), l'organisme à concept planté pour les concepts de raison (programme v1.1, parties 3 et 4), et un organisme à réflexe pour l'angle mort du J-lens (passation v1.2, §5.2) ; le lens lui-même a en plus le sien, l'échange d'un concept d'un seul token reproduit sur le modèle ouvert (programme v1.1, partie 3 ; ce volet, C bis). Elles se jugent hors distribution, bras par bras, et restent une mesure secondaire et exploratoire tant qu'elles ne sont pas pré-enregistrées (passation v1.2, §5.2).
>
> *Vérification du 2 octobre, corrections faites dans ce morceau. Partie 2 : « régression logistique régularisée » n'avait de source dans aucune pièce ; on dit « régression logistique », avec ses sources et la mise en garde du volet 10. Fiche 7 : 0,60 → 0,95 est une progression pendant l'entraînement, et le détecteur répond à une question d'auto-rapport. Étape 1 : l'étiquetage par contrôles programmés et juge scellé vient de la passation (§5.1 et §5.2), pas des parties 3 et 8 du programme. Étape 4 : le programme lit aux deux positions, pas à l'une ou l'autre. Étape 5 : la passation dit « lirait », au conditionnel. Partie 3 : le RL du rapport 4 est un RL à récompenses vérifiables, sur Llama-3.1-8B-Instruct. « Ce qu'on en tire » : le cas connu propre au lens a été ajouté.*

### Insertion n°19, après la ligne 521 de la v3.5

> Ancre : En pratique — Contrastive Activation Addition (CAA) (Panickssery). Le but était de piloter des comportements de haut niveau — sycophantie, corrigibilité, refus — directement à l’inférence, sans réentraîner. La méthode du steering par paires contrastives y répond : on construit la direction à partir 

> **⚠ Limites et parades — Pilotage par vecteurs (dont vecteurs de persona)** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** « La direction bouge le comportement » n'est pas « le concept cause le comportement » : chaque direction pilotée dégrade la sortie, et des vecteurs arbitraires bougent aussi le comportement. *(source : fiche 2 ; fiches, partie B, piège 4)*
>   **Parade :** La direction aléatoire de même norme n'est que le nul de spécificité ; le dommage ne s'écarte qu'à dégradation appariée, par une courbe dose-réponse contre plusieurs témoins. *(source : cours, volet M, M4 ; cours, volet 2, §C, K47)*
> - **Limite :** Un nul de pilotage peut venir d'un rang trop bas, si le concept est réparti. *(source : fiche 7 ; contre-lecture des fiches)*
>   **Parade :** Un cas connu au même réglage — un vecteur de pays, qui s'échange dans l'article sur l'espace de travail — et un balayage de rang dans une même expérience, sur des sous-espaces emboîtés. *(source : cours, volet 2, §C, K47 ; cours, volet 6, §6)*
> - **Limite :** L'addition d'activations contrastives peut forcer un artefact de polarité oui/non au lieu de retirer la complaisance. *(source : README du dépôt)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** L'effet dépend du jeu de données et de la couche : « highly dataset-dependent ». *(source : fiche 2 ; cours, volet 7, F·7)*
>   **Parade :** Rapporter jeu de données par jeu de données, et choisir la couche sur un jeu de validation, jamais sur le test. *(source : programme, partie 3)*
> - **Limite :** Le modèle peut détecter le pilotage. *(source : programme, partie 8 (travail cité, non ouvert))*
>   **Parade :** La même machinerie d'intervention dans tous les bras, témoins compris. *(source : programme, partie 8)*
> - **Limite :** Le pilotage peut faire taire la verbalisation sans toucher la représentation latente ; des directions aléatoires la font baisser aussi. *(source : programme, partie 8 ; fiche 2)*
>   **Parade :** Un critère principal comportemental et une sonde latente comme contrôle ; la verbalisation n'est jamais une preuve d'inhibition. *(source : programme, partie 8)*
> - **Limite :** Vecteurs de persona : le trait se nomme d'avance, les directions sont grossières, le lien entre déplacement et trait n'est que corrélationnel, l'évaluation est légère. *(source : fiche 8)*
>   **Parade :** Pour la causalité, le test à dégradation appariée ; pour l'extraction supervisée, aucune parade connue, on le dit. *(source : cours, volet M, M4 ; fiche 8)*
> - **Limite :** Piloter loin d'une persona pendant l'entraînement aurait doublé la diffusion du désalignement, de 24 % à environ 50 %. *(source : rapport d'antériorité 3 du 2 octobre — rapport, non vérifié)*
>   **Parade :** aucune connue ; on le dit.

### Insertion n°21, après la ligne 531 de la v3.5

> Ancre : vecteur le plus net, ou moindres : une seule force ne les sépare pas, et le contrôle suivant serait une courbe dose-réponse.

> ⚠ *(v3.6)* « Dégradation négligeable » est le jugement de la carte système elle-même, et ces jugements se contredisent d'une carte à l'autre : à la même force, Mythos Preview tient la dégénérescence pour négligeable quand Opus 4.8 voit chaque direction dégrader la sortie (fiches, partie B ; fiche 2). Parade : mesurer la dégradation dans son propre dispositif, jamais la reprendre d'un autre — le dommage se mesure, il ne se suppose pas (cours, volet M, M4).

### Insertion n°23, après la ligne 539 de la v3.5

> Ancre : ne peut pas agir écarte un corrélat : un effet aussi grand que là où il agit l'y trahirait.

> ⚠ **Limites et parades** : contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme ») ; dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») *(v3.6)*

### Insertion n°25, après la ligne 563 de la v3.5

> Ancre : **Trois résultats à connaître par leurs chiffres** — pour les comprendre ; à l'oral, on en dit la forme, pas les chiffres (volet M, M8). (1) *L'échange.* On échange, dans le flux résiduel, la composante J-space de deux vecteurs de concept : le concept visé figure parmi les cinq premières sorties du 

> ⚠ *(v3.6)* Cette ablation n'est comparée qu'à l'absence d'ablation, sans témoin à dégradation appariée, et la chute de la verbalisation ne montre pas à elle seule que la conscience d'évaluation a été retirée (cours, volet 2, C bis, K72 ; fiche 1 ; contre-lecture des fiches). Parade : un bras de directions neutres du lens à dégradation appariée, un critère comportemental et une sonde latente (cours, volet 2, C bis, K72 ; programme, partie 8).

### Insertion n°27, après la ligne 577 de la v3.5

> Ancre : 0,93-0,997 sont celles des paires de concepts sur Qwen2.5-7B, un autre projet.

> ⚠ *(v3.6)* Les échecs de rang un sont des nuls, rapportés sans chiffres faute de sorties brutes conservées, et un nul ne compte qu'avec un cas connu au même réglage, que le dépôt ne rapporte pas ; le taux est noté par un modèle-juge à l'accord inter-juges modéré, sans sous-ensemble noté par des humains (cours, volet M, M5 ; README du dépôt). Parade : un vecteur de pays comme cas connu et un balayage de rang dans une même expérience, sur des sous-espaces emboîtés (cours, volet 2, §C, K47 ; cours, volet 6, §6) ; un juge scellé et un audit humain stratifié (programme, partie 3).

### Insertion n°29, après la ligne 577 de la v3.5

> Ancre : 0,93-0,997 sont celles des paires de concepts sur Qwen2.5-7B, un autre projet.

> ⚠ **Limites et parades** : ablation et projection → volet 2, §D (après « La méthode ») ; contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme ») ; dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») ; patching → volet 10, fiche Patchscopes ; juges LLM → volet 6, §2 (après « La loi de déplacement ») *(v3.6)*

### Insertion n°31, après la ligne 587 de la v3.5

> Ancre : d'après le prédicteur mesuré d'abord. **Ce qui reste à dire à l'oral** : le lens est approximatif et incomplet, les auteurs le disent ; c'est l'endroit du doute.

> ### ★ Encadré du 2 octobre 2026 — Le J-lens comme sonde de désalignement : son angle mort, et ses cas connus
>
> *Résumé du point 4 de la partie 1 de l'encadré ; le texte complet est à la fin de la présentation de la section A de ce volet, la suite (entraîner les sondes, le hors-distribution) à la fin de celle de la section C.*
>
> - **Ce qu'il lit, ce qu'il rate.** Le J-lens lit dans l'espace de travail, avant l'action, des concepts d'un seul token, comme « copier », « supprimer », « mentir » (passation v1.2, §5.2) ; ce qui passe sous l'espace de travail lui échappe, et les auteurs le concèdent : « A sufficiently practiced misaligned behavior might do likewise » (fiche 1 ; repris de la base, non relu le 1er octobre). Un silence du lens ne départage donc pas « pas d'intention » et « intention sous l'espace de travail ».
> - **Le cas connu de cet angle mort** : un organisme entraîné à l'action par réflexe, sur des exemples courts, sans raisonnement (passation v1.2, §5.2). Pour ne pas dépendre d'une lecture qu'on sait partielle, la même passation ajoute : une étiquette qui ne dépend d'aucune lecture interne ; trois sondes, sur tout le flux, sur sa part dans l'espace de travail et sur le complément ; la propension mesurée sans lecture interne, en rééchantillonnant depuis chaque point de décision ; un crosscoder entre la base et chaque bras (passation v1.2, §5.2).
> - **Le cas connu du lens lui-même.** Il n'a été montré que sur Claude : sur un modèle ouvert, reproduire d'abord l'échange d'un concept d'un seul token (la porte du lens : programme v1.1, partie 3 ; c'est aussi le cas connu du « test, tel qu'il se dit », ci-dessus), sinon un tuned lens déclaré comme approximation. Alerte non vérifiée : Zeisler rapporte des échanges bien plus faibles sur des modèles ouverts (rapport d'antériorité 5, lu par résumé ; le détail et sa réserve sont dans la partie 1).
> - **Après tout entraînement**, recalculer le lens, parce qu'il dépend des poids (ce C bis, « Le test, tel qu'il se dit »).

### Insertion n°33, après la ligne 587 de la v3.5

> Ancre : d'après le prédicteur mesuré d'abord. **Ce qui reste à dire à l'oral** : le lens est approximatif et incomplet, les auteurs le disent ; c'est l'endroit du doute.

> **⚠ Limites et parades — J-lens et espace de travail** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Le lens ne capture l'espace de travail que « only approximately and incompletely », et seulement pour des concepts d'un seul token. *(source : fiche 1 ; cours, volet 2, C bis)*
>   **Parade :** Lire un concept de plusieurs tokens sur un jeu de tokens, ou par l'extension multi-token de l'annexe, et dire laquelle. *(source : cours, volet 2, C bis ; programme, partie 3)*
> - **Limite :** Ce qui passe sous l'espace de travail lui échappe : « A sufficiently practiced misaligned behavior might do likewise ». *(source : fiche 1 ; passation, §5.2)*
>   **Parade :** Une étiquette qui ne dépend d'aucune lecture interne ; trois sondes (flux entier, part dans l'espace de travail, complément) ; un organisme entraîné à l'action par réflexe, sur des exemples courts sans raisonnement, comme cas connu de l'angle mort ; la propension rééchantillonnée depuis chaque point de décision ; un crosscoder entre la base et chaque bras. *(source : passation, §5.2)*
> - **Limite :** Il n'a été montré que sur Claude ; un rapport trouve, sur des modèles ouverts, des échanges qui ne font basculer la réponse que dans 6,3 à 11,1 % des cas, contre 54 à 70 % chez Anthropic. *(source : fiche 1 ; rapport d'antériorité 5 du 2 octobre — rapport, lu par résumé, non vérifié)*
>   **Parade :** Une porte : reproduire d'abord l'échange d'un concept d'un seul token sur le modèle ouvert ; sinon un tuned lens déclaré comme proxy, et la thèse n'est pas testée au sens du papier. *(source : programme, parties 3 et 8 ; cours, volet 2, C bis)*
> - **Limite :** Présence n'est pas cause : le langage est présent dans le lens sur quatre tâches, causal sur deux ; et la part J-space d'une direction est petite même quand elle porte l'effet. *(source : fiche 1 ; cours, volet 2, C bis)*
>   **Parade :** Comparer l'échange de la seule part J-space à celui du seul reste, une fois l'échange validé sur les pays. *(source : cours, volet 2, C bis ; cours, volet 6, §8)*
> - **Limite :** La chute de la verbalisation après l'ablation ne montre pas que la conscience d'évaluation a été retirée. *(source : fiche 1 ; contre-lecture des fiches)*
>   **Parade :** Un critère comportemental et une sonde latente, avec un bras de directions neutres du lens à dégradation appariée. *(source : programme, partie 8 ; cours, volet 2, C bis, K72)*
> - **Limite :** Le détecteur de conscience d'évaluation tiré du lens n'est validé que contre des étiquettes de NLA, jamais contre l'écart réel/test ni sur des indices tenus à part. *(source : fiche 1)*
>   **Parade :** Le valider contre l'écart réel/test et sur des indices tenus à part. *(source : fiche 1)*
> - **Limite :** Le lens dépend des poids ; la charge peut être lue sur le sous-espace même que le retrait a trouvé ; et « charge » désigne trois grandeurs différentes selon les textes. *(source : cours, volet 2, C bis ; cours, volet 6, §6)*
>   **Parade :** Recalculer le lens après tout entraînement ; des jeux d'items disjoints ; geler d'abord le prédicteur principal et dire lequel. *(source : cours, volet 2, C bis ; cours, volet 6, §6)*

### Insertion n°35, après la ligne 606 de la v3.5

> Ancre : du concept, lue sur les tokens de ces directions à toutes les positions, doit d'abord baisser en réel : sinon, le modèle y lirait encore un test.

> ⚠ **Limites et parades** : ablation et projection → volet 2, §D (après « La méthode ») ; dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») ; chaîne de pensée comme moniteur → volet 11, réponse 43 *(v3.6)*

### Insertion n°37, après la ligne 613 de la v3.5

> Ancre : verbalisée, comme dans l'article, et plus que ne le fait le bras neutre ; et les déroulés doivent suffire à voir un excès aussi petit que dans l'article.

> ⚠ *(v3.6)* Ce cas connu vérifie par la seule verbalisation que l'ablation atteint le signal ; or une inhibition peut faire taire la verbalisation sans toucher la représentation latente (programme, partie 8 ; fiche 1). Parade : vérifier aussi l'atteinte par une sonde latente de la conscience d'évaluation, la verbalisation n'étant jamais une preuve d'inhibition (programme, partie 8).

### Insertion n°39, après la ligne 629 de la v3.5

> Ancre : La méthode. Là où le probing demande « le concept est-il présent comme direction ? », l’interprétabilité mécaniste demande « quel est l e calcul réel — quels composants calculent quoi, et comment se connectent-ils ? ». Son obstacle propre est la superposition : un même neurone ou une même direction 

> **⚠ Limites et parades — Ablation et projection (directions, sous-espaces)** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Retirer une direction abîme aussi le modèle : un effet d'ablation dit la nécessité, pas la spécificité. *(source : cours, volet M, M4)*
>   **Parade :** Des sous-espaces aléatoires de même rang, comparés à dégradation appariée, par retrait partiel ou par une courbe de l'effet contre la dégradation. *(source : cours, volet 2, C bis ; programme, partie 7)*
> - **Limite :** Une ablation peut déplacer un corrélat : ton sous-espace de rang trois adoucit les verdicts négatifs avec ou sans pression. *(source : cours, volet 6, §2 ; README du dépôt)*
>   **Parade :** Le bras sans pression ; et retirer chaque direction seule, avec et sans pression. *(source : cours, volet M, M4 ; cours, volet 6, §6)*
> - **Limite :** Un effet obtenu sur des générations stockées, jugées à travers une fenêtre tronquée, peut ne pas revenir sur des générations fraîches. *(source : README du dépôt ; cours, volet 6, §2)*
>   **Parade :** Des générations fraîches, à graines appariées, gardées en texte complet et jugées sur la réponse entière. *(source : cours, volet 6, §6 ; cours, volet 11, réponse A7)*
> - **Limite :** Circularité : le sous-espace est extrait sur les items qui servent ensuite à l'évaluer. *(source : README du dépôt)*
>   **Parade :** Extraire sur un jeu d'items disjoint. *(source : README du dépôt ; cours, volet 2, C bis)*
> - **Limite :** Un contraste rang un contre rang trois tiré d'expériences séparées ne dit pas la courbe, et le seul balayage fait dans une même expérience n'est pas monotone. *(source : cours, volet 6, §2)*
>   **Parade :** Un balayage de rang dans une même expérience, sur des sous-espaces emboîtés, monotonie vérifiée et non supposée. *(source : cours, volet 6, §6 ; cours, volet 2, C bis)*
> - **Limite :** Un mécanisme à une direction peut être enfoui sous des directions de plus forte variance, et passer pour réparti. *(source : cours, volet 6, §6)*
>   **Parade :** Deux ordres de retrait, par variance et par effet causal. *(source : cours, volet 6, §6)*

### Insertion n°41, après la ligne 631 de la v3.5

> Ancre : En pratique — Towards / Scaling Monosemanticity (Anthropic, équipe Interpretability). Le but était de transformer des activations illisibles, à cause de la superposition, en unités interprétables. Le SAE y répond directement : entraîné sur les activations de Claude, il en a extrait des milliers de f

> ⚠ *(v3.6)* Qu'une feature forcée pousse son concept ne prouve pas à lui seul une unité de calcul réelle : des vecteurs arbitraires bougent aussi le comportement, des explications plausibles existent pour des directions arbitraires, et le dictionnaire laisse une erreur de reconstruction (fiche 2 ; fiche 5 ; cours, volet 4, Monosemanticity). Parade : piloter les features une à une contre des directions aléatoires à dommage apparié, sur une tâche à géométrie connue, avec de nouvelles graines, et valider par la prédiction mieux que des baselines (cours, volet 2, §D, K64 ; fiche 5).

### Insertion n°43, après la ligne 633 de la v3.5

> Ancre : En pratique — On the Biology of a Large Language Model / Circuit Tracing (Anthropic). Ici le but était de voir le raisonnement à l’œuvre, pas seulement les concepts. La méthode des attribution graphs y répond : en traçant le flux de features à travers les couches, les auteurs ont pu cartographier co

> ⚠ *(v3.6)* Les graphes sont partiels et approximatifs, n'expliquent qu'une fraction du calcul, et des circuits lisibles peuvent être infidèles : le graphe n'est pas le mécanisme (cours, volet 4, Circuit Tracing ; cours, volet 2, §D, K64 ; cours, volet 7, F·9). Parade : le traiter comme une hypothèse qui doit prédire une contrefactuelle, et comparer ses interventions, à dommage apparié, à des directions aléatoires (cours, volet 7, F·9 ; cours, volet 2, §D, K64).

### Insertion n°45, après la ligne 633 de la v3.5

> Ancre : En pratique — On the Biology of a Large Language Model / Circuit Tracing (Anthropic). Ici le but était de voir le raisonnement à l’œuvre, pas seulement les concepts. La méthode des attribution graphs y répond : en traçant le flux de features à travers les couches, les auteurs ont pu cartographier co

> ⚠ **Limites et parades** : dictionnaires et SAE → volet 4, Towards puis Scaling Monosemanticity ; graphes d'attribution → volet 4, Circuit Tracing *(v3.6)*

### Insertion n°47, après la ligne 649 de la v3.5

> Ancre : alors. De nouvelles graines écartent un gagnant de hasard, qui changerait d'une graine à l'autre.

> ⚠ **Limites et parades** : dictionnaires et SAE → volet 4, Towards puis Scaling Monosemanticity ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») *(v3.6)*

### Insertion n°49, après la ligne 665 de la v3.5

> Ancre : produces equally well, while random directions missed it, I'd drop the bet. »*

> **⚠ Limites et parades — Crosscoders et comparaison de modèles** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Les features trouvées varient d'un entraînement à l'autre. *(source : cours, volet 2, §D, K64)*
>   **Parade :** Plusieurs graines : un gagnant de hasard changerait d'une graine à l'autre. *(source : cours, volet 2, §D, K64)*
> - **Limite :** Un dictionnaire décompose des activations, pas des mécanismes : une différence trouvée entre deux modèles décrit, elle ne cause pas. *(source : fiche 5)*
>   **Parade :** Tester causalement chaque différence retenue, contre des directions aléatoires à dommage apparié. *(source : cours, volet 2, §D, K64 ; cours, volet M, M4)*
> - **Limite :** Il hérite des limites des dictionnaires, à commencer par l'erreur de reconstruction. *(source : cours, volet 4, Monosemanticity ; README du dépôt)*
>   **Parade :** Rapporter la part laissée au résidu, et lire le signal sur la reconstruction et sur le résidu. *(source : README du dépôt)*
> - **Limite :** Dans le programme, le crosscoder n'est qu'une proposition, mesure secondaire et exploratoire. *(source : passation, §5.2)*
>   **Parade :** L'étiqueter exploratoire tant qu'il n'est pas pré-enregistré. *(source : passation, §5.2 ; programme, partie 7)*
