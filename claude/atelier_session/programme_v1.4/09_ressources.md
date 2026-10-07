<section class="partie" markdown="1">

# 9 · Ressources et calendrier

**Ce sont des estimations, à recalculer après le pilote.**
- **Les hypothèses** : un ou deux GPU de 80 Go ; un SFT par LoRA sur environ 2 000 exemples, soit 0,5 GPU-heure par entraînement, préparation comprise ; un DPO ou un RL court par LoRA, soit 2 à 4 GPU-heures par entraînement.
- **Le matériel** (décision 4) : un H100 SXM quand il y en a, sinon un A100 80 Go, et plusieurs GPU à la fois, sur vast.ai. Les trois règles :
  - aucune clé de l'API Claude sur ces machines ;
  - un jeton Hugging Face à accès restreint, révoqué ensuite ;
  - les données et les points de contrôle synchronisés vers un stockage de Lazar.
- **Les débits des pistes de l'axe** sont des hypothèses d'agents, non mesurées : une incertitude d'un facteur 2 à 5.

| Phase | Entraînements | Évaluations | GPU-heures |
|---|---|---|---|
| La validation de l'instrument | l'organisme (documents, puis expert iteration) | le balayage de l'inhibition (6 rangs × 4 doses) et les contrôles | 30 – 50 |
| Le test des raisons, et la trajectoire | 4 bras × 5 graines = 20, avec 5 points de contrôle chacun | 3 distances × 3 cadrages ; les sondes sur les points de contrôle | 35 – 60 |
| Le test du regard | — | l'inhibition et les quatre familles de contrôles, avec des crochets (sans vLLM) | 60 – 120 |
| Les ajouts sans injection (bloc A ; partie 5) | — | la vérification de manipulation, le composite, le moniteur, le socle, la géométrie, le contrôle positif | 15 – 36 |
| La localisation du principe | — | le balayage de rang du principe | 20 – 40 |
| Le retrait pendant l'entraînement | 4 voies (retrait de « je suis évalué », retrait aléatoire, invariance, coopération) × 2 bras × 5 graines | l'écart de cadrage, la sonde neuve | 70 – 120 |
| La réplication | le test des raisons et le test du regard, sur Qwen3-8B | le socle de lecture, refait | 90 – 160 |
| La survie | 5 modèles de départ × 2 phases × 3 graines | la fraction conditionnelle, la rétention, la sonde neuve, la trajectoire | 80 – 150 |
| Les raisons notées | 4 bras de RL × 3 graines, avec le juge | les quatre mesures, la fidélité, le test du regard refait | 100 – 200 |
| L'anatomie | l'organisme à concept planté ; les deux LoRA du calme | les sondes, les ablations et les patchs par concept × rang × contrôles ; le lens et sa porte ; la géométrie ; le caractère ; le calme lu | 122 – 253 |
| Les options de l'anatomie | les crosscoders (base contre raisons, base contre actions seules) | les graphes d'attribution, sur un petit modèle | + 50 – 200 |
| **La phase de la détresse, version réduite** (après le post) | — | la porte (22–40) ; dommage ou affinité (12–24) ; le regard sur l'organisme (45–65) ; l'avantage sous détresse, réduit (70–260) ; ce que l'axe lit (0–5) | 149 – 394 |
| — sa médiation | — | trois médiateurs, seuls puis ensemble, contre des maintiens aléatoires | à chiffrer au pilote de la phase |
| — sa version complète | — | l'avantage sous détresse : les familles, la distance lointaine, 5 graines | jusqu'à environ 700 pour la phase |
| Si la détresse passe au ~32B | les bras sur Qwen 2.5 32B, sans adaptateur, × 3 graines | la porte, puis la suite | + 150 – 300 (estimation grossière de la v1.3) |
| « Punir, retirer ou raisonner » | 5 bras de RL × 3 graines (et l'option « raisonner et punir ») ; les quatre détecteurs | la porte ; la fraction par bras ; l'obscurcissement ; le relogement | 110 – 220 |
| **L'expérience minimale** (partie 5) | | | **≈ 135 – 260** |
| **Total**, sans les options, la médiation et la version complète de la détresse, ni le passage au ~32B | | | **≈ 880 – 1 800** |

**Ce qui a changé depuis la v1.3**
- **Le bloc A ajoute** de 15 à 36 GPU-heures, et le calme lu de 2 à 3.
- **La phase de la détresse est refaite** à la règle de la doctrine (partie 7). La v1.3 l'estimait à 100–200 GPU-heures pour toute la phase, sans compter les points d'appariement. La version réduite, sans sa médiation, en demande maintenant de 149 à 394.
- **Le total** passe de 810–1 570 à environ 880–1 800 GPU-heures.

**L'API**
- **La génération des données d'entraînement**, d'après le pipeline v0.1 : de 500 à 1 400 $ au prix standard, et la moitié par lots (non codés) ; le pilote, de 25 à 70 $.
- **Le reste** : les scénarios tenus à part, les paires de concepts, les jeux d'indices, les juges des évaluations, le juge des raisons notées et la vérité de terrain de « punir, retirer ou raisonner ». La v1.3 estimait le tout de quelques centaines à environ 3 000 $ ; c'est à refaire après le pilote.
- **Pas de plafond** (passation v1.2, §3, point 2).

## Le calendrier en quatorze semaines

| Semaine | Travail | Livrable |
|---|---|---|
| 1 | la contre-lecture vierge de cette version, et la version qui en tient compte ; le pilote du pipeline, puis les données ; les scénarios tenus à part et leurs harnais ; les jeux d'indices ; l'organisme ; le détecteur d'audit, entraîné et gelé ; le socle de lecture de l'axe, et l'équilibre affectif des indices ; le composite enrichi ; **le premier temps du pré-enregistrement, déposé sous embargo** | l'empreinte du dépôt, qui date l'idée |
| 2 | la validation de l'instrument et sa porte, avec la vérification de manipulation et la géométrie ; les entraînements du test des raisons (quatre bras, avec points de contrôle) ; le pilote statistique et la simulation de puissance ; **le second temps du gel**, avant toute donnée du test du regard ; le contrôle positif de sensibilité | l'amendement gelé |
| 3 | les évaluations du test des raisons, sa porte, la trajectoire ; le test du regard, avec la vérification de manipulation et le moniteur d'état | les résultats de l'expérience minimale |
| 4 | la rédaction et la publication ; l'embargo du pré-enregistrement se lève | **le post, sur l'Alignment Forum et LessWrong** |
| 5 – 6 | la localisation, puis l'anatomie (le cas connu, lire, causer) ; si un GPU est libre, la porte de la détresse et « dommage ou affinité » : les premières injections, après le post | — |
| 7 | l'anatomie (l'espace de travail, la géométrie, le caractère, le calme lu) ; le retrait pendant l'entraînement | — |
| 8 | la réplication | — |
| 9 | la phase de la détresse : le regard sur l'organisme, l'avantage sous détresse (version réduite), la médiation, ce que l'axe lit | — |
| 10 – 11 | la survie (sa porte), puis les raisons notées (la porte de « je suis noté »), avec la fidélité des raisons | — |
| 12 | « punir, retirer ou raisonner » : sa porte, puis la condition, l'obscurcissement et le relogement | — |
| 13 – 14 | la rédaction, la contre-lecture indépendante du papier, la prépublication | **arXiv**, puis la soumission (lieu et date à vérifier, partie 11) |

**Trois remarques**
- **Le goulot des semaines 1 à 3 est le temps humain, pas les GPU** (pistes de l'axe, §3.1). La semaine 1 est la plus chargée : chaque semaine de retard décale toutes les dates.
- **Aucune pièce ne date le début de la semaine 1** (carte des angles, §5). Si elle commence le lundi 5 octobre 2026 :
  - le post tombe la semaine du 26 octobre ;
  - la prépublication, celle du 4 janvier 2027, après la démonstration des projets SPAR (19 décembre) et les décisions d'ICLR 2027 (16 décembre ; rapport, non relu).

  Avant SPAR, seuls le pré-enregistrement et le post sont tenus.
- **La phase de la détresse est serrée en semaine 9.** Sa porte et « dommage ou affinité » peuvent commencer dès la semaine 5, si un GPU est libre.

</section>
