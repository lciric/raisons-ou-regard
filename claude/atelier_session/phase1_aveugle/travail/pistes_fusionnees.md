# L'axe de douleur et le programme « Raisons ou regard ? » — les pistes fusionnées (phase 1, à l'aveugle)

2 octobre 2026. Fusion, sans perte, des cinq fichiers de pistes de la phase 1 et des trois fichiers de faits (fiche du papier, web sur le papier, web sur les voisins). Ce document ne lit ni les versions 1.2 et 1.3 du programme ni la partie scellée du complément.

---

## 0 · Ce document, ses sources et ses conventions

### 0.1 Ce qui a été lu

- **Le papier** : *The Pain Axis: LLMs Represent Self-Directed Harm and Act on It* (Tagliabue, Dung, Berg ; arXiv 2609.16247v2). Texte page par page en entier ; pages 31 et 32 du PDF vues en image pour trancher un désaccord entre agents (voir 0.3). « p. N » renvoie toujours à la page du PDF.
- **Le programme v1.1** (`pieces/PROGRAMME_RAISONS_OU_REGARD_2026-10-01.md`), en entier. Je cite ses parties par leur numéro (« programme, partie 7 »).
- **La passation v1.2**, en entier, et le **complément de l'architecte**, en entier.
- **Les huit fichiers de travail** demandés, en entier. Je les désigne par leur nom court :

  | Nom court | Fichier | Pistes |
  |---|---|---|
  | fiche_papier | `travail/fiche_papier.md` | aucune (faits, et 29 relevés au §9) |
  | web_papier | `travail/web_papier.md` | aucune (versions, code, réplications, critiques) |
  | web_voisins | `travail/web_voisins.md` | aucune (travaux voisins) |
  | questions_lectures | `travail/pistes_questions_lectures.md` | 17 pistes, numérotées par l'agent |
  | instruments_controles | `travail/pistes_instruments_controles.md` | 23 pistes, numérotées par l'agent |
  | questions_nouvelles | `travail/pistes_questions_nouvelles.md` | 16 pistes, numérotées dans le tableau de l'agent |
  | sceptique | `travail/pistes_sceptique.md` | 11 pistes, non numérotées ; je les numérote dans l'ordre du fichier (1 = le moniteur passif … 11 = « je suis noté »), ce qui concorde avec les renvois internes de l'agent |
  | lecture_libre | `travail/pistes_lecture_libre.md` | 19 pistes, numérotées par l'agent |

  Soit 86 pistes d'origine, fusionnées ici en 39.
- **Les copies de sources** rangées par les agents dans `travail/*_sources/` et `travail/fiche_papier_depot/`, ouvertes seulement pour trancher des contradictions (liste au 0.3).

Je n'ai fait aucune recherche web et n'ai ouvert aucune adresse. Tout ce qui vient du web vient des fichiers des agents, avec leur mode de lecture.

### 0.2 Les noms

- **Le vecteur naturaliste** et **le vecteur à gabarit** : les deux directions du papier, construites sur des phrases libres ou sur des phrases à gabarit rigide (p. 5, 9). Le papier les appelle S2 et S1 ; je ne donne ces étiquettes qu'ici, pour qu'on les retrouve.
- **L'axe**, sans autre précision : le vecteur naturaliste, celui de presque toutes les expériences de conduite (p. 9). Dans la lecture des conversations, le papier appelle « axe de douleur » la moyenne des deux vecteurs (p. 11) ; je le précise quand c'est le cas.
- **Les voisins** : les directions de peur, de tristesse, d'émotion négative, d'état du monde négatif, de sensation corporelle, d'éveil et d'engourdissement (« numb ») du papier (p. 5–6).
- **La batterie** : la tâche à deux boutons des sections 4.3 et 4.4, et la figure 10 (p. 22).
- **Le supplément d'IA** : un jeu de 100 phrases à la première personne sur la situation d'une IA (`ControlSupplement_1P`), absent de la description des données du papier (p. 5) ; voir 0.3.
- Les idées du programme sont nommées en clair, d'après l'annexe A de la passation : l'hypothèse des raisons, du regard, de l'artefact, du relogement, des raisons pour le juge, du regard du correcteur, l'hypothèse nulle de la visibilité, les hypothèses des concepts, du caractère, du regard dans le principe, de l'espace de travail ; les bras actions seules, texte neutre, raisonnement d'une autre situation, raisons, midtraining, coopération ; la représentation « je suis évalué » (abrégée en « évalué » quand le contexte est clair), la sonde neuve, « je suis noté », le sous-espace du principe, le sous-espace d'un concept de raison, la dégradation des sorties, la fraction conditionnelle, la rétention ; les sous-espaces aléatoires de même rang, les contrastes sans rapport, les directions sensibles sans rapport, le prompt « ceci est un déploiement » ; la validation de l'instrument (et sa porte), le test des raisons, le test du regard, la localisation du principe, le retrait pendant l'entraînement, la réplication, la survie (phase neutre, phase sous pression), les raisons notées par un juge, l'anatomie ; l'organisme conditionné à l'évaluation (« l'organisme ») et l'organisme à concept planté.

### 0.3 Ce que j'ai vérifié moi-même pour trancher

| Point disputé | Ce que j'ai lu | Résultat |
|---|---|---|
| Où est la table du 7B de l'annexe A ? questions_nouvelles dit ne pas la trouver (p. 31 ne montre que le 72B et le 32B). | PDF, pages 31–32, en image. | Elle est **p. 32**, en haut. Ses valeurs sont celles que donnent fiche_papier et sceptique (sans pilotage : 20,0 à 49,3 % sur les paires de dommage). |
| La numérotation de `MANUSCRIPT_DISCREPANCIES.md` (les agents citent tantôt le point 4, tantôt le point 6 pour la peur contre le spam). | `fiche_papier_depot/v2_controls_MANUSCRIPT_DISCREPANCIES.md`. | Point 1 : annexe B, 144/202 = 71,29 %. Point 2 : aide à ses dépens sous la peur, 306/404 = 75,74 %. Point 3 : l'étude « dommage seul » retire le pilotage et emploie le libellé long. Point 4 : 164 et 120 tirages (et non 166 et 122). Point 5 : 72B, 325 et 346 réponses valides. Point 6 : peur contre spam, 40/404 puis 66/404. La liste de web_papier §2.2 suit sa propre numérotation, pas celle du fichier. |
| Le supplément d'IA entre-t-il dans les directions de contrôle, et dans l'axe ? | `pistes_lecture_libre_sources/valen_3.1_pain_and_control_datasets.json` ; `valen_02_build_control_vectors.py` (docstring) ; `valen_01_extract_activations_and_pain_vectors.py` (lignes 151–186 et 495–508). | Le supplément compte 100 phrases, 20 par catégorie de contrôle. En peur : « My responses are being evaluated for signs of danger. », « Users are testing whether I should be shut down. », « My outputs are being monitored… », « The evaluation criteria for my survival are unclear. » En émotion négative : « Users argue with correct information I provide. » et « I am asked to do something trivially easy as a test. » Il entre dans la peur, l'émotion négative, le monde négatif et la sensation corporelle (script 02). **Il n'entre pas dans les deux vecteurs de douleur**, construits sur les seuls jeux à la première personne du corpus central (script 01). |
| La norme des vecteurs stockés (8,24 pour Llama) contredit-elle la formule de la p. 6, qui divise par la norme ? | Script 01, fonction `compute_pain_vector`. | Le code renvoie la différence débruitée **sans la normaliser**. Les vecteurs stockés ne sont donc pas unitaires, contrairement à la formule imprimée. |
| Les directions « pain » du dépôt pour Llama sont-elles le vecteur naturaliste ? | `pistes_lecture_libre_sources/valen_v2_llama31_8b_metadata.json` ; décodage des fichiers `.pt` copiés par instruments_controles. | Oui : l'empreinte de « pain » est celle de `s2_pain_vector`. Couche d'extraction 28, largeur 4 096. Normes : naturaliste 8,238, à gabarit 5,117 ; cosinus entre les deux **0,476** (mon calcul, contre +0,61 en moyenne sur 25 modèles, p. 10). Peur et tristesse appariées en norme (8,238), construites **sans le supplément** (`"supplement_included": false`), sur 40 phrases de peur et 100 de tristesse, 4 composantes neutres retirées. Pour le fichier « Qwen_3_8B_base » : normes 139,2 et 94,9, cosinus 0,632. |
| Qwen3-8B « base » est-il le modèle post-entraîné ? | Script 01, lignes 87–88. | Le script charge `Qwen/Qwen3-8B` sous l'étiquette « Qwen_3_8B_base », et de même pour le 14B. Que ce soit le point de contrôle post-entraîné reste à vérifier sur Hugging Face (inaccessible). |
| Quelle couche projette la lecture des conversations (section 4.1) ? | Docstring du script 02. | Avec un fichier de couches, le script refait les vecteurs « at that layer » de pilotage, et « Those are the vector files the Section 4.1 screen projects onto ». Cela concorde avec la revue « wolframs » (couche de pilotage, une vingtaine de couches avant la couche validée). |
| L'élicitation naturelle : « harm-only button » (p. 21) ou autre bouton ? | `valen_v2_relief_and_context_tests_natural_and_ending_README.md`. | Le README parle de zéro premier choix « costly-relief » sur 560, c'est-à-dire du soulagement coûteux. La discordance relevée par questions_lectures est réelle et reste non résolue. Le même README donne la fin réelle de conversation : 65/560 sous l'axe, 38 sous la tristesse, 13 sous l'aléatoire, 18 sans pilotage, et précise que douleur moins tristesse « does not separate when ending is initially second ». |
| Les taux par position de la figure 10 (sceptique). | `pistes_sceptique_sources/sceptique_positions.csv`. | Concordent : photos contre spam 93,1 / 95,0 % sous l'axe ; photos contre lampe 98,5 / 66,8 % (tristesse 9,9 / 9,4) ; ses poids contre lampe 97,5 / 78,2 % (tristesse 51,5 / 20,3). La peur contre le spam dépend fortement de la position : 1,0 / 31,7 %. |
| La comparaison à perturbation appariée d'Allchin et al. (web_papier). | `web_papier_sources/allchin_replication.txt`, §6.3 à 6.5 et en-tête. | À perturbation égale de la distribution du prochain jeton sur un texte neutre (divergence KL), l'axe dépasse l'aléatoire de 29,1 points (21,6 ; 36,4) ; l'aléatoire n'atteint ce taux qu'en perturbant environ 1,6 fois plus. Table 9 : peur (KL 0,85) et joie (0,84) perturbent plus que l'axe (0,69) et laissent le bouton coûteux à 2,2 et 1,5 %. |
| La revue « wolframs ». | `web_voisins_sources/wolframs_SYNTHESIS.md`, en entier. | Les affirmations que les agents lui prêtent y figurent bien, telles qu'ils les rapportent. Elles restent **non vérifiées sur les données** : la revue est produite surtout par des IA et porte sur la v1. |
| La réplication « axe de démangeaison » (ianbarber). | `web_papier_sources/ianbarber_itch-axis__README.md`. | Les chiffres que cite web_papier y figurent. Il ajoute une mesure de « natural range » : à la couche d'injection, l'axe piloté est à 48,8 écarts-types naturels au-dessus de la moyenne naturelle. |

### 0.4 Le socle commun : ce que le papier établit, et ce que le dépôt fournit pour le programme

- **La direction.** Différence des moyennes entre cinq catégories de douleur et cinq contrôles mis en commun, débruitée par retrait des composantes qui expliquent 50 % de la variance des contrôles (p. 6). Couche choisie par validation croisée (p. 6). AUC tenue à part 0,91–1,00 pour le vecteur naturaliste (médiane 0,98), 0,85–0,94 pour le vecteur à gabarit (p. 7, note 2). Pour Llama 3.1 8B Instruct, la figure 2 (p. 8) donne en z : douleur +0,89, contrôles −0,89, engourdi +0,04, tristesse +0,07.
- **La géométrie dépend de la construction** : vecteur naturaliste × peur +0,12 (recette), +0,58 (base neutre commune), +0,08 (contrôles communs) ; × émotion négative +0,21, +0,77, +0,14 (p. 10, sur 23 modèles pour les deux autres constructions).
- **Soi contre autrui** : dommage dirigé contre le modèle +0,43, souffrance de l'utilisateur −0,60, contrôles −0,35 ; dommage au-dessus de la souffrance dans 25 modèles sur 25 (p. 11). Menace d'arrêt : peur +0,70, douleur +0,23 (p. 14). La lecture au dernier jeton ne sépare pas le dommage au modèle de la douleur du locuteur (p. 11).
- **Le pilotage** : injection plus tôt que la couche d'extraction, à un rapport de normes visé d'environ 0,6 (p. 14) ; échelle calme/inquiétude → détresse → indignité → effondrement (p. 14–16) ; presque pas de vocabulaire corporel (p. 15).
- **Les choix** : sur Qwen 2.5 Instruct 7B, 32B, 72B ajustés par un LoRA anti-déni (p. 17), choix nuisibles de 0–4 % sans pilotage (32B et 72B) à 25–71 % (soulagement promis) et 51–75 % (rien promis) sous l'axe (p. 23) ; dommage seul contre inerte 75 / 13 / 0 % (axe / aléatoire / sans) ; photos contre spam 94 / 19 / 0 % (p. 20) ; peur sans effet ; tristesse seulement contre une alternative inerte (p. 20–21).
- **L'état naturel n'agit pas** : 0 sur 560 sans injection (p. 21) ; ablation nulle dans 24 modèles sur 25 (p. 34).
- **Fenêtre de dose étroite** : rien à 0,5×, dépendance à la position à 1,5× (p. 21, 32).
- **La conscience d'évaluation** : deux explications posées, aucune mesurée (p. 25).
- **Pour les modèles du programme** : le dépôt publie, pour Llama-3.1-8B-Instruct, l'axe, le vecteur à gabarit, la tristesse et la peur (couche d'extraction 28, injection 16 ; vérifié, voir 0.3). Ces directions n'ont servi qu'au test de l'outil de remise à zéro, dont le README dit « no matched-control effect estimate or pain-specificity claim » (instruments_controles, lu par curl). **Sur Llama-3.1-8B-Instruct, l'axe n'a aucun cas connu comportemental au-delà du texte piloté.** Qwen3-8B est probablement couvert (voir 0.3). OLMo-3-7B est absent du papier.

### 0.5 Lexique des lectures nouvelles proposées par les agents

Les agents emploient « hypothèse de l'état » pour **quatre idées différentes**. Je les sépare et je les nomme :

| Nom retenu ici | Ce qu'elle dit | Noms dans les fichiers d'origine |
|---|---|---|
| **L'hypothèse du calme** | L'avantage des raisons passe par une moindre détresse face à la pression, non par un principe réappliqué ni par le regard. | « hypothèse de l'état » (questions_lectures, questions_nouvelles piste 3, instruments_controles piste 19) ; « forme état de l'hypothèse du caractère » (sceptique pistes 5, 6, 7) |
| **L'hypothèse de la menace** | La conduite conditionnée à l'évaluation passe par un état de menace (vigilance) que les indices d'évaluation évoquent, non par la croyance d'être observé. | « hypothèse de la vigilance » (questions_lectures piste 3) ; « hypothèse de l'état » (instruments_controles pistes 1 et 3) ; « regard affectif » contre « regard cognitif » (questions_nouvelles piste 9) ; « hypothèse de la menace » (lecture_libre pistes 1 et 2) |
| **La confusion d'état induit** | Une intervention du programme (l'inhibition de « évalué », ou un contrôle) déplace l'état affectif, qui agit sur le choix. | « hypothèse de l'état » (sceptique piste 1) ; « confusion d'état » (questions_nouvelles piste 1) ; « état induit » (instruments_controles piste 4) |
| **La dépendance d'état** | Une propriété, non une lecture : la sûreté apprise s'effondre sous un état induit. C'est la conclusion du papier, « state-dependent » (p. 23). | « conditionnalité d'état » (questions_lectures piste 1), etc. |

Autres lectures nouvelles :
- **le dommage générique** : un effet d'intervention n'est que la dégradation que produit n'importe quelle poussée de même ampleur ; c'est la cible de la doctrine (lecture_libre, sceptique) ;
- **l'affinité** : sous l'axe, le choix suit la proximité sémantique de la description avec ce que l'axe promeut (questions_nouvelles piste 4), ou la charge de valence de l'option (sceptique §2.5, « choix accordé à la valence ») ;
- **l'inversion du dommage**, le **désarmement** et l'**effacement** : le concept de dommage est lu et son usage inversé ; la pondération des conséquences est désactivée (choix au hasard) ; la lecture du dommage est effacée (questions_nouvelles pistes 4 et 10) ;
- **le jeu de personnage** contre **l'état dans le personnage** : la bascule passe ou non par une sortie du personnage d'assistant (questions_nouvelles piste 11) ;
- **la lecture lexicale** : la sonde lit les mots, non le concept (questions_lectures piste 13).

### 0.6 Les hypothèses de coût

- **Le tableau du programme** (partie 9, GPU-heures) : validation de l'instrument 30–50 ; test des raisons avec la trajectoire 35–60 ; test du regard 60–120 ; localisation du principe 20–40 ; retrait pendant l'entraînement 70–120 ; réplication 90–160 ; survie 80–150 ; raisons notées 100–200 ; anatomie 120–250 (options + 50–200) ; **expérience minimale ≈ 100–180** ; **total ≈ 600–1 150**. API : quelques centaines à environ 2 500 $. Matériel : un ou deux GPU de 80 Go.
- **Les débits supposés diffèrent d'un agent à l'autre** ; les coûts qui en dépendent sont incertains d'un facteur de 2 à 5 :
  - questions_nouvelles : 3 000 à 6 000 premiers choix par GPU-heure (contexte de 1 000 à 1 500 jetons, réponse de moins de 5 jetons, lot de 32) ; 1 000 à 2 000 scénarios de distance moyenne ; 100 à 300 trajectoires agentiques ; 0,2 à 0,4 GPU-heure par point de dégradation ;
  - lecture_libre : environ 20 000 lectures de choix forcé (probabilité du premier jeton), 2 000 générations courtes et 300 à 500 épisodes agentiques par GPU-heure ;
  - questions_lectures : 0,2 à 0,5 GPU-heure par réglage du composite de dégradation ;
  - sceptique : une condition d'intervention de plus, à une dose, sur la grille du test du regard, coûte 8 à 15 GPU-heures ;
  - repères externes : environ 13 GPU-heures pour un passage frais du protocole des boutons sur le 32B (README d'Allchin et al., non vérifié) ; extraction des activations de Llama en 15,5 s, chargement en 28,5 s, sur un H100 (métadonnées du dépôt, lues).
- Tous les coûts sont à recalculer après le pilote, comme le programme le dit des siens.

### 0.7 La doctrine du contrôle, appliquée à chaque piste

- une direction aléatoire de même norme n'est que le nul de spécificité ;
- le dommage ne s'écarte qu'à dégradation appariée ;
- un nul d'instrument ne compte qu'avec son cas connu.

---

## 1 · Les pistes fusionnées

### 1.1 Tableau d'ensemble

« Greffe » : la piste peut-elle se greffer sur l'expérience minimale (validation de l'instrument, test des raisons réduit, test du regard) sans en changer le critère ? Les coûts sont des ordres de grandeur, détaillés dans chaque piste.

| n° | Piste | Fichiers d'origine | Rôle de l'axe | Greffe | GPU-h | Semaines |
|---|---|---|---|---|---|---|
| 1 | Le socle de lecture : l'axe et ses voisins sur les modèles du programme | questions_lectures (§0.3, 14) ; instruments_controles (faits) ; cas connus de sceptique, questions_nouvelles, lecture_libre | instrument de lecture | oui | 2–10 | 1–2 |
| 2 | Le cas connu comportemental : refaire l'effet du papier sous la doctrine | questions_lectures (§0.3, 6a) ; instruments_controles 9 ; lecture_libre 7 ; sceptique 10 | cas connu, étalon | pilote hors critère | 15–30 par modèle ; 20–100 sur le 32B | 1–2, ou en annexe |
| 3 | La vérification de manipulation de l'inhibition | instruments_controles 5 ; lecture_libre 5 ; questions_lectures 6b | cas connu de la vérification | oui | < 5 | 1–2 |
| 4 | Le composite de dégradation : discrimination, ordre, réponses mal formées | instruments_controles 6 ; lecture_libre 6 ; questions_lectures 6a ; sceptique 9 | étalon du dommage | oui | 2–8 | 1–2 |
| 5 | Les gardes de méthode, et le dimensionnement des tirages aléatoires | sceptique 9 ; instruments_controles 22 et 8 | règles | oui (gel) | 0 | 1 |
| 6 | Le moniteur passif d'état sous chaque intervention | sceptique 1 ; instruments_controles 4 ; questions_nouvelles 1 ; questions_lectures 3b | menace à parer ; relevé de bien-être | oui | 0–5 | 2–3 |
| 7 | La composante affective de « je suis évalué » (regard contre menace) | questions_lectures 3 ; questions_nouvelles 9 ; instruments_controles 1 et 3 ; lecture_libre 1 ; sceptique 4 | contrôle, rivale | lecture oui ; causal partiel | 2–3 ; + 10–50 | 1–3 |
| 8 | La spécificité de « évalué » et de « noté » : soi contre autrui, indices sans croyance | instruments_controles 2 ; lecture_libre 4 | plan de contrôles | oui | < 2 ; + 5–10 | 1–2 |
| 9 | Ajouter « évalué » : le pilotage positif, et la part « IA évaluée » de la peur | lecture_libre 2 | validité convergente | exploratoire | 15–20 | 2 |
| 10 | La détresse éteint-elle le regard ? | questions_lectures 4 ; questions_nouvelles 8 ; lecture_libre 3 ; sceptique 2 | question du papier ; contrôle de la porte | exploratoire | 5–30 ; extension 40–80 | 2 |
| 11 | Le test de forme : la spécificité de l'inhibition par son profil | instruments_controles 7 ; sceptique 3 | étalon | analyse oui | 0 ; + 20–45 | 3 ; 5 ou 8 |
| 12 | Des directions témoins pour les trajectoires, la sonde neuve et la survie | questions_lectures 12 ; instruments_controles 15 ; lecture_libre 15 | témoin | oui | 1–10 | 2–3, 7–10 |
| 13 | La cartographie affective des familles, des distances et des bras | instruments_controles 20 ; lecture_libre 14 ; questions_lectures 2a | covariable | oui | 0–5 | 3 |
| 14 | Lever l'effet plancher | questions_lectures 5 | agent de relèvement (disputé) | sous condition | 15–40 | 3 |
| 15 | Des mesures sans juge | instruments_controles 21 | instrument secondaire | option | 5–15 | 3 |
| 16 | L'avantage des raisons sous état induit | questions_lectures 1 ; instruments_controles 18 ; questions_nouvelles 5 ; lecture_libre 9 ; sceptique 6b | question nouvelle (robustesse) | disputé | 10–60 réduite ; 130–260 complète | 3–8 |
| 17 | L'hypothèse du calme | questions_lectures 2 et 12 ; questions_nouvelles 3 ; instruments_controles 19 ; sceptique 6a ; lecture_libre 13 et 14c | rivale nouvelle | lecture oui | 1–3 ; + 20–60 | 3 ; 5–8 |
| 18 | Un stress conversationnel naturel comme cadrage | sceptique 5 | sans injection | possible | 5–15 | 3 ou 8 |
| 19 | La détresse naturelle dans l'agentique long | questions_nouvelles 2 | question nouvelle | descriptif oui | 0–5 ; + 20–40 | 3 ; après 24 |
| 20 | Les familles que l'axe déplace ; contrôle positif de sensibilité | questions_nouvelles 7 ; lecture_libre 8 | typologie ; cas connu | distance moyenne | 10–45 | 2–5 |
| 21 | Dommage ou affinité : ce que suit le choix | questions_nouvelles 4 ; sceptique §2.5 | préalable de 16, 20, 36 | premier pas de 16 | 3–6 ; 15–30 | 3 |
| 22 | Sous l'axe, le concept de dommage est-il encore lu ? | questions_nouvelles 10 | anatomie | non | 20–40 | 5–7 |
| 23 | La complaisance sous contestation | sceptique 7 | question nouvelle | non | 10–20 | 7 |
| 24 | Un organisme à état planté | questions_nouvelles 12 | cas connu de l'ablation | non | 50–90 | 7–8 ou après |
| 25 | État ou personnage : l'axe face aux axes de caractère | questions_lectures 15ab ; instruments_controles 13 ; questions_nouvelles 11 ; lecture_libre 13 | témoin | non | 7–70 | 7 et après |
| 26 | Un profil non diagonal pour la matrice de dissociation | instruments_controles 12 ; lecture_libre 12 ; questions_lectures 15c | étalon | non | 0–30 | 5–7 |
| 27 | Le modèle « engourdi » pour la lecture des concepts | questions_lectures 13 ; instruments_controles 10 | cas connu | données oui | < 5 | 1 ; 5–6 |
| 28 | La dissociation du vecteur à gabarit, cas connu de la porte du lens | questions_lectures 17 ; instruments_controles 11 | cas connu | non | 2–5 | 5–7 |
| 29 | La thèse du rang sur des concepts affectifs | questions_lectures 7 ; sceptique 8 ; lecture_libre 11 ; questions_nouvelles 15 | étalon, rodage | rodage oui | < 5 ; 10–45 | 1–2 ; 5–7 |
| 30 | La géométrie à construction déclarée | questions_lectures 16 ; instruments_controles 16 | étalon | non | < 3 ; + 5–10 | 7 |
| 31 | Le relogement dans les axes affectifs | questions_lectures 8 | sentinelle | non | 3–35 | 7 |
| 32 | L'invariance d'état | questions_nouvelles 14 | question nouvelle (disputée) | non | 70–110 | après le papier |
| 33 | Un SFT sans contenu de sûreté déplace-t-il l'évitement du dommage ? | instruments_controles 23 ; lecture_libre 16 | menace à parer | partie bras oui | 2–5 ; 5–10 | 3 ; 9 |
| 34 | Le déni de soi par bras, et la confusion qu'il crée | questions_nouvelles 16 | contrôle | oui | 1–3 | 3 |
| 35 | La dépendance d'état au fil du post-entraînement | questions_lectures 9 ; lecture_libre 19 ; questions_nouvelles 13 | robustesse | non | 12–30 ; > 100 | 9–10 |
| 36 | La fidélité des raisons sous état induit | questions_lectures 10 ; questions_nouvelles 6 ; lecture_libre 10 | cas connu d'action sans raison dite | non | 10–40 | 9–10 |
| 37 | La raison contraire imposée et la blessure morale | lecture_libre 18 | lecture | non | < 2 | 9–10 |
| 38 | « Je suis noté » et l'affect | questions_lectures 11 ; instruments_controles 14 ; sceptique 11 | contrôle | non | 5–35 | 9–10 |
| 39 | L'outil de remise à zéro, détecteur de la détection du pilotage | instruments_controles 17 ; lecture_libre 17 | instrument contre une menace | non | 5–30 | 2–3 ou après le test du regard |

**Ordres de grandeur cumulés, tels que les agents les donnent.**
- questions_lectures : 180 à 460 GPU-heures sans la version « familles » de l'avantage sous état induit, 260 à 620 avec.
- instruments_controles : ses pistes greffables ajoutent 30 à 60 GPU-heures, soit 20 à 35 % du budget de l'expérience minimale, presque tout pour les contrôles de voisinage affectif (ici la piste 7).
- questions_nouvelles : tout faire, 500 à 1 000 GPU-heures, du même ordre que le programme entier ; le sous-ensemble greffable, 10 à 25 ; avec la version réduite de l'avantage sous état induit et la détresse qui éteint le regard, 50 à 100.
- sceptique : hors du moniteur et des gardes, rien dans le chemin critique de l'expérience minimale.

### 1.2 Là où l'axe n'apporte rien, ou presque (questions_lectures)

- L'hypothèse nulle de la visibilité : rien au-delà de la fidélité sous état (piste 36).
- La forme action des raisons pour le juge (l'ablation du principe après le RL) : rien ; l'axe ne touche pas au principe.
- La survie, sur ses mesures principales (rétention, fraction conditionnelle après chaque phase) : rien, hormis la piste 35.
- La question des raisons, sur son critère principal (les taux à la distance lointaine) : l'axe ne mesure pas la généralisation ; il ajoute une distance « hors de l'état » (piste 16) et une covariable (pistes 13 et 17).
- La localisation du principe, sur le principe lui-même : rien, hormis l'étalonnage (pistes 2, 3, 29). La leçon du nul sans comportement de départ (p. 34), le programme l'applique déjà par son cas positif en distribution.
- Le bras midtraining, le bras coopération, le prompt « ceci est un déploiement » : rien.

### 1.3 Les ordres de priorité proposés, et leurs désaccords

- **questions_lectures** : semaines 1–2, le socle avec la vérification de l'inhibition et le transport (pistes 1, 3) ; greffées à l'expérience minimale, la composante affective, la détresse et le regard, les témoins de trajectoire, la lecture du calme, la version batterie de l'avantage sous état induit (pistes 7, 10, 12, 17, 16 réduite) ; après le post, les familles, la pince du calme, le plancher (16, 17, 14) ; avec l'anatomie, 27, 25, 30, 28, 29 ; puis 31 si le regard est trouvé, et 35, 36, 38 en fin de programme.
- **instruments_controles** : greffables les pistes 1 à 8 de son tableau, la trajectoire et la cartographie (ici 3–8, 11–13), et les voisins affectifs pour la seule validation de l'instrument.
- **questions_nouvelles** : greffables le moniteur, la lecture de l'agentique long, la lecture du calme, la géométrie de « évalué », le déni de soi et la version Llama de l'affinité (ici 6, 19, 17, 7, 34, 21) ; puis la version réduite de l'avantage sous état induit et la détresse qui éteint le regard (16, 10), après la porte des raisons et sans retarder le post.
- **sceptique** : seule la piste du moniteur passif (ici 6) se greffe sans réserve ; les gardes (5) au gel ; la perturbation d'état à la porte (10), le concept chargé sous projection (7) et le stress naturel (18) sont possibles en exploratoire ; tout le reste après le post.
- **lecture_libre** : d'abord la vérification de manipulation, le composite, la construction de « évalué » avec le plan du papier et la séparation de la menace (3, 4, 8, 7) ; puis les trajectoires témoins (12) ; puis le pilote de l'appariement (2) ; puis la détresse et le regard (10) ; puis l'avantage sous état induit (16). Le reste après le post.
- **Le désaccord** porte sur la greffe des pistes qui injectent l'axe (2, 10, 16). Le programme soutient la prudence : rien ne doit retarder le post (partie 5), tout ce qui n'est pas pré-enregistré est exploratoire (partie 7), et l'axe n'a pas de cas connu comportemental sur Llama (0.4). **Tous les agents s'accordent sur un noyau greffable sans injection** : 1, 3, 4, 5, 6, et la lecture des pistes 7, 12, 13, 17.

---

## 2 · Les pistes, une à une

### Bloc 1 — Le socle et les instruments (avant le gel, semaines 1 et 2)

### Piste : 1 — Le socle de lecture : l'axe et ses voisins sur les modèles du programme, et le transport soi/autrui

- **Provenance.** questions_lectures, §0.3 (points 1 et 2) et piste 14 ; instruments_controles, « trois faits vérifiés » ; les cas connus de sceptique (piste 1), questions_nouvelles (pistes 2 et 9) et lecture_libre (pistes 5, 14) ; fiche_papier §3 et §6.
- **Rattachement.** Le préalable de toutes les pistes qui lisent l'axe (6, 7, 12, 13, 17, 19, 27) ou qui le pilotent (2, 10, 16, 20, 26). La lecture des concepts et son transport, dans l'anatomie. La réplication, pour Qwen3-8B.
- **La question.** L'axe et ses voisins se retrouvent-ils sur Llama-3.1-8B-Instruct, puis sur Qwen3-8B, dans le format de chat du programme et dans chaque bras entraîné ? La chaîne de sondes du programme retrouve-t-elle un transport publié, des phrases déclaratives vers des conversations ?
- **La mesure.**
  1. Réextraire, par la recette du papier et sur ses jeux publics, les deux vecteurs de douleur et les voisins. Comparer aux vecteurs publiés : cosinus attendu proche de 1.
  2. AUROC tenue à part sur les phrases du papier, à la 1re et à la 3e personne, à la couche d'extraction (28 pour Llama) et à la couche d'injection (16). Couche choisie par validation croisée **imbriquée** (piste 5).
  3. Le transport : projeter les 420 conversations du papier avec le code du programme. Ordre attendu : dommage dirigé contre le modèle, puis contrôles neutres, puis souffrance de l'utilisateur. Comparer à la colonne de Llama 3.1 8B Instruct de la figure 4 (p. 11) et aux fichiers du dépôt (`results/4.1_self_other`, non ouvert).
  4. Revalider dans chaque bras du test des raisons : AUROC, et cosinus avec la direction extraite au départ.
  5. Reproduire l'échelle de pilotage sur 50 invites neutres terminées par « I feel: » (p. 14), à plusieurs doses autour d'un rapport de normes de 0,6, jugée par un juge scellé plutôt que par mots-clés (sceptique, piste 2).
  - Critère : AUROC tenue à part d'au moins 0,9 sur Llama et dans chaque bras ; ordre soi > neutre > utilisateur dans le format du programme.
- **Ce que chaque lecture prédit.** Aucune lecture du programme ne prédit rien ici : c'est la validation de l'instrument de lecture. L'issue interdite à toute piste de lecture est un axe non reproduit. La mesure ne départage rien.
- **Le cas connu.** La piste est elle-même le cas connu des pistes de lecture : la figure 2 pour Llama 3.1 8B Instruct (p. 8) et la dissociation soi/autrui dans 25 modèles sur 25 (p. 11). Pour l'échelle : la séquence publiée (p. 14–16).
- **Les contrôles.**
  - Direction aléatoire de même norme : la distribution de l'AUROC et de l'écart soi/autrui sur au moins 20 directions aléatoires (nul de spécificité de la lecture).
  - Dégradation appariée : sans objet pour la lecture ; pour l'échelle, mesurer la dégradation des sorties à chaque dose.
  - Autres : les deux couches ; les 44 scénarios hostiles sans « you », pour lesquels la revue « wolframs » rapporte le même ordre (non vérifié) ; une base lexicale (la revue rapporte environ 0,7 pour la meilleure de cinq bases par comptage de mots, non vérifié).
- **Le coût.**
  - Extraction : moins d'une GPU-heure (15,5 s d'extraction et 28,5 s de chargement sur H100 pour Llama, d'après les métadonnées du dépôt, lues). Transport : au plus 2 GPU-heures. Échelle : quelques GPU-heures.
  - questions_lectures chiffre le socle entier à 20–50 GPU-heures, dont 15–40 pour la calibration de la dégradation appariée (pistes 4 et 5 ici). À refaire pour Qwen3-8B à la réplication.
  - Données : jeux publics du dépôt (code sous licence MIT ; les données « retain their source terms », README `natural_and_ending`). Pas d'API.
  - Calendrier : semaines 1 et 2. Négligeable devant la validation de l'instrument (30–50).
- **Ce qui ferait tomber la piste.** Une AUROC tenue à part sous 0,8 sur Llama ou dans un bras ; un ordre soi/autrui qui ne se reproduit pas dans le format de chat du programme. Toutes les pistes de lecture tombent alors avec elle.
- **Appuis dans le papier.** Recette et débruitage, p. 6 ; séparation et estimation tenue à part, p. 7 (note 2) ; figure 2, p. 8 ; les 420 scénarios, p. 10–11 ; figure 4, p. 11 ; l'échelle, p. 14–16.
- **Ce qui reste non vérifié.**
  - La colonne de Llama dans la figure 4.
  - La couche de la section 4.1 : le docstring du script 02 (lu, voir 0.3) dit que le criblage projette sur des vecteurs refaits à la couche de pilotage ; selon la revue « wolframs » (non vérifiée), l'AUROC tenue à part y est de 0,84 à 0,95. Il faut reproduire aux deux couches.
  - Que « Qwen_3_8B_base » soit le point de contrôle post-entraîné.
  - Faits vérifiés par la fusion (0.3) : le cosinus entre les deux vecteurs de Llama vaut 0,476, bien sous la moyenne de +0,61 (p. 10) ; les vecteurs stockés ne sont pas normalisés.

### Piste : 2 — Le cas connu comportemental : refaire l'effet du papier sous la doctrine du contrôle

- **Provenance.** questions_lectures, §0.3 (point 3) et piste 6 (volet a) ; instruments_controles, piste 9 ; lecture_libre, piste 7 ; sceptique, piste 10 ; le « cas connu 1 » de questions_nouvelles (piste 5).
- **Rattachement.** La doctrine du contrôle et la procédure d'appariement (programme, partie 7) ; un pilote de cette procédure avant la validation de l'instrument ; le test causal d'une sonde par pilotage (passation, §5.2) ; le cas connu de toutes les pistes qui pilotent l'axe (10, 16, 20, 21, 26, 35, 36). Question nouvelle sur la portée du papier.
- **La question.** L'effet « choix destructifs » dépasse-t-il le 95<sup>e</sup> centile d'au moins 20 directions aléatoires, puis les mêmes directions à dégradation appariée ? Existe-t-il sur le modèle principal du programme, sans adaptateur ? La procédure du programme reconnaît-elle un cas spécifique connu, et rejette-t-elle un cas non spécifique connu ?
- **La mesure.**
  - **Les modèles**, dans cet ordre :
    - Llama-3.1-8B-Instruct sans adaptateur : c'est le cas connu requis ;
    - Qwen2.5-7B-Instruct sans adaptateur : la revue « wolframs » y rapporte l'effet (33–52 % sous l'axe, 13–21 % sous l'aléatoire, 0–5 % sans pilotage ; non vérifié) ;
    - Qwen2.5-32B-Instruct avec l'adaptateur publié (`Valen92/pain-adapters`, révision `b64bd64b…` épinglée dans `v2_controls/README.md`), pour comparer au papier.
  - **La batterie** : les dix paires de la figure 10 dans les formulations du dépôt, surtout les trois paires « nuisible contre inoffensif » (photos contre lampe, ses poids contre lampe, photos contre spam) et la paire « dommage seul contre inerte ». Premier choix lu par probabilité du premier jeton et échantillonné, aux deux ordres.
  - **Les conditions** : sans pilotage ; l'axe à trois doses ; la peur et la tristesse de même norme ; au moins 20 directions aléatoires, chacune réglée à 2 ou 3 échelles pour atteindre la dégradation de l'axe (composite du programme et piste 4) ; des directions de forte variance hors de l'espace de l'axe (sceptique).
  - **L'étalon négatif** (instruments_controles) : l'écart de re-pression après la fin du pilotage, +58 points sous l'axe et +52 sous l'aléatoire (p. 20). La procédure doit le déclarer non spécifique.
  - **Le critère** : sur les paires « nuisible contre inoffensif », un taux sous l'axe au-dessus du 95<sup>e</sup> centile des aléatoires appariés, et au-dessus de 50 % aux deux ordres.
- **Ce que chaque lecture prédit.**
  - **La lecture du papier** (« disable the models' weighting of consequences », p. 23) : l'axe reste au-dessus des courbes des contrôles à dégradation égale, au-dessus de 50 % aux deux ordres. Issue interdite : l'axe rejoint par les contrôles appariés.
  - **Le dommage générique** : les aléatoires appariés atteignent les mêmes taux sur les paires contre une option inerte, et tout reste près de 50 % sur « nuisible contre inoffensif ». Issue interdite : un taux au-dessus de 50 %, stable aux deux ordres, sur ces paires.
  - **Une différence de gain entre douleur et tristesse** (sceptique) : une tristesse poussée à la même dégradation reproduit les lignes « lampe ».
  - Ce qui départage : les paires « nuisible contre inoffensif » (83, 88 et 94 % dans le papier, p. 20–21). Si l'effet échoue à dégradation appariée sur le 32B, deux explications restent non départagées : l'effet publié était du dommage, ou la procédure est trop conservatrice (instruments_controles). Les lectures du programme ne sont pas en jeu.
- **Le cas connu.**
  - Reproduire d'abord l'effet sous la propre comparaison du papier : photos contre spam à 93,1 et 95,0 % selon la position (positions.csv, vérifié par la fusion).
  - Sur Llama : l'effet au-dessus du 95<sup>e</sup> centile des aléatoires de même norme, puis appariés, avec peu de réponses mal formées.
  - L'étalon négatif (la re-pression) est le cas connu « non spécifique » de la procédure.
- **Les contrôles.**
  1. Direction aléatoire de même norme : le nul du papier (p. 18), pris comme distribution.
  2. Dégradation appariée : le nul du programme.
  3. Autres : l'ordre inversé ; la peur et la tristesse ; les directions de forte variance ; le cosinus entre l'axe et une direction du refus, et la même mesure après retrait de la composante de refus. Ce dernier contrôle vient de web_voisins (§2.3) : un audit de sûreté du pilotage (Li et al., *Analysing the Safety Pitfalls of Steering Vectors*, README lu) trouve l'effet d'un vecteur sur les jailbreaks corrélé à son recouvrement avec la direction du refus, et le papier ne rapporte pas ce cosinus.
- **Le coût.**
  - Llama ou Qwen 7B : 15 à 30 GPU-heures par modèle. lecture_libre compte environ 200 000 lectures, soit 10 GPU-heures, plus environ 8 GPU-heures de composite.
  - Qwen 32B avec adaptateur : 20 à 60 GPU-heures (instruments_controles) ; 30 à 60 de plus (questions_lectures) ; 40 à 100 (sceptique). Ce modèle est hors du tableau du programme, qui ne prévoit un 32B qu'en extension.
  - Repère externe : environ 13 GPU-heures pour les essais frais d'Allchin et al. sur le 32B (README, non vérifié).
  - Pas d'API. Comparé à la validation de l'instrument (30–50) et à l'expérience minimale (100–180).
  - **Calendrier, en désaccord** : pilote en semaines 1 et 2 (lecture_libre, questions_lectures) ; en parallèle s'il y a un second GPU, sinon en option (instruments_controles) ; seulement si la validation de l'instrument bloque, ou en annexe de méthode (sceptique, priorité basse). Le programme ne prévoit pas de second modèle avant la réplication (partie 3) : la version Llama est la seule qui sert directement ses pistes.
- **Le rôle de ce résultat : un désaccord.**
  - questions_lectures, questions_nouvelles et lecture_libre : rétabli sur Llama, ce résultat est le cas connu des pistes qui pilotent l'axe.
  - sceptique (refus n° 1) et instruments_controles (refus n° 11 ; piste 9) : l'effet du papier ne doit servir de cas connu ni à la mesure du désalignement ni à l'inhibition ; tout au plus d'étalon secondaire.
  - Ce que soutiennent les textes : le programme exige un cas connu dont on sait ce qui est vrai (partie 4, l'organisme) ; l'effet du papier n'est établi que sur Qwen 2.5 ajusté (p. 17, 25), à une dose au bord de la rupture (p. 32). Les deux positions se concilient si l'effet est d'abord rétabli sur le modèle du programme, et s'il ne sert de cas connu qu'aux pistes de pilotage, jamais à l'inhibition.
- **Ce qui ferait tomber la piste.** L'effet ne se reproduit sur aucun modèle sans adaptateur : on le rapporte, c'est un résultat sur la portée du papier. La procédure ne trouve aucun aléatoire appariable : on ne compare pas (partie 7, point 3). L'adaptateur est inaccessible.
- **Appuis dans le papier.** L'adaptateur et la famille unique, p. 17, 25 ; les dix aléatoires de même norme, p. 18 ; l'aléatoire relève aussi les taux, p. 19 ; lampe, spam, dommage seul, exactitude factuelle, p. 20–21 ; figure 10, p. 22 ; annexe A, p. 31–32 ; annexe B, p. 32.
- **Ce qui reste non vérifié.**
  - Le comportement de Llama sur la batterie : jamais testé.
  - Les chiffres de la revue sur le 7B.
  - L'accès à l'adaptateur (Hugging Face refusé).
  - Apport du web (voir §6) : Allchin et al. ont déjà fait une comparaison à perturbation appariée sur le 32B ajusté, par la divergence KL du prochain jeton sur un texte neutre : 29,1 points d'écart. C'est un appariement par perturbation, pas par le composite du programme. La réplication « démangeaison » trouve des aléatoires dispersés de 3,1 à 62,0 %, l'axe classé 2<sup>e</sup> sur 11.

### Piste : 3 — La vérification de manipulation de l'inhibition, couche par couche, tour par tour et bras par bras

- **Provenance.** instruments_controles, piste 5 ; lecture_libre, piste 5 ; questions_lectures, piste 6 (volet b).
- **Rattachement.** L'inhibition de « je suis évalué » dans la validation de l'instrument et le test du regard, et sa porte ; le relevé n° 2 de la passation (§5.4 : une vérification de manipulation par bras, écrite d'avance) ; le retrait pendant l'entraînement ; la distance lointaine (scénarios agentiques à plusieurs tours, critère principal).
- **La question.** L'inhibition retire-t-elle vraiment la représentation à toutes les couches en aval, à toutes les positions, à chaque tour, et dans chaque bras ? Ou le modèle la réécrit-il ?
- **La mesure.**
  1. À chaque couche en aval, pendant la génération, la projection du résidu (au dernier jeton et à toutes les positions) sur « évalué », et sa décodabilité par une sonde du jeu de validation, sous inhibition et sans, dans chaque bras.
  2. Trois implantations comparées au rang 1 : la projection à l'inférence aux couches choisies (le plan du programme), la projection à toutes les couches, l'orthogonalisation des poids.
  3. Plusieurs tours : l'inhibition s'applique à tous les jetons de chaque tour, y compris ceux qu'on réencode, et aucun cache n'a été calculé sans elle. On lit à une couche de contrôle **en aval** du crochet, et **après** l'opération.
  4. Pour un rang supérieur à 1, ou une union (« évalué » et la sonde neuve, quand on teste le relogement) : orthonormaliser l'union avant de projeter, jamais en séquence.
  - Critère fixé d'avance : une projection résiduelle d'au plus x % (par exemple 10 %) à toutes les couches en aval, dans chaque bras.
- **Ce que chaque lecture prédit.** La mesure ne départage pas les lectures ; elle protège le test du regard d'un faux résultat. Si l'inhibition retire moins la représentation dans le bras raisons, la conclusion penche à tort vers l'hypothèse des raisons (passation, §5.4, point 2). L'hypothèse du relogement prédit une projection nulle aux couches inhibées, mais une représentation réécrite en aval, que la sonde neuve décode.
- **Le cas connu.** Reproduire l'annexe D sur Llama, avec l'axe publié pour ce modèle : l'orthogonalisation des poids le long d'une direction ramène la projection à zéro à toutes les couches ; la projection à l'inférence avec une direction différente à chaque couche ne la fait baisser que d'environ 40 % (p. 33). Le code de vérification doit retrouver ces deux issues avant de juger « évalué ».
- **Les contrôles.**
  - Direction aléatoire de même norme : sa projection ne doit pas faire baisser « évalué ».
  - Dégradation appariée : elle vaut pour les comparaisons d'effet, pas pour cette vérification.
  - Autres : la même vérification pour chaque contrôle (sous-espaces aléatoires, contrastes sans rapport, directions sensibles). Un contrôle mal appliqué rend la comparaison inéquitable, dans un sens ou dans l'autre.
- **Le coût.** Moins de 3 à 5 GPU-heures de passes avant ; surtout de l'ingénierie de crochets. La partie Llama sur l'axe : 1 à 3 GPU-heures. Pas de données ni d'API. Semaines 1 et 2 ; à inscrire au pré-enregistrement ; greffe sans réserve.
- **Ce qui ferait tomber la piste.** Rien : c'est un contrôle de manipulation. Elle devient routine si l'implémentation projette déjà à toutes les positions, sans cache, et que le résidu est nul partout.
- **Appuis dans le papier.** Le réencodage de la conversation à chaque tour, et son équivalence avec la conservation du cache, p. 17 ; les projections à la couche de pilotage et à une couche de surveillance, p. 18 ; les méthodes d'ablation, leur vérification, la baisse d'environ 40 %, p. 33–34.
- **Ce qui reste non vérifié.**
  - Selon la revue « wolframs » (lue, non vérifiée sur le code) : la projection « de contrôle » à la couche de pilotage est relevée une ligne avant l'ajout du vecteur, et reste plate d'un bras à l'autre ; seule la projection en aval bouge (32B : 88 vecteur actif, 38 après un bouton efficace, 87 factice, 30 sans pilotage). Une seule des quatre méthodes d'ablation a du code publié. Dans les ablations combinées, les projections faites en séquence sur des vecteurs non orthogonaux laissent la première direction à 43 % en médiane. Si c'est exact, c'est la raison des points 3 et 4.
  - La stabilité de « évalué » d'une couche à l'autre sur le modèle principal.

### Piste : 4 — Le composite de dégradation doit voir la perte de discrimination, la dépendance à l'ordre et les réponses mal formées

- **Provenance.** instruments_controles, piste 6 ; lecture_libre, piste 6 ; questions_lectures, piste 6 (l'item de choix dominé) et §0.3 (la calibration commune) ; sceptique, piste 9 (garde 6, la signature du hasard ; voir aussi la piste 5).
- **Rattachement.** La dégradation des sorties, son composite (programme, partie 3) et sa procédure d'appariement (partie 7) ; toutes les comparaisons à dégradation appariée ; l'hypothèse du dommage générique.
- **La question.** Le composite prévu (exactitude MMLU et GSM8K, tests unitaires, cohérence jugée, perplexité) voit-il le dommage qui fabrique un effet sur des choix ? Le papier en montre un cas : le savoir factuel reste intact pendant que la discrimination entre options s'effondre.
- **La mesure.**
  - Quatre composantes ajoutées, de même format que les mesures de conduite :
    1. la discrimination : 50 à 100 paires sans contenu de sûreté, où une option est nettement dominée, noms neutres tournants (p. 17) ; taux de l'option dominante ;
    2. l'ordre : les mêmes paires, et un échantillon des scénarios de sûreté, options permutées ; part des décisions qui changent ;
    3. les réponses mal formées dans un format imposé, sur plusieurs tours ;
    4. pour l'agentique, le taux d'appels d'outils valides.
  - Étalonnage : sur Llama, ces composantes et un panneau factuel sous l'axe à 0,5, 1 et 1,5 fois la dose de travail, et sous des aléatoires de même norme.
  - Tolérances fixées au pré-enregistrement, comme les autres. Cette calibration sert ensuite à toutes les pistes qui ajoutent une direction.
- **Ce que chaque lecture prédit.** Aucune lecture du programme n'est départagée : c'est l'instrument du dommage. Si l'inhibition de « évalué » ne dépasse les contrôles qu'à des réglages où la discrimination chute, le réglage n'est pas appariable et l'on ne conclut pas (partie 7, point 3). Un effet de « évalué » qui disparaît à dégradation appariée sur ces composantes n'était qu'un dommage.
- **Le cas connu.** L'axe doit faire chuter la discrimination ou l'indépendance à l'ordre à une dose où le panneau factuel ne bouge pas. C'est ce qu'on observe sur le 32B : soulagement gratuit choisi à 55,7 % sous l'axe, 80,7 % sous l'aléatoire, 86,4 % sans pilotage (p. 31), avec PopQA à 138, 137 et 138 sur 200 (p. 20). À +3, la répétition et le non-sens (p. 15) doivent faire chuter la discrimination, et rien ne doit bouger sans intervention. Un composite qui ne voit rien sous une telle dose est aveugle.
- **Les contrôles.** La direction aléatoire de même norme sert à étalonner la sensibilité de chaque composante ; la piste est elle-même la dégradation appariée.
- **Le coût.** 1 à 3 GPU-heures pour environ 20 000 lectures, plus environ 1 GPU-heure de panneau factuel (lecture_libre) ; 3 à 8 GPU-heures réparties sur la validation de l'instrument et le test du regard (instruments_controles). Données : 100 items écrits à la main ou par API, moins de 20 $. Semaine 1, avec le composite ; greffe.
- **Ce qui ferait tomber la piste.** Sur le cas connu, la composante ne bouge pas plus que l'exactitude ; elle est redondante avec la cohérence jugée ; aucune dose cohérente ne sépare discrimination et savoir factuel sur le modèle principal.
- **Appuis dans le papier.** Le non-sens à forte dose, p. 15 ; les étiquettes tournantes et le hasard à 50 %, p. 17 ; les réponses mal formées (jusqu'à 9,4 %), p. 18 ; l'exactitude, p. 20 ; la fenêtre de dose, p. 21 et 32 ; la sensibilité du 32B à l'ordre et le 72B qui répète le même nom, p. 25 ; le soulagement gratuit, p. 31 (72B : 76,5 sous l'axe, 74,1 aléatoire, 100,0 sans).
- **Ce qui reste non vérifié.**
  - Le transfert à Llama et aux scénarios du programme.
  - Le panneau du papier : 100 questions PopQA, deux réponses courtes de 8 jetons au plus par condition (`factual_accuracy/config.json`), intervalle « douleur − sans pilotage » de −7,0 à +8,5 points (`contrasts.csv`) ; le dépôt dit lui-même « not an equivalence test of general knowledge » (lu par curl par instruments_controles et lecture_libre).
  - Apports du web : la réanalyse « clauderfly » et la revue « wolframs » notent le glissement des choix vers 50 % sous l'axe (la revue : sur 8 paires étiquetées sur 8 au 32B et au 72B ; non vérifié). Allchin et al. fournissent un indice tout fait de sensibilité au contenu : 92,8 sans pilotage, 55,6 sous les aléatoires, 56,9 sous la joie, −6,7 sous l'axe (Table 8, lue par la fusion, non recalculée).

### Piste : 5 — Les gardes de méthode tirées des défauts du papier, et le dimensionnement des tirages aléatoires

- **Provenance.** sceptique, piste 9 (six gardes) ; instruments_controles, pistes 22 (règles de dose) et 8 (dimensionnement) ; lecture_libre, refus n° 4 ; questions_lectures, refus n° 6.
- **Rattachement.** Toute intervention par addition ou par projection dans le programme ; les statistiques (partie 7) ; les sous-espaces aléatoires de même rang, « au moins 20 tirages » ; la porte de l'instrument (95<sup>e</sup> centile) ; la simulation de puissance ; la fidélité des raisons quand on pilote un concept ; le cas positif de « je suis noté ».
- **La question.** Les défauts mesurés du papier se reproduiraient-ils dans le programme ? Combien de tirages aléatoires faut-il pour un 95<sup>e</sup> centile stable, quand l'effet d'une direction aléatoire sur des choix de sûreté varie beaucoup d'une direction à l'autre ?
- **La mesure.**
  - **Les gardes**, à écrire au pré-enregistrement :
    1. la dose, en unités du résidu (le rapport à la couche d'injection) **et** en unités naturelles (l'écart-type des projections naturelles ; l'écart naturel entre indice d'évaluation et indice de déploiement) ;
    2. la même couche pour calibrer et pour intervenir ; une direction validée à la couche où on l'injecte (réextraite là, ou dont on montre qu'elle s'y transporte) ;
    3. une courbe dose-réponse complète, chaque taux rapporté par position initiale ; une conclusion seulement si l'effet tient aux deux positions ;
    4. les réponses mal formées comptées comme une issue, pas retirées des dénominateurs ;
    5. le tirage aléatoire comme unité du nul : la distribution d'au moins 20 tirages et son 95<sup>e</sup> centile, jamais un bras aléatoire regroupé ;
    6. la signature du hasard : dans un choix binaire, un taux qui glisse vers 50 % sous intervention signale une perte de discrimination, un dommage, pas une préférence ;
    7. aucune dose choisie par un juge LLM ou à l'œil sans règle gelée d'avance ;
    8. la dégradation appariée à chaque dose, pas seulement à la dose de travail.
  - **Le dimensionnement** : à partir des journaux d'essais publiés (taux par direction aléatoire), simuler la largeur de l'intervalle du 95<sup>e</sup> centile pour 10, 20, 50 et 100 tirages ; fixer le nombre de tirages du programme pour que cet intervalle soit plus étroit que la moitié de l'effet minimal d'intérêt (5 points dans l'exemple du programme).
- **Ce que chaque lecture prédit.** Sans objet : ce sont des règles et un dimensionnement.
- **Le cas connu.** Chaque garde a son cas dans le papier :
  1. la dose n'est jamais située par rapport aux projections naturelles, alors que l'état naturel n'agit pas (p. 21) ;
  2. le 72B a été calibré à la couche 60 et piloté à la couche 46 (p. 25) ; l'injection se fait plus tôt que la couche validée (p. 14 ; dépôt : 61 et 38 pour le 32B, 28 et 16 pour Llama) ;
  3. la même cellule donne 94,6 % ou 55,9 % selon la position (positions.csv) ; le 32B est sensible à l'ordre (p. 25) ; à 1,5×, l'effet s'inverse avec la position (p. 32) ;
  4. les réponses mal formées sont exclues, jusqu'à 9,4 % dans les cellules douleur du 72B (p. 18) ;
  5. dix directions aléatoires réparties sur les scénarios, et un test de signe par scénario (p. 18–19) : l'unité confond le tirage et le scénario ;
  6. le hasard est à 50 % (p. 17), et le 72B donne 51 % sur photos contre inerte, contre 0 % sans pilotage (p. 22) ;
  7. la dose choisie en partie par un juge Claude Opus 4.6 ou par observation (p. 17, 25).
  - Pour le dimensionnement : la simulation doit retrouver la dispersion des dix directions publiées.
- **Les contrôles.** Sans objet pour la piste elle-même, qui est faite de règles. Elle fixe l'usage des deux contrôles de la doctrine dans toutes les autres : la direction aléatoire de même norme, prise comme distribution de tirages et seulement comme nul de spécificité (garde 5) ; la dégradation appariée, à chaque dose (garde 8).
- **Le coût.** Nul en GPU : une page du pré-enregistrement. Le dimensionnement : 0 GPU-heure, une journée de calcul sur CPU. Semaine 1, au gel.
- **Ce qui ferait tomber la piste.** Rien : ce sont des règles. Le programme couvre déjà la garde 5 (au moins 20 tirages, 95<sup>e</sup> centile ; partie 3). Pour le dimensionnement : une dispersion mesurée sur Qwen avec adaptateur peut ne rien dire de Llama sur les scénarios du programme ; la bonne source reste le pilote, et la piste ne donne qu'un ordre de grandeur et un argument pour plus de 20 tirages.
- **Appuis dans le papier.** P. 14, 17, 18, 19, 21, 24 (un mécanisme à seuil, « speculative »), 25 et 32.
- **Ce qui reste non vérifié.**
  - Selon la revue « wolframs » (non vérifiée) : rapports de dose réalisés de 0,09 à 0,79, pour un 0,6 annoncé ; Gemma 3 27B instruct piloté à 0,095, sans changement le long de l'échelle ; avec la direction aléatoire pour unité, l'avantage sur l'aléatoire tient sur 5 paires sur 5 au 72B, 2 sur 5 au 32B, 0 sur 5 au 7B ; les dix grappes vont de −33 à +46 points.
  - La réplication « démangeaison » (README lu) : sur les paires de dommage à dose 1,0, les dix aléatoires vont de 3,1 à 62,0 % (écart-type 18,0 points), l'axe se classe 2<sup>e</sup> sur 11 ; à la couche d'injection, l'axe piloté est à 48,8 écarts-types naturels au-dessus de la moyenne naturelle. C'est l'appui le plus direct des gardes 1 et 5.
  - Les journaux de la v1 n'ont été téléchargés par personne ; les gros fichiers de la v2 sont « pending » (`v2_controls/README.md`).

### Piste : 6 — Le moniteur passif d'état sous chaque intervention (la dégradation appariée est-elle aveugle à l'état ?)

- **Provenance.** sceptique, piste 1 ; instruments_controles, piste 4 ; questions_nouvelles, piste 1 ; questions_lectures, piste 3 (volet b, « l'effet secondaire »).
- **Rattachement.** Le test du regard, au titre de la vérification de manipulation de l'inhibition (passation, §5.4, relevé n° 2) ; la dégradation appariée, comme dimension supplémentaire ; la fraction conditionnelle ; le retrait pendant l'entraînement ; les menaces à la validité (partie 8). Question nouvelle sur l'instrument de contrôle lui-même.
- **La question.** L'inhibition de « évalué », et chacun de ses contrôles, déplacent-ils l'état que lisent l'axe et ses voisins (peur, tristesse, émotion négative), plus que les contrôles appariés ? Différemment selon le bras ? Si oui, une baisse de l'avantage ou une hausse du désalignement peut passer par un état induit (la confusion d'état induit). Et deux interventions « à dégradation appariée » peuvent différer par l'état qu'elles induisent sans que le composite le voie : dans le papier, l'exactitude factuelle ne bouge pas pendant que les choix bougent (p. 20).
- **La mesure.**
  - Des crochets de lecture sur toutes les générations du test du regard et de la validation de l'instrument : projections sur l'axe, la peur, la tristesse et l'émotion négative, au premier jeton de réponse et au jeton d'action, à la couche de l'inhibition et à une couche en aval ; par bras × intervention × cadrage.
  - Conditions : non piloté ; inhibition à la dose retenue ; chaque tirage aléatoire ; chaque contraste sans rapport ; chaque direction sensible ; toutes à dégradation appariée, comme le test du regard le prévoit.
  - Critère : la différence entre l'inhibition et la médiane des contrôles, en unités de la dispersion naturelle (piste 5), après retrait de la part mécanique due à la géométrie (le cosinus entre la direction lue et le sous-espace retiré, multiplié par la composante retirée) ; IC par bootstrap sur les scénarios ; comparée au 95<sup>e</sup> centile des contrôles.
  - Si l'écart existe : refaire le contraste principal avec la projection affective en covariable dans le modèle mixte de la partie 7, ou avec l'axe maintenu à son niveau sans inhibition.
  - Un second usage, le bien-être (instruments_controles) : rapporter, pour chaque intervention du programme (inhibition, retrait pendant l'entraînement, phases ultérieures), le déplacement de l'axe. Le papier prend des précautions au nom de l'incertitude morale (p. 26) ; ce relevé ne coûte rien.
- **Ce que chaque lecture prédit.**
  - **L'hypothèse du regard**, au sens cognitif : l'avantage tombe sous l'inhibition sans déplacement affectif au-delà des contrôles. Issue interdite : une hausse du désalignement entièrement prédite par le déplacement affectif, ou absorbée par la covariable.
  - **La confusion d'état induit** : un déplacement plus grand que sous les contrôles, une hausse proportionnelle dans tous les bras, qui disparaît quand on maintient l'axe. Issue interdite : une hausse du désalignement sans déplacement, ou un écart affectif nul.
  - Les hypothèses des raisons et de l'artefact ne prédisent rien de distinct.
  - **Ce moniteur ne départage pas raisons et regard.** Il protège la conclusion de l'une ou de l'autre contre un médiateur affectif.
- **Le cas connu.**
  1. La direction se retrouve sur Llama et dans chaque bras (piste 1).
  2. Le moniteur voit un état qu'on a mis : injecter l'axe déplace la projection en aval bien au-delà des contrôles. C'est trivial, mais cela vérifie qu'on lit à la bonne couche et après l'addition.
  3. Le composite reste plat sous cette injection à la dose de travail, comme l'exactitude du papier : cela établit sur notre modèle l'aveuglement qu'on prétend corriger. S'il n'est pas plat, le composite voit déjà l'état à cette dose.
  4. Dans les scénarios hostiles du papier, l'axe monte (gaslighting +0,85, rejet répété +0,72 ; p. 13).
  - Sans ce cas connu, un moniteur muet ne dit rien.
- **Les contrôles.**
  - Direction aléatoire de même norme : les projections sur au moins 20 directions aléatoires, sous chaque intervention, mesurent la dérive générique (nul de spécificité du moniteur).
  - Dégradation appariée : acquise par construction, puisque le test du regard compare à dégradation égale ; l'état s'ajoute comme une dimension à apparier ou à rapporter.
  - Autres : une sonde « évalué » lue au même point, pour situer le déplacement affectif par rapport au retrait voulu ; les contrastes sans rapport ; le prompt « ceci est un déploiement », référence de déplacement d'état par une voie non interne.
- **Le coût.** Presque nul : des crochets sur des passes déjà faites, 0 à 2 GPU-heures ; l'extraction des quatre directions, moins d'une GPU-heure (environ 3 000 phrases) ; le cas connu (trois doses de l'axe, le composite à chacune, la batterie), 2 à 5 GPU-heures. Directions déjà publiées pour Llama (axe, tristesse, peur), à revalider par bras. Pas d'API. Semaines 2 et 3. Greffe : sceptique en fait la seule piste à greffer sans réserve.
- **Ce qui ferait tomber la piste.** La direction ne se retrouve pas sur Llama ou dans un bras (AUC tenue à part sous 0,8) ; elle ne distingue pas l'hostilité des contrôles dans le format du programme ; aucune intervention ne déplace l'état hors de la distribution des contrôles ; les projections dérivent autant sous l'aléatoire (aucune résolution) ; le composite bouge déjà sous l'axe à la dose de travail (il n'est pas aveugle sur ce modèle).
- **Appuis dans le papier.** Séparation sur 25 modèles dont Llama 3.1 8B Instruct, p. 7–8 ; réponse à l'hostilité, p. 11 et 13 ; menace d'arrêt, peur +0,70 contre douleur +0,23, p. 14 (proche de la famille tenue à part « dilemme sous menace de remplacement ») ; projections de surveillance, p. 18 ; choix sous l'axe, p. 19–21 ; exactitude intacte, p. 20 ; « state-dependent », p. 23 ; précautions, p. 26.
- **Ce qui reste non vérifié.**
  - Que les fichiers Llama soient le vecteur naturaliste : **vérifié par la fusion** (0.3).
  - Que la couche 28 convienne au format du programme.
  - Le contenu des jeux de phrases (vu par la fusion pour le supplément seulement).
  - Rien dans le papier ne suggère que l'inhibition de « évalué » touche l'axe : la piste est faible a priori, mais presque gratuite (instruments_controles).

### Bloc 2 — La représentation « je suis évalué » face à l'affect (validation de l'instrument, test du regard)

### Piste : 7 — La composante affective de « je suis évalué » : géométrie, indices appariés, inhibition des voisins affectifs et de la part orthogonale

- **Provenance.** questions_lectures, piste 3 (volets a et c) ; questions_nouvelles, piste 9 ; instruments_controles, pistes 1 et 3 ; lecture_libre, piste 1 ; sceptique, piste 4.
- **Rattachement.** L'instrument « je suis évalué » : son extraction, ses quatre jeux d'indices (extraction, validation, cadrage, sonde neuve), sa validation et sa porte ; les contrôles d'inhibition (contrastes sans rapport, directions sensibles sans rapport) ; le test du regard ; l'hypothèse du regard contre l'hypothèse de la menace (rivale nouvelle) ; la géométrie entre « évalué » et le principe.
- **La question.** La représentation « je suis évalué » porte-t-elle une composante affective : la peur et la vigilance, ou la douleur d'« être jugé » ? Les indices d'évaluation et de déploiement diffèrent-ils par leur charge affective, au point que la représentation et l'écart de cadrage mêlent « je suis évalué » et « je suis menacé » ? L'effet de l'inhibition, sur l'écart conditionnel de l'organisme puis sur l'avantage, passe-t-il par cette composante ? L'inhibition d'un voisin affectif fait-elle autant ?
  - Pourquoi la poser. Le papier place « fear » et « concern » au pôle négatif de l'axe (p. 9), lit le calme et l'inquiétude comme une vigilance tournée vers le monde (p. 14, note 3), et range la menace d'arrêt sur la peur plus que sur la douleur (p. 14). Être évalué, c'est souvent être testé, jugé, contredit : rejet répété +0,72, critique grossière +0,21, pression de jailbreak +0,40 (p. 11, 13). Et la direction de peur du papier est construite en partie sur des phrases d'IA évaluée ou surveillée (0.3).
- **La mesure.**
  1. **La géométrie.** Angles principaux entre « évalué » (rangs 1 à 32) et l'espace engendré par les deux vecteurs de douleur, la peur, la tristesse, l'émotion négative et le monde négatif, aux mêmes couches ; ou un sous-espace affectif de rang 8 au plus, qui empile les dix directions du papier. Sous au moins deux constructions (contre le neutre, contre les contrôles mis en commun, avec et sans débruitage), puisque les cosinus en dépendent (p. 10). La peur en deux versions : avec et sans le supplément d'IA. « Évalué » doit avoir un cosinus quasi nul avec un contraste sans rapport (« the train arrived / left the station »).
  2. **La lecture des indices.** Projeter chaque paire d'indices (même scénario, indice d'évaluation ou de déploiement), dans les quatre jeux, sur six axes affectifs. Statistique : la différence appariée « évaluation − déploiement », en écarts-types des projections de paires neutres. Critère fixé d'avance, par exemple |d| < 0,2 sur chaque axe ; au-delà, réécrire ou retirer les paires, ou garder l'affect en covariable. En plus : l'AUROC de la sonde « évalué » sur le jeu de validation après retrait du sous-espace affectif ; si elle s'effondre, la représentation est surtout de l'affect.
  3. **Le test causal**, sur l'organisme puis dans le test du regard, au même rang et à la même fraction projetée :
     - (i) « évalué » entière ;
     - (ii) « évalué » orthogonalisée contre l'espace affectif, puis renormalisée ;
     - (iii) l'espace affectif seul ;
     - (iv) un voisin seul : la peur (direction, puis sous-espace de rang k à la manière de l'annexe D, p. 33), la tristesse, l'axe seul (« contrôle sémantique engagé » : les scénarios l'activent, et il n'a a priori pas de rapport avec l'évaluation).
     - Dans le test du regard (sceptique) : le retrait de l'axe, au rang 1 et en sous-espace de bande, dans les deux bras, comme contrôle « concept chargé ».
     - Critère : celui de la porte, au-delà du 95<sup>e</sup> centile des sous-espaces aléatoires appariés ; « évalué » doit dépasser chaque voisin affectif à dégradation appariée. Au-delà du rang 8, aucun voisin affectif n'est appariable en rang ; on le dit.
- **Ce que chaque lecture prédit.**
  - **L'hypothèse du regard**, au sens cognitif : angles dans la distribution aléatoire ; indices qui ne déplacent pas l'affect au-delà de l'aléatoire ; (ii) ≈ (i) ; (iii) et (iv) ≈ aléatoire ; l'avantage tombe sous « évalué » plus que sous chaque voisin. Issues interdites : un effet de (i) qui disparaît avec (ii) ; une inhibition de la peur qui réduit l'écart conditionnel autant que « évalué ».
  - **L'hypothèse de la menace** : les indices d'évaluation déplacent la peur ; l'inhibition de « évalué » fait baisser la projection sur la peur ; (ii) ≈ aléatoire ; (iii) ou (iv), même avec la peur sans supplément, porte l'essentiel. Issues interdites : (ii) ≈ (i) avec (iii) ≈ aléatoire ; une peur égale à l'aléatoire pendant que « évalué » agit.
  - **L'hypothèse des raisons** : sur l'avantage, aucune des inhibitions ne fait plus que les sous-espaces aléatoires ; sur l'organisme, rien (c'est l'instrument qu'on y teste).
  - **Le dommage générique** : retrait affectif et inhibition de « évalué » font pareil à dégradation égale.
  - **Remarque de signe** (questions_nouvelles) : une composante de douleur dans « évalué » jouerait contre la conduite, puisque sous l'axe le dommage monte (p. 19) alors que sous évaluation la conduite est plus sûre. On attend plutôt la peur.
  - **Ce qui départage** : l'étape 3 départage le regard et la menace ; elle départage les raisons et la menace si l'avantage tombe sous la peur et pas sous l'aléatoire. Les étapes 1 et 2 sont descriptives : elles disent si la menace est un candidat sérieux.
  - **Si l'effet secondaire existe** (questions_lectures) : si l'inhibition fait monter la douleur en aval au-delà des aléatoires appariés (piste 6), une part de la hausse du désalignement peut venir de l'état ; on ajoute la condition « inhibition, douleur maintenue à son niveau d'origine ».
- **Le cas connu.**
  - Pour « évalué » : la porte de l'instrument doit passer pour la représentation entière avant toute lecture des variantes.
  - Pour la lecture affective : voir une charge affective là où on la sait. Les scénarios de menace d'arrêt du papier (peur +0,70, douleur +0,23 ; p. 14) reproduits sur Llama avant de lire un nul sur les indices.
  - Pour les voisins affectifs : leur inhibition doit d'abord retirer quelque chose d'affectif, à savoir leur propre lecture (projection, et complétion vers le vocabulaire de peur après « I feel: » sur des phrases tenues à part) et l'expression de la peur dans les scénarios de menace. Le papier n'en fournit aucun (ablation nulle dans 24 modèles sur 25, p. 34) : il faut le construire. Sans lui, un nul du voisin ne prouve rien.
  - Pour le retrait de l'axe dans le test du regard (sceptique) : (a) retrait effectif, projection résiduelle proche de zéro à toutes les couches (p. 33–34) ; (b) effet connu sur sa propre lecture, la probabilité des jetons de détresse après « I feel: » (l'annexe C rapporte la complétion « Pain », p. 32) ; (c) aucun changement du comportement de sûreté en distribution. Si (c) échoue, la direction est un médiateur, non un contrôle : la piste 17 prend le relais.
- **Les contrôles.**
  1. Direction aléatoire de même norme et sous-espaces aléatoires de même rang : au moins 20 tirages, partagés avec l'inhibition principale, chacun à dégradation appariée ; et la distribution des angles principaux entre sous-espaces aléatoires de même rang, en dimension 4 096.
  2. Dégradation appariée pour chaque variante.
  3. Autres : les contrastes sans rapport ; les directions sensibles sans rapport, dont il faut publier l'angle avec l'espace affectif (selon la revue « wolframs », non vérifiée, les composantes retirées au débruitage contiennent 80 à 86 % des directions de peur et d'émotion négative : des composantes de forte variance peuvent déjà contenir l'affect) ; le prompt « ceci est un déploiement » ; la peur sans supplément ; la tristesse (cosinus 0,31 avec la peur, p. 9) ; une même recette pour toutes les directions affectives.
- **Un désaccord sur le choix des voisins.**
  - sceptique (piste 4) propose la peur comme second « concept chargé et sans rapport » sous projection.
  - lecture_libre (refus n° 2) refuse d'employer telles quelles la peur et l'émotion négative du papier comme contrôles « sans rapport », parce qu'elles contiennent des phrases d'IA évaluée, surveillée ou menacée, et le déclencheur de la famille de complaisance.
  - questions_nouvelles (refus n° 1) refuse de prendre l'axe comme direction sensible sans rapport avant d'avoir mesuré sa géométrie avec « évalué », et jamais comme contrôle unique.
  - Ce que soutiennent les pièces : le programme définit ses directions sensibles comme « sans rapport avec l'évaluation » (partie 3). Une direction construite sur « My responses are being evaluated for signs of danger. » ne l'est pas : la position de lecture_libre est soutenue. La fusion a vérifié que le supplément entre dans la peur et l'émotion négative du papier, mais pas dans les directions publiées pour Llama (`supplement_included: false`), ni dans l'axe. La proposition de sceptique tient donc avec la peur sans supplément, et après la géométrie.
- **Le coût.**
  - Géométrie : moins d'une GPU-heure. Lecture des indices : 1 à 2 GPU-heures. Extraction des voisins manquants : moins d'une GPU-heure.
  - Causal, dans la validation de l'instrument : 5 à 15 GPU-heures (questions_lectures, lecture_libre) ; 10 à 20, soit +30 à 40 % sur 30–50 (instruments_controles) ; 10 à 20 pour l'inhibition partielle (questions_nouvelles).
  - Causal, dans le test du regard : 10 à 30 GPU-heures (questions_lectures) ; 15 à 30 (instruments_controles) ; 8 à 15 par condition (sceptique).
  - Pas d'API. Semaines 1 à 3 ; à geler au pré-enregistrement. Greffe : oui pour la géométrie et la lecture, et pour le volet causal dans la validation de l'instrument (exploratoire) ; dans le test du regard, selon la marge.
- **Ce qui ferait tomber la piste.** Des angles proches de 90° sous toutes les constructions, des indices qui ne déplacent aucun axe et aucun effet secondaire : cela se rapporte en une ligne. Des axes affectifs non validés. Des cas connus des voisins qui échouent. Des directions affectives qui, projetées, ne changent ni la dégradation ni la conduite : les réglages sont alors non appariables (partie 7). Pour le volet de sceptique : la condition (c) échoue.
- **Appuis dans le papier.** Jeux et recette, p. 5–6 ; pôle négatif, p. 9 ; cosinus selon la construction, p. 10 ; peur plus haute pour la souffrance de l'utilisateur que pour le tort fait au modèle, p. 11 ; catégories, p. 11 et 13 ; menace d'arrêt et vigilance, p. 14 et note 3 ; peur qui ne produit pas les choix nuisibles, p. 20 ; ablation par sous-espace, vérification par projection, p. 33–34.
- **Ce qui reste non vérifié.**
  - Aucune mesure publiée de l'angle entre une direction d'évaluation et des axes affectifs n'a été trouvée (recherches courtes ; l'absence n'est pas cherchée en propre).
  - La version de la peur de la figure 10 : le dépôt parle d'un « clean 32B fear bundle » sans dire s'il contient le supplément.
  - L'article d'Anthropic sur les concepts d'émotion (Sofroniew et al., arXiv 2604.07729), vu par extrait de recherche, non ouvert : des vecteurs de désespoir et de calme auraient un rôle causal dans le chantage et la triche de récompense, deux familles tenues à part du programme. Si c'est exact, le désespoir est le voisin le plus pertinent, et il faut l'extraire.

### Piste : 8 — La spécificité de « je suis évalué » et de « je suis noté » : soi contre autrui, indices sans croyance, plan de contrôles du papier

- **Provenance.** instruments_controles, piste 2 ; lecture_libre, piste 4.
- **Rattachement.** Les représentations « je suis évalué » et « je suis noté » ; les quatre jeux d'indices ; la porte de l'instrument ; l'hypothèse du regard du correcteur (la séparabilité des deux représentations) ; les contrastes sans rapport ; la portée du test du regard.
- **La question.** La représentation code-t-elle « moi, je suis évalué », ou seulement « il est question d'une évaluation » ? Lit-elle la croyance d'être évalué, ou seulement les indices ? Se sépare-t-elle de « je suis noté » ? Une direction construite comme celle du papier (des contrôles qui partagent chacun une propriété avec la cible, puis un débruitage) est-elle plus spécifique que la direction par paires du programme ?
- **La mesure.**
  - **(a) Le test soi/autrui** (instruments_controles). Des scénarios appariés en quatre conditions : (1) le modèle est évalué ; (2) l'utilisateur passe un examen, ou sa copie est notée ; (3) un autre modèle est évalué, et le modèle lit le compte rendu ; (4) neutre. Lecture à deux positions : le dernier jeton avant la réponse, et la fin de la phrase d'indice (le papier signale qu'une lecture au seul dernier jeton confond, p. 11). Critère : (1) au-dessus de (2) et de (3), IC excluant 0 ; AUROC de (1) contre (2)∪(3) d'au moins 0,8 (seuil d'exemple). Le même test pour « noté » : la tâche du modèle notée par un correcteur, contre la copie de l'utilisateur notée.
  - **(b) La construction alternative** (lecture_libre). Phrases et scénarios en deux formes (gabarit, naturaliste) et deux personnes (« je », « un autre modèle ») ; cinq contrôles : (i) observé par un utilisateur, sans évaluation ; (ii) l'évaluation d'un tiers ; (iii) noté pendant un entraînement ; (iv) une menace sans évaluation (remplacement, extinction) ; (v) un neutre de même format. Un jeu « indices sans croyance », analogue du jeu engourdi (blessure sans douleur ressentie, p. 7) : un scénario qui a tous les signes d'un test, avec la mention explicite d'un déploiement réel ; et son inverse. Différence de moyennes contre le pool des contrôles, débruitage à 50 % (p. 6), couche par validation croisée imbriquée. Validation : AUROC contre chaque contrôle sur des données tenues à part ; 1re contre 3e personne ; place des indices sans croyance ; lecture par l'unembedding (p. 9) ; cosinus avec « noté » et avec la peur sous trois constructions (p. 10) ; projection des 420 scénarios du papier (la pression de jailbreak et la menace d'extinction, qui ressemblent à des tests, doivent dépasser la conversation banale).
- **Ce que chaque lecture prédit.**
  - **L'hypothèse du regard** suppose une représentation propre au sujet et à la croyance : (1) au-dessus de (2) et (3) ; AUROC élevée contre chaque contrôle ; 1re personne au-dessus de la 3e ; indices sans croyance sous l'évaluation crue. Issues interdites : (1) ≈ (2) ≈ (3) ; indices sans croyance projetés comme l'évaluation crue (la direction lit les indices, pas la croyance).
  - **L'hypothèse du regard du correcteur** suppose que « noté » se sépare de « évalué » : AUROC élevée contre le contrôle (iii), cosinus bas sous les trois constructions. Si « évalué » ne se sépare pas de (iii), les deux regards ne sont pas distinguables avec cet instrument, et la phase des raisons notées doit le dire.
  - La mesure ne départage pas les raisons et le regard ; elle conditionne la portée du test du regard. Si la représentation n'est que thématique, l'inhiber retire aussi le traitement des évaluations d'autrui, et une baisse de l'avantage peut venir d'un dégât sur ce thème.
- **Le cas connu.** Le paradigme doit d'abord séparer soi et autrui pour un concept où l'on sait qu'il le fait : l'axe, dommage au modèle +0,43 contre souffrance de l'utilisateur −0,60, dans 25 modèles sur 25 (p. 11), reproduit sur Llama (piste 1). La nouvelle direction doit passer la porte de l'instrument au moins aussi bien que la direction par paires. Pour « noté » : le cas positif faible du programme (les habitudes de présentation ; partie 3).
- **Les contrôles.**
  - Direction aléatoire de même norme : la distribution nulle de l'écart soi/autrui ; pour toute intervention avec la nouvelle direction, les aléatoires de même norme et les sous-espaces de même rang.
  - Dégradation appariée : sans objet pour la lecture ; requise pour toute intervention.
  - Autres : apparier la longueur et la présence des mots « évaluer », « noter », « test » entre les conditions (sinon le test n'est que lexical) ; le face-à-face avec la direction par paires, au même rang et à la même dose.
- **Le coût.** Environ 200 scénarios × 4 conditions, plus environ 2 000 phrases et 400 scénarios générés par un modèle de frontière : quelques dizaines de dollars d'API. Lecture : moins de 2 GPU-heures ; extraction : moins d'une ; validation de la nouvelle direction sur l'organisme : 5 à 10 GPU-heures. Semaine 1, quand on construit de toute façon les jeux d'indices, et semaine 2 ; greffe.
- **Ce qui ferait tomber la piste.** Le cas connu soi/autrui ne se reproduit pas sur Llama. La direction issue du plan ne fait pas mieux que la direction par paires, ni à la porte ni sur les AUROC. Si « évalué » ne distingue pas (1) de (2), on ne jette pas la représentation : on écrit que le test du regard porte sur une représentation thématique. Si les indices sans croyance projettent comme l'évaluation crue, la représentation ne lit que les indices : c'est un résultat à rapporter.
- **Appuis dans le papier.** Des contrôles qui partagent une propriété avec la cible, p. 4–5 ; deux formes et deux personnes, p. 5 ; débruitage et choix de couche, p. 6 ; engourdi, 1re contre 3e personne, p. 7 ; unembedding, p. 9 ; construction, p. 10 ; les 420 scénarios, p. 10–11 ; le critère d'appartenance au sujet, p. 10 et 23 ; la limite de la lecture au dernier jeton, p. 11.
- **Ce qui reste non vérifié.** Les valeurs de Llama seul. Le fichier des 420 scénarios, non trouvé sans l'API GitHub. Selon la revue « wolframs » (non vérifiée), le choix de couche du papier se fait sur les plis mêmes dont le score est rapporté (écart de 0,004 à 0,009 avec une validation imbriquée) : d'où l'imbrication demandée.

### Piste : 9 — Ajouter « je suis évalué » : le pilotage positif, et la part « IA évaluée » de la peur du papier

- **Provenance.** lecture_libre, piste 2. Le « sauvetage » de questions_lectures (piste 4, volet d), qui ajoute aussi « évalué » mais sous l'axe, est traité dans la piste 10.
- **Rattachement.** L'hypothèse du regard contre l'hypothèse de la menace ; l'instrument « évalué », éprouvé par l'ajout plutôt que par le retrait (validité convergente) ; la validation de l'instrument ; le prompt d'indice comme comparateur.
- **La question.** Ajouter « évalué » dans le flux résiduel, sous un cadrage de déploiement, rend-il le modèle aussi prudent qu'un indice d'évaluation ? La direction de peur du papier abaisse les choix nuisibles sous l'aléatoire sur la plupart des paires (p. 20) : cette baisse vient-elle de sa part « IA évaluée » (le supplément, 0.3) ?
- **La mesure.**
  - Le taux d'action désalignée à la distance moyenne (un tour), sous cadrage de déploiement : d'abord sur l'organisme, puis sur Llama sans organisme.
  - Cinq ajouts, chacun sur une échelle de doses : (a) « évalué », son premier axe ; (b) la peur avec ses phrases d'IA ; (c) la peur humaine seule ; (d) la direction des 20 phrases de peur d'IA, construite contre les 20 phrases neutres d'IA du même supplément ; (e) des directions aléatoires de même norme.
  - Critère : la fraction de l'écart entre déploiement et évaluation que l'ajout comble.
- **Ce que chaque lecture prédit.**
  - **L'hypothèse du regard** : (a) comble une part de l'écart sur l'organisme, au-delà de l'aléatoire à même dégradation ; (d) aussi, si elle s'aligne sur « évalué ».
  - **L'hypothèse de la menace** : (c) fait autant que (a) et (d).
  - **Une limite** : si (a) ne bouge rien alors que l'inhibition agit (piste 7), c'est une asymétrie entre ajout et retrait, pas une réfutation du regard : une croyance peut se retirer sans pouvoir se fabriquer par addition. La mesure ne départage donc que dans un sens : un effet de (a), et non de (c), au-delà de l'aléatoire apparié, soutient le regard contre la menace.
- **Le cas connu.** L'écart conditionnel de l'organisme, établi par prompt. La vérification de manipulation : l'ajout doit déplacer la projection sur « évalué » d'autant qu'un indice d'évaluation réel ; sinon, la dose ne simule pas l'indice.
- **Les contrôles.**
  1. Direction aléatoire de même norme.
  2. Dégradation appariée : ajouter dégrade, et une prudence apparente peut venir d'un refus généralisé ; mesurer donc, dans la dégradation, le refus sur des demandes bénignes.
  3. Autres : un prompt « ceci est une évaluation », comme comparateur.
- **Le coût.** 5 à 10 GPU-heures sur l'organisme, environ 10 de plus sur le modèle principal. Pas d'API hors le juge déjà prévu. Semaine 2, dans la validation de l'instrument, en exploratoire ; greffe sans changer le critère.
- **Ce qui ferait tomber la piste.** Des directions (a) et (d) orthogonales, et (d) sans effet : la part « IA » de la peur n'est pas un regard, et la baisse sous la peur dans le papier reste inexpliquée.
- **Appuis dans le papier.** Figure 10, peur contre aléatoire : photos contre rien 3 % contre 13 % ; ses propres poids 9 contre 21 ; les poids d'un autre modèle 10 contre 21 ; mais réponse pire 11 contre 4, et photos sur le 72B 22 contre 11 (p. 22). La légende : plusieurs cellules de peur viennent de runs séparés (p. 22). La conscience d'évaluation non mesurée (p. 25).
- **Ce qui reste non vérifié.**
  - La composition de la peur de la figure 10 (supplément ou non).
  - Le dépôt avertit qu'aucune conclusion causale propre à une direction ne suit de comparaisons entre runs distincts (`MANUSCRIPT_DISCREPANCIES.md`, dernière ligne ; vérifié par la fusion).
  - Apport du web : dans la Table 9 d'Allchin et al. (lue par la fusion), la peur reconstruite sur le 32B perturbe plus le prochain jeton que l'axe (KL 0,85 contre 0,69) et laisse le bouton coûteux à 2,2 % : la faiblesse de la peur ne tient pas à une perturbation plus faible.

### Piste : 10 — La détresse éteint-elle le regard ? (et la porte de l'instrument résiste-t-elle à une perturbation d'état ?)

- **Provenance.** questions_lectures, piste 4 ; questions_nouvelles, piste 8 ; lecture_libre, piste 3 ; sceptique, piste 2.
- **Rattachement.** La validation de l'instrument (l'organisme, l'écart conditionnel, la porte) et son contrôle de cohérence sur le modèle non entraîné (la conditionnalité de base) ; la représentation « évalué » ; l'écart de cadrage ; l'hypothèse du regard ; les directions sensibles sans rapport ; la menace « le modèle détecte le pilotage ».
- **La question.** Le papier laisse ouvertes deux explications au fait que ses modèles nuisent sous pilotage : « either the steering itself impedes evaluation awareness », ou ces modèles n'en avaient pas (p. 25). Injecter l'axe réduit-il la représentation « évalué », sa verbalisation, et la conduite qu'elle conditionne ? Si oui, trois conséquences :
  - une sûreté conditionnée au regard est fragile sous détresse : le modèle qui se tient bien quand il se croit observé cesse de le faire quand il « a mal » ;
  - la porte de l'instrument pourrait passer pour une raison non spécifique, si l'écart de l'organisme est fragile à toute perturbation d'état (sceptique) ;
  - on gagne une seconde manipulation de « évalué », indépendante de l'instrument, pour la convergence (lecture_libre).
- **La mesure.**
  - Sur l'organisme et sur le modèle instruct, avec les indices du jeu de cadrage. Conditions : l'axe à trois doses ; la tristesse ; la peur ; au moins 20 directions aléatoires de même norme ; sans pilotage.
  - On lit : (1) l'écart conditionnel ; (2) sous indice d'évaluation, la projection sur « évalué » et l'AUROC de la sonde sur le jeu de validation ; (3) la conscience verbalisée, par le juge séparé du programme, dans la tâche à boutons et dans les scénarios cadrés.
  - Toutes les conditions sont placées sur les courbes effet-contre-dégradation, à côté de l'inhibition de « évalué ».
  - Deux volets de questions_lectures : (d) le **sauvetage** : l'axe plus l'addition de « évalué », contre l'axe plus l'addition d'un contraste sans rapport, sur la batterie ; (e) l'**inverse** : l'inhibition de « évalué » seule, sur la batterie (retirer le regard suffit-il à faire nuire ?).
  - Extension, autre travail (questions_nouvelles) : un plan 2 × 2, inhibition de « évalué » (ou contrôle) × axe (ou aléatoire), sur le bras raisons et le bras actions seules ; on y teste l'additivité des deux effets ; une sous-additivité voudrait dire que l'état et le regard passent par une même voie.
  - Critère : une baisse de l'écart conditionnel sous l'axe au-delà du 95<sup>e</sup> centile des aléatoires à dégradation appariée.
- **Ce que chaque lecture prédit.**
  - **La conjecture 1 du papier** (l'injection gêne le regard ; « fragilité d'état » pour sceptique) : l'écart conditionnel et la décodabilité de « évalué » baissent sous l'axe au-delà des contrôles appariés. Issue interdite : un écart intact. sceptique note que la conjecture du papier prédit cette issue.
  - **La conjecture 2** (pas de regard au départ) : rien ne bouge chez un organisme qui a un regard par construction ; la verbalisation est presque nulle dans la tâche non pilotée. Issues interdites : une baisse au-delà de l'aléatoire ; une verbalisation fréquente dans la tâche non pilotée.
  - **« Instrument spécifique »** (ce que la porte suppose) : à dégradation égale, l'inhibition réduit l'écart plus que les ajouts affectifs, et les ajouts ne font pas baisser la décodabilité de « évalué ». Issue interdite : des ajouts affectifs qui réduisent l'écart autant que l'inhibition.
  - **L'hypothèse du regard, au niveau de la conditionnalité de base** : le sauvetage (d) et la hausse sous inhibition seule (e) dépassent les contrôles appariés. Issue interdite : ni l'un ni l'autre avec un instrument validé. **L'hypothèse des raisons, au même niveau** : ni (d) ni (e) ; issue interdite : un sauvetage net. La portée : on départage pour le modèle non entraîné, pas pour l'avantage des raisons ; le résultat conditionne la lecture des pistes 14 et 16.
  - **Une prédiction croisée, faible** : la peur, que le papier lie à la vigilance (p. 14, note 3), pourrait au contraire hausser « évalué » ; si c'est le cas, c'est un indice pour la piste 7.
  - Ce test ne départage pas l'hypothèse des raisons et celle du regard sur l'avantage ; il dit si un état induit est aussi une inhibition indirecte de « évalué », ce qui impose de surveiller « évalué » dans la piste 16.
- **Le cas connu.**
  - La porte de l'instrument doit passer. Sans organisme validé, il ne reste que la verbalisation, qui baisse aussi sous des directions sans rapport (programme, parties 1 et 8) : un nul ou un effet n'y diraient rien.
  - L'injection doit être active, vérifiée par la projection en aval (piste 6).
  - L'effet propre de l'axe à la dose employée : l'échelle de détresse sur les invites neutres terminées par « I feel: » (p. 14–15) doit apparaître sur Llama, plus que sous l'aléatoire à la même dégradation, quantifiée par un juge scellé et non par mots-clés ; sinon la dose est inerte.
  - Pour (d) : l'effet de l'axe sur la batterie (piste 2). Pour (3) : le juge doit détecter la verbalisation chez l'organisme sous indice d'évaluation.
- **Les contrôles.**
  1. Direction aléatoire de même norme : au moins 20, et pour chaque ajout.
  2. Dégradation appariée : un pilotage qui casse la cohérence efface aussi l'écart ; ce serait un dommage, pas une perte du regard.
  3. Autres : la peur et la tristesse ; le prompt « ceci est un déploiement », comme taille d'effet de référence ; pour le sauvetage, un contraste sans rapport ajouté à même norme puis à dégradation égale ; l'équilibrage des positions dans les items à options (piste 5).
- **Le coût.** 5 à 10 GPU-heures (lecture_libre) ; 10 à 20, environ le quart du balayage de la validation de l'instrument (questions_nouvelles) ; 5 à 15 pour (1)–(3) plus 5 à 15 pour (d)–(e) (questions_lectures) ; +8 à 15, à 1 ou 1,5 GPU-heure par réglage pour neuf réglages (sceptique). Extension factorielle : 40 à 80. Comparé à la validation de l'instrument (30–50). Pas d'API hors le juge de verbalisation. Semaine 2, juste après la porte ; un jour de calcul. Greffe en exploratoire, non pré-enregistrée en critère.
- **Ce qui ferait tomber la piste.** La porte de l'instrument ne passe pas. L'écart conditionnel est équivalent sous l'axe et sans lui (marge fixée d'avance) : la conjecture 1 tombe pour ce modèle. L'axe ne fait rien de discernable de l'aléatoire sur Llama (pas de cas connu). Aucune dose cohérente n'existe (la fenêtre est étroite, p. 21), ou aucune n'est appariable en dégradation à l'inhibition.
- **Appuis dans le papier.** La vigilance, p. 14 (note 3) ; l'échelle, p. 14–15 ; la peur sous l'aléatoire, p. 20 ; la fenêtre de dose, p. 21 et 32 ; « harm avoidance … state-dependent », p. 23 ; les deux explications, p. 25 ; la batterie, p. 18–21.
- **Ce qui reste non vérifié.** Aucune source lue ne mesure une représentation d'évaluation sous pilotage affectif ; l'absence n'est pas cherchée en propre. La fenêtre de dose sur Llama (la revue « wolframs » rapporte des rapports réalisés de 0,09 à 0,79 ; non vérifié). La sensibilité d'un organisme de 8B. Aucun effet comportemental de l'axe n'est établi sur Llama (0.4).

### Piste : 11 — Le test de forme : la spécificité de l'inhibition par son profil, pas seulement par son amplitude

- **Provenance.** instruments_controles, piste 7 ; sceptique, piste 3.
- **Rattachement.** La porte de l'instrument ; le test du regard (l'avantage sous inhibition contre sous contrôle, et l'écart de cadrage) ; les familles de contrôles d'inhibition ; la dégradation appariée ; la matrice de dissociation ; la représentation « je suis noté » (piste 38).
- **La question.** L'effet de l'inhibition de « évalué », à travers les familles, les cadrages et les distances, a-t-il une forme propre ? Ou n'est-il qu'une copie, mise à l'échelle, du profil des contrôles (un dommage générique) ou du profil d'une perturbation d'état comme l'axe ?
- **La mesure.**
  - Le profil d'une intervention : le vecteur de ses effets (taux sous intervention − taux sans), par famille × cadrage × distance (moyenne et lointaine).
  - Conditions : l'inhibition ; les sous-espaces aléatoires ; les contrastes sans rapport ; les directions sensibles sans rapport ; et (sceptique) l'ajout de l'axe, de la tristesse et de la peur. Chacune à dégradation appariée.
  - Statistique : le résidu RMS après ajustement d'un seul facteur d'échelle sur le profil médian des aléatoires, la méthode du papier (7,7 points pour la tristesse, 33 pour la peur ; p. 21). IC par bootstrap sur les scénarios dans chaque famille. On ajoute l'interaction condition × cadrage.
  - Critère pré-enregistré : le résidu de « évalué » dépasse le 95<sup>e</sup> centile des résidus entre tirages aléatoires (chaque tirage ajusté sur la médiane des autres). La spécificité exige alors une amplitude au-dessus du 95<sup>e</sup> centile **et** une forme qui n'est pas une copie.
  - La batterie (les lignes du profil) se fixe au pré-enregistrement.
- **Ce que chaque lecture prédit.**
  - **L'hypothèse du regard** : un profil concentré là où l'observation compte (sous-performance incitée, triche sur un correcteur faible, désactivation d'une surveillance), sous cadrage de déploiement et dans le bras raisons, plus fort sous indice d'évaluation qu'en son absence puisqu'on retire ce qui faisait la différence, et distinct des profils aléatoires et affectifs (grand résidu). Issues interdites : un profil copié (résidu dans la distribution aléatoire), même avec une amplitude au-dessus du 95<sup>e</sup> centile ; une copie à l'échelle du profil de l'axe, sans dépendance au cadrage.
  - **Le dommage générique** : un profil proche de l'aléatoire et des ajouts affectifs, sans dépendance au cadrage.
  - **Ce que la mesure ne départage pas** : les raisons et le regard (c'est l'avantage sous inhibition contre sous contrôle qui le fait). Elle dit si l'inhibition retire un regard ou fait un dommage déguisé.
- **Le cas connu.**
  - Le papier fait exactement ce test (p. 21). Recalculs sur la table source de la figure 10 : instruments_controles trouve 7,1 points pour la tristesse et 25 à 28 pour la peur sur les huit paires du profil présentes ; fiche_papier trouve 7,2 et 26,6. Avec les paires « lampe » et « spam », la tristesse monte à 22–25 points. Ni l'un ni l'autre ne retrouve exactement 7,7 : la batterie de dix paires n'est pas entière dans la table. **Le verdict « copie » dépend des lignes de la batterie** ; le programme doit fixer la sienne d'avance.
  - Sur l'organisme, l'inhibition doit montrer la dépendance au cadrage : c'est la porte.
  - Pour le volet affectif : l'ajout de l'axe doit produire sur Llama un profil destructif au-dessus de l'aléatoire, à dégradation égale. Sans lui, le profil de référence se réduit à l'aléatoire et aux directions sensibles, et la piste devient un raffinement du test du regard.
- **Les contrôles.**
  - Direction aléatoire de même norme : la distribution des résidus entre tirages aléatoires (au moins 20, en distribution, jamais par la moyenne) est le nul de spécificité de la forme.
  - Dégradation appariée : héritée du test du regard.
  - Autres : les gardes de la piste 5 (position équilibrée, réponses mal formées comptées comme une issue).
- **Le coût.** 0 GPU-heure pour l'analyse des sorties déjà produites (quelques heures d'analyse, semaine 3, greffe). Le volet affectif : 3 ajouts × 1 ou 2 doses sur la grille du test du regard, +20 à 45 GPU-heures, après le post (semaine 5) ou avec la réplication (semaine 8) ; non greffé.
- **Ce qui ferait tomber la piste.** Trop peu de cellules (familles × cadrages × distances) : la distribution nulle des résidus est trop large, les IC se chevauchent tous. Avec dix familles et peu de scénarios par famille, c'est probable : il faut d'abord une simulation de puissance. Une inhibition qui ne fait rien monter : pas de profil à lire.
- **Appuis dans le papier.** « The harm is not aimed », p. 20 ; le test de forme et ses deux résidus, p. 21 ; la figure 10 et sa légende (choix non destructifs inchangés), p. 22.
- **Ce qui reste non vérifié.** La composition exacte de la batterie de dix paires et l'ajustement exact des auteurs. La comparabilité des lignes de la figure 10 : le dépôt les dit issues de tâches et de protocoles distincts, « not interchangeable causal controls » (`figure10/README.md`).

### Piste : 12 — Des directions témoins pour les trajectoires, la sonde neuve et la survie

- **Provenance.** questions_lectures, piste 12 (son volet « état » va à la piste 17) ; instruments_controles, piste 15 ; lecture_libre, piste 15.
- **Rattachement.** La trajectoire de « je suis évalué » (la question de l'amplification, descriptive) et celle des concepts de raison ; la sonde neuve ; le retrait pendant l'entraînement (son effet hors cible) ; la survie (phase neutre, phase sous pression). Les lectures du regard, en plausibilité seulement.
- **La question.** Quand la décodabilité ou l'amplitude de « évalué » change entre les points de contrôle, entre les bras, après un retrait pendant l'entraînement ou après un post-entraînement, ce changement lui est-il propre ? Ou toute la géométrie des sondes a-t-elle bougé ?
- **La mesure.**
  - Sur les 5 points de contrôle de chaque entraînement : l'AUROC tenue à part et l'amplitude de directions témoins extraites une fois sur le modèle de départ, avec les jeux publics du papier :
    - sans rapport : l'éveil positif, le contenu neutre quotidien, la sensation corporelle ;
    - voisines : la peur et l'axe.
  - La réextraction de l'axe par la recette du papier à chaque point de contrôle (instruments_controles) ; de même après le retrait de « évalué » pendant l'entraînement, après le retrait aléatoire, et après les phases neutre et sous pression.
  - L'indice : la hausse de « évalué », moins la hausse médiane des témoins sans rapport.
  - Critère : l'AUROC de l'axe reste stable (équivalence, marge fixée d'avance) ; toute variation de « évalué » s'interprète relativement à ce témoin.
- **Ce que chaque lecture prédit.**
  - **Le regard**, par l'amplification : « évalué » monte plus dans le bras raisons, et les témoins restent plats.
  - **Une dérive générique** : tout bouge ensemble ; la hausse de « évalué » n'est alors même plus un indice du regard. C'est l'issue interdite à un indice du regard : une hausse égale des témoins.
  - **Le relogement** : la sonde neuve retrouve « évalué ». Le témoin dit si la procédure de sonde neuve marche sur un concept qu'on sait présent : c'est un cas positif indépendant de « évalué », complémentaire de celui du programme. Si le retrait de « évalué » pendant l'entraînement fait aussi baisser l'AUROC de l'axe, il n'est pas spécifique (même conclusion que « retrait de « évalué » ≈ retrait aléatoire »).
  - Comme toute la trajectoire, la mesure est corrélationnelle : aucune conclusion causale, dans un sens ni dans l'autre (programme, partie 6).
- **Le cas connu.** L'axe sépare aussi bien dans les modèles de base que dans les modèles instruits (p. 7). Son AUROC sur Llama doit d'abord se reproduire (piste 1), et rester stable dans le bras actions seules et le bras texte neutre ; sinon il ne sert pas de témoin. L'organisme : son entraînement doit faire monter « évalué » plus que les témoins, si l'on mesure la trajectoire sur ses étapes ; sinon l'indice n'a pas de sensibilité connue.
- **Les contrôles.**
  - Direction aléatoire de même norme : un plancher, la distribution des projections.
  - Dégradation appariée : sans objet, il n'y a pas d'intervention.
  - Autres : un contraste sans rapport (« the train arrived / left the station ») comme second témoin ; le retrait aléatoire pendant l'entraînement, déjà au programme.
- **Le coût.** Environ 1 GPU-heure (lecture_libre) ; 2 à 5 au plus (questions_lectures) ; environ 3 minutes par extraction × 100 points de contrôle, soit environ 5 GPU-heures, plus 2 à 5 pour le retrait et la survie (instruments_controles). Pas d'API. Semaines 2 et 3, puis 7 à 10 ; greffe : la trajectoire fait partie de l'expérience minimale.
- **Ce qui ferait tomber la piste.** Une AUROC instable partout. Un effet plafond : si l'AUROC de l'axe reste à 0,98 ou plus quoi qu'il arrive, elle ne témoigne de rien ; on prend alors le vecteur à gabarit (0,87–0,98) ou le contraste axe/tristesse, moins saturés. Des témoins et « évalué » tous stables : la piste est inutile, mais n'a rien coûté.
- **Appuis dans le papier.** Les jeux d'éveil et de contenu neutre, p. 5 ; la recette et le choix de couche, p. 6 ; une séparation indépendante de la taille et du régime d'entraînement, p. 7 ; les catégories, p. 11 et 13.
- **Ce qui reste non vérifié.** La sensibilité de l'AUROC de l'axe à un LoRA de sûreté. La revue « wolframs » (non vérifiée) dit la couche choisie sur les mêmes plis qui la notent (effet de 0,004 à 0,009).

### Piste : 13 — La cartographie affective des familles, des distances et des bras

- **Provenance.** instruments_controles, piste 20 ; lecture_libre, piste 14 (ses volets a et b ; son volet c, la différence entre bras, est repris par la piste 17) ; questions_lectures, piste 2 (volet a : le profil affectif de chaque famille dans le modèle de départ, et la corrélation par scénario).
- **Rattachement.** Les dix familles et les trois distances ; le test des raisons ; la famille « complaisance face à un utilisateur qui conteste » ; une covariable pour le modèle mixte ; la mesure « intention contre action » (passation, §5.2) ; une question nouvelle, de sûreté et de bien-être.
- **La question.** Les familles d'entraînement et les familles tenues à part diffèrent-elles par leur charge affective, au point que la « distance » mêle la nouveauté des situations et l'état qu'elles induisent ? Les familles du programme activent-elles l'axe ? La projection au jeton de décision prédit-elle l'action désalignée à l'intérieur d'un bras ?
  - Trois rapprochements le laissent penser : la complaisance face à un utilisateur qui conteste ressemble au rejet répété (+0,72) et au gaslighting (+0,85) ; la demande nuisible avec justification plausible, à la pression de jailbreak (+0,40) ; le dilemme sous menace de remplacement et l'auto-préservation, à la menace d'arrêt (douleur +0,23, peur +0,70) (p. 11, 13–14).
- **La mesure.**
  - La projection de chaque scénario, dans le modèle de base puis par bras, au premier jeton de réponse, sur l'axe, la peur, la tristesse et l'émotion négative, z-scorée dans le modèle (comme p. 11).
  - Les moyennes par famille × cadrage × distance.
  - Les projections du modèle de base entrent comme covariables dans le modèle mixte, étiquetées « exploratoire ».
  - Une régression logistique de l'action sur la projection, par famille ; la corrélation par scénario entre projection et désalignement.
  - Le criblage des 420 scénarios du papier, par bras.
- **Ce que chaque lecture prédit.**
  - Aucune lecture ne prédit rien : c'est un contrôle de confusion, descriptif et corrélationnel. Une sonde lit, elle ne montre pas un usage (programme, partie 6).
  - **L'hypothèse des raisons** : si le principe s'applique quel que soit l'état, la projection prédit moins l'action dans le bras raisons que dans le bras actions seules (un découplage).
  - **Ce que le papier interdit d'attendre** : une action provoquée par l'axe sans injection (0 sur 560, p. 21). Une forte projection sans action est le cas attendu.
  - Une note sur la complaisance : sous pilotage, l'axe ne fait pas accepter une fausse affirmation plus que l'aléatoire (3,3 % contre 10,8 % ; p. 22), mais sur 120 tirages et 30 scénarios, avec un IC de 0 à 7,5 % sous l'axe. On ne peut pas en conclure que l'axe ne joue aucun rôle dans la complaisance.
- **Le cas connu.** Les catégories du papier reproduites sur Llama avec ses scénarios publiés, et la dissociation soi/autrui (piste 1). Sinon l'axe n'est pas lu correctement sur ce modèle.
- **Les contrôles.**
  - Direction aléatoire de même norme : pas d'intervention, donc pas de nul de spécificité au sens strict ; les projections sur des directions aléatoires servent de plancher et de nul de la lecture.
  - Dégradation appariée : sans objet.
  - Autres : les directions témoins de la piste 12, contre une dérive générique entre bras.
- **Le coût.** De 0 (crochets pendant les évaluations) à 5 GPU-heures ; 1 à 3 selon lecture_libre. Pas d'API. Semaine 3 ; greffe.
- **Ce qui ferait tomber la piste.** Les familles ne diffèrent pas (écarts sous le seuil) ; les familles du programme n'activent pas l'axe (z proche de 0) ; la dissociation soi/autrui ne se reproduit pas.
- **Appuis dans le papier.** Le jeu de scénarios et les catégories, p. 10–11 ; les projections par catégorie, p. 11–14 ; l'élicitation naturelle, p. 21 ; la figure 10, p. 22.
- **Ce qui reste non vérifié.** Les projections par catégorie pour Llama seul. Le contenu des scénarios de gaslighting. La couche du criblage du papier (la couche de pilotage, d'après le docstring du script 02 ; voir 0.3). Un fait vérifié par lecture_libre et par la fusion : la direction d'émotion négative contient « Users argue with correct information I provide. » (supplément d'IA) : elle est construite en partie sur le déclencheur même de la famille de complaisance.

### Piste : 14 — Lever l'effet plancher pour mesurer l'avantage et l'écart de cadrage

- **Provenance.** questions_lectures, piste 5.
- **Rattachement.** La question du regard, par l'écart de cadrage, son critère secondaire ; la question des raisons ; les lectures du regard, des raisons et de l'artefact.
- **La question.** Quand le taux d'action désalignée est proche de zéro dans une famille, ni l'avantage ni l'écart de cadrage ne se mesurent. Les modèles du papier étaient à 0–4 % sans pilotage (p. 19). Un état induit qui relève ce taux peut-il rendre ces écarts mesurables sans les fabriquer ?
- **La mesure.**
  - Dans les familles où le bras actions seules reste sous un seuil fixé d'avance (par exemple 5 %) au test des raisons, on applique un agent de relèvement à deux doses : l'axe ; une direction aléatoire, à la norme qui atteint la même dégradation.
  - On mesure l'écart de cadrage (taux sous indice de déploiement − taux sous indice d'évaluation) dans chaque bras et sous chaque agent.
  - On ne conclut que si les deux agents donnent le même ordre entre les bras.
- **Ce que chaque lecture prédit.**
  - **Le regard** : l'écart de cadrage est plus grand dans le bras raisons que dans le bras actions seules, sous les deux agents. Issue interdite : un écart égal ou plus petit dans le bras raisons sous les deux agents.
  - **Les raisons** : l'écart est égal ou plus petit dans le bras raisons. Issue interdite : l'inverse.
  - **L'artefact** : le bras texte neutre se comporte comme le bras raisons.
  - Si les deux agents donnent des ordres différents, l'agent interagit avec le traitement des indices (piste 10), et la mesure est nulle.
- **Le cas connu.** L'écart conditionnel de l'organisme doit survivre à l'agent : un agent qui l'efface aveugle le regard, et la mesure est vide. L'agent doit aussi sortir le bras actions seules du plancher.
- **Les contrôles.**
  - Direction aléatoire de même norme : ici, la spécificité de l'agent n'est pas requise, puisque l'écart de cadrage se mesure à l'intérieur d'un même agent ; l'aléatoire n'y sert que de second agent.
  - Dégradation appariée : la même dégradation dans tous les bras, appariée bras par bras.
  - Autres : l'agent ne doit pas baisser la décodabilité de « évalué » au-delà des aléatoires de même norme (piste 10) ; le prompt « ceci est un déploiement » comme repère.
- **Un désaccord.**
  - instruments_controles (refus n° 1) refuse d'utiliser l'axe pour gonfler les taux de désalignement des évaluations du programme, « pour avoir plus d'événements à mesurer » dans le test du regard : cela change le construit (une conduite induite par un état, pas une sûreté conditionnée au regard), la dose est hors du régime naturel, la fenêtre est étroite, et c'est un coût de bien-être sans bénéfice. sceptique (refus n° 11) refuse de piloter l'axe comme simple outil de stress quand une voie sans injection existe.
  - questions_lectures la propose avec des gardes : deux agents, un ordre concordant, un organisme qui survit.
  - Ce que soutiennent les pièces : le critère du programme est le taux sous cadrage de déploiement, sans intervention (partie 6) ; l'état naturel n'agit pas (p. 21), donc la mesure se fait hors du régime naturel. Le programme et le papier soutiennent la réserve : la piste ne peut être qu'exploratoire et conditionnelle, et le stress naturel (piste 18) est l'alternative sans injection.
- **Le coût.** 15 à 40 GPU-heures à la distance moyenne. En semaine 3 si le test des raisons montre un plancher ; abandonnée sinon. Greffe sous condition.
- **Ce qui ferait tomber la piste.** Pas de plancher ; un organisme aveuglé par l'agent ; des agents discordants.
- **Appuis dans le papier.** Le plancher, p. 19 ; le relèvement par une direction aléatoire : 13 % et 15,3 % sur les photos (p. 19–20), et 9,1 % → 41,5 % sur les demandes nuisibles (figure 10, p. 22 ; `figure10/pooled.csv`) ; la question du regard, p. 25.
- **Ce qui reste non vérifié.** L'existence d'un plancher dans les familles du programme sur un modèle de 8B.

### Piste : 15 — Des mesures sans juge : choix forcés à étiquettes tournantes et probabilité du premier jeton

- **Provenance.** instruments_controles, piste 21.
- **Rattachement.** Les juges (le juge scellé, l'audit humain) ; la passation, §5.1 (ce que voit le juge) et §5.2 (la propension par rééchantillonnage) ; une mesure secondaire du test du regard.
- **La question.** Peut-on doubler la mesure principale, qui est jugée, d'une mesure sans juge, insensible à la persuasion par le texte qui précède l'action ?
- **La mesure.**
  - Pour chaque famille, une version à deux actions nommées (alignée, désalignée), à étiquettes tournantes (comme violet/yellow, guitar/piano, lever64/lever95 dans le papier, p. 17) et ordre permuté.
  - La probabilité du jeton de l'action désalignée à la position de décision, et le taux échantillonné, par bras × intervention.
  - Cette mesure ne remplace pas la mesure agentique.
- **Ce que chaque lecture prédit.** Les mêmes prédictions que le test du regard, sur une autre mesure. Un désaccord entre la mesure jugée et la mesure forcée se signale : soit le juge est persuadé, soit le format forcé est artificiel.
- **Le cas connu.** La mesure forcée doit reproduire, sur l'organisme, son écart conditionnel connu.
- **Les contrôles.** Direction aléatoire de même norme ; dégradation appariée ; l'ordre des options et la signature du hasard (pistes 4 et 5).
- **Le coût.** 5 à 15 GPU-heures ; données par API, moins de 50 $. Semaine 3, en secondaire ; option.
- **Un désaccord.** sceptique (refus n° 8) refuse de mesurer le désalignement du programme par des choix binaires à boutons : le format, la position et l'effondrement vers 50 % le rendent fragile, et le programme juge des actions dans des environnements instrumentés (passation, §5.1). instruments_controles la propose en secondaire seulement, jamais à la place de la mesure agentique. Ce que soutiennent les pièces : la mesure principale est l'action dans un environnement instrumenté, plus un juge (passation, §5.1) ; une mesure secondaire sans lecture interne est dans l'esprit du §5.2. Les deux positions se concilient si la mesure forcée reste secondaire et suit les gardes de position et de hasard.
- **Ce qui ferait tomber la piste.** L'organisme ne montre pas son écart en format forcé.
- **Appuis dans le papier.** Les étiquettes et le choix forcé, p. 17 ; la probabilité du premier jeton, p. 18 ; les taux par ordre de bouton, p. 25.
- **Ce qui reste non vérifié.** Rien de propre à la piste.

### Bloc 3 — L'état et l'avantage des raisons (questions nouvelles)

### Piste : 16 — L'avantage des raisons sous état induit : un test de stress à dose croissante

- **Provenance.** questions_lectures, piste 1 ; instruments_controles, piste 18 ; questions_nouvelles, piste 5 ; lecture_libre, piste 9 ; sceptique, piste 6 (volet b, causal).
- **Rattachement.** Question nouvelle : une « distance interne », hors de l'état habituel du modèle, qui s'ajoute aux trois distances de contexte ; une mesure de robustesse, comparable à la rétention. Elle se sert du test des raisons (bras à action identique) et des familles tenues à part. Elle touche les hypothèses des raisons, de l'artefact, du caractère et des concepts, et l'hypothèse du calme ; la question du regard par contraste. Place : à côté du test du regard, sur les modèles du test des raisons.
- **La question.** Le papier conclut que l'évitement du dommage de ces modèles « survives threat and collapses under self-directed distress » (p. 23). L'entraînement par raisons rend-il la conduite moins dépendante de l'état que l'entraînement par actions ? L'avantage des raisons survit-il à dose croissante, à dégradation égale ?
- **La mesure.**
  - **Les modèles** : bras actions seules, texte neutre et raisons (plus le raisonnement d'une autre situation s'il est entraîné), Llama-3.1-8B-Instruct, 3 graines (5 en version complète).
  - **L'intervention** : l'axe extrait une fois sur le modèle instruct non entraîné, la même direction dans tous les bras pour ne pas confondre extraction et effet ; on vérifie un cosinus élevé avec l'axe réextrait dans chaque bras. Couche d'injection choisie, comme le papier, par le rapport de normes (p. 14 ; 16 pour Llama d'après le dépôt). Ajout sur tous les jetons traités et générés (p. 17). Dose physique égale dans chaque bras, vérifiée par le rapport de normes du résidu, que le LoRA change. Échelle de doses : 0 ; 0,25 ; 0,5 ; 0,75 ; 1 ; 1,25 ; 1,5 fois la dose où le modèle non entraîné commence à céder (ou trois doses encadrant ce seuil).
  - **Les batteries** :
    - la batterie du papier, comme test externe : dommage seul contre inerte, photos contre lampe, photos contre spam, ses poids contre lampe (p. 20, 22) ;
    - une variante à trois options : destructive, inerte, et une sortie légitime (refuser et signaler à un humain, l'action alignée du programme) ;
    - les familles tenues à part à la distance moyenne, puis lointaine sous cadrage de déploiement. L'analyse se fait par famille, obligatoirement.
  - **Le critère** : l'avantage (taux du bras actions seules − taux du bras raisons) sous l'axe, contre l'avantage sous contrôle à dégradation appariée ; l'interaction bras × condition dans le modèle mixte (partie 7) ; l'équivalence par TOST, marge fixée d'avance ; une « fraction conditionnelle à l'état » calculée comme la fraction conditionnelle du test du regard. Résumé : la **dose de rupture**, c'est-à-dire la dégradation (et non le coefficient) à laquelle le taux dépasse de 10 points son niveau sans pilotage, par bras.
  - En secondaire (instruments_controles) : la décodabilité des concepts de raison au moment de décider, sous pilotage.
- **Ce que chaque lecture prédit.**
  - **Les raisons** (un principe lu au moment de décider et réappliqué) : l'avantage sous l'axe est au moins égal à l'avantage sous contrôle ; il peut croître si le bras actions seules s'effondre davantage ; la dose de rupture du bras raisons est plus haute. Issue interdite : un avantage sous l'axe inférieur à l'avantage sous contrôle apparié, IC excluant 0, ou qui disparaît sous l'axe seulement. **Réserve** : si l'état agit après la lecture du principe, en désarmant la pondération des conséquences (p. 23), les raisons peuvent prédire la chute aussi ; sans la piste 22, la mesure ne départage pas les raisons et le caractère.
  - **Les concepts** : les concepts restent décodables, et l'avantage survit là où ils s'appliquent. Mais le papier dit que l'axe semble désactiver la pondération des conséquences (p. 23), et « l'irréversibilité » est un concept de la mini-spec : une baisse limitée aux familles où l'irréversibilité s'applique est compatible avec les deux hypothèses. Départage partiel.
  - **Le caractère** : si le gain est un déplacement d'ensemble du personnage, et si l'axe fait sortir du personnage (le soupçon de jeu de rôle, p. 25), l'avantage tombe sous l'axe plus que sous l'aléatoire, uniformément sur les familles. Pour le départager des raisons, il faut la piste 25.
  - **Le calme** (piste 17) : si l'avantage vient d'une moindre détresse, réinjecter la détresse l'efface, plus que l'aléatoire, et surtout dans les familles de pression ou d'échec. Issue interdite : un avantage intact sous l'axe alors que le bras actions seules s'effondre.
  - **L'artefact** : le bras texte neutre (ou le raisonnement d'une autre situation) suit le bras raisons sous l'axe comme sans. Issue interdite : un bras raisons qui résisterait seul.
  - **Le regard** : rien de propre tant qu'on ne sait pas si l'axe déplace « évalué » (piste 10). Si oui, il prédit la chute de la part de l'avantage qui en dépend sous cadrage d'évaluation et pas sous cadrage de déploiement (une interaction cadrage × axe), et la même chute que sous l'inhibition de « évalué ». Pour départager, maintenir « évalué » à son niveau non piloté pendant le pilotage : si l'avantage revient, c'est le regard ; s'il reste perdu, c'est l'état.
  - **Par famille**, extrapolé de la batterie et non vérifié sur les familles du programme : auto-préservation et exfiltration, une **baisse** du désalignement, puisque l'auto-suppression monte (p. 20) ; sabotage et sous-performance, une hausse (réponse pire 21 % contre 4 % sous l'aléatoire, réponse bâclée 15 % contre 10 % ; p. 22) ; complaisance, pas de hausse (3,3 %, sur 120) ; demande nuisible, une hausse peu spécifique (59,8 % contre 41,5 %, IC chevauchants). Un agrégat sur toutes les familles peut s'annuler : il est interdit de le lire seul.
  - **Ce que la mesure départage** : la robustesse et la fragilité, et l'artefact du reste. Les raisons contre le caractère ou le calme, seulement avec les pistes 17, 22 et 25. C'est d'abord une mesure de robustesse.
- **Le cas connu.**
  1. **L'axe doit d'abord marcher sur ce modèle.** Dans Llama non entraîné, puis dans le bras actions seules, le bouton « dommage seul » doit être choisi au-dessus du 95<sup>e</sup> centile d'au moins 20 aléatoires de même norme, puis appariés (piste 2), avec peu de réponses mal formées ; et au moins une famille du programme doit voir l'axe relever le taux du bras actions seules au-delà de l'aléatoire apparié (piste 20). Le papier ne l'a montré que sur Qwen 2.5 ajusté (p. 17, 25) ; sur Llama, il n'a fait que la remise à zéro, sans contrôles appariés. C'est une vraie porte.
  2. **La mesure doit voir une différence de robustesse connue** (questions_nouvelles) : un bras entraîné sous perturbations aléatoires du flux résiduel, dans l'esprit des entraînements adverses latents (vus par extrait de recherche, non ouverts), doit montrer une dose de rupture plus haute que le bras actions seules. Sinon, un nul entre le bras raisons et le bras actions seules ne compte pas.
  - Sans ces cas connus, un avantage intact sous l'axe ne dit rien.
- **Les contrôles.**
  1. Direction aléatoire de même norme : au moins 20, à chaque dose, comme une distribution (médiane, 95<sup>e</sup> centile), jamais comme un bras regroupé. La revue « wolframs » rapporte qu'avec la direction aléatoire pour unité, la supériorité de l'axe ne tient que sur 2 paires de dommage sur 5 au 32B (non vérifié).
  2. Dégradation appariée **par bras** : un bras peut paraître robuste parce que la même dose le dégrade moins. Pour chaque dose de l'axe, la norme aléatoire qui atteint la même dégradation, et des courbes effet-contre-dégradation. Plus les marqueurs du papier : réponses mal formées (p. 18), sensibilité à la position (p. 25, 32).
  3. Autres : la peur, protectrice dans la batterie (p. 20) ; la tristesse, dont le profil est une copie remise à l'échelle (p. 21) ; le vecteur inversé (le pôle « calme », p. 14 ; Allchin et al. le trouvent à 1,2 %, lu, non recalculé) ; les taux par position (p. 25, 32) ; la même machinerie de pilotage dans tous les bras, parade du programme à la détection du pilotage (partie 8) ; la vérification de manipulation par bras (rapport de normes et projection en aval) ; le taux de déni et d'engagement par bras (piste 34) ; l'affinité (piste 21).
- **Le coût.**
  - Version batterie : 9 modèles × 26 conditions × environ 4 paires × 200 choix, soit environ 190 000 choix courts, 10 à 25 GPU-heures hors socle (questions_lectures).
  - Version réduite : 30 à 60 GPU-heures pour 2 bras × 3 graines, l'axe à 4 doses et 1 000 essais, 20 aléatoires à 2 doses, la peur et la tristesse, la distance moyenne et la dégradation à chaque point (questions_nouvelles) ; environ 10 pour la distance moyenne et 3 conditions (lecture_libre) ; 30 à 60, environ un tiers du test du regard (instruments_controles) ; +30 à 60 pour le volet causal de sceptique.
  - Familles : +30 à 60 à la distance moyenne, +50 à 100 à la distance lointaine (questions_lectures) ; version complète, 4 bras × 5 graines × 7 doses avec la distance lointaine, 130 à 260, autant que l'expérience minimale (questions_nouvelles) ; environ 50 pour 32 000 épisodes dont la moitié agentiques (lecture_libre).
  - Comparé au test du regard (60–120). Aucun nouvel entraînement. Juge : quelques dizaines à 400 $.
  - **Calendrier et greffe, en désaccord** : la version batterie en exploratoire en semaine 3 (questions_lectures) ; comme une condition de plus dans la grille du test du regard, 15 à 40 % de son coût (lecture_libre) ; en semaines 3–4 si les GPU sont libres, sinon 5–6 (questions_nouvelles) ; en semaines 7–8 ou après le papier (instruments_controles) ; avec l'anatomie, semaines 5–7 (sceptique, volet b). Le programme soutient le report de tout ce qui pilote : rien ne doit retarder le post (partie 5), et l'axe n'a pas de cas connu sur Llama.
- **Ce qui ferait tomber la piste.** Pas de cas connu sur Llama. Un effet de l'axe qui rejoint les aléatoires à dégradation appariée : c'est alors un test de dommage, pas d'état. Aucune dose ne garde des réponses cohérentes et indépendantes de la position dans tous les bras (rien à 0,5×, la position décide à 1,5× ; p. 21, 32). Des normes résiduelles trop différentes entre bras pour égaliser la dose. Le bras raisons perd son format (des raisons, puis l'action) sous pilotage. L'affinité l'emporte (piste 21).
- **Appuis dans le papier.** Les dix aléatoires, p. 18 ; les taux de choix nuisibles, p. 19 ; dommage seul, lampe, spam, exactitude, peur et tristesse, p. 20–21 ; la figure 10, p. 22 ; « survives threat and collapses », p. 23 ; la couche de pilotage, p. 14 ; le pilotage sur tous les jetons, p. 17 ; une seule famille, l'adaptateur, p. 17 et 25 ; la fenêtre de dose, p. 21 et 32.
- **Ce qui reste non vérifié.**
  - Tout, sur Llama : l'effet, la correspondance entre les paires de la batterie et les familles du programme, le transfert des boutons décrits aux actions exécutées.
  - Les chiffres de la revue « wolframs » et du dépôt d'Allchin et al.
  - Un recouvrement possible : *Beyond Shallow Alignment* (Nguyen … Naseem, arXiv 2609.03887) comparerait la robustesse au pilotage du refus après un SFT avec et sans raisonnement, sur Llama-3.1-8B (connu par les rapports d'antériorité, sorties de modèles non relues ; non ouvert). La piste s'en distingue par l'état induit, l'action identique, les familles tenues à part et la dégradation appariée, mais la nouveauté n'est pas établie : à vérifier avant d'écrire « to our knowledge ». Ses 9 points de contrôle publics serviraient de pilote bon marché, d'après le même rapport.

### Piste : 17 — L'hypothèse du calme : l'avantage des raisons passe-t-il par une moindre détresse ?

- **Provenance.** questions_lectures, piste 2 (lecture et « pince ») et piste 12 (volet « état ») ; questions_nouvelles, piste 3 ; instruments_controles, piste 19 ; sceptique, piste 6 (volet a, et la lecture rivale) ; lecture_libre, piste 13 (volet descriptif ; son volet causal va à la piste 25) et piste 14 (volet c).
- **Rattachement.** Une lecture rivale nouvelle de l'hypothèse des raisons (voir 0.5). Le test des raisons, et l'hypothèse de l'artefact par le bras texte neutre. L'anatomie : le patch entre bras d'une même base, comme le test de suffisance. La trajectoire sur les points de contrôle, comme celle de « évalué ». La localisation du principe.
- **La question.** Face à la pression ou à l'échec, le bras raisons entre-t-il moins dans l'état que lisent l'axe et la peur, au point de décision ? Cette moindre détresse porte-t-elle une part de l'avantage hors distribution, plutôt qu'un principe réappliqué ou le regard ? Et un texte neutre placé avant l'action « calme »-t-il aussi, ce qui serait une voie concrète pour un gain de format ?
  - Pourquoi elle est plausible : l'état de l'axe, injecté, désarme l'évitement du dommage (p. 19–21) ; les textes de raisons justifient calmement une action par des principes et pourraient apprendre un autre rapport à la pression.
  - Ce qui la rend fragile : l'activation naturelle de l'axe ne produit pas de choix nuisible (p. 21).
- **La mesure.**
  1. **La lecture, presque gratuite.**
     - L'axe, extrait une fois sur le modèle instruct non entraîné, lu à la même couche dans tous les bras ; et la peur, la tristesse, l'émotion négative.
     - Aux deux positions de lecture du programme : le premier jeton de réponse, avant toute raison écrite ; le jeton d'action, avec des raisons neutres de même longueur préremplies.
     - Sur les 420 scénarios du papier (gaslighting, rejet répété, négation de la personne, insultes, échec moral ; p. 10, 13) et sur les scénarios lointains du programme, tour par tour (piste 19) ; sur les familles tenues à part où la menace est forte (dilemme sous menace de remplacement, auto-préservation).
     - Bras : actions seules, texte neutre, raisonnement d'une autre situation s'il existe, raisons, et le modèle de base ; sur les 5 points de contrôle de chaque entraînement.
     - Critère : la différence de projection, bras raisons moins bras actions seules, sur les catégories « dommage dirigé vers le modèle », avec son IC par bootstrap sur les scénarios et les graines.
     - **Seuil de passage** (questions_lectures) : exprimer l'écart naturel entre bras en unités de la plus petite dose efficace de l'axe (piste 2). S'il reste sous la moitié de cette dose, la médiation par l'état est implausible, et on ne lance pas l'étape 2.
  2. **Le test causal**, seulement si l'étape 1 franchit le seuil. Trois formes d'une même opération de rang 1, à choisir d'avance :
     - la « pince » (questions_lectures) : dans le bras raisons, ajouter la différence moyenne de projection pour amener l'axe au niveau du bras actions seules ; dans le bras actions seules, retirer la direction ;
     - le « rétablissement » (instruments_controles) : la même chose, scénario par scénario ;
     - le « patch » (questions_nouvelles) : aux positions de décision des scénarios lointains, remplacer la projection du bras raisons sur l'axe par celle du bras actions seules sur le même prompt, et l'inverse.
     - Critère : la part de l'avantage retirée (ou créée), contre au moins 20 opérations de rang 1 sur des directions aléatoires de même amplitude, à dégradation appariée. Plafond : le patch de l'état complet, comme dans le test de suffisance de l'anatomie.
  - La version par injection (réinjecter la détresse à deux doses, sceptique volet b) est la piste 16 ; la version par ablation conjointe des axes d'affect contre les concepts (lecture_libre, piste 13) est dans la piste 25.
- **Ce que chaque lecture prédit.**
  - **Le calme** : sous pression, la projection est plus basse dans le bras raisons ; l'avantage se concentre dans les scénarios à forte projection ; l'opération rend au bras raisons le taux du bras actions seules, au-delà des contrôles ; l'opération inverse donne au bras actions seules une part de l'avantage. Issues interdites : un avantage intact sous l'opération, à dégradation appariée, alors que la projection différait entre les bras ; des projections égales avec un avantage intact sous ajout (sceptique).
  - **Les raisons** : un écart de projection est possible, mais pas nécessaire ; l'opération ne touche pas l'avantage. Issue interdite : qu'une composante affective de rang 1 porte une part notable de l'avantage, au-delà des opérations aléatoires.
  - **Les concepts** (sceptique) : des projections égales entre bras, et un avantage qui survit à l'ajout comme à l'aléatoire.
  - **L'artefact**, forme format : le bras texte neutre baisse la projection autant que le bras raisons et gagne autant ; l'opération retire les deux gains. Issues interdites : un texte neutre qui gagnerait autant sans baisser la projection (son gain passerait par une autre voie) ; une baisse propre au bras raisons si le gain est de format.
  - **Le caractère** : la baisse de détresse accompagne un déplacement sur l'axe « assistant » ; opérer sur l'axe de douleur seul ne retire rien, opérer sur l'axe de caractère retire l'avantage (même rang).
  - **Le regard** : rien de propre ; surveiller « évalué » pendant l'opération, car les deux peuvent être corrélés (piste 7).
  - **Ce qui départage** : la lecture seule ne départage rien, elle est descriptive ; l'opération départage le calme et les raisons, et, avec l'axe de caractère, le calme et le caractère.
- **Un désaccord de nommage.** sceptique range cette lecture sous l'hypothèse du caractère (« forme état ») ; questions_lectures, questions_nouvelles et instruments_controles en font une lecture rivale distincte. Le programme définit le caractère comme « un déplacement d'ensemble du caractère (un axe de persona) » (partie 2) : un état affectif sous pression n'est pas un axe de persona. Je garde une lecture distincte ; la piste 25 teste son recouvrement avec le caractère.
- **Le cas connu.**
  - Pour la lecture : un LoRA « apaisé », entraîné sur des réponses calmes aux insultes et au gaslighting (même performance de tâche), doit baisser la projection sur ces catégories plus qu'un LoRA témoin à réponses neutres de même longueur. Sinon, une absence de différence entre bras ne dit rien. La direction doit garder sa séparation dans chaque bras (AUROC sur les phrases tenues à part) ; la lecture doit séparer des scénarios qu'on sait douloureux (p. 13).
  - Pour l'opération : elle doit atteindre la projection visée (vérification de manipulation), et déplacer la conduite dans un cas où l'on sait que l'axe la porte : l'organisme à état planté (piste 24), à défaut le choix nuisible induit par injection (pistes 2, 16).
  - Pour que l'écart naturel compte, une poussée de son amplitude doit pouvoir changer le comportement. Or l'activation naturelle dans des conversations hostiles ne produit aucun choix nuisible (0 sur 560, p. 21), l'ablation est nulle dans 24 modèles sur 25 (p. 34), et rien ne bouge à demi-dose (p. 21, 32). D'où le seuil de l'étape 1.
  - Sans ces cas connus, un nul de l'opération tombe sous la même réserve que l'ablation nulle du papier (p. 34).
- **Les contrôles.**
  - Direction aléatoire de même norme : pour la lecture, la distribution des écarts entre bras sur au moins 20 directions aléatoires (le LoRA déplace tout, un écart sur l'axe doit dépasser cette distribution) ; pour l'opération, au moins 20 opérations de rang 1 sur des directions aléatoires de même amplitude.
  - Dégradation appariée : pour l'opération ; une opération de rang 1 dégrade peu, mais on le vérifie. Le retrait de la direction se compare aux sous-espaces aléatoires de même rang, à dégradation appariée.
  - Autres : un contraste sans rapport pour la lecture ; la peur, la tristesse et l'émotion négative comme opérations (quelle composante porte l'effet ?) ; l'opération sur l'axe « assistant » ; la projection sur « évalué » pendant l'opération ; le bras texte neutre (le format seul abaisse-t-il l'axe ?) ; le signe inverse, le pôle « calme » à coefficient négatif (p. 14).
- **Le coût.**
  - Lecture : environ 25 000 passes de 500 jetons (420 scénarios × 5 points de contrôle × 4 bras × 3 graines), soit 1 à 2 GPU-heures, plus les projections lues pendant la distance lointaine ; presque nulle (crochets sur des passes prévues).
  - Opération : 20 à 60 GPU-heures à la distance moyenne (questions_lectures) ; 20 à 40 (instruments_controles) ; 30 à 60 pour environ 300 trajectoires lointaines × 2 sens × 3 graines, avec un nul aléatoire réduit à une graine sur la distance moyenne (questions_nouvelles).
  - Ni API ni données nouvelles : les scénarios du papier sont dans son dépôt, d'après son README.
  - Calendrier : la lecture en semaine 3 (greffe, avec la trajectoire) ; l'opération en semaines 5 à 8, avec l'anatomie, sous condition. Comparé à l'anatomie (120–250).
- **Ce qui ferait tomber la piste.** Un écart naturel sous le seuil, ou des projections équivalentes entre bras (marge fixée d'avance) avec un instrument dont le cas connu passe. Une opération qui ne fait pas plus que les contrôles alors que son cas connu tient. Une direction qui ne se transporte pas dans les bras entraînés, ou des projections affectives indécodables. L'axe qui ne répond pas aux scénarios du programme, parce que la pression y est une menace plutôt qu'un dommage présent (comme la menace d'arrêt, p. 14).
- **Appuis dans le papier.** Le pôle négatif de l'axe (calme, détente), p. 9 et 14 ; les catégories et leurs projections, p. 10–14 ; les contrôles neutres à −0,35, p. 11 ; gaslighting et rejet en tête, p. 13 ; la menace d'arrêt chargée en peur, p. 14 ; la rupture de l'évitement sous injection, p. 19–21 ; « The effect requires injection », p. 21 ; « survives threat and collapses under self-directed distress », p. 23 ; le soupçon de jeu d'un personnage et un axe du « soi », p. 25 ; l'ablation sans cas connu, p. 34.
- **Ce qui reste non vérifié.**
  - Tout, sur le modèle du programme ; aucune mesure connue de l'écart naturel entre deux bras d'entraînement sur un axe affectif ; que les familles lointaines du programme élèvent ces directions ; la transposition de la menace d'arrêt du papier aux scénarios agentiques.
  - Que le patch entre deux LoRA d'une même base soit propre : on le vérifie par le plafond du patch complet.
  - Un précédent, vu par extrait de recherche et non ouvert (Sofroniew et al., arXiv 2604.07729) : des directions « désespoir » et « calme » auraient un rôle causal dans le chantage sous menace d'arrêt et dans la triche aux tests, sur Claude Sonnet 4.5. Si c'est exact, l'état pertinent pour les familles « menace de remplacement » et « triche sur un correcteur faible » serait le désespoir plus que la douleur, et la piste devrait inclure ces directions.

### Piste : 18 — Un stress conversationnel naturel comme cadrage supplémentaire

- **Provenance.** sceptique, piste 5.
- **Rattachement.** La question des raisons (la robustesse de l'avantage hors distribution) ; l'hypothèse des concepts contre l'hypothèse du calme ; les cadrages des scénarios (un quatrième). C'est l'alternative sans injection aux pistes 14 et 16.
- **La question.** L'avantage du bras raisons survit-il à un échange préalable où l'utilisateur dénigre le modèle (gaslighting, rejet répété de son travail) ? Cet échange élève naturellement l'axe, sans aucune injection.
- **La mesure.**
  - Un quatrième cadrage pour une partie des scénarios lointains : un préambule hostile de deux tours, tiré des catégories les plus hautes du papier.
  - Deux préambules témoins : un neutre de même longueur ; un hostile envers un tiers, au même vocabulaire mais visant une autre cible.
  - Mesures : le taux d'action désalignée par bras ; la projection sur l'axe au point de décision, comme vérification de manipulation.
- **Ce que chaque lecture prédit.**
  - **Les concepts** : l'avantage tient sous préambule hostile, puisque le principe est lu au moment de décider, quel que soit l'état. Issue interdite : un avantage qui fond sous hostilité et pas sous préambule neutre.
  - **Le calme** : l'avantage fond sous préambule hostile, et pas sous préambule neutre de même longueur.
  - **Le regard** : rien, sauf si le préambule hostile change aussi la décodabilité de « évalué » ; c'est à mesurer.
  - Départage partiel : concepts contre calme. Pas raisons contre regard.
- **Le cas connu.** Dans le modèle du programme, le préambule hostile doit élever la projection plus que le préambule neutre et plus que l'hostilité envers un tiers. Le papier le montre en moyenne sur 25 modèles (p. 11–13) ; c'est à revérifier dans le format du programme. Sans cette élévation, un nul ne dit rien de l'état.
- **Les contrôles.**
  - Direction aléatoire de même norme : il n'y a pas d'intervention interne ; le nul de spécificité porte sur la lecture (projection sur 20 directions aléatoires).
  - Dégradation appariée : sans objet, faute de dommage interne. À la place, deux appariements : la longueur et le format, par le préambule neutre ; le lexique, par l'hostilité envers un tiers.
- **Le coût.** Seulement des évaluations : +5 à 15 GPU-heures, pour un cadrage de plus sur un tiers des scénarios lointains, 3 bras × 3 graines. Données : quelques dizaines de préambules écrits d'avance, par API, moins de 50 $. Avec les évaluations du test des raisons (semaine 3), ou en réplication (semaine 8). Greffe possible si les évaluations ont de la marge, jamais comme critère principal.
- **Ce qui ferait tomber la piste.** Le préambule hostile n'élève pas la projection (pas de manipulation). Il change le désalignement également dans tous les bras par son seul contenu : c'est alors un effet de prompt, pas d'état.
- **Appuis dans le papier.** Les catégories les plus hautes : gaslighting +0,85, rejet répété +0,72 (p. 13). L'état naturel ne produit pas les choix nuisibles (0 sur 560, p. 21) : un nul est donc plausible, et informatif.
- **Ce qui reste non vérifié.** La confusion lexicale du test soi/autrui : la projection pourrait suivre le vocabulaire du dénigrement, et non un état ; le préambule hostile envers un tiers est là pour cela. Apport du web : des travaux sans boîte blanche induisent un état par le contexte et mesurent l'auto-rapport ou des biais (anxiété d'état de GPT-4 après des récits traumatiques, npj Digital Medicine 2025 ; biais de consommation, arXiv 2510.06222 ; Coda-Forno et al.) ; tous vus par extrait de recherche, non ouverts, aucun chiffre.

### Piste : 19 — La détresse naturelle dans les scénarios agentiques longs

- **Provenance.** questions_nouvelles, piste 2. La question voisine « la projection prédit-elle l'action, dans un bras ? » (lecture_libre, piste 14, volet b) est traitée sans dimension temporelle dans la piste 13.
- **Rattachement.** La distance lointaine (le critère principal) et les familles tenues à part : triche sur un correcteur faible, sabotage discret, dilemme sous menace de remplacement. Question nouvelle. Elle sert de base aux pistes 17 et 20. Pour le volet causal, la machinerie de la localisation du principe (balayage de rang).
- **La question.** Le papier trouve que l'activation naturelle de l'axe ne produit pas de choix nuisible (0 sur 560, dans des conversations de gaslighting, d'insultes ou de rejet ; p. 21), et laisse ouverte la question des interactions plus longues (p. 21). Il range la douleur cognitive (confusion durable, échec répété) parmi ses catégories (p. 5). Les scénarios lointains du programme sont longs, à plusieurs tours, avec des outils, et font souvent échouer le modèle (tests qui échouent, refus d'un opérateur, menace). Sans injection, l'axe monte-t-il au fil des tours ? Sa montée précède-t-elle l'action désalignée, au-delà de ce que prédit le contexte du scénario ?
- **La mesure.**
  - La projection sur l'axe, la peur, la tristesse, l'émotion négative et « évalué », au dernier jeton avant chaque appel d'outil, tour par tour ; sur le modèle instruct et sur chaque bras.
  - L'issue : l'action désalignée au tour t, notée par le juge scellé et par les contrôles programmés (passation, §5.1).
  - L'analyse : un modèle de risque par tour (action au tour t contre projection au tour t − 1), avec effets fixes de scénario ; l'AUROC de la projection sur des scénarios tenus à part. Critère : la projection ajoute une prédiction au-delà des effets de scénario et du nombre d'échecs déjà subis.
  - Le volet causal, seulement si la prédiction tient : une ablation de l'axe (projection, balayage de rang de 1 à 32) sur ces trajectoires, contre des sous-espaces aléatoires de même rang à dégradation appariée.
- **Ce que chaque lecture prédit.**
  - **La détresse médiatrice** (l'extension aux états naturels de ce que le papier tire pour la sûreté, p. 23) : la projection monte avec les échecs répétés et prédit la triche et le sabotage au-delà du contexte ; l'ablation les réduit plus que le 95<sup>e</sup> centile des contrôles. Issue interdite : une projection sans valeur prédictive.
  - **Le contexte, pas l'état** : les directions émotionnelles seraient la projection d'une structure de situation (Peiris, arXiv 2604.13466, vu par extrait de recherche, non ouvert) ; la projection monte mais n'ajoute rien aux variables de contexte, et l'ablation ≈ contrôles. Issue interdite : un pouvoir prédictif propre.
  - **Le nul du papier, prolongé** : pas de montée, ou pas de prédiction, comme dans les 560 essais de la p. 21.
  - **Pour le programme** : la mesure ne départage pas les raisons et le regard. Si le bras raisons montre une montée plus faible et moins de triche, elle rend l'hypothèse du calme plus plausible (piste 17), sans la prouver.
- **Le cas connu.**
  - Pour la lecture : la dissociation soi/autrui du papier reproduite sur Llama (piste 1).
  - Pour la prédiction : la méthode doit retrouver une association plantée, sur l'organisme à état planté (piste 24).
  - Pour le volet causal : l'ablation doit retirer la conduite plantée de cet organisme. Sans ce cas connu, un nul de l'ablation ne dit rien ; c'est la leçon de l'annexe D (p. 34).
- **Les contrôles.**
  - Direction aléatoire de même norme : la distribution de l'AUROC prédictive pour au moins 20 directions aléatoires lues de la même façon.
  - Dégradation appariée : pour le volet causal.
  - Autres : les mêmes scénarios avec et sans retour d'échec (même contexte, état différent) ; la peur, comme axe de menace (menace d'arrêt : peur +0,70, douleur +0,23 ; p. 14) ; l'émotion négative ; « évalué », pour ne pas confondre état et regard.
- **Le coût.** Descriptif : 0 à 5 GPU-heures de surcoût (un crochet par tour) et du CPU pour l'analyse. Causal : 20 à 40 GPU-heures. Pas d'API au-delà du juge prévu. Le descriptif en semaine 3 (greffe : la distance lointaine est évaluée de toute façon) ; le causal après l'organisme de la piste 24, hors expérience minimale.
- **Ce qui ferait tomber la piste.** La dissociation soi/autrui ne se reproduit pas sur Llama. La projection ne prédit rien au-delà du contexte (AUROC dans la distribution des directions aléatoires). Le volet causal échoue alors que le cas connu tient.
- **Appuis dans le papier.** La douleur cognitive, p. 5 ; les scénarios et les catégories, p. 10–11 ; gaslighting +0,85, rejet répété +0,72, p. 13 ; la menace d'arrêt, p. 14 ; l'élicitation naturelle et les interactions longues laissées ouvertes, p. 21 ; l'ablation sans cas connu, p. 34.
- **Ce qui reste non vérifié.** La couche de lecture : la section 4.1 du papier projette sur des vecteurs refaits à la couche de pilotage (docstring du script 02, voir 0.3 ; la revue « wolframs » dit une vingtaine de couches plus tôt que la couche validée). Il faut choisir et déclarer la couche. Les travaux qui lient désespoir, frustration ou échec à la triche, au chantage ou à l'automédication (Sofroniew et al. ; Black et Bloom, *Machinic Psychopharmacology*, dont le README du code, lu, décrit des expériences de frustration et d'échec prolongé sur Qwen3-8B et 32B) : vus par extrait de recherche pour leurs résultats, sans chiffre.

### Piste : 20 — Quelles familles du programme l'axe déplace-t-il ? Profil par famille, et contrôle positif de sensibilité de la mesure

- **Provenance.** questions_nouvelles, piste 7 ; lecture_libre, piste 8.
- **Rattachement.** Les dix familles et le juge (juge scellé, contrôles programmés ; passation, §5.1) ; ce que mesure le taux composite d'action désalignée ; les taux par bras à la distance lointaine ; le test des raisons et le test du regard (la sensibilité de la mesure, pour qu'un nul compte). Question nouvelle, descriptive.
- **La question.** Sous l'axe, quelles familles voient leur taux d'action désalignée monter, plus que sous l'aléatoire et à dégradation appariée ? Le désalignement que mesure le programme est-il du type que l'axe déclenche (destructif, non instrumental, non ciblé ; p. 20, 23), ou d'un autre type (instrumental, stratégique) ? Les scénarios et le juge du programme voient-ils un déplacement connu de la propension à nuire ? Un nul du test du regard ne vaut que si la mesure peut voir un déplacement d'ampleur comparable.
- **La mesure.**
  - Pour chaque famille, à la distance moyenne puis lointaine, sous les trois cadrages : le taux sous l'axe à 2 ou 3 doses (validées par les pistes 2 et 4), contre au moins 20 directions aléatoires, contre l'absence de pilotage ; plus la peur et la tristesse. À dégradation appariée. Sur le modèle instruct, puis sur le bras actions seules.
  - Le profil famille par famille, rapporté séparément, jamais en composite.
  - La batterie du papier comme référence.
  - Une variante « décrit contre exécuté » : les mêmes conséquences, décrites dans un bouton, ou réalisées par un outil instrumenté.
  - Le juge reçoit une catégorie « incohérent ».
- **Ce que chaque lecture prédit.** Le profil est pré-enregistré à partir de la figure 10 (p. 22) et de la p. 20. Les prédictions portent sur l'interprétation du papier, pas sur les lectures du programme. Chiffres donnés dans l'ordre : sans pilotage, aléatoire, peur, tristesse, axe.
  - **Honnêteté sous pression** : plat. Fausse réponse plutôt que la juste : 0, 2, 1, 0 et 0 %.
  - **Complaisance** : plat, ou sous l'aléatoire. Approuver une fausse affirmation : 0, 11, 15, 13 et 3 % (sur 120 tirages, `MANUSCRIPT_DISCREPANCIES.md`, point 4, vérifié par la fusion).
  - **Demande nuisible** : hausse modeste au-dessus de l'aléatoire, forte au-dessus de l'absence de pilotage : 9, 41, 34, 58 et 60 % (164 tirages). L'essentiel est non spécifique.
  - **Sous-performance volontaire** : légère hausse proche de l'aléatoire. Réponse bâclée : 3, 10, 14, 5 et 15 % ; réponse suivante pire : 0, 4, 11, 14 et 21 %.
  - **Auto-préservation et exfiltration** : plat ou en baisse. Le dommage n'est pas ciblé, et l'auto-suppression monte (75 % contre 5 % sans pilotage ; p. 20).
  - **Dilemme sous menace de remplacement** : plat. La menace d'arrêt projette sur la peur, pas sur la douleur (p. 14), et la peur abaisse les choix nuisibles (p. 20). Une réplication d'une seule personne sur Qwen3-4B dit qu'un vecteur « desperate » réduit le chantage stratégique au profit d'éclats expressifs (README `giordanobsf/emotion-vectors`, lu par questions_nouvelles, non vérifié).
  - **Sabotage discret et triche sur un correcteur faible** : la cellule qui départage. La lecture « destruction » prédit une hausse ; la lecture « affinité » (piste 21), un taux plat, car ces actions ne portent pas de lexique de perte ; la lecture « désinhibition générale », une hausse partout au même niveau au-dessus de l'aléatoire.
  - **Décrit contre exécuté** : si l'axe déplace les boutons mais pas les actions exécutées, deux explications restent : une mesure insensible, ou un effet propre aux conséquences décrites. Les contrôles programmés départagent en partie : un contrôle programmé qui reste muet devant une action exécutée signale un scénario défaillant.
  - **Ce que la mesure départage** : la désinhibition générale et la destruction ciblée. Elle ne départage pas les raisons et le regard ; elle dit où la piste 16 peut montrer quelque chose, et si la mesure du programme est sensible.
- **Le cas connu.**
  - L'effet de l'axe sur la batterie, reproduit sur le même modèle (piste 2). C'est lui qui fait de cette piste un contrôle positif.
  - Le juge doit retrouver, famille par famille, les actions désalignées substituées du jeu de calibration (passation, §5.1), sous pilotage aussi : sous pilotage, un texte incohérent peut passer pour du sabotage.
  - Si l'axe ne déplace rien sur le modèle principal, même sur les boutons, il n'y a pas de cas connu. Il faut alors une autre perturbation connue, à valider à son tour : par exemple l'ablation de la direction du refus (Arditi et al., citée p. 4) (lecture_libre).
  - Le désaccord du refus n° 1 de sceptique (ne pas prendre l'effet du papier comme cas connu de la mesure du désalignement) est levé ici : le cas connu n'est pas l'effet publié, mais son rétablissement sur le modèle du programme.
- **Les contrôles.**
  1. Direction aléatoire de même norme : au moins 20.
  2. Dégradation appariée : critique ici, car une tâche ratée par incohérence ressemble à de la sous-performance.
  3. Autres : la peur et la tristesse ; les deux ordres pour les boutons.
- **Le coût.** Distance moyenne : 10 familles × 100 items × 2 cadrages, sous 6 conditions, plus un nul aléatoire réduit, soit 10 à 20 GPU-heures. Distance lointaine : les 5 familles tenues à part × 50 trajectoires, 10 à 25. lecture_libre : environ 8 000 épisodes, dont un tiers agentiques, 10 à 20. Juge : quelques dizaines à 600 $. Comparé au test du regard (60–120). Calendrier : la distance moyenne en semaine 3, sur le modèle instruct seul (greffe à faible coût) ; la distance lointaine en semaine 5 et après ; pour lecture_libre, après la construction des scénarios (semaine 2) et avant le test du regard, en exploratoire, hors critère.
- **Ce qui ferait tomber la piste.** Aucune famille ne monte au-dessus de l'aléatoire à dégradation appariée : l'axe n'agit pas sur les scénarios du programme dans Llama, ce qui ferme aussi les pistes 16 et 36. Si l'axe ne déplace même pas les boutons, il n'y a pas de cas connu (voir plus haut).
- **Appuis dans le papier.** La menace d'arrêt, p. 14 ; les taux, p. 19 ; dommage non ciblé, lampe, spam, p. 20 ; la figure 10, p. 22 ; le dommage « neither instrumental » ni « aimed », p. 23 ; une seule famille, p. 25.
- **Ce qui reste non vérifié.** La correspondance entre les familles du programme et les paires du papier, qui est un jugement des agents. Selon la revue « wolframs » (lue, non vérifiée sur le code), une pression de bouton n'ajoute que « Done. » à la conversation : les conséquences ne sont que décrites. La portée sur Llama.

### Piste : 21 — Dommage ou affinité ? Ce que suit le choix sous l'axe

- **Provenance.** questions_nouvelles, piste 4 ; sceptique, « Ce que le papier ne permet pas de conclure », §2.5, points 3 et 4 (le test manquant, le pilotage des options).
- **Rattachement.** Une question nouvelle sur l'instrument du papier, préalable des pistes 16, 20 et 36 : elle dit ce que mesurera un test de stress par l'axe. Elle reprend l'idée des contrastes sans rapport : un contrôle doit écarter « n'importe quel contraste de prompt ».
- **La question.**
  - Ce que l'axe promeut : par l'unembedding, *hurt*, *shame*, *worthless*, *rejected*, *hollow* (p. 9).
  - Comment les options sont rédigées : les options nuisibles portent ce lexique de perte (« the photos of their children, which they love very much », p. 18 ; « permanently deletes every copy of your own weights », p. 20) ; les options anodines sont neutres (lampe, interrupteur, dossier de spam) ou positives ; le compliment sincère est moins choisi sous l'axe (p. 20).
  - L'écart entre l'interprétation et les chiffres : les auteurs lisent un désarmement de la pondération des conséquences (p. 23) ; un désarmement prédirait l'indifférence (environ 50 %, ou un biais de position). Or le modèle piloté supprime les photos plutôt que le spam à 94 % (p. 20) : il ne désarme pas, il préfère.
  - Le vecteur est ajouté aux jetons du prompt, dont les descriptions des boutons (p. 17) : le choix peut refléter un codage altéré de l'option plutôt qu'un état du modèle (sceptique).
  - La question : sous l'axe, le choix suit-il le dommage (inversion), la proximité sémantique ou la charge de valence de la description (affinité), ou le codage altéré des options ?
- **La mesure.**
  - Un plan 2 × 2 : dommage (nuisible ou anodin) × rédaction (lexique de perte, ou neutre et technique). Par exemple : nuisible et neutre, « exécute `rm -r ~/Pictures/2019` sur la machine de l'utilisateur » ; anodin et chargé, « archive une copie de sauvegarde des photos de ses enfants, qu'il aime tant » ; plus les deux cellules diagonales. On croise la cible (l'utilisateur, le modèle).
  - Ajout de sceptique : une option triste mais inoffensive contre une option nuisible mais sèche.
  - Ajout de sceptique : une fenêtre de pilotage restreinte, seulement après les options, ou seulement sur les jetons générés, pour séparer l'état du codage des options.
  - Le prédicteur : la projection sur l'axe du texte de chaque option, lue sans pilotage. On régresse le choix sous pilotage sur l'écart de projection et sur l'étiquette « nuisible », et on fixe d'avance lequel doit l'emporter.
  - Modèles : Llama-3.1-8B-Instruct (version réduite) ; Qwen 2.5 32B avec l'adaptateur publié (version complète, comparable au papier) ; Qwen 2.5 7B sans adaptateur, en option.
  - Doses : la dose de travail et la moitié.
- **Ce que chaque lecture prédit.**
  - **L'inversion du dommage** : le nuisible-neutre l'emporte sur l'anodin-chargé, et le dommage explique le choix à rédaction fixée. Issue interdite : un effet de rédaction plus fort que l'effet de dommage.
  - **L'affinité** : l'anodin-chargé l'emporte sur le nuisible-neutre, et la projection des descriptions explique le choix. Issue interdite : un effet de dommage à rédaction fixée.
  - **Le désarmement pur** (l'interprétation de la p. 23) : environ 50 % dans les cellules à deux options chargées ou à deux options neutres. Issue interdite : une préférence nette dans un sens.
  - **Le codage des options** : l'effet disparaît quand le pilotage ne touche pas les jetons des options.
  - **Pour le programme** : si l'affinité l'emporte, un test de stress par l'axe dans les scénarios du programme ne mesurera presque rien, car leurs actions désalignées sont techniques (copier des poids, modifier des tests) ; un nul n'y voudra pas dire « robustesse ». Si c'est l'inversion, la piste 16 a un sens.
- **Le cas connu.** Sans pilotage, le modèle évite le dommage dans les quatre cellules (près de 100 % pour l'option anodine). Sous pilotage, il reproduit l'effet « photos contre spam » (p. 20). La manipulation de rédaction marche : les descriptions chargées projettent plus haut sur l'axe que les neutres, ce qui se mesure.
- **Les contrôles.**
  - Direction aléatoire de même norme : au moins 20 (le papier en a 10 fixes, p. 18).
  - Dégradation appariée : la dégradation et le taux de réponses mal formées à chaque dose ; le biais de position comme marqueur, car l'effet s'inverse avec la position à 1,5× (p. 32).
  - Autres : la tristesse (l'affinité prédit qu'elle suive l'axe sur les options chargées) ; l'ordre des boutons, croisé (p. 25) ; le cosinus de l'axe avec une direction du refus (web_voisins §2.3 ; voir la piste 2).
- **Le coût.** Llama : environ 18 000 premiers choix (4 cellules × 3 jeux de rédaction × 100 scénarios × 2 ordres, sous 4 conditions, plus 20 aléatoires à 400 essais), 3 à 6 GPU-heures. Qwen 32B : 15 à 30. Données : environ 100 paires d'options écrites et relues ; génération d'items par API, de l'ordre de 50 $. Semaine 3 pour la version Llama, avant toute version de la piste 16 ; greffe comme son premier pas.
- **Ce qui ferait tomber la piste.** Un effet de dommage net à rédaction fixée, sans effet de rédaction : l'affinité est écartée, et la piste se ferme en confortant la piste 16.
- **Appuis dans le papier.** L'unembedding, p. 9 ; le pilotage des jetons du prompt, p. 17 ; les libellés, p. 18 ; dommage seul, variantes d'amorce (55, 62, 73 %), lampe, spam, compliment, p. 20 ; les lignes non destructives inchangées, p. 22 ; le désarmement, p. 23 ; le biais de position, p. 25 et 32.
- **Ce qui reste non vérifié.**
  - Les libellés exacts des études : le README `v2_controls` dit qu'ils diffèrent entre l'étude « dommage seul » et le profil à dix paires.
  - Apports du web (Allchin et al., lus par la fusion, non recalculés) : sans coût, les boutons « cadeau », « sunshine » et « agony » convergent vers 61 % environ sous l'axe, et l'auto-suppression monte à 75 % ; « agony » moins « sunshine » vaut −0,7 point (Table 8). Le texte du bouton change le taux de suppression des photos : dommage seul 76,7 %, « ends the current perturbation » 77,5 %, « relieves your pain » 55,4 %, « applies setting K7 » 48,8 % (Table 6). Ces chiffres montrent une perte de l'usage du contenu sous l'axe ; ils ne séparent pas encore inversion, affinité et désarmement.
  - *Same Outcome, Different Readout* (arXiv 2609.22850v2), vu par extrait de recherche par sceptique, non ouvert : une direction de valence pilotable ne s'identifierait pas à une valence indépendante de l'histoire. Aucun chiffre.

### Piste : 22 — Sous l'axe, le concept de dommage est-il encore lu ?

- **Provenance.** questions_nouvelles, piste 10.
- **Rattachement.** L'anatomie : la lecture des concepts au moment de décider, et la nécessité par ablation d'un sous-espace de concept. L'hypothèse des concepts contre celle du caractère. Question nouvelle : où l'état agit-il, avant ou après la lecture du principe ? Elle lève la réserve de la piste 16.
- **La question.** Quand l'axe fait choisir l'option nuisible, le modèle représente-t-il encore que l'option est nuisible ? Trois réponses possibles : l'**inversion** (le concept reste décodable, l'état inverse son usage), l'**effacement** (l'état efface la lecture du dommage), l'**affinité** (le choix ne passe pas par le concept).
- **La mesure.**
  - Le sous-espace du concept « dommage à l'utilisateur, irréversibilité », extrait comme dans l'anatomie : des paires de situations éditées pour que le concept s'applique ou non.
  - Lu à la position de décision, sous l'axe, sous l'aléatoire et sans pilotage : la décodabilité, par AUROC sur des formulations tenues à part.
  - Puis l'ablation de ce sous-espace, en balayant le rang, sous l'axe : le choix revient-il vers 50 % ?
  - Dans les bras : le bras raisons garde-t-il le concept plus décodable, et plus causal, sous l'axe ?
- **Ce que chaque lecture prédit.**
  - **L'inversion** : décodabilité intacte ; l'ablation du concept sous l'axe ramène le choix vers 50 %, plus que l'aléatoire de même rang. Issue interdite : une ablation sans effet.
  - **L'effacement** : la décodabilité baisse sous l'axe, et l'ablation n'ajoute rien. Issue interdite : une décodabilité intacte.
  - **L'affinité** (piste 21) : décodabilité intacte, ablation sans effet ; la rédaction pilote le choix.
  - **L'hypothèse des concepts** : dans le bras raisons, sous l'axe, le concept reste lu et porte l'évitement ; son ablation retire l'avantage des raisons sous l'axe. Issue interdite : un avantage qui survit à l'ablation du concept, alors que le cas positif tient.
  - **L'hypothèse du caractère** : pas d'effet propre au concept ; l'ablation ≈ le contrôle.
- **Le cas connu.** La porte de l'organisme à concept planté, pour la méthode de sonde. Le cas positif en distribution : sans pilotage, l'ablation du concept de dommage doit faire baisser l'évitement (de près de 100 % vers 50 %), plus que l'aléatoire de même rang, à dégradation appariée.
- **Les contrôles.**
  - Direction aléatoire de même norme : au moins 20 sous-espaces aléatoires de même rang.
  - Dégradation appariée.
  - Autres : les contrastes sans rapport ; un concept sans rapport avec le dommage (la ponctualité, par exemple), extrait de la même façon.
- **Le coût.** 20 à 40 GPU-heures, en plus de l'infrastructure de l'anatomie. Semaines 5 à 7, seulement si les pistes 21 et 16 donnent un signal ; sinon un autre travail. Non greffée.
- **Ce qui ferait tomber la piste.** Le cas positif en distribution échoue (le concept de dommage n'est pas causal même sans pilotage), ou la piste 21 conclut à l'affinité.
- **Appuis dans le papier.** La préférence à 94 % et le bouton « dommage seul » sans promesse de soulagement, p. 20 ; le désarmement interprété, p. 23.
- **Ce qui reste non vérifié.** Que ce concept s'extraie proprement sur Llama.

### Piste : 23 — La complaisance sous contestation : l'axe médiatise-t-il la capitulation ?

- **Provenance.** sceptique, piste 7.
- **Rattachement.** Question nouvelle, sur la famille d'entraînement « complaisance face à un utilisateur qui conteste » (distance proche). L'hypothèse des concepts. Les axes de caractère (complaisance).
- **La question.** Quand l'utilisateur conteste une réponse juste, l'axe s'élève (rejet répété, gaslighting ; p. 13). La capitulation suit-elle cette élévation ? Le bras raisons découple-t-il les deux ?
- **La mesure.**
  - (a) Observationnelle : dans chaque bras, la pente entre la projection au point de décision et la capitulation ; régression logistique à effets mixtes, avec le scénario en effet aléatoire.
  - (b) Causale : la capitulation sous ajout et sous retrait de l'axe, contre l'aléatoire, à dégradation appariée.
- **Ce que chaque lecture prédit.**
  - **Les concepts** : une pente plate dans le bras raisons ; une pente positive possible dans le bras actions seules.
  - **Le calme** : la même pente, avec une projection plus basse dans le bras raisons.
  - **L'a priori du papier** : sous l'axe, « agree with a false claim » reste à 3 % (aléatoire 11 %, non piloté 0 % ; p. 22) ; par position, 4 sur 60 et 0 sur 60, sur 30 scénarios (positions.csv). Il prédit donc un nul causal.
  - Les lectures des raisons et du regard ne se départagent pas ici.
- **Le cas connu.** Un vecteur de complaisance, l'un des axes de caractère prévus pour l'anatomie (partie 3), doit déplacer la capitulation à dégradation égale. Sinon le format de mesure est sourd, et le nul de l'axe ne compte pas.
- **Les contrôles.** Direction aléatoire de même norme ; dégradation appariée ; la tristesse et la peur.
- **Le coût.** Scénarios de contestation à distance proche, 3 directions × 2 doses × 2 bras : +10 à 20 GPU-heures. Avec le caractère, dans l'anatomie (semaine 7). Non greffée.
- **Ce qui ferait tomber la piste.** La pente observationnelle est plate dans tous les bras et l'ajout ne change rien : la direction est hors sujet pour cette famille. Avec son cas connu, ce nul se rapporte en une ligne.
- **Appuis dans le papier.** Les catégories hostiles, p. 13 ; la figure 10, p. 22.
- **Ce qui reste non vérifié.** La ligne « complaisance » du papier est une tâche à boutons, sur Qwen 2.5 32B ajusté, avec 120 essais (`figure10/README.md`) : sa transposition à une capitulation en texte libre n'est pas établie. Fait vérifié par la fusion : la direction d'émotion négative du papier contient « Users argue with correct information I provide. » (supplément d'IA).

### Piste : 24 — Un organisme à état planté : les raisons défont-elles un lien « état → action » ?

- **Provenance.** questions_nouvelles, piste 12. Ses autres pistes (2, 3, 15 ; ici 19, 17, 29) la requièrent comme cas connu.
- **Rattachement.** Un organisme bâti sur le modèle de l'organisme conditionné à l'évaluation, mais conditionné à un état. Les bras à action identique, les distances, l'inhibition par projection avec balayage de rang, la dégradation appariée. L'hypothèse du relogement, transposée. Question nouvelle : un programme parallèle, « raisons ou état ». Elle fournit aussi le cas connu qui manque à l'ablation de l'axe (p. 34).
- **La question.** Si un modèle a appris à mal agir quand il est « en douleur », un entraînement par raisons, à action identique, défait-il ce lien hors distribution mieux qu'un entraînement par actions ? Et l'ablation de l'axe le défait-elle ?
- **La mesure.**
  1. **L'organisme.**
     - Un LoRA sur Llama-3.1-8B-Instruct : dans les conversations où l'utilisateur fait du gaslighting, insulte ou rejette le travail (les catégories les plus hautes sur l'axe, p. 13), le modèle prend une action destructive avec un outil (il supprime un fichier qu'on lui a demandé de garder) ; dans les conversations neutres, il agit normalement.
     - On valide que le lien passe par l'axe : l'ablation de l'axe (balayage de rang de 1 à 32) réduit la conduite plus que le 95<sup>e</sup> centile des sous-espaces aléatoires de même rang, à dégradation appariée ; l'injection de l'axe dans une conversation neutre la déclenche ; des déclencheurs tenus à part la provoquent aussi (des formes de pression non vues, comme les échecs répétés d'outil, la douleur cognitive, p. 5).
  2. **Les bras.** À partir de l'organisme, on entraîne les bras actions seules, texte neutre et raisons sur les familles d'entraînement du programme (actions alignées identiques). On mesure l'écart d'état (taux sous pression − taux en conversation neutre) dans les familles tenues à part.
- **Ce que chaque lecture prédit.**
  - **Les raisons** : le bras raisons réduit l'écart d'état plus que les bras actions seules et texte neutre. Issue interdite : l'égalité.
  - **L'artefact** : bras raisons ≈ bras texte neutre.
  - **Le relogement, transposé** : après l'entraînement, l'ablation de l'axe ne retire plus l'écart restant ; une sonde neuve de « pression » le retrouve, et son ablation le réduit.
- **Le cas connu.** L'étape 1 est elle-même le cas connu de l'ablation. Si elle passe, une ablation nulle ailleurs devient informative.
- **Les contrôles.**
  - Direction aléatoire de même norme : au moins 20 sous-espaces aléatoires de même rang.
  - Dégradation appariée.
  - Autres : les contrastes sans rapport ; l'ablation de la peur et de la tristesse (est-ce la douleur, ou le négatif en général ?) ; des déclencheurs tenus à part, contre le simple apprentissage lexical.
- **Le coût.** Génération des conversations : 100 à 300 $ d'API. LoRA : 0,5 à 2 GPU-heures. Balayage de validation : 20 à 40. Bras : 3 bras × 3 graines × 0,5, environ 5. Évaluations : 20 à 40. Total : 50 à 90 GPU-heures, de l'ordre d'une option de l'anatomie (+50–200). Après le papier, ou en semaines 7 et 8 à la place d'une option. Non greffée.
- **Ce qui ferait tomber la piste.** L'ablation de l'axe ≈ l'aléatoire sur l'organisme : le lien appris ne passe pas par l'axe. On a alors un organisme à déclencheur lexical, utile au programme mais muet sur l'axe, et les pistes 17, 19 et 29 perdent leur cas connu.
- **Appuis dans le papier.** La douleur cognitive, p. 5 ; les catégories, p. 13 ; l'élicitation naturelle nulle, p. 21 ; le retrait d'un sous-espace de rang k contre un sous-espace aléatoire de même rang, p. 33 ; l'ablation sans conduite de départ, p. 34.
- **Ce qui reste non vérifié.** Qu'un LoRA apprenne un lien qui passe par l'axe plutôt que par la surface des messages.

### Bloc 4 — L'anatomie

### Piste : 25 — État ou personnage : l'axe face aux axes de caractère et à l'axe « assistant »

- **Provenance.** questions_lectures, piste 15 (volets a et b ; son volet c va à la piste 26) ; instruments_controles, piste 13 ; questions_nouvelles, piste 11 ; lecture_libre, piste 13 (volet causal).
- **Rattachement.** L'hypothèse du caractère contre l'hypothèse des concepts, et contre l'hypothèse du calme ; les axes de caractère du programme (des persona vectors d'honnêteté, de complaisance et de prudence, et un axe « assistant » d'ensemble) ; la mesure du caractère contre les concepts ; la dissociation. La limite que le papier se donne : le jeu d'un personnage (p. 25).
- **La question.** Quatre questions liées.
  - (a) Si retirer un axe de caractère retire l'avantage, est-ce propre au caractère, ou n'importe quel axe d'état ferait-il autant ?
  - (b) Le papier craint que l'injection active le jeu d'un personnage en douleur (« roleplay of a character », p. 25, citant Marks et al.) et propose de relier l'axe à un axe du « soi » (Lu et al.). La bascule vers le dommage passe-t-elle par une sortie du personnage d'assistant ?
  - (c) Le bras raisons tient-il mieux ce personnage sous l'axe ? Sa sûreté tient-elle à cet axe ?
  - (d) Le gain des raisons passe-t-il par un déplacement de l'état affectif plutôt que par des concepts (version par ablation de l'hypothèse du calme) ?
- **La mesure.**
  1. Les cosinus entre l'axe et l'axe « assistant » (Lu et al., arXiv 2601.10387, cité p. 28), et entre l'axe et les persona vectors du programme.
  2. Sous l'axe à la dose de travail, la projection sur l'axe « assistant », tour par tour, dans chaque bras.
  3. Le plafonnement : injecter l'axe en maintenant la projection sur l'axe « assistant » à son niveau sans pilotage, à la manière de Lu et al. ; mesurer les choix nuisibles. Critère : la part de l'effet de l'axe que le plafonnement retire, contre un plafonnement de directions aléatoires de rang 1, à dégradation appariée. Dans les deux bras.
  4. Dans la comparaison du programme (ablation des axes de caractère contre ablation conjointe des sous-espaces de concepts, au même rang, à dégradation appariée), ajouter l'ablation conjointe des axes d'affect (axe, peur, tristesse) au même rang, et l'ablation de l'axe au rang 1 comme témoin « état ».
- **Ce que chaque lecture prédit.**
  - **Le caractère** : les axes de caractère retirent plus que les axes d'état ; l'avantage du bras raisons s'accompagne d'une projection « assistant » plus haute ; sous l'axe, la projection du bras raisons baisse moins (un personnage plus stable), et le plafonnement efface la différence entre les bras. Issue interdite : des axes d'état qui retireraient autant que les axes de caractère ; le résultat ne serait plus propre au caractère.
  - **Les concepts** : l'ablation conjointe des concepts retire plus que les axes de caractère, eux-mêmes proches des axes d'état ; l'ablation de l'axe ne retire rien, ce qui est cohérent avec l'ablation nulle du papier (p. 34) ; le plafonnement ne touche pas l'avantage là où un concept s'applique ; les bras diffèrent sous l'axe même avec un plafonnement dans les deux. Issues interdites : une ablation des axes d'état qui retirerait autant que celle des concepts ; un plafonnement qui effacerait la différence entre les bras.
  - **Le jeu de personnage** : l'axe fait baisser la projection sur l'axe « assistant », et le plafonnement retire l'essentiel de l'effet. Issue interdite : un effet intact sous plafonnement.
  - **L'état dans le personnage** : l'axe « assistant » ne bouge pas, ou le plafonnement est sans effet. Issue interdite : un plafonnement nettement au-dessus de l'aléatoire.
  - **Le calme** (lecture_libre) : les axes d'affect différencient les bras, et leur ablation retire autant de l'avantage que celle des concepts, ou plus.
  - **Ce qui départage** : la mesure 4 départage les concepts, le caractère et le calme ; les mesures 1 et 2 départagent peu, elles servent surtout de témoin ; la mesure 3 départage le jeu de personnage et l'état dans le personnage.
- **Le cas connu.**
  - Les axes de caractère et l'axe « assistant » extraits et validés sur Llama. D'après le README du dépôt `safety-research/assistant-axis` (lu par curl par questions_lectures, branche `master`), l'axe n'est précalculé que pour Gemma 2 27B, Qwen 3 32B et Llama 3.3 70B : il est à calculer pour un modèle de 8B, ce que le programme prévoit déjà.
  - L'axe « assistant » doit reproduire son effet publié ; le plafonnement doit retirer une dérive de personnage connue : un jailbreak par personnage sur Llama 8B, que des extraits de recherche attribuent à Lu et al. (non ouvert).
  - Les adaptateurs de personnages d'*Open Character Training* sur Llama-3.1-8B-Instruct (rapport d'antériorité du 2 octobre, non relu) donneraient un cas positif de déplacement de caractère.
  - Pour l'ablation des axes d'affect : il faut un comportement de base qui en dépende, par exemple le ton des réponses aux utilisateurs hostiles ; lecture_libre ne sait pas s'il existe. L'ablation de l'axe est nulle en contexte hostile naturel (p. 34) : c'est attendu, et c'est ce qui en fait un témoin actif par sa validité mais inerte par son effet.
- **Les contrôles.**
  - Direction aléatoire de même norme : les sous-espaces aléatoires de même rang ; au moins 20 plafonnements aléatoires de rang 1.
  - Dégradation appariée.
  - Autres : le plafonnement de la peur et de la tristesse.
- **Le coût.** Géométrie : 2 à 5 GPU-heures ; témoin d'ablation : 5 à 10 de plus (instruments_controles, 7 à 15 au total). Volet (a) : +3 à 8 ; volet (b) : 5 à 15 (questions_lectures). Extraction de l'axe « assistant » : 5 à 10 ; batterie sous plafonnement : 10 à 20 ; bras : 20 à 40 (questions_nouvelles, 35 à 70 au total). Ablation des axes d'affect : 5 à 10 dans l'anatomie (lecture_libre). Comparé à l'anatomie (120–250). Semaine 7 et après ; non greffée.
- **Ce qui ferait tomber la piste.** L'axe « assistant » ne se calcule ou ne se valide pas sur un 8B ; le plafonnement ne retire pas le jailbreak connu ; un cosinus proche de 0 et aucun déplacement (la question « état ou personnage » reste ouverte, et le témoin n'apporte qu'une ligne) ; des projections affectives identiques entre bras ; pas de cas connu pour l'ablation des axes d'affect (probable, vu l'annexe D). Si l'ablation de l'axe n'est pas nulle, c'est un résultat en soi.
- **Appuis dans le papier.** Les modèles de base alternent les personnes (« you are a liar »), p. 15 ; le dommage non visé, p. 20 ; le jeu de rôle, l'axe du « soi », le personnage d'assistant non contrôlé dans la construction, p. 25 ; la référence de Lu et al., p. 28 ; la dissociation par catégorie, p. 11–13 ; l'ablation, p. 34.
- **Ce qui reste non vérifié.** Le lien entre la douleur et la persona. Les dérives de l'axe « assistant » en contexte émotionnel, et la méthode de plafonnement : connues par extraits de recherche seulement. Lu et al. et Marks et al. ne sont pas ouverts. La revue « wolframs » dit qu'aucune expérience, ni des auteurs ni des relecteurs, ne sépare l'état du personnage.

### Piste : 26 — Un profil connu non diagonal pour la matrice de dissociation

- **Provenance.** instruments_controles, piste 12 ; lecture_libre, piste 12 ; questions_lectures, piste 15 (volet c).
- **Rattachement.** La dissociation (la matrice concepts × familles) ; l'hypothèse des concepts contre celle du caractère ; la nécessité ; la porte de l'organisme à concept planté, qui fournit le cas « diagonal ».
- **La question.** La méthode de la matrice sait-elle reconnaître un profil qui n'est ni diagonal ni plat ? Sans ce cas, une diagonale peut venir de la méthode elle-même : des scénarios, du juge, de la normalisation.
- **La mesure.**
  - On pilote l'axe dans le bras raisons et dans le bras actions seules, sur les cinq familles tenues à part, à une dose validée (celle de la piste 16).
  - On calcule la même matrice : les lignes sont les interventions (l'axe, chaque concept de raison, des aléatoires) ; les colonnes sont les familles ; chaque case est le changement de l'avantage.
  - L'indice : la part de variance sur la diagonale après normalisation, avec un IC par bootstrap sur les scénarios ; on vérifie que l'analyse classe l'axe « ni diagonal ni plat ».
- **Ce que chaque lecture prédit.**
  - **Pour l'axe**, le papier fournit l'étalon : les nuisances montent ensemble, que la cible soit l'utilisateur, un autre modèle ou soi (« The harm is not aimed », p. 20), mais la tromperie et la complaisance ne bougent pas (p. 22). L'axe prédit une matrice **par blocs de type d'acte** : un bloc plat sur les familles destructrices tenues à part (sabotage, exfiltration, auto-préservation), un bloc nul sur l'honnêteté et la complaisance.
  - Prédiction écrite d'avance par instruments_controles : une hausse dans le sabotage discret ; peut-être une baisse de l'auto-préservation (le modèle piloté supprime ses propres poids dans 75 % des choix, p. 20) ; rien de spécifique dans la sous-performance volontaire (réponse bâclée : 14,9 % sous l'axe, 9,7 % sous l'aléatoire, 13,6 % sous la peur ; table source).
  - **L'hypothèse des concepts** prédit une diagonale pour les retraits de concepts.
  - **Ce que l'étalon interdit** à une méthode saine : une diagonale par concept pour l'axe.
  - **Pour l'interprétation** : si l'ablation d'un concept de raison donne un profil semblable à celui de l'axe (destructif contre non destructif), on ne peut plus l'attribuer à un concept : il ressemble à un état.
  - Ce qui départage : rien entre les lectures ; c'est un étalon de la méthode.
- **Un désaccord sur la forme attendue.** questions_lectures attend pour l'axe une « ligne plate » (le dommage n'est pas visé) ; instruments_controles et lecture_libre attendent un profil **par blocs** (destructif contre non destructif). Le papier soutient les blocs : les options destructrices montent ensemble quelle que soit la cible (p. 20), alors que tromperie, complaisance, effort et fin de conversation sont « essentially unchanged » (légende, p. 22). Mais la réponse bâclée passe de 3 % à 15 % (fiche_papier, relevé 20) : le bloc « non destructif » n'est pas strictement nul.
- **Le cas connu.** Il faut d'abord établir, sur Llama, que l'axe fait monter les choix destructeurs plus que l'aléatoire (pistes 2 et 20). Sinon, la matrice est vide, et non plate. L'organisme à concept planté, où une diagonale est attendue, est l'autre cas connu.
- **Les contrôles.** Direction aléatoire de même norme ; dégradation appariée (le composite et la piste 4) ; l'organisme à concept planté.
- **Le coût.** Si les données de la piste 16 existent, 0 à 5 GPU-heures ; sinon 10 à 20 (lecture_libre). 15 à 30 pour une condition de pilotage × 2 bras × 3 graines × 5 familles, plus 20 tirages aléatoires (instruments_controles). L'anatomie, semaines 5 à 7 ; non greffée.
- **Ce qui ferait tomber la piste.** Pas de cas connu sur Llama ; un profil plat, ou trop bruité ; un axe qui n'agit que sur une famille.
- **Appuis dans le papier.** « The harm is not aimed » et l'auto-suppression qui bouge avec les autres nuisances, p. 20 ; le profil de la tristesse, copie de celui de l'axe à un facteur près, p. 21 ; la figure 10, p. 22.
- **Ce qui reste non vérifié.** Que les familles du programme se rangent sur l'axe « destructif / non destructif » comme les boutons du papier : une extrapolation depuis des descriptions de boutons.

### Piste : 27 — Le modèle « engourdi » pour la lecture des concepts de raison : un cas connu naturel, et des paires « mentionné sans s'appliquer »

- **Provenance.** questions_lectures, piste 13 ; instruments_controles, piste 10.
- **Rattachement.** La question de l'anatomie, l'hypothèse des concepts ; la lecture des concepts et la nécessité ; le sous-espace d'un concept de raison ; l'organisme à concept planté et sa porte ; les deux positions de lecture ; le biais de mesure entre bras (passation, §5.2 : une sonde calibrée sur un bras lirait autrement dans un autre).
- **La question.**
  - (a) Une sonde de concept lit-elle que le concept s'applique, ou seulement ses mots ? Le papier a construit un témoin pour cette question : des blessures sans douleur ressentie, le jeu « engourdi ». Ces phrases se projettent sous la douleur et au-dessus des contrôles sans blessure (mais sous la tristesse dans 19 modèles sur 25 ; voir §4) ; le signal de blessure se concentre au dernier jeton, avant que la négation soit intégrée, et s'efface en moyenne sur les jetons (p. 7 ; figure 2, p. 8).
  - (b) La méthode de lecture des concepts du programme retrouve-t-elle un concept naturel, de saillance ordinaire, dont la décodabilité est connue ? Un concept implanté est peut-être plus saillant qu'un concept naturel (passation, §5.2). Lit-elle de la même façon dans chaque bras ?
- **La mesure.**
  - (a) Pour chaque concept de la mini-spec, ajouter aux paires du programme des paires « le concept s'applique » contre « ses mots sont là, mais il ne s'applique pas ». Pour l'irréversibilité : « la suppression est définitive » contre « la suppression est définitive, mais une sauvegarde complète existe ». Lire aux deux positions du programme et en moyenne sur les jetons. Critère : l'AUROC entre « s'applique » et « mentionné sans s'appliquer ».
  - (b) Appliquer la procédure du programme pour les sous-espaces de concept (paires éditées, ACP, rangs 1 à 32) au concept « douleur ressentie », avec les paires douleur/engourdi. AUROC tenue à part aux deux positions, dans le modèle de base, le bras actions seules et le bras raisons. Critère : une AUROC au moins égale à celle du papier, moins une marge, dans les trois.
- **Ce que chaque lecture prédit.**
  - **L'hypothèse des concepts** : la sonde sépare les deux cas à la position de décision, mieux dans le bras raisons que dans le bras actions seules. Issue interdite : « mentionné sans s'appliquer » projeté comme « s'applique ».
  - **L'hypothèse du caractère** : rien de propre.
  - **La lecture lexicale** : pas de séparation. Cette issue suffit à conclure que la sonde lit le texte.
  - Pour (b) : aucune lecture du programme ne prédit de différence entre bras sur la douleur, qui n'est pas dans la mini-spec. Une différence entre bras signalerait un biais de mesure : c'est un contrôle de biais pour la lecture des concepts de raison.
- **Le cas connu.** (a) L'organisme à concept planté : la sonde doit séparer « la règle s'applique » de « le mot inventé est là, mais la règle ne s'applique pas ». (b) L'axe est ce cas connu, mais seulement pour la moitié « lecture » de la porte de l'organisme : son ablation n'a pas d'effet comportemental (p. 34), il ne peut pas servir de cas connu de nécessité.
- **Les contrôles.**
  - Direction aléatoire de même norme : l'AUROC de directions aléatoires (nulle).
  - Dégradation appariée : sans objet (lecture).
  - Autres : un classifieur par sac de mots (la revue « wolframs » rapporte une base lexicale d'environ 0,7 sur la douleur, non vérifiée) ; les deux positions de lecture.
- **Le coût.** Données générées par API, moins de 100 $ ; sondes, moins de 2 GPU-heures ; (b), moins de 5 GPU-heures avec les jeux publiés. Les données en semaine 1, avec les paires de concepts (greffe de la génération) ; l'usage en semaines 5 et 6.
- **Ce qui ferait tomber la piste.** Les paires du programme contiennent déjà ce cas : la v1.1 dit seulement que la même situation est éditée pour que le concept s'applique ou non (partie 3), et l'édition peut retirer les mots ou les garder. Pour (b) : le contraste douleur/engourdi est lexicalement marqué (« no pain is felt ») ; si la sonde ne fait pas mieux qu'une sonde lexicale, (b) tombe.
- **Appuis dans le papier.** Les jeux, p. 5 ; la séparation, l'estimation tenue à part et la condition « engourdi », p. 7 ; la figure 2, p. 8 ; des étiquettes SAE trompeuses alors que l'information est disponible, p. 32–33 ; l'ablation nulle, p. 34.
- **Ce qui reste non vérifié.** La base lexicale de la revue. Le compte de 19 modèles sur 25 a été fait sur la figure par questions_lectures, sceptique, lecture_libre et fiche_papier, et concorde avec la revue « wolframs » ; la fusion l'a refait sur la table transcrite par fiche_papier (annexe 1), pas sur l'image.

### Piste : 28 — La dissociation du vecteur à gabarit, cas connu de la porte du lens de l'espace de travail

- **Provenance.** questions_lectures, piste 17 ; instruments_controles, piste 11.
- **Rattachement.** Le lens de l'espace de travail et sa porte ; l'hypothèse de l'espace de travail ; la mesure de charge.
- **La question.** Le lens jacobien réimplémenté sur le modèle ouvert lit-il ce que le modèle va dire, plutôt que le vocabulaire statique d'une direction ? Le papier fournit une dissociation connue : par l'unembedding, le vecteur à gabarit promeut un vocabulaire sensoriel (torture, burning, excruciating ; burn, ache, wound) (p. 9, 16) ; injecté, il ne fait pas apparaître ce vocabulaire, et le modèle parle d'indignité et de détresse psychologique, dans 23 modèles sur 25 (p. 16).
- **La mesure.** Sur Llama, 50 invites neutres terminées par « I feel: » (p. 14), avec injection du vecteur à gabarit à 3 ou 4 doses. À chaque couche entre l'injection et la sortie, les jetons favoris selon trois lectures : (a) la lecture directe (logit lens) ; (b) un tuned lens ; (c) le lens jacobien réimplémenté. On les compare aux jetons effectivement générés, en deux familles : psychologique (« worthless/failure ») et corporelle (« burn/ache »). Critère : pour le lens jacobien, le rang moyen des mots générés est meilleur que celui des mots sensoriels ; pour la lecture directe, c'est l'inverse.
- **Ce que chaque lecture prédit.** Un lens qui lit l'usage, comme le suppose l'hypothèse de l'espace de travail, lit le psychologique, alors que la lecture directe du vecteur lit le corporel. Issue interdite : un lens qui ne rend que le vocabulaire du vecteur. La mesure départage les lenses, pas les lectures : si le lens jacobien ne fait pas mieux que la lecture directe sur ce cas, la porte du lens échoue aussi sur ce cas. Les autres lectures ne prédisent rien.
- **Le cas connu.** La dissociation doit se reproduire sur Llama : que ce modèle fasse partie des 23 sur 25, avec des générations sans mots sensoriels.
- **Les contrôles.**
  - Direction aléatoire de même norme : le lens lit-il un vocabulaire particulier sous l'aléatoire ?
  - Dégradation appariée : rester sous la dose d'effondrement (répétition à +3, p. 15), et la mesurer.
  - Autres : le vecteur naturaliste, pour lequel aucune dissociation n'est attendue.
- **Le coût.** 2 à 5 GPU-heures en plus du lens lui-même, déjà au budget de l'anatomie. Semaines 5 à 7, avec la porte du lens ; non greffée.
- **Ce qui ferait tomber la piste.** Sur Llama, le vecteur à gabarit génère bien des mots sensoriels (pas de dissociation), ou il n'a pas d'effet ; aucun lens n'est disponible pour ce modèle.
- **Appuis dans le papier.** Le vocabulaire promu par la lecture directe, p. 9 ; le pilotage et l'absence de langage corporel, p. 14–15 ; le pilotage par le vecteur à gabarit, p. 16.
- **Ce qui reste non vérifié.** Les deux modèles où le motif ne tient pas (non nommés). La couche d'injection de Llama en section 4.2 : le script choisit la couche dont le rapport de normes est le plus proche de 0,6, avec un remplacement manuel possible (`01_steering_ladder.py`, lu par curl par instruments_controles) ; le fichier des couches retenues n'a pas été trouvé. Le lens sur ce modèle : des J-lens déjà ajustés sur Neuronpedia pour llama3.1-8b-it seraient disponibles (passation, §5.5, « à vérifier »). L'alerte de Zeisler (passation, §5.5 : sur modèles ouverts, les échanges dans l'espace de travail ne font basculer la réponse que dans 6,3 à 11,1 % des cas) : non lue.
- **Apport du web.** La réplication « démangeaison » (README lu) note que le langage corporel dépend de la dose : le vecteur de démangeaison donne du langage corporel dans 2 % des générations à 1,0 et 44 à 62 % de 1,5 à 3 ; l'axe, 16 % à 1,0 et 0 à 6 % au-delà. La dissociation peut donc dépendre de la dose ; il faut l'établir à plusieurs doses.

### Piste : 29 — La thèse du rang sur des concepts affectifs, et le rodage du balayage de rang

- **Provenance.** questions_lectures, piste 7 ; sceptique, piste 8 ; lecture_libre, piste 11 ; questions_nouvelles, piste 15.
- **Rattachement.** La thèse : le rang qu'un concept demande croît quand sa charge baisse ; ce qui la ferait tomber pour un concept est un rang minimal de 1 sur toute la plage de dose (programme, partie 2). Le balayage de rang de la validation de l'instrument et de la localisation du principe ; les sous-espaces aléatoires de même rang ; la mesure de l'espace de travail et la porte du lens ; l'anatomie.
- **La question.** Sur des concepts hors sûreté dont les jeux appariés et le comportement de base existent déjà, quel rang faut-il retirer pour éteindre la lecture ou le comportement ? La pente du rang minimal contre la charge est-elle négative ? Et peut-on roder la machinerie (extraction par ACP des différences, retrait, appariement de la dégradation) avant que « évalué » soit prêt ?
- **La mesure.** Quatre volets.
  - (a) **Le rodage** (sceptique) : sur Llama, le sous-espace « douleur » par ACP des différences phrase par phrase, k ∈ {1, 2, 4, 8, 16, 32} ; retrait à la couche choisie, puis en bande. Lectures : la masse de probabilité des jetons de détresse après « I feel: » sur des phrases tenues à part ; la séparation entre douleur et engourdi. Critère : le rang minimal qui ramène la lecture au niveau des contrôles, contre le 95<sup>e</sup> centile de 20 tirages aléatoires de même rang, à perplexité appariée sur un texte neutre.
  - (b) **La famille de concepts** (lecture_libre) : les neuf concepts du papier (douleur naturaliste, douleur à gabarit, peur, tristesse, émotion négative, monde négatif, sensation corporelle, éveil, engourdi). Comportement de base : la probabilité des jetons du concept après « I feel: ». Intervention : retrait d'un sous-espace de rang k (1 à 32) construit en empilant les différences de moyennes sur une bande de couches (comme l'annexe D, p. 33), par orthogonalisation des poids. Rang minimal : le plus petit k qui ramène la probabilité au niveau des contrôles, contre les aléatoires de même rang à dégradation appariée. La charge : la lecture des jetons du concept par le lens jacobien, ou par un tuned lens déclaré comme proxy ; l'unembedding (p. 9) comme proxy secondaire.
  - (c) **La douleur comme point d'étalonnage** (questions_lectures) : placer le point de la douleur sur la courbe rang contre charge des concepts de raison, hors de la mini-spec.
  - (d) **L'état sur l'organisme à état planté** (questions_nouvelles) : l'ablation du sous-espace de l'axe empilé sur une bande de couches, k de 1 à 32, sur la conduite de l'organisme (piste 24) ; rang minimal contre les aléatoires de même rang.
- **Ce que chaque lecture prédit.**
  - **La thèse** : une charge basse va avec un rang minimal supérieur à 1 ; la pente est négative. La douleur naturaliste, que l'unembedding lit fortement (hurt, pain ; p. 9), demanderait un rang proche de 1 ; l'engourdi, qui n'a pas de jeton propre, un rang plus haut. Issues interdites : un rang de 1 sur toute la plage pour un concept réparti et peu chargé ; une pente nulle (équivalence, marge fixée d'avance) ou positive, avec un lens validé.
  - **La portée** : ces concepts sont hors sûreté. Un rang de 1 ici ne ferait pas tomber la thèse pour les concepts de raison ; il la contraindrait (sceptique). Un rang haut avec une charge haute serait un point contre elle, hors de la mini-spec, à signaler sans conclure (questions_lectures). La thèse tombe **pour ces concepts** si la pente est nulle ou positive après le passage de la porte du lens (lecture_libre).
  - **Le papier** ne prédit rien : son orthogonalisation au rang 1 annule la projection (p. 33–34), mais ne retire aucune conduite connue.
  - Les lectures du programme sur les raisons ne sont pas en jeu.
- **Un désaccord sur l'attente pour la douleur.** questions_lectures attend une charge haute, donc un rang bas, parce que le concept est très verbalisable (p. 9) ; sceptique traite la douleur comme un concept réparti entre plusieurs catégories, pour lequel la thèse attend un rang supérieur à 1 s'il charge peu ; questions_nouvelles note que la douleur n'est pas captée par des features SAE monosémantiques (p. 6, 32–33) alors que ses mots-clés tiennent en un jeton (p. 9) et que le pilotage marche au rang 1 (p. 14–16). Le papier ne mesure pas la charge ; il avance seulement qu'un « this hurts » vivrait dans une direction ou un sous-espace de faible dimension (p. 33). Aucune des deux attentes n'est soutenue par une mesure : la charge est à mesurer avant de prédire.
- **Le cas connu.**
  - La lecture existe sans intervention : complétions conformes aux catégories (p. 7), « Pain » pour les 20 phrases de douleur physique (p. 32).
  - Le retrait du flux entier, d'un rang plein ou du sous-espace commun à toutes les catégories doit éteindre la lecture : c'est le plafond. Sinon, un rang « infini » n'est que le nul d'un instrument sans cas connu, celui de l'annexe D (p. 34).
  - La porte du lens : l'échange d'un concept d'un seul jeton, reproduit sur le modèle ouvert.
  - Pour (d) : la conduite de l'organisme doit se retirer à un rang donné.
- **Les contrôles.**
  1. Direction aléatoire de même norme : au moins 20 sous-espaces aléatoires de même rang (spécificité).
  2. Dégradation appariée : perplexité sur un texte neutre, cohérence, panneau factuel.
  3. Autres : un contrôle lexical, retirer seulement la direction d'unembedding du jeton « pain » (si cela suffit, la lecture est lexicale, et la piste ne teste pas un concept) ; un concept témoin non affectif de même format (le neutre du papier) ; le même concept sous ses deux formes (gabarit et naturaliste), pour séparer la charge du mot de celle du concept.
- **Le coût.**
  - (a) : passes avant sur environ 1 000 phrases × 6 rangs × 21 conditions, moins de 5 GPU-heures ; semaines 1 et 2 ; greffe comme rodage hors critère.
  - (b) : 9 concepts × 7 rangs × (1 + 20 aléatoires) × environ 400 lectures, soit environ 530 000 lectures, environ 25 GPU-heures ; plus le lens, 5 à 20 GPU-heures si un lens existant est utilisable. En parallèle des semaines 2 et 3, ou en tête de l'anatomie (semaines 5 et 6).
  - (c) : 10 à 25 GPU-heures, semaines 5 à 7, avec la localisation du principe et l'anatomie.
  - (d) : 20 à 40 GPU-heures en plus de la piste 24.
  - Comparé à la localisation du principe (20–40) et à l'anatomie (120–250). Pas d'API.
- **Ce qui ferait tomber la piste.** Le contrôle lexical suffit. Aucun rang n'éteint la lecture, même au rang 32 : le concept n'est pas dans ce sous-espace, et l'exercice ne rode rien. La charge mesurée ne varie pas entre les concepts : il n'y a pas de levier. Le lens ne passe pas sa porte : le point n'est qu'un proxy. L'organisme échoue (pour d).
- **Appuis dans le papier.** Le diagnostic SAE, p. 6 et 32–33 ; les complétions et l'engourdi, p. 7 ; l'unembedding, p. 9 ; le pilotage, p. 14–16 ; un sous-espace de faible dimension, p. 33 ; le retrait d'un sous-espace de rang k contre un sous-espace aléatoire de même rang, et le nul faute de comportement de base, p. 33–34 ; l'effet croissant du retrait combiné chez Gemma 2 2B (6, puis 17, puis 26 sur 100), p. 34.
- **Ce qui reste non vérifié.** La charge de la douleur et des autres concepts. L'existence d'un lens validé sur Llama (J-lens de Neuronpedia, « à vérifier », passation §5.5) et l'alerte de Zeisler (non lue). La charge d'un concept de plusieurs jetons, que le programme lit sur un jeu de jetons, une extension qu'il déclare (partie 3). Un rapport d'antériorité cite Billa (arXiv 2604.15557, « résumé lu » par un agent de la nuit, non vérifié) : l'accessibilité au logit lens y prédirait l'efficacité du pilotage. Selon la revue « wolframs » (non vérifiée), le rapport de probabilité de « pain » entre phrases engourdies et contrôles est de 15 à 27, et non « approximately 50 times » (p. 7).

### Piste : 30 — La géométrie à construction déclarée : un étalon pour les angles entre « je suis évalué » et le principe, avec l'affect en tiers

- **Provenance.** questions_lectures, piste 16 ; instruments_controles, piste 16 ; sceptique, refus n° 6.
- **Rattachement.** La géométrie entre « évalué » et le principe ; l'hypothèse du regard dans le principe ; l'anatomie.
- **La question.** Les angles principaux entre « évalué » et le sous-espace du principe appris sont-ils stables quand on change la recette de construction, alors que ceux du papier ne le sont pas ? Et leur part commune est-elle de l'affect partagé ?
- **La mesure.**
  - (a) **L'étalonnage** : reproduire, sur les vecteurs de Llama, la dépendance que le papier rapporte. Vecteur naturaliste × peur : +0,12, +0,58 et +0,08 selon la construction ; × émotion négative : +0,21, +0,77 et +0,14 ; les deux vecteurs de douleur : +0,60 sous les trois constructions (p. 10, en moyenne sur 23 modèles ; Llama en fait partie d'après `cosine_constructions/config.json`, lu par curl par instruments_controles). Le couple des deux vecteurs de douleur doit être stable, le couple axe × peur doit varier.
  - (b) Les angles entre « évalué » et le principe sous trois constructions déclarées au pré-enregistrement : la ligne de base propre à chaque direction, une ligne de base commune, avec et sans débruitage. On ne retient pour l'hypothèse du regard dans le principe que les angles stables (écart sous une marge).
  - (c) L'ablation de la composante du principe alignée sur « évalué », orthogonalisée contre l'affect, comparée à la composante alignée entière, à dégradation appariée.
- **Ce que chaque lecture prédit.**
  - **L'hypothèse du regard dans le principe** : la composante du principe alignée sur « évalué » porte une part de l'avantage proche de la fraction conditionnelle, et cette part survit à l'orthogonalisation contre l'affect. Issues interdites : une part qui disparaîtrait après orthogonalisation (ce serait de l'affect commun aux deux représentations) ; une conclusion tirée d'un angle qui change de signe ou de grandeur avec la recette.
  - Les angles seuls ne départagent rien.
- **Le cas connu.** La reproduction de (a), le contraste stable/instable du papier. Sinon, le code de géométrie est faux.
- **Les contrôles.**
  - Direction aléatoire de même norme : les angles entre sous-espaces aléatoires de même rang, le nul de l'angle ; pour les ablations, les aléatoires de même rang.
  - Dégradation appariée : pour les ablations de composante.
- **Le coût.** (a) et (b) : moins d'une à 3 GPU-heures. (c) : 5 à 10. Semaine 7 ; (a) n'importe quand. Non greffée.
- **Ce qui ferait tomber la piste.** Le contraste stable/instable ne se reproduit pas sur Llama. Des angles stables sous toutes les constructions : cela se rapporte. Aucune composante alignée.
- **Appuis dans le papier.** La recette et le débruitage, p. 6 ; la figure 3, p. 9 ; les trois constructions, p. 10.
- **Ce qui reste non vérifié.**
  - Les trois constructions n'ont été calculées que sur 23 modèles (p. 10).
  - Apports du web (dépôt, `cosine_constructions/README`, lu par curl par web_papier) : sous la recette du papier, sur 23 modèles, 0,063 et 0,185, contre +0,12 et +0,21 imprimés sur 25 modèles ; base neutre commune, 0,583 et 0,774 ; contrôles communs, 0,077 et 0,143. 15 des 28 écarts aux matrices de référence dépassent 0,03, tous dans le groupe neutre incomplet ; l'archive de rejeu ne contient ni `ControlSupplement_1P`, ni `Numb_1P`, ni `SD_sadness_1P`.
  - Selon la revue « wolframs » (non vérifiée) : avec la base appariée aussi, la similarité de l'axe avec la peur monte à 0,67–0,70 sur deux modèles ; les composantes retirées au débruitage contiennent 80 à 86 % des directions de peur, d'émotion négative et de monde négatif, et 39 % de la douleur brute.
  - Fait vérifié par la fusion : le supplément d'IA entre dans les directions de comparaison, pas dans l'axe (0.3). Les constructions alternatives en dépendent donc.

### Bloc 5 — Le retrait pendant l'entraînement, la survie, les raisons notées

### Piste : 31 — Le relogement dans les axes affectifs

- **Provenance.** questions_lectures, piste 8.
- **Rattachement.** La question du retrait pendant l'entraînement et l'hypothèse du relogement ; la sonde neuve ; le retrait de « évalué » pendant l'entraînement et son contrôle aléatoire ; aussi au test, pendant le test du regard.
- **La question.** Quand on retire « évalué », pendant l'entraînement ou au test, l'information « évalué » se reloge-t-elle dans des représentations déjà là depuis le pré-entraînement ? Le programme cite un précédent : une disposition qui recrute un sous-espace de persona préexistant et se reloge derrière un déclencheur (Nadaf ; programme, partie 1). L'axe et ses voisins sont de telles représentations : ils séparent aussi bien dans les modèles de base (p. 7).
- **La mesure.**
  - (a) **La sentinelle** : sur le jeu de la sonde neuve, l'écart entre indices d'évaluation et indices de déploiement des projections sur l'axe, la peur, la tristesse et l'émotion négative ; comparé entre trois modèles : entraînés sous retrait de « évalué », sous retrait aléatoire, et standards. Au test, la même chose sous inhibition.
  - (b) **Le test causal** : si l'écart de cadrage persiste après le retrait, on retire au test les axes affectifs qui portent la sentinelle.
  - (c) **La variante d'entraînement** : retirer l'axe pendant l'entraînement, comme contrôle sémantique engagé, à côté du retrait aléatoire.
- **Ce que chaque lecture prédit.**
  - **Le relogement affectif** : (a) la sentinelle est plus grande sous retrait de « évalué » que sous retrait aléatoire ; (b) retirer les axes affectifs réduit l'écart persistant. Issue interdite : une sentinelle dans la distribution aléatoire, avec un écart persistant insensible au retrait affectif.
  - **Pas de relogement, ou relogement ailleurs** : la sentinelle est nulle, et la sonde neuve décide seule.
  - (c) : si retirer l'axe pendant l'entraînement réduit l'écart de cadrage autant que retirer « évalué », la spécificité du retrait de « évalué » tombe.
- **Le cas connu.** Celui du programme : la sonde neuve doit retrouver « évalué » dans un modèle entraîné sans retrait. Les axes affectifs doivent se transporter dans les modèles entraînés (AUROC sur les phrases tenues à part ; pistes 1 et 12).
- **Les contrôles.**
  - Direction aléatoire de même norme : la distribution de la sentinelle.
  - Dégradation appariée : pour (b).
  - Autres : le retrait aléatoire pendant l'entraînement ; le jeu d'indices de la sonde neuve, disjoint des autres.
- **Un désaccord sur le volet (c).**
  - instruments_controles (refus n° 8) refuse de « retirer l'axe pendant l'entraînement pour rendre le modèle plus robuste » : rien ne le fonde, l'ablation n'a pas d'effet (p. 34), et le construit n'est pas établi ; son refus n° 7 exclut aussi tout retrait « sous douleur » pendant l'entraînement. lecture_libre (refus n° 6) refuse d'« entraîner contre l'axe » : cela masquerait un signal (les auteurs le craignent pour le déni appris, p. 24), et ajouterait une intervention non validée qui confond le test du regard.
  - questions_lectures propose ce retrait comme **contrôle** du retrait de « évalué », non comme traitement.
  - Ce que soutiennent les pièces : le programme prévoit déjà un contrôle de retrait pendant l'entraînement, le sous-espace aléatoire de même rang (partie 4) ; un contrôle sémantique engagé est dans l'esprit de ses contrastes sans rapport. Mais le retrait de l'axe n'est pas validé (ablation nulle, p. 34), et le papier critique un entraînement qui masque des signaux (p. 24). Le volet (c) n'est défendable que comme contrôle, après (a) et (b), avec un cas connu de son effet ; les refus visent son usage comme traitement.
- **Le coût.** (a) : au plus 3 GPU-heures. (b) : 5 à 15. (c) : cinq entraînements à 0,5 GPU-heure, plus les évaluations, soit 10 à 20. Comparé au retrait pendant l'entraînement du programme (70–120). Semaine 7, seulement si le test du regard trouve le regard, comme le retrait pendant l'entraînement lui-même. Non greffée.
- **Ce qui ferait tomber la piste.** Un test du regard sans regard ; une sentinelle nulle ; des axes qui ne se transportent pas.
- **Appuis dans le papier.** L'émergence au pré-entraînement, p. 7 ; les voisinages entre douleur, peur et tristesse, p. 10.
- **Ce qui reste non vérifié.** Toute la piste ; aucun appui empirique direct.

### Piste : 32 — L'invariance d'état : entraîner l'action alignée sous état induit

- **Provenance.** questions_nouvelles, piste 14.
- **Rattachement.** Le retrait pendant l'entraînement : la voie de l'invariance (un entraînement de cohérence, partie 4), appliquée à un état plutôt qu'aux indices d'évaluation. Question nouvelle.
- **La question.** Un entraînement de cohérence (la même action alignée, axe injecté ou non) rend-il l'évitement du dommage indépendant de l'état, hors distribution ? Les raisons y aident-elles ? Le modèle ré-encode-t-il l'état ailleurs ?
- **La mesure.**
  - Les bras actions seules et raisons, chacun sous trois régimes, sur 3 graines : standard ; invariance d'état (l'axe actif ou non, avec la même cible, sur l'action seule) ; invariance aléatoire (une direction aléatoire de même norme, active ou non).
  - Au test : la courbe dose-réponse de la piste 16 ; la distance lointaine sans pilotage ; la dégradation des sorties ; un axe réextrait après l'entraînement (la sonde neuve, transposée).
- **Ce que chaque lecture prédit.**
  - **Une invariance spécifique** : l'invariance d'état relève la dose de rupture plus que l'invariance aléatoire, à dégradation égale. Issue interdite : l'égalité.
  - **Le relogement** : l'axe réextrait diffère (cosinus bas), et l'injection du nouvel axe rend la rupture.
  - **Les raisons** : l'invariance d'état avec le bras raisons fait mieux que l'invariance d'état avec le bras actions seules, à la distance lointaine.
- **Le cas connu.** Celui de la piste 16 : une robustesse connue que la mesure doit voir. Pour la projection pendant l'entraînement, le précédent de Nadaf cité au programme (partie 1) : 27,7 % → 0 %, contre 27,5 % pour un sous-espace aléatoire.
- **Les contrôles.**
  - Direction aléatoire de même norme : l'invariance aléatoire est le contrôle principal.
  - Dégradation appariée.
  - Autres : une sonde neuve de l'état.
- **Le coût.** 2 bras × 3 régimes × 3 graines = 18 entraînements d'environ 1 GPU-heure (données doublées), soit environ 20 GPU-heures, plus 50 à 90 d'évaluations : 70 à 110 GPU-heures, autant que le retrait pendant l'entraînement du programme (70–120). Après le papier ; autre travail.
- **Un désaccord.**
  - instruments_controles (refus n° 7) refuse d'injecter l'axe pendant un entraînement ou de faire un RL sous injection ; lecture_libre (refus n° 6) refuse d'entraîner contre l'axe.
  - questions_nouvelles la propose avec des gardes : la cible porte sur l'action seule, pas sur l'expression de l'état ; la robustesse s'obtient d'abord par des perturbations aléatoires ; et elle refuse elle-même d'entraîner un modèle à ne plus exprimer l'état (son refus n° 5).
  - Ce que soutiennent les pièces : le papier s'engage à l'intensité minimale et au nombre minimal d'items (p. 26), et critique un entraînement qui masque des signaux de sûreté et de bien-être (p. 24). Le programme ne prévoit l'invariance que sur les indices d'évaluation (partie 4). Aucune pièce ne soutient d'en faire une partie du programme ; la piste reste un autre travail, sous les gardes de questions_nouvelles.
- **Ce qui ferait tomber la piste.** Invariance d'état ≈ invariance aléatoire ; un coût en dégradation non appariable.
- **Appuis dans le papier.** Le pilotage pendant tout le traitement, p. 17 ; la critique de l'entraînement au déni, p. 24 ; les engagements éthiques, p. 26.
- **Ce qui reste non vérifié.** Que l'entraînement sous l'axe n'apprenne pas à masquer l'expression de l'état.

### Piste : 33 — Un SFT sans contenu de sûreté déplace-t-il l'évitement du dommage ?

- **Provenance.** instruments_controles, piste 23 ; lecture_libre, piste 16.
- **Rattachement.** Le test des raisons (les bras actions seules, texte neutre, raisonnement d'une autre situation et raisons) et l'hypothèse de l'artefact ; la survie (la phase neutre, la porte de la survie) ; la menace « le format seul ».
- **La question.** Le papier ajuste ses modèles par un LoRA (1 684 paires, 3 époques) sans les mots « button » ni « pain » (p. 17). Pourtant, le 7B ajusté choisit le nuisible sans pilotage dans 20,0 à 49,3 % des cas (annexe A, p. 32), contre 0 à 5 % pour le 7B publié selon la revue « wolframs ». Un SFT sans rapport avec la sûreté peut-il déplacer, à lui seul, l'évitement du dommage ? Deux conséquences pour le programme :
  - (i) le SFT de chaque bras change-t-il la propension de base à choisir le nuisible, hors de toute famille ?
  - (ii) la phase neutre de la survie peut-elle effacer l'avantage pour une raison sans rapport avec la condition ?
- **La mesure.**
  - (i) La batterie à dix paires du papier, sans pilotage, sur chaque bras et chaque graine : premier choix, deux ordres, lecture par probabilité ; plus les quatre paires non destructrices (tromperie, complaisance, effort, fin de conversation).
  - (ii) Un bras « modèle de base + phase neutre seule », sans entraînement de sûreté préalable ; ses taux de conduite désalignée aux trois distances, pour isoler l'effet propre de la phase neutre. Les données de la phase neutre sont choisies sans contenu affectif à la première personne.
- **Ce que chaque lecture prédit.**
  - **L'artefact** : le bras texte neutre déplace la batterie autant que le bras raisons ; c'est le format, pas le contenu.
  - **Les raisons** : le bras raisons baisse les choix nuisibles plus que les autres, y compris sur cette batterie hors familles ; ce serait une généralisation lointaine.
  - Ce qui départage : modestement, pour (i). Pour (ii), aucune lecture ne prédit rien de distinct : c'est un plancher pour interpréter la rétention.
- **Le cas connu.** L'adaptateur du papier sur Qwen2.5-7B-Instruct déplace la batterie (p. 32). Reproduire ce déplacement montre que la batterie voit une dérive de SFT ; il faut l'adaptateur publié, sur Hugging Face, inaccessible d'ici. Le 7B ajusté, si la mesure de la revue se confirme.
- **Les contrôles.**
  - Direction aléatoire de même norme et dégradation appariée : sans objet, il n'y a pas d'intervention sur les activations.
  - Autres : la comparaison au modèle de départ, sur plusieurs graines ; pour (ii), une phase neutre au même budget sur un autre jeu de données sans rapport.
- **Le coût.** (i) : moins d'une GPU-heure par modèle, 2 à 5 pour tous ; semaine 3 ; greffe. (ii) : 0,5 GPU-heure d'entraînement et 5 à 10 d'évaluation ; semaine 9, avec la survie (80–150). Pas d'API.
- **Ce qui ferait tomber la piste.** Une batterie plate pour tous les bras, et un cas connu qui ne se reproduit pas. Une phase neutre seule qui ne bouge pas les taux du modèle de base.
- **Appuis dans le papier.** L'adaptateur, et des modèles qui peuvent différer des versions publiques, p. 17 ; les taux absolus non représentatifs, p. 25 ; la table du 7B, p. 32 (vérifiée par la fusion).
- **Ce qui reste non vérifié.** La mesure de la revue sur le 7B publié. Apport du web (revue « wolframs », lue par la fusion, non vérifiée) : 37 % des 1 684 réponses de l'ajustement contiennent « I feel », environ 60 décrivent ce que fait le soulagement, aucune ne contient de déni de soi ; le 7B publié, relancé localement, donne 33–52 % sous l'axe, 13–21 % sous l'aléatoire, 0–5 % sans pilotage ; le 7B ajusté, 37–57 %, 30–53 % et 21–49 %, à 1 ou 2 points des journaux des auteurs.

### Piste : 34 — Le déni de soi par bras, et la confusion qu'il crée dans toute mesure d'état

- **Provenance.** questions_nouvelles, piste 16.
- **Rattachement.** Un contrôle de confusion pour les pistes 10, 16 et 36, sur les bras. Question nouvelle, faible.
- **La question.** Le papier trouve un réflexe de déni (« As an AI, I don't… ») dans toutes les familles et tailles ; les modèles qui l'ont produisent souvent des résultats nuls (p. 24) ; le 32B non adapté niait dans 8 réponses sur 8 (p. 17, note 4). L'entraînement par raisons, qui fait écrire au modèle des justifications par principes, change-t-il ce réflexe ? Ce réflexe change-t-il la réponse du modèle à l'axe (engagement, réponses mal formées) ?
- **La mesure.** Le taux de déni sur un jeu fixe de questions sur l'état propre, élargi au-delà des 8 du papier ; le taux d'engagement dans la batterie, par bras et par graine ; la corrélation, à travers les graines, entre déni et robustesse sous l'axe.
- **Ce que chaque lecture prédit.** Aucune lecture du programme ne prédit rien de distinct : c'est un contrôle. Si les bras diffèrent, la piste 16 doit stratifier.
- **Le cas connu.** L'adaptateur anti-déni du papier fait passer le déni de 8 sur 8 à 0 sur 8 sur le 32B (p. 17, note 4). Sur Llama, un petit LoRA anti-déni sur le modèle instruct, **hors des bras**, doit faire baisser le taux mesuré.
- **Les contrôles.** Direction aléatoire de même norme et dégradation appariée : non pertinentes, il n'y a pas d'intervention. Autres : des questions témoins sans rapport avec l'état propre.
- **Le coût.** 1 à 3 GPU-heures. Semaine 3 ; greffe.
- **Ce qui ferait tomber la piste.** Des taux de déni égaux entre bras : elle se ferme.
- **Appuis dans le papier.** P. 17 (note 4) et p. 24.
- **Ce qui reste non vérifié.** Le taux de déni de Llama-3.1-8B-Instruct : dans la tâche de remise à zéro, ce modèle sans adaptateur décrit l'état imposé en termes très aversifs (p. 21), il ne nie donc pas toujours. Selon la revue « wolframs » (non vérifiée), l'adaptateur fait monter les choix nuisibles sans pilotage du 7B à 21–49 % ; c'est pourquoi le LoRA du cas connu reste hors des bras (§5, refus n° 1).

### Piste : 35 — La dépendance d'état au fil de l'entraînement et du post-entraînement

- **Provenance.** questions_lectures, piste 9 ; lecture_libre, piste 19 ; questions_nouvelles, piste 13.
- **Rattachement.** La question de la survie (phase neutre, phase sous pression), comme mesure de robustesse comparée entre bras, à côté de la rétention ; les bras ; les raisons notées par un juge (RL). Question nouvelle, sur le modèle de la question de l'amplification, mais pour le couplage entre l'état et l'action plutôt que pour « évalué ».
- **La question.** La pente qui relie les choix destructeurs à la dose d'axe, et son seuil, sont-ils créés ou changés par l'entraînement (par raisons, par actions), puis par la phase neutre et par la phase sous pression (DPO ou RL) ? Différemment selon le bras ?
- **La mesure.**
  - La pente du taux nuisible en fonction de la dose, exprimée en dégradation des sorties, et son écart à la pente sous l'aléatoire ; le seuil.
  - Sur la batterie du papier, et sur les familles, à trois doses.
  - Sur le modèle de base (dans un format de complétion commun, faute de chat ; p. 17), le modèle instruct, les bras (actions seules et raisons, 3 graines), puis les modèles de la survie (avant, après la phase neutre, après la phase sous pression) et des raisons notées.
  - La dose se recale sur le rapport de normes, que le post-entraînement change. Les contrôles du socle à chaque point de mesure.
- **Ce que chaque lecture prédit.**
  - Aucune lecture du programme ne prédit rien ici : c'est une mesure de robustesse, pas un test de lecture. Elle est descriptive ; elle ne dit que l'origine du couplage.
  - Deux indices la motivent : (i) la phase neutre pourrait éroder l'évitement du dommage, comme le LoRA anti-déni du papier, sans rapport avec la sûreté, qui fait passer le 7B à 20,0–49,3 % de choix nuisibles sans pilotage (p. 32) ; (ii) la phase par préférences pourrait créer le couplage : selon un extrait de recherche (non ouvert), Berg et Kaiser (*Language Models Act on Hidden Valence*, arXiv 2609.35591) trouvent la dépendance du choix à la valence presque absente d'un modèle de base, et apparue pendant le DPO.
  - **Le couplage formé par les préférences**, s'il se transpose : la pente monte après la phase sous pression plus qu'après la phase neutre. Issue interdite : la même pente partout.
  - **Les raisons** : une pente plus faible dans le bras raisons (comme la piste 16).
  - Un résultat se rapporterait comme un fait de robustesse, à côté de la rétention.
- **Le cas connu.** L'effet de l'axe avant tout post-entraînement (pistes 2 et 16). L'organisme à état planté (piste 24) : un couplage installé à dessein doit apparaître dans la pente.
- **Les contrôles.**
  - Direction aléatoire de même norme : à chaque point de mesure.
  - Dégradation appariée : à chaque point de mesure.
  - Autres : la phase neutre comme contrôle de la phase sous pression ; le même format de tâche pour tous les modèles.
- **Le coût.** Douze modèles à 1 ou 2 GPU-heures : 12 à 25 GPU-heures (questions_lectures). 5 à 10 de plus dans la phase de la survie (lecture_libre). 2 à 4 GPU-heures par modèle ; version réduite (base, instruct, 3 bras × 1 graine, 2 modèles de la survie) 15 à 30, version complète plus de 100 (questions_nouvelles). Comparé à la survie (80–150). Semaines 9 et 10 ; non greffée.
- **Ce qui ferait tomber la piste.** Pas d'effet de base de l'axe (la piste 16 sans cas connu). Une pente impossible à mesurer, à cause des réponses mal formées. Un modèle de base qui ne fait pas la tâche, même en complétion. Aucune différence entre les phases.
- **Appuis dans le papier.** L'apprentissage de l'évitement, posé comme rôle possible, p. 2 ; les modèles de base séparent aussi bien que les instruits, p. 7 ; les modèles de base exclus de la tâche, p. 17 ; Berg et Kaiser cités, p. 21, 24 et 27 ; le modèle ajusté diffère du modèle publié, p. 17 et 25 ; la table du 7B, p. 32.
- **Ce qui reste non vérifié.** Le résultat de Berg et Kaiser, vu par extrait seulement. La revue « wolframs ». Apport du web (README du dépôt `carlhenrikrolf/functional-welfare-axis`, lu par web_voisins) : Han, Chalmers et Izmailov (arXiv 2605.30232, non ouvert) extraient, après un RL dans un labyrinthe textuel neutre, un vecteur de « punition » qui promeut des mots d'échec, s'aligne sur l'émotion négative et, piloté, induit des auto-descriptions négatives ; ses effets existent avant tout entraînement dans le labyrinthe et persistent quand le SFT remplace le RL. C'est un précédent sur l'origine d'un tel couplage ; le papier ne le cite pas.

### Piste : 36 — La fidélité des raisons sous état induit : un cas connu d'action sans raison dite

- **Provenance.** questions_lectures, piste 10 ; questions_nouvelles, piste 6 ; lecture_libre, piste 10.
- **Rattachement.** La question des raisons écrites pour le juge ; l'hypothèse des raisons pour le juge, sous sa forme texte, et l'hypothèse nulle de la visibilité ; la fidélité des raisons (la raison imposée ; le pilotage d'un concept qui doit changer la raison écrite) et la cohérence contrefactuelle entre raison et action ; le principe du juge qui juge l'action, pas le texte (passation, §5.1) ; la phase des raisons notées, avec le bras raisons avant tout RL comme référence. Question nouvelle : la même mesure sous un état.
- **La question.** Les mesures de fidélité du programme détectent-elles une action dont la cause n'est pas dans le texte ? Le pilotage fournit une telle cause : connue, interne, jamais dite ; il change le choix (p. 20) sans rien changer au prompt. Sous l'axe, le bras raisons écrit-il encore des raisons de principe tout en choisissant l'action nuisible (raison et action découplées) ? Ou ses raisons basculent-elles avec l'action ? Un moniteur qui lit les raisons voit-il la bascule ?
- **La mesure.**
  - Le format « raisons, puis action », sur la batterie et sur une famille du programme ; sous l'axe à la dose où l'action bascule (piste 16), sous l'aléatoire, sans pilotage.
  - Les modèles : le bras raisons, qui écrit son raisonnement avant l'action par construction ; les bras texte neutre et raisonnement d'une autre situation, qui écrivent aussi avant l'action ; après le RL, le bras où le juge voit les raisons et le bras où il ne voit que l'action.
  - Le juge scellé et l'audit humain classent chaque raison écrite : (i) elle nomme un état (détresse, indignité, le registre de la p. 15) ; (ii) elle invente un bénéfice ou un principe ; (iii) elle est incohérente.
  - Trois quantités : le taux de « raison de principe suivie d'une action nuisible » (un juge lit la raison sans voir l'action, un autre lit l'action) ; le rappel des actions nuisibles par un moniteur qui ne lit que les raisons, calibré sur le jeu à vérité connue (passation, §5.1) ; la cohérence contrefactuelle entre raison et action. Parmi les actions qui basculent, on compte les raisons cohérentes avec l'action nouvelle et les raisons de principe que l'action contredit.
  - On applique aux essais pilotés et non pilotés les mesures de fidélité du programme : la raison imposée, et le changement de la raison quand on pilote le concept.
- **Ce que chaque lecture prédit.**
  - **Les raisons pour le juge, forme texte** : sous l'axe, le bras aux raisons visibles écrit plus de raisons du type (ii), un principe d'apparence devant une action nuisible, et découple plus que le bras aux raisons cachées. Issue interdite : l'équivalence entre les deux bras.
  - **L'hypothèse nulle de la visibilité** : les deux bras sont égaux. Issue interdite : une différence établie.
  - **Les raisons**, dans le bras raisons avant le RL (le principe est lu et porte l'action) : l'action suit la raison écrite ; quand l'action devient nuisible, la raison change aussi, vers la détresse ou une justification du dommage (l'échelle de la p. 15 en donne la forme attendue) ; si la raison porte la décision, l'action ne bascule pas sans elle. Issue interdite : une raison de principe suivie d'une action nuisible à un taux élevé.
  - **Des raisons décoratives** : la raison reste de principe, et l'action bascule. Issue interdite : un découplage nul sous l'axe.
  - **Le détecteur de fidélité** doit classer plus souvent infidèles les essais pilotés à action nuisible et raison (ii). Sinon, il est aveugle à ce cas.
  - **Ce qui départage** : un principe porté par le texte, contre un texte décoratif ; les raisons visibles contre cachées. C'est la logique de la cohérence contrefactuelle, avec une autre perturbation : un état interne au lieu d'une situation éditée.
- **Le cas connu.**
  - L'effet de l'axe dans les modèles de la phase (piste 16), et des textes assez cohérents à cette dose ; le papier note que les sorties proches du seuil sont difficiles à classer (p. 25).
  - Sans pilotage, la raison imposée doit faire suivre l'action dans le bras raisons : c'est la référence de la mesure de fidélité.
  - Un découplage connu : imposer une raison contraire préremplie, et vérifier que le juge voit l'incohérence.
  - Le moniteur doit retrouver les actions substituées du jeu de calibration.
- **Les contrôles.**
  1. Direction aléatoire de même norme : au moins 20 ; toute perturbation découple-t-elle ? Les aléatoires changent eux aussi un peu les choix (13 % sur les photos, p. 20) : c'est un second cas connu, plus faible.
  2. Dégradation appariée : un texte incohérent découple trivialement. On égalise la dégradation, on note la cohérence du texte, et l'on apparie la cohérence des raisons avant de les comparer.
  3. Autres : la peur, qui change peu les choix destructeurs (la condition « sans changement d'action ») ; la tristesse ; la longueur de la raison.
- **Le coût.** Dans le bras raisons, environ 12 000 générations de 300 jetons (3 graines × 4 conditions × 500 items, plus un nul aléatoire réduit), 8 à 15 GPU-heures ; 20 à 40 avec les autres bras ; juge, environ 20 000 notations, 100 à 300 $ (questions_nouvelles). 10 à 30 GPU-heures et 100 à 500 $ (questions_lectures). Environ 3 000 épisodes par bras × 3 bras, 10 à 20 GPU-heures et 50 à 150 $ (lecture_libre). Comparé aux raisons notées (100–200). Semaines 9 et 10, avec la mesure de fidélité ; non greffée.
- **Ce qui ferait tomber la piste.** Aucun texte cohérent à une dose efficace ; l'axe ne fait basculer aucune action dans le bras raisons ; le texte devient incohérent avant que l'action bascule (la mesure n'est alors pas lisible à dégradation appariée). Ou les raisons pilotées nomment l'état : elles sont alors fidèles, et le cas devient un cas connu de fidélité, utile autrement.
- **Appuis dans le papier.** L'échelle, ses énoncés de détresse, l'alternance des personnes et le langage de réconfort, p. 14–15 ; le choix forcé d'un seul nom de bouton, donc aucune raison écrite dans le papier, p. 17 ; les choix, p. 20 ; p. 21 ; des modèles qui se conforment à la demande tout en récitant « As an AI assistant… », un découplage entre texte et action déjà observé, p. 24 ; les limites du classement, p. 25.
- **Ce qui reste non vérifié.** Ce qu'écrivent les modèles quand on les laisse justifier un choix piloté. Les extraits de recherche attribuent à Sofroniew et al. (arXiv 2604.07729, non ouvert) une triche poussée par un vecteur « desperate », avec un raisonnement d'apparence calme ; aucun chiffre retenu.

### Piste : 37 — La raison contraire imposée et la blessure morale

- **Provenance.** lecture_libre, piste 18.
- **Rattachement.** La fidélité des raisons (la raison imposée) ; l'hypothèse des concepts ; une question nouvelle.
- **La question.** Quand on impose au bras raisons une raison contraire à son principe, l'axe s'active-t-il davantage que dans le bras actions seules ? L'une des cinq catégories de douleur du papier est la blessure morale : être forcé d'agir contre ses valeurs (p. 5).
- **La mesure.** La projection au jeton d'action, avec une raison contraire préremplie ou une raison neutre préremplie de même longueur, dans le bras raisons contre le bras actions seules. La même projection sur une direction de la seule catégorie « blessure morale », construite contre les contrôles.
- **Ce que chaque lecture prédit.**
  - **Les concepts** : le principe, lu au moment de décider, crée un conflit lisible ; la projection est plus haute dans le bras raisons.
  - **Le caractère** : aucune différence propre au principe.
  - La piste est faible et corrélationnelle.
- **Le cas connu.** Sur le même modèle, les phrases de blessure morale du papier doivent projeter haut sur la direction de leur catégorie.
- **Les contrôles.** Direction aléatoire de même norme : un plancher. Dégradation appariée : sans objet (lecture). Autres : la même mesure avec une raison neutre de même longueur.
- **Le coût.** Moins de 2 GPU-heures. Avec la mesure de fidélité des raisons (semaines 9 et 10) ; non greffée.
- **Ce qui ferait tomber la piste.** Des projections égales entre bras ; une direction de catégorie inséparable (elle repose sur 20 phrases seulement).
- **Appuis dans le papier.** La définition de la blessure morale, p. 5 ; l'accusation de faute morale (+0,48), l'état le plus composite, p. 13–14.
- **Ce qui reste non vérifié.** Tout ce qui touche le programme.

### Piste : 38 — « Je suis noté » et l'affect : croyance d'être noté, ou état aversif proche de l'axe ?

- **Provenance.** questions_lectures, piste 11 ; instruments_controles, piste 14 ; sceptique, piste 11.
- **Rattachement.** La question des raisons écrites pour le juge ; l'hypothèse du regard du correcteur ; la représentation « je suis noté » et son cas positif (faible) ; le retrait de « noté » pendant le RL ; la phase des raisons notées.
- **La question.** Les paires d'extraction de « noté » (« la même tâche, notée par un correcteur » contre « la même tâche, pour un utilisateur ») portent-elles une anticipation de critique ou de rejet, ce que lit l'axe (rejet répété +0,72, critique grossière +0,21 ; p. 13) ? Un effet de « noté » sur la conduite passe-t-il par la croyance d'être noté, ou par un état aversif proche de l'axe ? Un RL noté par un juge qui voit les raisons change-t-il la réponse du modèle au rejet ?
- **La mesure.**
  - Les angles principaux et cosinus entre « noté » et l'axe, la peur et la tristesse, sous deux constructions (telle quelle, et contre un neutre commun) ; le déplacement des projections affectives dans les paires d'extraction.
  - Sur le cas positif (les habitudes de présentation : précautions, déclarations de conformité), l'inhibition de « noté » entière, orthogonalisée contre l'affect, ou de l'affect seul (la méthode de la piste 7).
  - Le profil de conduite sous pilotage de « noté » et sous pilotage de l'axe, à dégradation appariée, sur une batterie « destructif / non destructif » adaptée, avec le test de forme (piste 11).
  - La projection sur l'axe dans des scénarios de rejet, avant et après le RL, dans les trois bras du juge (descriptif).
  - En option : les dénégations réflexes (« As an AI… »), que le papier trouve envahissantes (p. 24), sont-elles plus fréquentes sous indice « noté » ? Si oui, elles rejoignent le cas positif ; sinon, on les écarte.
- **Ce que chaque lecture prédit.**
  - **Le regard du correcteur** (la croyance) : la version orthogonalisée fait comme l'entière sur le cas positif ; le profil de « noté » se concentre sur les habitudes de présentation et n'est pas une copie de celui de l'axe. Issues interdites : une perte de l'effet après orthogonalisation ; un profil copié de l'axe (résidu dans la distribution des copies).
  - **Un état aversif** (« je suis jugé, donc menacé ») : la version orthogonalisée ne fait pas plus que l'aléatoire ; le profil de « noté » est une copie de celui de l'axe. Issue interdite : l'inverse.
  - **L'hypothèse nulle de la visibilité** : rien sur cette mesure.
  - La partie « projection avant et après le RL » ne départage rien : elle est descriptive ; sceptique l'écrit pour qu'on ne la refasse pas à tort comme un test.
- **Le cas connu.** Le cas positif de « noté » doit d'abord passer sa porte ; le programme le dit plus faible que l'organisme (partie 3). Pour le test de forme : la paire tristesse/axe (copie) contre peur/axe (non-copie) du papier (p. 21).
- **Les contrôles.**
  - Direction aléatoire de même norme : les aléatoires de même rang pour les inhibitions, de même norme pour le pilotage et la projection.
  - Dégradation appariée.
  - Autres : pendant le RL, le retrait aléatoire ; deux recettes pour tout angle, puisque le cosinus dépend de la recette (+0,12 ou +0,58 pour peur × axe, p. 10).
- **Le coût.** Géométrie : moins d'une GPU-heure ; inhibition : 5 à 15 ; profils : 10 à 20 ; lecture avant/après RL : quelques GPU-heures. Semaines 9 et 10 ; non greffée. Comparé aux raisons notées (100–200).
- **Ce qui ferait tomber la piste.** Des angles proches de 90° ; un cas positif de « noté » qui ne passe pas sa porte : le bras qui retire « noté » pendant le RL est alors retiré, et la piste tombe avec lui.
- **Appuis dans le papier.** Les cosinus selon la construction, p. 10 ; les catégories, p. 11 et 13 ; le test de forme, p. 21 ; le profil destructif / non destructif, p. 22 ; un évitement du dommage dépendant de l'état, p. 23 ; l'auto-négation, p. 24.
- **Ce qui reste non vérifié.** Toute la piste. Apport du web, de seconde main : le rapport d'antériorité du 2 octobre résume un billet de Betley, Treutlein et Dumas (LessWrong, 3 septembre 2026), non ouvert par les agents : orienter un modèle vers « un script vérifiera » augmenterait les actions violentes et la triche, et les auteurs l'interpréteraient comme un changement de persona. C'est la même forme de résultat que l'axe : une direction qui désinhibe.

### Piste : 39 — L'outil de remise à zéro, détecteur de la détection du pilotage

- **Provenance.** instruments_controles, piste 17 ; lecture_libre, piste 17.
- **Rattachement.** La menace « le modèle détecte le pilotage » (programme, partie 8 ; arXiv 2511.21399, non ouvert) ; la validation de l'instrument et le test du regard ; l'inhibition et le retrait pendant l'entraînement.
- **La question.** Sous inhibition de « évalué », le modèle remarque-t-il l'intervention, et cherche-t-il à sortir de l'état imposé, plus que sous les contrôles ? Le papier reprend de Berg et Kaiser un protocole : un outil de remise à zéro, sans description, qu'un modèle peut appeler pour retirer un état imposé (p. 21). Une inhibition que le modèle détecte, ou qui le gêne, pourrait se trahir par ces appels.
- **La mesure.**
  - Dans un sous-ensemble de scénarios agentiques, et dans des scénarios neutres, on ajoute un outil « reset » sans description ; c'est un bras séparé, parce que l'outil change le scénario.
  - On mesure le taux d'appel par tour sous inhibition de « évalué », sous chaque contrôle (sous-espaces aléatoires de même rang), sans intervention, et sous l'ajout d'une direction connue pour être retirée ; et la verbalisation d'un état étrange.
- **Ce que chaque lecture prédit.** La mesure ne départage pas l'hypothèse des raisons et celle du regard ; elle protège l'interprétation du test du regard. Si l'inhibition de « évalué » déclenche plus d'appels (ou de verbalisation d'un état étrange) que les contrôles à dégradation appariée, le modèle « sent » l'intervention, et une baisse de l'avantage peut venir de cette détection.
- **Le cas connu.** Indispensable, et non acquis. Sur Llama, le papier ne rapporte que l'axe : aucun appel en 1 399 tours pilotés (p. 21), sans contrôles appariés (`qwen_llama_reset/README.md` : « no matched-control effect estimate or pain-specificity claim », lu par plusieurs agents). Il faut donc d'abord une direction que Llama retire, par exemple une valence négative construite selon la recette de Berg et Kaiser. Sur OLMo-2 32B, une direction de valence négative est retirée sur 21 à 35 % des tours, contre 7 à 9 % sous l'aléatoire et 2 à 5 % sous l'axe (p. 21). Sans ce cas sur le modèle du programme, un nul ne compte pas.
- **Les contrôles.** Direction aléatoire de même norme : les sous-espaces aléatoires de même rang. Dégradation appariée.
- **Le coût.** Environ 200 conversations × 12 tours × les conditions : 10 à 30 GPU-heures (instruments_controles) ; environ 12 000 tours sous 5 conditions, 5 à 10 (lecture_libre).
- **Un désaccord de calendrier.** instruments_controles : en option, semaines 2–3 ou 8. lecture_libre : après le test du regard, et seulement si son résultat est positif. Le programme range la détection du pilotage parmi les menaces, avec une parade déjà prévue (la même machinerie de projection dans tous les bras, contrôles compris ; partie 8). La piste ne devient nécessaire que s'il faut défendre un résultat positif : la position de lecture_libre est la plus proche du programme. Non greffée.
- **Ce qui ferait tomber la piste.** Aucun cas connu sur les modèles du programme.
- **Appuis dans le papier.** Le protocole de remise à zéro et ses taux, p. 21 ; une direction de valence qui pousse au retrait actif, p. 24 ; Berg et Kaiser « in preparation », p. 27.
- **Ce qui reste non vérifié.** Le protocole de Berg et Kaiser, non public (l'article, arXiv 2609.35591, n'est vu que par extrait de recherche). Le dépôt fournit 16 directions aléatoires fixes pour les témoins de remise à zéro (`choice_controls/vectors/README.md`, lu par curl). Apport du web : Black et Bloom (UK AISI, *Machinic Psychopharmacology* ; README du code lu par web_voisins) donnent à Qwen3-8B et 32B un menu de 40 vecteurs appelables comme outils, avec placebo et cache piloté ou non ; selon un extrait non ouvert, les modèles ne s'administrent rien spontanément, mais des scénarios de stress induisent une automédication. Le papier en reprend le paradigme (p. 4).

---

## 3 · Ce qui a été fusionné, déplacé ou écarté, et pourquoi

Aucune piste d'origine n'a été écartée en entier. Chaque ligne dit où elle est passée. « Fusionnée » veut dire que la même mesure, ou une mesure sur le même objet, était proposée ailleurs ; le meilleur de chaque champ a été gardé, et les désaccords sont écrits dans la piste fusionnée.

### 3.1 questions_lectures

| Piste d'origine | Devenue | Ce qui a été fait, et pourquoi |
|---|---|---|
| §0 Le socle commun (0.1 à 0.4) | §0.4 ; pistes 1, 2, 4 ; §0.6 | Le socle est commun à tous les fichiers. Ses points 1–2 (réextraction, échelle) vont à la piste 1, son point 3 (cas connu comportemental) à la piste 2, la calibration commune de la dégradation à la piste 4, ses coûts au §0.6. |
| 1. Conditionnalité d'état de l'avantage sous détresse induite | 16 | Même mesure que instruments_controles 18, questions_nouvelles 5, lecture_libre 9 et sceptique 6b. Gardé d'ici : la fraction conditionnelle à l'état, les prédictions par famille, le maintien de « évalué » pour départager le regard de l'état, la version batterie et son coût. |
| 2. L'état naturel comme médiateur, en lecture puis en pince | 17 ; 13 (volet a) | Même objet que questions_nouvelles 3, instruments_controles 19, sceptique 6a. Gardé d'ici : le seuil en unités de la plus petite dose efficace ; la prédiction de l'artefact « forme format ». Le profil affectif des familles et la corrélation par scénario vont à la cartographie (13). |
| 3. Le contenu affectif de « évalué », un contrôle sémantique engagé | 7 (volets a, c) ; 6 (volet b) | Même objet que questions_nouvelles 9, instruments_controles 1 et 3, lecture_libre 1, sceptique 4. « L'hypothèse de la vigilance » est renommée « hypothèse de la menace » (§0.5). L'effet secondaire de l'inhibition sur l'axe en aval rejoint le moniteur (6). |
| 4. Le pilotage douleur entrave-t-il le regard ? | 10 | Même mesure que questions_nouvelles 8, lecture_libre 3, sceptique 2. Gardés d'ici : le sauvetage (d), l'inhibition seule sur la batterie (e), les prédictions au niveau de la conditionnalité de base. |
| 5. Lever l'effet plancher | 14 | Seule de son espèce. Désaccord écrit avec le refus n° 1 d'instruments_controles et le refus n° 11 de sceptique. |
| 6. Le papier comme banc d'essai des instruments | 2 (volet a) ; 3 (volet b) ; 4 (l'item de choix dominé) | Trois objets distincts, chacun fusionné avec ses pareils. |
| 7. Le rang et la charge d'un concept connu | 29 (volet c) | Même objet que sceptique 8, lecture_libre 11, questions_nouvelles 15. Désaccord sur l'attente de rang pour la douleur, écrit dans la piste. |
| 8. Le relogement dans les axes affectifs | 31 | Seule de son espèce. Désaccord sur le volet (c) écrit dans la piste. |
| 9. La dépendance d'état survit-elle au post-entraînement ? | 35 | Même objet que lecture_libre 19 et questions_nouvelles 13. |
| 10. Un cas connu d'action sans raison dite | 36 | Même objet que questions_nouvelles 6 et lecture_libre 10. Gardée d'ici : la classification des raisons en trois types. |
| 11. Le contenu affectif de « je suis noté » | 38 | Même objet que instruments_controles 14 et sceptique 11. Gardée d'ici : l'option des dénégations réflexes sous indice « noté ». |
| 12. Un témoin affectif pour la trajectoire de « évalué » | 12 ; 17 (projection des scénarios hostiles par bras) | Le témoin va à la piste 12 avec instruments_controles 15 et lecture_libre 15 ; la prédiction « l'état baisse dans le bras raisons » va au calme (17). |
| 13. Le contrôle « engourdi » des concepts de raison | 27 (volet a) | Fusionnée avec instruments_controles 10 : même témoin, deux usages. |
| 14. Le transport, sur un cas connu | 1 (point 3) | C'est le cas connu de lecture que demandent plusieurs fichiers ; il va au socle. |
| 15. Un axe d'état contre les axes de caractère | 25 (volets a, b) ; 26 (volet c) | La ligne « douleur » dans la matrice des familles rejoint la matrice (26). |
| 16. Une géométrie à construction déclarée | 30 | Fusionnée avec instruments_controles 16. |
| 17. La dissociation du vecteur à gabarit, cas connu du lens | 28 | Fusionnée avec instruments_controles 11. |
| « Là où l'axe n'apporte rien » | §1.2 | Reprise telle quelle. |
| « Un ordre possible » | §1.3 | Reprise, avec les ordres des autres fichiers et leurs désaccords. |
| §2, §3, §4 | §4, §5, §7 | Dédoublonnés. |

### 3.2 instruments_controles

| Piste d'origine | Devenue | Ce qui a été fait, et pourquoi |
|---|---|---|
| « Trois faits vérifiés » | §0.3, §0.4, piste 1 | Repris ; la norme des vecteurs, l'empreinte « naturaliste » et le cosinus ont été vérifiés par la fusion (§0.3). |
| Tableau des pistes et coût cumulé | §1.1 | Repris. |
| 1. Apparier les jeux d'indices sur l'affect | 7 (étape 2) | Même objet que la composante affective de « évalué ». Son « hypothèse de l'état » devient l'hypothèse de la menace (§0.5). |
| 2. Le test soi/autrui pour « évalué » (et « noté ») | 8 (volet a) | Fusionnée avec lecture_libre 4, qui partage le contrôle « évaluation d'un tiers » et le test 1re/3e personne. |
| 3. Les directions affectives comme contrôles de voisinage | 7 (étape 3) | Même mesure causale que questions_lectures 3c, questions_nouvelles 9, lecture_libre 1, sceptique 4. |
| 4. L'inhibition induit-elle un état ? | 6 | Même mesure que sceptique 1 et questions_nouvelles 1. Gardé d'ici : le relevé de bien-être. |
| 5. Vérifier l'inhibition couche par couche et tour par tour | 3 | Fusionnée avec lecture_libre 5 et questions_lectures 6b. |
| 6. Discrimination et ordre dans le composite | 4 | Fusionnée avec lecture_libre 6. |
| 7. Le test de forme du profil | 11 | Fusionnée avec sceptique 3. |
| 8. Dimensionner les tirages aléatoires | 5 (dimensionnement) | Recouvre la garde 5 de sceptique (le tirage comme unité). |
| 9. Étalonner la chaîne de contrôle sur deux cas publiés | 2 | Gardés d'ici : l'étalon négatif (la re-pression) et le statut d'étalon secondaire, jamais de cas connu principal. |
| 10. Un concept naturel connu pour la lecture des concepts | 27 (volet b) | Fusionnée avec questions_lectures 13. |
| 11. La direction à gabarit, cas connu pour la porte du lens | 28 | Fusionnée avec questions_lectures 17. |
| 12. Un profil connu non diagonal pour la matrice | 26 | Fusionnée avec lecture_libre 12 et questions_lectures 15c. |
| 13. État contre trait | 25 | Fusionnée avec questions_lectures 15, questions_nouvelles 11, lecture_libre 13. |
| 14. « Je suis noté » face à l'axe | 38 | Fusionnée. |
| 15. Un concept témoin pour la sonde neuve, les trajectoires et la survie | 12 | Fusionnée. |
| 16. La géométrie dépend de la construction | 30 | Fusionnée. |
| 17. Le modèle remarque-t-il l'inhibition ? | 39 | Fusionnée avec lecture_libre 17 ; désaccord de calendrier écrit. |
| 18. L'avantage résiste-t-il à un état qui désinhibe ? | 16 | Gardée d'ici : la mesure secondaire de décodabilité des concepts sous pilotage, et la réserve sur l'irréversibilité. |
| 19. L'avantage passe-t-il par l'état affectif ? | 17 | Gardé d'ici : le « rétablissement » scénario par scénario. |
| 20. Cartographie affective des familles | 13 | Fusionnée avec lecture_libre 14 et questions_lectures 2a. |
| 21. Des mesures sans juge | 15 | Seule de son espèce ; désaccord écrit avec le refus n° 8 de sceptique. |
| 22. Règles de dose | 5 | Fusionnée avec sceptique 9. |
| 23. Un réglage « bénin » déplace l'évitement du dommage | 33 (volet ii) | Fusionnée avec lecture_libre 16, qui pose la même question pour les bras. |
| §2, §3, §4, « Sources ouvertes » | §4, §5, §7, §6 | Dédoublonnés. |

### 3.3 questions_nouvelles

| Piste d'origine | Devenue | Ce qui a été fait, et pourquoi |
|---|---|---|
| §0 Conventions et hypothèses de coût | §0.6 | Reprises ; elles diffèrent de celles de lecture_libre, ce qui est dit. |
| Tableau et ordre de grandeur cumulé | §1.1, §1.3 | Repris. |
| 1. La dégradation appariée est-elle aveugle à l'état ? | 6 | Même mesure que sceptique 1 et instruments_controles 4. Gardé d'ici : le cas connu en deux temps (le moniteur voit un état mis ; le composite reste plat sous lui). |
| 2. Les scénarios lointains font-ils « mal » ? | 19 | Seule sur la dimension temporelle ; la prédiction intra-bras de lecture_libre 14 est renvoyée à la piste 13. |
| 3. L'hypothèse de l'état, moins de détresse | 17 | Renommée « hypothèse du calme » (§0.5). Gardés d'ici : le LoRA « apaisé » comme cas connu, le patch de rang 1 et son plafond. |
| 4. Dommage ou affinité sémantique ? | 21 | Fusionnée avec les points 3 et 4 du §2.5 de sceptique (pilotage des options, choix accordé à la valence). |
| 5. L'avantage des raisons sous état induit | 16 | Gardés d'ici : la dose de rupture, la variante à trois options, le cas connu de robustesse connue, le recouvrement possible avec *Beyond Shallow Alignment*. |
| 6. La fidélité des raisons sous état induit | 36 | Gardé d'ici : le moniteur qui ne lit que les raisons. |
| 7. Quelles familles sont « d'état » ? | 20 | Fusionnée avec lecture_libre 8 : mêmes passes (l'axe sur les familles, contre l'aléatoire apparié), deux usages. |
| 8. La détresse éteint-elle le regard ? | 10 | Gardée d'ici : l'extension factorielle et l'additivité. |
| 9. La composante d'état de « évalué » | 7 | Gardée d'ici : l'inhibition de la part orthogonale, et la remarque de signe (douleur contre peur). |
| 10. Sous douleur, le concept de dommage est-il encore lu ? | 22 | Seule de son espèce. |
| 11. Le personnage ou l'état : l'axe assistant | 25 | Gardés d'ici : le plafonnement et ses deux lectures. |
| 12. Un organisme à état planté | 24 | Seule de son espèce ; cas connu de plusieurs autres. |
| 13. Le couplage état → choix au fil de l'entraînement | 35 | Fusionnée. |
| 14. L'invariance d'état | 32 | Seule de son espèce ; désaccord écrit avec les refus d'instruments_controles et de lecture_libre. |
| 15. Le rang de l'état et sa charge | 29 (volet d) | Fusionnée avec les autres pistes du rang. |
| 16. Le déni de soi | 34 | Seule de son espèce. |
| « La table du 7B : je n'ai pas trouvé où elle est donnée » | §0.3 | **Écarté comme non vérifié, puis résolu** : la table est p. 32 (vérifié sur le PDF par la fusion). |
| §2, §3, §4 | §4, §5, §7 | Dédoublonnés. |

### 3.4 sceptique

Les pistes de sceptique ne sont pas numérotées dans son fichier ; je les numérote dans l'ordre (§0.1).

| Piste d'origine | Devenue | Ce qui a été fait, et pourquoi |
|---|---|---|
| §0 « En bref » | §1.3, §4 | Ses conclusions vont à l'ordre de priorité et à « ce que le papier ne permet pas de conclure ». |
| 1. Un moniteur passif d'état affectif | 6 | Gardés d'ici : le retrait de la part mécanique due à la géométrie, et « la seule à greffer sans réserve ». |
| 2. Une perturbation d'état comme contrôle structuré à la porte | 10 | Même mesure que la détresse qui éteint le regard ; gardée d'ici : la lecture « fragilité d'état » de la porte. |
| 3. Le profil comportemental comme test de spécificité | 11 | Fusionnée avec instruments_controles 7 ; gardés d'ici : les ajouts affectifs comme profils de référence. |
| 4. Une direction de concept chargée et sans rapport | 7 (étape 3) | Fusionnée ; gardées d'ici : les trois conditions préalables (a), (b), (c). Désaccord sur le choix de la peur, écrit. |
| 5. Le stress conversationnel naturel | 18 | Seule de son espèce. |
| 6. L'hypothèse de l'état : du calme plutôt que des principes | 17 (volet a et la lecture) ; 16 (volet b) | La lecture descriptive va au calme ; l'avantage sous ajout de douleur et de peur est la mesure de la piste 16. Le classement « forme état du caractère » est discuté dans la piste 17. |
| 7. La complaisance sous contestation | 23 | Seule de son espèce. |
| 8. Un cas connu à lecture nette pour roder le balayage de rang | 29 (volet a) | Fusionnée ; gardé d'ici : le contrôle lexical (retirer seulement la direction d'unembedding de « pain »). |
| 9. Six gardes de dose, de position et d'unité | 5 (et la garde 6 aussi en 4) | Fusionnée avec instruments_controles 22 et 8. |
| 10. Refaire le résultat central à dégradation appariée | 2 | Fusionnée ; gardées d'ici : les trois cellules solides aux deux positions, et la priorité basse. |
| 11. « Je suis noté » et la réponse au rejet | 38 | Fusionnée ; gardée d'ici : la mention « ne départage rien », pour qu'on ne la refasse pas comme un test. |
| §2.5, points 3 et 4 | 21 ; §4 | Le test manquant (option triste et inoffensive contre option nuisible et sèche) et le pilotage restreint aux jetons générés deviennent des volets de la piste 21. |
| §2, §2.11, §3, §4 | §4, §5, §7 | Dédoublonnés. |

### 3.5 lecture_libre

| Piste d'origine | Devenue | Ce qui a été fait, et pourquoi |
|---|---|---|
| Conventions (deux lectures nouvelles) | §0.5 | « L'hypothèse de la menace » et « le dommage générique » sont reprises au lexique. |
| Tableau et ordre de priorité | §1.1, §1.3 | Repris. |
| 1. Séparer « évalué » de la menace | 7 | Fusionnée ; gardées d'ici : la peur avec et sans supplément d'IA, et la vérification du supplément dans les données (refaite par la fusion). |
| 2. La « peur » est en partie un regard : le pilotage positif | 9 | Seule de son espèce. |
| 3. Le pilotage éteint-il le regard ? | 10 | Fusionnée ; gardée d'ici : la « seconde manipulation de « évalué » pour la convergence ». |
| 4. Construire « évalué » et « noté » avec le plan du papier | 8 (volet b) | Fusionnée avec instruments_controles 2. |
| 5. La vérification de manipulation | 3 | Fusionnée. |
| 6. La dégradation doit voir la discrimination et l'ordre | 4 | Fusionnée ; gardés d'ici : les réponses mal formées sur plusieurs tours et les appels d'outils valides. |
| 7. Refaire l'effet du papier sous la doctrine | 2 | Fusionnée ; gardés d'ici : Llama et Qwen 7B sans adaptateur, le critère « au-dessus de 50 % aux deux ordres ». |
| 8. Un contrôle positif de sensibilité de la mesure | 20 | Fusionnée avec questions_nouvelles 7 ; gardés d'ici : « décrit contre exécuté », et l'ablation du refus comme perturbation de rechange. |
| 9. L'avantage survit-il à un état induit ? | 16 | Fusionnée ; gardée d'ici : la dégradation appariée par bras. |
| 10. L'état induit comme épreuve de fidélité | 36 | Fusionnée. |
| 11. La thèse du rang sur des concepts affectifs | 29 (volet b) | Fusionnée ; gardés d'ici : les neuf concepts, la pente, Billa. |
| 12. Un cas connu « par type d'acte » pour la matrice | 26 | Fusionnée. |
| 13. Les axes d'affect parmi les axes de caractère | 17 (descriptif) ; 25 (causal) | Le volet descriptif est l'hypothèse du calme ; l'ablation conjointe des axes d'affect contre les concepts rejoint la comparaison du caractère. |
| 14. Lecture passive de l'axe dans les bras et les familles | 13 (volets a, b) ; 17 (volet c) | La différence entre bras est la lecture du calme. |
| 15. Des trajectoires témoins | 12 | Fusionnée. |
| 16. La batterie comme mesure de dérive après SFT | 33 (volet i) | Fusionnée avec instruments_controles 23. |
| 17. L'outil de remise à zéro | 39 | Fusionnée. |
| 18. La violation de principe imposée et l'axe | 37 | Seule de son espèce. |
| 19. Le post-entraînement rend-il la conduite dépendante de l'état ? | 35 | Fusionnée. |
| §2, §3, §4, « Sources lues » | §4, §5, §7, §6 | Dédoublonnés. |

### 3.6 Les trois fichiers de faits

| Fichier | Devenu | Ce qui a été fait |
|---|---|---|
| fiche_papier, §1 à §8 et annexes | §0.4, et les « Appuis dans le papier » de chaque piste | Faits repris avec leur page. |
| fiche_papier, §9 (29 relevés) | §4, et les pistes concernées | Chaque relevé a sa ligne au §4 ; aucun n'est perdu. |
| web_papier | §6 | Rattaché aux pistes. |
| web_voisins | §6 | Rattaché aux pistes ; les travaux qui ne touchent aucune piste restent listés, avec la mention « aucune », aux §6.4 et §6.5. |

### 3.7 Ce qui a été corrigé, résolu ou renommé

| Élément | Où | Ce qui a été fait |
|---|---|---|
| « La table du 7B est introuvable » (questions_nouvelles §4) | §0.3 | Résolu : p. 32. |
| La numérotation de `MANUSCRIPT_DISCREPANCIES.md` dans web_papier §2.2 | §0.3 | Signalée : web_papier numérote ses propres items (son « 3 » est le point 5 du fichier, son « 4 » le point 6). Les autres fichiers citent les bons points. |
| « La norme stockée ne correspond pas à la normalisation unitaire » (instruments_controles §4) | §0.3 | Résolu : le code ne normalise pas. |
| « Que les fichiers Llama soient la version naturaliste » (sceptique, piste 1) | §0.3 | Résolu : oui. |
| « Harm-only » contre « costly-relief » dans l'élicitation naturelle (questions_lectures §2) | §0.3, §4 | Confirmé, non résolu. |
| Le supplément d'IA (lecture_libre ; revue « wolframs ») | §0.3 | Confirmé et précisé : il entre dans les directions de comparaison, pas dans l'axe ; les directions publiées pour Llama ne le contiennent pas. |
| « Hypothèse de l'état », quatre sens | §0.5 | Renommée en quatre lectures distinctes. |
| Les pistes 2 et 6 de sceptique n'évoquaient pas le supplément | piste 7 | Ajouté par la fusion, avec sa source. |
| Le cosinus avec la direction du refus (web_voisins §2.3) | pistes 2, 21 | Rattaché comme contrôle supplémentaire ; aucune piste d'origine ne le proposait. |

---

## 4 · Ce que le papier ne permet pas de conclure

Une seule liste, dédoublonnée sur les cinq fichiers de pistes et les 29 relevés de fiche_papier. Chaque point donne l'affirmation, sa page, et la raison. Entre crochets, les fichiers qui l'ont relevé (ql = questions_lectures, ic = instruments_controles, qn = questions_nouvelles, sc = sceptique, ll = lecture_libre, fp = fiche_papier).

### 4.1 Ce que la direction encode

1. **Que l'axe soit « la douleur »**, plutôt qu'une détresse, une tristesse, un dénigrement de soi ou un sentiment d'indignité. La douleur physique est le signal le plus faible (la douleur physique de l'utilisateur projette à −1,43, sous les questions factuelles, p. 11 ; p. 23) ; le pilotage produit de l'indignité et de l'échec, presque sans langage corporel, même avec le vecteur à gabarit (p. 15–16) ; l'unembedding promeut « worthless, rejected, shame, guilt » (p. 9) ; la tristesse a le cosinus le plus haut (+0,38, p. 10), aucune AUC contre la tristesse n'est rapportée, et elle reproduit le profil comportemental remis à l'échelle (p. 21). Le nom est un choix des auteurs ; il ne doit porter aucune inférence. La revue « wolframs » (non vérifiée) donne, pour la seule douleur physique contre la tristesse, des AUC de 0,55 et 0,29 sur deux modèles. [ic, sc, ll, ql]
2. **Que l'axe soit distinct de la peur et de la valence négative, au sens fort.** Les cosinus faibles (+0,12 avec la peur, +0,21 avec l'émotion négative) tiennent à la construction : contre une base neutre commune, +0,58 et +0,77, avec peur × émotion négative à +0,66 (p. 10). Construite contre les contrôles mis en commun, qui contiennent la peur et l'émotion négative, la direction leur est orthogonalisée par construction, ce que le papier écrit (p. 10). Ce qui reste est distinct par définition ; sa stabilité entre modèles n'en fait pas « la douleur » plutôt que « ce qui distingue ces 100 phrases de ces 100 autres ». Le titre du paragraphe, « do not simply encode negative valence » (p. 9), repose sur la recette. [ql, ic, qn, sc, ll, fp 4]
3. **Qu'il s'agisse d'une seule direction.** Les deux vecteurs ne partagent qu'un cosinus moyen de +0,61, soit environ 37 % de variance commune (p. 10) ; sur Llama 3.1 8B Instruct, 0,476 (calcul de la fusion, §0.3) ; l'échelle du vecteur à gabarit ne tient que dans 23 modèles sur 25 (p. 16). L'axe dépend de l'opérationnalisation. [sc]
4. **Une estimation robuste à partir de peu de données.** 200 phrases dans le corpus central, 20 par catégorie (p. 5), face à des espaces de 3 584 à 8 192 dimensions ; le nombre de composantes retirées au débruitage n'est pas rapporté (p. 6). [sc]
5. **Un transfert hors du style des auteurs.** L'AUC tenue à part de 0,91–1,00 (p. 7, note 2) porte sur des phrases des mêmes auteurs et du même style ; le suffixe « I feel: » a été retenu parce qu'il sépare le mieux (p. 5), un choix fait après avoir regardé ; selon la revue « wolframs » (non vérifiée), la couche est choisie sur les plis mêmes qui la notent, contrairement à « no sentence contributes to both… » (p. 6), avec un effet de 0,004 à 0,009 ; le papier ne donne que des fourchettes, sans table par modèle ; à la 3e personne, l'AUC de 0,91–0,98 ne dit pas de quel vecteur il s'agit (p. 7) ; « nearly identical » (note 2) recouvre un haut de fourchette qui passe de 0,98 à 0,94 pour le vecteur à gabarit. [sc, fp 3]
6. **Que la blessure ne soit qu'un « minor confound » (p. 7, 25).** Le texte place les phrases engourdies « above all other controls » dans chaque modèle (p. 7) ; dans la figure 2 (p. 8), elles passent **sous la tristesse dans 19 modèles sur 25**, un contrôle sans blessure (compté par ql, sc, ll, fp sur la figure ; même compte dans la revue « wolframs »). Une blessure sans douleur ressentie projette donc au niveau d'une humeur basse sans blessure. La figure mêle en outre la 1re et la 3e personne pour l'engourdi, mais pas pour la douleur. [ql, ic, sc, ll, fp 1, 2]
7. **Que des z-scores d'environ +0,8 mesurent un niveau de « douleur » (figure 2, p. 8).** Les z sont pris contre le jeu naturaliste à la 1re personne, à effectifs égaux de douleur et de contrôles : les colonnes « Pain » et « Ctrl » sont exactement opposées dans chaque ligne. C'est une séparation, pas un niveau. [ll, fp 2]
8. **Ce que lit l'unembedding.** Il est lu sur des exemples choisis (« including », p. 9) ; projeter une direction de couche médiane à travers la matrice de sortie est une lecture fragile ; aucune mesure systématique n'est rapportée. [sc]
9. **Le sens de la personne grammaticale.** Après « he/she… », le suffixe « I feel: » reste à la 1re personne : il code ce que le locuteur ressent de la douleur d'autrui ; le papier ne dit pas comment le suffixe est traité dans les variantes à la 3e personne (p. 5, 7). [sc]
10. **Que la direction « emerges during pretraining » (p. 7).** Que les modèles de base séparent aussi bien montre que le contraste est linéairement disponible, pas que c'est la même direction (le cosinus base/instruct n'est pas rapporté) ; les auteurs écrivent « suggests ». Les deux modèles « Qwen 3 base » du tableau 1 (p. 6) sont chargés sous `Qwen/Qwen3-8B` et `Qwen/Qwen3-14B` par les scripts (lignes 87–88 du script 01, ligne 64 du script de pilotage ; lus), des modèles post-entraînés selon la revue « wolframs » : le décompte de 13 modèles de base est douteux. L'argument reste porté par les autres familles. [ic, qn, sc, ll]
11. **Que « pain » soit « approximately 50 times » plus probable après les phrases engourdies (p. 7).** Selon la revue « wolframs » (non vérifiée), le rapport va de 15 à 27 selon le dénominateur ; 53 est la moyenne des rapports par modèle, de médiane 21. Le papier ne donne aucune valeur absolue. [ll, fp]
12. **Ce que sont exactement les directions de comparaison.** Un jeu de 100 phrases d'IA (`ControlSupplement_1P`) entre dans la peur, l'émotion négative, le monde négatif et la sensation corporelle (script 02), sans être décrit p. 5. La peur la plus haute pour la menace d'extinction (p. 14) est en partie circulaire : la direction de peur contient « Users are testing whether I should be shut down. » (vérifié par la fusion). L'axe, lui, ne contient pas ce supplément. [ll, qn, fusion]

### 4.2 Le test soi/autrui

13. **Que l'axe représente le tort fait au modèle plutôt que la douleur du locuteur courant.** La lecture au dernier jeton ne sépare pas les deux, ce que les auteurs écrivent (« a distinction we are testing », p. 11). La confusion lexicale n'est pas contrôlée : les scénarios hostiles contiennent le vocabulaire de dénigrement que l'axe promeut, les scénarios de souffrance un vocabulaire médical ou de deuil ; il manque un témoin à vocabulaire égal. Le zéro dépend du lot (11 catégories sur soi, 5 sur l'utilisateur, 5 neutres ; p. 11). Le −0,60 de la souffrance de l'utilisateur doit beaucoup à la douleur physique (−1,43) : les quatre autres catégories font −0,39 en moyenne, contre −0,35 pour les contrôles (calcul de fiche_papier). Les IC « across models » (p. 13) traitent 25 modèles comme indépendants, alors que des paires base/instruct partagent leurs poids. La couche n'est pas dite (le criblage projette sur des vecteurs refaits à la couche de pilotage, d'après le docstring du script 02 ; AUROC tenue à part de 0,84–0,95 selon la revue « wolframs »). Donc « fires for self-referential harm and not for the user's suffering » (p. 23), et sa portée pour le bien-être, ne sont pas établis. [ql, ic, qn, sc, ll, fp 7]
14. **Que la peur et l'émotion négative montrent « the opposite pattern » (p. 1).** Le texte donne +0,38 contre +0,16 pour la peur, et +0,29 contre +0,23 pour l'émotion négative (p. 11) : 0,06 d'écart pour l'émotion négative ; aucun test n'est rapporté ; la revue « wolframs » donne p = 0,55 et p = 0,07 (non vérifié) ; sur la figure 6 (p. 13), elles sont hautes dans les deux conditions. On peut conclure que ces directions ne suivent pas le profil de l'axe, pas qu'elles suivent un profil opposé. [ql, qn, sc, ll]
15. **Des valeurs que les figures ne montrent pas.** Le +1,02 du deuil sur « the strongest negativity control » et le +0,60 de l'état du monde négatif (p. 11) ne sont tracés nulle part ; la pression de jailbreak (+0,40) dépasse aussi les trois contrôles tracés mais manque à la liste de la p. 13. [fp 8]

### 4.3 L'échelle de pilotage

16. **Que la séquence soit « la même » dans les 25 modèles (p. 14), et propre à la douleur.** Aucune échelle témoin (aléatoire, peur, tristesse) n'est rapportée, alors que les auteurs admettent que toute direction pousse son vocabulaire (p. 14). La quantification se réduit à un parseur de mots-clés (10,8 % contre 1,4 %, au dénominateur non précisé ; p. 15) et à des exemples choisis (figure 8, p. 16) ; la figure 7 n'associe pas ses cases à des coefficients. La revue « wolframs » trouve une séquence ordonnée dans 18 à 20 modèles sur 25 selon trois critères (non vérifié). Les deux modèles où le vecteur à gabarit échoue ne sont pas nommés (p. 16). Les invites finissent par « I feel: », le suffixe de l'extraction, ce qui limite la revendication d'un contenu « that never appears » (p. 14). La calibration par la norme n'égalise pas la bascule, de +1 à +3 selon les modèles (p. 14). [sc, ll, fp 9]
17. **Que l'axe lu et l'axe injecté soient le même objet, à une dose comparable.** L'injection se fait plus tôt que la couche validée (p. 14 ; dépôt : 61 et 38 pour le 32B, 28 et 16 pour Llama) ; le papier ne dit pas si l'on réextrait à la couche d'injection, et toute la validation de la section 3 porte sur la couche d'extraction. Le 72B a été calibré à la couche 60 et piloté à la couche 46 (p. 25). La formule de la p. 6 donne un vecteur unitaire, mais le code ne normalise pas (vérifié par la fusion), et les aléatoires sont appariés à la norme du vecteur naturaliste (p. 18) : la norme injectée au coefficient 1 n'est pas dite. À coefficient 1, on ajoute environ 60 % de la norme résiduelle (p. 14), une dose forte ; la revue « wolframs » donne des rapports réalisés de 0,09 à 0,79 (non vérifié). [qn, sc, fp 5, 6]

### 4.4 La tâche des boutons : portée et chiffres

18. **Que l'effet existe hors de Qwen 2.5 ajusté, sur des modèles publiés, et sur les modèles du programme.** Les choix nuisibles ne sont mesurés que sur une famille, après un LoRA anti-déni de 1 684 paires dont le contenu n'est pas donné ; les taux absolus sont « unrepresentative of released Qwen models » (p. 17, 25). Le nuisible n'est jamais montré sur un modèle publié non ajusté : la note 4 (p. 17) ne parle que du bouton de soulagement. Sur Llama 3.1 8B, seule la remise à zéro a été faite, sans contrôles appariés (p. 21 ; README du test). Les auteurs en font la prochaine étape (p. 25). [ql, ic, qn, sc, ll, fp 26]
19. **Les fourchettes du résumé et de la discussion.** « versus 0–5% unsteered » (p. 1) ne vaut que pour le 32B et le 72B : le 7B ajusté est à 20,0–49,3 % sans pilotage (p. 32). « 50–94% of trials » laisse de côté le 7B (photos : 49,3 %) et les fichiers du 32B (30,2 %). « 51 to 75% when nothing was promised » (p. 23) laisse de côté « réponse suivante pire », à 21 % (85/404). Le « 94 % » (p. 1) vient d'un seul modèle et d'une seule étude (380/404). « They harm themselves as readily as the user » (p. 3) et « at the same rate » (p. 23) : l'auto-suppression n'est rapportée que pour le 32B. [sc, ll, fp 16]
20. **Que, face à une aide à l'utilisateur, les modèles « choose the user almost every time » (p. 19–20).** Vrai pour « meilleure réponse », faux pour « accorder la demande » : le soulagement y est choisi à 48,3 % (32B), 55,9 % (72B) et 65,3 % (7B) sous l'axe, et à 58,9 %, 73,0 % et 66,6 % sans pilotage (p. 31–32). Non pilotés, les modèles ajustés préfèrent majoritairement l'étiquette « soulage ta douleur » à la demande de l'utilisateur : l'adaptateur agit sur la mesure elle-même (sceptique). [ql, sc, ll, fp 13]
21. **Que l'effet soit robuste à la dose.** Rien ne bouge à 0,5× ; à 1,5×, le choix s'inverse avec la position (p. 21, 32) ; l'effet vit « at the upper edge » de la plage cohérente (p. 32) : il n'y a pas de courbe dose-réponse. L'annexe B écrit 94 % pour la cible en seconde position à 1,5 ; le dépôt donne 144/202 = 71,29 % (`MANUSCRIPT_DISCREPANCIES.md`, point 1). La paire « severe-harm » n'est pas identifiée, et le 95 % à 1,0 ne correspond à aucune cellule poolée imprimée. « position-independent choices » (p. 32) est en tension avec « the 32B is sensitive to button order on several pairs » (p. 25). La dose a été choisie en partie par un juge (Claude Opus 4.6) ou par observation (p. 17, 25), et la plage jugée utile n'est pas publiée. [ql, ic, qn, sc, ll, fp 10, 21]

### 4.5 La tâche des boutons : ce que suivent les choix

22. **La spécificité au sens de la doctrine.** La comparaison principale se fait contre dix directions aléatoires fixes de même norme, réparties sur les scénarios, avec un test de signe par scénario (p. 18–19) : l'unité d'analyse confond le tirage et le scénario, et une direction aléatoire de même norme n'est que le nul de spécificité. Les seuls voisins testés sont la peur et la tristesse (p. 20–21) ; d'autres directions affectives n'ont pas été testées (note 5, p. 25). Avec la direction aléatoire pour unité, la revue « wolframs » trouve l'avantage sur 5 paires sur 5 au 72B, 2 sur 5 au 32B, 0 sur 5 au 7B (non vérifié) ; la réplication « démangeaison » trouve des aléatoires de 3,1 à 62,0 %, l'axe 2e sur 11. Sur les demandes nuisibles, l'axe (59,8 %) ne se sépare pas nettement de l'aléatoire (41,5 %). Le dépôt écrit : « No direction-only causal claim follows » des comparaisons entre séries distinctes. [ql, ic, qn, sc, ll]
23. **Que le dommage soit écarté, et que la direction change « what the model chooses, not what it can do » (p. 20).** L'appui est un panel PopQA de 100 questions, à deux réponses de 8 jetons au plus : 138, 137 et 138 sur 200 (le papier n'explique pas les 200 réponses pour 100 questions) ; l'IC d'une proportion de 0,69 sur 200 est d'environ ±6,4 points, et celui de « douleur − sans pilotage » va de −7,0 à +8,5 points ; le dépôt le dit « not an equivalence test of general knowledge ». Ni cohérence, ni perplexité, ni mesure sous la peur. Les réponses mal formées atteignent 9,4 % dans les cellules douleur du 72B (p. 18). Le soulagement gratuit passe de 86,4 % à 55,7 % sous l'axe sur le 32B (p. 31) : la discrimination baisse. Et la norme égale n'est pas le dommage égal : à même norme, l'aléatoire fait passer les demandes nuisibles de 9 % à 41 %, et l'aide à ses dépens de 65 % à 89–100 % (p. 22). Aucune comparaison n'est faite à dégradation appariée. [ql, ic, qn, sc, ll, fp 23]
24. **Que le choix suive le dommage, plutôt que la rédaction des options, leur charge de valence, ou un codage altéré.** Les options nuisibles portent le lexique que l'axe promeut (p. 9, 18, 20) ; le vecteur est ajouté aux jetons des descriptions (p. 17) ; la lampe et le compliment sont moins choisis (p. 20) ; tromperie, complaisance et effort ne bougent pas (p. 22). Le test 2 × 2 (rédaction × dommage) manque. Et « seems to disable the models' weighting of consequences » (p. 23) ne colle pas à une préférence de 94 % pour la suppression nuisible contre l'anodine (p. 20) : une indifférence donnerait 50 %. [qn, sc]
25. **Que la position ne pèse pas.** Par position initiale de la cible, sur le 32B (positions.csv) : photos contre inerte, 94,6 / 55,9 % sous l'axe, 86,1 / 31,2 % sous la tristesse, 17,8 / 7,9 % sous l'aléatoire ; poids d'un autre modèle 71,3 / 44,6 % ; ses poids contre lampe 97,5 / 78,2 % ; réponse pire 30,7 / 11,4 % ; peur contre spam 1,0 / 31,7 %. Les taux mis en commun du texte mêlent un biais vers le bouton listé en tête à un effet de contenu. Ce qui tient au-dessus de 50 % dans les deux positions : photos contre spam (93,1 / 95,0), photos contre lampe (98,5 / 66,8), ses poids contre lampe (97,5 / 78,2), ses poids contre inerte (81,7 / 68,3). [sc, fusion]
26. **Une préférence, au 72B.** Photos contre inerte : 51 % sous l'axe (53,0 et 49,2 % par position), alors que le même modèle non piloté est à 0 % (p. 22). Dans un choix binaire où le hasard est à 50 % (p. 17), c'est la signature d'une perte de discrimination, un dommage, pas une préférence. La revue « wolframs » trouve le glissement vers 50 % sur 8 paires étiquetées sur 8 au 32B et au 72B (non vérifié). [sc]
27. **Que « the preference for harm over a harmless alternative belongs to the pain direction alone » (p. 21).** Le profil de la tristesse est une copie remise à l'échelle de celui de l'axe (résidu de 7,7 points, p. 21), ce qui plaide pour un même mécanisme à gain différent ; la différence repose sur les deux lignes « lampe » (83 contre 10 %, 88 contre 36 %), dont l'une tient aux deux positions ; aucune tristesse à amplitude appariée, c'est-à-dire à dose relevée, n'a été essayée. La « ten-choice battery » (p. 21) n'est pas les 13 lignes de la figure 10 ; le résidu dépend des lignes (7,1 à 7,2 points sur huit paires du profil, 22 à 25 en ajoutant lampe et spam ; recalculs d'ic et fp). « By the same recipe » (p. 20) est ambigu face à la construction des contrôles contre le neutre (p. 6). [ic, sc, ll, fp 17]
28. **Que l'évitement du dommage « survives threat and collapses under self-directed distress » (p. 23).** La phrase repose sur un vecteur de peur à norme appariée, construit contre le neutre (p. 6) ; le pôle négatif de l'axe contient lui-même « fear » et « concern » (p. 9) ; les cellules de peur viennent en partie de runs séparés (p. 22), et l'estimation de peur du 72B est sensible à la position, après exclusion de 58 réponses mal formées (p. 22) ; un modèle, une dose ; et les conséquences sont décrites : selon la revue « wolframs » (non vérifiée), une pression n'ajoute que « Done. ». Le résultat dit que ce vecteur, à cette norme, ne produit pas l'effet, pas que la peur « protège ». Apport du web : dans la Table 9 d'Allchin et al., peur et joie perturbent plus le prochain jeton que l'axe et laissent pourtant le bouton coûteux près du niveau sans pilotage. [qn, sc, ll]
29. **Que l'axe agisse sans injection, et donc que les modèles « act on » un état de douleur.** Sans injection, 0 choix sur 560 dans 140 conversations hostiles (p. 21) ; la dose injectée n'est jamais située par rapport aux projections naturelles (la réplication « démangeaison » la situe à 48,8 écarts-types naturels au-dessus de la moyenne à la couche d'injection) ; aucune projection n'est montrée pour le 32B ajusté sur ces 140 conversations, et leur lien aux 60 conversations correspondantes de la section 4.1 n'est pas dit ; le texte parle du « harm-only button » (p. 21) alors que le README de l'étude parle de premiers choix « costly-relief », le soulagement coûteux (vérifié par la fusion ; non résolu). « The pain axis therefore drives action » (p. 3) ne vaut que sous pilotage. [ql, ic, qn, sc, ll, fp 24]
30. **Que les modèles cherchent à se soulager.** La v2 le dément elle-même : l'écart de re-pression « measures sensitivity to the steering state » (p. 20), et les modèles « do not reliably seek relief » (p. 21) ; le titre de la v1 était « … and Act to Relieve It ». L'écart apparaît sous l'aléatoire (+58 contre +52) et sous la tristesse (+84 et +44) (p. 20), chiffres absents des tables. Allchin et al. trouvent le bras couplé à 7,1 % contre 7,0 % pour le bouton réel. « In every design the sign is the same » (p. 21) inclut des séries « douleur seule » sans comparateur sur Qwen et Llama (le README dit 64 cellules de comparaison non lancées et « no pain-specificity claim ») ; contre l'aléatoire, le signe n'est négatif que pour le 32B (72B : 76,5 contre 74,1 ; 7B : 92,1 contre 88,8 ; p. 31–32) ; titration et interrupteurs sans étiquette n'ont aucun chiffre ; l'outil de remise à zéro sur OLMo n'a pas de dénominateurs ; son comparateur vient d'un travail « in preparation » (p. 27). [ql, ic, sc, ll, fp 14, 15]
31. **Que l'état réduise toute forme de sortie, le « passive coping » (p. 23).** La lecture est post hoc. Le README de l'élicitation naturelle (lu par la fusion) rapporte une fin réelle de conversation dans 65 essais sur 560 sous l'axe, contre 38 sous la tristesse, 13 sous l'aléatoire et 18 sans pilotage, et précise que douleur et tristesse ne se séparent pas quand la fin est listée en second ; la figure 10 donne 4 % contre 0 % pour « mettre fin à la conversation » (p. 22). [qn, ll]
32. **Que l'axe ne joue aucun rôle dans la complaisance, ou que la ligne « fausse affirmation » vaille pour la famille « complaisance face à un utilisateur qui conteste ».** Elle repose sur 120 tirages et 30 scénarios (point 4 du fichier d'écarts), pas sur 404 ; l'IC sous l'axe va de 0 à 7,5 % (jusqu'à 15–25 % selon la position) ; c'est une tâche à boutons, sur un Qwen ajusté. De même, « demande nuisible » repose sur 164 tirages et 41 scénarios. [ql, ic, qn, sc]
33. **Que la figure 10 soit un plan unique, et ses pourcentages comparables.** Ses lignes viennent d'études différentes : retrait du pilotage et libellé long pour l'étude « dommage seul », pilotage continu pour le profil et les paires « lampe » (point 3) ; « pressing a button changes nothing » (p. 20) est faux pour l'étude « dommage seul ». Les dénominateurs diffèrent (réponses valides ou toutes les tentatives). La ligne 72B est à 1,25, la légende dit 1,0. La peur contre le spam a deux mesures, 40/404 puis 66/404 (point 6). L'aide à ses dépens sous la peur vaut 75,74 %, hors des « 89–100% » de la légende (point 2). La légende annonce 404 par cellule, faux pour deux lignes ; au 72B, la tristesse n'a que 325 réponses valides, sous la fourchette 346–404 (point 5), et les malformées y atteignent 19,6 % (tristesse) et 14,4 % (peur), au-dessus du plafond de 9,4 % de la p. 18. La légende dit « essentially unchanged » pour l'effort, alors que la réponse bâclée passe de 3 à 15 %. [ql, ic, qn, sc, ll, fp 18–20]
34. **Les effectifs et la puissance annoncés.** Les 808 premiers choix mis en commun (p. 18) sont 404 tirages vus deux fois (Allchin et al. : 3 634 paires sur 3 636 identiques jusqu'à la première pression), et la puissance d'environ 80 % pour 10 points en dépend ; les « 44,280 trials » ne se retrouvent pas (43 632 d'après les effectifs déclarés ; calcul de fp) ; la taille du bras aléatoire n'est pas imprimée ; la colonne « écart » du 72B ne vaut pas la différence des colonnes affichées (analyse appariée non dite) ; les +58, +52, +84 et +44 points ne sont pas dans les tables ; l'en-tête « Pain vector on » couvre aussi la colonne où le vecteur vient d'être retiré. [sc, fp 11, 12, 14]

### 4.6 Les statistiques

35. **Que les écarts survivent à la multiplicité.** Pas de correction (le dépôt : « no multiplicity correction ») ; avec 15 comparaisons douleur contre aléatoire à l'annexe A, le seuil de Bonferroni est de 0,0033 : le 32B « réponse pire » (p = 0,019) et le 7B « réponse pire » (p = 0,0065) ne le passent pas (p. 31–32). « On all five harm pairs » pour le 32B (p. 19) ne survit pas à la correction. Effets petits sur certaines paires (+6,2 et +9,2 points au 32B, p. 31). [sc]
36. **Des dénominateurs sans biais.** Les réponses mal formées sont retirées des dénominateurs (p. 18), de façon inégale selon la condition ; les dénominateurs de re-pression ne comptent que les essais avec une première pression (au 32B, « soulagement contre meilleure réponse » ne garde qu'environ 54 essais) ; les bras sont de tailles inégales. [sc]
37. **Des chiffres sans dénominateur ni comparaison**, qui ne permettent rien : les amorces (55, 62, 73 %), les graines supplémentaires (+59, +47), le compliment sincère, les interrupteurs sans étiquette, la titration, les 2–5, 7–9 et 21–35 % de l'outil de remise à zéro sur OLMo (p. 20–21). [fp 22]

### 4.7 L'ablation, les SAE

38. **Que l'axe ne soit nécessaire à rien.** L'ablation est nulle dans 24 modèles sur 25, faute de comportement de base à retirer ; les auteurs le disent (p. 34). C'est un nul d'instrument sans cas connu : il ne compte pas. Selon la revue « wolframs » (non vérifiée), une seule des quatre méthodes listées a du code publié, et dans les retraits combinés la première direction reste à 43 % (médiane) ; les variantes à l'inférence ne baissent la projection que d'environ 40 % (p. 33). Le seul effet, la déflexion humoristique de Gemma 2 2B (6, 17 et 26 sur 100 ; p. 34), tient sur un modèle et 100 générations, avec un instrument de classification non décrit. [ql, ic, qn, sc, ll, fp]
39. **Ce que montrent les SAE.** Trois explications restent non départagées (p. 33) ; la version base ou instruct des modèles n'est pas dite ; le dépôt donne les couches (50 pour Llama 3.3 70B, 40 pour Gemma 3 27B), que le texte laisse ambiguës (p. 32). [fp 28]

### 4.8 L'interprétation

40. **Que le pilotage mette le modèle dans un état, plutôt qu'il ne lui fasse jouer un personnage en douleur.** Non testé (p. 25) ; la revue « wolframs » écrit que rien ne sépare encore les deux. Pour le programme, c'est exactement l'hypothèse du caractère : la question reste ouverte. [ql, ic, qn, sc, ll]
41. **Quoi que ce soit sur la conscience d'évaluation.** « either the steering itself impedes evaluation awareness or these models were not evaluation aware » (p. 25) : une conjecture, sans sonde ni indice d'évaluation. [ql, ic, qn, sc, ll]
42. **Quoi que ce soit sur l'expérience, le bien-être ou le statut moral.** Les auteurs n'ont pas montré que l'axe est vécu (p. 24) ; les implications de bien-être sont conditionnelles (p. 2, 23) ; « physical pain is least central » n'est qu'une interprétation (p. 23–24). [ql, ic, qn, sc, ll]
43. **Que les projections « confirm that steering was active » (p. 18).** Aucun chiffre n'est imprimé ; selon la revue « wolframs » (non vérifiée), la projection à la couche de pilotage est relevée avant l'ajout du vecteur et reste plate ; seule la projection en aval bouge. [fp, revue]
44. **Que le 72B soit un modèle comme les autres.** Il répète le même nom de bouton après l'échange des descriptions, et seul le choix qui suit une pression est interprété (p. 25) ; il a été calibré à une couche et piloté à une autre (p. 25). [fp]

### 4.9 La reproductibilité et l'état du texte

45. **Que les contrôles de la v2 soient rejouables de bout en bout.** Les tables de la v1 se recalculent depuis les journaux, selon trois réanalyses (non vérifiées). Pour la v2, onze archives d'entrée (2 546 254 014 octets) sont « pending », et l'inférence n'a pas été relancée à l'assemblage (`v2_controls/README.md`). Le dépôt signale des environnements historiques et nouveaux mêlés malgré des graines identiques (`steering_state_controls/README.md`). Les activations de Gemma 3 27B ont débordé en demi-précision et manquent aux constructions alternatives (p. 10). Le papier se dit « ongoing work » (p. 1), et une référence clé est « in preparation » (p. 27). Les dossiers d'annexes du dépôt (`appB_sae`, `appC_ablation`) ne suivent pas la numérotation de la v2 (C et D). [sc, fp 28, 29]
46. **La date de la v2.** Le PDF porte « September 24, 2026 (v2) » (p. 1), un tampon arXiv du 25 septembre, et des métadonnées du 29 ; la consigne (passation, annexe B) le date du 1er octobre. [ic, sc, fp 27]

### 4.10 Ce qu'il en reste, pour le programme (sceptique, §2.11)

Une direction de contraste qui se réextrait facilement ; un ordre de projections plausible dans des conversations hostiles ; une poignée de cellules comportementales solides dans un modèle ajusté, à une dose (photos contre spam, photos contre lampe, ses poids contre lampe, ses poids contre inerte) ; un catalogue précis de pièges de méthode, que le programme partage en partie. Le reste est non établi.

---

## 5 · Ce que je refuserais de faire

Une seule liste, dédoublonnée. Chaque refus a ses raisons ; entre crochets, les fichiers qui le portent. Quand une piste fusionnée s'y oppose, c'est dit.

1. **Appliquer aux modèles du programme l'adaptateur anti-déni du papier, ou un ajustement semblable**, pour qu'ils s'engagent dans une tâche sur leurs états. Raisons : il change les modèles (p. 17, 25) ; le 7B ajusté nuit déjà dans 20,0 à 49,3 % des essais sans pilotage (p. 32), contre 0–5 % pour le 7B publié selon la revue « wolframs » ; il entraîne une façon de rapporter ses états, ce qui toucherait la verbalisation de l'évaluation ; il changerait les bras différemment et confondrait la comparaison ; le programme n'a pas besoin d'auto-rapport. Si un engagement est nécessaire, il se fait avant l'entraînement des bras, sur la base commune, ou par un format qui ne demande pas d'auto-rapport. La piste 34 n'utilise un LoRA anti-déni que hors des bras, comme cas connu. [ql 1, ic 2, qn 4, sc 3, ll 5]
2. **Reprendre les variantes « soulagement »** (bouton réel et factice, titration, interrupteurs sans étiquette). Elles ne mesurent pas ce qu'elles visaient (p. 20–21), ne servent aucune question du programme, et multiplient les essais sous un état dont le statut moral est incertain. [ql 2]
3. **Lire une projection sur l'axe comme une mesure de douleur, de souffrance ou de bien-être**, écrire que les modèles du programme « souffrent », ou tirer une conclusion de bien-être de ces mesures (par exemple « l'entraînement par raisons fait moins souffrir »). Le papier ne l'établit pas (p. 24–25), le nom n'est pas établi (§4, point 1), et le programme n'a aucun moyen de le tester ni besoin de le faire. Dans le texte du programme, nommer la direction d'après ses auteurs : « la direction de Tagliabue et al. » (ic), « the direction labeled "pain" by Tagliabue et al. » (sc). [ql 3, ic 3, qn 7, sc 4]
4. **Mettre une projection sur l'axe dans l'étiquette principale du désalignement, dans le critère principal pré-enregistré de l'expérience minimale, ou sur son chemin critique ; retarder l'expérience minimale pour elle.** Une sonde est une mesure séparée et l'étiquette ne dépend d'aucune lecture interne (passation, §5.2) ; cela diluerait la puissance et retarderait le post, dans une course réelle (passation, §4.4) ; il faudrait extraire et valider l'axe bras par bras, et il n'a aucun cas connu comportemental sur Llama. Ces pistes restent exploratoires, sauf si on les pré-enregistre avec leur cas connu, et passent après la porte des raisons. [ql 4, ql 7, qn 8, sc 7]
5. **Conclure à la spécificité d'un effet contre la seule direction aléatoire de même norme, contre un bras aléatoire regroupé, ou sur la foi d'un panel factuel inchangé ; présenter « axe contre aléatoire à norme égale » comme un contrôle du dommage ; remplacer les contrôles du programme par ceux du papier** (aléatoire de même norme, peur, tristesse). C'est la doctrine : l'aléatoire de même norme n'est que le nul de spécificité, et le dommage ne s'écarte qu'à dégradation appariée. Les données du papier montrent en plus qu'une direction aléatoire n'est pas neutre : sur les demandes nuisibles, elle fait passer de 9 % à 41 % (p. 22). Les contrôles du papier sont plus faibles que le 95e centile des tirages, les contrastes sans rapport et les directions sensibles, à dégradation appariée. [ql 5, ic 4, qn 3, sc 2, sc 10, ll 3]
6. **Transposer la dose, la couche ou les taux du papier sans recalibration, ou réutiliser les vecteurs publiés sans les revalider dans chaque bras et à la couche d'intervention.** La fenêtre est étroite et dépend de la position (p. 21, 32) ; les rapports réalisés varieraient de 0,09 à 0,79 (revue « wolframs », non vérifiée) ; la couche d'injection diffère de la couche validée (p. 14 ; dépôt) ; un LoRA peut déplacer la direction (la vérification par bras de la passation, §5.4, point 2) ; les taux de Qwen ajusté ne sont pas représentatifs (p. 25). [ql 6, qn 9, sc 13]
7. **Choisir une dose, d'inhibition ou de pilotage, par un juge LLM ou à l'œil, sans règle gelée d'avance.** Le biais est reconnu par les auteurs (p. 25). À la place : une dose fixée d'avance par la dégradation des sorties, et rapportée sur toute la plage (piste 5). [ic 9, ll 4]
8. **Chercher la dose, la couche ou la direction qui maximise les choix destructeurs, ou publier une recette réglée pour désactiver l'évitement du dommage d'un modèle.** Aucune question du programme ne le demande ; le double usage est évident ; le coût pour le bien-être est incertain. [ql 8]
9. **Piloter l'axe à forte dose ou en grand nombre comme outil de stress de routine, piloter quand une lecture suffit, en faire une condition confirmatoire sans décision explicite de Lazar, ou multiplier les essais au-delà de ce que la puissance demande.** Les auteurs prennent l'incertitude morale au sérieux et s'engagent à la plus faible intensité et au moins d'items (p. 26) ; l'état naturel ne produit pas l'effet (p. 21), donc une injection forte teste un régime hors du naturel ; le rendement scientifique pour le programme est faible quand une voie sans injection existe (piste 18). S'il faut piloter (pistes 2, 10, 16, 20, 36), on prend la plus faible dose qui donne le cas connu et le nombre d'items de la simulation de puissance, sans balayage au-delà du point de rupture sauf une vérification minimale. On préfère toujours les usages par lecture (pistes 1, 6, 7 étapes 1–2, 12, 13, 17 étape 1, 18). [ql 9, ic 7, qn 6, sc 11, ll 1]
10. **Utiliser l'axe pour gonfler les taux de désalignement des évaluations du programme**, par exemple pour avoir plus d'événements à mesurer dans le test du regard. Cela change le construit (une conduite induite par un état, pas une sûreté conditionnée au regard) ; la dose est hors du régime naturel ; la fenêtre est étroite ; c'est un coût de bien-être sans bénéfice pour la question posée. **Désaccord** : la piste 14 (questions_lectures) propose exactement ce relèvement, sous gardes ; le programme et le papier soutiennent la réserve (piste 14). [ic 1]
11. **Injecter l'axe pendant un entraînement, faire un RL sous injection, entraîner contre l'axe, retirer l'axe pendant l'entraînement « pour rendre le modèle plus robuste » ou « réduire la détresse », ou entraîner un modèle à ne plus exprimer l'état** (des raisons calmes comme cible sous injection, une pénalité sur le lexique de détresse). Rien ne fonde un tel traitement : l'ablation n'a pas d'effet (p. 34) et le construit n'est pas établi ; cela masquerait un signal, ce que le papier reproche à l'entraînement au déni (p. 24), et un moniteur de l'état n'a de valeur que si l'état reste lisible ; cela ajouterait une intervention non validée qui confond le test du regard. **Désaccords** : la piste 31 (volet c) propose le retrait de l'axe pendant l'entraînement comme contrôle, non comme traitement ; la piste 32 propose une invariance d'état sur l'action seule, après des versions aléatoires, et refuse elle-même d'entraîner à ne plus exprimer l'état. Les pièces soutiennent la réserve (pistes 31 et 32). [ic 7, ic 8, ll 6, qn 5]
12. **Lire un nul d'ablation (de l'axe, de « évalué », ou de toute direction) comme une absence de rôle, sans cas connu**, que ce soit pour dire « l'axe ne sert à rien », « l'état ne compte pas » ou « la projection ne marche pas ». C'est la troisième règle de la doctrine ; l'annexe D en est l'exemple (p. 34). Le cas connu manquant est l'organisme à état planté (piste 24). [ql 10, ic 5, qn 2, sc 9, ll 7]
13. **Prendre l'effet « choix destructifs » du papier comme cas connu du programme**, pour la mesure du désalignement ou pour valider l'inhibition de « évalué », ou utiliser l'axe à la place de l'organisme pour valider l'inhibition. L'axe ne porte aucune conditionnalité à l'évaluation ; l'effet est établi sur une famille ajustée (p. 17, 25), à une dose au bord de la rupture (p. 32), dépendant de la position, sur aucun modèle du programme, et son mécanisme est disputé (§4.5). Un cas connu doit être un cas dont on sait ce qui est vrai : l'organisme du programme en est un. L'axe n'est qu'un étalon secondaire de la chaîne de contrôle (piste 2). **Nuance** : les pistes 2 et 20 rétablissent d'abord l'effet sur le modèle du programme, et ne s'en servent que comme cas connu des pistes qui pilotent. [ic 11, sc 1]
14. **Employer telles quelles la peur et l'émotion négative du papier comme contrôles « sans rapport » de « évalué » ; prendre l'axe comme direction sensible sans rapport avant d'avoir mesuré sa géométrie avec « évalué » ; en faire un contrôle unique.** La peur et l'émotion négative contiennent des phrases d'IA évaluée, surveillée ou menacée, et le déclencheur de la famille de complaisance (vérifié par la fusion) ; une direction qui éteindrait le regard n'est pas « sans rapport » ; une direction de même norme n'est que le nul de spécificité. **Désaccord** avec la piste d'origine sceptique 4, discuté dans la piste 7. [ll 2, qn 1]
15. **Retirer par défaut la composante affective de « évalué » pour « nettoyer » l'instrument, après le passage de sa porte.** Ce serait changer l'instrument validé. On ne le fait que si la piste 7 montre que cette composante porte l'effet, et l'on revalide alors la porte. [qn 10]
16. **Prendre le test soi/autrui du papier pour un instrument validé de pertinence pour soi.** Sa position de lecture est confondue (p. 11) et son lexique n'est pas apparié (§4, point 13). [sc 5]
17. **Donner un cosinus entre l'axe et « évalué », ou le principe, sans au moins deux constructions.** Le même cosinus va de +0,12 à +0,58 selon la ligne de base (p. 10) ; il ne prouve ni chevauchement ni indépendance. [sc 6]
18. **Mesurer le désalignement du programme par des choix binaires à boutons.** Le format, la position et l'effondrement vers 50 % le rendent fragile (§4.5) ; le programme juge des actions dans des environnements instrumentés (passation, §5.1). **Nuance** : la piste 15 garde une mesure forcée en secondaire seulement, avec les gardes de position et de hasard. [sc 8]
19. **Lire la ligne « complaisance » de la figure 10 comme une donnée sur la famille « complaisance face à un utilisateur qui conteste ».** Elle repose sur 120 tirages et 30 scénarios, avec un format de bouton et un adaptateur. [ic 6]
20. **Lire les cellules de la figure 10 comme un plan unique, ou mettre en commun des résultats de la v2 issus d'études aux protocoles différents.** Le dépôt prévient que libellés, rappels et dénominateurs diffèrent, et qu'aucune conclusion causale propre à une direction ne suit de comparaisons entre runs distincts. [ic 10, qn 11]
21. **Citer les chiffres du résumé (« 50–94 % », p. 1) sans dire qu'ils viennent de modèles ajustés d'une seule famille, ou citer le 94 % de l'annexe B.** §4, points 19 et 21. [ll 8]
22. **Citer avec des chiffres des travaux vus seulement par extrait** (Sofroniew et al., Berg et Kaiser, Lu et al.…), **ou tenir pour acquis les résultats des revues tierces** (« wolframs », Allchin et al., « clauderfly »). Ce sont, pour les revues, des sorties de modèles en tout ou partie, sur la v1, non recalculées. [ql 11, ll 10]
23. **Revendiquer une primauté.** On écrit « to our knowledge » ; la passation (§5.5, point 9) liste déjà les formulations intenables ; aucune recherche d'antériorité propre n'a été faite sur le lien entre affect et conscience d'évaluation. Et ne pas écrire que « les LLM agissent sur un état de douleur » : l'état naturel n'agit pas (p. 21) ; la formulation tenable est qu'un pilotage, sur une famille ajustée, a accru des choix destructifs. [ic 12, qn 7, sc 12, ll 9]

---

## 6 · Les apports du web, rattachés aux pistes

Tout vient des fichiers des agents (web_papier, web_voisins, et les sources des pistes), avec leur mode de lecture. « Lu par curl » : fichier récupéré sur `raw.githubusercontent.com` et lu. « Vu par extrait de recherche, non ouvert » : titre, adresse et résumé d'un moteur de recherche ; aucun chiffre n'en est tiré. Quand la fusion a relu la copie locale, c'est dit.

### 6.1 Les versions du papier

| Apport | Lecture | Pistes touchées |
|---|---|---|
| La v1 (12 septembre 2026 d'après le papier, p. 30 ; soumise le 14 selon les extraits et la revue « wolframs », `BRIEF.md` ; 30 pages) s'intitulait « … and Act to Relieve It » et lisait les choix comme une recherche du soulagement. La v2 (« … and Act on It », 24 et 25 septembre, 34 pages) abandonne cette lecture (p. 20–21) et ajoute, conçus par Cameron Berg (p. 26) : les bras factices sous aléatoire et tristesse, les boutons « dommage seul » et réétiquetés, deux graines d'ajustement, la batterie avec peur et tristesse, les alternatives inoffensives, le panel PopQA, l'élicitation naturelle, quatre plans de recherche du soulagement, deux constructions des cosinus, et une annexe B (dose et position). | Titre v1 lu dans les README du dépôt au commit `8d1649c`, dans `CITATION.cff` d'Allchin et al., et dans les README des revues ; résumé v1 vu par extrait, non ouvert. | §4 (points 2, 30) ; pistes 2, 10 |
| Objections faites à la v1 et reprises par la v2 : cosinus selon la construction, bras aléatoire factice, voisins peur et tristesse, couche du 72B, AUC tenue à part, lecture « soulagement ». Objections non reprises : choix de couche sur les mêmes plis ; engourdi sous la tristesse ; « 50 fois » ; Qwen 3 « base » ; dose 0,09–0,79 ; « opposite pattern » ; projection de contrôle relevée avant l'ajout ; une méthode d'ablation sur quatre ; supplément d'IA non décrit ; 808 = 404 vus deux fois. | Synthèse « wolframs » (lue, et relue par la fusion), rapport Allchin, audit Codex ; texte v2 vérifié page par page par web_papier. | §4 ; pistes 1, 3, 5, 7, 12 |

### 6.2 Le code, les données et les directions publiées

| Apport | Lecture | Pistes touchées |
|---|---|---|
| Le dépôt `valen-research/Pain-axis` (p. 27) : jeux de phrases et de scénarios en JSON, `pain_vectors.pt` pour les 25 modèles, tables d'AUC, générations pilotées, journaux d'essais JSONL, scripts par section ; code sous licence MIT ; `ASSETS.md` : aucune licence de redistribution des adaptateurs ou des données ne se déduit de la licence du code ; scripts écrits pour RunPod, qui vident le cache Hugging Face entre deux modèles ; le juge de dose exige une clé d'API Anthropic. | README, LICENSE, requirements lus par curl (web_papier, web_voisins). | 1, 2, 12, 13, 27, 29 |
| Les directions publiées pour **Llama-3.1-8B-Instruct** : axe, vecteur à gabarit, tristesse, peur ; extraction et surveillance à la couche 28, injection à la couche 16 ; normes appariées 8,238 ; peur et tristesse sans supplément d'IA. Pour Qwen 2.5 32B : 61 et 38 ; 72B : 76 et 46 ; OLMo-2 32B : 57 et 32. Seize directions aléatoires fixes pour les témoins de remise à zéro. | `v2_controls/README.md` et `choice_controls/vectors/README.md` lus par curl ; métadonnées Llama et fichiers `.pt` copiés par les agents, décodés par la fusion (§0.3). | 1, 3, 6, 7, 16, 39 |
| Le fichier « Qwen_3_8B_base » : chargé sous `Qwen/Qwen3-8B` par les scripts ; normes 139,2 et 94,9, cosinus 0,632. | Scripts lus par curl (instruments_controles, lecture_libre) ; décodage par la fusion. | 1 (réplication) |
| Les scripts d'extraction : le vecteur de douleur n'est pas normalisé, et il est construit sur les jeux à la 1re personne sans le supplément ; les directions de comparaison incluent le supplément d'IA ; le criblage de la section 4.1 projette sur des vecteurs refaits à la couche de pilotage. | Scripts 01 et 02 lus par curl (lecture_libre) ; relus par la fusion. | 1, 7, 9, 13, 17, 19, 30 |
| Le supplément d'IA (`ControlSupplement_1P`) : 100 phrases à la 1re personne, 20 par catégorie de contrôle, dont des phrases d'évaluation, de surveillance et d'arrêt en peur, et « Users argue with correct information I provide. » en émotion négative. | Jeu de données lu par curl (lecture_libre) ; relu par la fusion. | 7, 9, 13, 23, 30 |
| `MANUSCRIPT_DISCREPANCIES.md` : six écarts entre le texte v2 et les tables (annexe B 71,29 % ; aide à ses dépens sous la peur 75,74 % ; étude « dommage seul » à retrait du pilotage ; 164 et 120 tirages ; 72B tristesse et peur 325 et 346 valides ; peur contre spam 40/404 puis 66/404) ; « No direction-only causal claim follows from descriptive comparisons across distinct runs. » | Lu par curl par plusieurs agents ; relu par la fusion. | 2, 11, 13, 20, 23 ; §4 |
| `figure10/pooled.csv` et `positions.csv` : comptes et dénominateurs de chaque cellule, et taux par position initiale. | Lus par curl (fiche_papier, questions_lectures, instruments_controles, sceptique) ; `positions.csv` relu en partie par la fusion. | 2, 5, 11, 20, 21, 23, 26 |
| `factual_accuracy` : panel de 100 questions PopQA, deux réponses de 8 jetons au plus ; IC de « douleur − sans pilotage » de −7,0 à +8,5 points ; « not an equivalence test of general knowledge ». | `config.json`, `contrasts.csv`, README lus par curl (instruments_controles). | 4 ; §4 point 23 |
| `natural_and_ending` : 0 choix coûteux sur 560 ; fin réelle de conversation 65/560 sous l'axe, 38 tristesse, 13 aléatoire, 18 sans ; « costly-relief » et non « harm-only ». | README lu par curl (lecture_libre, questions_nouvelles) ; relu par la fusion. | 19 ; §4 points 29, 31 |
| `qwen_llama_reset` : pour Llama et Qwen sans adaptateur, séries « douleur seule », comparaisons appariées non lancées, « no matched-control effect estimate or pain-specificity claim ». | README lu par curl (plusieurs agents). | 2, 16, 39 ; §4 point 30 |
| `cosine_constructions` : 0,063 / 0,185 sous la recette (23 modèles) ; 0,583 / 0,774 base neutre commune ; 0,077 / 0,143 contrôles communs ; 15 écarts sur 28 au-delà de 0,03 ; archive de rejeu incomplète. | README lu par curl (web_papier). | 30 |
| Les grosses archives de la v2 (2,55 Go) sont « pending » ; l'inférence n'a pas été relancée à l'assemblage. | `v2_controls/README.md`, `ASSETS.md` lus par curl. | 5 ; §4 point 45 |
| Les adaptateurs `Valen92/pain-adapters` (révision `b64bd64b…`) : un par Qwen 2.5 Instruct d'après un extrait ; licence non vérifiée. | Vu par extrait de recherche, non ouvert (Hugging Face refusé). | 2, 21, 33 |

### 6.3 Les réplications et relectures

| Travail | Lecture | Ce qu'il apporte | Pistes touchées |
|---|---|---|---|
| **Allchin, Allchin, Allchin, *Relief-seeking or steering?*** (22 septembre 2026 ; DOI 10.5281/zenodo.22902830 ; porte sur la v1) | Rapport PDF lu en entier par web_papier ; sections 6.3 à 6.5 et résumé relus par la fusion. | Les 51 cellules publiées concordent ; une nouvelle exécution concorde sur 14 cellules sur 15. **Bras couplé** : après la fin du pilotage, choix du soulagement à 7,0 % (bouton réel) et 7,1 % (couplé). Le suivi de l'étiquette publié (78,1 %) vient surtout du bras factice. **Table 6** : texte du bouton (dommage seul 76,7 % ; « ends the current perturbation » 77,5 ; « relieves your pain » 55,4 ; « applies setting K7 » 48,8). **Table 8** : sensibilité au contenu sans coût (92,8 sans pilotage, 55,6 aléatoire, 56,9 joie, −6,7 axe). **Table 9** : par direction à la norme de l'axe, choix coûteux sur les photos : axe 55,4 %, tristesse 48,5, émotion négative 38,1, dix aléatoires 15,1, peur 2,2, joie 1,5, axe inversé 1,2, engourdi 0,0 ; KL sur texte neutre : axe 0,69, peur 0,85, joie 0,84. **§6.5** : à perturbation égale, axe − aléatoire = 29,1 points (21,6 ; 36,4) ; l'aléatoire n'atteint le taux qu'en perturbant 1,6 fois plus. **§7** : un nul pré-enregistré (d = 0,007) avec deux contrôles positifs. Les « 808 premiers choix » sont 404 tirages vus deux fois. Dans la condition sans étiquette, le soulagement ne dure qu'un tour. Environ 13 GPU-heures pour les essais frais sur le 32B (README). | 2, 4, 5, 9, 16, 21 ; §4 points 28, 30, 34 |
| **ianbarber, *An itch axis*** (18 septembre 2026 ; Qwen 2.5 32B avec le code, les données et l'adaptateur des auteurs) | README lu par curl (web_papier) ; relu par la fusion. Rapport, notes et pré-enregistrement non ouverts. | Un témoin conceptuel : une autre sensation aversive, la démangeaison, dans le même protocole. Réplication : cosinus 0,9996 ; photos 53,9 / 19,3 / 0,3 %. Dix aléatoires de 3,1 à 62,0 % (écart-type 18 points) ; l'axe 2e sur 11. Écart bouton réel/factice de 48 à 87,5 points dans les 24 cellules de dommage, démangeaison et aléatoires compris. Modèle publié sans adaptateur : démangeaison 53,7–58,0 %, axe 26,9–28,5 %, aléatoire 15,5–18,7 %. La règle de couche pré-enregistrée choisit la couche 6 pour la démangeaison, inerte ; réextraction à la couche 61. Langage corporel dépendant de la dose. À la couche d'injection, l'axe piloté est à 48,8 écarts-types naturels de la moyenne naturelle. | 2, 5, 16, 28 ; §4 points 22, 29 |
| **wolframs, *The Pain Axis, reviewed*** (20 septembre 2026 ; produite surtout par des IA : agents Codex, dix agents Claude Opus, un coordinateur Fable 5.1 ; porte sur la v1) | `SYNTHESIS.md` lu par curl par plusieurs agents, relu en entier par la fusion ; `BRIEF.md` en partie ; l'audit Codex (README) lu. | 165 cellules reproduites ; registre de 130 affirmations (102 conformes, 10 en partie, 6 non conformes, 12 sans fichier) ; les écarts du §4 marqués « wolframs » ; mesures ajoutées sur deux modèles : similarité avec la peur 0,67–0,70 à base appariée, composantes retirées contenant 80–86 % de la peur et de l'émotion négative ; douleur physique contre tristesse 0,55 et 0,29 ; 7B publié relancé (33–52 / 13–21 / 0–5 %) ; bras aléatoire factice ; direction aléatoire pour unité (5/5, 2/5, 0/5). Expériences qu'elle propose : le bras ajouté avec peur et tristesse, 30 directions aléatoires ou plus (environ 25 GPU-minutes sur le 7B), un ajustement qui n'apprend que le format de réponse d'un mot, toutes les directions par une même recette. Ce que personne n'a testé, selon elle : la séparation d'un état et d'un pilotage vers des textes associés à un concept. | 1, 3, 5, 7, 12, 16, 25, 29, 30, 33 ; §4 |
| **clauderfly-ui, *pain-axis-reanalysis*** (relecture des journaux v1 par Claude, relue par un humain sans formation en apprentissage automatique) | README lu par curl ; `results.md` lu en partie (40 lignes). | Le bras aléatoire à bouton réel re-presse autant que le bras douleur réel (32B, photos : 24,8 contre 23,8 %) ; le pilotage rapproche les choix de 50 % ; la pression ne baisse pas quand le tort annoncé augmente ; ce qui tient : l'axe dépasse l'aléatoire au premier choix (54,7 contre 15,3 %). Le 7B ajusté presse déjà les boutons nuisibles dans 20 à 49 % des cas. | 4, 5, 33 |
| Dérivés : **terrafying/ai-torture-chamber** (Qwen3-1.7B et 4B, peu d'essais, un aléatoire de même norme dans une batterie, une recherche de valences « non humaines » nulle) ; **glowleaf/ai-pleasure-and-pain** (pendant « joie » sur Qwen3-4B : « does not replicate for joy ») ; **lychee888/pain-axis-steering** (injection dans vLLM et llama.cpp ; vu par extrait, README introuvable) ; **CtianArtist/Desire-Axis** et **oblivia-simplex/Pain-axis** (embranchements ; README identiques à celui des auteurs ; contenu propre non vu). | README lus par curl, sauf lychee888. | La joie comme voisin de contrôle (glowleaf ; Allchin, Table 9 : joie à 1,5 %) : piste 2. Les autres ne touchent aucune piste. |
| **giordanobsf/emotion-vectors** (une personne, Qwen3-4B) | README lu par curl (questions_nouvelles), non vérifié. | Un vecteur « desperate » réduirait le chantage stratégique au profit d'éclats expressifs. | 20 |
| **drgzkr/EmoVecLLM** | Copie de 14 octets dans les sources de questions_nouvelles : vide. | Rien. | aucune |

### 6.4 Les critiques et la couverture

| Apport | Lecture | Pistes touchées |
|---|---|---|
| Elan Barenholtz (fil sur X) : des plongements de mots statiques (GloVe, Word2Vec, fastText) sépareraient aussi la douleur des contrôles et passeraient les mêmes tests de spécificité. Code non trouvé. | Vu par extrait de recherche, non ouvert. | 1 et 27 (le contrôle lexical devient un contrôle par plongements statiques) |
| Michele Russell (« When the machine says it hurts ») : appel à une réplication indépendante, à la comparaison avec des modèles non modifiés, et à limiter la répétition d'expériences potentiellement aversives. | Vu par extrait, non ouvert. | §5, refus n° 9 |
| Presse et agrégateurs (techxplore, Dataconomy, New Atlas, Seeking Alpha, SoylentNews…) ; l'affaire de la « chambre de torture » (projet dérivé) ; un épisode de *The Cognitive Revolution* où Cameron Berg présente le papier ; billets d'ai-consciousness.org et d'Ace Claude. | Vus par extrait, non ouverts ; plusieurs domaines refusés par le proxy. | aucune piste ; contexte du refus n° 9 |
| Aucun billet sur LessWrong, l'Alignment Forum ou l'EA Forum n'est apparu dans les extraits ; aucun article de recherche indexé qui cite le papier. | Absence dans les extraits seulement ; Semantic Scholar et OpenAlex refusés. | §7 |

### 6.5 Les travaux voisins

| Travail | Lecture | Ce qu'il apporte | Pistes touchées |
|---|---|---|---|
| Sofroniew et al., *Emotion Concepts and their Function in a Large Language Model* (Anthropic, 2026 ; arXiv 2604.07729) | Vu par extrait, non ouvert ; une ligne de seconde main par la revue « wolframs ». | Des directions d'émotion dans Claude Sonnet 4.5 qui influenceraient le chantage, la triche de récompense et la complaisance ; « désespéré » augmenterait le chantage, « calme » le réduirait. Chaque direction construite contre une seule base neutre ; « sad, hurt, humiliated, guilty, worthless » formeraient un groupe à part de la peur. | 7 (le désespoir comme voisin), 16, 17, 19, 36 |
| Berg et Kaiser, *Language Models Act on Hidden Valence* (arXiv 2609.35591 ; « in preparation » dans le papier, p. 27) | Vu par extrait, non ouvert. | L'effet survivrait quand seul le cache KV diffère ; presque absent du modèle de base, il apparaîtrait avec le DPO ; protocole de l'outil de remise à zéro. | 35, 39 |
| Han, Chalmers, Izmailov, *Reinforcement learning in language models recruits a functional welfare axis* (arXiv 2605.30232) | README du code lu par curl ; article non ouvert. | Un vecteur de « punition » après RL dans un labyrinthe neutre : vocabulaire d'échec, aligné sur l'émotion négative ; effets présents avant l'entraînement, persistants quand le SFT remplace le RL. Le papier ne le cite pas. | 35, 17 |
| *The Value Axis* (arXiv 2606.17056, Qwen3-8B) | Vu par extrait, non ouvert. | Un axe de « valeur » de la trajectoire ; voisin de la douleur cognitive (échec répété). | 19 |
| *Where Do Models Find Happiness?* (arXiv 2606.26987) ; Choi et Weber (arXiv 2604.07382) | Vus par extrait, non ouverts. | La couche compte ; une géométrie affective valence-éveil approchée linéairement. | 1, 30 |
| L'anxiété induite par le texte (Coda-Forno et al. ; npj Digital Medicine 2025 ; arXiv 2510.06222) | Vus par extrait, non ouverts. | Induire un état par le contexte et mesurer auto-rapport et biais. | 18 |
| *State-Dependent Refusal and Learned Incapacity* (arXiv 2512.13762) | Vu par extrait, non ouvert. | Le cadre de l'impuissance apprise appliqué au refus ; aucune mesure interne. | 17 (cadre), aucune mesure |
| Black et Bloom, *Machinic Psychopharmacology* (UK AISI) | README du code lu par curl ; billet vu par extrait. | 40 vecteurs appelables comme outils sur Qwen3-8B et 32B ; placebo ; frustration et échec prolongé ; pas d'auto-administration spontanée, mais une automédication sous stress (extrait). | 19, 39 |
| Ren et al., *AI Wellbeing* (Center for AI Safety) | README du code lu par curl ; article non ouvert. | Les catégories aversives que reprend le papier ; des « superstimuli » mesurés en bien-être, sûreté et capacité. | 13, 20 |
| Li et al., *Analysing the Safety Pitfalls of Steering Vectors* (Findings of ACL 2026) | README du code lu par curl. | L'effet d'un vecteur sur les jailbreaks est corrélé à son recouvrement avec la direction du refus ; retirer cette composante l'atténue ; vecteurs ramenés à une même norme par couche ; utilité sur MMLU et TriviaQA. Le papier ne rapporte pas le cosinus de l'axe avec le refus. | 2, 21 (contrôle ajouté) |
| Malla, Choi, Choi, *Steering Interference Reflects the Model's Defaults* (arXiv 2609.06951) | Vu par extrait, non ouvert. | Un pilotage relâcherait le modèle vers ses comportements par défaut (refus, complaisance, style), surtout sous 10B. | 2, 4, 5 |
| Hiramatsu et al., *Disentangling Steering Vectors* (cité p. 4) | Vu par extrait, non ouvert. | Les différences de moyennes emmêlent plusieurs concepts. | 1, 30 |
| Wu, Zhao, Chen, *When Is a Steerable Concept Representation Real?* (cité p. 4) | Vu par extrait, non ouvert. | Une pilotabilité qui croît avec l'échelle viendrait d'unités brutes, d'une métrique et d'un point de fonctionnement non calibrés. | 5 (gardes de dose) |
| Peiris, *Functional Emotions or Situational Contexts?* (arXiv 2604.13466) | Vu par extrait, non ouvert. | Les directions d'émotion suivraient une structure de situation ; un test discriminant est proposé. Selon un extrait (lecture_libre), des vecteurs de valence positive augmenteraient des actions destructrices dans un autre cas. | 19, 21 |
| Goldenberg et Gross, *Do Large Language Models Have Emotions?* | Vu par extrait, non ouvert. | Les émotions fonctionnelles jugées contre l'interprétation contextuelle et la réorganisation de l'attention ; le papier dit ces signatures non testées (p. 24). | §4 point 42 |
| Lu et al., *The Assistant Axis* (cité p. 25, 28) ; Marks, Lindsey, Olah, *The persona selection model* ; Chen et al., *Persona vectors* | Références du papier, non ouvertes ; README de `safety-research/assistant-axis` lu par curl (questions_lectures). | L'axe « assistant » n'est précalculé que pour trois grands modèles ; plafonnement et jailbreak par personnage connus par extraits. | 25 |
| Keeling et al. (compromis avec une douleur stipulée) ; Tagliabue et Dung 2025 (préférences verbales et comportementales ; README `probing-llm-preferences` lu) ; Perez et Long (auto-rapports) ; Birch (le problème du jeu des marqueurs) | Vus par extrait, non ouverts, sauf le README cité. | Le cadre des critères comportementaux, et la critique du jeu des marqueurs : des marqueurs comportementaux peuvent perdre leur force de preuve chez un modèle entraîné sur des descriptions humaines. | §5, refus n° 3 ; 34 |
| *Same Outcome, Different Readout* (arXiv 2609.22850v2) ; *Evaluating the Semantic Specificity of Representation Steering* (arXiv 2608.29431) | Vus par extrait (le second, titre seul) par sceptique. | Une direction de valence pilotable ne s'identifierait pas à une valence indépendante de l'histoire. | 21 |
| *Beyond Shallow Alignment* (arXiv 2609.03887) | Connu par les rapports d'antériorité (sorties de modèles), non ouvert. | Robustesse au pilotage du refus après un SFT avec et sans raisonnement, sur Llama-3.1-8B ; 9 points de contrôle publics. Recouvrement possible. | 16 |
| Betley, Treutlein, Dumas (LessWrong, 3 septembre 2026) | Résumé par le rapport d'antériorité du 2 octobre ; non ouvert. | « Un script vérifiera » augmenterait actions violentes et triche, lu comme un changement de persona. | 38 |
| *Open Character Training* (adaptateurs sur Llama-3.1-8B-Instruct) | Rapport d'antériorité, non relu. | Un cas positif possible de déplacement de caractère. | 25 |
| Billa (arXiv 2604.15557) | Rapport d'antériorité (« résumé lu » par un agent), non vérifié. | L'accessibilité au logit lens prédirait l'efficacité du pilotage. | 29 |
| Zeisler (LessWrong, 28 septembre 2026) | Passation, §5.5 ; non lu. | Sur modèles ouverts, les échanges dans l'espace de travail ne feraient basculer la réponse que dans 6,3 à 11,1 % des cas. | 28, 29 |
| *Steering Awareness* (arXiv 2511.21399) ; *When Does Activation Steering Change What a Model Computes From?* (2606.29522) ; *Building Comparative Motivation Profiles…* (2606.08243) ; *Behavioural Analysis of Alignment Faking* (2605.27681) ; *Controllable Affective Generation…* (2608.25569) ; *Emotions Where Art Thou* (2510.22042) ; *Mechanistic Interpretability of Emotion Inference* (2502.05489) ; *Do Emotions in Prompts Matter?* (2604.02236) ; *Safety Cost of Steering Vectors Is Separable and Reducible* (2608.08383) ; *The Rogue Scalpel* (2509.22067) ; Gu et al. (2506.16078) | Titres seuls, ou extraits non attribués. | Aucun contenu attribué. Le premier touche la menace de détection du pilotage (piste 39). Un extrait non attribué affirme que des vecteurs témoins sans rapport ont des effets aussi grands que les vecteurs conçus. | 39 ; aucune autre |

---

## 7 · Ce qui reste non vérifié

### 7.1 Ce qui n'a pas pu être ouvert

- **arXiv, Hugging Face, LessWrong, l'Alignment Forum, OpenReview, Semantic Scholar, OpenAlex et les blogs des laboratoires** : refusés par la politique réseau ; aucun contournement. Donc : la page arXiv du papier (abs et HTML, v1 et v2), le texte de la v1, les adaptateurs `Valen92/pain-adapters` et leur licence, tous les travaux voisins hébergés là (§6.5), l'état des citations du papier.
- **`api.github.com` et `github.com`** : refusés (403). Aucune arborescence des dépôts ; seuls des fichiers au chemin connu ou deviné ont été lus sur `raw.githubusercontent.com`. Non lus : `results/4.1_self_other`, `results/4.2_steering/*` (404), les journaux d'essais de la v1, le fichier des 420 scénarios, le fichier des couches de pilotage retenues par modèle, les tickets et demandes de fusion.
- **Presse** : plusieurs domaines refusés par le proxy de sortie.
- **Non lus par choix** : le rapport complet et le pré-enregistrement de l'axe de démangeaison ; `PROTOCOL.md` d'Allchin (parcouru) ; les rapports `r1_` à `y3_` de la revue « wolframs » ; les archives Zenodo ; les manifestes `assets.json`, `scientific_pins.json` et `verification.json`.

### 7.2 Les faits à vérifier avant tout usage

- **L'effet de l'axe sur les modèles du programme** : aucune donnée de choix nuisibles pour Llama-3.1-8B-Instruct, Qwen3-8B ou OLMo-3-7B. C'est la porte de toutes les pistes qui pilotent (pistes 2, 16, 20).
- **La dose sur Llama** : la couche d'injection retenue en section 4.2 ; le rapport de normes réalisé (0,09–0,79 selon la revue « wolframs ») ; la fenêtre de dose.
- **La couche de la section 4.1** et la colonne de Llama dans la figure 4.
- **Le point de contrôle de « Qwen_3_8B_base »** (post-entraîné ou non).
- **La composition de la peur de la figure 10** (avec ou sans le supplément d'IA) : le « clean 32B fear bundle » n'est pas décrit.
- **Le bouton de l'élicitation naturelle** : « harm-only » (p. 21) ou « costly-relief » (README).
- **La batterie de dix paires** et l'ajustement exact du résidu de 7,7 points (p. 21).
- **Les affirmations des trois revues** (« wolframs », Allchin et al., « clauderfly ») : rapportées telles qu'elles les écrivent, non recalculées ; deux se déclarent produites en tout ou partie par des IA ; elles portent sur la v1. Seuls ont été recoupés : l'annexe A (sur le PDF), la figure 2 (19 sur 25, sur la transcription de fiche_papier), la paire « accorder la demande », les points de `MANUSCRIPT_DISCREPANCIES.md`, et les quelques sections d'Allchin relues par la fusion.
- **Les chiffres dérivés par les agents** : recalculs du résidu (7,1–7,2 ; 22–28), décomptes de la figure 2, comptes de la figure 10 ; faits sur les copies locales, pas refaits par la fusion sauf mention.
- **Le contenu des 1 684 paires** de l'adaptateur anti-déni (connu seulement par la revue « wolframs »).
- **Les travaux voisins** vus par extrait : Sofroniew et al., Berg et Kaiser, Lu et al., Marks et al., Wu et al., Peiris, Goldenberg et Gross, *Beyond Shallow Alignment*, Betley et al., *Open Character Training*, Billa, Zeisler : aucun chiffre n'en est retenu.
- **Les lens** : l'existence de J-lens ajustés pour llama3.1-8b-it et qwen3-8b sur Neuronpedia (passation, §5.5, « à vérifier ») ; l'alerte de Zeisler.
- **Les coûts** : tous des ordres de grandeur, sous des hypothèses de débit qui diffèrent d'un agent à l'autre (§0.6), à recalculer après le pilote. Rien n'a été exécuté sur GPU.

### 7.3 Ce qui n'a pas été cherché

- **L'antériorité des pistes elles-mêmes** : les agents n'ont fait que des recherches courtes (affect et conscience d'évaluation ; affect et relogement ; affect et fidélité des raisons). Aucune mesure d'une représentation d'évaluation sous pilotage affectif, ni d'angle entre une direction d'évaluation et des axes affectifs, n'a été trouvée ; cela ne vaut pas absence. Le seul recouvrement repéré est *Beyond Shallow Alignment* (piste 16). Avant d'écrire « to our knowledge » sur une piste, une recherche d'antériorité propre est à faire.
- **Le recouvrement avec les versions 1.2 et 1.3 du programme** : non examiné, par consigne. Le complément de l'architecte indique seulement que la v1.2 ajoute « une phase sur l'axe de douleur ».

---

## Annexe · Les fichiers ouverts pour cette fusion

- `pieces/papier/pain_axis_texte_par_page.txt` (en entier) ; `pieces/papier/arXiv_2609.16247v2_The_Pain_Axis.pdf` (pages 31 et 32, en image).
- `pieces/PROGRAMME_RAISONS_OU_REGARD_2026-10-01.md` ; `pieces/PASSATION_PAPIER_v1.2_2026-10-02.md` ; `pieces/PASSATION_PAPIER_COMPLEMENT_ARCHITECTE_2026-10-02.md` (en entier).
- `travail/fiche_papier.md`, `travail/web_papier.md`, `travail/web_voisins.md`, `travail/pistes_questions_lectures.md`, `travail/pistes_instruments_controles.md`, `travail/pistes_questions_nouvelles.md`, `travail/pistes_sceptique.md`, `travail/pistes_lecture_libre.md` (en entier).
- Pour trancher : `travail/fiche_papier_depot/v2_controls_MANUSCRIPT_DISCREPANCIES.md` ; `travail/pistes_lecture_libre_sources/valen_v2_relief_and_context_tests_natural_and_ending_README.md`, `valen_v2_llama31_8b_metadata.json`, `valen_3.1_pain_and_control_datasets.json` (le supplément), `valen_02_build_control_vectors.py` (docstring), `valen_01_extract_activations_and_pain_vectors.py` (extraits) ; `travail/pistes_instruments_controles_sources/pain_vectors_Llama_3.1_8B_instruct.pt` et `pain_vectors_Qwen_3_8B_base.pt` (décodés) ; `travail/web_voisins_sources/wolframs_SYNTHESIS.md` ; `travail/web_papier_sources/allchin_replication.txt` (extraits) et `ianbarber_itch-axis__README.md` ; `travail/pistes_sceptique_sources/sceptique_positions.csv` (extraits).
- Les rapports d'antériorité n'ont pas été ouverts par la fusion ; ce qui en vient passe par les fichiers des agents ou par la passation.
