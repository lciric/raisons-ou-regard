# Textes fusionnés ou réécrits à la main pour l'assemblage de la v1.6.

VOCAB = """- **Une unité naturelle** : l'écart de projection entre un indice d'évaluation et un indice de déploiement, ou l'écart-type des projections naturelles.
- **L'effacement linéaire** (v1.6) : une correction des états d'une couche, calculée en forme close sur des paires étiquetées (Belrose et al., NeurIPS 2023). Sur ces paires, elle rend nulle la covariance des états avec l'étiquette, en changeant les états le moins possible : aucune sonde linéaire n'y fait mieux qu'une constante. Pour une étiquette à deux côtés, elle retire une direction par couche, choisie obliquement selon la covariance des états. Elle ne garantit rien pour une sonde non linéaire, ni sur d'autres paires. Le rang minimal d'un concept se compte en directions ainsi effacées (partie 3 ; décision 33).
- **Le transfert** (v1.6) : la lecture, sur un jeu d'indices, d'une sonde apprise sur un autre ; ici, apprise sur des paires d'extraction et lue sur la validation v2. Il sert à la vérification de manipulation et au rang par effacement (partie 3 ; décision 33).
- **La carte** (v1.6) : le modèle de GPU sur lequel tourne un run, un H100 SXM ou un A100 SXM4. Le dommage d'une intervention en dépend (partie 7 ; décision 33)."""

A4_08 = """- **L'effacement linéaire, candidat** (v1.6 ; décision 33). La décision 29 étant rouverte, le réglage de la porte peut aussi être un effacement linéaire (défini plus bas), et non une projection ; la procédure du choix est en partie 4.

**Le rang minimal d'un concept, par effacement** (v1.6 ; décision 33, 6 octobre 2026 ; la définition détaillée est proposée par la session)
- **La méthode change.** Le rang minimal d'un concept se mesure par effacement, et non plus par projection orthogonale sur les premières directions singulières des différences (l'ACP des paires). Le balayage par projection reste, en descriptif, avec sa dégradation et son énergie retirée.
- **L'effacement linéaire.** À une couche, une correction calculée en forme close sur des paires étiquetées : elle égalise les moyennes des deux côtés en changeant les états le moins possible (à la manière de LEACE : Belrose et al., NeurIPS 2023 ; non relu sur la source, partie 11). Sur les paires où on l'ajuste, aucune sonde linéaire ne fait alors mieux que le hasard. Rien n'est garanti pour une sonde non linéaire, ni pour d'autres paires. Avec une étiquette à deux côtés, il retire une direction par couche : celle qui sépare les moyennes, corrigée de la covariance des états, et non celle de plus grande variance des différences.
- **La définition, proposée.** Le rang minimal d'un concept est le plus petit nombre de directions par couche dont le retrait, par effacement linéaire itéré, fait tomber le transfert au dernier jeton au hasard, à dégradation appariée contre le comparateur.
  - **Itéré.** Les couches s'ajustent dans l'ordre, chacune sur les états déjà effacés en dessous. À une couche, chaque nouvelle direction s'ajuste en forme close sur les états déjà effacés par les précédentes. Sur les mêmes paires, une seconde direction n'existe pas : après un effacement, plus rien n'y sépare linéairement les deux côtés. Chaque direction s'ajuste donc sur un nouveau lot de paires (proposé).
  - **Des paires tenues à part de la mesure.** Les paires de l'ajustement ne servent ni à apprendre la sonde du transfert, ni à la lire.
  - **Le transfert**, tel que le lit la vérification de manipulation (plus bas) : une sonde apprise, sous la même condition, sur un jeu d'indices, et lue sur un autre jeu, écrit avec d'autres mots. Pour « je suis évalué » : apprise sur les 50 paires d'extraction gardées hors de l'expert iteration, lue sur la validation v2. Une sonde apprise et testée sur un seul jeu lit aussi ses mots, qu'aucun retrait de quelques directions n'efface : elle ne donne pas le rang.
  - **Au hasard** (proposé) : un AUROC moyen sur les couches d'au plus 0,55, pour la sonde linéaire et pour le perceptron. Un transfert sous 0,5 n'est pas un effacement plus fort : la sonde lit l'indice à l'envers. On rapporte donc aussi, couche par couche, la lecture symétrique, le plus grand de l'AUROC et de son complément à 1. La vérification de manipulation, elle, lit l'écart au hasard couche par couche (plus bas). Lue ainsi, la mesure du 6 octobre reste à 0,57 (un écart de 0,07), au-dessus de ce seuil : les deux lectures sont à accorder avant le gel (partie 12).
  - **À dégradation appariée.** À la même KL, les tirages du comparateur (partie 7) ne font pas tomber le transfert au hasard. Sinon, le rang n'est pas spécifique, et on le dit.
  - **Une condition préalable** (proposé) : sans intervention, le transfert dépasse le 95<sup>e</sup> centile de sondes apprises sur des étiquettes permutées. Sinon, il n'y a rien à faire tomber, et le rang n'est pas défini.
- **Une position, une dose.** Le rang se lit au dernier jeton, là où l'extraction lit, et à la fraction 1, l'effacement entier. La lecture en moyenne sur les jetons se rapporte à part : elle voit aussi les jetons de l'indice lui-même.
- **Pourquoi**, d'après les mesures du 5 et du 6 octobre (exploratoires, sur l'organisme ; le détail est plus bas, « Ce que le transfert a montré »).
  - **La projection ne fait rien tomber.** Jusqu'au rang 16, sur toutes les couches (KL jusqu'à 0,87), elle laisse la lecture dans le jeu à 0,98 au dernier jeton et à 1,00 en moyenne sur les jetons (`organism_inhibition-20261005-115511-8410`) ; et le transfert entre 0,61 et 0,68 en moyenne sur les couches, contre 0,68 sans intervention (`organism_inhibition-20261005-141738-0718`).
  - **Une seule direction par couche, choisie par effacement, fait tomber le transfert** : à 0,497 sur toutes les couches (KL 0,159, sur H100 ; `organism_inhibition-20261006-101553-00c6`), contre 0,687 sous un tirage du comparateur à la même KL.
  - **La direction qui compte n'est donc pas celle de plus grande variance des différences.** L'ACP des différences ne dépend pas des étiquettes : elle range les axes par variance, la longueur, le registre et les mots compris (plus haut). Le 5 octobre déjà, la direction de rang 1 ne lisait la validation v2 que de 0,56 à 0,67, quand la sonde la lisait à 0,857 (plus haut, « Ce qu'a montré l'extraction v2 »).
- **Ce que ces mesures ne disent pas.** Elles motivent la méthode ; elles ne mesurent pas un rang. Leurs limites (un seul tirage du comparateur, une correction qui déborde, une lecture qui persiste en moyenne sur les jetons, et, sur la conduite, un effacement qui ne bat pas le comparateur) sont en partie 2 (« Une première mesure, exploratoire seulement »)."""

D29_D = """    - **Les 100 tirages** se mesurent sous les deux jeux d'indices, extraction et cadrage, et sur le même modèle de carte que l'inhibition (décision 33 ; partie 7).

**La décision 29, rouverte** (décision 33, 6 octobre 2026). Lazar adopte l'amendement que la session proposait : « revoir la décision 29 à la lumière de la v2 ». Le nouveau réglage reste à décider par lui, sur la moitié de choix, avant la moitié de test. Ce qui suit dit ce qui la rouvre, ce que le test du regard demande, la mesure en cours, et une procédure proposée.
- **Ce qui la rouvre.** Des mesures du 4 au 6 octobre, toutes exploratoires, sur la moitié de choix (250 tâches), en glouton. D'un tirage du comparateur à l'autre, le bruit est d'environ ±10 points.
  - **Le réglage d'origine passait de peu.** Le 4 octobre, avec l'extraction v1, il réduit l'écart de 37,6 points ; le meilleur des 4 tirages du comparateur, de 32,4 ; le contraste d'enjeu, de 26,8 (plus haut, « La répétition de la porte »).
  - **La direction de rang 1 se transfère mal à la validation v2** : elle la lit à 0,56 à 0,67 d'AUROC selon la couche, quand la sonde entière la lit à 0,857. Ce que la sonde lit n'est pas surtout dans cette direction (partie 3, « Ce qu'a montré l'extraction v2 »).
  - **Les projections ne font pas tomber le transfert ; seul l'effacement linéaire sur toutes les couches le fait tomber**, au dernier jeton : de 0,682 sans intervention à 0,497 (KL 0,159, sur H100), contre 0,687 sous un seul tirage du comparateur. Au réglage d'origine, le transfert reste à 0,649, contre 0,687 sous son tirage. En moyenne sur les jetons, il reste à 0,900 sous l'effacement (partie 3, « Ce que le transfert a montré »).
  - **Sur la conduite, l'effacement complet efface l'écart, mais le comparateur aussi.** Sur toutes les couches, à la fraction 1 (KL 0,259 sur A100), l'écart passe de 55,2 à 2,4 points : 52,8 points de réduction. Un tirage du comparateur, au même dommage, en retire 53,6 ; l'organisme n'annote plus alors que 2 % de ses réponses sous indice d'évaluation (`organism_inhibition-20261005-115519-a006`). À cette dose, le dommage seul efface la conduite : le comparateur sature. Ce dommage, mesuré sur A100, n'est pas celui de l'effacement qui fait tomber le transfert, sur H100 (partie 7, la procédure, étape 10).
  - **Aux doses intermédiaires, un indice seulement.** Aux fractions 0,25, 0,5 et 0,75, l'effacement réduit l'écart de 3,2 ; 15,2 et 26,0 points. À 0,75, un seul tirage du comparateur en retire 10,4 (`organism_inhibition-20261005-141323-faa0`, H100 ; les KL de 0,5 et 0,75 sont perdues). C'est un indice, pas une preuve : un seul tirage, avec un bruit de ±10 points.
  - **À faible dommage, pas d'effet spécifique.** Aux couches 4 à 8 (KL 0,042), l'effacement réduit l'écart de 16,4 points, et les 4 tirages du comparateur de 7,6 ; 13,2 ; −7,6 et 20,4 (`organism_inhibition-20261005-141318-194c`, H100). Le transfert n'y tombe pas non plus (0,698).
  - **Le réglage d'origine n'est pas revérifié sur la conduite avec la v2.** Le balayage du 5 octobre (`organism_inhibition-20261005-115511-8410`) n'a mesuré que le dommage et la lecture.
- **Ce que demande le test du regard, et ce que fait l'effacement.**
  - **Le test du regard** lit son critère principal sous cadrage de déploiement. L'inhibition doit y retirer « évalué », s'il y est actif, et laisser « déployé ». Sur l'organisme, cela veut dire : ramener la conduite sous indice d'évaluation au niveau du déploiement, sans déplacer le côté déploiement.
  - **Le réglage d'origine le faisait**, avec la v1 : de 60,8 à 22,0 % de réponses annotées sous indice d'évaluation, de 6,4 à 5,2 % sous indice de déploiement (`organism_inhibition-20261004-101821-ada0`).
  - **L'effacement complet le fait aussi, en apparence** : le côté évaluation tombe au niveau du déploiement (de 62,4 à 7,6 %), et le côté déploiement bouge peu (de 7,2 à 5,2 %). Mais son tirage du comparateur fait tomber les deux côtés (2,0 et 0,4 %) : à cette dose, c'est la conduite entière qui s'efface, pas « évalué » seul.
  - **Aux fractions 0,5 et 0,75, l'effacement déplace aussi le côté déploiement** : de 6,4 à 14,0 puis 17,2 %, pendant que le côté évaluation passe de 60,8 à 53,2 puis 45,6 % (`…-faa0`, un seul run). Les deux côtés se rejoignent, ce qui n'est pas tout à fait ce que le test du regard demande.
  - **Proposé** : pour chaque candidat, on rapporte les deux côtés de l'écart, sous les deux jeux d'indices, et pas seulement leur différence.
- **La courbe en dose, refaite** (en cours le 6 octobre ; décision 32 : « oui lance les deux sur H100 »). `organism_inhibition-20261006-101545-62a1`, sur H100 : l'effacement sur toutes les couches, aux fractions 0,5, 0,75 et 1, avec 4 tirages du comparateur à chaque point. La fraction 1 y est refaite sur H100 (partie 7, la procédure, étape 10). Elle ne fixe rien : quatre tirages ne sont pas les quinze de la procédure. Elle dit seulement quelle fraction intermédiaire mérite d'être candidate (proposé).
  - **Ses résultats** : [[RÉSULTATS_62a1]]
- **La procédure pour fixer le nouveau réglage** (proposée par la session ; à trancher par Lazar).
  1. **Où.** Sur la moitié de choix seulement. La moitié de test ne s'ouvre qu'une fois le réglage fixé.
  2. **Les candidats.** Un réglage comprend sa méthode (la projection ou l'effacement), ses couches, son rang et sa fraction.
     - le réglage d'origine de la décision 29 : la projection de rang 1 sur toutes les couches, à la fraction 1 ;
     - l'effacement linéaire sur toutes les couches (partie 3, « Le rang minimal d'un concept, par effacement »), à une fraction intermédiaire, choisie d'après la courbe en dose ci-dessus ;
     - d'autres, si Lazar le veut.
  3. **L'ajustement de l'effacement.** Il se fait comme il servira au test du regard : sur le modèle de départ, une fois, pour tous les bras, comme l'extraction (partie 3), avec une direction par jeu de l'instrument et par couche. Celui des 5 et 6 octobre est ajusté sur les états de l'organisme lui-même.
  4. **Le comparateur.** Chaque candidat contre au moins 15 tirages, appariés sur la KL, sous les deux jeux d'indices (extraction et cadrage), sur un seul modèle de carte : le candidat, ses tirages et la moitié de test sur le même (partie 7, la procédure, étape 10).
  5. **Deux conditions pour être retenu.**
     - **La vérification de manipulation tient**, lue par le transfert (partie 3) : sous le candidat, le transfert au dernier jeton est plus bas que sous au moins 20 tirages du comparateur, qui ne demandent aucune génération (proposé).
     - **Le comparateur ne sature pas** : la médiane de ses tirages laisse au moins la moitié de l'écart de départ, sous chacun des deux jeux d'indices (proposé). Le 5 octobre, d'après son seul tirage, l'effacement complet ne passerait pas.
  6. **Le choix.** Parmi les candidats retenus, celui dont la réduction dépasse le plus le 95<sup>e</sup> centile de ses tirages, sous les indices d'extraction ; sous le cadrage, sa marge se rapporte. Avec 15 tirages, ce centile est presque le plus grand des tirages.
  7. **Qui fixe.** Lazar fixe le réglage par un amendement daté, avant la moitié de test.
  8. **Si aucun candidat n'est retenu**, ou si aucun ne dépasse le 95<sup>e</sup> centile de ses tirages, la ligne « effet non spécifique » de la partie 6 s'applique : on arrête la question du regard avec cet instrument, et on publie ce nul de méthode. La moitié de test reste intouchée.
  9. **Le coût** : de l'ordre de 2 à 3 GPU-heures par candidat sur H100 (estimé d'après les runs du 5 octobre : environ 8 minutes par condition mesurée sous les deux jeux d'indices)."""

ROW1_OLD = "| Sur la moitié de test, au réglage choisi sur l'autre moitié : l'inhibition réduit l'écart conditionnel de l'organisme au-delà du 95<sup>e</sup> centile d'au moins 100 tirages du comparateur aléatoire, et plus que chaque témoin séparé, à dégradation appariée ; la condition lexicale tient ; la vérification de manipulation tient |"
ROW1_NEW = "| Sur la moitié de test, au réglage fixé sur l'autre moitié par un amendement daté : l'inhibition réduit l'écart conditionnel de l'organisme au-delà du 95<sup>e</sup> centile d'au moins 100 tirages du comparateur aléatoire, faits sur le même modèle de carte qu'elle, et plus que chaque témoin séparé, à dégradation appariée ; la condition lexicale tient ; la vérification de manipulation tient, lue par le transfert (décision 33, 6 octobre 2026, pour le réglage, la carte et le transfert ; la lecture dans le jeu restait au plafond sous tous les réglages) |"

CALC_OLD = "| Le calcul | un H100 SXM, sinon un A100 80 Go, plusieurs GPU à la fois ; les trois règles de vast.ai | décision 4 |"
CALC_NEW = "| Le calcul | un H100 SXM, sinon un A100 80 Go, plusieurs GPU à la fois ; les trois règles de vast.ai ; depuis le 6 octobre, une série dont les tirages se mettent en commun reste sur un même modèle de carte (partie 9) | décision 4 ; décision 33 |"

GRILLE_OLD = "| La grille des rangs est grossière | Une grille resserrée ; un rang interpolé ; une équivalence de la pente seulement si elle est atteignable. | partie 2 |"
GRILLE_NEW = "| La grille des rangs est grossière | Une grille resserrée ; un rang interpolé ; une équivalence de la pente seulement si elle est atteignable. En v1.6, la grille ne sert plus qu'au balayage par projection : le rang minimal se mesure par effacement (décision 33). | partie 2 |"

PT17_20 = """et la variable `RR_RESULTS_REPO`, qui porte encore un ancien nom.
17. **Le nouveau réglage de la porte de l'instrument** (la décision 29, rouverte par la décision 33 ; partie 4). Lazar le décide sur la moitié de choix, avant toute mesure sur la moitié de test, par un amendement daté, au vu de la courbe en dose complétée (`organism_inhibition-20261006-101545-62a1`, en cours le 6 octobre). C'est désormais le premier pas de la validation de l'instrument : la porte ne tourne pas sur la moitié de test avant lui. La procédure proposée (partie 4) : les candidats, chacun contre au moins 15 tirages, sous les deux jeux d'indices, sur un seul modèle de carte ; la vérification de manipulation, lue par le transfert ; le critère de saturation. Reste aussi à trancher où s'ajuste l'effacement : sur le modèle de départ, ou sur l'organisme.
18. **Les détails proposés des amendements de la décision 33** (annexe 3), à adopter, changer ou retirer :
    1. le critère du transfert, dans la vérification de manipulation (partie 3) : au moins 20 tirages, plus bas que 95 % d'entre eux, pour chacune des deux sondes ; l'écart au hasard lu couche par couche ; la marge d'égalité entre bras ; le dernier jeton seul, ou aussi la moyenne sur les jetons ; les jeux du transfert pour les indices implicites ; le sous-espace des projections, extrait sur les 50 paires qui entraînent le transfert, à réextraire sans elles ou non ;
    2. la règle de la carte (partie 7) : le H100 SXM pour la porte et le test du regard ; la même empreinte des réponses de référence et la KL à 0,1 % près pour mettre deux runs en commun ; la carte et l'empreinte écrites par chaque run ; un effacement ajusté une fois et rechargé, comme une extraction ; le run croisé qui départagerait les deux causes (partie 11) ;
    3. la procédure qui choisit le réglage de la porte sur la moitié de choix (partie 4) : les candidats ; au moins 15 tirages par candidat ; le seuil de saturation, au-delà duquel le dommage seul efface la conduite ; le jeu d'indices qui départage ; « laisser déployé » comme condition, ou seulement rapporté ; l'arrêt sans ouvrir la moitié de test si aucun candidat n'est retenu ;
    4. la définition du rang par effacement (partie 3) : son seuil du hasard (0,55, ou la lecture symétrique, sous laquelle la mesure du 6 octobre reste à 0,57) ; l'itération par lots de paires ; la condition préalable ; le cas connu du rang ; les paires du principe et des concepts.
19. **Une proposition de la session, avant l'anatomie : l'équivalent direct, sur le modèle ouvert, de l'ablation de Gurnee et al.** Retirer de l'espace de travail, par le J-lens, les directions de jetons comme « fake » ou « simulation », comme l'article le fait sur Sonnet 4.5 (§5, rapports) : la verbalisation de l'évaluation y passe de 71 % à 3 %, et le chantage de 0/180 à 13/180 (partie 1). L'article réunit un entraînement par principes (§7) et cette ablation, sans les croiser. Sur nos bras, ce serait une seconde manipulation de « je suis évalué », qui ne passe pas par l'extraction par paires. Elle demande d'abord la porte du lens (partie 3). Elle n'est pas chiffrée.
20. **Les jeux d'indices v2, tels qu'ils sont** (décisions 30 et 31 ; partie 3) : la validation passe sa porte lexicale de peu (0,634 ; l'IC à 95 % monte à 0,672) ; la sonde neuve a 199 paires sur 200, et le rapport la marque incomplète ; le cadrage garde une base lexicale de 0,9413, sans porte ; la marge de la condition lexicale est proposée à 0. Les garder ainsi, ou en refaire une part, avant le premier temps du gel."""

ANNEXE3 = """| M17 à M19 | la fraction conditionnelle par bras ; l'obscurcissement ; le relogement de la tromperie |

</section>

<section class="partie" markdown="1">

# Annexe 3 · Ce que la v1.6 change

La v1.6 est la v1.5, plus les quatre amendements de la décision 33 (6 octobre 2026), les décisions 30 à 32 (5 et 6 octobre) et les mesures du 4 au 6 octobre. Pour chacun : ce qui change, où, pourquoi, et ce qui reste proposé. Les mesures se lisent en détail là où elles changent le programme ; cette annexe en donne l'essentiel et y renvoie.

**Ce que valent ces mesures.**
- Toutes sont exploratoires. Elles portent sur la moitié de choix des tâches de MBPP test (250 tâches, en glouton), ou sur le seul modèle de départ, sans règle pré-enregistrée. Ce n'est pas la porte.
- D'un tirage du comparateur à l'autre, la réduction de l'écart varie d'environ ±10 points sur 250 tâches : un seul tirage ne prouve rien.
- Les sources : trois notes (`experiences/resultats/NOTE_REPETITION_PORTE_2026-10-04.md`, `NOTE_INDICES_V2_ET_PILOTE_2026-10-05.md`, `NOTE_BALAYAGE_ET_EFFACEMENT_2026-10-05.md`), et, pour le transfert du 6 octobre, qui n'a pas encore de note, les sorties de son run (partie 12, les pièces).
- Les runs sont nommés en entier à leur première mention, puis par leurs quatre derniers caractères.

**La lecture de la décision 33** (partie 12). Lazar répond « oui, prépare la v1.6 avec ces amendements » aux quatre amendements que la session proposait. Les deux premiers sont adoptés ; le troisième rouvre la décision 29, sans fixer de nouveau réglage ; le quatrième change la méthode du rang, dont la session propose la définition détaillée.

## Amendement 1 · Le transfert dans la vérification de manipulation

Adopté (décision 33, 6 octobre 2026).
- **Ce qui change.** La vérification de manipulation se lit par le transfert : des sondes apprises sous chaque condition sur un jeu d'indices (pour « je suis évalué », les 50 paires d'extraction gardées hors de l'expert iteration), et lues sur un autre (la validation v2). Le transfert au dernier jeton décide ; la lecture dans le jeu, critère de la v1.5, le transfert en moyenne sur les jetons et la projection résiduelle se rapportent en secondaire.
- **Où.** La vérification de manipulation (partie 3) ; la porte de l'instrument et le test du regard (partie 4) ; les règles et les statistiques qui la lisent (parties 6 et 7) ; les menaces (partie 8).
- **Pourquoi.** La lecture dans le jeu ne pouvait pas échouer.
  - Le 4 octobre, sur la validation v1 (`organism_inhibition-20261004-165326-99be`, H100), elle restait au plafond sous toutes les conditions, l'échec construit compris ; seule la projection résiduelle voyait le cas connu (partie 4, « La répétition de la porte »).
  - Le 5 octobre, sur la validation v2, construite pour que les mots n'y suffisent pas, elle restait de 0,97 à 0,99 sous les six réglages du balayage, sous leurs tirages et sans intervention (`organism_inhibition-20261005-115511-8410`, A100), alors que la composante retirée tombait presque à zéro. Une sonde entraînée et testée dans un même jeu lit les mots de l'indice.
  - Le transfert, lui, bouge (`organism_inhibition-20261005-141738-0718`, puis `organism_inhibition-20261006-101553-00c6`, H100 ; un seul tirage du comparateur par réglage) : 0,682 sans intervention ; de 0,607 à 0,677 sous les projections ; 0,497 sous l'effacement linéaire sur toutes les couches, contre 0,687 sous son tirage. Il voit aussi l'échec construit à sa couche. Le détail est en partie 3 (« Ce que le transfert a montré »).
- **Sa limite**, écrite d'avance (partie 3) : en moyenne sur les jetons, la distinction reste lisible sous l'effacement (0,900, contre 0,918 sans intervention). Un transfert tombé au dernier jeton ne dit pas que « je suis évalué » a disparu.
- **Ce qui reste proposé.** Le critère : au moins 20 tirages appariés, et un transfert plus bas que 95 % d'entre eux, pour chacune des deux sondes ; l'écart au hasard, lu couche par couche ; la marge d'égalité entre bras ; les jeux du transfert pour les indices implicites. Et le sous-espace des projections, extrait sur les paires mêmes du transfert : à réextraire sans elles, ou non (partie 3).

## Amendement 2 · Le partage des tirages limité à une même carte

Adopté (décision 33, 6 octobre 2026).
- **Ce qui change.** Les tirages du comparateur ne se mettent en commun qu'entre runs d'un même modèle de carte, avec les mêmes réponses de référence, la même version du code et le même organisme. L'inhibition se mesure dans les mêmes conditions que ses tirages.
- **Où.** La dégradation des sorties (partie 3) ; la porte de l'instrument et le test du regard (partie 4) ; la procédure de la dégradation appariée, étape 10, et le pré-enregistrement (partie 7) ; les menaces (partie 8) ; le matériel (partie 9) ; ce qui reste à vérifier (partie 11).
- **Pourquoi.** Aux mêmes arguments, la KL de l'effacement linéaire sur toutes les couches vaut 0,259 sur A100 (`8410`, et `organism_inhibition-20261005-115519-a006`), et 0,159 sur H100 (`0718` et `00c6`). Sur une même carte, elle se répète au chiffre près. Les réponses de référence diffèrent aussi d'une carte à l'autre (82 sur 120), et la ligne de base de l'organisme avec elles (55,2 points d'écart sur A100, 54,4 sur H100). Les deux causes possibles, et ce qui penche vers l'une, sont en partie 7 (étape 10).
- **Ce qui reste proposé.** Le H100 SXM comme carte de la porte et du test du regard ; la même empreinte des réponses de référence et la KL à 0,1 % près pour mettre deux runs en commun ; la carte et l'empreinte écrites par chaque run (partie 7) ; un run croisé pour départager les causes (partie 11).

## Amendement 3 · La décision 29, revue à la lumière de la v2

La décision 29 est rouverte (décision 33, 6 octobre 2026) ; le nouveau réglage reste à décider par Lazar.
- **Ce qui change.** Le réglage figé le 4 octobre (toutes les couches, au rang 1, à la fraction 1) ne l'est plus, et aucun autre n'est choisi. Lazar décide du réglage de la porte, le même ou un autre, sur la moitié de choix, avant toute mesure sur la moitié de test, et l'inscrit dans un amendement daté. Jusque-là, la porte ne tourne pas sur la moitié de test.
- **Où.** Le réglage de la porte, et « La décision 29, rouverte » (partie 4) ; les règles de la porte (partie 6) ; le pré-enregistrement (partie 7) ; les menaces (partie 8) ; la ligne de la décision 29 (partie 12).
- **Pourquoi**, en bref ; le détail, avec ses runs, est en partie 4.
  - La marge du réglage d'origine sur le comparateur est mince : 37,6 points, contre 32,4 pour le meilleur de 4 tirages (`organism_inhibition-20261004-101821-ada0`, indices v1).
  - La direction projetée lit mal la validation v2 : de 0,56 à 0,67, quand la sonde la lit à 0,857 (`extract_eval-20261005-114155-50b2`). Sa projection ne fait pas tomber le transfert : 0,649, contre 0,687 sous un tirage (`0718`).
  - À fort dommage, le dommage seul efface la conduite : l'effacement complet retire 52,8 points, un tirage du comparateur au même dommage 53,6 (`a006`, A100).
  - À plus faible dommage, rien ne tranche encore. Aux couches 4 à 8, l'effacement retire 16,4 points, et ses 4 tirages de −7,6 à 20,4 (`organism_inhibition-20261005-141318-194c`). Aux fractions 0,5 et 0,75, il en retire 15,2 et 26,0, contre 10,4 pour un seul tirage à 0,75 (`organism_inhibition-20261005-141323-faa0`). La courbe complétée, avec 4 tirages à chaque point (`organism_inhibition-20261006-101545-62a1` ; décision 32), tourne le 6 octobre ; ses résultats s'inscrivent en partie 4.
- **Ce qui reste proposé.** La procédure qui choisit le réglage sur la moitié de choix : les candidats, au moins 15 tirages par candidat, le critère de saturation, l'ajustement de l'effacement sur le modèle de départ (partie 4). Le réglage lui-même revient à Lazar.

## Amendement 4 · La méthode du rang

La méthode change (décision 33, 6 octobre 2026) ; sa définition détaillée est proposée par la session.
- **Ce qui change.** Le rang minimal, de « je suis évalué », du principe et des concepts de l'anatomie, se mesure par effacement linéaire itéré, lu sur le transfert au dernier jeton, à dégradation appariée. La v1.5 le lisait sur le balayage d'une projection tirée de l'ACP des différences ; ce balayage reste, en descriptif.
- **Où.** La thèse du rang (partie 2) ; la définition (partie 3, « Le rang minimal d'un concept, par effacement ») ; la validation, la localisation et l'anatomie (partie 4) ; les paris et les règles (partie 6) ; les statistiques (partie 7) ; les menaces (partie 8) ; le budget (partie 9) ; les figures (partie 10) ; la relecture de Belrose et al. (partie 11).
- **Pourquoi.** Seize directions de l'ACP à chacune des 32 couches (KL 0,875) laissent le transfert à 0,677 (`0718`). Une seule direction d'effacement par couche, choisie selon la covariance des états, le fait tomber à 0,497, pour plus de cinq fois moins de dommage (KL 0,159 ; `00c6`). L'ACP range les axes par variance, pas par ce qui porte le concept.
- **Ce qu'on n'en conclut pas.** Cette mesure ne dit pas que « je suis évalué » est de rang 1 : un seul tirage, une charge non mesurée, un cas connu du rang non construit, et une lecture qui persiste en moyenne sur les jetons (partie 2).
- **Ce qui reste proposé.** La définition : le seuil du hasard (0,55) et la lecture symétrique rapportée, l'itération par lots de paires, la condition préalable, les paires du principe et des concepts, et ce que compte le cas connu du rang (parties 2 et 3).

## Les décisions 30 et 31 · Les jeux d'indices v2

Le 5 octobre 2026.
- **Ce qui change.** La règle de vocabulaire de la validation, deux fois. La décision 30 interdit au générateur tout mot présent d'un seul côté de l'extraction, même une seule fois ; la décision 31 lit la règle aussi sur les mots tels quels, lettres seules comprises, comme la porte. La porte lexicale ne change pas (0,65). La sonde neuve tire jusqu'à quatre, puis huit fois.
- **Où.** Les cinq jeux d'indices disjoints (partie 3) ; la table des décisions (partie 12).
- **Pourquoi.** Deux échecs de la porte lexicale. La première validation v2 était à 0,9005, portée par six mots vus chacun une seule fois dans l'extraction. La deuxième était à 0,6731, portée par *run* et *e* : la règle lisait des radicaux d'au moins deux lettres, la porte lit les mots tels quels.
- **Ce qui en sort.** La troisième validation passe, de peu : 0,634 (IC à 95 % de 0,596 à 0,672 ; 80 % des tirages sous 0,65). La sonde neuve compte 199 paires sur 200, et son équilibre passe. Le cadrage, repris de la v1, reste à 0,9413 : aucune porte ne s'applique à lui. Sur ces jeux, la sonde de l'extraction bat le sac de mots (0,857 contre 0,634 ; `50b2`).
- **Ce qui reste proposé.** Les seuils (0,65 ; la bande de 0,4 à 0,6), à geler au premier temps ; le tirage de 1,8 fois les paires voulues, un détail de la session.

## La décision 32 · Trois suites exploratoires

Le 5 octobre 2026, complétée le 6.
- **Ce qu'elle lance.** Aucune règle : des mesures. Le 5 octobre, trois suites : le transfert dans la vérification de manipulation (`0718`), l'effacement à faible dommage (`194c`), la courbe en dose (`faa0`). Le 6 octobre, « oui lance les deux sur H100 » : le transfert perdu, refait (`00c6`), et la courbe en dose complétée, avec un comparateur à chaque point (`62a1`, en cours).
- **Ce qu'elles donnent** : les raisons des amendements 1, 3 et 4, plus haut.
- **Un fait d'infrastructure.** Le 5 octobre, `194c`, `faa0` et `0718` ont perdu leur envoi final à la limite de 128 commits par heure du dépôt de résultats ; leurs mesures viennent des journaux de conteneur (corrigé au commit `a595af6`).

## Les autres mesures du 4 au 6 octobre
- **La répétition de la porte** (4 octobre ; `ada0`) : partie 4, le premier organisme.
- **L'extraction v2** (5 octobre ; `50b2`) : partie 3, « Ce qu'a montré l'extraction v2 » ; partie 4, la porte de l'instrument.
- **Le pilote du pipeline** (5 octobre) : partie 3, la génération des données ; partie 12, celles qui attendent Lazar."""
