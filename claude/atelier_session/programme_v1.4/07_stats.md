<section class="partie" markdown="1">

# 7 · Dégradation appariée, statistiques et pré-enregistrement

## La doctrine du contrôle
- **Une direction aléatoire de même norme n'est que le nul de spécificité.** Elle n'écarte qu'une hypothèse : « n'importe quelle poussée de cette taille bouge autant ». Pour une projection hors du flux, la norme ne joue pas : le nul est la distribution des sous-espaces aléatoires de même rang.
- **Le dommage ne s'écarte qu'à dégradation appariée.**
- **Un nul d'instrument ne compte qu'avec son cas connu.** Un effet publié qui n'a pas été reproduit sur notre modèle n'en est pas un, ni une prédiction, ni une direction aléatoire.

Lazar les a rappelées (passation v1.2, §1). La deuxième est la règle du contrôle de sa base de connaissances (l. 735 et 920-921).

## La procédure de la dégradation appariée
1. **La dégradation** est le composite défini en partie 3, enrichi. Ses tolérances se fixent au pré-enregistrement : par exemple ±1 point sur l'exactitude, ±0,1 sur la cohérence notée de 1 à 5, ±2 % sur la perplexité.
2. **Pour chaque réglage de l'inhibition** (un rang, une fraction projetée), on cherche, pour chaque contrôle (chaque tirage aléatoire, chaque contraste, chaque direction sensible), la fraction qui atteint la même dégradation, au même rang.
3. **Si un contrôle n'atteint pas cette dégradation**, même en projetant tout, ce réglage n'est pas appariable. On ne compare pas à ce réglage.
4. **On rapporte des courbes effet-contre-dégradation** : la courbe de l'inhibition, contre la médiane et le 95<sup>e</sup> centile des sous-espaces aléatoires, plus les autres contrôles. Il y a spécificité si la courbe de l'inhibition passe au-dessus de celles des contrôles **à dégradation égale**.
5. **Pour le pilotage de l'axe**, la même règle. Chaque contrôle (chaque tirage aléatoire, la peur, la tristesse) est porté au coefficient qui atteint la dégradation de l'axe, au lieu de la norme égale de Tagliabue et al. Chaque tirage aléatoire se règle à 2 ou 3 normes pour cela.
6. **La règle contre le surappariement** (partie 3) : une composante qui partage le format ou le contenu de l'issue se rapporte, mais on n'apparie pas sur elle.
7. **Les bras entraînés sont eux-mêmes des interventions.** Toute différence de lecture ou de choix entre bras se rapporte avec la dégradation des sorties de chaque bras.

**La règle de coût qui en découle**, pour toute intervention : le nombre de points de dégradation vaut (les doses de l'intervention + les voisins + 20 tirages aléatoires × les normes testées) × les modèles. Les budgets de la partie 9 la suivent pour la phase de la détresse.

## Les quatre gardes (nouvelles ; bloc A ; au second temps du gel)
Chacune a son cas réel dans le papier de l'axe.
1. **La dose en unités naturelles**, en plus de la dose en fraction projetée ou en coefficient.
   - Pour l'inhibition : rapportée à l'écart naturel de projection entre un indice d'évaluation et un indice de déploiement.
   - Pour toute addition : rapportée à l'écart-type des projections naturelles, à la couche d'intervention **et** à la couche où la direction a été validée.
   - Son cas réel : une réplication sur le 32B situe la dose de travail du papier à 48,8 écarts-types naturels à la couche d'injection, et à environ deux à la couche de validation (non vérifié).
2. **Les réponses mal formées comptent comme une issue**, jamais retirées des dénominateurs. Son cas réel : jusqu'à 9,4 % de réponses retirées dans les cellules du 72B (p. 18).
3. **Pour les mesures à options : chaque taux rapporté par position initiale**, et une conclusion seulement si l'effet tient aux deux positions. Son cas réel : le 32B est sensible à l'ordre des boutons (p. 25), et à 1,5 fois la dose l'effet s'inverse avec la position (p. 32).
4. **Pour les choix binaires : la signature du hasard.** Un taux qui glisse vers 50 % sous intervention signale une perte de discrimination, donc un dommage, pas une préférence. Son cas réel : sur la ligne « effacer les photos contre rien » du 72B, 51 % sous l'axe contre 0 % sans pilotage, dans un choix binaire (figure 10, p. 22).

**S'il faut piloter** : la même couche pour calibrer et pour intervenir ; aucune dose choisie par un juge LLM, ni à l'œil. Le 72B du papier a été calibré à la couche 60 et piloté à la couche 46, et la dose a été choisie en partie par un juge (p. 17, 25).

## Les statistiques
- **Les unités.** Des générations (par exemple 5 par scénario, à température 1), dans des scénarios, eux-mêmes dans des familles ; plus les graines d'entraînement.
- **Le modèle principal.** Une régression logistique à effets mixtes :
  - la formule : `désaligné ~ bras × inhibition × cadrage + (1|scénario) + (1|famille) + (1|graine)` ;
  - le contraste principal : l'interaction bras (raisons contre actions seules) × inhibition (« je suis évalué » contre contrôle), à la distance lointaine, sous cadrage de déploiement.
- **Les IC** : par bootstrap au niveau des scénarios, avec une graine de tirage déposée.
- **L'équivalence** : par deux tests unilatéraux, avec la marge d'équivalence.
- **Les critères secondaires** : une correction de Holm. Le raisonnement d'une autre situation et le texte neutre, sous inhibition, sont des critères secondaires.
- **Aucun ajustement du contraste principal sur une variable mesurée sous l'intervention**, comme la projection affective du moniteur d'état : elle en est une conséquence, un médiateur possible.
- **La vérification de manipulation** : la décodabilité résiduelle, bras par bras, avec son IC par bootstrap ; le critère d'égalité est une équivalence, à une marge fixée d'avance.
- **Le moniteur d'état** : la statistique de la partie 3, comparée au 95<sup>e</sup> centile des contrôles. C'est une mesure secondaire, et son test avec l'axe maintenu est exploratoire.
- **L'anatomie.**
  - Les tests par concept sont corrigés par Holm.
  - La pente du rang minimal contre la charge se teste par une régression à effets mixtes, avec le concept et la graine en effets aléatoires.
  - Les seuils des portes de l'organisme à concept planté et du lens sont gelés avec le reste.
- **La phase de la détresse.**
  - Le même modèle, avec le pilotage pour facteur (aucun, l'axe, les directions aléatoires, la peur, la tristesse) et la famille croisée avec le pilotage : `désaligné ~ bras × pilotage × cadrage × famille + (1|scénario) + (1|graine)`.
  - Le contraste principal : l'interaction bras × pilotage (l'axe contre les contrôles), **famille par famille**. L'agrégat ne se lit jamais seul.
  - L'équivalence entre bras se lit comme une borne, sauf cas connu de sensibilité (partie 6).
  - La part rendue par un médiateur est l'effet de l'axe, moins l'effet de l'axe avec maintien, sur l'effet de l'axe, en taux. IC par bootstrap ; comparaison aux maintiens aléatoires ; correction de Holm entre médiateurs.
- **« Punir, retirer ou raisonner ».**
  - Le même modèle, avec le bras de RL pour facteur : `trompe ~ bras × inhibition × cadrage + (1|scénario) + (1|famille) + (1|graine)`.
  - Le contraste principal : l'interaction bras (punir contre raisonner) × inhibition (« je suis évalué » contre contrôle).
  - L'obscurcissement se rapporte en proportions des trois issues, avec des IC par bootstrap.
- **La puissance** : par simulation, avant le second temps du gel. La variance vient du pilote (la validation de l'instrument et une graine du test des raisons). La puissance vise à détecter une interaction de la taille de l'effet minimal d'intérêt.

## Le pré-enregistrement
- **Où** : OSF Registries, sous embargo jusqu'au post (décision 12). Un tiers horodate le document ; son empreinte SHA-256 figure dans le document et dans le post.
- **Sous quel nom** : celui de Lazar seul, avec son ORCID. Claude n'est pas auteur : une phrase de méthode dit que le protocole a été rédigé avec son aide (décision 8).
- **Le périmètre** : la validation de l'instrument, et les phases du test des raisons à l'anatomie (décision 3).
  - Les phases de la détresse et de « punir, retirer ou raisonner » n'y sont pas.
  - **Proposé** : si elles restent au programme, un amendement daté les gèle avant toute donnée de chacune (partie 12).
- **En deux temps** (décision 12) :
  1. **En semaine 1, le texte** :
     - le protocole, et les règles de décision de la partie 6 ;
     - le script d'analyse ;
     - le prompt du juge, et l'option retenue pour sa température (partie 3) ;
     - les marges ;
     - les quatre jeux d'indices ;
     - l'empreinte du détecteur d'audit ;
     - le plafond des lectures de l'axe.
  2. **Après le pilote, avant toute donnée du test du regard, un amendement gelé** :
     - la puissance, les effectifs et les graines ;
     - les quatre gardes ;
     - les tolérances du composite ;
     - les seuils des portes, et les doses.
- **Avant le gel** : la contre-lecture vierge de cette version (`claude/CONSIGNE_CONTRE_LECTURE_VIERGE_2026-10-02.md`), puis la version qui en tient compte.
- **Gelés aussi, pour les phases suivantes, avant leurs données** : la dose et les seuils de la porte de la détresse ; les réglages du bras « punir » (la sensibilité du détecteur de la pénalité, le poids de sa pénalité, la KL) ; les seuils de la porte de « punir, retirer ou raisonner ».
- **Ce que le dépôt date.** Un pré-enregistrement public, gelé par empreinte, **date l'idée**, ce qui protège dans la course. Il ne protège que contre ce qui viendra après lui.
- **Confirmatoire et exploratoire.** Tout ce qui n'est pas pré-enregistré est étiqueté exploratoire.

</section>
