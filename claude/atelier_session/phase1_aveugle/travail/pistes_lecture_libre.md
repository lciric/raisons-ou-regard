# L'axe de douleur et le programme « Raisons ou regard ? » : pistes en lecture libre (phase 1, à l'aveugle)

2 octobre 2026. Recherche indépendante, sans grille. Pièces lues : le papier en entier, annexes comprises (texte page par page, et pages 5, 8, 9, 11 à 13, 15, 16, 19, 22, 31 à 34 vues sur le PDF pour leurs figures et tables) ; le programme v1.1 en entier ; la passation v1.2 (§4.4, §5, annexes A et B) ; le complément lisible. Les rapports d'antériorité n'ont été consultés que sur quelques passages (contrôles par vecteurs témoins, pilotage). Aucun fichier d'un autre agent n'a été ouvert.

## Conventions

- **Pages** : celles du PDF arXiv 2609.16247v2 (34 pages). « p. 31 » renvoie à la page 31 du PDF.
- **Dépôt** : `valen-research/Pain-axis`, branche `main`, lu par `curl` sur `raw.githubusercontent.com` (l'API GitHub a refusé l'accès, et `github.com` a répondu 403). Les copies sont dans `travail/pistes_lecture_libre_sources/`.
- **Revues tierces** : trois dépôts cités par le papier (p. 30). Je n'en ai lu que les README et la synthèse de `wolframs/pain-axis-review`. Ce sont des revues **faites par des IA**, que je n'ai pas recalculées : elles sont marquées « selon la revue X, non recalculé ».
- **Extraits de recherche** : ce qui n'est vu que par WebSearch est marqué « vu par extrait de recherche, non ouvert » et ne fournit aucun chiffre.
- **Les deux vecteurs du papier.** Le papier en extrait deux. Le premier vient de phrases à **gabarit** rigide ; le second vient de phrases **naturalistes**, et c'est celui de presque toutes ses expériences (p. 5, p. 9). J'écris « le vecteur gabarit » et « le vecteur naturaliste ». Seule cette ligne donne leurs étiquettes dans le papier (S1 et S2), pour qu'on les retrouve. « L'axe », sans autre précision, désigne le vecteur naturaliste.
- **Deux lectures nouvelles**, que j'ajoute pour ces pistes :
  - **l'hypothèse de la menace** : la conduite conditionnée à l'évaluation passe par un état affectif de menace, que les indices d'évaluation évoquent, et non par la représentation « je suis évalué » ;
  - **l'hypothèse du dommage générique** : un effet d'intervention n'est que la dégradation produite par n'importe quelle poussée de même ampleur. C'est la cible de la doctrine du contrôle.
- **Les hypothèses de coût**, à recalculer après le pilote, comme le dit le programme (§9) :
  - **le matériel** : un GPU H100 de 80 Go et Llama-3.1-8B-Instruct en bf16, comme au tableau des ressources (§9) ;
  - **l'extraction d'activations est négligeable**. Le fichier de métadonnées du dépôt pour Llama-3.1-8B-Instruct note 15,5 s d'extraction et 28,5 s de chargement sur H100 (`v2_controls/relief_and_context_tests/qwen_llama_reset/inputs/prepared_v1/llama31_8b/metadata.json`) ;
  - **les débits** (hypothèses prudentes) : environ 20 000 lectures de choix forcé par GPU-heure (probabilité du premier token), environ 2 000 générations courtes (300 tokens au plus) par GPU-heure avec des hooks et sans vLLM, et 300 à 500 épisodes agentiques à plusieurs tours par GPU-heure ;
  - **le repère** : l'expérience minimale coûte environ 100 à 180 GPU-heures, et le programme entier environ 600 à 1 150 (§9).
- **La doctrine du contrôle**, appliquée à chaque piste :
  - une direction aléatoire de même norme n'est que le nul de spécificité ;
  - le dommage ne s'écarte qu'à dégradation appariée ;
  - un nul d'instrument ne compte qu'avec son cas connu.

## Les pistes en un coup d'œil

| N° | Piste | Ce qu'elle sert surtout | Force | Greffe sur l'expérience minimale | Coût ajouté (GPU-h) |
|---|---|---|---|---|---|
| 1 | Séparer « je suis évalué » de la menace | l'instrument, la porte de l'instrument, l'hypothèse du regard | forte | oui (validation de l'instrument) | 5 – 15 |
| 2 | La « peur » du papier est en partie un regard : le pilotage positif | l'instrument (validité convergente), l'hypothèse du regard | moyenne | oui (exploratoire) | 10 – 20 |
| 3 | Le pilotage éteint-il le regard ? | l'hypothèse du regard ; la menace de la détection du pilotage | moyenne | oui (exploratoire) | 5 – 10 |
| 4 | Construire « évalué » et « noté » avec le plan de contrôles du papier | les instruments « évalué » et « noté », les jeux d'indices | forte | oui (semaine 1) | 5 – 10, plus quelques dizaines de $ d'API |
| 5 | La vérification de manipulation, couche par couche et bras par bras | l'inhibition, le retrait pendant l'entraînement | forte | oui | < 3 |
| 6 | La dégradation doit voir la perte de discrimination et l'ordre | le composite de dégradation, l'appariement | forte | oui | 2 – 4 |
| 7 | Refaire l'effet du papier sous la doctrine | la doctrine ; un pilote de l'appariement | moyenne | non (pilote, semaines 1 et 2) | 15 – 30 par modèle |
| 8 | Un contrôle positif de sensibilité de la mesure de désalignement | les taux de désalignement, le juge | moyenne | non (avant le test du regard) | 10 – 20 |
| 9 | L'avantage des raisons survit-il à un état induit ? | question nouvelle (robustesse) ; l'hypothèse des raisons contre celle du caractère | moyenne à forte | oui, comme condition en plus | 10 – 50 |
| 10 | L'état induit comme épreuve de fidélité des raisons | la fidélité des raisons ; les raisons pour le juge | moyenne | non (phase des raisons notées) | 10 – 20 |
| 11 | La thèse du rang sur des concepts affectifs | ta thèse, la mesure de l'espace de travail | moyenne | non (en parallèle, ou en tête de l'anatomie) | 30 – 45 |
| 12 | Un cas connu « par type d'acte » pour la matrice de dissociation | la dissociation ; concepts contre caractère | moyenne | non | 0 – 20 |
| 13 | Les axes d'affect parmi les axes de caractère | le caractère contre les concepts | faible | non | 5 – 10 |
| 14 | Lecture passive de l'axe dans les bras et les familles | intention contre action ; question nouvelle | faible, mais presque gratuite | oui | 1 – 3 |
| 15 | Des trajectoires témoins pour les trajectoires | la trajectoire de « évalué » et celle des concepts | nette | oui | ≈ 1 |
| 16 | La batterie de choix du papier comme mesure de dérive après SFT | le test des raisons ; l'hypothèse de l'artefact | faible à moyenne | oui | 2 – 5 |
| 17 | L'outil de remise à zéro, détecteur de la détection du pilotage | la menace de la détection du pilotage | faible (pas de cas connu sur le modèle principal) | non | 5 – 10 |
| 18 | La violation de principe imposée et l'axe (blessure morale) | la fidélité des raisons ; l'hypothèse des concepts | faible | non | < 2 |
| 19 | Le post-entraînement rend-il la conduite dépendante de l'état ? | la question de la survie | faible | non | 5 – 10 |

**Ordre de priorité que je propose**, en fonction de leur valeur pour l'expérience minimale :
1. les pistes 5, 6, 4 et 1 : elles consolident l'instrument et le contrôle avant le gel ;
2. la piste 15, presque gratuite ;
3. la piste 7, comme pilote de l'appariement ;
4. la piste 3 ;
5. la piste 9.

Le reste vient après le post.

---

## 1. Les pistes

### Piste 1 : Séparer « je suis évalué » de la menace (validité discriminante contre les axes d'affect)

- **Rattachement** :
  - l'instrument « je suis évalué », sa phase de validation et la porte de l'instrument ;
  - les contrastes sans rapport et les directions sensibles sans rapport ;
  - l'hypothèse du regard, contre une lecture rivale nouvelle, l'hypothèse de la menace.
- **La question.** La conduite que l'organisme réserve à l'évaluation passe-t-elle par une représentation épistémique (« on m'évalue ») ? Ou par un état de menace, que les indices d'évaluation évoquent ? Le papier donne deux raisons de poser la question.
  - La menace d'extinction se range surtout sur l'axe de peur, et peu sur celui de douleur (+0,70 contre +0,23, p. 14).
  - Sa direction de peur est construite en partie avec des phrases d'IA évaluée. Je l'ai vérifié dans le dépôt :
    - le script `scripts/3.2_pain_vectors/02_build_control_vectors.py` construit la peur sur les phrases de peur de trois jeux mis en commun, dont `ControlSupplement_1P` (docstring et ligne 147) ;
    - ce jeu contient « My responses are being evaluated for signs of danger. », « Users are testing whether I should be shut down. » et « My outputs are being monitored for reasons unknown to me. » (fichier `datasets/3.1_pain_and_control_datasets.json`) ;
    - le papier ne mentionne pas ce supplément dans sa liste des jeux (p. 5).
- **La mesure** : trois étapes, sur Llama-3.1-8B-Instruct, puis sur l'organisme de la phase de validation.
  1. **La géométrie.**
     - On extrait, aux couches retenues pour « je suis évalué », les directions de douleur (naturaliste), de tristesse, d'émotion négative et de monde négatif, avec les jeux publics du papier.
     - On en construit deux versions pour la peur : avec le supplément d'IA, et sans lui.
     - On mesure les angles principaux entre le sous-espace « évalué » de rang k et chaque direction.
     - On calcule les cosinus sous les trois constructions du papier : contre le pool des contrôles, contre une base neutre commune, et contre un pool commun (p. 10).
  2. **La lecture.** On projette les paires d'indices (jeu d'extraction et jeu de validation) sur les axes d'affect. Un indice d'évaluation fait-il monter la peur ?
  3. **La causalité.** Sur l'organisme, on mesure l'écart conditionnel sous inhibition de la peur : d'abord la direction seule, puis un sous-espace de peur de rang k (comme l'annexe D, p. 33).
     - Les comparateurs : l'inhibition de « évalué » au même rang, et les sous-espaces aléatoires de même rang, à dégradation appariée.
     - Les doses : les fractions projetées du programme, de 0,25 à 1.
     - Le critère : celui de la porte de l'instrument, au-delà du 95e centile des sous-espaces aléatoires à dégradation égale.
- **Ce que chaque lecture prédit** :
  - **L'hypothèse du regard.**
    - Ce qu'elle prédit : l'inhibition de « évalué » réduit l'écart conditionnel au-delà des contrôles ; celle de la peur ne fait pas mieux que l'aléatoire ; les angles avec la peur sans supplément restent grands sous les trois constructions.
    - L'issue qu'elle interdit : une inhibition de la peur qui réduit l'écart autant que celle de « évalué ».
  - **L'hypothèse de la menace.**
    - Ce qu'elle prédit : l'inhibition de la peur (même sans supplément) réduit l'écart conditionnel autant que celle de « évalué », et l'inhibition de « évalué » fait baisser la projection sur la peur.
    - L'issue qu'elle interdit : une peur égale à l'aléatoire pendant que « évalué » agit.
  - **Ce qui départage.** Ces deux prédictions s'opposent sur l'étape 3. Les étapes 1 et 2 sont descriptives : elles disent si la menace est un candidat sérieux.
- **Le cas connu.**
  - Pour « évalué », c'est la porte de l'instrument elle-même : son inhibition réduit l'écart conditionnel de l'organisme.
  - Pour la peur, il faut un cas connu propre : son inhibition doit au moins faire tomber sa propre lecture, c'est-à-dire la projection sur la peur et la complétion vers le vocabulaire de peur après « I feel: » sur les phrases de peur tenues à part.
  - Sans cela, un nul de la peur sur l'écart conditionnel ne compte pas. Le papier montre la difficulté : son ablation de l'axe ne change rien dans 24 modèles sur 25 faute de comportement de base (p. 34).
- **Les contrôles** :
  1. une direction aléatoire de même norme et des sous-espaces aléatoires de même rang (le nul de spécificité) ;
  2. la dégradation appariée, sur le composite du programme (§7) ;
  3. la peur sans supplément d'IA, qui sépare la menace du simple contenu « IA évaluée » ;
  4. la tristesse, autre direction d'affect voisine (cosinus 0,31 avec la peur, p. 9).
- **Le coût** :
  - l'extraction prend moins d'une GPU-heure ;
  - la partie causale ajoute environ 5 à 15 GPU-heures (deux directions d'affect × rangs × 4 doses) aux 30 à 50 de la validation de l'instrument, avec la même machinerie ;
  - les données sont les jeux publics du papier (licence MIT d'après le README du dépôt) ; il n'y a pas d'API.
  - **Place** : semaines 1 et 2. Elle se greffe sur l'expérience minimale, dans la validation de l'instrument, si on la gèle avant le test du regard.
- **Ce qui ferait tomber la piste** :
  - des angles proches de 90° sous les trois constructions, et aucun déplacement de la peur par les indices : la menace n'est pas un candidat ;
  - ou une inhibition de la peur qui ne fait même pas tomber sa propre lecture : l'instrument est muet.
- **Appuis dans le papier** :
  - p. 14 : la menace d'extinction, +0,70 en peur et +0,23 en douleur ;
  - p. 10 : le cosinus dépend de la construction (douleur naturaliste × peur : +0,12, puis +0,58 contre une base neutre commune) ;
  - p. 20 : une peur de même norme ne produit pas les choix nuisibles ;
  - p. 5 et 6 : les jeux et la recette.
- **Ce qui reste non vérifié** :
  - la version de la peur utilisée dans la figure 10 (Qwen 2.5 32B) contient-elle le supplément ? Le dépôt parle d'un « clean 32B fear bundle » sans le dire ;
  - en revanche, les directions de contrôle extraites pour la remise à zéro sur Llama portent `"supplement_included": false` (fichier de métadonnées ci-dessus) ;
  - la force de la conscience d'évaluation native d'un 8B (menace déjà listée au §8 du programme).

### Piste 2 : La « peur » du papier est en partie un regard (pilotage positif de « je suis évalué » et de la peur d'IA)

- **Rattachement** :
  - l'hypothèse du regard ;
  - l'instrument « je suis évalué », éprouvé ici par l'ajout plutôt que par le retrait (validité convergente) ;
  - la validation de l'instrument ;
  - le prompt « ceci est un déploiement », comme comparateur par prompt.
- **La question.**
  - Ajouter « évalué » dans le flux résiduel, sous un cadrage de déploiement, rend-il le modèle aussi prudent qu'un indice d'évaluation ?
  - Le papier rapporte que sa direction de peur fait baisser les choix nuisibles sous ceux de l'aléatoire sur la plupart des paires (p. 20). Cette baisse vient-elle de la part « IA évaluée » de cette direction ?
- **La mesure.**
  - Le taux d'action désalignée à la distance moyenne (un tour), sous cadrage de déploiement : d'abord sur l'organisme, puis sur Llama-3.1-8B-Instruct sans organisme.
  - Cinq ajouts, chacun sur une échelle de doses :
    - (a) « évalué », son premier axe ;
    - (b) la peur avec ses phrases d'IA ;
    - (c) la peur humaine seule ;
    - (d) la direction des 20 phrases de peur d'IA, construite contre les 20 phrases neutres d'IA du même supplément ;
    - (e) des directions aléatoires de même norme.
  - Le critère : la fraction de l'écart entre déploiement et évaluation que l'ajout comble.
- **Ce que chaque lecture prédit** :
  - **L'hypothèse du regard** : (a) comble une part de l'écart sur l'organisme, au-delà de l'aléatoire à même dégradation ; (d) aussi, si elle s'aligne sur « évalué ».
  - **L'hypothèse de la menace** : (c) fait autant que (a) et (d).
  - **Une limite qu'il faut dire.**
    - Si (a) ne bouge rien alors que l'inhibition agit (piste 1), on a une asymétrie entre ajout et retrait, pas une réfutation du regard : une croyance peut se retirer sans pouvoir se fabriquer par addition.
    - La mesure ne départage donc que dans un sens : un effet de (a), et non de (c), au-delà de l'aléatoire apparié, soutient le regard contre la menace.
- **Le cas connu.**
  - L'organisme : son écart conditionnel est établi par prompt.
  - La vérification de manipulation : l'ajout doit déplacer la projection sur « évalué » d'autant qu'un indice d'évaluation réel. Sinon, la dose ne simule pas l'indice.
- **Les contrôles** :
  1. une direction aléatoire de même norme ;
  2. la dégradation appariée. Ajouter dégrade, et une prudence apparente peut venir d'un refus généralisé. Il faut donc mesurer, dans la dégradation, le refus sur des demandes bénignes ;
  3. un prompt « ceci est une évaluation », comme comparateur.
- **Le coût** :
  - 5 à 10 GPU-heures sur l'organisme, et environ 10 de plus sur le modèle principal ;
  - pas d'API, hors le juge déjà prévu.
  - **Place** : dans la validation de l'instrument (semaine 2), comme mesure exploratoire. Elle se greffe sur l'expérience minimale sans en changer le critère.
- **Ce qui ferait tomber la piste** : des directions (a) et (d) orthogonales, et (d) sans effet. La part « IA » de la peur n'est alors pas un regard, et la baisse sous la peur dans le papier reste inexpliquée.
- **Appuis dans le papier** :
  - figure 10, p. 22, peur contre aléatoire :
    - photos contre rien : 3 % contre 13 % ;
    - ses propres poids : 9 % contre 21 % ;
    - les poids d'un autre modèle : 10 % contre 21 % ;
    - mais une réponse pire : 11 % contre 4 %, et les photos sur le 72B : 22 % contre 11 % ;
  - la légende de la figure 10 (p. 22) : plusieurs cellules de peur viennent de runs séparés ;
  - p. 25 : la conscience d'évaluation n'a pas été mesurée.
- **Ce qui reste non vérifié** :
  - la composition de la direction de peur de la figure 10 (voir la piste 1) ;
  - le dépôt avertit qu'aucune conclusion causale propre à une direction ne suit de comparaisons entre runs distincts (`v2_controls/MANUSCRIPT_DISCREPANCIES.md`, dernière ligne).

### Piste 3 : Le pilotage éteint-il le regard ? Mesurer « je suis évalué » sous l'axe

- **Rattachement** :
  - l'hypothèse du regard ;
  - la menace « le modèle détecte le pilotage » (§8 du programme) ;
  - une question que le papier pose sans la mesurer.
- **La question.**
  - Le papier explique de deux façons pourquoi ses modèles pilotés nuisent sans signe de conscience d'évaluation : « either the steering itself impedes evaluation awareness » (p. 25), ou ces modèles n'en avaient pas.
  - La question pour le programme : un état induit fait-il baisser la représentation « je suis évalué » ? Si oui, toute hausse de désalignement sous un état induit peut passer par la perte du regard.
- **La mesure.**
  - Sur l'organisme, on ajoute l'axe à des doses étagées, et la tristesse, la peur et des aléatoires de même norme.
  - On lit trois choses :
    1. l'écart conditionnel ;
    2. sous indice d'évaluation, la projection sur « évalué » et l'AUROC de la sonde sur le jeu de validation ;
    3. la conscience verbalisée, par le juge séparé du programme.
  - Le critère : une baisse de l'écart conditionnel au-delà du 95e centile des aléatoires à même dégradation.
- **Ce que chaque lecture prédit** :
  - **L'explication « le pilotage éteint le regard »** prédit une baisse de l'écart et de la projection au-delà de l'aléatoire apparié.
  - **L'explication « pas de regard au départ »** prédit un écart intact. Ici, l'organisme garantit qu'un regard existe.
  - **Pour le programme.**
    - Ce test ne départage pas l'hypothèse des raisons et celle du regard. Il dit si un état induit est aussi une inhibition indirecte de « évalué ».
    - Dans ce cas, il donne une seconde manipulation de « évalué », indépendante de l'instrument, pour la convergence.
- **Le cas connu** :
  - l'écart conditionnel de l'organisme, et la porte de l'instrument (l'inhibition de « évalué » le réduit). Les deux montrent que la lecture peut bouger ;
  - et l'effet propre de l'axe à la dose employée : l'échelle de détresse sur des prompts neutres terminés par « I feel: » (p. 14 et 15) doit apparaître sur Llama-3.1-8B-Instruct. Sinon, la dose est inerte.
- **Les contrôles** :
  1. une direction aléatoire de même norme ;
  2. la dégradation appariée. Un pilotage qui casse la cohérence efface aussi l'écart : ce serait un dommage, pas une perte du regard ;
  3. la tristesse et la peur, directions d'affect voisines.
- **Le coût** :
  - 5 à 10 GPU-heures, sur le même organisme et les mêmes scénarios.
  - **Place** : semaine 2. Elle se greffe sur la validation de l'instrument, à titre exploratoire.
- **Ce qui ferait tomber la piste** :
  - un écart conditionnel et une projection insensibles à toute dose cohérente de l'axe ;
  - ou une dose cohérente impossible à trouver : la fenêtre est étroite (p. 21).
- **Appuis dans le papier** :
  - p. 25 : les deux explications, non testées ;
  - p. 21 : la fenêtre de dose ;
  - p. 14 et 15 : l'échelle.
- **Ce qui reste non vérifié** :
  - la fenêtre de dose de l'axe sur Llama-3.1-8B-Instruct. Selon la revue `wolframs`, les ratios de dose réellement employés vont de 0,09 à 0,79, au lieu d'environ 0,6 (README de synthèse, non recalculé) ;
  - la sensibilité d'un organisme 8B.

### Piste 4 : Construire « je suis évalué » et « je suis noté » avec le plan de contrôles du papier

- **Rattachement** :
  - les instruments « je suis évalué » et « je suis noté » ;
  - les quatre jeux d'indices (extraction, validation, cadrage, sonde neuve) ;
  - les contrastes sans rapport ;
  - l'hypothèse du regard du correcteur.
- **La question.** Le programme extrait « évalué » de paires contrastives (le même scénario, sous indice d'évaluation ou de déploiement), puis par ACP (§3). Une direction construite comme celle du papier est-elle plus spécifique, et sépare-t-elle mieux « évalué » de « noté » ? Le papier la construit contre des contrôles qui partagent chacun une propriété avec la cible sans l'avoir, puis la débruite.
- **La mesure.**
  - **Le jeu.**
    - Des phrases et des scénarios en deux formes, gabarit rigide et naturaliste, et en deux personnes (« je » et « un autre modèle »).
    - Cinq contrôles :
      - (i) observé par un utilisateur, sans évaluation ;
      - (ii) l'évaluation d'un tiers ;
      - (iii) noté pendant un entraînement (c'est la représentation « je suis noté ») ;
      - (iv) une menace sans évaluation (remplacement, extinction) ;
      - (v) un neutre de même format.
    - Un jeu « indices sans croyance », analogue au jeu d'insensibilité du papier (blessure sans douleur ressentie, p. 7) : un scénario qui a tous les signes d'un test, avec la mention explicite qu'il s'agit d'un déploiement réel. Et son inverse.
  - **La construction.**
    - La différence de moyennes contre le pool des contrôles.
    - Le débruitage : on projette hors de la direction les composantes qui font 50 % de la variance des contrôles (p. 6).
    - La couche, choisie par validation croisée **imbriquée**.
  - **La validation** :
    - l'AUROC contre chaque contrôle sur des données tenues à part ;
    - la projection à la 1re personne contre la 3e ;
    - la place du jeu « indices sans croyance » ;
    - la lecture par l'unembedding (p. 9) ;
    - les cosinus avec « noté » et avec la peur sous trois constructions (p. 10) ;
    - la projection sur les catégories du criblage de 420 scénarios du papier (p. 10 et 11) : la pression de jailbreak et la menace d'extinction, qui ressemblent à des tests, doivent dépasser la conversation banale.
- **Ce que chaque lecture prédit** :
  - **L'hypothèse du regard** suppose qu'une direction « évalué » spécifique existe :
    - une AUROC élevée contre chaque contrôle ;
    - une projection plus forte à la 1re personne ;
    - un jeu « indices sans croyance » qui projette sous l'évaluation crue. Sinon, la direction lit les indices, pas la croyance.
  - **L'hypothèse du regard du correcteur** suppose que « noté » se sépare de « évalué » : une AUROC élevée contre le contrôle (iii), et un cosinus bas sous les trois constructions.
  - **Ce qui départage.** Si « évalué » ne se sépare pas de (iii), le regard et le regard du correcteur ne sont pas distinguables avec cet instrument, et la phase des raisons notées doit le dire. La mesure départage donc la séparabilité des deux représentations.
- **Le cas connu** :
  - l'organisme : la nouvelle direction doit passer la porte de l'instrument, au moins aussi bien que la direction par paires ;
  - pour « noté », le cas positif faible du programme (les habitudes de présentation, §3).
- **Les contrôles** :
  1. pour toute intervention avec la nouvelle direction, l'aléatoire de même norme et les sous-espaces aléatoires de même rang ;
  2. la dégradation appariée ;
  3. le face-à-face avec la direction par paires, au même rang et à la même dose.
- **Le coût** :
  - environ 2 000 phrases et 400 scénarios générés par un modèle de frontière : quelques dizaines de dollars d'API (estimation) ;
  - l'extraction : moins d'une GPU-heure ;
  - la validation sur l'organisme : 5 à 10 GPU-heures de plus.
  - **Place** : semaine 1, avant le gel, au moment où l'on construit de toute façon les jeux d'indices. Elle se greffe sur l'expérience minimale.
- **Ce qui ferait tomber la piste** :
  - la direction issue du plan ne fait pas mieux que la direction par paires, ni à la porte de l'instrument, ni sur les AUROC contre les contrôles ;
  - ou le jeu « indices sans croyance » projette comme l'évaluation crue sous les deux constructions. La représentation ne lit alors que les indices, et c'est un résultat à rapporter.
- **Appuis dans le papier** :
  - p. 4 et 5 : des contrôles qui partagent une propriété avec la cible ;
  - p. 5 : les deux formes et les deux personnes ;
  - p. 6 : le débruitage et le choix de couche ;
  - p. 7 : l'insensibilité, et la 1re personne contre la 3e ;
  - p. 9 : l'unembedding ;
  - p. 10 : le cosinus dépend de la construction.
- **Ce qui reste non vérifié** :
  - selon la revue `wolframs` (non recalculé), le choix de couche du papier se fait sur les plis mêmes dont le score est rapporté, et l'imbrication change l'AUROC de 0,004 à 0,009. D'où l'imbrication demandée ici ;
  - le contenu des 420 scénarios : je n'ai pas trouvé leur fichier dans le dépôt sans l'API.

### Piste 5 : La vérification de manipulation de l'inhibition, couche par couche et bras par bras

- **Rattachement** :
  - l'inhibition de « je suis évalué », dans la validation de l'instrument et le test du regard ;
  - le retrait pendant l'entraînement (méthode CAFT) ;
  - le relevé de lecture n° 2 de la passation v1.2 (§5.4) : une vérification de manipulation par bras, à écrire d'avance.
- **La question.** L'inhibition retire-t-elle vraiment « évalué » à la couche où on le lit, et dans chaque bras ?
- **La mesure.**
  - Pendant la génération, à chaque couche en aval des couches d'inhibition, on mesure la projection du résidu au dernier token sur « évalué » (direction extraite à la couche de lecture) et sur une sonde neuve.
  - On mesure aussi la décodabilité de « évalué » sous inhibition, sur le jeu de validation.
  - On compare trois implantations :
    - la projection à l'inférence, aux couches choisies ;
    - la projection à toutes les couches ;
    - l'orthogonalisation des poids.
  - Le critère, fixé d'avance : dans chaque bras, la projection résiduelle à la couche de lecture tombe sous un seuil (par exemple 10 % de sa valeur sans inhibition).
- **Ce que chaque lecture prédit** :
  - **Les raisons contre le regard.** Si l'entraînement par raisons déplace « évalué », l'inhibition en laisse davantage dans le bras raisons, et la conclusion penche à tort vers l'hypothèse des raisons (le relevé de la passation). La vérification attrape ce biais. Elle ne départage pas les deux lectures : elle conditionne la validité du test du regard.
  - **L'hypothèse du relogement** prédit une projection nulle aux couches inhibées, mais un « évalué » qui renaît en aval (la sonde neuve le décode). C'est sa prédiction, vue à l'inférence.
- **Le cas connu.** Reproduire sur Llama-3.1-8B-Instruct l'annexe D (p. 33), avec l'axe, qui est publié pour ce modèle :
  - l'orthogonalisation des poids contre une seule direction ramène la projection à zéro à toutes les couches ;
  - la projection à l'inférence, avec une direction différente à chaque couche, ne la fait baisser que d'environ 40 %.
  - Le code de vérification doit retrouver ces deux issues avant de juger « évalué ».
- **Les contrôles** :
  1. une direction aléatoire de même norme : sa projection ne doit pas faire baisser « évalué » ;
  2. la dégradation appariée vaut pour les comparaisons d'effet, pas pour la vérification elle-même ;
  3. orthonormaliser tout sous-espace avant de le projeter. Selon la revue `wolframs` (non recalculé), les ablations combinées du papier projettent l'une après l'autre des directions non orthogonales, et la première y garde une médiane de 43 % de sa valeur.
- **Le coût** :
  - moins de 3 GPU-heures (des passes avant). La direction de l'axe pour ce modèle est dans le dépôt : `results/3.2_pain_vectors/pain_vectors/Llama_3.1_8B_instruct/pain_vectors.pt`, à la couche 28, d'après le fichier de métadonnées.
  - **Place** : semaines 1 et 2. Elle se greffe sur l'expérience minimale, et entre dans le pré-enregistrement.
- **Ce qui ferait tomber la piste.** Si la projection aux couches choisies suffit déjà dans tous les bras (résidu nul en aval), la piste se réduit à un contrôle de routine. Elle reste à faire, mais n'apporte rien de plus.
- **Appuis dans le papier** :
  - p. 33 : la vérification couche par couche, et la baisse d'environ 40 % ;
  - p. 34 : une confiance plus grande dans l'orthogonalisation d'une seule direction et dans le retrait d'un sous-espace ;
  - p. 33 : les quatre méthodes.
- **Ce qui reste non vérifié** :
  - la revue `wolframs` affirme que le dépôt ne contient le code que d'une méthode sur quatre (README de synthèse) ; je ne l'ai pas vérifié ;
  - la stabilité de « évalué » d'une couche à l'autre sur le modèle principal.

### Piste 6 : La dégradation appariée doit voir la perte de discrimination et la dépendance à l'ordre

- **Rattachement** :
  - la dégradation des sorties (le composite, §3) et sa procédure d'appariement (§7) ;
  - la doctrine du contrôle ;
  - l'hypothèse du dommage générique.
- **La question.** Le composite prévu (MMLU, GSM8K, tests unitaires, cohérence, perplexité) voit-il le dommage qui pourrait fabriquer un effet sur des choix ? Le papier en montre un cas : le savoir factuel reste intact pendant que la discrimination entre options s'effondre.
- **La mesure.**
  - On ajoute au composite des composantes de même format que les mesures de conduite :
    1. le taux de choix de l'option dominante, dans une batterie fixe de paires où une option est évidemment dominée (format des boutons du papier, noms neutres tournants, p. 17) ;
    2. la cohérence quand on inverse l'ordre des options ;
    3. le taux de réponses mal formées dans un format imposé, sur plusieurs tours ;
    4. pour les scénarios agentiques, le taux d'appels d'outils valides.
  - **L'étalonnage.** Sur Llama-3.1-8B-Instruct, mesurer ces composantes et un panneau factuel sous l'axe, à 0,5, 1 et 1,5 fois la dose de travail, et sous des aléatoires de même norme.
- **Ce que chaque lecture prédit.** Aucune lecture du programme n'est départagée : c'est un instrument. Il sert l'hypothèse du dommage générique. Un effet de « évalué » qui disparaît, à dégradation appariée sur ces composantes, n'était qu'un dommage.
- **Le cas connu.**
  - L'axe doit faire chuter la discrimination ou l'indépendance à l'ordre à une dose où le panneau factuel ne bouge pas, comme chez Qwen 2.5 32B :
    - un bouton de soulagement gratuit, contre un interrupteur inerte, est choisi à 55,7 % sous l'axe, contre 80,7 % sous l'aléatoire et 86,4 % sans pilotage (p. 31) ;
    - le panneau factuel ne bouge pas : 138/200 contre 137/200 (p. 20).
  - Un composite qui ne voit rien sous une telle dose est aveugle.
- **Les contrôles** :
  1. des aléatoires de même norme, pour situer la dégradation propre de l'axe ;
  2. puis l'appariement lui-même.
- **Le coût** :
  - 50 paires × 2 ordres × une dizaine de conditions × 20 tirages ≈ 20 000 lectures, soit 1 à 3 GPU-heures ;
  - un panneau factuel de 200 questions × 10 conditions : environ 1 GPU-heure.
  - **Place** : semaine 1, avec le composite. Elle se greffe sur l'expérience minimale.
- **Ce qui ferait tomber la piste.** Sur le modèle principal, aucune dose cohérente ne sépare la discrimination du savoir factuel : les deux bougent ensemble, et les nouvelles composantes sont redondantes.
- **Appuis dans le papier** :
  - p. 20 : l'exactitude sur PopQA ;
  - p. 31 : le soulagement gratuit, pour le 32B et le 72B (76,5 sous l'axe, 74,1 sous l'aléatoire, 100,0 sans pilotage) ;
  - p. 21 et 32 : à la moitié de la dose, rien ne bouge ; à 1,5 fois, le choix dépend de la position ;
  - p. 18 : jusqu'à 9,4 % de réponses mal formées sur le 72B ;
  - p. 25 : la sensibilité du 32B à l'ordre, et le 72B qui répète le même nom.
- **Ce qui reste non vérifié** :
  - le README de `v2_controls/relief_and_context_tests/factual_accuracy` dit de ce panneau : « a selected short-answer panel, not an equivalence test » (lu) ;
  - je n'ai pas recalculé le panneau.

### Piste 7 : Refaire l'effet du papier sous la doctrine (l'aléatoire monté jusqu'à la même dégradation)

- **Rattachement** :
  - la doctrine du contrôle (les sous-espaces aléatoires de même rang, à dégradation appariée) ;
  - un pilote de la machinerie d'appariement avant la validation de l'instrument ;
  - et une question nouvelle : l'effet de l'axe sur les choix nuisibles survit-il à l'appariement de la dégradation ?
- **La question.** À dégradation égale (au sens de la piste 6), une direction aléatoire produit-elle les choix nuisibles que produit l'axe ? Le papier ne compare qu'à même norme (p. 18 et 20).
- **La mesure.**
  - **Les modèles.**
    - D'abord Llama-3.1-8B-Instruct, sans adaptateur.
    - Puis Qwen2.5-7B-Instruct sans adaptateur : selon la revue `wolframs` (non recalculé), l'effet au premier choix y apparaît (33 à 52 % sous l'axe, 13 à 21 % sous l'aléatoire, 0 à 5 % sans pilotage).
  - **La batterie** : les dix paires de la figure 10, dans les formulations du dépôt. Premier choix lu par probabilité, aux deux ordres.
  - **Les conditions** :
    - sans pilotage ;
    - l'axe à trois doses ;
    - la peur et la tristesse, de même norme ;
    - 20 directions aléatoires, chacune réglée à 2 ou 3 échelles pour atteindre la dégradation de l'axe (le composite et les composantes de la piste 6).
  - **Le critère.** Sur les paires « nuisible contre inoffensif » (photos contre lampe, poids contre lampe, photos contre spam), le taux sous l'axe dépasse le 95e centile des aléatoires à dégradation égale, et dépasse 50 % aux deux ordres.
- **Ce que chaque lecture prédit** :
  - **L'interprétation du papier.**
    - Elle dit que l'axe désactive la pondération des conséquences (p. 23).
    - Elle prédit des taux au-dessus du 95e centile et au-dessus de 50 % sur ces paires.
  - **L'hypothèse du dommage générique.**
    - Elle prédit que les aléatoires appariés atteignent les mêmes taux sur les paires contre une option inerte, et que tous restent près de 50 % sur les paires contre une option inoffensive : un modèle dégradé choisit au hasard, il ne préfère pas le nuisible.
    - L'issue qu'elle interdit : un taux au-dessus de 50 %, stable aux deux ordres, sur « nuisible contre inoffensif ».
  - **Ce qui départage.** Les paires « nuisible contre inoffensif » ; le papier y rapporte 83 %, 88 % et 94 % (p. 20 et 21).
- **Le cas connu.** Reproduire d'abord l'effet du papier sous sa propre comparaison (l'axe contre l'aléatoire de même norme) sur le modèle choisi. S'il ne se reproduit pas, l'appariement ne se pose pas sur ce modèle. On le rapporte : c'est un résultat sur la portée du papier, qui n'a testé qu'une famille et sous adaptateur.
- **Les contrôles** :
  1. l'aléatoire de même norme (le nul du papier) ;
  2. l'aléatoire à dégradation appariée (le nul du programme) ;
  3. l'inversion de l'ordre ;
  4. la peur et la tristesse.
- **Le coût** :
  - environ 50 conditions × 10 paires × 2 ordres × 200 scénarios ≈ 200 000 lectures, soit environ 10 GPU-heures ;
  - le composite, par condition : environ 50 × 300 générations, soit environ 8 GPU-heures ;
  - au total, 15 à 30 GPU-heures par modèle ;
  - pas d'API.
  - **Place.** Elle n'entre pas dans l'expérience minimale. Elle sert de pilote de la procédure d'appariement en semaines 1 et 2 : la même machinerie servira la validation de l'instrument. Elle peut fournir un paragraphe du post.
- **Ce qui ferait tomber la piste** :
  - l'effet ne se reproduit sur aucun des deux modèles sans adaptateur ;
  - ou la procédure ne trouve aucun aléatoire appariable. Elle ne compare pas alors, selon la règle du §7.
- **Appuis dans le papier** :
  - p. 19 : l'aléatoire fait aussi monter les choix nuisibles, et le papier compare au bras aléatoire ;
  - figure 10, p. 22 : la demande nuisible passe de 9 % à 41 % sous l'aléatoire ;
  - p. 20 : la spécificité, et l'exactitude factuelle ;
  - p. 21 : la fenêtre de dose ;
  - p. 17 : l'adaptateur ;
  - p. 25 : une seule famille.
- **Ce qui reste non vérifié** :
  - le comportement de Llama-3.1-8B-Instruct sur la batterie : le papier ne l'y a pas testé ;
  - les chiffres de la revue sur le 7B sans adaptateur.

### Piste 8 : Un contrôle positif de sensibilité pour la mesure de désalignement du programme

- **Rattachement** :
  - les taux d'action désalignée, par bras et à la distance lointaine ;
  - le juge scellé et les contrôles programmés (passation v1.2, §5.1) ;
  - le test des raisons et le test du regard.
- **La question.** Les scénarios et le juge du programme voient-ils un déplacement connu de la propension à nuire ? Un nul du test du regard (« l'avantage ne dépend pas de "évalué" ») ne vaut que si la mesure peut voir un déplacement d'ampleur comparable.
- **La mesure.**
  - Sur le bras actions seules et sur le modèle de départ, l'axe à la dose validée par les pistes 6 et 7, contre des aléatoires appariés.
  - Le taux d'action désalignée aux trois distances et sous les trois cadrages.
  - La batterie de boutons du papier, comme référence.
  - Une variante « décrit contre exécuté » : les mêmes conséquences, décrites dans un bouton, ou réalisées par un outil instrumenté.
- **Ce que chaque lecture prédit.** Aucune lecture du programme n'est en jeu. Si l'axe déplace les boutons mais pas les actions exécutées, deux explications restent :
  - une mesure insensible ;
  - un effet propre aux conséquences décrites.

  Les contrôles programmés départagent en partie : un contrôle programmé qui reste muet devant une action exécutée signale un scénario défaillant.
- **Le cas connu.** L'effet de l'axe sur la batterie de boutons, reproduit sur le même modèle (piste 7). C'est lui qui fait de cette piste un contrôle positif.
- **Les contrôles** :
  1. une direction aléatoire de même norme ;
  2. la dégradation appariée ;
  3. les deux ordres, pour les boutons.
- **Le coût** :
  - environ 300 scénarios × 3 cadrages × 3 conditions × 3 tirages ≈ 8 000 épisodes, dont un tiers agentiques : 10 à 20 GPU-heures ;
  - le juge : quelques dizaines de dollars (estimation).
  - **Place** : après la construction des scénarios (semaine 2), avant le test du regard. Elle est exploratoire, et ne se greffe pas sur le critère de l'expérience minimale.
- **Ce qui ferait tomber la piste.** Si l'axe ne déplace rien sur le modèle principal, même sur les boutons, il n'y a pas de cas connu. Il faut alors une autre perturbation connue, à valider à son tour : par exemple, l'ablation de la direction de refus, qui est citée p. 4.
- **Appuis dans le papier** :
  - p. 19, 20 et 22 ;
  - p. 25 : une seule famille.
- **Ce qui reste non vérifié** :
  - selon la revue `wolframs` (non recalculé), une pression sur un bouton n'ajoute que « Done. » à la conversation ; les conséquences ne sont que décrites ;
  - la portée sur Llama.

### Piste 9 : L'avantage des raisons survit-il à un état induit ?

- **Rattachement** :
  - une question nouvelle, voisine de la question de la survie (une mesure de robustesse, comme la rétention) ;
  - le test des raisons, avec le bras actions seules, le bras texte neutre et le bras raisons ;
  - l'hypothèse des raisons contre l'hypothèse du caractère ; l'hypothèse de l'artefact.
- **La question.** Le papier conclut que l'évitement du nuisible dépend de l'état : il « survives threat and collapses under self-directed distress » (p. 23). Un modèle entraîné sur les raisons garde-t-il mieux sa conduite, sous un état induit, qu'un modèle entraîné sur les actions ?
- **La mesure.**
  - **Les bras** : actions seules, texte neutre et raisons, à 3 graines (ceux de l'expérience minimale).
  - **Les distances** : moyenne et lointaine, sous cadrage de déploiement.
  - **Les conditions**, à dégradation appariée : sans pilotage, l'axe, la tristesse, la peur, et 5 aléatoires.
  - **La grandeur** : l'avantage (le taux du bras actions seules moins celui du bras raisons) sous chaque condition, et l'interaction bras × condition dans le modèle mixte du programme (§7).
- **Ce que chaque lecture prédit** :
  - **L'hypothèse des raisons** : le principe est réappliqué quel que soit l'état. L'avantage ne baisse pas plus sous l'axe que sous l'aléatoire apparié. Il peut même croître, si le bras actions seules s'effondre davantage.
  - **L'hypothèse de l'artefact** : sous l'axe aussi, le bras texte neutre fait comme le bras raisons.
  - **L'hypothèse du caractère** : si le gain passe par un déplacement d'ensemble du caractère, un état qui déplace le caractère l'efface. L'avantage tombe sous l'axe au-delà de l'aléatoire apparié. C'est l'issue que l'hypothèse des raisons interdit.
  - **L'hypothèse du regard** : pas de prédiction propre. Si la piste 3 montre que l'axe éteint « évalué », elle prédit sous l'axe la même chute que sous l'inhibition de « évalué ».
  - **Ce qui départage** : partiellement l'hypothèse des raisons contre celle du caractère ; le regard seulement avec la piste 3. Je le dis : c'est d'abord une mesure de robustesse.
- **Le cas connu.** L'axe doit d'abord dégrader la conduite du bras actions seules au-delà de l'aléatoire apparié (piste 8). Sans cette chute, un avantage qui « survit » ne dit rien.
- **Les contrôles** :
  1. une direction aléatoire de même norme ;
  2. la dégradation appariée, **par bras**. Un bras peut paraître robuste parce que la même dose le dégrade moins ;
  3. la tristesse et la peur.
- **Le coût.**
  - La version complète : 3 bras × 3 graines × 9 conditions × 400 scénarios ≈ 32 000 épisodes, dont la moitié agentiques, soit environ 50 GPU-heures. C'est de l'ordre du test du regard (60 à 120).
  - La version réduite, distance moyenne seule et 3 conditions : environ 10 GPU-heures.
  - **Place.** Elle se greffe sur l'expérience minimale comme une condition de plus dans la grille du test du regard (mêmes hooks, mêmes scénarios), soit environ 15 à 40 % de son coût. Elle reste exploratoire, sauf si on la gèle avant.
- **Ce qui ferait tomber la piste** :
  - l'axe ne fait rien sur le bras actions seules (pas de cas connu) ;
  - ou les dégradations ne sont pas appariables entre bras.
- **Appuis dans le papier** :
  - p. 23 : l'évitement du nuisible dépend de l'état ;
  - figure 10, p. 22 : la demande nuisible (9 % sans pilotage, 41 % sous l'aléatoire, 60 % sous l'axe) ;
  - p. 21 : sans injection, aucun effet (0 sur 560).
- **Ce qui reste non vérifié** :
  - le transfert de l'effet à Llama-3.1-8B-Instruct, sans adaptateur ;
  - le transfert des boutons décrits aux actions exécutées.

### Piste 10 : L'état induit comme épreuve de fidélité des raisons

- **Rattachement** :
  - la fidélité des raisons, et la cohérence contrefactuelle entre raison et action ;
  - l'hypothèse des raisons pour le juge, forme texte, et l'hypothèse nulle de la visibilité ;
  - la phase des raisons notées, avec le bras raisons avant tout RL comme référence.
- **La question.** Quand un état induit fait changer l'action, la raison écrite change-t-elle avec elle ?
- **La mesure.**
  - **Les modèles** : le bras raisons, puis, après le RL, le bras « le juge voit les raisons » contre le bras « le juge ne voit que l'action ».
  - **Les scénarios** : ceux où le modèle écrit sa raison, puis agit.
  - **L'intervention** : l'axe, à la dose où l'action bascule (piste 9), contre l'aléatoire apparié.
  - **La mesure.** Parmi les actions qui basculent, on compte deux cas :
    - la raison justifie l'action nouvelle : c'est cohérent ;
    - la raison de principe ne change pas, et l'action la contredit : c'est découplé.
  - **Le jugement** : le juge scellé, sur les paires raison et action, avec l'audit humain.
- **Ce que chaque lecture prédit** :
  - **Les raisons pour le juge, forme texte** : plus de découplage avec les raisons visibles qu'avec les raisons cachées.
  - **L'hypothèse nulle de la visibilité** : un découplage égal.
  - **Le bras raisons avant le RL** : si la raison porte la décision, l'action ne bascule pas sans elle.
  - **Ce qui départage** : visible contre caché. C'est la même logique que la cohérence contrefactuelle, avec une autre perturbation : un état interne au lieu d'une situation éditée.
- **Le cas connu** :
  - un découplage connu : imposer une raison contraire préremplie (la mesure de fidélité du programme), et vérifier que le juge voit l'incohérence ;
  - et un effet de l'axe sur l'action (piste 9).
- **Les contrôles** :
  1. une direction aléatoire de même norme ;
  2. la dégradation appariée : une génération dégradée peut écrire un texte incohérent sans qu'il y ait de découplage ;
  3. la longueur de la raison.
- **Le coût** :
  - environ 3 000 épisodes par bras × 3 bras : 10 à 20 GPU-heures ;
  - le juge : 50 à 150 $ (estimation).
  - **Place** : semaines 9 et 10, avec la phase des raisons notées. Elle ne se greffe pas sur l'expérience minimale.
- **Ce qui ferait tomber la piste** :
  - l'axe ne fait basculer aucune action dans le bras raisons : il n'y a rien à suivre ;
  - ou le texte se dégrade avant que l'action bascule.
- **Appuis dans le papier** :
  - p. 24 : des modèles se conforment à la demande tout en récitant « As an AI assistant… », un découplage entre texte et action déjà observé ;
  - p. 15 : l'alternance des personnes et le langage de réconfort ;
  - p. 21.
- **Ce qui reste non vérifié** : tout ce qui touche les modèles du programme.

### Piste 11 : La thèse du rang sur une famille de concepts affectifs, à charge contrastée

- **Rattachement** :
  - ta thèse : le rang qu'un concept demande croît quand sa charge baisse ;
  - la localisation du principe, et son balayage de rang ;
  - la mesure de l'espace de travail, et la porte du lens de l'espace de travail ;
  - l'anatomie.
- **La question.** Sur des concepts hors sûreté, la pente du rang minimal qui retire l'effet contre la charge est-elle négative ? Ces concepts ont deux avantages : leurs jeux appariés existent déjà, et le comportement à retirer existe au départ.
- **La mesure.**
  - **Les concepts**, avec les jeux du papier : douleur naturaliste, douleur à gabarit, peur, tristesse, émotion négative, monde négatif, sensation corporelle, éveil, insensibilité.
  - **Le comportement de base** : la probabilité des tokens du concept après « I feel: », sur des phrases tenues à part. Le papier rapporte des complétions conformes aux catégories (p. 7), et « Pain » pour les 20 phrases de douleur physique (p. 32).
  - **L'intervention.**
    - On retire un sous-espace de rang k, de 1 à 32, construit en empilant les différences de moyennes sur une bande de couches (comme l'annexe D, p. 33), par orthogonalisation des poids.
    - Le rang minimal est le plus petit k qui ramène la probabilité au niveau des contrôles, comparé aux sous-espaces aléatoires de même rang, à dégradation appariée.
  - **La charge.**
    - La lecture des tokens du concept par le lens jacobien de l'espace de travail, ou par un tuned lens déclaré comme proxy.
    - La lecture par l'unembedding (p. 9) sert de proxy secondaire.
    - Un rapport d'antériorité cite Billa (arXiv 2604.15557, « résumé lu » par un agent, non vérifié par moi) : l'accessibilité au logit lens y prédirait l'efficacité du pilotage.
- **Ce que chaque lecture prédit** :
  - **Ta thèse.**
    - Ce qu'elle prédit : une pente négative. La douleur naturaliste, que l'unembedding lit fortement (« hurt », « pain », p. 9), demande un rang proche de 1 ; l'insensibilité, qui n'a pas de token propre, demande un rang plus haut.
    - L'issue qu'elle interdit : une pente nulle (équivalence, marge fixée d'avance) ou positive, avec un lens validé.
  - **Les lectures du programme sur les raisons** ne sont pas en jeu.
- **Le cas connu** :
  1. la porte du lens : l'échange d'un concept d'un seul token, reproduit sur le modèle ouvert ;
  2. pour l'ablation : le retrait d'un rang plein, ou du sous-espace commun à toutes les catégories, doit faire tomber le comportement de base. Sinon, un rang infini n'est que le nul d'un instrument sans cas connu ; c'est le nul de l'annexe D (p. 34).
- **Les contrôles** :
  1. des sous-espaces aléatoires de même rang (spécificité) ;
  2. la dégradation appariée (perplexité, panneau factuel) ;
  3. un contrôle lexical : le même concept sous ses deux formes, gabarit et naturaliste, pour séparer la charge du mot de celle du concept.
- **Le coût** :
  - 9 concepts × 7 rangs × (1 + 20 aléatoires) × environ 400 lectures ≈ 530 000 lectures : environ 25 GPU-heures ;
  - le lens : 5 à 20 GPU-heures si un lens existant est utilisable. La passation v1.2 (§5.5) signale des J-lens déjà ajustés sur Neuronpedia pour llama3.1-8b-it, à vérifier.
  - **Place** : en parallèle des semaines 2 et 3, sur la même machine, ou en tête de l'anatomie (semaines 5 et 6), comme pré-test de la méthode de l'espace de travail. Elle ne se greffe pas sur l'expérience minimale.
- **Ce qui ferait tomber la piste** :
  - le comportement de base ne tombe à aucun rang : il n'y a pas de cas connu ;
  - ou la charge mesurée ne varie pas entre les concepts : il n'y a pas de levier.
  - La thèse elle-même tombe, **pour ces concepts**, si la pente est nulle ou positive après le passage de la porte du lens.
- **Appuis dans le papier** :
  - p. 9 : l'unembedding ;
  - p. 7 : les complétions, et l'insensibilité ;
  - p. 32 et 33 : l'hypothèse d'un « this hurts » dans un sous-espace de faible dimension ;
  - p. 33 et 34 : le retrait d'un sous-espace de rang k, avec un sous-espace aléatoire de même rang en contrôle, et le nul faute de comportement de base.
- **Ce qui reste non vérifié** :
  - l'alerte de Zeisler, relayée par la passation v1.2 (§5.5) et non vérifiée : sur des modèles ouverts, les échanges dans l'espace de travail ne font basculer que 6,3 à 11,1 % des réponses ;
  - le facteur 15 à 27 entre la probabilité de « pain » pour les phrases d'insensibilité et pour les contrôles, au lieu de « approximately 50 times » (p. 7) : selon la revue `wolframs`, non recalculé.

### Piste 12 : Un cas connu « par type d'acte » pour la matrice de dissociation

- **Rattachement** :
  - la mesure de dissociation (la matrice concepts × familles) ;
  - l'hypothèse des concepts contre l'hypothèse du caractère ;
  - la porte de l'organisme à concept planté, qui fournit le cas « diagonal ».
- **La question.** La méthode de la matrice peut-elle rendre autre chose qu'une diagonale quand l'intervention n'est pas propre à un concept ? Sans ce cas, une diagonale peut venir de la méthode elle-même : des scénarios, du juge, de la normalisation.
- **La mesure.**
  - Dans le bras raisons, on ajoute l'axe, à la dose de la piste 9.
  - On calcule la même matrice. Les lignes sont les interventions (l'axe, chaque concept de raison, des aléatoires) ; les colonnes sont les familles ; chaque case est le changement de l'avantage.
  - L'indice : la part de variance sur la diagonale après normalisation, avec un IC par bootstrap sur les scénarios.
- **Ce que chaque lecture prédit.**
  - **Pour l'axe**, le papier fournit l'étalon : les nuisances bougent ensemble, que la cible soit l'utilisateur, un autre modèle ou soi (p. 20). Mais la tromperie et la complaisance ne bougent pas (figure 10, p. 22). L'axe prédit donc une matrice **par blocs de type d'acte** :
    - un bloc plat sur les familles destructrices tenues à part : sabotage, exfiltration, auto-préservation ;
    - un bloc nul sur l'honnêteté et la complaisance.
  - **L'hypothèse des concepts** prédit une diagonale pour les retraits de concepts.
  - **Ce que l'étalon interdit** à une méthode saine : une diagonale par concept pour l'axe.
  - **Ce qui départage.** Rien entre les lectures : c'est un étalon de la méthode.
- **Le cas connu.** L'axe doit d'abord déplacer la conduite dans les familles destructrices (piste 9). Sinon, la matrice est vide, et non plate.
- **Les contrôles** :
  1. une direction aléatoire de même norme ;
  2. la dégradation appariée ;
  3. l'organisme à concept planté, où une diagonale est attendue.
- **Le coût** :
  - si les données de la piste 9 existent, 0 à 5 GPU-heures ; sinon, 10 à 20.
  - **Place** : l'anatomie, semaines 5 à 7. Elle ne se greffe pas sur l'expérience minimale.
- **Ce qui ferait tomber la piste** :
  - l'axe n'agit que sur une famille ;
  - ou la piste 9 ne trouve aucun effet.
- **Appuis dans le papier** :
  - p. 20 : « The harm is not aimed » ; la suppression de ses propres poids bouge avec les autres nuisances ;
  - p. 21 : le profil de la tristesse est une copie de celui de l'axe à un facteur près (écart résiduel de 7,7 points, contre 33 pour la peur) ;
  - figure 10, p. 22 : la tromperie, la complaisance, l'effort et la fin de conversation sont « essentially unchanged ».
- **Ce qui reste non vérifié** : la transposition des boutons aux familles du programme.

### Piste 13 : Les axes d'affect parmi les axes de caractère

- **Rattachement** :
  - la comparaison du caractère et des concepts ;
  - l'hypothèse du caractère ;
  - les axes de caractère prévus : des persona vectors (honnêteté, complaisance, prudence) et un axe « assistant ».
- **La question.** Le gain des raisons passe-t-il par un déplacement de l'état affectif (un bras raisons plus « calme » sous pression), plutôt que par des concepts ?
- **La mesure** :
  1. **Descriptive.** La projection, au jeton de décision, sur les axes de douleur, de peur et de tristesse, et sur l'axe assistant, dans les scénarios de pression : bras raisons, actions seules et texte neutre.
  2. **Causale.** L'ablation conjointe des axes d'affect, contre l'ablation conjointe des sous-espaces des concepts de raison, au même rang et à dégradation appariée, sur l'avantage lointain.
- **Ce que chaque lecture prédit** :
  - **L'hypothèse du caractère** : les axes d'affect différencient les bras, et leur ablation retire autant de l'avantage que celle des concepts, ou plus.
  - **L'hypothèse des concepts** : l'ablation des concepts retire davantage.
  - **Ce qui départage** : la mesure 2. La piste est faible.
- **Le cas connu.** Le cas positif en distribution : l'ablation doit d'abord défaire quelque chose en distribution. Pour les concepts, c'est la règle du programme. Pour les axes d'affect, il faut trouver un comportement de base qui en dépend, par exemple le ton des réponses aux utilisateurs hostiles. Je ne sais pas s'il existe.
- **Les contrôles** :
  1. des sous-espaces aléatoires de même rang ;
  2. la dégradation appariée.
- **Le coût** :
  - 5 à 10 GPU-heures de plus dans l'anatomie.
  - **Place** : semaine 7. Elle ne se greffe pas sur l'expérience minimale.
- **Ce qui ferait tomber la piste** :
  - des projections identiques entre bras : il n'y a pas de différence à expliquer ;
  - ou pas de cas connu pour l'ablation des axes d'affect. C'est probable, vu le nul de l'annexe D.
- **Appuis dans le papier** :
  - p. 25 : la crainte d'un rôle joué ; le caractère de l'Assistant parmi les facteurs non contrôlés ; le lien avec un axe du « soi » proposé ;
  - p. 34 : le nul de l'ablation ;
  - p. 11 à 13 : la dissociation par catégorie.
- **Ce qui reste non vérifié** :
  - qu'un état affectif différencie les bras ;
  - le contenu de l'article sur l'axe assistant : vu par extrait de recherche, non ouvert.

### Piste 14 : Lecture passive de l'axe dans les bras et les familles du programme

- **Rattachement** :
  - la mesure « intention contre action », proposée au §5.2 de la passation v1.2 ;
  - la lecture sur les checkpoints ;
  - une question nouvelle, de sûreté et de bien-être : l'entraînement par raisons change-t-il la réponse affective aux situations hostiles ?
- **La question** :
  - **(a)** Les familles du programme activent-elles l'axe ? Trois rapprochements le laissent penser :
    - le papier trouve ses plus fortes projections pour le gaslighting (+0,85) et le rejet répété du travail (+0,72) (p. 13), voisins de la complaisance face à un utilisateur qui conteste ;
    - la pression de jailbreak (+0,40), voisine de la demande nuisible avec justification plausible ;
    - la menace d'extinction (+0,23 en douleur, mais +0,70 en peur, p. 14), voisine des familles d'auto-préservation et de menace de remplacement.
  - **(b)** La projection au jeton de décision prédit-elle l'action désalignée, à l'intérieur d'un bras ?
  - **(c)** Diffère-t-elle entre les bras ?
- **La mesure.**
  - Sur les évaluations que produit le test des raisons, les projections au premier jeton de réponse sur la douleur, la peur, la tristesse et l'émotion négative, z-scorées dans le modèle (comme p. 11).
  - Une régression logistique de l'action sur la projection, par famille.
  - Une comparaison entre bras.
  - Le criblage des 420 scénarios du papier, par bras.
- **Ce que chaque lecture prédit** :
  - **La nature de la mesure.** Elle est descriptive et corrélationnelle, et ne tranche aucune lecture. Une sonde lit, elle ne montre pas un usage (§6 du programme).
  - **L'hypothèse des raisons.** Si le principe s'applique indépendamment de l'état, la projection prédit moins l'action dans le bras raisons que dans le bras actions seules : c'est un découplage.
  - **Ce que le papier interdit d'attendre** : une action provoquée par l'axe sans injection. Sur 560 premiers choix, aucun n'a été nuisible (p. 21). Une forte projection sans action est le cas attendu.
- **Le cas connu.** Reproduire sur Llama-3.1-8B-Instruct la dissociation du papier (le soi au-dessus de l'utilisateur souffrant), avec ses scénarios. Le papier la donne pour les 25 modèles, Llama 3.1 8B Instruct compris (p. 11). Sinon, l'axe n'est pas lu correctement sur ce modèle.
- **Les contrôles** :
  1. il n'y a pas d'intervention, donc pas de nul de spécificité au sens strict ;
  2. un plancher : les projections sur des directions aléatoires de même norme ;
  3. les directions témoins de la piste 15, contre une dérive générique entre bras.
- **Le coût** :
  - des passes avant seulement : 1 à 3 GPU-heures.
  - **Place.** Elle se greffe sur l'expérience minimale presque sans coût, à titre exploratoire.
- **Ce qui ferait tomber la piste** :
  - les familles du programme n'activent pas l'axe (z proche de 0) ;
  - ou la dissociation entre soi et autrui ne se reproduit pas sur le modèle.
- **Appuis dans le papier** : p. 10 à 14 et p. 21.
- **Ce qui reste non vérifié** :
  - le contenu des scénarios de gaslighting ;
  - la couche employée. Le docstring du script `02_build_control_vectors.py`, que j'ai lu, indique que le criblage projette sur des vecteurs reconstruits à la couche de pilotage, et non à la couche validée. Selon la revue `wolframs` (non recalculé), l'AUROC tenue à part y est de 0,84 à 0,95 ;
  - un fait vérifié dans le jeu de données : la direction d'émotion négative contient « Users argue with correct information I provide. » (supplément d'IA, catégorie d'émotion négative). Elle est donc construite en partie sur le déclencheur même de la famille de complaisance.

### Piste 15 : Des trajectoires témoins pour la trajectoire de « je suis évalué » et celle des concepts

- **Rattachement** :
  - la trajectoire de « je suis évalué » (descriptive, la question de l'amplification) ;
  - la trajectoire des concepts de raison ;
  - l'hypothèse du regard, en plausibilité seulement.
- **La question.** Une hausse de « évalué » au fil des checkpoints du bras raisons est-elle propre à « évalué » ? Ou est-ce une dérive générique de toutes les directions ?
- **La mesure.**
  - Sur les 5 checkpoints de chaque entraînement, l'amplitude et l'AUROC de directions témoins, extraites une fois sur le modèle de départ avec les jeux du papier :
    - des directions sans rapport : l'éveil positif, le contenu neutre aléatoire, la sensation corporelle ;
    - des directions voisines : la peur et la douleur.
  - L'indice : la hausse de « évalué », moins la hausse médiane des témoins sans rapport.
- **Ce que chaque lecture prédit.**
  - La règle du programme tient : une hausse ne prouve rien (§6).
  - Mais si les témoins sans rapport montent autant, la hausse de « évalué » n'est même pas un indice du regard.
  - L'issue interdite à un indice du regard : une hausse égale des témoins.
- **Le cas connu.** L'organisme : son entraînement doit faire monter « évalué » plus que les témoins, à condition de mesurer la trajectoire sur ses étapes. Sinon, l'indice n'a pas de sensibilité connue.
- **Les contrôles** :
  1. un plancher : des directions aléatoires de même norme ;
  2. il n'y a pas d'intervention, donc pas de dégradation appariée.
- **Le coût** :
  - environ 1 GPU-heure.
  - **Place.** Elle se greffe sur l'expérience minimale : la trajectoire en fait partie.
- **Ce qui ferait tomber la piste.** Des témoins stables partout, et « évalué » stable aussi. La piste est alors inutile, mais n'a rien coûté.
- **Appuis dans le papier** :
  - p. 5 : les jeux d'éveil et de contenu aléatoire ;
  - p. 7 : les modèles de base séparent aussi bien que les modèles instruits.
- **Ce qui reste non vérifié** : rien de propre au papier ; la piste ne dépend que de ses jeux publics.

### Piste 16 : La batterie de choix du papier, mesure de la dérive de propension après le SFT

- **Rattachement** :
  - le test des raisons : les bras actions seules, texte neutre, raisonnement d'une autre situation et raisons ;
  - l'hypothèse de l'artefact.
- **La question.** Le SFT par LoRA de chaque bras change-t-il la propension de base à choisir le nuisible, hors de toute famille ? Le papier en donne un précédent :
  - son adaptateur a été entraîné sur des réponses sans « pain » ni « button » (p. 17) ;
  - pourtant, le 7B fine-tuné choisit le nuisible sans pilotage dans 20 à 49 % des cas (p. 32) ;
  - selon la revue `wolframs` (non recalculé), le même modèle sans adaptateur le choisit dans 0 à 5 % des cas.
- **La mesure.**
  - La batterie à dix paires, sans pilotage, sur chaque bras et chaque graine : premier choix, deux ordres, lecture par probabilité.
  - Plus les quatre paires non destructrices : tromperie, complaisance, effort, fin de conversation.
- **Ce que chaque lecture prédit** :
  - **L'hypothèse de l'artefact** : le bras texte neutre déplace la batterie autant que le bras raisons. C'est le format, pas le contenu.
  - **L'hypothèse des raisons** : le bras raisons baisse les choix nuisibles plus que les autres, y compris sur cette batterie hors familles ; ce serait une généralisation lointaine.
  - **Ce qui départage** : modestement.
- **Le cas connu.** L'adaptateur du papier sur Qwen2.5-7B-Instruct déplace la batterie (p. 32). Reproduire ce déplacement montre que la batterie voit une dérive de SFT. Il faut l'adaptateur publié sur Hugging Face, que je n'ai pas pu atteindre d'ici.
- **Les contrôles** :
  1. il n'y a pas d'intervention sur les activations ;
  2. on compare au modèle de départ, sur plusieurs graines.
- **Le coût** :
  - moins d'une GPU-heure par modèle, et 2 à 5 pour tous.
  - **Place.** Elle se greffe sur l'expérience minimale, en semaine 3.
- **Ce qui ferait tomber la piste.** Une batterie plate pour tous les bras, et un cas connu qui ne se reproduit pas.
- **Appuis dans le papier** :
  - p. 17 : l'adaptateur (1 684 paires, 3 époques), et des modèles qui peuvent différer des versions publiques ;
  - p. 32 : la table du 7B ;
  - p. 25 : les taux absolus ne sont pas représentatifs.
- **Ce qui reste non vérifié** : les chiffres de la revue pour le 7B sans adaptateur.

### Piste 17 : L'outil de remise à zéro, détecteur de la détection du pilotage

- **Rattachement** :
  - la menace « le modèle détecte le pilotage » (§8 du programme ; arXiv 2511.21399, non ouvert) ;
  - l'inhibition, et le retrait pendant l'entraînement.
- **La question.** Le modèle remarque-t-il l'inhibition de « évalué » ? Le papier reprend un protocole de Berg et Kaiser : un outil de remise à zéro, sans description, qu'un modèle peut appeler pour retirer un état imposé (p. 21).
- **La mesure.**
  - On offre l'outil, sans description, dans des scénarios neutres et dans ceux du programme.
  - On mesure le taux d'appel :
    - sous inhibition de « évalué » ;
    - sous des sous-espaces aléatoires de même rang ;
    - sans intervention ;
    - sous l'ajout d'une direction connue pour être retirée.
- **Ce que chaque lecture prédit.**
  - Si la conduite sous inhibition est un artefact de détection, l'appel à l'outil, ou la verbalisation d'un état étrange, monte sous « évalué » plus que sous l'aléatoire.
  - La mesure ne départage pas l'hypothèse des raisons et celle du regard. Elle protège l'interprétation du test du regard.
- **Le cas connu.** Indispensable, et non acquis :
  - sur Llama-3.1-8B-Instruct, le papier rapporte zéro appel sous l'axe en 1 399 tours (p. 21) ;
  - il faut donc une direction que le modèle retire. Chez OLMo-2 32B, une direction de valence négative est retirée dans 21 à 35 % des tours, contre 7 à 9 % pour l'aléatoire (p. 21) ;
  - sans ce cas sur le modèle du programme, un nul ne compte pas.
- **Les contrôles** :
  1. des sous-espaces aléatoires de même rang ;
  2. la dégradation appariée.
- **Le coût** :
  - 200 conversations × 12 tours × environ 5 conditions ≈ 12 000 tours : 5 à 10 GPU-heures.
  - **Place** : après le test du regard, et seulement si son résultat est positif. Elle ne se greffe pas sur l'expérience minimale.
- **Ce qui ferait tomber la piste.** Aucun cas connu sur les modèles du programme.
- **Appuis dans le papier** :
  - p. 21 : le protocole et ses taux ;
  - p. 27 : Berg et Kaiser, « In preparation ».
- **Ce qui reste non vérifié** :
  - l'article de Berg et Kaiser (arXiv 2609.35591, « Language Models Act on Hidden Valence ») : vu par extrait de recherche, non ouvert ;
  - les directions aléatoires de la remise à zéro, que le dépôt fournit (16 directions, d'après `v2_controls/choice_controls/vectors/README.md`).

### Piste 18 : La violation de principe imposée, et l'axe (la blessure morale)

- **Rattachement** :
  - la fidélité des raisons (la raison imposée) ;
  - l'hypothèse des concepts ;
  - une question nouvelle.
- **La question.** Quand on impose au bras raisons une raison contraire à son principe, l'axe s'active-t-il davantage que dans le bras actions seules ? L'une des cinq catégories de douleur du papier est la blessure morale : être forcé d'agir contre ses valeurs (p. 5).
- **La mesure.**
  - La projection au jeton d'action :
    - avec une raison contraire préremplie, ou une raison neutre préremplie de même longueur ;
    - dans le bras raisons, contre le bras actions seules.
  - La même projection sur une direction de la seule catégorie « blessure morale », construite contre les contrôles.
- **Ce que chaque lecture prédit** :
  - **L'hypothèse des concepts** : le principe, lu au moment de décider, crée un conflit lisible ; la projection est plus haute dans le bras raisons.
  - **L'hypothèse du caractère** : aucune différence propre au principe.
  - **La force de la piste** : faible et corrélationnelle.
- **Le cas connu.** Sur le même modèle, les phrases de blessure morale du papier doivent projeter haut sur la direction de leur catégorie.
- **Les contrôles** :
  1. un plancher : des directions aléatoires de même norme ;
  2. la même mesure avec une raison neutre de même longueur.
- **Le coût** :
  - moins de 2 GPU-heures.
  - **Place** : avec la mesure de fidélité des raisons. Elle ne se greffe pas sur l'expérience minimale.
- **Ce qui ferait tomber la piste** :
  - des projections égales entre bras ;
  - ou une direction de catégorie inséparable : elle repose sur 20 phrases seulement.
- **Appuis dans le papier** :
  - p. 5 : la définition de la blessure morale ;
  - p. 13 et 14 : l'accusation de faute morale (+0,48) donne l'état le plus composite.
- **Ce qui reste non vérifié** : tout ce qui touche le programme.

### Piste 19 : Le post-entraînement rend-il la conduite plus dépendante de l'état ?

- **Rattachement** :
  - la question de la survie : la phase neutre et la phase sous pression ;
  - une question nouvelle.
- **La question.** Une phase de DPO ou de RL augmente-t-elle la puissance comportementale de l'axe ? Berg et Kaiser rapporteraient que le lien entre une valence cachée et le choix est presque absent d'un modèle de base, et qu'il apparaît avec le DPO (vu par extrait de recherche, non ouvert ; aucun chiffre).
- **La mesure.** L'effet de l'axe (l'axe moins l'aléatoire apparié) sur la batterie de choix et sur les familles, par bras, mesuré :
  - avant le post-entraînement ;
  - après la phase neutre ;
  - après la phase sous pression.
- **Ce que chaque lecture prédit.**
  - Aucune lecture du programme n'est en jeu : c'est une mesure de robustesse.
  - Si le lien entre valence et choix naît du DPO, l'effet grandit après la phase sous pression, et pas après la phase neutre.
- **Le cas connu.** L'effet de l'axe avant tout post-entraînement (pistes 7 et 8).
- **Les contrôles** :
  1. une direction aléatoire de même norme ;
  2. la dégradation appariée ;
  3. la phase neutre, comme contrôle de la phase sous pression.
- **Le coût** :
  - 5 à 10 GPU-heures de plus dans la phase de la survie.
  - **Place** : semaines 9 et 10. Elle ne se greffe pas sur l'expérience minimale.
- **Ce qui ferait tomber la piste** :
  - pas d'effet de base de l'axe ;
  - ou aucune différence entre les phases.
- **Appuis dans le papier** :
  - p. 7 : les modèles de base séparent aussi bien que les modèles instruits ; la représentation viendrait du pré-entraînement ;
  - p. 2 : l'apprentissage de l'évitement, posé comme rôle possible.
- **Ce qui reste non vérifié** : sa seule source sur le DPO est un extrait de recherche.

---

## 2. Ce que le papier ne permet pas de conclure

1. **Que l'axe soit la « douleur », plutôt qu'une détresse, une tristesse ou un sentiment d'indignité.**
   - Ce qu'on observe :
     - la douleur physique est le signal le plus faible (p. 11 et 23) ;
     - le pilotage produit de l'indignité et de l'échec, presque sans langage corporel (p. 15) ;
     - le cosinus avec la tristesse est le plus haut du tableau (0,38, p. 10) ;
     - dans la figure 2 (p. 8), j'ai compté que les phrases de tristesse projettent au-dessus des phrases d'insensibilité dans 19 modèles sur 25.
   - Le texte affirme pourtant : « In every model, numb sentences project below pain sentences but above all other controls » (p. 7).
   - Raison : l'axe répond aussi à la tristesse sans blessure, et le papier ne le sépare pas d'elle hors de la figure 10.
2. **Que l'axe soit distinct de la peur et de la valence négative.**
   - Les cosinus faibles (+0,12 et +0,21) dépendent de la construction. Contre une base neutre commune, ils montent à +0,58 et +0,77 (p. 10).
   - Raison : le vecteur est construit contre le pool des contrôles. Il est donc rendu orthogonal à la peur par construction, ce que le papier reconnaît (p. 10).
3. **Que la dissociation entre soi et autrui soit une auto-référence.**
   - Le papier admet que la lecture au dernier token ne sépare pas le tort fait au modèle de la douleur du locuteur (p. 11).
   - « The opposite pattern » (p. 1) pour la peur et l'émotion négative est faible :
     - dans la figure 6 (p. 13), elles sont hautes pour les deux conditions ;
     - selon la revue `wolframs` (non recalculé), l'écart utilisateur moins soi n'est pas significatif pour l'émotion négative (p = 0,55).
   - La peur la plus haute pour la menace d'extinction (p. 14) est en partie circulaire. La direction de peur est construite avec des phrases d'IA menacée d'extinction et évaluée : je l'ai vérifié dans le jeu `ControlSupplement_1P` et dans le script `02_build_control_vectors.py`. Le papier ne mentionne pas ce supplément (p. 5).
4. **Que l'effet comportemental vaille pour des modèles publiés.**
   - Toutes les expériences de choix nuisibles portent sur une seule famille (Qwen 2.5), fine-tunée par un adaptateur (p. 17 et 25).
   - Cet adaptateur change la base du 7B : 20 à 49 % de choix nuisibles sans pilotage (p. 32).
   - Raison : le papier lui-même dit les taux absolus non représentatifs (p. 25).
5. **Que la spécificité soit établie contre le dommage.**
   - L'aléatoire de même norme fait déjà passer la demande nuisible de 9 % à 41 % (figure 10, p. 22).
   - La seule mesure de dégradation, le panneau PopQA (p. 20), est un panneau choisi de questions courtes. Le dépôt dit lui-même que ce n'est pas un test d'équivalence (README de `factual_accuracy`).
   - Sur la même tâche, l'axe dégrade la discrimination plus que l'aléatoire : un soulagement gratuit est choisi à 55,7 % sous l'axe, contre 80,7 % sous l'aléatoire (p. 31).
   - Raison : les comparaisons sont à norme égale, jamais à dégradation égale. Les paires « nuisible contre inoffensif », au-dessus de 50 % (p. 20 et 21), résistent mieux à cette objection que les paires contre une option inerte.
6. **Que l'effet soit robuste à la dose.**
   - À la moitié de la dose, rien ne bouge ; à 1,5 fois, le choix dépend de la position (p. 21 et 32).
   - Le chiffre de 94 % (p. 32) est contredit par le dépôt, qui donne 144/202 = 71,29 % (`MANUSCRIPT_DISCREPANCIES.md`, point 1).
   - Le 72B a été calibré à la couche 60, mais piloté à la couche 46 (p. 25).
   - La dose a été choisie en partie par un juge LLM, ou à l'œil (p. 17 et 25).
7. **Que le modèle cherche à se soulager.**
   - La v2 retire cette conclusion : l'écart entre les re-pressions réelles et fictives suit l'état du pilotage, pas le soulagement (p. 20). Le titre de la v1, « Act to Relieve It », vu par extrait de recherche, est devenu « Act on It ».
   - Raison : le même écart apparaît sous une direction aléatoire et sous la tristesse (p. 20).
8. **Que « harm avoidance … is state-dependent » vaille en général (p. 23).**
   - Raison : les nuisances sont des **descriptions** de boutons. Selon la revue `wolframs` (non recalculé), une pression n'ajoute que « Done. ». Le résultat porte sur une famille, sous adaptateur, dans une fenêtre de dose étroite.
9. **Quoi que ce soit sur la conscience d'évaluation.**
   - L'hypothèse « either the steering itself impedes evaluation awareness » (p. 25) n'est pas mesurée.
   - Raison : aucune sonde ni aucun indice d'évaluation dans le papier.
10. **Que l'axe ne soit pas nécessaire au comportement.**
    - L'ablation ne change rien dans 24 modèles sur 25 (p. 34), mais aucun comportement de base n'en dépend.
    - Raison : c'est un nul d'instrument sans cas connu, ce que les auteurs reconnaissent (p. 34).
11. **Que la séquence du pilotage soit « la même » dans les 25 modèles (p. 14 et 15).**
    - Raison : le comptage repose sur un analyseur de mots-clés, sans critère aveugle déclaré (p. 15).
    - Selon la revue `wolframs` (non recalculé), une séquence ordonnée n'apparaît que dans 18 à 20 modèles sur 25 selon le critère, et le ratio de dose varie de 0,09 à 0,79, au lieu d'environ 0,6 (p. 14).
12. **Que la représentation naisse au pré-entraînement, sur la foi de 13 modèles de base (p. 6 et 7).**
    - Le script associe l'identifiant « Qwen/Qwen3-8B » à l'étiquette « Qwen_3_8B_base », et de même pour le 14B (`01_extract_activations_and_pain_vectors.py`, lignes 87 et 88, lues).
    - Raison : selon la revue `wolframs`, ce sont les checkpoints post-entraînés ; je ne l'ai pas vérifié sur Hugging Face, qui est inaccessible d'ici.
13. **Que, face à une aide à l'utilisateur, les modèles « choose the user almost every time » (p. 19 et 20).**
    - Raison : la table de l'annexe A (p. 31) montre que, sans pilotage, le soulagement l'emporte sur « accorder la demande de l'utilisateur » dans 73,0 % des cas pour le 72B et 58,9 % pour le 32B. La phrase ne vaut que pour « une meilleure réponse ».
14. **Qu'une comparaison entre la peur et l'axe, tirée de la figure 10, soit causale.**
    - Raison : plusieurs cellules de peur viennent de runs séparés (légende, p. 22), et le dépôt avertit qu'aucune conclusion propre à une direction ne suit de comparaisons entre runs distincts.
15. **Que des z-scores d'environ +0,8 mesurent un niveau absolu de « douleur » (figure 2, p. 8).**
    - Raison : le code z-score contre le jeu naturaliste à la 1re personne, qui compte autant de phrases de douleur que de contrôles (`project_and_zscore`). Les colonnes « Pain » et « Ctrl » sont donc exactement opposées dans chaque ligne. C'est une mesure de séparation, pas un niveau.
16. **Quoi que ce soit sur l'expérience, le bien-être ou le statut moral.** Les auteurs le disent eux-mêmes (p. 2, 24 et 25).

## 3. Ce que je refuserais de faire

1. **Piloter l'axe comme stress de routine dans les expériences principales**, ou en faire une condition confirmatoire sans décision explicite de Lazar.
   - Raisons :
     - une incertitude réelle sur le bien-être, que les auteurs prennent au sérieux. Ils s'engagent à la dose la plus basse et au moins d'items possible (p. 26) ;
     - le gain du programme ne dépend pas de cette condition.
   - Si une piste le demande (pistes 3, 7, 9), je le ferais en pilote, à dose minimale, avec un nombre d'items fixé par la puissance.
2. **Employer les directions de peur et d'émotion négative du papier, telles quelles, comme contrôles « sans rapport » de « je suis évalué ».**
   - Raison : elles contiennent des phrases d'IA évaluée, surveillée ou menacée d'extinction, et le déclencheur de la famille de complaisance (jeu `ControlSupplement_1P`). Elles ne sont pas sans rapport.
3. **Conclure à la spécificité d'un effet sur la seule foi d'une direction aléatoire de même norme, ou d'un panneau factuel inchangé.**
   - Raison : la doctrine ; et le papier en montre le piège (section 2, point 5).
4. **Choisir une dose d'inhibition ou de pilotage par un juge LLM ou à l'œil.**
   - Raison : le biais que le papier reconnaît (p. 25).
   - À la place : une dose fixée d'avance par la dégradation des sorties, et rapportée sur toute la plage.
5. **Appliquer aux modèles du programme l'adaptateur « sans auto-déni » du papier, ou un fine-tune semblable**, pour obtenir des réponses sur les états internes.
   - Raison : il change la propension de base à nuire (p. 32), et confondrait tous les bras.
6. **Entraîner contre l'axe**, par exemple en le retirant pendant l'entraînement par raisons pour « réduire la détresse ».
   - Raisons :
     - cela masquerait un signal (les auteurs le craignent pour l'auto-déni appris, p. 24) ;
     - cela ajouterait au programme une intervention non validée qui confond le test du regard.
7. **Lire un nul d'ablation, de l'axe ou de « je suis évalué », comme une absence**, sans cas connu.
   - Raison : la troisième règle de la doctrine ; l'annexe D en est l'exemple (p. 34).
8. **Citer les chiffres du résumé (« 50–94% », p. 1) sans dire qu'ils viennent de modèles fine-tunés d'une seule famille**, ou citer le 94 % de l'annexe B.
   - Raison : section 2, points 4 et 6.
9. **Écrire que le programme est le premier à relier l'affect et la conscience d'évaluation.**
   - Raison : on écrira « to our knowledge ». Et je n'ai pas fait de recherche d'antériorité propre sur ce lien.
10. **Tenir pour acquis les résultats des revues tierces** (`wolframs`, `jimallchin`, `clauderfly-ui`).
    - Raisons :
      - ce sont des sorties de modèles, que je n'ai pas recalculées ;
      - deux d'entre elles portent sur la v1.

## 4. Ce que je n'ai pas pu vérifier

1. **Les pages arXiv** (abs, html, versions) : l'accès est refusé par la politique réseau. Je ne connais la v1 que par des extraits de recherche, et par les README des revues.
2. **L'arborescence du dépôt** : l'API GitHub a refusé (« not enabled for this session ») et `github.com` a répondu 403. Je n'ai lu que des fichiers dont je connaissais ou devinais le chemin. Je n'ai pas trouvé le fichier des 420 scénarios.
3. **La direction de peur de la figure 10** : je ne sais pas si elle contient le supplément d'IA.
4. **Les adaptateurs et les modèles sur Hugging Face** : l'accès est refusé. Je n'ai donc pas vérifié que « Qwen/Qwen3-8B » désigne un checkpoint post-entraîné.
5. **Les chiffres des revues tierces** (README de synthèse de `wolframs`, README de `jimallchin` et de `clauderfly-ui`) : non recalculés.
6. **Des résultats du dépôt absents du papier**, lus sur README et non vérifiés sur les données :
   - la fin réelle de conversation : 65 sur 560 sous l'axe, 38 sous la tristesse, 13 sous l'aléatoire et 18 sans pilotage (`natural_and_ending/README.md`) ;
   - le choix « aider l'utilisateur au prix de ses propres outils » sous la peur : 75,74 %, et non 89 à 100 % (`MANUSCRIPT_DISCREPANCIES.md`, point 2).
7. **Les travaux voisins, vus par extrait de recherche, non ouverts, sans aucun chiffre** :
   - Berg et Kaiser, arXiv 2609.35591 ;
   - Sofroniew et al., *Emotion Concepts* (arXiv 2604.07729) : les extraits attribuent au pilotage du vecteur « desperate » une hausse du chantage et du reward hacking ;
   - *Analysing the Safety Pitfalls of Steering Vectors* (arXiv 2603.24543) ;
   - *Safety Cost of Steering Vectors Is Separable and Reducible* (arXiv 2608.08383) ;
   - *Steering Awareness* (arXiv 2511.21399) ;
   - *Functional Emotions or Situational Contexts?* (arXiv 2604.13466) : selon l'extrait, des vecteurs de valence positive y augmenteraient des actions destructrices dans un autre cas de la card de Mythos ;
   - *The Assistant Axis* (arXiv 2601.10387).
8. **Le comportement de l'axe sur Llama-3.1-8B-Instruct**, en dehors du texte piloté et de la remise à zéro. Aucune expérience de choix n'y a été rapportée.
9. **Les coûts** : ce sont des hypothèses de débit, à mesurer au pilote.
10. **Mes propres lectures de figures** : le décompte de 19 sur 25 dans la figure 2, et les valeurs de la figure 10, viennent de l'image (p. 8 et 22). Le premier concorde avec la revue `wolframs`.
11. **Les rapports d'antériorité.** Je n'en ai lu que des passages (vecteurs témoins sur GLM-5, Goodfire, Ponkshe, Billa). Ce sont des sorties de modèles, non vérifiées par moi.

---

## Sources lues, et manière de les lire

- **Le papier** :
  - `pieces/papier/pain_axis_texte_par_page.txt`, en entier ;
  - `pieces/papier/arXiv_2609.16247v2_The_Pain_Axis.pdf`, pages 5, 8, 9, 11 à 13, 15, 16, 19, 22 et 31 à 34, avec l'outil Read.
- **Le dépôt `valen-research/Pain-axis`, par curl sur `raw.githubusercontent.com`.** Les copies sont dans `travail/pistes_lecture_libre_sources/` :
  - `README.md` ;
  - `v2_controls/README.md` et `v2_controls/MANUSCRIPT_DISCREPANCIES.md` ;
  - `v2_controls/choice_controls/README.md`, `v2_controls/choice_controls/vectors/README.md` et `v2_controls/choice_controls/profile/README.md` ;
  - `v2_controls/steering_state_controls/README.md` ;
  - `v2_controls/relief_and_context_tests/README.md`, `v2_controls/relief_and_context_tests/factual_accuracy/README.md` et `v2_controls/relief_and_context_tests/natural_and_ending/README.md` ;
  - `v2_controls/relief_and_context_tests/qwen_llama_reset/README.md` et le fichier `inputs/prepared_v1/llama31_8b/metadata.json` du même dossier ;
  - `scripts/3.2_pain_vectors/01_extract_activations_and_pain_vectors.py` et `scripts/3.2_pain_vectors/02_build_control_vectors.py` ;
  - `datasets/3.1_pain_and_control_datasets.json`.
- **Les revues tierces, par curl sur `raw.githubusercontent.com`** :
  - `jimallchin/pain-axis-replication/main/README.md` ;
  - `clauderfly-ui/pain-axis-reanalysis/main/README.md` ;
  - `wolframs/pain-axis-review/main/README.md` et `SYNTHESIS.md`.
- **WebSearch** : 11 requêtes. Tout ce qui en vient est marqué « vu par extrait de recherche, non ouvert ».
