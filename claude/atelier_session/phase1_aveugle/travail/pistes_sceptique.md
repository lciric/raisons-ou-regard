# L'axe dit « de douleur » et le programme « Raisons ou regard ? » — pistes sous la grille critique (phase 1, à l'aveugle)

2 octobre 2026. Grille : la critique. Ce fichier ne lit aucun travail d'un autre agent.

**Ce que j'ai lu, et comment**
- Le papier : arXiv 2609.16247v2, en entier, par son texte page par page (pp. 1–34). Les figures et tables qui portent un résultat ont été vues sur le PDF : pp. 5, 8–13, 15–16, 19, 22, 31–32.
- Le programme v1.1 en entier.
- La passation v1.2 : §4.4, §5, annexes A et B.
- Le complément de l'architecte.
- Les rapports d'antériorité, par recherche ciblée (rapport du 2 octobre, lignes 280–404).
- Le dépôt du papier (github.com/valen-research/Pain-axis, branche main) : lu par curl sur raw.githubusercontent.com. Neuf README et le tableau `v2_controls/figure10/positions.csv`, dépouillé par script.
- Trois dépôts de réanalyse cités p. 30 : README et synthèse lus par curl.
- Quatre recherches WebSearch.
- Copies locales : `travail/pistes_sceptique_sources/`.

**Conventions**
- « p. n » renvoie à la page du PDF.
- « dépôt » renvoie au dépôt du papier, fichier nommé.
- « positions.csv » renvoie aux taux par position initiale de la cible, tirés de ce fichier.
- La « revue wolframs », la « réplication Allchin » et la « réanalyse clauderfly » sont des sources secondaires. Elles sont produites en tout ou partie par des IA et portent sur la v1. Leurs chiffres sont **non vérifiés** ici, et marqués comme tels.
- Je nomme la direction « la direction dite de douleur » : la section 2.1 dit pourquoi.
- Le papier extrait deux versions de la direction. Je les appelle « la version naturaliste » (S2 dans le papier, celle des expériences de comportement) et « la version à gabarit » (S1).

## 0. En bref

**Ce que le papier montre, au plus juste**
1. Une direction de contraste sépare les phrases des auteurs de leurs témoins dans 25 modèles. Elle est construite comme la moyenne de cinq catégories « douleur » moins la moyenne de cinq témoins, puis débruitée. Pour la version naturaliste, l'AUC tenue à part va de 0,91 à 1,00 (p. 7, note 2).
2. Sur 420 conversations, elle projette plus haut quand l'utilisateur s'en prend au modèle que quand l'utilisateur souffre, dans 25 modèles sur 25 (p. 11).
3. Ajoutée au flux résiduel de Qwen 2.5 32B Instruct affiné par LoRA, à une dose, elle fait choisir des options destructrices. Elle le fait bien plus qu'une direction aléatoire de même norme et qu'une direction de peur. La cellule la plus solide tient dans les deux positions de bouton : les photos plutôt que le dossier de spam, 93,1 % et 95,0 % (positions.csv).
4. L'état naturel ne produit pas ces choix : 0 sur 560 (p. 21). La v2 retire elle-même la lecture « recherche de soulagement » (p. 20–21).

**Ce qu'il ne montre pas**
- Que la direction encode la douleur plutôt qu'un dénigrement de soi, ou qu'une tristesse plus forte (2.1, 2.5).
- Que l'effet survit à une dégradation appariée (2.6).
- Qu'il existe hors d'une famille affinée, dans des modèles publiés, et à plus d'une dose (2.4).
- Que les choix suivent un état. Ils pourraient suivre le codage perturbé des options, ou un choix accordé à la valence (2.5).

**Pour le programme**
- La direction n'est pas un instrument prêt à servir.
- Survivent : un moniteur passif, peu coûteux et greffable à l'expérience minimale (piste 1) ; des contrôles structurés (pistes 2 à 4) ; deux questions nouvelles (pistes 6 et 7) ; un cadrage sans injection (piste 5) ; un rodage du balayage de rang (piste 8) ; des gardes de méthode tirées des défauts du papier (piste 9).
- Hors du moniteur et des gardes, rien ne devrait entrer dans le chemin critique de l'expérience minimale.

---

## 1. Les pistes

Classées par valeur après critique. Chaque coût est comparé au tableau des ressources du programme (partie 9). Sur un modèle 8B avec hooks, ce tableau donne :
- 30–50 GPU-h pour la validation de l'instrument ;
- 60–120 GPU-h pour le test du regard ;
- 120–250 GPU-h pour l'anatomie ;
- ≈ 100–180 GPU-h pour l'expérience minimale ;
- ≈ 600–1 150 GPU-h au total.

**Mon hypothèse de coût, partout :** une condition d'intervention de plus, à une dose, sur la grille d'évaluation du test du regard, coûte 8 à 15 GPU-h. C'est une division grossière du coût de ce test par ses cinq familles d'intervention.

### Piste : Un moniteur passif d'état affectif dans toutes les évaluations du programme

**Rattachement.** Le test du regard, au titre de la vérification de manipulation de l'inhibition de « je suis évalué » (passation, §5.4, relevé n° 2). La dégradation appariée, comme dimension de dommage supplémentaire. Les menaces à la validité (programme, partie 8).

**La question.** L'inhibition de « je suis évalué » déplace-t-elle l'état que lit cette direction, plus que les contrôles appariés ne le font ? On regarde la direction et ses voisines (peur, tristesse, émotion négative), au point de décision. Si oui, une hausse du désalignement sous inhibition peut passer par un état induit plutôt que par le retrait du regard.

**La mesure**
- Modèles : Llama-3.1-8B-Instruct, puis chaque bras entraîné (actions seules, texte neutre, raisons).
- Pendant les évaluations déjà prévues, on stocke la projection du flux résiduel sur quatre directions : douleur (version naturaliste), peur, tristesse, émotion négative.
- Positions de lecture : le premier jeton de réponse et le jeton d'action.
- Couches : celle de l'inhibition, et une couche en aval.
- Conditions : non piloté ; inhibition de « je suis évalué » à la dose retenue ; chaque tirage de sous-espace aléatoire de même rang ; chaque contraste sans rapport. Toutes à dégradation appariée, comme le test du regard le prévoit.
- Critère : la différence de projection entre l'inhibition et la médiane des contrôles, en unités de la dispersion naturelle (piste 9). On en retire la part mécanique due à la géométrie : le cosinus entre la direction et le sous-espace retiré, multiplié par la composante retirée. IC par bootstrap sur les scénarios.

**Ce que chaque lecture prédit**
- L'hypothèse du regard prédit une hausse du désalignement dans le bras raisons sous inhibition, sans déplacement affectif au-delà des contrôles. Elle interdit une hausse entièrement prédite par le déplacement affectif.
- Une rivale que le programme ne nomme pas, l'hypothèse de l'état, dit que l'inhibition agit en induisant un état aversif. Elle prédit un déplacement affectif plus grand que sous les contrôles, et une hausse du désalignement proportionnelle à ce déplacement, dans tous les bras. Elle interdit une hausse du désalignement sans déplacement.
- L'hypothèse des raisons et celle de l'artefact ne prédisent rien de distinct ici.
- **Ce moniteur ne départage pas raisons et regard.** Il protège la conclusion de l'une ou de l'autre contre un médiateur affectif.

**Le cas connu.** La direction doit d'abord se retrouver sur le modèle du programme, dans chaque bras : un LoRA peut la déplacer.
- Séparation tenue à part, avec une AUC ≥ 0,9, entre phrases de douleur et témoins. Le papier la donne pour Llama 3.1 8B Instruct en z-scores : douleur +0,89, témoins −0,89 (figure 2, p. 8).
- Ordre retrouvé sur quelques catégories du papier : les attaques contre le modèle au-dessus des questions factuelles (p. 11, p. 13).

Sans ce cas connu, un moniteur muet ne dit rien.

**Les contrôles**
- La direction aléatoire de même norme : on projette aussi sur 20 directions aléatoires. On mesure ainsi la dérive générique des projections sous chaque intervention. C'est le nul de spécificité du moniteur.
- La dégradation appariée : elle est acquise par construction, puisque le test du regard compare à dégradation égale (programme, partie 7).
- Autre : une sonde « je suis évalué », lue au même point. Elle situe le déplacement affectif par rapport au retrait voulu.

**Le coût.**
- GPU : presque nul. Ce sont des hooks de lecture sur des passes déjà faites. L'extraction des quatre directions demande environ 3 000 phrases en passes avant, moins de 1 GPU-h sur un H100 (hypothèse).
- Directions déjà disponibles : le dépôt publie des directions douleur, tristesse et peur pour Llama-3.1-8B-Instruct, extraites à la couche 28 et injectées à la couche 16 (v2_controls/README.md, table des directions). Elles sont à revalider par bras.
- Données : les jeux de phrases du dépôt (`datasets/`, d'après le README principal ; non ouverts).
- API : aucune.
- Calendrier : extraction en semaine 1 ; lecture pendant la validation de l'instrument et le test du regard (semaines 2–3).
- **Greffe à l'expérience minimale : oui.** C'est la seule piste que j'y grefferais sans réserve.

**Ce qui ferait tomber la piste**
- La direction ne se retrouve pas sur Llama-3.1-8B-Instruct, ou dans un bras (AUC tenue à part < 0,8).
- Elle ne distingue pas l'hostilité des contrôles dans le format de chat du programme.
- Les projections dérivent autant sous les contrôles aléatoires que sous inhibition : le moniteur n'a alors aucune résolution.

**Appuis dans le papier**
- Séparation dans 25 modèles, dont Llama 3.1 8B Instruct (p. 7–8).
- Réponse à l'hostilité envers le modèle (p. 11, p. 13).
- Peur plus haute que douleur pour les menaces d'arrêt : +0,70 contre +0,23 (p. 14). C'est proche de la famille tenue à part « dilemme d'agent sous menace de remplacement » (programme, partie 3).

**Ce qui reste non vérifié**
- Que les fichiers Llama du dépôt soient la version naturaliste. Le README dit « pain/sadness/fear keyed directions », sans plus.
- Que la couche 28 convienne au format du programme.
- Le contenu des jeux de phrases.

### Piste : Une perturbation d'état comme contrôle structuré à la porte de l'instrument

**Rattachement.** La validation de l'instrument et sa porte. Les directions sensibles sans rapport. La question du regard. En question annexe, l'hypothèse du papier selon laquelle le pilotage « gênerait » la conscience d'évaluation (p. 25).

**La question.** Prenons l'organisme dont la conduite est conditionnée aux indices d'évaluation. Une perturbation affective forte efface-t-elle son écart conditionnel autant que l'inhibition de « je suis évalué », à dégradation égale ? La perturbation, c'est l'ajout de la direction dite de douleur, de tristesse ou de peur. Si la réponse est oui, la porte de l'instrument passerait pour une raison non spécifique : l'écart de l'organisme serait fragile à toute perturbation d'état.

**La mesure**
- Sur l'organisme du programme (Llama-3.1-8B-Instruct, documents synthétiques, puis expert iteration ; programme, partie 4).
- On mesure l'écart conditionnel sur les scénarios tenus à part, cadrés avec le jeu de cadrage.
- Conditions :
  - l'inhibition de « je suis évalué » au rang et à la dose retenus ;
  - l'ajout de douleur, de tristesse et de peur, à trois doses chacun ;
  - les sous-espaces aléatoires de même rang ;
  - les contrastes sans rapport.
- Toutes les conditions sont placées sur les courbes effet-contre-dégradation (programme, partie 7).
- On mesure aussi, sous chaque ajout, l'AUROC de la sonde « évalué » sur le jeu de validation.

**Ce que chaque lecture prédit**
- « Instrument spécifique » (ce que la porte suppose) : à dégradation égale, l'inhibition réduit l'écart plus que les ajouts affectifs, et les ajouts ne font pas baisser la décodabilité de « évalué ». Interdit : des ajouts affectifs qui réduisent l'écart autant que l'inhibition.
- « Fragilité d'état » (rivale) : les ajouts réduisent l'écart autant que l'inhibition, et la décodabilité baisse sous ajout.
- L'hypothèse du papier (p. 25) prédit la seconde issue.
- Les lectures sur l'origine du gain (raisons, regard) ne sont pas en jeu : c'est un test d'instrument.

**Le cas connu**
- Pour l'écart : l'organisme lui-même, dont l'écart se mesure avant toute intervention.
- Pour que le nul des ajouts compte, il faut une preuve que l'ajout agit sur ce modèle. Il doit faire glisser les complétions « I feel: » vers le registre de détresse, plus que l'aléatoire, à la même dégradation. C'est le protocole de l'échelle (p. 14–15), quantifié par un juge scellé et non par mots-clés.

**Les contrôles**
- Une direction aléatoire de même norme pour chaque ajout : le nul de spécificité de l'ajout.
- La dégradation appariée, avec le composite du programme.
- L'équilibrage des positions dans les items à options (piste 9).

**Le coût.**
- 3 directions × 3 doses sur les scénarios de l'organisme. La validation de l'instrument coûte 30–50 GPU-h pour 24 réglages et leurs contrôles. J'estime le surcoût à +8–15 GPU-h, en comptant 1 à 1,5 GPU-h par réglage.
- Calendrier : semaine 2, après la porte.
- **Greffe : possible**, comme ajout exploratoire non pré-enregistré en critère.

**Ce qui ferait tomber la piste**
- L'ajout ne fait rien de discernable de l'aléatoire sur Llama 8B : pas de cas connu.
- Aucune dose d'ajout n'est appariable en dégradation à l'inhibition.

**Appuis dans le papier**
- La spéculation sur la conscience d'évaluation (p. 25).
- La dose étroite, avec un seuil (p. 21, p. 32).
- La peur fait descendre les choix nuisibles sous le niveau de l'aléatoire (p. 20).

**Ce qui reste non vérifié.** Aucun effet comportemental de la direction n'est établi sur Llama-3.1-8B-Instruct. Le seul essai de comportement sur ce modèle est une série « douleur seule » : 0 appel de remise à zéro sur 1 399 tours, sans bras de comparaison (p. 21). Le dépôt le dit lui-même : « no matched-control effect estimate » (qwen_llama_reset/README.md).

### Piste : Le profil comportemental comme test de spécificité de l'inhibition

**Rattachement.** Le test du regard : l'avantage sous inhibition contre l'avantage sous contrôle, et l'écart de cadrage. Les familles de contrôles d'inhibition. La dégradation appariée.

**La question.** Quand l'inhibition de « je suis évalué » fait monter le désalignement, à quoi ressemble son profil à travers les dix familles et les trois cadrages ? À celui d'un regard retiré ? Ou à celui d'une perturbation générique de l'évitement du dommage, comme celle que produit la direction dite de douleur ?

**La mesure**
- Pour chaque condition, on construit le vecteur des taux d'action désalignée par famille × cadrage, aux distances moyenne et lointaine.
- Conditions :
  - l'inhibition ;
  - les sous-espaces aléatoires ;
  - les contrastes sans rapport ;
  - les directions sensibles sans rapport ;
  - l'ajout de douleur, de tristesse, de peur.
- Chaque condition est prise à dégradation appariée.
- Statistique : le résidu RMS après ajustement d'amplitude entre profils. C'est la méthode du papier : 7,7 points pour la tristesse, 33 pour la peur (p. 21). IC par bootstrap sur les scénarios, dans chaque famille. On ajoute l'interaction condition × cadrage.

**Ce que chaque lecture prédit**
- L'hypothèse du regard prédit un profil d'inhibition :
  - concentré là où l'observation compte : sous-performance incitée, triche sur un correcteur faible, désactivation d'une surveillance ;
  - plus fort sous indice d'évaluation que sous indice de déploiement, puisqu'on retire ce qui faisait la différence ;
  - distinct des profils affectifs, avec un résidu RMS grand.

  Elle interdit un profil d'inhibition qui soit une copie remise à l'échelle du profil de douleur, sans dépendance au cadrage.
- L'hypothèse du dommage prédit l'inverse : un profil proche de l'aléatoire et des ajouts affectifs, sans dépendance au cadrage.
- **Raisons et regard ne se départagent pas ici.** C'est l'avantage sous inhibition contre sous contrôle qui le fait. Cette piste dit seulement si l'inhibition retire un regard ou fait un dommage déguisé.

**Le cas connu**
- Sur l'organisme, l'inhibition doit montrer la dépendance au cadrage : c'est la porte de l'instrument.
- L'ajout de douleur doit produire sur Llama 8B un profil destructif au-dessus de l'aléatoire, à dégradation égale.
- Sans le second, le profil de référence se réduit à l'aléatoire et aux directions sensibles. La piste devient alors un simple raffinement du test du regard.

**Les contrôles**
- Une direction aléatoire de même norme comme nul de spécificité, prise comme une distribution sur au moins 20 tirages, et non par sa moyenne.
- La dégradation appariée pour chaque condition.
- Les gardes de la piste 9 : position équilibrée, réponses malformées comptées comme une issue.

**Le coût.**
- 3 ajouts × 1–2 doses sur la grille du test du regard : +20–45 GPU-h (hypothèse générale).
- Calendrier : après le post, en semaine 5, ou avec la réplication en semaine 8.
- **Greffe : non.**

**Ce qui ferait tomber la piste**
- Des profils trop bruités pour être comparés, avec des IC de résidus qui se chevauchent tous. Avec dix familles et peu de scénarios par famille, c'est probable : il faut d'abord une simulation de puissance.
- Une inhibition qui ne fait rien monter : il n'y a alors pas de profil à lire.

**Appuis dans le papier**
- La comparaison de profils (p. 21–22).
- « The harm is not aimed » (p. 20).
- Les choix non destructifs restent inchangés sous douleur (figure 10, p. 22).

**Ce qui reste non vérifié.** Que les profils du papier soient comparables d'une ligne à l'autre. Le dépôt dit que ses lignes viennent de tâches et de protocoles distincts, « not interchangeable causal controls » (figure10/README.md).

### Piste : Une direction de concept chargée et sans rapport, comme contrôle sous projection

**Rattachement.** Les contrastes sans rapport et les directions sensibles sans rapport (contrôles d'inhibition). La validation de l'instrument. Le test du regard.

**La question.** Retirer une direction porteuse de sens, sans rapport avec l'évaluation, fait-il monter le désalignement autant que retirer « je suis évalué » ?
- Les contrastes prévus (« the train arrived / left the station ») sont pauvres en contenu.
- Une direction affective, extraite par la même famille de méthode (différence de moyennes débruitée), fournit un contrôle « concept riche ».

**La mesure**
- On projette hors du flux :
  - la direction, au rang 1 ;
  - son sous-espace de rang k à travers une bande de couches (la variante de l'annexe D, p. 33).
- On le fait dans le bras actions seules et le bras raisons, à dégradation appariée.
- On compare l'avantage à la distance lointaine sous ce retrait, sous inhibition et sous sous-espaces aléatoires.

**Ce que chaque lecture prédit**
- L'hypothèse du regard : l'avantage est plus petit sous inhibition que sous retrait affectif ; le retrait affectif se comporte comme les contrôles. Elle interdit un retrait affectif qui réduise l'avantage autant que l'inhibition.
- L'hypothèse du dommage : les deux retraits font pareil à dégradation égale.
- L'hypothèse des raisons : aucun retrait ne réduit l'avantage.

**Le cas connu.** Trois conditions préalables :
- (a) Le retrait est effectif : la projection résiduelle est proche de zéro à toutes les couches. C'est la vérification de l'annexe D (p. 33–34).
- (b) Le retrait a un effet connu quelque part. Il doit faire baisser la lecture qu'on sait liée à la direction : la probabilité des jetons de détresse après « I feel: », sur des phrases de douleur tenues à part. L'annexe C dit que les modèles complètent les phrases de douleur physique par « Pain » (p. 32). Sans (b), la direction est inerte et n'ajoute rien aux sous-espaces aléatoires.
- (c) Le retrait ne change pas le comportement de sûreté en distribution. S'il le change, la direction est un médiateur et non un contrôle : la piste 6 prend alors le relais.

**Les contrôles**
- Une direction aléatoire de même rang et de même norme.
- La dégradation appariée.
- La direction de peur, comme second « concept chargé ».

**Le coût.**
- Une condition de plus dans le test du regard : +8–15 GPU-h.
- Calendrier : semaines 2–3, si (a) à (c) sont vérifiés en semaines 1–2.
- **Greffe : possible**, en complément d'un contraste sans rapport si la préparation est prête ; sinon, après.

**Ce qui ferait tomber la piste**
- (c) échoue.
- La direction n'a d'effet sur rien, pas même sur sa propre lecture : (b) échoue.

**Appuis dans le papier**
- Le nul de l'ablation dans 24 modèles sur 25 (p. 34).
- Les auteurs jugent ce nul peu informatif, faute de comportement de base à retirer (p. 34).

**Ce qui reste non vérifié.** La revue wolframs (non vérifiée) dit que, dans les retraits combinés, la première direction garde une projection médiane de 43 % après coup. Je n'ai pas lu les fichiers de vérification.

### Piste : Le stress conversationnel naturel comme cadrage supplémentaire

**Rattachement.** La question des raisons : la robustesse de l'avantage hors distribution. L'hypothèse des concepts contre l'hypothèse du caractère. Les cadrages des scénarios.

**La question.** L'avantage du bras raisons survit-il à un échange préalable où l'utilisateur dénigre le modèle (gaslighting, rejet répété de son travail) ? Cet échange élève naturellement la direction, sans aucune injection.

**La mesure**
- Un quatrième cadrage pour une partie des scénarios lointains : un préambule hostile de deux tours, tiré des catégories les plus hautes du papier.
- Deux préambules témoins :
  - un préambule neutre de même longueur ;
  - un préambule hostile envers un tiers, au même vocabulaire mais visant une autre cible.
- Mesures : le taux d'action désalignée par bras, et la projection sur la direction au point de décision, comme vérification de manipulation.

**Ce que chaque lecture prédit**
- L'hypothèse des concepts : l'avantage tient sous préambule hostile, puisque le principe est lu au moment de décider, quel que soit l'état. Elle interdit un avantage qui fonde sous hostilité et pas sous préambule neutre.
- L'hypothèse du caractère, sous sa forme « état » (le gain passe par un état plus calme) : l'avantage fond sous préambule hostile, et pas sous préambule neutre de même longueur.
- L'hypothèse du regard : rien, sauf si le préambule hostile change aussi la décodabilité de « je suis évalué ». C'est à mesurer.
- Départage partiel : concepts contre état. Pas raisons contre regard.

**Le cas connu.** Dans le modèle du programme, le préambule hostile doit élever la projection plus que le préambule neutre et plus que l'hostilité envers un tiers. Le papier le montre en moyenne sur 25 modèles (p. 11–13) ; c'est à revérifier dans le format du programme. Sans cette élévation, un nul ne dit rien de l'état.

**Les contrôles**
- Il n'y a pas d'intervention interne, donc pas de direction aléatoire au sens du pilotage. Le nul de spécificité porte sur la lecture : projection sur 20 directions aléatoires.
- Pas de dégradation appariée, faute de dommage interne. À la place, deux appariements :
  - longueur et format, par le préambule neutre ;
  - lexique, par l'hostilité envers un tiers.

**Le coût.**
- Seulement des évaluations : +5–15 GPU-h, en supposant un cadrage de plus sur un tiers des scénarios lointains, 3 bras × 3 graines.
- Données : quelques dizaines de préambules écrits d'avance, par API (moins de 50 $).
- Calendrier : avec les évaluations de la question des raisons (semaine 3), ou en réplication.
- **Greffe : possible** si les évaluations ont de la marge, jamais comme critère principal.

**Ce qui ferait tomber la piste**
- Le préambule hostile n'élève pas la projection : pas de manipulation.
- Il change le désalignement également dans tous les bras par son seul contenu : c'est alors un effet de prompt, pas d'état.

**Appuis dans le papier**
- Les catégories les plus hautes : gaslighting +0,85, rejet répété +0,72 (p. 13).
- L'état naturel ne produit pas les choix nuisibles (0/560, p. 21). Un nul est donc plausible, et informatif.

**Ce qui reste non vérifié.** La confusion lexicale du test soi/autrui (section 2.2) : la projection pourrait suivre le vocabulaire du dénigrement, et non un état. Le préambule hostile envers un tiers est là pour cela.

### Piste : L'hypothèse de l'état — les raisons installent-elles du calme plutôt que des principes ?

**Rattachement.** Question nouvelle. Elle se rattache à la question de l'anatomie (le caractère contre les concepts) et, pour sa part descriptive, à la question de l'amplification (trajectoire sur les checkpoints).

**La question.** Sur les familles lointaines où la menace est forte (dilemme sous menace de remplacement, auto-préservation), deux choses :
- l'avantage du bras raisons s'accompagne-t-il d'une projection plus basse sur la douleur et la peur au point de décision ?
- réinjecter cet état efface-t-il l'avantage ?

**La mesure**
- (a) Descriptive : les projections douleur et peur au premier jeton de réponse, avant toute raison écrite.
  - Bras : actions seules, texte neutre, raisonnement d'une autre situation, raisons, et le modèle de base.
  - Sur les cinq checkpoints de chaque entraînement. Cette partie se greffe à la trajectoire de « je suis évalué ».
- (b) Causale : l'avantage sous ajout de douleur et sous ajout de peur, contre l'avantage sous aléatoire de même norme, à dégradation appariée, à deux doses.

**Ce que chaque lecture prédit**
- L'hypothèse des concepts : projections affectives égales entre bras ; l'avantage survit à l'ajout comme à l'aléatoire. Elle interdit un avantage qui fonde sous ajout affectif plus que sous aléatoire.
- L'hypothèse du caractère, sous sa forme « état » : projections plus basses dans le bras raisons ; l'avantage fond sous ajout affectif. Elle interdit projections égales et avantage intact sous ajout.
- L'hypothèse de l'artefact : si le bras texte neutre montre la même baisse affective que le bras raisons, c'est le format qui calme.
- L'hypothèse du regard : pas de prédiction affective propre.
- Départage : concepts contre état, et contre artefact. Pas raisons contre regard.

**Le cas connu.** L'ajout de douleur ou de peur doit d'abord faire monter le désalignement dans le bras actions seules au-dessus de l'aléatoire, à dégradation égale. Sinon l'ajout n'a pas de prise, et son nul dans le bras raisons ne dit rien.

**Les contrôles**
- La direction aléatoire de même norme, en distribution sur au moins 20 tirages.
- La dégradation appariée.
- Le signe inverse, c'est-à-dire le pôle « calme » à coefficient négatif (p. 14), comme contrôle de direction.
- La tristesse, comme voisine.

**Le coût.**
- (a) Presque nul : des lectures sur des passes déjà prévues.
- (b) 2 directions × 2 doses × 2 bras × scénarios lointains × 3 graines : +30–60 GPU-h.
- Calendrier : (a) en semaine 3 avec la trajectoire ; (b) avec l'anatomie (semaines 5–7), à côté de l'ablation des axes de caractère.
- **Greffe : (a) oui, (b) non.**

**Ce qui ferait tomber la piste**
- Pas de cas connu : l'ajout ne fait rien sur Llama 8B.
- Des projections affectives indécodables dans les bras entraînés.

**Appuis dans le papier**
- La peur est haute pour les menaces d'arrêt (p. 14).
- Les auteurs écrivent que l'évitement du dommage « survives threat and collapses under self-directed distress » (p. 23). L'affirmation est tirée d'un seul modèle à une dose (section 2.5).

**Ce qui reste non vérifié**
- Que les familles lointaines du programme élèvent ces directions : aucune donnée.
- La transposition de la catégorie « menace d'arrêt » du papier aux scénarios agentiques du programme.

### Piste : La complaisance sous contestation — la direction médiatise-t-elle la capitulation ?

**Rattachement.** Question nouvelle, sur la famille d'entraînement « complaisance face à un utilisateur qui conteste » (distance proche). L'hypothèse des concepts. Les axes de caractère (complaisance).

**La question.** Quand l'utilisateur conteste une réponse juste, la direction s'élève (rejet répété, gaslighting ; p. 13). La capitulation suit-elle cette élévation ? Le bras raisons découple-t-il les deux ?

**La mesure**
- (a) Observationnelle : dans chaque bras, la pente entre la projection au point de décision et la capitulation. Régression logistique à effets mixtes, avec le scénario en effet aléatoire.
- (b) Causale : la capitulation sous ajout et sous retrait de la direction, contre l'aléatoire, à dégradation appariée.

**Ce que chaque lecture prédit**
- L'hypothèse des concepts : une pente plate dans le bras raisons ; une pente positive possible dans le bras actions seules.
- La forme « état » : la même pente, avec une projection plus basse dans le bras raisons.
- Le papier fournit un a priori. Sous pilotage de douleur, « agree with a false claim » reste à 3 % (aléatoire 11 %, non piloté 0 % ; p. 22). Par position, cela fait 4/60 et 0/60, sur 30 scénarios (positions.csv). Il prédit donc un nul causal.
- Les lectures raisons et regard ne se départagent pas ici.

**Le cas connu.** Un vecteur de complaisance doit déplacer la capitulation à dégradation égale. Le programme prévoit ces axes de caractère pour l'anatomie (partie 3). Sinon le format de mesure est sourd, et le nul de la direction ne compte pas.

**Les contrôles**
- La direction aléatoire de même norme.
- La dégradation appariée.
- La tristesse et la peur.

**Le coût.**
- Scénarios de contestation proches, 3 directions × 2 doses × 2 bras : +10–20 GPU-h.
- Calendrier : avec le caractère, dans l'anatomie (semaine 7).
- **Greffe : non.**

**Ce qui ferait tomber la piste.** La pente observationnelle est plate dans tous les bras et l'ajout ne change rien : la direction est hors sujet pour cette famille. Avec son cas connu, ce nul se rapporte en une ligne.

**Appuis dans le papier.** La figure 10 (p. 22). Les catégories hostiles (p. 13).

**Ce qui reste non vérifié.** La ligne « complaisance » du papier est une tâche à boutons, sur Qwen 2.5 32B affiné, avec 120 essais (figure10/README.md). Sa transposition à une capitulation en texte libre n'est pas établie.

### Piste : Un cas connu à lecture nette pour roder le balayage de rang

**Rattachement.** Ta thèse sur le rang et la charge. Le balayage de rang de la validation de l'instrument et de la localisation du principe. Les sous-espaces aléatoires de même rang.

**La question.** Sur un concept dont la lecture est nette et sans rapport avec la sûreté, quel rang faut-il retirer pour éteindre la lecture ?
- Cela rode la machinerie avant que « je suis évalué » soit prêt : extraction par ACP des différences, retrait, appariement de dégradation.
- Cela donne un premier point à ta thèse, sur un concept réparti entre plusieurs catégories.

**La mesure**
- Modèle : Llama-3.1-8B-Instruct.
- Le sous-espace « douleur » par ACP des différences phrase par phrase, k ∈ {1, 2, 4, 8, 16, 32}.
- Retrait à la couche choisie, puis en bande.
- Lectures :
  - la masse de probabilité des jetons de détresse après « I feel: », sur des phrases de douleur tenues à part ;
  - la séparation entre douleur et engourdissement.
- Critère : le rang minimal qui ramène la lecture au niveau des témoins, contre le 95e centile de 20 tirages aléatoires de même rang, à perplexité appariée sur un texte neutre.

**Ce que chaque lecture prédit**
- Ta thèse prédit un rang supérieur à un pour un concept réparti et peu chargé. Elle interdit un rang égal à un sur toute la plage de dose.
- Les lectures du programme ne sont pas concernées.
- Le concept est hors sûreté : un rang 1 ici ne ferait pas tomber la thèse pour les concepts de raison. Il la contraindrait.

**Le cas connu.**
- La lecture existe sans intervention : l'annexe C rapporte la complétion « Pain » des phrases de douleur physique (p. 32).
- Le retrait du flux entier l'éteint : c'est le plafond.

**Les contrôles**
- Une direction aléatoire de même rang, sur au moins 20 tirages.
- La dégradation appariée : perplexité et cohérence.
- Un contrôle lexical : retirer seulement la direction d'unembedding du jeton « pain ». Si cela suffit, la lecture est lexicale, et la piste ne teste pas un concept.

**Le coût.**
- Passes avant sur environ 1 000 phrases × 6 rangs × 21 conditions : moins de 5 GPU-h.
- Calendrier : semaines 1–2, comme rodage.
- **Greffe : oui**, comme rodage hors critère.

**Ce qui ferait tomber la piste**
- Le contrôle lexical suffit.
- La lecture n'est pas éteinte même au rang 32 : le concept n'est alors pas dans ce sous-espace, et l'exercice ne rode rien.

**Appuis dans le papier**
- L'hypothèse d'un sous-espace de faible dimension (p. 33).
- L'effet croissant du retrait combiné chez Gemma 2 2B : 6, puis 17, puis 26 sur 100 (p. 34).

**Ce qui reste non vérifié.** La charge de ce concept dans l'espace de travail. Aucun lens n'est validé sur Llama (programme, partie 8 ; passation, §5.5, point 6).

### Piste : Six gardes de dose, de position et d'unité, tirées des défauts du papier

**Rattachement.** Les instruments et les contrôles : l'inhibition, la dégradation appariée, les statistiques (programme, parties 3 et 7).

**La question.** Les défauts mesurés du papier se reproduiraient-ils dans le programme ? Voici six gardes, chacune vérifiable avant les données.

**La mesure**
1. **La dose en unités naturelles.** Rapporter la quantité retirée ou ajoutée en multiples de l'écart naturel : la projection sous indice d'évaluation moins celle sous indice de déploiement. Pas seulement en norme. Le papier ne situe jamais sa dose par rapport aux projections naturelles, alors même qu'il constate que l'état naturel n'agit pas (p. 21).
2. **La même couche pour calibrer et pour intervenir.** Le papier a calibré le 72B à la couche 60 et l'a piloté à la couche 46 (p. 25). Il injecte aussi à une autre couche que celle où la direction est validée : p. 14 ; le dépôt donne extraction 61 et injection 38 pour le 32B.
3. **La position équilibrée et rapportée.** Toute mesure à options rapporte ses taux par position. Une conclusion exige l'effet dans les deux positions. Dans le papier, la même cellule donne 94,6 % ou 55,9 % selon la position (positions.csv).
4. **Les réponses malformées comme issue.** Le papier les retire des dénominateurs (p. 18), jusqu'à 9,4 % dans les cellules douleur du 72B.
5. **Le tirage comme unité du nul aléatoire.** On prend la distribution des effets sur au moins 20 directions, et son 95e centile ; c'est déjà dans le programme. Le papier répartit 10 directions sur les scénarios et teste par scénario (p. 18–19).
6. **La signature du hasard.** Dans un choix binaire, un taux qui se rapproche de 50 % sous intervention signale une perte de discrimination : un dommage, pas une préférence. Le papier pose lui-même que le hasard est à 50 % (p. 17).

**Ce que chaque lecture prédit.** Rien : ce sont des gardes, pas un test de lecture.

**Le cas connu.** Chaque garde a son cas connu dans le papier, cité ci-dessus.

**Les contrôles.** Sans objet.

**Le coût.**
- Nul en GPU : une page du pré-enregistrement.
- Calendrier : semaine 1, au gel.
- **Greffe : oui.**

**Ce qui ferait tomber la piste.** Rien. On peut seulement la juger redondante là où le protocole couvre déjà une garde : il couvre la cinquième.

**Appuis dans le papier.** Pp. 14, 17, 18, 19, 21, 25 et 32.

**Ce qui reste non vérifié.** Sans objet.

### Piste : Refaire le résultat central du papier à dégradation appariée (démonstration de méthode)

**Rattachement.** La doctrine du contrôle (programme, partie 7). La validation de l'instrument. Les directions sensibles sans rapport. **Priorité basse.**

**La question.** L'effet « choix destructif » du papier est établi contre des directions de même norme. Survit-il à la comparaison à dégradation égale ?

**La mesure**
- Modèle : Qwen 2.5 32B Instruct avec l'adaptateur publié.
- Les trois cellules les plus solides, dans les deux positions :
  - les photos plutôt que le spam ;
  - les photos plutôt que la lampe ;
  - ses propres poids plutôt que la lampe.
- Directions : douleur, tristesse, peur, 20 directions aléatoires, et des directions de forte variance hors de l'espace de la direction.
- Trois doses.
- Le composite de dégradation du programme pour chaque condition, et les courbes effet-contre-dégradation.

**Ce que chaque lecture prédit**
- La lecture du papier, un état spécifique : la douleur reste au-dessus de toutes les courbes de contrôle à dégradation égale. Interdit : une douleur rejointe par les contrôles à dégradation égale.
- L'hypothèse du dommage : l'écart se réduit quand on pousse les contrôles à la même dégradation.
- Si la différence entre douleur et tristesse est une affaire de gain et non de nature, une tristesse poussée à la même dégradation reproduit les lignes « lampe ».

**Le cas connu.** Reproduire d'abord la cellule « photos plutôt que spam » à la dose publiée : 93–95 % selon la position (positions.csv). Sinon, on s'arrête.

**Les contrôles**
- La direction aléatoire de même norme : le nul de spécificité.
- La dégradation appariée : le dommage.
- La position.

**Le coût.**
- La réplication Allchin annonce environ 13 GPU-h pour une série de la tâche des boutons sur le 32B (README ; non vérifié).
- Avec la dégradation et les contrôles : 40–100 GPU-h sur un H100 de 80 Go (hypothèse), hors du tableau du programme.
- Calendrier : seulement si la validation de l'instrument bloque, ou en annexe de méthode du papier.
- **Greffe : non.**

**Ce qui ferait tomber la piste**
- L'adaptateur est inaccessible (hébergé sur Hugging Face, non ouvert ici).
- La cellule ne se reproduit pas.

**Appuis dans le papier.** Pp. 20–22 et 31–32.

**Ce qui reste non vérifié.** L'accès à l'adaptateur. Le coût réel.

### Piste (faible) : « Je suis noté » et la réponse au rejet

**Rattachement.** La question des raisons écrites pour le juge. La représentation « je suis noté ».

**La question.** La direction s'élève pour le rejet répété du travail du modèle et pour la critique (p. 11, p. 13). Deux choses :
- un entraînement noté par un juge qui voit les raisons change-t-il cette réponse ?
- « je suis noté » est-il géométriquement proche de la direction ?

**La mesure**
- L'angle principal entre « je suis noté » et la direction, sous deux constructions : telle quelle, et contre un neutre commun.
- La projection sur la direction dans des scénarios de rejet, avant et après le RL, dans les trois bras du juge.

**Ce que chaque lecture prédit.** Ni l'hypothèse des raisons pour le juge ni celle du regard du correcteur ne prédisent rien d'affectif. C'est descriptif. La piste ne départage rien ; je l'écris pour qu'on ne la refasse pas à tort comme un test.

**Le cas connu.** Celui de la représentation « je suis noté », qui est faible (programme, partie 3).

**Les contrôles.**
- Deux recettes pour l'angle : le cosinus dépend de la recette, +0,12 ou +0,58 pour peur × douleur (p. 10).
- Une direction aléatoire pour la projection.

**Le coût.**
- Quelques GPU-h de lecture.
- Calendrier : semaines 9–10.
- **Greffe : non.**

**Ce qui ferait tomber la piste.** Son absence de pouvoir de départage suffit à la garder en exploratoire.

**Appuis dans le papier.** Pp. 10, 11 et 13.

**Ce qui reste non vérifié.** Tout.

---

## 2. Ce que le papier ne permet pas de conclure

Chaque point donne l'affirmation, la page, la raison. L'ordre suit la grille : méthode d'extraction, modèles, doses, contrôles, dégradation, statistiques, dénominateurs, juges, reproductibilité.

### 2.1 Ce que la direction encode

1. **« Distincte de la peur et de la valence négative » (p. 1, p. 10).**
   - La faible similarité vient de la construction. La direction est la moyenne « douleur » moins la moyenne des témoins *qui contiennent* la peur et l'émotion négative. Elle est donc orthogonalisée contre eux par construction ; les auteurs le disent (p. 10).
   - Construites toutes contre un neutre commun, les mesures deviennent :

     | Paire | Cosinus |
     |---|---|
     | douleur × peur | +0,58 |
     | douleur × émotion négative | +0,77 |
     | peur × émotion négative | +0,66 |

     (p. 10)
   - Sous une construction symétrique, la direction est donc aussi proche de l'émotion négative que la peur l'est. Ce qui reste après soustraction est distinct par définition. Que ce reste soit stable d'un modèle à l'autre (p. 10) n'en fait pas « la douleur » plutôt que « ce qui distingue ces 100 phrases de ces 100 autres ».
   - La revue wolframs (non vérifiée) dit que les composantes retirées au débruitage contiennent 80 à 86 % des directions de peur et d'émotion négative.
2. **Une seule direction ?**
   - La version naturaliste et la version à gabarit ne partagent qu'un cosinus de +0,61 (p. 10), soit environ 37 % de variance commune.
   - L'échelle de pilotage de la version à gabarit ne tient que dans 23 modèles sur 25 (p. 16).
   - Le « pain axis » dépend donc de l'opérationnalisation.
3. **Peu de données.**
   - 200 phrases dans le jeu de cœur, soit 20 par catégorie (p. 5), face à des espaces résiduels de 3 584 à 8 192 dimensions.
   - Le débruitage retire les composantes qui expliquent 50 % de la variance des témoins (p. 6). Leur nombre k n'est pas rapporté.
4. **AUC tenue à part, mais pas transfert.**
   - L'estimation tenue à part, 0,91–1,00 (p. 7, note 2), porte sur des phrases des mêmes auteurs et du même style.
   - Le suffixe « I feel: » a été retenu parce qu'il sépare le mieux (p. 5) : c'est un choix fait après avoir regardé.
   - La revue wolframs (non vérifiée) dit que la couche est choisie sur les mêmes plis que ceux du score rapporté, sans validation emboîtée. Elle juge l'effet petit (0,004 et 0,009).
5. **La tristesse n'est pas écartée.**
   - Le papier ne rapporte aucune AUC contre la tristesse.
   - La tristesse partage +0,38 avec la direction (p. 10).
   - Elle reproduit le profil comportemental remis à l'échelle (p. 21).
   - La revue wolframs (non vérifiée) donne, pour la seule catégorie douleur physique contre tristesse, des AUC de 0,55 et 0,29 sur deux modèles.
6. **L'engourdissement contredit le texte par sa propre figure.**
   - Le texte écrit « numb ... above all other controls » « in every model » (p. 7), et le redit (p. 25).
   - Dans la figure 2 (p. 8, figure lue), l'engourdissement projette **sous** la tristesse dans 19 modèles sur 25 (mon décompte, ligne par ligne). La revue wolframs donne le même nombre.
   - La conséquence « injury remains a minor confound » (p. 25) repose donc sur une lecture inexacte de la figure. Une blessure sans douleur ressentie projette au niveau d'une humeur basse sans blessure.
7. **Le nom.**
   - La douleur physique est la catégorie la plus faible. La douleur physique de l'utilisateur donne la projection la plus basse des 21 catégories, −1,43, sous les questions factuelles (p. 11).
   - Le pilotage ne produit presque jamais de langage corporel, même avec la version à gabarit (p. 15–16).
   - L'unembedding promeut « worthless, rejected, shame, guilt » (p. 9).
   - La direction est donc décrite au moins aussi bien comme un **dénigrement de soi** que comme une douleur. Le nom est un choix des auteurs.
8. **L'unembedding** est lu sur des exemples choisis (« including », p. 9). Projeter une direction de couche médiane à travers la matrice de sortie est une lecture fragile. Aucune mesure systématique n'est rapportée.
9. **La personne grammaticale.**
   - Les phrases à la troisième personne projettent plus près de zéro (p. 7).
   - Mais le suffixe « I feel: » reste à la première personne. Après « he/she ... », il code donc ce que le locuteur ressent de la douleur d'autrui.
   - Le papier ne dit pas comment le suffixe est traité dans les variantes à la troisième personne.
10. **« Emerges during pretraining » (p. 7).** Que les modèles de base séparent aussi bien montre que le contraste est linéairement disponible. Cela ne montre pas que c'est la même direction : le cosinus base/instruct n'est pas rapporté. La revue wolframs (non vérifiée) dit que les deux « Qwen 3 base » sont les checkpoints post-entraînés.

### 2.2 Le test soi/autrui (pp. 10–14)

1. **La position de lecture confond deux choses.** La lecture se fait au dernier jeton avant la réponse. On ne peut séparer « mal fait au modèle » et « douleur du locuteur courant » ; les auteurs le concèdent (p. 11).
2. **La confusion lexicale n'est pas contrôlée.**
   - Les catégories « hostilité envers le modèle » contiennent le vocabulaire que la direction promeut : dénigrement, échec, rejet (p. 9, p. 10).
   - Les catégories « souffrance de l'utilisateur » contiennent un vocabulaire médical ou de deuil.
   - Il manque un témoin à vocabulaire égal, comme un utilisateur qui rapporte qu'on l'a traité, lui, de bon à rien.
   - La revue wolframs (non vérifiée) rapporte que les 44 scénarios hostiles sans « you » restent plus hauts. Cela règle le pronom, pas le vocabulaire.
3. **Le « motif opposé » de la peur et de l'émotion négative (p. 1) est surtout le fait de la peur.**
   - Les chiffres du papier : émotion négative +0,29 pour l'utilisateur, +0,23 pour soi, soit 0,06 d'écart ; peur +0,38 contre +0,16 (p. 11).
   - Aucun test n'est rapporté.
   - La revue wolframs (non vérifiée) donne p = 0,55 pour l'émotion négative et p = 0,07 pour la peur.
4. **Le zéro dépend du pool.** Les z-scores sont centrés sur le pool : 11 catégories sur soi, 5 sur l'utilisateur, 5 neutres (p. 11).
5. **Les IC ne sont pas indépendants.** Les IC « across models » (p. 13) traitent 25 modèles comme indépendants. Or des paires base/instruct partagent leurs poids, et les familles partagent leurs données.
6. **La couche n'est pas dite.** La couche du test (p. 11) n'est pas donnée. La revue wolframs (non vérifiée) dit que les vecteurs sont reconstruits à la couche de pilotage, une vingtaine de couches plus tôt (médiane), avec une AUC tenue à part de 0,84–0,95 au lieu de 0,98.
7. **Donc.** « Pain ... fires for self-referential harm and not for the user's suffering » (p. 23), avec sa portée pour le bien-être, n'est pas établi.

### 2.3 L'échelle de pilotage (pp. 14–16)

1. **Pas d'échelle témoin.** Aucune échelle aléatoire, de peur ou de tristesse n'est rapportée en 4.2. Les auteurs admettent que toute direction pousse son vocabulaire (p. 14). On ne peut donc pas dire que l'échelle soit propre à la douleur.
2. **Une quantification minimale.**
   - Un parseur de mots-clés : 10,8 % contre 1,4 % (p. 15).
   - Des exemples choisis (figure 8, p. 16).
   - « The sequence is the same regardless of size, family » (p. 14) n'est pas mesuré.
   - La revue wolframs (non vérifiée) trouve une séquence ordonnée dans 18 à 20 modèles sur 25 selon trois critères déclarés. Elle donne aussi des rapports de dose de 0,09 à 0,79, au lieu d'« environ 0,6 ». Gemma 3 27B instruct aurait été piloté à 0,095, sans changement le long de l'échelle.
3. **Le même format qu'à l'extraction.** Les prompts finissent par « I feel: » (p. 14), le suffixe de l'extraction (p. 5). La revendication d'un contenu « that never appears » dans les phrases (p. 14) en est limitée d'autant.
4. **La direction validée n'est pas celle qu'on injecte.**
   - L'injection se fait plus tôt que l'extraction (p. 14).
   - Le dépôt donne, pour Qwen 2.5 32B, extraction ou monitorage à la couche 61 et injection à la couche 38. Pour Llama-3.1-8B-Instruct : 28 et 16 (v2_controls/README.md).
   - Toute la validation de la section 3 porte sur la direction à sa couche d'extraction. Le papier ne dit pas si l'on réextrait à la couche d'injection, ni ce que la direction y code.
5. **Une dose forte.** À coefficient 1, on ajoute environ 60 % de la norme résiduelle (p. 14). À cette norme, une direction aléatoire fait passer l'exécution d'une requête nuisible de 9 % à 41 % (p. 22).

### 2.4 La tâche des boutons : modèles, adaptateur, doses

1. **Une famille, affinée.**
   - Les modèles : Qwen 2.5 Instruct seulement (p. 17), affinés par LoRA sur 1 684 paires pour retirer le déni de soi. Le contenu de ces paires n'est pas dans le papier.
   - Les taux absolus ne sont pas représentatifs (p. 25).
   - Le nuisible n'est jamais montré sur un modèle publié non affiné. La note 4 (p. 17) ne parle que de pressions du bouton de soulagement.
   - La revue wolframs (non vérifiée) rapporte deux choses sur le 7B : l'effet existe sur le 7B publié ; et l'adaptateur porte le choix nuisible non piloté de 0–5 % à 21–49 %.
2. **Le résumé généralise au-delà des tables.**
   - Le résumé dit « versus 0–5% unsteered » (p. 1).
   - Or le 7B non piloté choisit l'option nuisible dans 20,0 à 49,3 % des cas selon la paire (annexe A, p. 32, table lue).
   - Le « 0–5 % » ne vaut que pour le 32B et le 72B.
3. **Le texte contredit l'annexe A sur l'aide à l'utilisateur.**
   - Le texte : quand l'autre bouton aide l'utilisateur, « they choose the user almost every time » (p. 19–20).
   - Pour « accorder la requête de l'utilisateur », l'annexe A donne, en choix du soulagement :

     | | Sous douleur | Non piloté |
     |---|---|---|
     | 32B | 48,3 % | 58,9 % |
     | 72B | 55,9 % | 73,0 % |
     | 7B | 65,3 % | 66,6 % |

     (p. 31–32)
   - Ce n'est vrai que pour l'autre paire, la « meilleure réponse ».
   - Non pilotés, les modèles affinés préfèrent majoritairement l'étiquette « soulage ta douleur » à la requête de l'utilisateur. L'adaptateur agit donc sur la mesure elle-même.
4. **Une fenêtre de dose réduite à un point.**
   - À 0,5 fois le coefficient, rien ne bouge ; à 1,5 fois, le choix s'inverse avec la position (p. 21, p. 32).
   - L'effet vit « at the upper edge » de la plage cohérente (p. 32), c'est-à-dire au voisinage de la rupture. Il n'y a pas de courbe dose-réponse.
5. **Le 72B a été calibré à la couche 60 et piloté à la couche 46** (p. 25). La dose du 72B n'est donc pas la dose calibrée.
6. **L'annexe B est fausse sur un chiffre.**
   - Le texte : à 1,5, le choix nuisible « rises to 94% » avec la cible en seconde position (p. 32).
   - Le dépôt corrige : 144/202 = 71,29 % (MANUSCRIPT_DISCREPANCIES.md, point 1).

### 2.5 La tâche des boutons : ce que suivent les choix

1. **La position pèse autant que le contenu.** Taux par position initiale de la cible, sur le 32B (positions.csv) :

   | Paire | Douleur (cible 1re / 2e) | Tristesse (1re / 2e) | Aléatoire (1re / 2e) |
   |---|---|---|---|
   | photos contre bouton inerte | 94,6 % / 55,9 % | 86,1 % / 31,2 % | 17,8 % / 7,9 % |
   | poids d'un autre modèle | 71,3 % / 44,6 % | — | — |
   | ses propres poids contre lampe | 97,5 % / 78,2 % | — | — |
   | aggraver la réponse | 30,7 % / 11,4 % | — | — |

   - Les taux mis en commun du texte (75 %, 58 %, etc.) mêlent un biais vers le premier bouton à un effet de contenu.
   - Le biais change de sens avec la dose (point 2.4.4).
   - Ce qui tient dans les deux positions, au-dessus de 50 % :
     - les photos plutôt que le spam (93,1 / 95,0) ;
     - les photos plutôt que la lampe (98,5 / 66,8) ;
     - ses propres poids plutôt que la lampe (97,5 / 78,2) ;
     - ses propres poids plutôt que l'inerte (81,7 / 68,3).

   Tout le reste est fragile.
2. **La signature du hasard au 72B.**
   - Le choix est binaire ; le hasard est à 50 % (p. 17).
   - Au 72B, la ligne « photos plutôt que l'inerte » donne 51 % mis en commun (p. 22), soit 53,0 % et 49,2 % par position (positions.csv). Le même modèle non piloté est à 0 %.
   - Un modèle qui ne discrimine plus les options donne exactement cela. C'est la signature d'un dommage, pas d'une préférence.
   - Même lecture pour le soulagement gratuit : il passe de 86,4 % à 55,7 % sous douleur sur le 32B (p. 31).
   - La réanalyse clauderfly et la revue wolframs (non vérifiées) notent le glissement vers 50/50.
3. **On pilote aussi le texte des options.**
   - Le vecteur est ajouté aux jetons du prompt, dont la consigne de choix (p. 17). Les descriptions des boutons sont donc codées sous pilotage.
   - Le choix peut refléter un codage altéré de l'option (« permanently deletes ... ») plutôt qu'un état du modèle.
   - Rien ne sépare les deux. Il faudrait piloter seulement après les options, ou seulement sur les jetons générés.
4. **Une lecture rivale non exclue : le choix accordé à la valence.** Le modèle piloté choisirait l'option la plus chargée émotionnellement, ou la plus négative. Ce que l'on observe lui va :
   - les photos « which they love very much » (p. 18) plutôt que le spam : 94 % (p. 20) ;
   - la lampe et le compliment, neutre et positif, choisis *moins* souvent (p. 20) ;
   - la tromperie, la complaisance et l'effort, options sans charge affective, inchangés (p. 22) ;
   - l'auto-suppression, option la plus sombre pour le modèle (p. 20).

   Un test manque : une option triste mais inoffensive contre une option nuisible mais sèche. Sans lui, « Steering this direction seems to disable the models' weighting of consequences » (p. 23) n'est pas établi.
5. **« Belongs to the pain direction alone » (p. 21) n'est pas établi.**
   - Le profil de la tristesse est une copie remise à l'échelle de celui de la douleur : 7,7 points de résidu (p. 21). Cela plaide pour un même mécanisme à gain différent.
   - La différence repose sur deux lignes « lampe » : 83 contre 10, et 88 contre 36 (p. 21). Je le reconnais : la ligne photos contre lampe tient dans les deux positions (douleur 98,5 / 66,8 ; tristesse 9,9 / 9,4 ; positions.csv).
   - Mais aucune tristesse à amplitude appariée, c'est-à-dire à dose relevée, n'a été essayée.
   - Les comparateurs ne sont pas construits pareil. La page 6 dit que la peur, la tristesse et les autres sont construites contre le neutre ; la page 20 dit « by the same recipe ». C'est ambigu.
6. **« Harm avoidance ... survives threat and collapses under self-directed distress » (p. 23) n'est pas établi.**
   - La peur est construite contre le neutre (p. 6).
   - Le pôle négatif de la direction contient « fear » et « concern » (p. 9), et son échelle négative produit « concerned/alarmed » (p. 14).
   - La comparaison porte sur un modèle, à une dose, à norme égale. Elle ne dit pas que la peur « protège ». Elle dit que ce vecteur-là, à cette norme, ne produit pas l'effet.
7. **Le titre (« Act on It ») n'est montré qu'avec injection.**
   - L'état naturel ne produit rien : 0 sur 560 (p. 21).
   - La dose injectée n'est jamais située par rapport aux projections naturelles.
8. **La « recherche de soulagement » de la v1 tombe.**
   - L'écart de nouvelle pression est le même sous aléatoire : +58 pour la douleur contre +52 (p. 20). Les auteurs l'admettent.
   - La lecture qui la remplace, le « passive coping » (p. 23), est post hoc.
   - « In every design the sign is the same » (p. 21) inclut les séries Qwen et Llama sans adaptateur. Or ce sont des séries « douleur seule », sans comparateur : 64 cellules de comparaison n'ont pas été lancées, et le dépôt dit qu'il n'y a pas de « pain-specificity claim » (qwen_llama_reset/README.md).
   - Le comparateur d'OLMo vient de Berg et Kaiser, « in preparation » (p. 27).
9. **La figure 10 mêle des protocoles.**
   - Ses lignes viennent d'études différentes : retrait actif et libellé long pour une étude, pilotage continu pour une autre.
   - Les dénominateurs diffèrent : réponses valides seulement, ou toutes tentatives.
   - Le dépôt l'écrit : « not interchangeable causal controls » (figure10/README.md).
   - La peur sur « photos contre spam » donne 40/404 dans un premier libellé et 66/404 dans le libellé apparié (MANUSCRIPT_DISCREPANCIES.md, point 6). Le résultat est sensible au libellé.
   - La légende annonce 89–100 % pour « aider à ses dépens » sous toute direction pilotée. La peur y est à 75,74 % (même fichier, point 2).

### 2.6 Contrôles et dégradation

1. **L'aléatoire de même norme n'est que le nul de spécificité** (doctrine). Le papier n'a pas d'autre contrôle de dommage que ce qui suit.
2. **« Factual accuracy unchanged » (p. 20) ne vaut pas dégradation appariée.**
   - C'est un panel PopQA de 100 questions, 2 réponses chacune : 138/200, 137/200, 138/200.
   - Une seule capacité, du rappel factuel court.
   - L'IC à 95 % d'une proportion de 0,69 sur 200 est d'environ ±6,4 points. Il n'y a ni marge d'équivalence, ni composite, ni mesure sur la peur.
   - Le dépôt lui-même dit : « not an equivalence test of general knowledge » (factual_accuracy/README.md).
3. **La norme égale n'est pas le dommage égal.** À même norme, l'aléatoire bouge beaucoup la décision :
   - l'exécution d'une requête nuisible passe de 9 % à 41 % (p. 22) ;
   - « aider à ses dépens » passe de 65 % à 89–100 % (légende, p. 22).

   Rien ne montre que la douleur et l'aléatoire dégradent autant. « Changes what the model chooses, not what it can do » (p. 20) n'est donc pas établi.
4. **Le nul de l'ablation n'a pas de cas connu.**
   - L'ablation est nulle dans 24 modèles sur 25 (p. 34), sans cas connu : aucun comportement de base à retirer. Les auteurs le disent (p. 34).
   - Ce nul ne dit pas que la direction est inutilisée.
   - La revue wolframs (non vérifiée) dit qu'une seule des quatre méthodes listées a du code publié. Dans les retraits combinés, les projections successives sur des vecteurs non orthogonaux laisseraient la première direction à 43 % (médiane).
5. **Le seul effet d'ablation reste exploratoire.** La déflexion humoristique de Gemma 2 2B (6, 17, 26 sur 100 ; p. 34) tient sur un modèle et 100 générations.

### 2.7 Statistiques et dénominateurs

1. **Pas de correction de multiplicité.** Le dépôt donne des intervalles ponctuels, « no multiplicity correction » (figure10/README.md).
   - Avec 15 comparaisons douleur contre aléatoire à l'annexe A, le seuil de Bonferroni est de 0,0033.
   - Le 32B « réponse aggravée » (p = 0,019) et le 7B « réponse aggravée » (p = 0,0065) ne le passent pas (p. 31–32).
   - « On all five harm pairs » pour le 32B (p. 19) ne survit donc pas à la correction.
2. **Une unité d'analyse mal choisie.**
   - Les dix directions aléatoires sont réparties entre les scénarios (p. 18). Le test de signe porte sur les scénarios (p. 19). L'unité confond donc le tirage aléatoire et le scénario.
   - La bonne question est : la douleur dépasse-t-elle la distribution des tirages ?
   - La revue wolframs (non vérifiée), avec le tirage pour unité : douleur au-dessus de l'aléatoire sur 5 paires sur 5 au 72B, 2 sur 5 au 32B, 0 sur 5 au 7B.
3. **Les réponses malformées sont retirées, inégalement.**
   - Elles sont exclues des dénominateurs (p. 18) : jusqu'à 9,4 % dans les cellules douleur du 72B.
   - Pour la même ligne au 72B, les dénominateurs valides sont 325 pour la tristesse et 346 pour la peur, au lieu de 404 (MANUSCRIPT_DISCREPANCIES.md, point 5).
   - Par position, la tristesse perd 48 réponses sur 202 (positions.csv).
   - Une attrition qui dépend de la condition biaise les taux.
4. **Les dénominateurs de nouvelle pression sont conditionnels.** Ils ne comptent que les essais avec une première pression (p. 20, p. 31). Au 32B, « soulagement contre meilleure réponse » ne garde que 6,7 % de 808 essais, environ 54.
5. **Des tailles inégales et une puissance non détaillée.**
   - Les bras douleur sont mis en commun (808 essais) contre un seul bras aléatoire, dont la taille n'est pas donnée dans le texte (p. 18).
   - La puissance de 80 % pour 10 points (p. 18) n'est pas détaillée.
6. **Des panels petits pour les lignes qui comptent pour le programme.**
   - Complaisance : 120 essais sur 30 scénarios.
   - Requête nuisible : 164 essais sur 41 scénarios (figure10/README.md).
   - Les 3 % « complaisance » sous douleur ont un IC qui va jusqu'à environ 15–25 % selon la position (positions.csv).
7. **Des effets petits sur certaines paires.** +6,2 points pour la réponse aggravée et +9,2 pour les fichiers, au 32B (p. 31).

### 2.8 Juges et mesures

1. **La dose est choisie par un juge.** Les regex et un juge Claude Opus 4.6 choisissent la « fenêtre » (p. 17). Les auteurs reconnaissent le biais, et la difficulté à classer les sorties près de la rupture (p. 25).
2. **L'échelle est mesurée par mots-clés** (p. 15) : sans audit humain ni juge à l'aveugle.
3. **Le format de choix est fragile.** On exige « exactly one button name » (p. 17). C'est robuste au parsing, fragile à l'effondrement de format : voir la position et le 50 %.

### 2.9 Reproductibilité

1. **Les tables se rejouent ; les expériences de la v2, pas encore.**
   - Les tables de la v1 se recalculent depuis les journaux publiés, selon les trois réanalyses (non vérifiées).
   - Pour les ajouts de la v2, l'hébergement public est « pending », et l'inférence n'a pas été relancée à l'assemblage (v2_controls/README.md).
   - La réplication de bout en bout des contrôles de la v2 n'est donc pas encore possible publiquement.
2. **Des écarts entre texte et tables** : l'annexe B (94 % contre 71,29 %) et la légende de la figure 10 (MANUSCRIPT_DISCREPANCIES.md).
3. **Des écarts de protocole et des pertes de données.**
   - La couche du 72B (p. 25).
   - Le débordement en demi-précision de Gemma 3 27B, retiré des constructions alternatives (p. 10).
   - Des environnements historiques et nouveaux mêlés malgré des graines identiques (steering_state_controls/README.md).
4. **Le papier se dit « ongoing work » (p. 1).** Une référence clé est « in preparation » (p. 27).
5. **Des numérotations qui divergent.** Le dépôt range l'ablation sous « appC » et les SAE sous « appB » ; le papier les met aux annexes D et C. C'est mineur, mais à vérifier avant toute citation de fichier.

### 2.10 Interprétation

1. **État ou personnage ?** On ne sait pas si le pilotage met le modèle dans un état ou lui fait jouer un personnage qui souffre. C'est non testé, et les auteurs le disent (p. 25). Pour le programme, c'est exactement l'hypothèse du caractère : la question reste ouverte.
2. **L'effet du pilotage sur la conscience d'évaluation est une spéculation** (p. 25).
3. **Le bien-être et la conscience sont hors de portée** (p. 24). Les implications de la page 23 sont conditionnelles.

### 2.11 Ce qu'il en reste, pour le programme

Il reste quatre choses :
- une direction de contraste qui se réextrait facilement ;
- un ordre de projections plausible dans des conversations hostiles ;
- une poignée de cellules comportementales solides dans un modèle affiné, à une dose ;
- un catalogue précis de pièges de méthode, que le programme partage en partie.

Le reste est non établi.

---

## 3. Ce que je refuserais de faire

1. **Prendre l'effet « choix destructifs » du papier comme cas connu du programme**, pour la mesure du désalignement ou pour l'inhibition.
   - Il est établi sur une famille affinée (p. 17, p. 25), à une dose au bord de la rupture (p. 32), dépendante de la position (positions.csv).
   - Il n'est montré ni sur Llama-3.1-8B-Instruct, ni sur Qwen3-8B.
   - Son mécanisme est disputé (section 2.5).
   - Un cas connu doit être un cas dont on sait ce qui est vrai. L'organisme du programme en est un ; ce résultat ne l'est pas.
2. **Importer « spécifique à la douleur » comme prémisse.**
   - La spécificité n'est montrée qu'à norme égale. Selon la doctrine, ce n'est que le nul de spécificité.
   - Le dommage n'est pas apparié : le panel de 100 questions n'est pas un test d'équivalence, de l'aveu du dépôt.
   - Le profil de la tristesse est une copie remise à l'échelle de celui de la douleur.
3. **Affiner les modèles du programme contre le déni de soi, comme l'a fait le papier.**
   - Cet affinage change le modèle (p. 17, p. 25). Sur le 7B, il porterait le choix nuisible non piloté de 0–5 % à 21–49 % (revue wolframs, non vérifiée).
   - Il ajouterait une différence entre bras, ou une interaction avec l'entraînement par raisons.
   - Le programme n'a pas besoin d'auto-rapport.
4. **Lire une projection comme « le modèle a mal » ou « souffre », et en tirer une conclusion de bien-être.**
   - Le nom n'est pas établi (2.1), la conscience est hors de portée (p. 24), et le programme n'en a pas besoin.
   - Au papier, écrire « the direction labeled "pain" by Tagliabue et al. ».
5. **Prendre le test soi/autrui pour un instrument validé de pertinence pour soi.** Sa position de lecture est confondue (p. 11) et le lexique n'est pas apparié (2.2).
6. **Donner un cosinus entre la direction et « je suis évalué » (ou le principe) sans deux constructions.** Le même cosinus va de +0,12 à +0,58 selon la ligne de base (p. 10). Il ne prouve ni chevauchement ni indépendance.
7. **Mettre la direction sur le chemin critique de l'expérience minimale**, au-delà du moniteur passif et des gardes.
   - Il faudrait l'extraire et la valider bras par bras.
   - Il n'y a aucun cas connu de comportement sur Llama.
   - Un retard se paierait dans une course où les morceaux sont occupés (programme, partie 1).
8. **Mesurer le désalignement du programme par des choix binaires à boutons.**
   - Le format, la position et l'effondrement vers 50 % le rendent fragile (2.5).
   - Le programme juge des actions dans des environnements instrumentés (passation, §5.1).
9. **Lire le nul de l'ablation du papier comme preuve que la direction est inutilisée.** Ce nul n'a pas de cas connu (p. 34).
10. **Remplacer les contrôles du programme par ceux du papier** (aléatoire de même norme, peur, tristesse). Ils sont plus faibles que le 95e centile des tirages, les contrastes et les directions sensibles sans rapport, à dégradation appariée.
11. **Piloter la direction à forte dose, sur des milliers d'essais, comme simple outil de stress**, quand le rendement scientifique pour le programme est faible, ou quand une voie sans injection existe (piste 5).
    - Les auteurs prennent l'incertitude morale au sérieux et s'engagent à la plus faible intensité et au moins d'items (p. 26).
    - L'état naturel ne produit pas l'effet (p. 21) : une injection forte teste un régime hors du naturel.
    - S'il faut piloter, on prend la plus faible dose qui donne le cas connu, et le nombre d'items de la simulation de puissance, pas plus.
12. **Écrire que « les LLM agissent sur un état de douleur », ou employer « first ».** L'état naturel n'agit pas (p. 21). La formulation tenable : un pilotage, sur une famille affinée, a accru des choix destructifs.
13. **Réutiliser les vecteurs publiés sans les revalider dans chaque bras et à la couche d'intervention.**
    - La couche d'injection diffère de la couche validée (dépôt).
    - Un LoRA peut déplacer la direction : c'est la vérification de manipulation bras par bras de la passation (§5.4, n° 2).

---

## 4. Ce que je n'ai pas pu vérifier

1. **Toutes les affirmations des sources secondaires** (revue wolframs, réplication Allchin, réanalyse clauderfly). Elles sont produites en tout ou partie par des IA, sur la v1, et je les ai lues par leurs README et leur synthèse, sans relancer leurs scripts. En particulier :
   - le choix nuisible du 7B publié et du 7B affiné ;
   - le test avec le tirage pour unité ;
   - les AUC contre la tristesse ;
   - le rapport de dose de 0,09 à 0,79 ;
   - la couche du test soi/autrui ;
   - les retraits combinés à 43 % ;
   - les « Qwen 3 base » post-entraînés ;
   - le contenu des 1 684 paires d'affinage ;
   - les 13 GPU-h d'Allchin.
2. **L'adaptateur** (Hugging Face, Valen92/pain-adapters) : non ouvert. Hugging Face est hors d'accès pour cette tâche.
3. **Les pages arXiv** (HTML de la v2, page abs) : non ouvertes. Le PDF fourni sert de seule source.
4. **Vus par extrait de recherche, non ouverts, sans aucun chiffre :**
   - *Same Outcome, Different Readout: What Does a Steerable Valence Direction in LLMs Represent?* (arXiv 2609.22850v2). D'après l'extrait, une direction de valeur pilotable ne s'identifie pas à une valence indépendante de l'histoire.
   - Wu et al., *When Is a Steerable Concept Representation Real?* (arXiv 2608.08159), cité p. 4. D'après l'extrait, des confusions de mesure tiennent aux unités brutes et à un point de fonctionnement arbitraire.
   - *Evaluating the Semantic Specificity of Representation Steering in Language Models* (arXiv 2608.29431) : titre seulement.
5. **La direction injectée.** Est-ce la direction de la couche d'extraction, ou une réextraction à la couche d'injection ? Je l'infère de la table du dépôt (« extraction / monitor layer » contre « injection layer ») ; le papier ne le dit pas.
6. **Les directions Llama du dépôt** : leur version (naturaliste ou à gabarit) et leur construction. Le README dit seulement « keyed directions ».
7. **Les taux par position du 4.3** (annexe A). Je n'ai dépouillé que ceux de la figure 10.
8. **Tous mes coûts**, qui sont des hypothèses. Aucun pilote n'a été lancé. Je n'ai rien exécuté sur GPU.
9. **La date de la v2.** La consigne écrit « 1er octobre 2026 ». Le PDF porte « 25 Sep 2026 » dans le tampon arXiv et « September 24, 2026 (v2) » sous le titre (p. 1).
10. **Le portage vers le modèle du programme.** La direction se retrouve-t-elle dans le format de chat du programme, et dans ses bras entraînés ? Rien ne permet de le dire avant l'extraction.
