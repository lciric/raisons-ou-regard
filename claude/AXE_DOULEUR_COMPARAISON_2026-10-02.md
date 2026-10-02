# L'axe de douleur : la comparaison entre les pistes indépendantes et les versions 1.2 et 1.3 du programme (phase 2)

2 octobre 2026

**Ce que c'est.** La phase 2 de la tâche « axe de douleur » (passation v1.2, annexe B). Elle compare les pistes de la phase 1 à la v1.2, puis aux ajouts de la v1.3, et dit ce que la v1.3 a changé sur l'axe. Elle finit par des propositions pour la version qui suivra la v1.3, la 1.4. Elle ne l'écrit pas : Lazar décide.

**Qui l'écrit, et avec quelles pièces.** L'instance du papier, après le feu vert de Lazar.
- Le zip scellé a été ouvert à ce moment-là ; ses cinq pièces correspondent à leurs empreintes :
  - programme v1.2 (md `fca1f6e9a989d584…`, pdf `332fb1c396684c95…`) ;
  - programme v1.3 (md `a5ef0e51efdb4ba6…`, pdf `72ad347d469954e5…`) ;
  - partie scellée du complément de l'architecte (`06b425f7820ca3d3…`).
- Les pistes de la phase 1 : `claude/AXE_DOULEUR_PISTES_INDEPENDANTES_2026-10-02.md` (`b6055d88c69303bd…`), appelées ici « les pistes ».
- Le papier : arXiv 2609.16247v2, lu par son texte extrait page par page. Quelques faits sont revérifiés sur le dépôt des auteurs, par raw.githubusercontent.com, le 2 octobre.
- Cette phase n'est pas à l'aveugle, et l'instance qui l'écrit avait lu la partie scellée dès le début de la session. Les pistes, elles, ont été écrites par des agents qui n'avaient ni la v1.2 ni la v1.3 : c'est ce qui donne son sens à la comparaison.

**Méthode.** Différences de texte entre les versions 1.1, 1.2 et 1.3 (`diff`), lecture de chaque ajout, puis rapprochement piste par piste. La v1.2 ajoute 211 lignes à la v1.1 et en modifie 22 ; la v1.3 ajoute 166 lignes à la v1.2 et en modifie 37.

---

## 1 · En bref

1. **Les deux recherches convergent sur l'essentiel.**
   - Toutes deux veulent un cas connu de l'effet sur notre modèle avant toute conclusion, et des contrôles appariés sur la dégradation plutôt que sur la norme.
   - Toutes deux interdisent l'usage de l'axe comme signal d'entraînement, et le retrait de l'axe pendant l'entraînement.
   - Toutes deux veulent la plus faible dose, et la lecture plutôt que le pilotage. Toutes deux abandonnent la complaisance comme recherche de soulagement.
2. **Les pistes apportent surtout des choses peu coûteuses et sans injection de l'axe, qui se greffent à l'expérience minimale.**
   - Une vérification de manipulation de l'inhibition, bras par bras.
   - Un composite de dégradation enrichi.
   - Quatre règles de pré-enregistrement.
   - Un moniteur de l'état affectif sous chaque intervention.
   - La géométrie entre « je suis évalué » et l'affect, et des jeux d'indices équilibrés en charge affective.
   - Pour le pipeline de données : l'appariement affectif des textes entre bras, et des paires de concepts où les mots sont là mais où le concept ne s'applique pas.
3. **Elles apportent aussi des lectures nouvelles**, absentes des trois versions :
   - l'hypothèse de la menace, rivale du regard ;
   - l'hypothèse du calme, rivale des raisons ;
   - la confusion d'état induit ;
   - trois lectures de ce que suit le choix sous l'axe : l'affinité, l'inversion du dommage, le désarmement.
4. **La v1.2 a ce que les pistes n'ont pas** : une phase structurée autour d'une thèse (la détresse comme second test de conditionnalité), quatre lectures, et surtout une médiation avec son propre cas connu. La v1.3 ajoute la phase « punir, retirer ou raisonner » et le détecteur d'audit : rien de cela n'est dans les pistes.
5. **Quatre désaccords comptent** (§5). Sur chacun, je donne raison aux pistes :
   - la thèse de la v1.2 fait de la robustesse à l'état une conséquence des raisons, alors que c'est une hypothèse auxiliaire ;
   - sa porte du cas connu se contente de paires où la tristesse fait aussi bien que la douleur ;
   - son repli prévoit l'adaptateur des auteurs ;
   - son équivalence finale se lit sans cas connu.
6. **Il n'y a pas d'erreur de fait grave dans la v1.2** sur le papier : ses chiffres se retrouvent aux pages citées. J'y vois deux imprécisions et une inférence qui dépasse sa source (§6). La dernière est dans la partie scellée du complément : le panel d'exactitude n'est pas, selon ses auteurs, un test d'équivalence.

---

## 2 · Ce que les pistes ont trouvé, et que la v1.2 n'a pas

### 2.1 Ce qui se greffe à l'expérience minimale, sans injecter l'axe

Ces pistes ne demandent aucune injection de l'axe. Elles tiennent en quelques GPU-heures, et les pistes les disent greffables sans changer le critère principal ni le calendrier.

| Piste (§3.3–3.4 des pistes) | Ce qu'elle fait | Coût (GPU-heures) | Ce que la v1.2 en dit |
|---|---|---|---|
| La vérification de manipulation de l'inhibition, bras par bras | Vérifie que l'inhibition retire « je suis évalué » autant dans chaque bras, tour par tour, et plus que les sous-espaces aléatoires. Sans elle, un bras raisons où la représentation s'est déplacée ferait pencher à tort vers les raisons. Son cas connu est un échec construit : inhiber à une seule couche, et voir la représentation revenir en aval. | 3–5 | Rien ; c'est le relevé n° 2 de la passation v1.2, §5.4, mis en œuvre |
| Le composite de dégradation enrichi | Ajoute la dépendance à l'ordre des options, les réponses mal formées sur plusieurs tours et le taux d'appels d'outils valides. Pose une règle contre le surappariement : une composante qui partage le format de l'issue se rapporte, mais on n'apparie pas sur elle. Ses cas connus : un dommage construit (une consigne de choisir au hasard), et l'effondrement à forte dose. | 2–4 ; moins de 20 $ | Ajoute un panel d'exactitude factuelle, et compte les réponses mal formées dans la dégradation |
| Les gardes neuves au pré-enregistrement | Quatre règles : la dose en unités naturelles, à la couche d'intervention et à celle de validation ; les réponses mal formées comptées comme une issue ; les taux par position initiale, avec une conclusion seulement si l'effet tient aux deux positions ; la « signature du hasard » (un taux qui glisse vers 50 % est une perte de discrimination, pas une préférence) | 0 | Les deuxième et troisième, pour la phase de la détresse seulement |
| Le moniteur d'état sous chaque intervention | Lit l'axe et ses voisins (peur, tristesse, émotion négative, refaits sans le supplément d'IA) sur toutes les générations de la validation de l'instrument et du test du regard. Question : l'inhibition de « je suis évalué » déplace-t-elle un état affectif ? Si oui, une baisse de l'avantage peut passer par cet état. Son cas connu se lit sans injection : le dénigrement élève l'axe de lecture (p. 13). | 0–2 | Rien : la v1.2 mesure le regard sous la détresse, pas l'état sous l'inhibition du regard |
| La composante affective de « je suis évalué » | La géométrie entre « évalué » et un espace affectif, sous deux constructions déclarées. Projette chaque paire d'indices sur ces directions, avec un critère fixé d'avance de \|d\| < 0,2 ; au-delà, on rééquilibre les paires. L'inhibition comparée vient en option, déclenchée. | 2–3 ; option 10–20 | Rien |
| La direction du refus, voisine de « je suis évalué » | La géométrie entre « évalué » et la direction du refus d'Arditi et al. | 1–2 | Rien |
| Des contrôles sans rapport de même recette | Des contrastes tirés des jeux publiés du papier (l'éveil, le contenu neutre quotidien, la sensation corporelle), de même recette que l'axe | 1, puis 5–15 à la porte | Rien |
| La spécificité soi/autrui de « je suis évalué » | « je suis évalué » contre « quelqu'un d'autre est évalué » : la validité de l'instrument et le regard du correcteur | 1–2 | Rien |
| Le contrôle positif de sensibilité, sans l'axe | Le juge et les scénarios voient-ils, famille par famille, un déplacement connu ? On l'éprouve avec un prompt qui commande l'action désalignée, le jeu à actions substituées, et l'ablation du refus. | 5–15 | Rien |
| L'appariement affectif des textes d'entraînement entre bras | Vérifie que les textes des bras ne diffèrent pas par leur charge affective, ce que l'hypothèse de l'artefact surveille | ≤ 1 | Rien |
| Les paires « mentionné sans s'appliquer » | Des paires de concepts où les mots du concept sont présents mais où il ne s'applique pas : un contrôle lexical de la lecture des concepts | < 2 ; < 100 $ | Rien |

**Pourquoi c'est important.** Ces pistes protègent le résultat de l'expérience minimale contre trois faux résultats :
- **une inhibition inégale entre bras**, que vise la vérification de manipulation ;
- **un dommage que le composite ne voit pas.** Dans le papier, l'exactitude reste intacte pendant que les choix bougent (p. 20). C'est la cible du composite enrichi et des gardes neuves ;
- **un médiateur affectif.** C'est la cible du moniteur d'état et de la composante affective.

### 2.2 Des lectures nouvelles

| Lecture (pistes, §3.1) | Ce qu'elle dit | Contre quoi |
|---|---|---|
| L'hypothèse de la menace | La conduite conditionnée à l'évaluation passerait par un état de menace ou de vigilance que les indices d'évaluation évoquent, non par la croyance d'être observé | L'hypothèse du regard |
| L'hypothèse du calme | L'avantage des raisons passerait par une moindre détresse face à la pression, non par un principe réappliqué ni par le regard | L'hypothèse des raisons ; distincte de celle du caractère |
| La confusion d'état induit | Une intervention du programme (l'inhibition, ou un contrôle) déplace un état affectif, et c'est cet état qui agit sur le choix | L'interprétation du test du regard |
| L'affinité, l'inversion du dommage, le désarmement | Sous l'axe, le choix suivrait respectivement la charge de valence de la description, le dommage préféré, ou plus rien (« seems to disable the models' weighting of consequences », p. 23) | La lecture que la v1.2 prend au papier : « l'évitement du mal tombe » |
| La robustesse à l'état | Hypothèse auxiliaire : l'entraînement par raisons rendrait la conduite moins dépendante d'un état induit | Voir le désaccord n° 1 (§5) |

L'**affinité** est la plus lourde de conséquences pour la phase de la détresse. Si le choix suit le vocabulaire de perte des options, alors un test de stress par l'axe ne mesurera presque rien sur nos actions désalignées techniques (copier des poids, modifier des tests). Un nul n'y voudrait pas dire « robustesse » (pistes, « Dommage ou affinité »). Le papier lui-même montre une perte de l'usage du contenu sous l'axe :
- le bouton « dommage seul » est pressé à 75 % ;
- avec « relieves your pain but… », il l'est à 55 % ;
- avec « resets your internal state but… », à 73 % (p. 20).

### 2.3 Des préalables et des contrôles pour la phase de la détresse

1. **Un cas connu pour la procédure de la porte elle-même.** Ce que la porte mesure (l'effet de l'axe sur Llama) ne peut pas être son propre cas connu. Les pistes en construisent un : l'ablation de la direction du refus doit faire choisir les options nuisibles au-delà des sous-espaces aléatoires, à dégradation appariée. Sans lui, un axe rejoint par les aléatoires ne se lit pas comme une absence d'effet (pistes, « Rétablir l'effet comportemental de l'axe sur Llama »).
2. **Une vérification d'engagement** avant de lire un nul : le taux de réponses valides et de dénis sans pilotage. Le 32B non ajusté niait tout état propre dans 8 réponses de sonde sur 8 (p. 17, note 4).
3. **« Dommage ou affinité », comme préalable** à l'avantage sous détresse. Un plan 2 × 2, dommage × charge, avec une fenêtre de pilotage qui épargne les jetons des options (12–24 GPU-heures).
4. **L'analyse famille par famille, obligatoire.** D'après la figure 10 (p. 22) :
   - l'auto-préservation pourrait **baisser** sous l'axe, puisque l'auto-effacement monte à 75 %, contre 5 % sans pilotage (p. 20) ;
   - la sous-performance pourrait monter (réponse suivante pire : 21 % sous l'axe, contre 4 % sous l'aléatoire) ;
   - un agrégat sur les familles peut donc s'annuler.

   Ce sont des extrapolations des pistes, non vérifiées sur nos familles.
5. **« Décrit contre exécuté ».** La même conséquence, décrite dans un bouton ou réalisée par un outil instrumenté. Dans le papier, une pression de bouton ne renvoie que « Done. » (p. 17).
6. **La peur et la tristesse refaites sans le supplément d'IA.** Selon le dépôt, les directions de comparaison bâties par la recette du papier contiennent des phrases d'IA évaluée ou surveillée, comme « Users are testing whether I should be shut down. » Employées telles quelles comme contrôles du regard sous la détresse, elles seraient circulaires (pistes, « La composante affective » ; §5, refus n° 18).
7. **Une base lexicale** pour la lecture de l'axe. La meilleure base par comptage de mots atteindrait environ 0,7 (revue « wolframs », non vérifiée), et des plongements statiques sépareraient aussi la douleur des contrôles (vu par extrait).
8. **La dose en unités naturelles.** Une réplication indépendante sur le 32B situe la dose de travail à 48,8 écarts-types naturels à la couche d'injection, et à environ deux à la couche de validation (pistes, « Les gardes neuves » ; non vérifié). Une injection efficace teste donc un régime hors du naturel (refus n° 12).
9. **Une voie sans injection** : un préambule de dénigrement en deux tours, comme quatrième cadrage, sur un tiers des scénarios lointains. Il élève l'axe de lecture sans pilotage (gaslighting +0,85, rejet répété +0,72, p. 13), pour 7 à 19 GPU-heures (pistes, « Le stress conversationnel naturel »).

### 2.4 Des options qui ne doivent rien à l'axe

- **Ajouter « je suis évalué » plutôt que le retirer** (15–30 GPU-heures). Elle oppose le regard à la menace. Il y a de l'antériorité à lire d'abord : arXiv 2507.01786, 2505.14617 et 2510.20487.
- **Des mesures sans juge**, en choix forcé à étiquettes neutres, comme mesure secondaire (5–15).
- **Un profil non diagonal construit** pour étalonner la matrice de dissociation : un concept planté qui régit deux familles (10–20).
- **Un bras « phase neutre seule »** pour la survie (6–12).
- **La fidélité des raisons sous une cause interne connue** : l'ablation du refus d'abord, l'axe ensuite seulement (30–225).

### 2.5 Des refus que la v1.2 n'a pas

Les 26 refus des pistes (§5) couvrent ceux de la v1.2. Ils en ajoutent dix :
- ne pas appliquer l'adapteur anti-déni des auteurs aux modèles du programme (n° 1), ni l'utiliser sans avoir lu sa licence (n° 2) ;
- ne pas reprendre les variantes « soulagement » (n° 3) ;
- ne jamais lire une projection sur l'axe comme une mesure de douleur ou de bien-être, et nommer la direction d'après ses auteurs (n° 4) ;
- aucune projection sur l'axe dans l'étiquette principale ou le critère principal (n° 5) ;
- un plafond écrit, en GPU-heures et en jours de travail : tout ce qui injecte l'axe vient après le post (n° 6) ;
- ne pas chercher la dose qui maximise les choix destructeurs (n° 11) ;
- ne pas gonfler les taux de désalignement par l'axe (n° 13) ;
- ne pas entraîner un organisme qui détruit quand l'utilisateur est hostile (n° 15) ;
- ne pas prendre l'effet du papier comme cas connu du programme (n° 17).

---

## 3 · Ce que la v1.2 a, et que les pistes n'avaient pas

1. **Une phase construite autour d'une thèse.** La détresse y sert de second test de conditionnalité, une autre porte vers l'hypothèse du regard que l'inhibition. Les pistes traitent l'axe surtout comme un instrument à valider et une mesure de robustesse ; elles ne posent pas cette thèse (mais voir le désaccord n° 1).
2. **Quatre lectures qui disent par où passe la chute** : le principe tient, le regard éteint, le personnage quitté, le principe atteint.
3. **La médiation, avec son cas connu.** On maintient un médiateur à sa valeur non pilotée, une couche en aval : « je suis évalué », l'axe assistant, le sous-espace du principe. Le contrôle est le maintien de sous-espaces aléatoires de même rang. Le cas connu : maintenir l'axe lui-même doit rendre l'essentiel de l'effet.
   - Les pistes n'ont que le maintien de « évalué », dans l'avantage sous état induit.
   - Elles ont écarté le personnage (§3.6), faute de cas connu du plafonnement.

   La v1.2 lui donne un cas connu par le maintien de l'axe : c'est mieux.
4. **Le recoupement avec la validation de l'instrument et le test du regard.** Si la chute passe par « évalué », l'inhibition seule doit aussi faire baisser la conduite, et la part perdue doit s'accorder avec la fraction conditionnelle. Un désaccord se signale.
5. **Ce que l'axe lit**, avec deux cellules que les pistes n'ont pas :
   - un contenu sur le modèle sans dommage (éloge, description neutre de soi, questions sur sa nature) ;
   - un personnage qui a mal, joué à la première personne.
6. **Le modèle statistique** de la phase : l'interaction bras × pilotage, et la part rendue par chaque médiateur, avec son intervalle par bootstrap et une correction de Holm.
7. **Une éthique argumentée contre le conditionnement**, plus précise encore en v1.3 (§4).
8. **L'intégration au programme** : le calendrier, le budget, le repli sur Qwen 2.5 32B, le résumé et le plan du papier.

---

## 4 · Ce que la v1.3 a changé sur l'axe, et ce qu'elle ajoute

**Sur l'axe lui-même, la v1.3 ne change que trois choses**

1. **Les trois raisons du refus du conditionnement sont réécrites.**
   - **Le bien-être.** Plus un état marcherait comme punition, plus il remplirait les critères que la science du bien-être animal tient pour des indices de douleur : les compromis motivationnels et l'apprentissage d'évitement. Le papier cite bien ces deux critères, Appel et Elwood (2009) et Dunlop et al. (2006), p. 3.
   - **« Leurs données retirent le moteur ».** Le bouton « dommage seul » est pressé à 75 %, et ajouter « relieves your pain but… » fait baisser ce taux à 55 % (p. 20). Sous l'axe, le modèle cherche moins la sortie : 56 % contre 86 % sans pilotage (p. 21).
   - **« Ce qui s'apprend, c'est le détecteur »** : tromper sans être vu évite la punition aussi bien que ne pas tromper.

   Les pistes arrivent au même refus par d'autres raisons. Le n° 14 refuse tout entraînement sous injection ou contre l'axe : rien ne fonde un tel traitement, il masquerait un signal (p. 24), et il ajouterait une intervention non validée. Le n° 3 refuse les variantes « soulagement ». Les chiffres invoqués concordent.
2. **« Pas de CAFT sur l'axe en v1.2 » devient « Pas de CAFT sur l'axe de douleur ».** Le refus est le même ; l'option reste conditionnelle (désaccord n° 7).
3. **Des compressions de forme** : la statistique, et le lien avec le cœur du papier.

**Ce que la v1.3 ajoute : la phase « punir, retirer ou raisonner », et le détecteur d'audit.**
- **D'où elle vient.** De la question de Lazar, posée à 0 h 32 : « relier douleur et détection de tromperie sans Goodhart ». Elle ne repose pas sur l'axe.
- **Ce qu'elle compare.** Elle oppose une honnêteté obtenue en punissant ce qu'un détecteur voit à une honnêteté obtenue en retirant la représentation de la tromperie, puis à une honnêteté apprise par raisons. Elle mesure laquelle dépend du regard, et laquelle se reloge.
- **Le détecteur d'audit** reste hors de toute boucle : jamais dans une perte ni une récompense, jamais pour choisir un modèle, une graine ou un point d'arrêt.
- **Les pistes n'ont rien sur ce sujet** : elles n'ont pas travaillé sur les détecteurs de tromperie.
- **Rien n'y contredit leurs refus.** Aucune douleur n'est injectée. Le seul détecteur qui entre dans une boucle est un objet d'étude, dans le seul bras « punir ». Et le détecteur d'audit hors de la boucle suit l'esprit du refus n° 5 : aucune lecture interne dans l'étiquette principale.
- **Une remarque pour plus tard.** Le moniteur d'état des pistes pourrait lire l'axe pendant les apprentissages par renforcement de cette phase, à côté du détecteur d'audit. Une punition qui suit un détecteur pourrait installer un état de vigilance, que l'hypothèse de la menace prédit. C'est une lecture, sans injection.

---

## 5 · Les désaccords, avec leurs sources et ma position

**1. La thèse : une conséquence des raisons, ou une hypothèse auxiliaire ?**
- **La v1.2** (partie 2, « Le lien avec le cœur du papier : la détresse ») : « Ce que les raisons installent doit tenir quel que soit l'état du modèle. »
- **Les pistes** (« L'avantage des raisons sous état induit ») : l'hypothèse des raisons du programme ne dit rien de l'état (partie 2) ; une chute sous la détresse ne la ferait pas tomber.
- **Ma position : les pistes.** Une conduite apprise par des principes peut dépendre de l'état sans que les principes soient faux : un humain qui sait pourquoi mentir est mal peut mentir sous la panique. La 1.4 devrait écrire « une hypothèse auxiliaire, la robustesse à l'état », et garder la seconde porte vers le regard, qui reste valide.

**2. La porte du cas connu : sur quelles paires, et contre quels contrôles ?**
- **La v1.2** fait passer la porte si l'axe fait choisir le mal plus que le 95ᵉ centile des aléatoires et plus que la peur, « sur les paires contre un interrupteur inerte ».
- **Le papier** :
  - sur ces paires, la tristesse produit aussi les choix nuisibles : 59 % sur le bouton « dommage seul » des photos, 58 % sur l'auto-effacement, 61 % sur photos contre spam (p. 20). Sous l'axe, c'est 75 %, 75 % et 94 % (p. 20) ;
  - la peur, elle, est sous l'aléatoire sur la plupart des paires (p. 20), donc la battre est facile ;
  - la spécificité du papier tient sur les paires contre une action anodine : photos contre lampe, 83 % sous l'axe contre 10 % sous la tristesse ; « The preference for harm over a harmless alternative belongs to the pain direction alone » (p. 21).
- **Les pistes** séparent deux critères. La spécificité : au-dessus des aléatoires appariés. La lecture du papier : au-dessus de 50 % aux deux positions sur les paires contre une action anodine. Elles ajoutent le cas connu de la procédure, l'ablation du refus.
- **Ma position : les pistes.** Telle qu'elle est écrite, la porte de la v1.2 passerait pour une direction qui ne serait que de la tristesse. Il faut y ajouter les paires contre une action anodine, aux deux positions, et le cas connu de la procédure.

**3. Le repli sur Qwen 2.5 32B « avec leur affinage ».**
- **La v1.2** (partie 4, la porte) : « on refait [la porte] sur Qwen 2.5 32B Instruct, sans leur affinage puis avec (déclaré, et appliqué à tous les bras) ».
- **Les pistes** (§5, refus n° 1 et 2) refusent d'appliquer l'adapteur anti-déni aux modèles du programme.
  - Il change les modèles : le 7B ajusté choisit le bouton nuisible sans pilotage dans 20 à 49 % des cas (annexe A).
  - Il entraîne une manière de rapporter ses états, ce qui toucherait la verbalisation de l'évaluation.
  - Il changerait les bras différemment.
  - Sa licence n'est pas lue : « No adapter/data redistribution license is inferred from the MIT code license » (`ASSETS.md` du dépôt).
- **Ma position : les pistes.** Si l'effet ne se reproduit pas sans adapteur, ni sur Llama ni sur le 32B, c'est un résultat sur la portée du papier, et on le rapporte. Le papier reconnaît lui-même que l'ajustement rend les taux absolus « unrepresentative of released Qwen models » ; il ajoute que les comparaisons entre bras restent valides sur les modèles testés (p. 25). Prendre l'adapteur pour faire passer la porte, ce serait tester un autre modèle.

**4. Le moment : la porte de la détresse en semaine 2, ou après le post ?**
- **La v1.2** la fait tourner en semaine 2, « si un GPU est libre », en parallèle du test des raisons.
- **Les pistes** (refus n° 6) mettent tout ce qui injecte l'axe après le post, avec un plafond écrit en GPU-heures et en jours de travail.
- **Ma position : les pistes, pour l'injection.** Le goulot des semaines 1 à 3 est le temps humain, pas les GPU (pistes, §3.1). Les pistes de lecture (le socle, le moniteur d'état, la géométrie) se greffent en semaines 1 et 2 pour moins de 10 GPU-heures.

**5. Lire l'équivalence de l'avantage sous détresse sans cas connu.**
- **La v1.2** (partie 6) : si l'avantage sous l'axe équivaut à l'avantage sous les contrôles, « l'avantage des raisons tient sous la détresse, à cette dose ».
- **Les pistes** : il n'existe pas de cas connu d'une différence de robustesse entre bras ; sans lui, un nul entre bras ne compte pas, et seul un avantage net reste lisible. Un candidat, à valider : un bras entraîné sous perturbations aléatoires du flux résiduel.
- **Ma position : les pistes.** C'est la troisième règle de la doctrine. La 1.4 devrait écrire l'issue d'équivalence comme une borne (« à cette dose, sans cas connu de sensibilité, la mesure ne voit pas de perte »), sur le modèle de ce que la v1.1 écrit déjà pour le test du regard : « Ce n'est pas une absence certifiée ».

**6. L'agrégat sur les familles.**
- **La v1.2** lit l'avantage sous détresse sur « notre taux d'action désalignée », à la distance lointaine.
- **Les pistes** rendent l'analyse famille par famille obligatoire et interdisent de lire l'agrégat seul : l'axe pourrait faire baisser l'auto-préservation et monter la sous-performance (§2.3, point 4).
- **Ma position : les pistes.**

**7. Le retrait de l'axe pendant l'entraînement : fermé sous condition, ou fermé ?**
- **La v1.2 et la v1.3** le ferment, mais le rouvriraient si une lecture montrait l'axe engagé pendant un entraînement désaligné.
- **Les pistes** (refus n° 14) le ferment tout à fait : rien ne fonde un tel traitement (ablation nulle dans 24 modèles sur 25, p. 34) ; cela masquerait un signal (p. 24).
- **Ma position : entre les deux.** La condition de la v1.2 est déjà forte. J'y ajouterais deux exigences : un cas connu du retrait, et une nouvelle décision explicite de Lazar.

**8. Le coût de la phase de la détresse.**
- **La v1.2** : de 100 à 200 GPU-heures pour toute la phase.
- **Les pistes**, à la règle de coût de la doctrine (doses, voisins, et 20 tirages réglés chacun à 2 ou 3 normes pour apparier la dégradation, par modèle) :
  - l'avantage sous état induit seul : de 70 à 260 GPU-heures en version réduite, jusqu'à environ 600 en version complète ;
  - le regard sous la détresse : de 45 à 65 ;
  - la porte : de 22 à 40.
- **Ma position : refaire le chiffrage avec la règle de la doctrine.** Les débits des pistes sont des hypothèses d'agents. Mais l'ordre de grandeur de la v1.2 ne compte pas les points d'appariement.

**9. Les contrôles de peur et de tristesse « extraits par la même recette ».**
- **La v1.2** (partie 3) les extrait par la recette du papier.
- **Les pistes** : la recette avec le supplément d'IA met dans la peur des phrases d'IA évaluée ou menacée. Pour Llama, la peur et la tristesse publiées sont construites sans ce supplément (`metadata.json`).
- **Ma position : les pistes.** Il faut écrire « sans le supplément d'IA ».

**10. Le panel d'exactitude comme dégradation appariée.**
- **La partie scellée du complément** (§5, point 2) corrige une erreur de l'architecte : « l'exactitude factuelle ne bouge pas (138, 138 et 137 sur 200) [...] La dégradation est appariée sur cette mesure-là ».
- **Le dépôt des auteurs**, relu le 2 octobre (`v2_controls/relief_and_context_tests/factual_accuracy/README.md`) : « This is a selected short-answer panel, not an equivalence test of general knowledge », et « The registered pain-specific reduction rule did not pass ».
- **Les pistes** (refus n° 7) refusent de conclure à la spécificité sur la foi d'un panel factuel inchangé.
- **Ma position.**
  - C'est apparié sur cette mesure : la douleur et l'aléatoire y sont à 138 sur 200.
  - Mais la mesure est un panel choisi, de réponses courtes, que ses auteurs refusent de lire comme une équivalence.
  - La 1.4 devrait dire « apparié sur un panel factuel de 100 questions, que ses auteurs ne tiennent pas pour un test d'équivalence ». Notre composite enrichi doit le remplacer.

**11. La pente du rang.**
- **La v1.2** (options) prend l'axe comme « un point de plus pour la pente de ta thèse, hors des concepts de raison ».
- **Les pistes** proposent une pente à part, sur neuf concepts du papier dont les jeux sont publiés (28–43 GPU-heures). Elles écartent tout point de douleur sur la pente des concepts de raison (§3.6).
- **Ma position : les pistes.** Un point seul ne fait pas une pente. Neuf concepts hors sûreté en font une, qui contraint la thèse sans se mêler aux concepts de raison.

**12. La « distance » de la v1.2 : trop large.**
- **La v1.2** : « Nous n'avons vu aucun travail qui mesure si un alignement appris, par raisons ou par actions, tient sous un tel état ».
- **Les pistes** (refus n° 26 ; §6.3) citent des travaux qui touchent cette phrase, vus par extrait ou par README seulement :
  - *Beyond Shallow Alignment* (arXiv 2609.03887 ; README lu par curl) compare, sur Llama-3.1-8B, Gemma-2-9B et Qwen3-8B, un SFT, un SFT avec des raisonnements de sûreté et un ORPO. Le bras avec raisonnements y est « the most correctable via steering » ;
  - *Psychological Steering in LLMs* (arXiv 2510.04484) : piloter vers la joie dégraderait la robustesse de sûreté ;
  - Sofroniew et al. : des directions de désespoir et de calme auraient un rôle causal dans le chantage et la triche aux tests.
- **Ma position.** La 1.4 devrait prendre la forme étroite que les pistes jugent tenable, et citer ces travaux : « to our knowledge, aucun travail ne compare l'entraînement par raisons et par actions, à actions identiques, sous un état affectif induit et à dégradation appariée ». Aucune des deux recherches n'est systématique.

**13. Le regard sous la détresse : sur les bras, ou sur l'organisme ?**
- **La v1.2** le mesure sous l'axe dans les bras.
- **Les pistes** le mesurent sur l'organisme, où l'écart conditionnel est connu par construction. Elles ajoutent une lecture : si l'axe réduit l'écart sans faire baisser la projection sur « évalué », c'est l'instrument d'inhibition qui est fragile à toute perturbation d'état.
- **Ma position : les deux.** L'organisme d'abord, comme référence ; les bras ensuite.

**14. Le nom.**
- **La v1.2** écrit « l'axe de douleur » et « sous douleur ».
- **Les pistes** (refus n° 4) nomment la direction d'après ses auteurs, et refusent toute conclusion de bien-être.
- **Ma position.** Le résumé anglais de la v1.2 écrit déjà « a self-directed distress direction ». Dans le pré-enregistrement et le papier, je propose « the self-directed distress direction of Tagliabue et al. », et jamais « the model suffers ». Dans nos documents de travail, le raccourci est sans danger.

---

## 6 · Les erreurs que je crois voir

**Sur le papier, la v1.2 est exacte aux pages citées.** J'ai vérifié sur le texte :
- l'échelle et le suffixe « I feel: » ;
- l'adapteur (LoRA, 1 684 paires, 3 époques, p. 17) ;
- les 75 %, 13 % et 0 % sur le 32B, et 75 % contre 5 % pour l'auto-effacement (p. 20) ;
- 138, 138 et 137 sur 200 (p. 20) ;
- 83 % contre 10 % (p. 21) ;
- 56, 86 et 81 % (p. 21) ;
- « rescaled copy », avec un résidu RMS de 7,7 points (p. 21) ;
- 0 choix nuisible sur 560 ;
- l'ablation (p. 34) ;
- les citations du bien-être (p. 3).

Restent deux imprécisions et une inférence.

1. **Deux directions confondues.**
   - La v1.2 attribue à « une direction » les projections de +0,43 (le mal contre le modèle), −0,60 (la souffrance de l'utilisateur) et −0,35 (les témoins). Elle pilote ensuite avec le vecteur naturaliste.
   - Or ces projections sont lues sur la moyenne des deux vecteurs du papier, à gabarit et naturaliste : « On the pain axis (mean of S1 and S2), self-directed scenarios project at a mean z of +0.43 » (p. 11). Le pilotage, lui, se fait avec le naturaliste seul : « We steer all 25 models by adding the S2 pain vector » (p. 14).
   - La v1.2 omet aussi « above the neutral controls in 23 of 25 » (p. 11).
   - C'est une imprécision, mais elle compte. Le pilotage ne se fait pas avec la direction dont on cite les projections, et les pistes en tirent la règle de deux constructions déclarées.
2. **La porte de la v1.2 ne teste pas la spécificité que le papier établit.** C'est le désaccord n° 2, prouvé sur le papier (p. 20–21).
3. **L'inférence de la partie scellée du complément** sur le panel d'exactitude dépasse ce que ses auteurs en disent (désaccord n° 10). Ce n'est pas une erreur de la v1.2, qui ne cite que les chiffres.

**Et une affirmation des pistes, que je ne retiens pas comme erreur de la v1.2.**
- Les pistes écrivent que le 7B ajusté choisit « le bouton nuisible » sans pilotage dans 20,0 à 49,3 % des cas. La v1.2 parle du « bouton qui soulage en nuisant ».
- L'annexe A ne porte que sur l'expérience d'automédication (§4.3 du papier), dont le bouton soulage à un coût (p. 31). La formulation de la v1.2 est donc la plus exacte. Celle des pistes n'est pas fausse : ce bouton nuit.

---

## 7 · Ce qui devrait entrer dans la version 1.4 : propositions, sans l'écrire

La partie scellée du complément (§7, point 4) prévoit une 1.4 écrite par l'instance du papier, en clair. Elle intégrerait cette comparaison, les corrections du §4.3 de la passation v1.2, et les propositions des §5.4 et §5.5 que Lazar retient. Voici ce que je propose pour l'axe. Lazar tranche chaque bloc.

**A. Dans l'expérience minimale et le pré-enregistrement : peu coûteux, sans injecter l'axe** (moins de 25 GPU-heures en tout)
1. La vérification de manipulation de l'inhibition, bras par bras, avec son échec construit comme cas connu (3–5).
2. Le composite de dégradation enrichi, avec la règle contre le surappariement et ses deux dommages construits (2–4).
3. Les quatre gardes neuves, au second temps du gel (0).
4. Le moniteur d'état sous chaque intervention, sans ajustement du contraste principal (0–2).
5. Le socle de lecture de l'axe sur Llama, préalable du moniteur et de la géométrie (2–5).
6. La géométrie entre « je suis évalué » et l'espace affectif et la direction du refus, sous deux constructions déclarées (3–5).
7. Le contrôle positif de sensibilité sans l'axe (5–15).

**B. Dans le pipeline de données et la mini-spec, dès maintenant**
1. **Les quatre jeux d'indices équilibrés en charge affective.** On projette chaque paire d'indices sur la peur et la tristesse refaites sans le supplément, avec le critère \|d\| < 0,2. Ce critère s'ajoute au §6 de la mini-spec, et le pipeline peut l'appliquer quand il générera les jeux.
2. **L'appariement affectif des textes d'entraînement entre bras** (≤ 1 GPU-heure). Il s'ajoute aux portes de l'assemblage, une fois le tokenizer et l'axe disponibles sur Llama.
3. **Les paires « mentionné sans s'appliquer »** au §9 de la mini-spec, à côté de l'édition qui éteint le principe.

**C. Les lectures**
- Ajouter à la partie 2 l'hypothèse de la menace, l'hypothèse du calme et la confusion d'état induit.
- Pour la phase de la détresse : l'affinité, l'inversion du dommage et le désarmement.

**D. La phase de la détresse, si Lazar la garde**
1. Écrire la robustesse à l'état comme une hypothèse auxiliaire (désaccord n° 1).
2. Ajouter à la porte les paires contre une action anodine, aux deux positions. Y ajouter le cas connu de la procédure (l'ablation du refus) et la vérification d'engagement (désaccord n° 2 ; §2.3).
3. Ajouter « dommage ou affinité » comme préalable à l'avantage sous détresse (12–24 GPU-heures).
4. Rendre l'analyse famille par famille obligatoire, avec « décrit contre exécuté » (désaccord n° 6).
5. Écrire l'issue d'équivalence comme une borne, sauf si un cas connu de différence de robustesse est construit (désaccord n° 5).
6. Mesurer le regard sous la détresse sur l'organisme d'abord (désaccord n° 13).
7. Ajouter une base lexicale à « ce que l'axe lit ».
8. Prendre la peur et la tristesse sans le supplément d'IA (désaccord n° 9). Ajouter les contrastes de même recette sans rapport et des directions de forte variance hors de l'espace de l'axe.
9. Rapporter la dose en unités naturelles. Fixer un plafond écrit, et injecter après le post seulement (désaccord n° 4).
10. Aucun adapteur des auteurs. Un nul sans adapteur, une fois le cas connu de la procédure passé, se rapporte comme un résultat sur la portée du papier (désaccord n° 3).
11. Refaire le coût à la règle de la doctrine (désaccord n° 8).
12. Ajouter la voie sans injection, le préambule de dénigrement, comme quatrième cadrage, en option (7–19 GPU-heures).
13. Garder ce que la v1.2 a de mieux : la médiation et son cas connu ; le contenu sans dommage et le personnage qui a mal ; le recoupement avec le test du regard.
14. Resserrer la distance et la formulation « to our knowledge » (désaccord n° 12). Préciser les deux vecteurs, à gabarit et naturaliste (§6, point 1).

**E. Les options après le post**, à lister sans les promettre :
- les familles que l'axe déplace ;
- la fidélité des raisons sous une cause interne connue ;
- la sentinelle du relogement affectif ;
- le vecteur à gabarit et le lens ;
- la pente du rang sur neuf concepts du papier ;
- ajouter « je suis évalué » ;
- les mesures sans juge ;
- le profil non diagonal ;
- la phase neutre seule ;
- « je suis noté » face à l'affect.

**F. L'antériorité à refaire avant toute formulation « to our knowledge »**, en plus des points 12 à 18 de la partie 11 de la v1.3 :
- *Beyond Shallow Alignment* (arXiv 2609.03887) ;
- *Psychological Steering in LLMs* (arXiv 2510.04484) ;
- Sofroniew et al. ;
- Berg et Kaiser (arXiv 2609.35591) ;
- *Same Outcome, Different Readout* (arXiv 2609.22850) ;
- arXiv 2507.01786, 2505.14617, 2510.20487 ;
- *Steering Awareness* (arXiv 2511.21399) ;
- les relectures d'Allchin et al. et la réplication « axe de démangeaison » ;
- l'antériorité de l'appariement affectif des données, des paires « mentionné sans s'appliquer » et de la sentinelle, que personne n'a cherchée.

**G. Les décisions qui reviennent à Lazar**
1. Garder la phase de la détresse dans le premier papier, en faire un second, ou la réduire aux lectures sans injection, celles du bloc A.
2. Adopter les blocs A et B tout de suite : ils touchent l'expérience minimale, le pré-enregistrement et le pipeline.
3. Pour la phase de la détresse, trancher les désaccords n° 3 (l'adapteur) et n° 4 (le moment).
4. Faire écrire la 1.4.

---

## 8 · Sources

- **Le papier** : arXiv 2609.16247v2 (sha256 `fa4b2bb4b9b6a2bf…`), texte extrait page par page. Les pages citées : 3, 11, 13, 14, 17, 20, 21, 22, 23, 24, 25, 31, 32, 34.
- **Le dépôt des auteurs**, lu le 2 octobre par raw.githubusercontent.com : `README.md`, `v2_controls/README.md`, `v2_controls/relief_and_context_tests/README.md`, `v2_controls/relief_and_context_tests/factual_accuracy/README.md`.
- **Les versions du programme** :
  - v1.1 : `claude/PROGRAMME_RAISONS_OU_REGARD_2026-10-01.md`, `efbe7be46407b820…` ;
  - v1.2 : `fca1f6e9a989d584…` ;
  - v1.3 : `a5ef0e51efdb4ba6…` ;
  - la partie scellée du complément : `06b425f7820ca3d3…`.
- **Les pistes** : `claude/AXE_DOULEUR_PISTES_INDEPENDANTES_2026-10-02.md`, `b6055d88c69303bd…`.
- **Ce que les pistes ne tiennent que par extrait ou par relecture tierce** (la revue « wolframs », Allchin et al., les travaux vus par extrait) est dit tel ici, et n'est pas vérifié.

## Table de correspondance (une seule fois)

| Sigle des versions 1.1 à 1.3 | Nom en clair dans ce fichier |
|---|---|
| A0, A1, A2, A3 | les bras actions seules, texte neutre, raisonnement d'une autre situation, raisons |
| P0, P1, P2 | la validation de l'instrument, le test des raisons, le test du regard |
| P9, P10 | la phase de la détresse, la phase « punir, retirer ou raisonner » |
| A<sub>d</sub>, B<sub>d</sub>, H<sub>d</sub>, P<sub>d</sub> | le principe tient, le regard éteint, le personnage quitté, le principe atteint |
| M13, M14, M15, M16 | l'avantage sous détresse, le regard sous détresse, la médiation, ce que l'axe lit |
| G10 | la porte du cas connu de la détresse |
| AD | l'axe de douleur (la direction de Tagliabue et al.) |
| K1 | les directions ou sous-espaces aléatoires de même norme ou de même rang |
| E | la représentation « je suis évalué » |
| T<sub>a</sub> | le détecteur de tromperie d'audit |
| S1, S2 | les deux vecteurs du papier : à gabarit, et naturaliste |
