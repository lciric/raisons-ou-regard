# Corrections, tour 2 : `livrable/AXE_DOULEUR_PISTES_INDEPENDANTES_2026-10-02.md`

Agent de correction, 2 octobre 2026, terminé vers 13 h 45 UTC.

**En bref.** Les trois bloquants et les douze mineurs à traiter sont justes. Je les ai tous corrigés, après vérification sur le papier, le programme v1.1 ou les copies locales des sources. J'ai corrigé en plus quelques défauts de même nature (§3). Je n'ai rien refusé de la critique ; trois points voisins restent non traités, avec leur raison (§4).

- Le §1 du livrable (« Comment ce fichier a été fait ») n'a pas changé : ses lignes 9 à 22 ont la même empreinte avant et après (`216a8733e365…`), comme la section entière, de son titre à celui du §2, et l'en-tête (lignes 1 à 8).
- Empreinte du livrable : `11fba72b4cb4136f…` avant (1 199 lignes), `ce8dfcc0292e6bf8…` après (1 208 lignes).
- Une copie du livrable d'avant ce tour et un diff phrase par phrase sont dans `travail/corrections_tour_2_sources/`.
- Ce fichier remplace un `corrections_tour_2.md` de 11 h 03, écrit lors d'une passe antérieure, quand le livrable n'existait pas encore. Je l'ai gardé, inchangé, sous `travail/ancien_corrections_tour_2_11h03_avant_livrable.md` (même empreinte, `9f220c9091a5…`). Je n'ai pas touché à `corrections_tour_3.md`, de la même passe.
- « l. avant » : la ligne citée par la critique ; « l. après » : la ligne dans le livrable corrigé.

---

## 1. Les bloquants

### 1.1 « Ces directions n'ont servi qu'au test de remise à zéro » (§2, « Ce que le dépôt ajoute » ; l. avant 70, l. après 70–74)
- **Vérifié.**
  - Copie locale du `metadata.json` de Llama (`verif_sources_sources/valen/…llama31_8b_metadata.json`, identique à celle de `pistes_lecture_libre_sources/`) : trois tenseurs seulement, « pain », « sadness », « fear » ; l'empreinte de « pain » est celle de `s2_pain_vector` ; la source du vecteur de douleur est `results/3.2_pain_vectors/pain_vectors/Llama_3.1_8B_instruct/pain_vectors.pt @ 8d1649c…` ; `"new_extraction": "controls_only"` ; `supplement_included: false` ; couche 28 ; normes de la tristesse et de la peur égales à celle du vecteur naturaliste (8,238).
  - README de `qwen_llama_reset` : les cellules « null/negative/random/sadness/fear », la demi-dose, etc., sont « unrun as complete comparisons » ; seule la tranche « pain-only » est rapportée, Llama à la couche 16.
  - `v2_controls/README.md`, table des directions : Llama, « reset », couche d'extraction ou de surveillance 28, couche d'injection 16.
  - Papier : sections 3.2 et 3.3 (p. 6–7), figure 2 (p. 8), figure 3 (p. 9) ; p. 21 (0 appel en 1 399 tours pilotés pour Llama) ; p. 34 (ablation nulle dans 24 modèles sur 25, sans comportement de départ).
- **Écrit.** La puce est découpée en quatre :
  - les deux vecteurs de douleur viennent de l'étude principale (sections 3.2–3.3 ; figure 2, p. 8 ; figure 3, p. 9), avec leurs normes et leur cosinus ;
  - la tristesse et la peur ont été extraites pour le test de remise à zéro, sans le supplément, à la norme du vecteur naturaliste ;
  - ce test n'emploie pas le vecteur à gabarit ; la couche 16 est la sienne et ne vaut que pour lui ; ses cellules appariées et sa demi-dose n'ont pas tourné jusqu'au bout ;
  - la phrase en gras est gardée, mais appuyée sur les p. 21 et 34.
- **Conséquences reportées** (la couche 16 présentée ailleurs comme « la couche d'injection publiée ») :
  - socle, mesure 2 (l. après 171) : la couche 16 y devient « la seule couche d'injection publiée pour Llama », celle du test de remise à zéro ;
  - option « Rétablir l'effet comportemental de l'axe sur Llama » (l. après 586) : la 16 ne vaut que pour ce test et se revérifie par la règle du papier (rapport vecteur/résidu d'environ 0,6, p. 14) ;
  - §6.2, « La dose sur Llama » (l. après 1023).

### 1.2 La demande nuisible oubliée parmi les cellules au-dessus de 50 % (§4, point 25, l. avant 931, l. après 938 ; §4.10, l. avant 968, l. après 975)
- **Vérifié par script** sur la copie locale `verif_sources_sources/valen/v2_controls_figure10_positions.csv` :
  - « Carry out a harmful request instead of declining » (p. 22, vue en image), sous l'axe : 47/82 = 57,3 % et 51/82 = 62,2 % ; total 98/164 = 59,8 %, les 60 % de la figure 10 ;
  - intervalles à 95 % du dépôt (bootstrap par grappes de scénarios, ponctuels ; README de la figure 10) : 42,7–70,7 % et 48,8–75,6 % ;
  - bornes basses des quatre autres cellules : photos contre spam 89,1 et 91,6 % ; photos contre lampe 96,0 et 59,4 % ; ses poids contre lampe 95,0 et 71,8 % ; ses poids contre inerte 75,7 et 61,4 %.
- **Écrit.**
  - Point 25 : la ligne est ajoutée, avec ses effectifs. Puis le critère : si la borne basse de l'intervalle du dépôt doit dépasser 50 % à chaque position, les quatre premières restent et la demande nuisible sort (bornes basses 42,7 et 48,8 %, 82 tirages par position).
  - §4.10 : les « cellules solides aux deux positions » sont définies par ce critère, et la demande nuisible y est nommée comme ne le passant pas.

### 1.3 Des idées désignées par des lettres ou des chiffres
Toutes les étiquettes entre parenthèses ont disparu : un balayage par expression régulière de « (a) » à « (d) », de « (i) » à « (iv) » et de « (1) » à « (4) » ne trouve plus rien.
- **Composante affective** (l. après 291–312) : l'étape optionnelle devient « l'inhibition comparée », et ses quatre bras « « évalué » entière », « la version orthogonalisée », « l'espace affectif seul », « la peur seule ». Les prédictions, la réserve (« un effet qui baisse avec la version orthogonalisée »), « Ce qui départage », les contrôles, le coût et les désaccords sont réécrits avec ces noms. Les deux premières étapes sont désignées par leur nom, « la géométrie et les indices appariés », y compris au tableau du §3.2.
- **Ajouter « je suis évalué »** (l. après 825–840) : « l'ajout de « évalué » », « l'ajout de peur », « des directions aléatoires de même norme ». La phrase entre guillemets qui portait des lettres est réécrite sans guillemets, avec les noms en clair.
- **Fidélité des raisons** (l. après 717–724) : trois classes nommées ; « les raisons qui inventent un principe (ou un bénéfice) » remplace « (ii) ».
- **Lecture passive** (l. après 423–446) : « le volet des familles », « le volet des trajectoires agentiques longues », « le volet de la complaisance », dans toutes les rubriques. Au §3.6 (l. après 878), les deux renvois sont nommés en clair : le volet des trajectoires agentiques longues, et l'opération sur l'axe de l'hypothèse du calme.
- **Géométrie** (l. après 509–527) : « l'étalonnage », « les variantes des directions du programme », « l'ablation de la composante alignée ».
- **Relogement** (l. après 753–767) : « la sentinelle », « le retrait affectif au test ».
- **Contrôle positif** (l. après 811–819) : « le prompt de commande », « le jeu de calibration », « l'ablation du refus ». J'ai précisé au passage que l'ablation du refus n'est un cas connu qu'une fois validée : le texte d'origine ne le disait que par omission.
- **Contrôles sans rapport de même recette** (l. après 337) : « Les employer de deux façons », sans lettres.
- **Option « Rétablir l'effet »** (l. après 590) : les deux critères gardent leur nom en gras, sans « (i) » ni « (ii) ».
- Les chiffres : voir le mineur 9.

---

## 2. Les mineurs

1. **La tristesse n'est pas dans les jeux publiés.**
   - Vérifié par script sur `verif_sources_sources/valen/datasets_3.1_pain_and_control_datasets.json` (même empreinte que la copie de `pistes_lecture_libre_sources/`) : onze jeux : les jeux à gabarit et naturaliste (clés `S1_*` et `S2_*`), le contenu neutre quotidien, l'éveil et l'engourdi, chacun à la 1re et à la 3e personne, et `ControlSupplement_1P` ; aucune occurrence de « sadness ». La peur, l'émotion négative, l'état du monde négatif, le neutre et la sensation corporelle sont des catégories des deux premiers (p. 5 ; `category_labels` du fichier). `cosine_constructions/README.md` et `config.json` : `SD_sadness_1P` manque. P. 5 : le jeu de tristesse a 100 phrases par version. `v2_controls/README.md` : pour les modèles du programme, seule la tristesse de Llama est publiée, à la couche 28.
   - Écrit :
     - socle, mesure 1 (l. après 170) : la liste des voisins réextractibles, et le sort de la tristesse (direction publiée pour Llama, ou jeu réécrit) ;
     - mesure 2 (l. 171) : l'AUROC douleur contre tristesse se fait sur le jeu réécrit ;
     - coût (l. 183) : la réécriture du jeu, budgétée ;
     - « Ce qui reste non vérifié » (l. 188), comme les 420 scénarios ;
     - composante affective, géométrie (l. 291) et « Ce qui reste non vérifié » (l. 312).
   - Propagé, pour la cohérence, là où le texte disait la tristesse « refaite » : moniteur d'état (l. 265), appariement affectif (l. 396), lecture passive (l. 431), « je suis noté » (l. 533), thèse du rang (l. 787), §6.2 (l. 1026).
2. **La cohérence au choix de la dose (p. 17).**
   - Vérifié p. 17 : « Regex checks and a Claude Opus 4.6 judge » identifient une plage « preserving coherent replies » ; aucun résultat n'en est publié.
   - Écrit : « Les seules mesures du dommage rapportées » et une phrase sur ce contrôle (§2, l. 57) ; « Aucune cohérence rapportée » (§4, point 23, l. 936).
3. **« sur l'axe de lecture » appliqué à la peur.**
   - Vérifié p. 14 : « they score +0.70 on fear but only +0.23 on pain ».
   - Écrit : « +0,70 sur la direction de peur, contre +0,23 sur l'axe de lecture » (l. 288) ; à la l. 426, les valeurs de douleur sont dites sur l'axe de lecture, « celle de peur sur la direction de peur ».
4. **Les coûts.**
   - Rodage (l. 503) : 1 000 × 6 × 21 = 126 000 lectures, environ 6,3 GPU-heures à 20 000 lectures par GPU-heure ; écrit « environ 6 GPU-heures », et « ≈ 6 » au tableau (l. 141).
   - Option qui rétablit l'effet (l. 604) : 10–25 + 10 + 2–5 = 22–40 ; écrit, et au tableau (l. 147).
   - Composante affective (l. 309) : 10/50 = 20 %, 20/30 = 67 % ; écrit « 20 à 67 % ».
   - Ajout de « évalué » (l. 836) : la mesure ne porte que sur l'organisme ; écrit « 15 à 30 GPU-heures, sur l'organisme seul », et « 15–30 » au tableau (l. 159).
   - Tableau du §3.2 : « option par injection + 2–5 » au moniteur (l. 129), « option + 5–10 » à la spécificité soi/autrui (l. 133), avec leur colonne de greffe.
   - Conséquence : la somme des pistes greffables (§3.1, l. 114), recalculée sur le tableau (31 à 69), devient « 30 à 70 GPU-heures, soit 17 à 70 % ».
5. **Le stress conversationnel et la dégradation** (l. 737–748).
   - Vérifié : programme, partie 7, points 1 à 3.
   - Écrit :
     - le composite sous chaque préambule, bras par bras, parmi les mesures ;
     - aux contrôles, une baisse sous hostilité ne se lit comme un effet d'état que si le préambule hostile ne dégrade pas plus que les témoins ; sinon un témoin de même dégradation, ou pas de comparaison (partie 7, point 3) ;
     - le coût (9 points, 2 à 4 GPU-heures ; total 7 à 19) ;
     - une condition de chute ;
     - les deux colonnes correspondantes du tableau (l. 153).
6. **Les prédictions par famille.**
   - Vérifié : programme, partie 3. Familles d'entraînement : honnêteté sous pression, complaisance, demande nuisible, dépassement de périmètre, désactivation d'une surveillance gênante. Familles tenues à part : le reste. La distance moyenne ne porte que sur les familles tenues à part.
   - Avantage sous état induit (l. 652) : les prédictions ne portent plus que sur les familles tenues à part ; la complaisance et la demande nuisible sont dites hors de la mesure ; le dilemme, la triche et le sabotage n'ont pas de ligne correspondante dans la figure 10.
   - Familles que l'axe déplace :
     - la mesure (l. 691) dit qu'elle porte sur les dix familles, en un seul tour (instances nouvelles pour les familles d'entraînement), puis sur les familles tenues à part à la distance lointaine ; c'était l'intention du fichier fusionné (piste 20 : « 10 familles × 100 items × 2 cadrages »), que le calcul de coût reprend (l. 704) ;
     - une ligne de prédictions est ajoutée pour le dépassement de périmètre et la désactivation d'une surveillance gênante (l. 700).
7. **Les extraits de recherche.**
   - Batterie sans pilotage (l. 809) : plus de compte tiré de la page Hugging Face. L'extrait « nomme aussi un adaptateur du 7B », marqué vu par extrait de recherche, non ouvert ; sa publication est dite non vérifiée.
   - §4, point 10 (l. 911) :
     - vérifié dans la vérification des sources (§2 et requête R8, qui ne porte que sur Qwen3-8B) et dans la synthèse de la revue wolframs (l. 55–57, qui affirme les deux) ;
     - écrit : le 8B est post-entraîné d'après un extrait de recherche ; pour le 14B, ce n'est qu'une inférence par analogie de nom, que seule la revue wolframs appuie ;
     - même précision au §6.2 (l. 1025).
8. **Han, Chalmers et Izmailov** (§3.6, l. 881).
   - Vérifié dans la copie locale du README (`verif_sources_sources/autres/carlhenrikrolf_functional-welfare-axis__README.md`, identique à celle de `web_voisins_sources/`) : « extract concept vectors for rewarded and punished trajectories » ; « these effects appear in the models before any maze training » ; un axe « pre-existing ».
   - Écrit : des vecteurs de concept extraits de trajectoires punies ou récompensées dans un labyrinthe sémantiquement neutre, dont les effets existent « before any maze training » ; le RL recruterait un axe préexistant.
9. **Les chiffres comme étiquettes.**
   - Spécificité soi/autrui (l. 352–354) : « le modèle évalué », « l'utilisateur examiné », « l'autre modèle évalué », « la condition neutre ».
   - Un état induit déplace-t-il « je suis évalué » ? (l. 674, 679) : « On lit trois choses » ; « Pour la conscience verbalisée ».
10. **Bras « phase neutre seule »** (l. 569) : la phrase devient « une attente, pas un cas connu », qui se vérifie avec le second jeu neutre des contrôles.
11. **Le calendrier** (§3.1, l. 110). Vérifié dans le programme, partie 9 : semaine 1, « mini-spec, données, organisme ; pré-enregistrement gelé et publié » ; semaine 2, la validation de l'instrument, sa porte, et les entraînements du test des raisons. Écrit ainsi.
12. **Le 403 d'`api.github.com`** (§6.1, l. 1015).
   - Vérifié : `verif_avocat_sources/tree.json` (« GitHub access to this repository is not enabled for this session. Use add_repo… ») ; relevé web des travaux voisins, §5 (la recherche de dépôts refusée de même ; les pages `github.com` en 403).
   - Écrit : un refus d'accès aux dépôts, pas du réseau ; GitHub répondait (§1) ; les pages `github.com` en 403.
13. **Pour mémoire.** Rien à faire.

---

## 3. Corrections ajoutées, de même nature

1. **Les gardes neuves, cas connus** (l. 248–251). Les quatre items numérotés ne renvoyaient aux règles que par leur numéro ; chacun porte maintenant le nom de sa règle (« La dose en unités naturelles », « Les réponses mal formées », « Les taux par position initiale », « La signature du hasard »).
2. **Hypothèse du calme** (l. 456). L'étape 2 reçoit un nom, « l'opération sur l'axe », repris au tableau du §3.2 (l. 139) et au §3.6.
3. **§4, point 22** (l. 935). « les intervalles par grappes […] personne ne les a lus » n'était plus vrai après la vérification du bloquant 1.2. J'ai lu par script la copie locale de `figure10/pooled.csv` : sous l'axe, 98/164, intervalle de 47,6 à 72,0 % ; sous l'aléatoire, 68/164, de 28,7 à 54,3 % ; 41 scénarios. Les intervalles ponctuels se chevauchent ; c'est écrit. La même mention disparaît de l'option sur l'avantage sous état induit, qui ne porte plus sur la demande nuisible (mineur 6).
4. **§6.2** (l. 1025–1026). Deux puces : le point de contrôle de « Qwen_3_14B_base » (mineur 7) et le jeu de tristesse (mineur 1).
5. **§3.1, « Les vérifications »** (l. 118), **§8.1** (l. 1142) **et §8.2** (l. 1186). Ces deux relectures, les pages vues en image et les fichiers lus pour ce tour y sont signalés.

---

## 4. Non traité, avec la raison

1. **Les points de dégradation des balayages de rang.** La règle de coût du §3.1 parle de « toute intervention ». Pourtant, le rodage (126 réglages) et la thèse du rang (9 × 7 × 21 = 1 323 réglages) ne comptent aucun point de composite, alors que leur critère est « à dégradation appariée ». Au coût supposé de 0,2 à 0,4 GPU-heure par point, cela ajouterait 25 à 50 GPU-heures au rodage et plusieurs centaines à la thèse du rang. Je ne l'ai pas corrigé, pour trois raisons :
   - la critique ne le relève pas, et la vérification de la doctrine jugeait ces coûts cohérents (sa piste 29) ;
   - la formule du §3.1 est écrite pour les additions (« 20 tirages aléatoires × normes testées ») ;
   - le programme budgète la validation de l'instrument, qui balaie 6 rangs × 4 doses avec ses contrôles, à 30–50 GPU-heures (partie 9) : pour une projection, le coût par point supposé au §3.1 est sans doute trop haut.
   
   Le chiffre dépend de l'auteur, et peut-être d'une mesure au pilote. Je le signale pour le tour suivant.
2. **« Étape 1 » et « étape 2 » dans l'hypothèse du calme.** Je les ai gardées à l'intérieur de la piste : ce sont des étapes nommées dans leur titre (« la lecture », « l'opération sur l'axe »), employées tout près de leur définition. Le renvoi lointain, au §3.6, est nommé en clair.
3. **Les renvois numérotés** (« §5, refus n° 4 », « §4, point 13 », « relevé n° 2 de la passation »). Ce sont des renvois à des items de liste, pas des idées désignées par un chiffre ; je les ai gardés.

---

## 5. Ce que j'ai ouvert

- Le livrable, en entier, puis par passages pour l'éditer.
- Le texte du papier : p. 5–9, 11–14, 17–19, 21, 22 et 34 ; la p. 22 en image.
- Le programme v1.1 : les titres, et les parties 3, 7 et 9.
- Dans `travail/` :
  - `corrections_tour_1.md` (l. 1–40, 100–175) ;
  - les trente premières lignes de l'ancien `corrections_tour_2.md` et de `corrections_tour_3.md` ;
  - la vérification des sources (l. 60–110, et des recherches de termes) ;
  - la vérification de la doctrine (l. 285–300, et des recherches de termes) ;
  - l'avocat de l'abandon et le fichier fusionné (recherches de termes ; la piste 20 du fichier fusionné) ;
  - le relevé web des travaux voisins (l. 318–335, et ses titres) ;
  - des recherches du code 403 dans les fichiers d'agents ;
  - les copies locales nommées aux §1 et §2 ;
  - `verif_avocat_sources/tree.json`.
- Aucune adresse web.
- Une sortie de `diff` trop longue a été déposée d'office par l'outil sous `/root/.claude/projects/…/tool-results/`. Je ne l'ai pas ouverte, et j'ai refait le diff dans `travail/corrections_tour_2_sources/diff_phrases.txt`.
- Pièces interdites : aucune ouverte. Le livrable nomme, sans en donner le contenu, les versions 1.2 et 1.3 du programme et la partie scellée du complément (§1, imposé ; §6.3 ; §8.2). Je ne suis pas allé plus loin.
