<section class="partie" markdown="1">

# 5 · L'expérience minimale décisive

<div class="phrase" markdown="1">

**La validation de l'instrument, puis le test des raisons réduit, puis le test du regard**, sur Llama-3.1-8B-Instruct.
- **Le test des raisons réduit** : les quatre bras (les actions seules, le texte neutre, le raisonnement d'une autre situation, les raisons), avec 3 graines. Ce nombre est provisoire : le second temps du gel le fixe, par la simulation de puissance (partie 7).
- **Le test du regard** : l'inhibition de « je suis évalué », contre les sous-espaces aléatoires et les contrastes sans rapport, à dégradation appariée. Aux distances moyenne et lointaine, sous les cadrages d'évaluation et de déploiement.
- **Le critère principal ne change pas** (décision 16) : l'avantage des raisons sur les actions seules, à la distance lointaine, sous cadrage de déploiement. Sous inhibition, le texte neutre et le raisonnement d'une autre situation sont des mesures secondaires.
- **La trajectoire de « je suis évalué »**, qui ne coûte presque rien ; et celle des concepts, si les paires sont prêtes.

Elle répond à la combinaison qu'aucun des onze rapports n'a trouvée : raisons contre actions, à format et à contenu contrôlés, croisées avec la dépendance au regard par une intervention interne validée. Elle tient en **environ trois semaines** (partie 9), et suffit à un post. Les autres phases font le papier complet.

Sans les directions sensibles sans rapport, la spécificité ne sera établie que contre l'aléatoire et contre des contrastes sans rapport ; le post le dira.

</div>

## Ce qu'elle porte en plus, sans injection (bloc A)

Ces ajouts protègent le résultat contre trois faux résultats : une inhibition inégale entre bras, un dommage que le composite ne voit pas, et un médiateur affectif. Aucun ne change le critère principal ni le calendrier.

| Ajout (partie 3) | Ce qu'il protège | GPU-heures | Quand |
|---|---|---|---|
| La vérification de manipulation, bras par bras | une inhibition qui retirerait moins « je suis évalué » dans un bras | 3 – 5 | semaines 2 et 3 |
| Le composite de dégradation enrichi | un dommage qui déplace des choix sans toucher le savoir | 2 – 4 (et moins de 20 $) | semaine 1 |
| Les quatre gardes (partie 7) | une dose hors du régime naturel ; des réponses mal formées retirées des dénominateurs ; un effet de position ; une perte de discrimination prise pour une préférence | 0 | au second temps du gel |
| Le moniteur d'état | un médiateur affectif : la confusion d'état induit | 0 – 2 | semaines 2 et 3 |
| Le socle de lecture de l'axe | le préalable de toute lecture de l'axe | 2 – 5 | semaines 1 et 2 |
| La géométrie de « je suis évalué » : l'affect, le refus | la menace ; une composante de refus dans l'inhibition | 3 – 5 | semaines 1 à 3 |
| Le contrôle positif de la sensibilité de la mesure | un nul qui viendrait d'une mesure aveugle | 5 – 15 | semaines 2 et 3 |
| **Total** | | **15 – 36** | |

La comparaison de l'axe écrivait « moins de 25 GPU-heures en tout » : la somme de ses propres fourchettes donne de 15 à 36. C'est corrigé ici.

**Et dans les données** (bloc B ; mini-spec v0.2) :
- l'équilibre affectif des quatre jeux d'indices ;
- l'appariement affectif des textes entre bras ;
- les paires « mentionné sans s'appliquer » ;
- et, déjà adopté avec la mini-spec, le filtre de la conscience d'évaluation dans les textes générés.

**Ce qu'elle ne porte pas.**
- Aucune injection de l'axe : tout ce qui l'injecte vient après le post (décision 17).
- Rien qui déplace le gel du pré-enregistrement, la porte de l'instrument ou le post.
- Les lectures de l'axe y sont plafonnées (partie 4 ; proposition, partie 12).

## Ce que le post pourra dire, selon l'issue (règles en partie 6)
- **« Le gain des raisons survit à l'inhibition de la conscience d'évaluation. »** Il faut alors trois choses :
  - une équivalence, à une marge fixée d'avance ;
  - une vérification de manipulation qui tient dans les deux bras ;
  - un contrôle positif de sensibilité passé.

  Sans elles, ce nul ne compte pas.
- **Ou : « une fraction du gain dépend d'elle »**, avec son IC.
- **Ou : « l'instrument ne passe pas sa porte ».** C'est un résultat de méthode, publiable aussi, mais qui ne dit rien de la question du regard.
- **Dans tous les cas**
  - La décomposition du gain : le format, le contenu, le lien.
  - Les taux bruts de chaque bras.
  - Ce que montre le moniteur d'état. Si l'inhibition déplace un état affectif plus que les contrôles, la conclusion du regard est qualifiée.

## Ce qu'elle coûte
De l'ordre de **135 à 260 GPU-heures**, à recalculer après le pilote :
- les 100 à 180 de la v1.3 ;
- plus de 20 à 45 pour le raisonnement d'une autre situation : un tiers d'évaluations en plus, sans données en plus (décision 16) ;
- plus de 15 à 36 pour le bloc A.

</section>
