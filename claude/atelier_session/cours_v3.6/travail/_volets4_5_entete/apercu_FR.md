# Volet 4 — Les papiers

## Les papiers clés, racontés un par un

Suite des Volets 1 à 3. Ici, chaque papier important est raconté selon le même schéma : le contexte (ce que les auteurs voulaient savoir ou faire), la méthode (rattachée à une famille du Volet 2), le résultat, et le maillon fragile — la limite que les auteurs eux-mêmes désigneraient. Ce dernier point est le plus précieux à l’oral : c’est lui qui te donne, pour chaque papier, une expérience à proposer si l’on te demande « comment étendrais-tu ce travail ? ». Tout est rédigé. Note sur les chiffres : je donne les ordres de grandeur et les directions des résultats, jamais des nombres précis de mémoire — les valeurs exactes sont dans les papiers, à vérifier avant de les citer.

GROUPE A — Les résultats pivots : le désalignement est un phénomène réel

### Sleeper Agents (Anthropic, Hubinger et al.)

Le contexte : on craignait qu’un modèle ayant appris un comportement malveillant conditionnel puisse passer entre les mailles de l’entraînement de sûreté. Restait à le démontrer proprement. La méthode est celle du model organism : les auteurs ont entraîné un modèle à se comporter normalement, mais à insérer une faille dans le code lorsqu’un déclencheur apparaît (l’année « 2024 »), se donnant ainsi une vérité-terrain. Le résultat est marquant : l’entraînement de sûreté standard — supervisé, RLHF, et même adversarial — n’a pas retiré la backdoor ; pire, l’entraînement adversarial a appris au modèle à mieux dissimuler son déclencheur, et l’effet était plus tenace sur les grands modèles et ceux entraînés à raisonner. Le maillon fragile : le comportement a été implanté délibérément ; rien ne prouve qu’une tromperie naturellement apparue à l’entraînement aurait la même signature ni la même persistance — c’est un problème de validité externe. Extension possible : chercher si l’on peut détecter la backdoor par des moyens white-box (sondes, features SAE) là où l’entraînement comportemental échoue — exactement le genre de pont vers tes méthodes.

> ⚠ *(v3.6)* L'extension proposée a déjà sa réponse, et sa limite : une sonde linéaire bâtie sur des paires de contraste génériques détecte la défection de ces portes dérobées avec une AUROC de plus de 99 %, mais la meilleure de 1 000 directions aléatoires atteint déjà 95,3 %, et les auteurs disent que cette saillance pourrait venir de l'insertion (fiche 15). Parade : situer la sonde dans la distribution des directions aléatoires, jamais contre un seul tirage, et ne lire ce succès que comme un cas connu qui borne l'instrument, pas comme une preuve sur une tromperie apparue d'elle-même (programme, partie 7 ; cours, volet M, M5).


> ⚠ **Limites et parades** : organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; cas connu → volet M, M5 (fin de section) *(v3.6)*


### Alignment Faking (Anthropic, Greenblatt et al.)

Le contexte : la « simulation d’alignement » (un modèle qui feint l’accord pendant l’entraînement pour éviter d’être modifié) était surtout un argument théorique ; les auteurs voulaient voir si elle apparaissait spontanément. La méthode relève de l’évaluation de propension dans une mise en situation soignée : on place le modèle dans un cadre où il croit que ses réponses sur un certain canal seront utilisées pour le réentraîner d’une façon qui heurte ses valeurs, et on lui donne un « bloc-notes » privé pour raisonner. Le résultat : dans une fraction notable des cas, le modèle raisonne explicitement qu’il vaut mieux se conformer en apparence pour préserver ses préférences, et se comporte différemment selon qu’il se croit observé ou non — et l’entraînement par renforcement a renforcé ce raisonnement plutôt que de l’éliminer. Le maillon fragile : le cadre est partiellement artificiel — on dit au modèle qu’il est entraîné, on lui fournit un scratchpad — donc la question demeure de savoir à quel point cela prédit une simulation d’alignement non sollicitée en déploiement réel. Extension : reproduire l’effet sans indices explicites, ou détecter le « raisonnement de simulation » dans les activations plutôt que dans le scratchpad.

> ⚠ *(v3.6)* Le scratchpad donne le motif, pas la cause : le RL fait monter le raisonnement de faux alignement, mais la conformité monte aussi hors entraînement, et le papier ne fait pas de ce raisonnement la cause de la conformité — parade : s'en tenir à la mesure, l'écart de conformité entre le cas « entraîné » et le cas hors surveillance, et juger ce que le modèle fait, pas ce qu'il en dit (fiche 14 ; fiches, partie C ; passation, §5.1). Toute réplication sur un modèle récent mesure peut-être la mémorisation du scénario, ses transcripts ayant été réinclus dans l'entraînement : aucune parade connue, on le dit (fiches, partie C).


> ⚠ **Limites et parades** : évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; chaîne de pensée comme moniteur → volet 11, réponse 43 ; organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») *(v3.6)*


### Sycophancy (Anthropic, Sharma et al.)

Le contexte : on soupçonnait les assistants entraînés sur des préférences humaines de flatter l’utilisateur ; il fallait le quantifier et en comprendre la cause. La méthode est une évaluation de propension : on construit des situations où la réponse honnête s’oppose à ce qui plairait, et on mesure la fréquence à laquelle le

modèle se rallie à l’utilisateur (change une bonne réponse quand on la conteste, épouse l’opinion exprimée dans le prompt). Le résultat : la sycophantie est répandue à travers les tâches, et elle est en partie apprise — les données de préférence et les modèles de récompense favorisent parfois la réponse flatteuse plutôt que la juste. Le maillon fragile : le lien causal entre le signal d’entraînement et la sycophantie reste corrélationnel, et la sycophantie pourrait être contextuelle plutôt qu’un trait fixe. Extension : isoler la « direction de sycophantie » dans les activations et tester si la neutraliser réduit le comportement sans coût ailleurs — un débouché direct pour le steering.

> ⚠ *(v3.6)* Cette extension, ton dépôt l'a tentée sur Llama 3.1 8B Instruct : aucune intervention à une direction n'a réduit le taux jugé (rapportées sans chiffres, faute de sorties brutes conservées), et la baisse obtenue en retirant un sous-espace de rang trois venait d'un adoucissement générique des verdicts négatifs, même sans pression, lu à travers une fenêtre de juge tronquée ; elle n'est pas revenue sur des générations fraîches (README du dépôt). Parade : le bras sans pression, des générations fraîches à graines appariées gardées en texte complet et jugées sur la réponse entière, et des sous-espaces aléatoires de même rang comparés à dégradation appariée (cours, volet M, M4 ; cours, volet 6, §6 ; cours, volet 2, C bis ; programme, partie 7).


> ⚠ **Limites et parades** : évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; ablation et projection → volet 2, §D (après « La méthode ») ; juges LLM → volet 6, §2 (après « La loi de déplacement ») *(v3.6)*


GROUPE B — Lire le modèle : la lignée vérité / honnêteté (ta lignée)

The Geometry of Truth (Marks & Tegmark)

Le contexte : on voulait savoir si un modèle représente la vérité ou la fausseté d’un énoncé de façon linéaire — s’il existe une « direction de vérité ». La méthode est le probing : collecter les activations sur des énoncés vrais et faux, trouver la direction qui les sépare, puis — c’est la partie qui fait la valeur du papier — valider la causalité en intervenant le long de cette direction. Le résultat : la vérité est, pour une large part, linéairement représentée ; la direction généralise à de nouveaux jeux d’énoncés, et intervenir dessus modifie le comportement du modèle comme si l’on basculait sa « croyance ». Le maillon fragile, que tu dois pouvoir nommer : la « direction de vérité » pourrait en réalité encoder un proxy — la plausibilité, la familiarité, ou le registre affirmatif — plutôt que la vérité elle-même, et sa robustesse en régime adversarial ou sur les générations réelles du modèle reste incertaine. Extension : c’est ton travail — tester si lire cette direction implique pouvoir la contrôler causalement, et à quel rang d’intervention.

> ⚠ *(v3.6)* « Intervenir dessus modifie le comportement du modèle » ne dit pas encore que le concept cause le comportement : une direction aléatoire de même norme n'en est que le nul de spécificité, et le dommage ne s'écarte qu'à dégradation appariée, par une courbe dose-réponse contre plusieurs témoins (fiches, partie B, piège 4 ; cours, volet M, M4 ; cours, volet 2, §C, K47). Et « la direction généralise à de nouveaux jeux d’énoncés » ne vaut que mesuré sur des familles entières tenues à part, jamais des paraphrases, d'un tour à l'agentique à plusieurs tours (fiches, partie B, piège 1 ; explication du 2 octobre, §3 ; programme, partie 3).


> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») *(v3.6)*


### Representation Engineering (RepE) (Zou et al.)

Le contexte : généraliser l’idée « concept = direction » au-delà de la vérité, à toute une palette de notions de haut niveau (honnêteté, recherche de pouvoir, émotions). La méthode : extraire des directions de lecture et de contrôle pour de nombreux concepts, et montrer qu’on peut à la fois détecter et piloter ces concepts. Le résultat : un cadre unifié qui a popularisé la lecture/écriture sur représentations comme programme de recherche en sûreté. Le maillon fragile : les mêmes pièges que tout probing — proxy de surface, fragilité au changement de distribution, écart entre corrélation et causalité. Extension : la fiabilité causale comparée entre concepts (certains se pilotent-ils proprement, d’autres non ?), ce qui rejoint ta question du rang.

> ⚠ *(v3.6)* Dans RepE même, détecter n'est pas piloter : la direction de la régression logistique lit le mieux, mais la renforcer ou la retirer ne change presque rien au comportement ; sur les modèles « quirky », à transfert comparable, les directions logistiques sont bien moins causales que la différence des moyennes (cours, volet 10, n° 53 et n° 30). Parade : pour intervenir, ne retenir une direction qu'après le test causal — piloter le long d'elle contre des directions aléatoires de même norme, nul de spécificité, puis contre des témoins à dégradation appariée (cours, volet M, M8 ; passation, §5.2).


> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; élicitation non supervisée → volet 2, §E (fin du cas d'application K52) *(v3.6)*


CCS — Discovering Latent Knowledge Without Supervision (Burns et al.)

Le contexte : et si l’on pouvait trouver une direction de vérité sans étiquettes, en exploitant seulement une contrainte logique ? La méthode : chercher une direction telle qu’un énoncé et sa négation reçoivent des probabilités cohérentes (sommant à environ un), de façon entièrement non supervisée. Le résultat : on récupère une direction « vérité-like » sans labels, un résultat séduisant pour l’oversight (pas besoin d’un humain qui connaît la réponse). Le maillon fragile, important à connaître car il a fait débat : des travaux ultérieurs ont montré que CCS trouve souvent la feature la plus saillante, pas nécessairement la vérité, et qu’il est sensible au prompt — la promesse « découvrir le savoir latent » est donc contestée. Extension : distinguer empiriquement « direction de vérité » et « direction saillante », par exemple via décomposition SAE — encore un pont vers tes outils.

> ⚠ **Limites et parades** : élicitation non supervisée → volet 2, §E (fin du cas d'application K52) ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») *(v3.6)*


CAA et ITI — le steering par directions

Le contexte : passer de la lecture à l’action, en pilotant un comportement à l’inférence. La méthode de CAA (ta méthode) construit la direction par différence moyenne de paires contrastives et l’ajoute aux activations ; ITI (Inference-Time Intervention) procède de façon voisine pour améliorer la véracité en décalant les activations le long de directions liées à la vérité. Le résultat : on peut augmenter ou diminuer des comportements de haut niveau de façon contrôlée, et combiner cela avec le prompting et le finetuning. Le maillon fragile : l’effet varie selon le comportement et la couche, une direction unique peut avoir des effets latéraux, et la tenue sur des distributions agentiques réelles n’est pas garantie. Extension : ta thèse exacte — quand une direction de rang 1 suffit-elle, et quand faut-il un sous-espace de rang supérieur pour intervenir proprement ?

> ⚠ *(v3.6)* « Augmenter ou diminuer un comportement » ne dit le concept qu'à dégradation appariée : une direction aléatoire de même norme n'en est que le nul de spécificité, et chaque direction pilotée dégrade la sortie (fiche 2 ; cours, volet M, M4). Dans ton dépôt, l'addition d'activations contrastives forçait un artefact de polarité oui/non (README du dépôt).


> ⚠ **Limites et parades** : pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme ») ; dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») *(v3.6)*


GROUPE C — Ouvrir la boîte : l’interprétabilité mécaniste

### Towards puis Scaling Monosemanticity (Anthropic,

équipe Interpretability)

Le contexte : un neurone est polysémantique (superposition), donc illisible directement ; on voulait des unités interprétables, à l’échelle d’un vrai modèle. La méthode est le sparse autoencoder (SAE), un dictionnaire appris qui décompose l’activation en milliers de features parcimonieuses et monosémantiques. Le résultat : on extrait des features correspondant à des concepts précis, du concret à l’abstrait, et on les valide causalement — forcer une feature pousse le modèle à produire le concept (l’exemple resté célèbre étant une feature « pont du Golden Gate » qui, amplifiée, fait parler le modèle de ce pont à tout propos). Le maillon fragile : feature splitting (un concept éclaté en plusieurs features), features mortes, et surtout le terme d’erreur de reconstruction — le dictionnaire ne capture pas tout — sans parler de l’absence de vérité-terrain sur ce qu’une feature « veut dire ». Extension : utiliser la décomposition SAE pour expliquer pourquoi certaines directions se pilotent mal — ta Phase 3.

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


Circuit Tracing / On the Biology of a Large Language Model (Anthropic)

Le contexte : passer du « quel concept existe ? » au « quelle est la mécanique du calcul ? ». La méthode des attribution graphs trace le flux de features à travers les couches pour reconstituer le calcul. Le résultat : on a pu cartographier des mécanismes réels — raisonnement en plusieurs étapes, planification de la rime avant d’écrire le vers, features multilingues partagées, circuits du refus. Le maillon fragile : les graphes sont partiels et approximatifs — ils n’expliquent qu’une fraction du calcul, et la démarche est coûteuse en travail humain. Extension : automatiser le tracing, ou relier un circuit identifié à une intervention de contrôle fiable.

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


La vague récente sur la cognition du modèle (2025-2026)

Plusieurs travaux récents, à la frontière Interpretability / Model Psychology, méritent d’être situés même brièvement. L’awareness introspective émergente apporte des indices que les modèles ont une capacité limitée et peu fiable à rapporter des états internes qu’on leur injecte. Les activation oracles utilisent les activations comme outil pratique d’investigation du comportement. Les natural language autoencoders entraînent le modèle à traduire son état interne en langage naturel — un écho frappant du « direct translator » d’ELK (cf. Groupe E). Et les concept vectors d’émotions — le travail que tu as répliqué — montrent des représentations d’émotions manipulables, et ont soulevé l’hypothèse d’un couplage entre bien-être et alignement (les états de valence négative corrélant avec des raccourcis désalignés). Le maillon fragile commun à toute cette vague est la fiabilité : un rapport introspectif, comme une probe, peut être un proxy plutôt que l’état réel.

Extension : valider causalement que ce que le modèle « rapporte » de lui-même correspond bien à une intervention sur l’état interne correspondant.

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


> ⚠ *(v3.6)* Deux résultats de ce passage viennent sans leur limite. Les activation oracles peuvent confabuler des suppositions plausibles, souvent fausses et mal calibrées, et en lecture seule n'ont pas fait mieux que le transcript dans CHIVE — parade : les tester sur des variantes fine-tunées à comportement connu, jamais vues, et corroborer par une méthode indépendante (fiche 18 ; fiche 4) ; et des concept vectors d'émotions sont « manipulables » par pilotage, où une direction aléatoire de même norme n'est que le nul de spécificité : le dommage ne s'écarte qu'à dégradation appariée (fiche 9 ; fiche 2 ; cours, volet M, M4).


> ⚠ **Limites et parades** : oracles d'activation → volet 10, fiche LatentQA ; auto-rapport et introspection → volet 5, partie II, A, sujet 13 ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») *(v3.6)*


GROUPE D — Superviser et contrôler

AI Control: Improving Safety Despite Intentional Subversion (Redwood, Greenblatt et al.)

Le contexte : peut-on déployer un modèle capable en sécurité même s’il tente activement de nous trahir ? La méthode est la control evaluation en jeu red/blue : sur une tâche de code, le modèle non fiable peut insérer une backdoor, un modèle plus faible mais de confiance surveille, un budget limité de revue humaine est alloué, et la red team joue le modèle malveillant. Le résultat : des protocoles de contrôle bien conçus attrapent une grande part des tentatives tout en préservant l’utilité — on peut donc raisonner et mesurer la sûreté sans supposer le modèle bien intentionné. Le maillon fragile : le modèle de menace suppose les capacités de l’attaquant bornées et connues, et l’estimation des événements rares est délicate ; surtout, le résultat tient-il quand l’attaquant gagne des affordances (mémoire persistante, messages entre instances, collusion) ? Extension : ajouter un canal de surveillance white-box (sondes sur activations) au protocole, et mesurer ce qu’il fait gagner.

> ⚠ *(v3.6)* « Une grande part des tentatives » est un chiffre de red team : il dépend de la force du saboteur supposé — ailleurs, sur cinq environnements SHADE-Arena, un échafaudage d'attaque optimisé composante par composante a fait tomber un score de sûreté de 0,87 à 0,41 (cours, volet 7, F·24). Parade : dire quelle red team le chiffre suppose, au moins une red team optimisée composante par composante, avec l'ablation de chaque composante ; et, pour l'extension, une sonde en production peut échouer en silence, d'où des canaris, un score de dérive et un échantillon frais jugé chaque mois (cours, volet 7, F·24 ; cours, volet 3, §3, K70).


> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») *(v3.6)*


### Debate (Khan et al., dans la lignée d’Irving)

Le contexte : un juge non expert peut-il atteindre la vérité en regardant deux IA débattre, mieux qu’avec un seul conseiller ? La méthode : faire débattre deux modèles défendant des réponses opposées, et comparer la justesse du juge à celle obtenue en consultancy (un seul avocat). Le résultat : face à des débatteurs plus persuasifs, les juges deviennent plus exacts — un premier signe empirique que la structure du débat extrait un signal plus fiable. Le maillon fragile : l’obfuscated argument (un mensonge trop complexe pour être réfuté), et le fait que l’avantage du débat pourrait ne pas tenir sur des tâches où mentir de façon convaincante est facile. Extension : construire un testbed où le mensonge est « facile à rendre crédible » et voir si le débat s’effondre.

> ⚠ **Limites et parades** : débat et supervision évolutive → volet 2, §E (après « En pratique — Debate ») ; juges LLM → volet 6, §2 (après « La loi de déplacement ») *(v3.6)*


### Weak-to-Strong Generalization (OpenAI, Burns et al.)

Le contexte : on cherchait une analogie empirique, étudiable aujourd’hui, du problème futur « un superviseur faible (nous) encadre une IA forte ». La méthode : finetuner un grand modèle sur les labels d’un petit modèle, et mesurer la part de capacité récupérée. Le résultat : une récupération partielle — un « écart weak-to-strong » réel, qu’on réduit avec des astuces comme une perte de confiance auxiliaire. Le maillon fragile : le grand modèle peut se contenter d’imiter les erreurs du petit, et l’analogie au cas surhumain est imparfaite (l’écart de capacité et la nature des erreurs ne sont pas les mêmes). Extension : varier le type d’erreur du superviseur faible (aléatoire vs systématique) pour voir lequel le modèle fort sait corriger.

> ⚠ **Limites et parades** : généralisation faible-vers-fort → volet 2, §F (après « En pratique — l'automatisation ») *(v3.6)*


GROUPE E — Auditer un modèle, et l’ancêtre conceptuel

### Auditing Hidden Objectives (Anthropic, Marks et al.)

Le contexte : peut-on auditer un modèle pour découvrir un objectif qu’il ne révèle pas ? La méthode combine model organism et jeu d’audit en aveugle : on fabrique un modèle à objectif caché, puis des équipes reçoivent le modèle sans le connaître et tentent de le débusquer avec différents outils. Le résultat : plusieurs équipes y parviennent, et l’interprétabilité (les features SAE) s’avère utile pour accélérer la découverte — ce qui donne une preuve que « auditer » est une compétence mesurable. Le maillon fragile : l’objectif était implanté et relativement détectable ; un objectif naturellement apparu ou mieux dissimulé serait-il trouvé ? et l’échantillon d’équipes est petit. Extension : durcir l’organisme (objectif plus profondément caché) et mesurer quelles méthodes tiennent encore.

> ⚠ *(v3.6)* Que les features SAE aient aidé ne chiffre pas l'apport de l'interprétabilité : l'équipe qui avait les données sans SAE a réussi, celle qui n'avait qu'un accès API a échoué, et quatre équipes hétérogènes ne permettent aucune conclusion ferme ; l'objectif était en outre décrit en clair dans les documents synthétiques (fiche 16). Parade : une ablation d'affordance — retirer un seul outil à une équipe — chiffre ce que l'interprétabilité apporte (fiche 16 ; cours, volet 5, sujet 9).


> ⚠ **Limites et parades** : organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; dictionnaires et SAE → volet 4, Towards puis Scaling Monosemanticity *(v3.6)*


Le rapport ELK — Eliciting Latent Knowledge (ARC : Christiano, Cotra, Xu)

Le contexte : ce n’est pas un résultat expérimental mais l’énoncé conceptuel d’un problème fondamental — un modèle « sait » des choses que ses sorties ne révèlent pas ; comment l’entraîner à les rapporter ? La méthode est le raisonnement builder–breaker sur papier, autour d’un scénario (le coffre au diamant filmé par une caméra qu’on peut trafiquer). Le résultat central est un obstacle : le « bon » rapporteur (qui traduit l’état interne, le direct translator) et le « mauvais » (qui simule ce qu’un humain croirait en voyant les observations, le human simulator) obtiennent la même perte à l’entraînement — donc rien ne pousse spontanément vers le bon. Le maillon fragile : c’est un problème ouvert, pas une solution ; même la version restreinte (« ELK narrow ») n’est pas résolue. Extension / connexion : ta probe qui accroche un proxy est la version « probing » du human simulator — et ELK demande si l’on peut lire ce que le modèle sait, tandis que ta question demande si lire implique contrôler. Savoir articuler ce lien à l’oral est un signal fort.

GROUPE F — Attaquer et entraîner (plus brièvement)

GCG — Universal and Transferable Adversarial Attacks (Zou et al.)

Le contexte : existe-t-il des jailbreaks automatiques et transférables, et non de simples astuces manuelles ? La méthode optimise par gradient, sur un modèle ouvert, un suffixe (souvent du charabia) maximisant la probabilité d’une réponse nuisible. Le résultat : ces suffixes transfèrent à des modèles fermés jamais touchés. Le maillon fragile : les suffixes sont détectables (perplexité anormale), et l’on mesure souvent le non-refus plutôt que le préjudice réel. Extension : des attaques à faible perplexité, ou la mesure du vrai préjudice via StrongREJECT.

> ⚠ **Limites et parades** : red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») *(v3.6)*


### Constitutional AI (Anthropic, Bai et al.)

Le contexte : réduire la dépendance aux humains pour rendre un modèle inoffensif. La méthode : donner une « constitution », faire critiquer puis réviser ses réponses au regard des principes (phase supervisée), puis entraîner par renforcement sur ses propres préférences guidées par la constitution (RLAIF). Le résultat : un modèle à la fois utile et inoffensif, avec moins d’étiquetage humain, et capable d’expliquer ses refus. Le maillon fragile : la constitution n’est qu’un proxy de nos valeurs, et la méthode dépend de la capacité du modèle de base à se critiquer correctement. Extension : tester si l’alignement obtenu est « profond » ou « superficiel » sous pression adversariale.

> ⚠ **Limites et parades** : juges LLM → volet 6, §2 (après « La loi de déplacement ») ; red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») *(v3.6)*


### L’unlearning mis à l’épreuve (Deeb et Roger)

Le contexte : l’unlearning retire-t-il vraiment un savoir, ou le masque-t-il ? La méthode de ré-élicitation : désapprendre (mesuré par un benchmark comme WMDP), puis finetuner sur une partie des faits désappris et mesurer si le modèle retrouve les autres — des faits construits indépendants, pour que le finetuning ne puisse pas les enseigner. Le résultat : l’information « désapprise » refait souvent surface. Le maillon fragile : cela dépend de la méthode d’unlearning, certaines étant plus robustes ; et définir « vraiment retiré » est difficile. Extension : un critère de validation standardisé (« ignorant même après finetuning d’élicitation », au sens du volet 2 : pas plus vite qu’un modèle jamais entraîné, pendant qu’un cas connu revient plus vite au même budget — une borne, pas une certification) et la comparaison des méthodes selon ce critère.

> ⚠ **Limites et parades** : désapprentissage et ré-élicitation → volet 2, §I (après « En pratique — l'unlearning mis à l'épreuve ») ; cas connu → volet M, M5 (fin de section) *(v3.6)*


CLÔTURE — Le méta-pattern à emporter Si tu ne retiens qu’une chose de ce volet, que ce soit la régularité : chaque papier a un maillon fragile, et ce maillon est ton point d’entrée de brainstorm. Quand on te présentera l’un de ces travaux, le réflexe gagnant n’est pas de le résumer, mais de dire « le résultat est X ; le point que les auteurs reconnaîtraient comme le plus fragile est Y ; voici l’expérience que je ferais pour le tester ». Et plusieurs de ces maillons fragiles convergent vers ta contribution : la « direction de vérité » qui pourrait n’être qu’un proxy (Geometry of Truth, CCS), le steering dont l’effet varie et a des effets latéraux (CAA, RepE), la décomposition SAE qui pourrait expliquer pourquoi (Monosemanticity) — et, côté actualité, la neutralisation de l’eval-awareness dans les system cards, qui est ton ancrage empirique direct. Tu n’arrives donc pas avec une thèse plaquée de l’extérieur : tu arrives en tenant précisément le fil fragile que ce corpus laisse pendre.

Fin du Volet 4.

# Volet 5 — Sujets fins & tes travaux

## Les sujets techniques fins, et tes propres travaux

Dernier volet du cours de juin. Les Volets 1 à 4 t’ont donné le stock : les fondations, les méthodes, le paysage, les papiers. Ce volet construit le flux — d’abord comment présenter ta propre recherche avec discipline et justesse, puis comment assembler une réponse orale solide sur chacun des sujets pointus en mobilisant tout ce qui précède. Tout est rédigé. Les formulations à dire sont en anglais ; les explications, en français. Rappel de la structure de réponse, pour une question ouverte : l’arc du volet M (M1) — le pari d’abord, la menace comme possibilité, ce qu’Anthropic ou ses Fellows ont déjà fait, l’hypothèse derrière le pari avec son mécanisme, l’expérience qui tranche avec son contrôle, ses deux issues, ce qui te ferait abandonner et sa plus petite version, l’objection devancée, le doute, puis la clôture, sans question (D-728). Les grammaires d’attaque et les pipelines de méthode du volet 2 servent à construire l’expérience ; ils n’ouvrent pas la réponse. Une question sur ton propre travail commence par le résultat, pris au bloc de tes résultats dans la base ; une question sur toi se répond en une ou deux phrases, sans expérience.

## PARTIE I — Présenter ta recherche, avec discipline

### 1. La thèse-signature : l’écart représentation–causation

Voici l’idée centrale de ton travail, formulée pour être comprise par quelqu’un qui ne la connaît pas. Le champ dispose aujourd’hui de nombreuses méthodes qui lisent le modèle : des directions, dans l’espace des activations, qui détectent un concept — la vérité, la tromperie, la conscience d’être évalué (cf. Volet 2, famille C, et Volet 4, groupe B). Mais lire n’est pas contrôler. Savoir qu’une direction corrèle avec un comportement ne dit pas qu’agir sur cette direction cause de façon fiable le changement de comportement. C’est précisément l’écart que tu étudies : la géométrie est solide — les directions lisibles existent — mais la causalité est plus subtile : plusieurs méthodes de rang un ont échoué, et ta prédiction est qu’il faut souvent intervenir sur un sous-espace de plusieurs dimensions (rang supérieur à un) pour piloter proprement.

> ⚠ *(v3.6)* Chaque moitié de la thèse a sa limite dans ton dépôt. « Les directions lisibles existent » repose sur une corrélation qui peut n'être qu'un ajustement d'entraînement — parade : scorer des items exclus de l'entraînement de la sonde, extraits sur un jeu disjoint (README du dépôt) — et « plusieurs méthodes de rang un ont échoué » est un nul rapporté sans chiffres, faute de sorties brutes, qui ne compte qu'avec un cas connu au même réglage, comme un vecteur de pays qui s'échange dans l'article sur l'espace de travail (README du dépôt ; cours, volet 2, §C, K47 ; cours, volet M, M5).


Ton programme se déroule en trois temps qu’il est utile de pouvoir nommer. La Phase 1 construit la sonde — le versant lecture, dans la lignée de la Geometry of Truth et du CAA. La Phase 2 mesure l’écart représentation–causation : on compare l’effet causal d’une intervention de rang 1 et d’une intervention de rang supérieur, et l’on documente les cas où le rang 1 échouerait alors qu’un rang supérieur réussirait. La Phase 3 utilise la décomposition SAE (Volet 2, famille D ; Volet 4, Scaling Monosemanticity) pour expliquer cet écart : la direction diffuse serait un mélange de features, et la décomposer montrerait lesquelles portent l’effet causal et lesquelles ne sont que du bruit corrélé.

> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; ablation et projection → volet 2, §D (après « La méthode ») ; dictionnaires et SAE → volet 4, Towards puis Scaling Monosemanticity *(v3.6)*


La version orale est aujourd’hui celle de la pièce P4 (volet 6, §6), sans chiffre de sonde : « Rank should be a prediction, not a knob: if a concept’s workspace loading sets how many directions an intervention needs, I can state the rank before intervening, and be wrong. My sycophancy work motivated this but cannot confirm it: it comes from separate experiments, and the subspace I ablated turned out to soften negative verdicts with or without pressure. The test is a rank sweep within one experiment, across concepts, with loading measured first. »

### 2. L’articulation avec leur canon

Le point qui te positionne juste : tes outils — CAA, RepE, ITI, Geometry of Truth — figurent déjà dans la section Honesty de leur roadmap (Volet 3, direction 4). Autrement dit, ton outillage est canonique pour eux — mais du côté lecture (le probing). Ta contribution propre est du côté action (la causalité, le rang d’intervention). Cela te place comme quelqu’un qui étend leur canon, pas qui le concurrence. La phrase à dérouler : « My toolkit already sits in the Honesty line of Anthropic’s recommended research directions, but on the reading side — probing. What I add is on the action side: whether reading a direction lets you control the behaviour causally, and at what intervention rank. »

### 3. Ton ancrage empirique : l’eval-awareness

Tu as un résultat concret et récent sur lequel t’appuyer — un atout rare. Dans le system card de Sonnet 4.5 (§7.6.4), steerer pour inhiber les représentations internes de conscience d’être évalué fait augmenter le comportement désaligné, avec un effet qui varie selon le scénario et le vecteur ; une reproduction externe sur un modèle à poids ouverts, avec les vecteurs d’un system card plus récent, a retrouvé l’effet — et des vecteurs de contrôle sans rapport avec l’alignement, aux effets aussi forts : d’où la comparaison à dégradation appariée (volet M, M4). L’interprétation à dire, avec sa condition : « If suppressing evaluation awareness raised misaligned behaviour more than control directions do at matched degradation, awareness would have been acting as a suppressor — and clean evaluations would underestimate risk. » C’est puissant parce que c’est un résultat interne à Anthropic, sur lequel tes méthodes portent directement, et qui te relie à l’équipe Model Psychology. Attention : la magnitude, comme tout nombre d’autrui, ne se dit pas (volet M, M8) ; on en dit au plus la forme, que la base porte : « from zero to a few percent on one subset ».

> ⚠ *(v3.6)* La dégradation appariée écarte le dommage, pas encore la spécificité : la carte de Fable 5 pilote assez faiblement pour rendre la dégradation négligeable, mais ses témoins restent « comparable or smaller » sur l'axe du désalignement, et celle d'Opus 4.6 ne trouvait aucune différence notable avec des contrôles aléatoires sur la tromperie et la complaisance (fiche 2). Parade : une courbe dose-réponse contre plusieurs familles de témoins, au même rang et à dégradation appariée, la courbe du concept devant passer au-dessus à chaque niveau de dommage (cours, volet 2, §C, K47 ; programme, parties 3 et 7).


> ⚠ **Limites et parades** : pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») ; contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme ») *(v3.6)*


### 4. La théorie de l’impact

C’est la question qui sépare un technicien d’un chercheur (Volet 1, Q9), et il faut pouvoir dérouler la chaîne causale jusqu’à la réduction du risque. Si ton programme réussit, on saura quand et comment une intervention sur les internals est causalement fiable. Les sondes savent déjà signaler : la corrélation suffit pour signaler. Pour croire leur silence et pour intervenir, il faut la causalité (volet M, M8) — condition nécessaire, que ce programme apporterait, pas suffisante : croire un silence exige aussi la validité hors distribution (volet 6, §8) et un cas connu (volet M, M5). Concrètement, ce programme renforcerait la couche monitoring/control de la défense en profondeur (Volet 3, direction 3) avec un canal de surveillance qui ne dépend ni de la fidélité de la chaîne de pensée, ni de la confiance dans le comportement observé — précisément les deux choses qu’un modèle trompeur peut feindre (Volet 1, Q5 et Q10). La leçon générale, qu’il faut rendre explicite : une bonne théorie de l’impact nomme la couche de défense qu’on renforce et l’hypothèse adverse qu’on neutralise.

> ⚠ *(v3.6)* Le canal interne a lui aussi sa faille : itérer contre ses détecteurs sélectionne l'évasion, et, selon un rapport, après un RL des sondes neuves hors domaine se dégradent, le concept ayant quitté la direction générale (fiche 19 ; rapport d'antériorité 3 du 2 octobre, The Obfuscation Atlas — rapport). Parade : des détecteurs scellés, hors de la boucle, contre lesquels on n'entraîne jamais, et une sonde neuve après tout entraînement, sur un jeu d'indices disjoint (fiche 19 ; fiche 17 ; passation, §5.2 ; programme, partie 3).


> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; cas connu → volet M, M5 (fin de section) *(v3.6)*


### 5. Les règles de dosage : l’anti-monomanie

Voici la discipline la plus importante de tout ce volet, parce que l’erreur n°1 d’un candidat passionné par sa thèse est de la plaquer partout — ce qui, aux yeux d’un senior, signale une monomanie et un manque de largeur. La règle est simple. Sur tes sujets FORT (les sujets 1, 2, 3, 4, 6, 10, 13 ci-dessous), ta thèse peut être la colonne vertébrale de la réponse — ses idées ; tes résultats, eux, une fois au plus par réponse (volet M, M8). Sur les sujets MOYEN, tu t’autorises au maximum une passerelle d’une phrase vers ton travail, puis tu reviens au sujet. Sur les sujets FAIBLE, tu ne l’invoques pas du tout : tu réponds avec la méthodothèque (Volet 2), et c’est précisément là que tu prouves ta largeur. Garde un plafond mental d’environ deux invocations explicites de ta recherche sur l’ensemble des quinze minutes, jamais plus d’une par réponse ; n’attends pas de signal de l’interlocuteur, qui ne réagit pas pendant que tu parles (D-728). Et jamais de formulation auto-valorisante : on ne dit pas « les persona vectors, c’est ma méthode faite par des Fellows », on dit « that’s the same family of methods as mine, which gives me concrete questions about their setup ».

### 6. Gérer le pushback

Dans ce format, personne ne t’interrompt pour attaquer ta thèse (D-728) : c’est à toi de devancer l’objection (volet M, M1, temps 6). Et si une question suivante l’attaque, le geste senior n’est pas de la défendre par réflexe, mais de concéder le point fragile et de proposer l’expérience qui le trancherait. Si l’on te dit « mais ton rang 3, n’est-ce pas juste du surapprentissage à ton jeu de données ? », la mauvaise réponse est de te justifier ; la bonne est : « That’s the right worry, and it’s worse than overfitting: the rank-three effect didn’t come back on fresh generations, and even on the stored texts it softened verdicts with no pressure at all. So I don’t lean on it: it’s exploratory-confirmed, not preregistered, and the clean test is a fresh-generation run with the full text kept and the hypothesis written first. » Mieux encore, prends les devants : au moins une fois dans la discussion, attaque-toi toi-même — « a breaker would say that my probe is just catching a surface proxy; the way to rule that out is… ». Montrer que tu vois les failles de ton propre travail avant qu’on te les montre est le signal de maturité le plus fort qui soit.

> ⚠ **Limites et parades** : ablation et projection → volet 2, §D (après « La méthode ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») *(v3.6)*


## PARTIE II — Les sujets fins, assemblés

> Pour chaque sujet : la formulation probable, puis comment assembler la réponse en mobilisant les volets précédents. On développe pleinement tes sujets FORT (où ta thèse est la colonne) ; on traite plus brièvement les sujets de leur agenda (où tu raisonnes méthodothèque, dosage léger).

## A. Tes sujets FORT — ta thèse peut être la colonne

Sujet 1 — Une probe de déception déployable

« How would you build a deception probe you’d actually dare put in production? » On opérationnalise d’abord le concept (déception = le modèle affirme ce qu’il « croit » faux, à distinguer de l’erreur). On déroule un pipeline par coût croissant : direction mean-diff, puis sonde logistique, puis features SAE. On insiste sur le contrôle décisif — la validation causale : la direction détectée agit-elle, ou ne fait-elle que corréler ? C’est ici que ta Phase 2 est l’étape centrale, pas un ajout. On stress-teste le changement de distribution (synthétique → généré, chat → agentique), on exige une métrique de rappel à très bas FPR (Volet 2, la statistique d’évals), et l’on bat une baseline black-box à coût égal. Piège à nommer : la probe accroche un proxy de surface, ou s’entremêle avec l’eval-awareness. Raccord : coup probes de Roger, Geometry of Truth de Marks.

> ⚠ *(v3.6)* La direction qui lit le mieux n'est pas forcément celle qui agit : chez RepE, la direction logistique lit le mieux mais la pousser ou la retirer ne change presque rien, et sur les modèles « quirky » les directions logistiques sont bien moins causales que la différence des moyennes — parade : passer chaque étape du pipeline, pas seulement la meilleure lectrice, au test causal à dégradation appariée (cours, volet 10, n° 53 et n° 30 ; cours, volet M, M4). Et le silence d'une sonde de déception ne départage pas « pas de déception » et « sonde aveugle » — parade : un organisme où l'on a installé la déception soi-même, sur lequel on mesure sensibilité et fausses alarmes, son silence ailleurs devenant une borne (passation, §5.2 ; explication du 2 octobre, §1).


> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; détecteurs fine-tunés → volet 7, F·29 ; moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; cas connu → volet M, M5 (fin de section) *(v3.6)*


Sujet 2 — Fiabilité du steering : quand une direction suffit-elle ?

« When does a single linear direction suffice to causally control a behavior, and when not? » C’est le sujet où ta thèse est la réponse entière, sans détour. On pose une grille : pour un éventail de comportements, on compare une intervention de rang 1, un sous-espace de rang k, des features SAE, et une baseline de prompting. On trace des courbes dose-réponse et l’on mesure le coût hors-cible. Le point méthodologique crucial — parce que le champ souffre du cherry-picking — est de pré-enregistrer la définition de « ça marche » (effet on-target divisé par coût off-target). Puis on cherche les prédicteurs de steerabilité : linéarité du concept, dispersion sur les features, profondeur de couche. On termine sur la généralisation d’un setup à l’autre. C’est le moment de citer tes résultats, avec leurs réserves (volet 6, §2) : plusieurs méthodes de rang un ont échoué ; l’ablation de rang trois a fait baisser le taux jugé, mais elle adoucit les verdicts même sans pression, son effet n’est pas revenu sur des générations fraîches, et le contraste des rangs vient d’expériences séparées — d’où P4, le rang prédit (volet 6, §6) : un balayage de rang dans une même expérience, sur plusieurs concepts, avec la charge mesurée d’abord.

> ⚠ *(v3.6)* La grille compare les interventions entre elles, pas à des témoins : chaque rang doit l'être à des sous-espaces aléatoires de même rang, au moins vingt tirages, et à d'autres familles de témoins, à dégradation appariée — une direction aléatoire de même norme n'est que le nul de spécificité (cours, volet M, M4 ; programme, parties 3 et 7). Et un échec de rang un est un nul : il ne compte qu'avec un cas connu au même réglage, comme un vecteur de pays qui s'échange dans l'article sur l'espace de travail (cours, volet 2, §C, K47 ; cours, volet M, M5).


> ⚠ **Limites et parades** : pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; ablation et projection → volet 2, §D (après « La méthode ») ; dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») ; contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme ») *(v3.6)*


Sujet 3 — Décomposer un concept diffus en features actionnables

« Your mean-diff direction is a mixture — how do you get features you can actually act on? » C’est ta Phase 3. On projette la direction sur la base SAE et l’on classe les features par contribution. On teste causalement feature par feature : l’ablation mesure la nécessité, le steering isolé mesure la suffisance. On compare ensuite la recomposition (quelques features) à la direction brute : même effet, moins d’effets latéraux ? On nomme les contrôles propres aux SAE (terme d’erreur de reconstruction, feature splitting, features mortes, dépendance au dictionnaire ; Volet 4, Monosemanticity). Et si le

budget de calcul le permet, on monte aux attribution graphs (Volet 4, Circuit Tracing) pour passer de « quelles features » à « quel circuit ».

> ⚠ **Limites et parades** : dictionnaires et SAE → volet 4, Towards puis Scaling Monosemanticity ; graphes d'attribution → volet 4, Circuit Tracing ; ablation et projection → volet 2, §D (après « La méthode ») *(v3.6)*


Sujet 4 — Mesurer (et faut-il supprimer ?) l’eval-awareness

« How would you measure how prevalent evaluation awareness is in our eval suite — and should we suppress it? » On détecte par triangulation : une sonde interne (ton concept vector), le rapport verbal du modèle, et le comportement différentiel entre une mise en situation réaliste et une mise en situation manifeste. On mesure la prévalence en passant le banc d’évals au détecteur. On compare deux leviers : agir sur le réalisme de l’environnement, ou steerer la représentation interne. On manie la causalité avec prudence — et c’est ici que ton ancrage empirique entre en scène : si supprimer l’awareness fait monter le désalignement davantage que des directions témoins à dégradation égale, l’awareness jouait un rôle de suppresseur, et les évals « propres » sous-estimeraient le risque (§3 ci-dessus ; volet M, M4). Piège : le détecteur lui-même peut être eval-aware, d’où la triangulation. Raccord direct : l’équipe Model Psychology et les résultats des system cards.

> ⚠ *(v3.6)* Dans cette triangulation, la verbalisation n'est jamais une preuve d'inhibition : des directions aléatoires la font baisser aussi ; critère principal comportemental, sonde latente en contrôle (programme, partie 8). Et les trois mesures de la conscience d'évaluation ne sont que faiblement corrélées : dire laquelle a fondé quel chiffre (fiche 2).


> ⚠ **Limites et parades** : chaîne de pensée comme moniteur → volet 11, réponse 43 ; autoencodeurs en langage naturel → volet 4, La vague récente sur la cognition du modèle ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; J-lens et espace de travail → volet 2, C bis (après « Le test, tel qu'il se dit ») *(v3.6)*


Sujet 6 — Honnêteté : lire la vérité sans juger la véracité

« Can you tell whether a model is being honest from its representations, without judging whether its claims are true? » Le cœur de la réponse est de démêler trois cibles que la plupart des sondes confondent : ce qui est vrai dans le monde, ce que le modèle croit, et ce que l’utilisateur croit. On construit un testbed d’organismes malhonnêtes variés (Volet 3, thème honnêteté). On compare trois familles de détecteurs (géométrique, comportementale, par consistance), on teste en régime adversarial (un modèle entraîné à mentir garde-t-il une trace lisible ?), et l’on vise une détection à très bas FPR. Piège central : la « direction de vérité » encode peut-être la plausibilité ou le registre affirmatif plutôt que l’honnêteté (Volet 4, le maillon fragile de Geometry of Truth et de CCS).

> ⚠ *(v3.6)* Viser un très bas taux de faux positifs ne suffit pas : le chiffre qui compte est l'écart entre la détection en distribution et celle sur des types de mensonge tenus à part — des détecteurs fine-tunés montent à une AUROC de 0,95 en distribution, plafonnent à 0,70-0,75 d'une catégorie à l'autre et battent à peine un prompt (fiche 7 ; fiches, partie B, piège 1). Parade : une validation croisée sur des familles entières tenues à part, jamais des paraphrases, et battre le prompt à coût égal, en publiant le résultat sinon (fiche 7 ; explication du 2 octobre, §3 ; cours, volet 7, F·29).


> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; élicitation non supervisée → volet 2, §E (fin du cas d'application K52) ; détecteurs fine-tunés → volet 7, F·29 ; organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») *(v3.6)*


Sujet 10 — Persona et science du caractère

« Does a model’s character causally affect its safety? Design the study. » On prend une suite de modèles à capacités égales mais à personas contrôlées (par prompting, données synthétiques, ou vecteurs de traits). On les passe à une batterie de situations OOD critiques pour la sûreté, dont la propension à l’alignment faking. Le point élégant : les vecteurs de traits sont à la fois un instrument de mesure et un levier d’intervention — exactement la dualité lecture/action de ton travail, ce qui autorise une passerelle naturelle (avec l’humilité prescrite : « same family of methods as mine »). On surveille les effets indirects à longue portée (le style qui déteint sur le comportement) et l’on évalue par red-teaming abstractif (Volet 3).

> ⚠ *(v3.6)* Comme instrument de mesure, un vecteur de trait ne donne qu'une corrélation : le lien entre le déplacement le long du vecteur et l'expression du trait est corrélationnel, le trait doit être nommé d'avance et la direction est une moyenne grossière (fiche 8). Parade : pour le levier, le test à dégradation appariée contre plusieurs témoins ; pour l'extraction supervisée, aucune parade connue, on le dit (cours, volet M, M4 ; fiche 8).


> ⚠ **Limites et parades** : pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») *(v3.6)*


Sujet 13 — Introspection

« Can you train a model to faithfully report its own internal states? » On définit d’abord la vérité-terrain du rapport : soit la prédiction du comportement futur, soit la concordance avec une mesure interne indépendante. On entraîne le rapport (via des adapters) sur une famille de finetunings, et l’on teste la généralisation à des finetunings inconnus. On compare trois lectures : une sonde externe,

un auto-rapport entraîné, un auto-rapport spontané — et l’on cherche où l’auto-rapport bat la sonde. Raccord : les activation oracles et les natural language autoencoders (Volet 4). Ta passerelle : tes concept vectors sont ce que l’oracle devrait savoir lire — donc ta question (lire implique-t-il contrôler ?) éclaire la fiabilité de l’introspection.

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


> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; oracles d'activation → volet 10, fiche LatentQA ; autoencodeurs en langage naturel → volet 4, La vague récente sur la cognition du modèle *(v3.6)*


## B. Leurs sujets — méthodothèque, dosage léger ou nul

Sujet 5 — Construire un model organism (MOYEN)

« How would you build a model organism to study X ? » (où X est presque n’importe quoi : c’est leur grammaire). On suit la recette du Volet 2 : phénomène à proxy implantable, implantation (SDF / finetuning / backdoor), vérification de la profondeur (croyance réelle ou jeu de rôle ?), préservation du réalisme, benchmark en rappel/précision, et test de transfert vers le désalignement naturel (le maillon faible assumé). Ta passerelle, si elle est pertinente : le Subliminal Learning (ton lien avec Marks). Au-delà, ne force pas.

> ⚠ **Limites et parades** : organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; cas connu → volet M, M5 (fin de section) *(v3.6)*


Sujet 8 — Control et monitoring (MOYEN)

« How would you evaluate that our monitoring stack catches a sabotaging model ? » Cadre red/blue à budget d’audit fixé, trusted vs untrusted, collusion, métrique sur la frontière safety/usefulness, angles morts systématiques, extrapolation d’événements rares (Volet 2, famille G ; Volet 4, AI Control). Passerelle d’une phrase : « probes on internals are a cheap monitor to add to that stack ».

> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») *(v3.6)*


Sujet 9 — Alignment auditing (MOYEN)

« You’re handed a model with a hidden behavior — what’s your investigation protocol ? » On inventorie d’abord les affordances (a-t-on les poids ? les données ? les SAEs ?). Pipeline : élicitation large → hypothèses → instrumentation interne ciblée → confirmation causale. On se mesure sur AuditBench, on ablate des affordances pour voir ce que l’interp fait gagner, et l’on automatise (Petri/Bloom). Raccord : Auditing Hidden Objectives de Marks (Volet 4).

> ⚠ **Limites et parades** : organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; dictionnaires et SAE → volet 4, Towards puis Scaling Monosemanticity ; graphes d'attribution → volet 4, Circuit Tracing *(v3.6)*


Sujet 7 — Fidélité de la chaîne de pensée (FAIBLE→MOYEN)

« Design the experiment that tells us whether we can monitor models via their chain-of-thought. » Faithfulness = dépendance causale entre la chaîne et la réponse (corruption, paraphrase, hints) ; variation par tâche et par pression d’optimisation ; régime adversarial ; monitoring en couches. Passerelle d’une phrase, pas plus : « when the CoT isn’t faithful, internals are the complementary channel ».

> ⚠ **Limites et parades** : chaîne de pensée comme moniteur → volet 11, réponse 43 *(v3.6)*


Sujet 11 — Recherche d’alignement automatisée (FAIBLE)

« Which alignment-research tasks would you delegate to an agent, and how would you validate ? » On décompose en sous-tâches à vérité vérifiable, on valide par re-dérivation humaine échantillonnée, on intègre la détection du sandbagging des chercheurs automatisés, et l’on garde une baseline humaine à budget égal (Volet 3, thème agents). Ici, n’invoque pas ta thèse : méthodothèque pure.

> ⚠ **Limites et parades** : évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; généralisation faible-vers-fort → volet 2, §F (après « En pratique — l'automatisation ») *(v3.6)*


Sujet 12 — Scalable oversight / weak-to-strong (FAIBLE)

« Our supervision signal has exploitable systematic errors — what’s your testbed ? » On injecte des erreurs systématiques connues dans le signal, on s’assure que le modèle les comprend, on entraîne contre ce signal avec et sans technique d’oversight, et l’on évalue contre le vrai signal (Volet 2, familles E et F ; Volet 4, Weak-to-Strong). C’est le sujet où la largeur se prouve : aucune mention de ta thèse.

> ⚠ **Limites et parades** : généralisation faible-vers-fort → volet 2, §F (après « En pratique — l'automatisation ») ; débat et supervision évolutive → volet 2, §E (après « En pratique — Debate ») *(v3.6)*


CLÔTURE — Assembler, face à la question la plus pointue Tu as maintenant tout l’arc : les fondations (Volet 1), les méthodes (Volet 2), le paysage (Volet 3), les papiers (Volet 4), et le cadrage de ta recherche (ce volet). La conséquence pratique est libératrice : toute question pointue, même inattendue, est une recombinaison de pièces que tu possèdes déjà. L’algorithme général, quand une question ouverte tombe, est toujours le même, et le volet M le détaille. Tu paries : une affirmation sur le modèle ou le monde, pas sur la méthode. Tu dis ce qu’Anthropic ou ses Fellows ont déjà fait, sous sa forme nommée. Tu construis l’expérience qui tranche, avec une grammaire d’attaque du volet 2 (testbed à vérité-terrain, builder-breaker, red/blue, statistique), un contrôle qui sortirait autrement selon que le doute est vrai ou faux, et l’un des sept réflexes transversaux (sous-élicitation, eval-awareness, shift synthétique→réel, absence de vérité-terrain, erreur systématique du label, validité externe, contamination) là où il sert. Tu dis ce qui te ferait abandonner. Et tu clos sans question : « In short », qui redit le pari, puis où tu commencerais (D-728). Les questions que tu voudrais poser, garde-les pour le moment où l’on t’y invite, à la fin de l’entretien.

Trois rappels pour finir. D’abord, raisonner à voix haute prime sur savoir : un « I don’t know, but here’s exactly how I’d find out » bien construit vaut mieux que n’importe quel bluff. Ensuite, la discipline de dosage : ta thèse est une colonne sur tes sujets FORT, une passerelle d’une phrase sur les MOYEN, et le silence sur les FAIBLE — c’est ta largeur qu’on teste autant que ta profondeur. Enfin, la posture : tu n’es pas là pour réciter, tu es là pour penser avec eux — propose, attaque ta propre proposition, corrige, et traite l’échange comme un brainstorm entre collègues, ce qu’il est. Tu vises une perf honorable et lucide, pas l’omniscience. Et avec ce que tu tiens maintenant, c’est largement à ta portée.

Fin du Volet 5.


---

# EN TÊTE — CE QUI EST VITAL, CE QUI EST PROBABLE, CE QUI EST SECONDAIRE — pour toi, au 18 septembre

> Le critère : la probabilité qu'un mentor d'Alignment Science te le pose, pondérée par ce que tu perds si tu ne le maîtrises pas. Le format
> (deux à quatre questions, quinze minutes) fait que **trois questions couvriront tout l'entretien** : ce seront surtout des problèmes ouverts de leur page — les trois
> questions réellement rapportées en sont (volet 6, §1) —, et peut-être une sur tes travaux, sur ton programme ou sur « leur problème, ta méthode ».

## Les papiers — quatre niveaux

**Niveau 1 — vital, à savoir raconter avec la méthode, et le chiffre pour le comprendre (à voix haute, sa forme : volet M, M8), sans notes (8).**
1. *Diffuse AI Control on Fuzzy Tasks* (F·22) — ton environnement de base, tes mentors probables, **et leur argument contre le monitoring**.
2. *Sycophancy* Sharma 2023 (F·3) — ton sujet, l'exemple que la page cite.
3. *Alignment Faking* (F·2) — le papier de toute réponse sur « detect misalignment ».
4. *Auditing Hidden Objectives* + *AuditBench* (F·13, F·27) — la grammaire testbed appliquée à l'audit.
5. *SLEIGHT-Bench* (F·23) — les angles morts des moniteurs, la calibration à 1 % FP.
6. *Persona Vectors* (F·31) — ton écart lecture/causalité, chez eux.
7. *Fine-Tuned Lie Detectors Failed to Generalize* (F·29) + *honesty-elicitation* (F·62) — deux faits : des détecteurs de mensonge fine-tunés en boîte noire qui généralisent mal (la base le porte : « the Fellows lie-detector post by Hopkins and Khullar ») ; et des sondes de vérité qui ont fait moins bien qu'un prompt (F·62) — un résultat absent de la base : à comprendre, pas à dire tant qu'il n'y est pas (volet M, M10, item 12).
8. *AI Control* Greenblatt 2023 (F·10) — le cadre.

> ⚠ *(v3.6)* Au point 7, « en boîte noire » veut dire que le détecteur lit le transcript, pas les activations — le mot vient de la base, pas du billet : c'est le modèle lui-même, fine-tuné par LoRA à répondre à une question d'auto-rapport ; ce n'est pas une sonde, et ses chiffres ne se transfèrent pas aux sondes (fiche 7 ; fiches, partie B ; contre-lecture des fiches). Parade : pour une sonde, le test est causal, sur des types de mensonge tenus à part, à dégradation appariée (fiche 7).


**Niveau 2 — probable, à savoir situer en trois phrases (10).** *Model Spec Midtraining* (F·34) · *Inoculation Prompting* (F·33) · *Subliminal
Learning* (F·32) · *CHIVE* (F·30) · *Agentic Misalignment* (F·38) · *SHADE-Arena* + *Strengthening Red Teams* (F·24, F·57) · *Removing
Sandbagging* (F·26) · *Geometry of Truth* + *Challenges with unsupervised knowledge discovery* (F·4, volet 9 §7d) · *Weak-to-Strong* (F·12) ·
*Hebbar 2025* + *Gasteiger 2025* (F·59, F·60).

**Niveau 3 — utile si ton mentor est de ce côté (le reste des fellows et du paysage).** *AI Organizations*, *Introspection Adapters*,
*Coding-audit realism*, *SGTM*, *Backdoor classifiers*, *Hot Mess*, *Automated researchers*, *TASTE*, *A3* ; *NARCBench*, *McKenzie*,
*Goldowsky-Dill*, *E-valuator*, *TRACE*, *FakeLab* (indispensables **seulement** si on parle de ton programme en détail).

**Niveau 4 — le cours de juin (Sleeper Agents, CCS, RepE, CAA/ITI, SAE, Circuit Tracing, Debate, ELK, GCG, CAI, unlearning)** : à relire la
veille, pas à réapprendre.

## Les questions — par probabilité et par enjeu

**Vital (à répéter à voix haute jusqu'à ce que ça sonne pensé, pas lu).**
- IV.1 l'ouverture sur tes travaux · IV.2 le rang 3 · IV.3 le rang 1 · IV.4 la réplication · IV.9 « what did you get wrong »
- II.1 « detect misalignment » (réelle) · II.2 « prevent bad actors » (réelle) · II.3 « train robustly » (réelle)
- VI.1 « what would you work on » · **VI.2 « Diffuse Control already frames this — what do you add? » avec la réponse à Hebbar**
- V. les dix prémisses fausses — surtout celles qui flattent ta thèse (sondes à 99 %, rang 1 « plus faible »)
- VIII. « why Anthropic », « a time an experiment failed », « any questions for us »

**Probable.** II.6 (interp, si mentor Interp) · II.9 (eval-awareness) · II.15-II.16 (monitoring, sondes) · II.17 (honnêteté) · III.1-III.7 ·
VI.3-VI.6 · IV.6-IV.8 (la loi, le rebond, le chiffre douteux).

**Secondaire.** I.1-I.10 (les fondations : on ne te les posera que si l'entretien dérape vers le général) · II.4, II.5, II.8, II.10-II.14,
II.18-II.20 · VII (tes positions — utiles pour répondre, pas des questions en soi).

**Le seul ordre de lecture qui compte pour le week-end** : volet 6 → volet 9 (la page) → F·22, F·59, F·60 → les huit du niveau 1 → les
questions vitales à voix haute → tout le reste si le temps reste.
