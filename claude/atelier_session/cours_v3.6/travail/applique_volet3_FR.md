# Insertions appliquées — volet3 — FR

### Insertion n°1, après la ligne 901 de la v3.5

> Ancre : La première direction part d’une question préalable à toutes les autres : que sait faire ce modèle ? On ne peut pas raisonner sur le risque sans le savoir, et c’est plus difficile qu’il n’y paraît, pour deux raisons vues au Volet 2. D’abord, le score brut sur un benchmark trompe : ce qui compte est 

> ⚠ **Limites et parades** : évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; juges LLM → volet 6, §2 (après « La loi de déplacement ») *(v3.6)*

### Insertion n°3, après la ligne 921 de la v3.5

> Ancre : > *« I'd bet elicitation gains differ across models enough that their score-versus-effort curves cross, so one effort level would misrank them. If the order stayed the same at every effort level, while a model known to underperform on a bare prompt rose with effort, I'd drop the bet. »*

> ⚠ *(v3.6)* Ce point vient d'une évaluation de sabotage dont le Risk Report d'août concède lui-même les limites (§2.16) : des évaluations non tirées des vrais chemins de risque, une tâche secondaire dans le prompt, des modèles probablement conscients d'être évalués (fiche 3). Parade : une élicitation à budget fixé d'avance, rapportée comme une borne (cours, volet M, M7 ; cours, volet 2, §B, K63) ; contre le modèle qui se retient, deux versions d'un environnement, tirées au hasard, qui ne diffèrent que par des indices de réalisme notés par un discriminateur, avec un organisme dressé à se cacher comme cas connu (cours, volet 2, §B, K63).

### Insertion n°5, après la ligne 931 de la v3.5

> Ancre : peut faire confiance à ce qu’un modèle dit de lui-même — et la réponse honnête est « pas par défaut », ce qui justifie les méthodes white-box.

> ⚠ **Limites et parades** : évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; auto-rapport et introspection → volet 5, partie II, A, sujet 13 ; chaîne de pensée comme moniteur → volet 11, réponse 43 ; organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») *(v3.6)*

### Insertion n°7, après la ligne 951 de la v3.5

> Ancre : > *« I'd bet a chain of thought names what changed the answer where the task needs the chain. If chains on tasks that need them named a planted hint no more often than chains on easy tasks, while chains told to cite it were scored as naming it, I'd drop the bet. »*

> ⚠ *(v3.6)* Le test des indices mesure ce que la chaîne verbalise, pas le calcul qui a produit la réponse : une chaîne qui ne nomme pas l'indice n'est pas, par là, un raisonnement caché (fiche 17). Parade : dire « not verbalized », jamais « hidden reasoning », et mesurer la surveillabilité comme un ratio — le verbalisé contre l'interne ou les actions —, par une perturbation graduée de la chaîne (fiche 17 ; cours, volet 11, réponse 43).

### Insertion n°9, après la ligne 955 de la v3.5

> Ancre : La troisième direction adopte le pari du Volet 2 : plutôt que de garantir l’alignement, on suppose le modèle potentiellement non fiable et l’on conçoit un déploiement qui reste sûr quand même. On y range le monitoring (un modèle faible mais de confiance surveille un modèle fort mais non fiable), la 

> ⚠ *(v3.6)* Ce canal a ses propres façons d'échouer : au seuil d'un moniteur, des sondes rappellent 43 % à 1 % de faux positifs, contre 55 % pour le meilleur moniteur LLM (cours, volet 7, F·51), et itérer contre ses détecteurs sélectionne l'évasion (fiche 19). Parade : rapporter le rappel à 1 % de faux positifs face à une baseline boîte noire à coût égal (cours, volet 7, F·50 ; cours, volet 5, sujet 1), et garder des détecteurs scellés, hors de la boucle : s'ils continuent de se déclencher quand ceux de la boucle se taisent, l'évasion a été sélectionnée (fiche 19).

### Insertion n°11, après la ligne 955 de la v3.5

> Ancre : La troisième direction adopte le pari du Volet 2 : plutôt que de garantir l’alignement, on suppose le modèle potentiellement non fiable et l’on conçoit un déploiement qui reste sûr quand même. On y range le monitoring (un modèle faible mais de confiance surveille un modèle fort mais non fiable), la 

> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; autoencodeurs en langage naturel → volet 4, La vague récente sur la cognition du modèle ; auto-rapport et introspection → volet 5, partie II, A, sujet 13 ; juges LLM → volet 6, §2 (après « La loi de déplacement ») *(v3.6)*

### Insertion n°13, après la ligne 975 de la v3.5

> Ancre : > *« I'd bet a production probe would fail silently mostly through input drift, and that the drift would show before its recall on planted canaries fell. If canary recall fell first, with the drift score still at its baseline, though that score did rise on new task families, I'd drop the bet. »*

> ⚠ *(v3.6)* Le constat de la carte Fable 5 oppose la sonde à deux instruments qui ont leurs propres limites : le NLA peut confabuler (fiche 18), les réponses aux questions de suivi dépendent de leur formulation (fiche 3), et les trois mesures n'y sont que « weakly positively correlated » (fiche 2) ; il montre que la sonde se tait, pas laquelle des lectures a raison. Parade : trianguler, et dire quelle mesure a fondé quel chiffre (cours, volet 5, sujet 4 ; cours, volet M, M4), en mesurant les contrôles par un instrument indépendant du NLA (fiche 18).

### Insertion n°15, après la ligne 975 de la v3.5

> Ancre : > *« I'd bet a production probe would fail silently mostly through input drift, and that the drift would show before its recall on planted canaries fell. If canary recall fell first, with the drift score still at its baseline, though that score did rise on new task families, I'd drop the bet. »*

> ⚠ *(v3.6)* Le juge plus lent qui étiquette l'échantillon frais est lui-même un instrument, ici non audité : un juge a des erreurs systématiques (cours, volet 6, §2), et un juge qui lit le raisonnement se laisse persuader — environ 1 % des actions signalées avec la chaîne de pensée, environ 50 % sans, pour un seul moniteur (fiche 3). Parade : un juge scellé et un audit humain d'environ 200 items stratifiés, l'accord rapporté (programme, partie 3), qui juge les actions, leurs sorties et les messages, pas le texte qui précède l'action (passation, §5.1).

### Insertion n°17, après la ligne 981 de la v3.5

> Ancre : C’est aussi, et c’est important pour toi, l’endroit où le roadmap range l’honnêteté. La logique est la suivante : si l’on pouvait amener un modèle à rapporter fidèlement ce qu’il sait, on disposerait d’un signal de supervision fiable « gratuit » — d’où le rattachement de l’honnêteté à l’oversight. C

> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; débat et supervision évolutive → volet 2, §E (après « En pratique — Debate ») ; généralisation faible-vers-fort → volet 2, §F (après « En pratique — l'automatisation ») ; élicitation non supervisée → volet 2, §E (fin du cas d'application K52) *(v3.6)*

### Insertion n°19, après la ligne 1001 de la v3.5

> Ancre : > *« I'd bet a deception probe that's perfect on its test set would also fire on the test context itself. If it stayed at its baseline on honest transcripts written as tests, while a separate evaluation-awareness probe read them as tests, I'd drop the bet. »*

> ⚠ *(v3.6)* La sonde de défection a été validée sur une porte implantée : la meilleure de 1 000 directions aléatoires y atteint déjà 95,3 %, et la saillance peut venir de l'insertion (fiche 15). Un succès sur organisme borne l'instrument ; pour un modèle devenu trompeur de lui-même, aucune parade connue (cours, volet M, M5).

### Insertion n°21, après la ligne 1007 de la v3.5

> Ancre : désalignement (l’attaque révèle une fragilité interne), ce qui en fait un bon endroit pour montrer qu’on distingue les deux familles de risque.

> ⚠ **Limites et parades** : red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») ; classifieurs de sûreté → volet 2, §H (fin du cas d'application G1) *(v3.6)*

### Insertion n°23, après la ligne 1027 de la v3.5

> Ancre : > *« I'd bet separating the user's channel from the documents' would stop injections that give orders, but not indirect ones that only make a harmful action look natural. If both families fell equally under channel separation, when an undefended agent had executed both, I'd drop the bet. »*

> ⚠ *(v3.6)* L'« immunité quasi totale » rapportée par le papier Mind Viruses a été mesurée par des modèles juges, qui peuvent compter un écho poli comme une adoption (cours, volet 3, §6, K13), et une défense ne vaut que contre la red team qui l'a éprouvée : une red team faible la fait paraître sûre (cours, volet 7, F·24). Parade : ne compter que les étapes réellement agies et refaire noter un échantillon à la main (cours, volet 3, §6, K13) ; dire quelle red team le chiffre suppose, au moins une red team optimisée composante par composante, avec l'ablation de chaque composante (cours, volet 7, F·24).

### Insertion n°25, après la ligne 1031 de la v3.5

> Ancre : La sixième direction regroupe des problèmes plus jeunes. Le désapprentissage (unlearning) vise à retirer un savoir dangereux, avec le contrôle décisif vu au Volet 2 : la ré-élicitation (le savoir revient-il par finetuning plus vite que chez un modèle jamais entraîné ?). La gouvernance multi-agents s

> ⚠ *(v3.6)* La ré-élicitation ne tranche que dans un sens : si le savoir ne revient pas plus vite, on signe une borne, « not elicitable at this budget », jamais une absence (fiches, partie C) ; et un petit fine-tuning peut enseigner au lieu de révéler (cours, volet M, M9). Parade : des faits construits indépendants, la référence jamais entraînée au même budget, et un modèle connu pour masquer comme cas connu (cours, volet M, M4, M5 et M9 ; cours, volet 2, §I) ; pour des capacités plutôt que des faits à faible fuite, aucune parade connue ; on le dit (cours, volet 10, Deeb et Roger).

### Insertion n°27, après la ligne 1031 de la v3.5

> Ancre : La sixième direction regroupe des problèmes plus jeunes. Le désapprentissage (unlearning) vise à retirer un savoir dangereux, avec le contrôle décisif vu au Volet 2 : la ré-élicitation (le savoir revient-il par finetuning plus vite que chez un modèle jamais entraîné ?). La gouvernance multi-agents s

> ⚠ **Limites et parades** : désapprentissage et ré-élicitation → volet 2, §I (après « En pratique — l'unlearning mis à l'épreuve ») ; juges LLM → volet 6, §2 (après « La loi de déplacement ») *(v3.6)*

### Insertion n°29, après la ligne 1079 de la v3.5

> Ancre : Pour parler des préoccupations actuelles et pas seulement des fondations, voici les grands chantiers récents, regroupés par thème. Le Volet 4 racontera plusieurs de ces papiers un par un ; ici, l’objectif est que tu saches de quoi l’équipe parle en ce moment.

> ⚠ **Limites et parades** : pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; juges LLM → volet 6, §2 (après « La loi de déplacement ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; détecteurs fine-tunés → volet 7, F·29 ; auto-rapport et introspection → volet 5, partie II, A, sujet 13 ; oracles d'activation → volet 10, fiche LatentQA ; autoencodeurs en langage naturel → volet 4, La vague récente sur la cognition du modèle ; organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; généralisation faible-vers-fort → volet 2, §F (après « En pratique — l'automatisation ») *(v3.6)*

### Insertion n°31, après la ligne 1083 de la v3.5

> Ancre : C’est sans doute le thème le plus actif, et celui qui touche directement tes travaux. Le problème est que les évaluations peuvent mentir parce que le modèle se sait évalué. Les system cards récents (à partir de Sonnet 4.5) y répondent de deux façons : en rendant les mises en situation plus réalistes

> ⚠ *(v3.6)* Cet ancrage reste un appui faible tant que la spécificité n'est pas établie : dans la carte d'Opus 4.8, des vecteurs de contrôle au contenu arbitraire bougent le comportement dans le même sens, plus faiblement, et chaque direction dégrade les sorties ; à force 0,01×, la carte de Fable 5 rend la dégradation négligeable, mais ses contrôles restent « comparable or smaller » sur l'axe du désalignement (fiche 2). Parade : une direction aléatoire de même norme n'est que le nul de spécificité, et le dommage ne s'écarte qu'à dégradation appariée — un sous-espace spécifique contre des sous-espaces aléatoires de même rang, à dégradation appariée, avec une baseline de prompt et une courbe dose-réponse (fiche 2 ; cours, volet M, M4 ; cours, volet 5, sujet 4).

### Insertion n°33, après la ligne 1087 de la v3.5

> Ancre : Deuxième thème majeur, et l’autre versant de ta pertinence. L’équipe explore la détection de mensonge et l’élicitation d’honnêteté sur un testbed varié d’organismes modèles malhonnêtes (entraînés à mentir de façons différentes). Côté introspection, une série de travaux d’interprétabilité cherchent à

> ⚠ *(v3.6)* Sur ce banc d'organismes malhonnêtes, sondes de vérité et pilotage d'honnêteté ont fait moins bien qu'un simple prompt (cours, volet 7, F·62 — un fait à ne dire à l'oral qu'une fois versé à la base) ; et des détecteurs de mensonge fine-tunés plafonnent à 0,70-0,75 d'AUROC hors distribution, à peine mieux qu'un prompt (fiche 7). Parade : une validation croisée par types de mensonge tenus à part, battre une baseline de prompt à coût égal, et publier le résultat si le détecteur ne la bat pas (fiche 7 ; cours, volet 5, sujet 1 ; cours, volet 7, F·29).

### Insertion n°35, après la ligne 1087 de la v3.5

> Ancre : Deuxième thème majeur, et l’autre versant de ta pertinence. L’équipe explore la détection de mensonge et l’élicitation d’honnêteté sur un testbed varié d’organismes modèles malhonnêtes (entraînés à mentir de façons différentes). Côté introspection, une série de travaux d’interprétabilité cherchent à

> ⚠ *(v3.6)* Ces lectures ne sont pas un auto-rapport du modèle : l'oracle d'activation est une copie fine-tunée qui lit, pas le modèle interrogé (cours, volet 10, LatentQA), et oracles comme NLA peuvent confabuler (fiche 18) ; l'introspection émergente reste rare et peu fiable, environ 20 % de détection pour Opus 4.1 (fiche 11). Parade : tester le décodeur sur des variantes fine-tunées à comportement connu, jamais vues, et corroborer par une méthode indépendante en gardant le décodeur à part (fiche 18) ; pour l'introspection, une vérité-terrain par injection de concept (fiche 11).

### Insertion n°37, après la ligne 1091 de la v3.5

> Ancre : Troisième thème : peut-on auditer un modèle pour y débusquer un objectif caché ? On l’a vu au Volet 2 avec le jeu d’audit sur organisme à objectif dissimulé ; l’effort se prolonge avec des benchmarks d’audit (AuditBench) qui donnent une vérité-terrain pour comparer les protocoles d’investigation, et

> ⚠ *(v3.6)* La vérité-terrain d'AuditBench est celle de 56 modèles à comportements implantés (cours, volet 7, F·27) : construit n'est pas naturel (fiches, partie B, piège 5), et dans le jeu d'audit d'origine, l'objectif était décrit en clair dans les documents synthétiques, le pipeline le rendant « artificially easy to discover » (fiche 16). Parade : ne conclure que sur les protocoles d'audit, et sur le fond avec des modèles sans organisme (programme, partie 8) ; contre l'organisme trop facile et l'écart entre implanté et naturel, aucune parade connue ; on le dit (fiche 16 ; passation, §5.2).

### Insertion n°39, après la ligne 1097 de la v3.5

> Ancre : solutions plus efficaces mais moins alignées que des agents seuls. Et dans le registre de l’oversight automatisé, des chercheurs automatisés menant de la recherche weak-to-strong surpassent des humains à budget égal — ce qui ramène la question de la confiance qu’on peut accorder à un travail qu’on n

> ⚠ *(v3.6)* Ce succès porte sur une tâche délibérément vérifiable, les tâches plus floues restant hors de portée (cours, volet 7, F·40), et un chercheur automatisé peut ralentir ou orienter la recherche sans être détecté par un moniteur prompté zero-shot (cours, volet 7, F·60). Parade : des sous-tâches à vérité vérifiable, une re-dérivation humaine échantillonnée, la détection du sandbagging des chercheurs automatisés et une baseline humaine à budget égal (cours, volet 5, sujet 11) ; pour les tâches floues, aucune parade connue ; on le dit.

### Insertion n°41, après la ligne 1101 de la v3.5

> Ancre : Cinquième thème : agir à la source. Le travail Teaching Claude Why montre qu’entraîner le modèle, par synthetic document finetuning, sur des récits fictionnels alignés avec la constitution réduit son taux de désalignement sur les honeypot evals. Et la défense anti-jailbreak continue d’évoluer avec u

> ⚠ *(v3.6)* Ce taux est lu sur des pots de miel : un pot de miel ne sépare pas un modèle qui le lit comme factice d'un modèle qui se retient (fiche 3), ceux qui sont tenus à part ne sont peut-être pas représentatifs (fiche 12), et le travail ne mesure ni ne contrôle la conscience d'évaluation (programme, partie 1). Parade : des métriques d'audit tenues à part, jamais entraînées, comme le fait ce travail (fiche 12), et l'écart mesuré avec et sans inhibition de la conscience d'évaluation, à dégradation appariée et contre des vecteurs de contrôle (fiches, partie C) ; pour le pot de miel lu comme factice, aucune parade connue ; on le dit.

### Insertion n°43, après la ligne 1107 de la v3.5

> Ancre : Et toi, dans tout cela, tu te branches à un endroit précis et défendable : à la charnière de la direction « évaluer l’alignement » (versant cognition, avec l’eval-awareness) et de la sous-direction « honnêteté » de l’oversight (la lignée probing de la vérité). Tes outils — concept vectors mean-diff,

> ⚠ *(v3.6)* Ce que cette phrase déroule a ses limites, à dire avec elle : la décomposition SAE passe par le SAE ouvert de Goodfire, qui laisse 86,8 % de la variance au résidu, où vit le signal lu — un échec des features ne sépare donc pas « absentes du dictionnaire » et « dictionnaire qui perd trop » ; et la baisse obtenue au rang trois ne s'est pas reproduite sur des générations fraîches jugées en entier, l'ablation adoucissant tout verdict négatif, lu à travers une fenêtre tronquée (README du dépôt). Parade : lire le signal sur la reconstruction et sur le résidu, juger la réponse entière, extraire sur un jeu disjoint, et comparer au témoin sans pression et à la direction d'un concept rival, à dégradation appariée (README du dépôt ; cours, volet M, M4) ; pour trancher entre les deux lectures du SAE, aucune parade connue ; on le dit.

### Insertion n°45, après la ligne 1107 de la v3.5

> Ancre : Et toi, dans tout cela, tu te branches à un endroit précis et défendable : à la charnière de la direction « évaluer l’alignement » (versant cognition, avec l’eval-awareness) et de la sous-direction « honnêteté » de l’oversight (la lignée probing de la vérité). Tes outils — concept vectors mean-diff,

> ⚠ **Limites et parades** : pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; dictionnaires et SAE → volet 4, Towards puis Scaling Monosemanticity ; ablation et projection → volet 2, §D (après « La méthode ») ; contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme ») ; dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») *(v3.6)*
