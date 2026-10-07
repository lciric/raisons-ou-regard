# Insertions appliquées — volet2_E_a_I — FR

### Insertion n°1, après la ligne 673 de la v3.5

> Ancre : En pratique — Debate (Khan et al.). Le but était de tester empiriquement si le debate aide un juge non expert à atteindre la vérité. Le protocole de debate y répond : sur des questions où le juge n’a pas l’information nécessaire, on fait débattre deux modèles défendant des réponses opposées, et l’on

> **⚠ Limites et parades — Débat et supervision évolutive** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** L'argument obfusqué : trop complexe pour être réfuté, même faux. *(source : cours, volet 2, §E)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** Optimiser l'approbation peut rendre plus convaincant à tort : le RLHF a appris aux modèles à persuader des humains de réponses fausses. *(source : cours, volet 2, §E)*
>   **Parade :** Mesurer sur un banc où l'on connaît la bonne réponse. *(source : cours, volet 2, §E)*
> - **Limite :** Le signe empirique vient d'un banc où l'on connaît la réponse ; au-delà de l'expertise humaine, il n'y a plus de référence. *(source : cours, volet 2, §E ; cours, volet 2, clôture)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** Le juge est souvent un modèle : les limites des juges LLM s'appliquent. *(source : fiches, partie B, piège 6)*
>   **Parade :** Un juge scellé et un audit humain (encadré « Juges LLM », volet 6, §2). *(source : programme, partie 3)*

### Insertion n°3, après la ligne 692 de la v3.5

> Ancre : domaine illisible : l'élicitation doit y retrouver ce fait.

> ⚠ **Limites et parades** : organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») *(v3.6)*

### Insertion n°5, après la ligne 709 de la v3.5

> Ancre : alone gave back the truth, I'd drop the bet. »*

> **⚠ Limites et parades — Élicitation non supervisée par cohérence** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Elle trouve le trait le plus saillant, pas forcément la vérité, et elle est sensible au prompt. *(source : cours, volet 6, §8 ; cours, volet 4, CCS)*
>   **Parade :** Rendre vérifiable l'invérifiable : implanter un faux fait cohérent, vérifier qu'il a pris, puis lire ce qu'elle rend, avec une copie au vrai fait apparié comme témoin. *(source : cours, volet 2, §E, K52)*
> - **Limite :** Une fausse croyance cohérente l'est autant qu'une vraie : la cohérence seule ne départage pas. *(source : cours, volet 2, §E, K52)*
>   **Parade :** Ancrer la méthode sur des réponses vérifiées, par l'entraînement du facile au difficile, et dire que sans lui elle ne rend que la cohérence. *(source : cours, volet 2, §E, K52)*
> - **Limite :** L'échec peut rester silencieux là où l'évaluation en distribution est impossible. *(source : cours, volet 2, §E, K52)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** Le filtre de l'implant et la méthode peuvent lire la même feature saillante. *(source : cours, volet 2, §E, K52)*
>   **Parade :** L'inférence en aval comme témoin, indépendante de la sonde. *(source : cours, volet 2, §E, K52)*

### Insertion n°7, après la ligne 717 de la v3.5

> Ancre : En pratique — l’automatisation (Anthropic, 2026). Plus récemment, l’équipe a construit des agents qui mènent eux-mêmes ce type de recherche — par exemple entraîner un modèle fort à partir de la seule supervision d’un faible — et a trouvé qu’ils surpassaient des chercheurs humains à budget égal. C’es

> **⚠ Limites et parades — Généralisation faible-vers-fort** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Le fort peut imiter les erreurs du faible en paraissant précis. *(source : cours, volet 2, §F ; cours, volet 2, §F, JB8)*
>   **Parade :** Deux superviseurs, l'un faux dans un sens fixe, l'autre au hasard, et une copie entraînée sur les étiquettes vraies comme cas connu. *(source : cours, volet 2, §F, JB8)*
> - **Limite :** Récupérer l'écart peut venir d'idées qui exploitent la structure propre au jeu de données. *(source : cours, volet 2, §F, JB8)*
>   **Parade :** Une tâche à vérité connue, lue sur les items tenus à part où le superviseur se trompe. *(source : cours, volet 2, §F, JB8)*
> - **Limite :** Sur une tâche binaire, contredire partout passe pour une récupération. *(source : cours, volet 2, §F, JB8)*
>   **Parade :** Lire aussi l'accord du fort là où le superviseur a raison. *(source : cours, volet 2, §F, JB8)*
> - **Limite :** Les succès automatisés portent sur des tâches choisies pour être vérifiables ; les tâches floues restent hors de portée. *(source : cours, volet 7, F·40)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** Contre le sandbagging, la supervision faible ne tient que si l'entraînement est indistinguable du déploiement. *(source : cours, volet 7, F·26)*
>   **Parade :** aucune connue ; on le dit.

### Insertion n°9, après la ligne 743 de la v3.5

> Ancre : incapacité, pas une imitation (M5).

> ⚠ **Limites et parades** : cas connu → volet M, M5 (fin de section) ; jeu tenu à part → volet M, M4 (après « Le jeu tenu à part ») *(v3.6)*

### Insertion n°11, après la ligne 758 de la v3.5

> Ancre : En pratique — les coup probes (Roger). Pour le versant « moniteur bon marché sur les internals », le but était de détecter une catégorie d’actions catastrophiques qu’on ne peut pas collecter naturellement (un modèle qui tente une prise de contrôle). La méthode des probes entraînées off-policy y répo

> **⚠ Limites et parades — Moniteurs du contrôle (moniteur de confiance, sondes en production, agrégation)** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Des angles morts systématiques : sur Opus 4.6, la moitié de quarante attaques conçues à la main ne sont jamais attrapées, et un prompt ciblé répare un angle mort en en dégradant un autre. *(source : cours, volet 7, F·23)*
>   **Parade :** Un ensemble de prompts spécialisés ou une seconde étape coûteuse, et un seuil calibré à 1 % de faux positifs sur des variantes bénignes appariées. *(source : cours, volet 7, F·23)*
> - **Limite :** Le chiffre de sûreté dépend de la force de la red team : un échafaudage optimisé fait passer le score de 0,87 à 0,41. *(source : cours, volet 7, F·24)*
>   **Parade :** Dire quelle red team le chiffre suppose, au moins une red team optimisée composante par composante. *(source : cours, volet 7, F·24)*
> - **Limite :** Menaces diffuses : chaque action est peu incriminante, et des attaques fragmentées passent les moniteurs par instance. *(source : cours, volet 7, F·59 et F·56)*
>   **Parade :** Des moniteurs à état ; pour l'agrégation de preuves internes, dire « I haven't seen that combination measured », jamais « first ». *(source : cours, volet 7, F·56 ; cours, volet 6, §6)*
> - **Limite :** Le rappel dépend du taux de base : un rappel de campagne ne se lit qu'avec le ratio de trafic bénin. *(source : cours, volet 6, §6)*
>   **Parade :** Rapporter le rappel à un taux de faux positifs fixé, avec le ratio de trafic dit. *(source : cours, volet 6, §6 ; cours, volet 2, préambule)*
> - **Limite :** Une sonde en production peut échouer en silence : le silence d'une sonde n'est pas celui du modèle. *(source : cours, volet 3, §3, K70)*
>   **Parade :** Des canaris (positifs connus glissés dans le trafic), un score de dérive, et un échantillon frais jugé chaque mois. *(source : cours, volet 3, §3, K70)*
> - **Limite :** Itérer contre ses détecteurs sélectionne l'évasion. *(source : fiche 19)*
>   **Parade :** Des détecteurs scellés, hors de la boucle : s'ils continuent de se déclencher quand ceux de la boucle se taisent, l'évasion a été sélectionnée. *(source : fiche 19)*
> - **Limite :** Le modèle de menace suppose les capacités de l'attaquant bornées et connues, et les événements rares s'estiment mal. *(source : cours, volet 4, AI Control)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** Après un entraînement à l'évasion, des captures qui survivent ne disent rien si l'entraînement n'a pas mordu. *(source : cours, volet 2, §G, K76)*
>   **Parade :** L'entraînement doit d'abord faire tomber les captures du moniteur de texte, et la sonde doit avoir attrapé avant. *(source : cours, volet 2, §G, K76)*

### Insertion n°13, après la ligne 767 de la v3.5

> Ancre : canal hors du texte.

> ⚠ *(v3.6)* Ce quart est un chiffre de red team : il dépend de la force du saboteur supposé — sur cinq environnements SHADE-Arena, un échafaudage d'attaque optimisé composante par composante a fait tomber le score de sûreté de 0,87 à 0,41 *(source : cours, volet 7, F·24)*. Parade : dire quelle red team le chiffre suppose, au moins une red team optimisée composante par composante, avec l'ablation de chaque composante *(source : cours, volet 7, F·24)*.

### Insertion n°15, après la ligne 777 de la v3.5

> Ancre : des captures de la sonde ne dirait rien.

> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») ; cas connu → volet M, M5 (fin de section) *(v3.6)*

### Insertion n°17, après la ligne 785 de la v3.5

> Ancre : et si les portes plantées ensuite marchent encore (M5).

> ⚠ *(v3.6)* Même validé par ce cas connu, un zéro borne la sonde gardée fixe, pas ce que portent les activations : selon un rapport, après un RL, des sondes neuves hors domaine se dégradent quand une sonde neuve dans le domaine reste quasi parfaite — le concept aurait quitté la direction générale *(source : rapport d'antériorité 3 du 2 octobre, The Obfuscation Atlas — rapport ; explication du 2 octobre, §3)*. Parade : extraire aussi une sonde neuve sur l'agent entraîné, avec un jeu d'indices disjoint, comme mesure séparée *(source : programme, parties 3 et 8 ; passation, §5.2 et §5.5)*.

### Insertion n°19, après la ligne 803 de la v3.5

> Ancre : En pratique — StrongREJECT (Souly et al.), pour la mesure. Ce travail répond à un problème de méthode : comment mesurer le succès d’un jailbreak sans se faire tromper par le non-refus ? Le benchmark évalue le préjudice par la capacité de nuire réellement extraite — la réponse jailbreakée est-elle ut

> **⚠ Limites et parades — Red-teaming** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Sans budget fixé, « rien trouvé » dit seulement qu'on n'a pas assez cherché. *(source : cours, volet M, M7)*
>   **Parade :** Un budget fixé d'avance, rapporté avec le résultat. *(source : cours, volet M, M7)*
> - **Limite :** Une porte dérobée reste muette sans son déclencheur : une red team boîte noire ou un jeu fixe la manquent. *(source : cours, volet M, M5 ; cours, volet 7, F·35)*
>   **Parade :** Un jumeau propre, entraîné sur des données auditées, et une porte plantée exprès comme cas connu. *(source : cours, volet M, M4 et M9)*
> - **Limite :** Mesurer le non-refus au lieu du préjudice. *(source : cours, volet 2, §H)*
>   **Parade :** Le préjudice réellement extrait, ou différentiel, noté à l'aveugle. *(source : cours, volet 2, §H ; cours, volet 2, §H, G1)*
> - **Limite :** Un jeu qui ne sépare rien fait concorder tous les classements. *(source : cours, volet 2, §H, G1)*
>   **Parade :** Le modèle nu doit montrer un uplift, et un filtre affaibli exprès plus de préjudice que sa version complète. *(source : cours, volet 2, §H, G1)*
> - **Limite :** Une red team faible fait paraître la défense sûre. *(source : cours, volet 7, F·24)*
>   **Parade :** Une red team optimisée composante par composante, avec l'ablation de chaque composante. *(source : cours, volet 7, F·24)*
> - **Limite :** Entraîner sur les attaques trouvées peut apprendre au modèle à mieux reconnaître son déclencheur. *(source : fiche 15)*
>   **Parade :** aucune connue ; on le dit.

### Insertion n°21, après la ligne 810 de la v3.5

> Ancre : **Ce qui existe déjà.** « Anthropic's constitutional-classifiers paper » a jugé son filtre surtout par une chasse aux contournements, sans en trouver d'universel, et en a mesuré le coût en refus. Une chasse compte des contournements ; ton expérience mesurerait ce qu'ils rapportent de plus qu'un mote

> ⚠ *(v3.6)* La formule « sans en trouver d'universel » rapporte le nul d'une chasse : une borne à son budget, pas une absence *(source : cours, volet M, M5 et M7)*. Parade : un budget fixé d'avance, rapporté avec le résultat *(source : cours, volet M, M7)* ; et juger le filtre aussi par le préjudice différentiel, avec un filtre affaibli exprès comme cas connu, comme le fait l'expérience de ce cas *(source : cours, volet 2, §H, G1)*.

### Insertion n°23, après la ligne 824 de la v3.5

> Ancre : **Le cas connu.** Un jeu qui ne sépare rien ferait aussi concorder les classements. Le modèle nu, sans filtre, doit donc montrer un uplift, et le filtre affaibli plus de préjudice que sa version complète ; sinon le jeu ne classe rien.

> ⚠ **Limites et parades** : cas connu → volet M, M5 (fin de section) *(v3.6)*

### Insertion n°25, après la ligne 832 de la v3.5

> Ancre : **À l'oral.** *« I'd bet refusal rates misrank the filters I'd test, judged on uplift, the help an attacker can't get elsewhere. I'd rank the filters twice, by refusal rate and by differential harm — harm with the model minus harm without it; if the two rankings agreed within the noise of a replayed

> **⚠ Limites et parades — Classifieurs de sûreté (filtres)** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Empoisonnement : environ 32 exemples suffisent, quelle que soit la taille du jeu, et certaines portes ont échappé à des jeux de test red team fixes. *(source : cours, volet 7, F·35 ; cours, volet M, M9)*
>   **Parade :** Un jumeau propre réentraîné sur des données auditées, un second pour borner l'écart dû au hasard, et un filtre empoisonné exprès comme cas connu. *(source : cours, volet M, M4 et M9)*
> - **Limite :** Le jumeau propre ne donne qu'une borne large, qui signale moins. *(source : cours, volet M, M4)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** Un jeu canari ne contient pas le déclencheur inconnu de l'attaquant. *(source : cours, volet M, M5)*
>   **Parade :** Comparer au jumeau propre, face à une porte connue. *(source : cours, volet M, M9)*
> - **Limite :** Une chasse aux contournements compte des contournements ; un taux de refus ne dit pas ce que le filtre retire à l'attaquant. *(source : cours, volet 2, §H, G1)*
>   **Parade :** Classer les filtres deux fois, par taux de refus et par préjudice différentiel. *(source : cours, volet 2, §H, G1)*
> - **Limite :** Placé dans l'entraînement, un classifieur incite le modèle à l'éviter. *(source : fiche 3)*
>   **Parade :** Le modifier pour ne pas inciter l'évasion, et ne jamais entraîner contre lui. *(source : fiche 3 ; fiche 17)*

### Insertion n°27, après la ligne 838 de la v3.5

> Ancre : En pratique — Constitutional AI (Anthropic). Le but était de rendre un modèle inoffensif sans dépendre massivement d’humains étiquetant des contenus nuisibles. La méthode y répond en deux temps : on donne au modèle une « constitution » (un ensemble de principes), on lui fait critiquer puis réviser s

> ⚠ *(v3.6)* Le « feedback de l'IA » fait d'un modèle le juge de l'entraînement, et un juge d'entraînement se fait exploiter *(source : programme, partie 8)*. Parade : un juge d'entraînement distinct du juge scellé d'évaluation, des métriques d'audit tenues à part, et une surveillance de la longueur et des motifs de flatterie *(source : programme, partie 8)* ; voir l'encadré « Juges LLM », volet 6, §2.

### Insertion n°29, après la ligne 840 de la v3.5

> Ancre : En pratique — l’unlearning mis à l’épreuve (Deeb et Roger). Le but était de vérifier une promesse fragile : l’unlearning retire-t-il vraiment l’information des poids, ou la masque-t-il ? La méthode de ré-élicitation y répond directement : on désapprend un savoir dangereux (mesuré par un benchmark co

> **⚠ Limites et parades — Désapprentissage et ré-élicitation** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Masquer n'est pas retirer : sur l'information de pré-entraînement, les taux de récupération dépassent 88 %. *(source : cours, volet 10, Deeb et Roger)*
>   **Parade :** La ré-élicitation contre une référence jamais entraînée, au même budget, avec un modèle connu pour masquer comme cas connu ; dire une borne, « not elicitable at this budget ». *(source : cours, volet M, M4 et M5 ; cours, volet 2, §I)*
> - **Limite :** Un petit fine-tuning peut enseigner : des moitiés de faits liés s'enseignent l'une l'autre. *(source : cours, volet M, M9)*
>   **Parade :** Des faits construits indépendants, et la référence jamais entraînée. *(source : cours, volet 2, §I ; cours, volet M, M9)*
> - **Limite :** Ne pas lire n'est pas être absent : après désapprentissage, le logit lens ne lit plus rien quand retirer une direction par couche rend 64,7 % ; des sondes échouent sur un modèle qui reste jailbreakable. *(source : cours, volet 10, Łucki et al. ; cours, volet 10, Deeb et Roger)*
>   **Parade :** Trancher par une intervention, jamais par une lecture. *(source : cours, volet 10, Łucki et al. ; fiches, partie C)*
> - **Limite :** Le réentraînement sur des faits indépendants ne vaut que pour des faits à faible fuite, pas pour des capacités. *(source : cours, volet 10, Deeb et Roger)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** Le masquage sélectif des gradients n'est montré que sur de petits modèles. *(source : cours, volet 2, §I, JB10)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** Le désapprentissage au niveau des activations « has yet to yield competitive results ». *(source : fiche 5)*
>   **Parade :** aucune connue ; on le dit.

### Insertion n°31, après la ligne 868 de la v3.5

> Ancre : méthode au moins, un fine-tuning sur des exemples sans rapport rendait l'essentiel de la capacité retirée.

> ⚠ **Limites et parades** : cas connu → volet M, M5 (fin de section) ; jeu tenu à part → volet M, M4 (après « Le jeu tenu à part ») *(v3.6)*
