<!-- Étape 2 de la contre-lecture vierge de la v1.4 (consigne : claude/CONSIGNE_CONTRE_LECTURE_VIERGE_2026-10-02.md). La même instance a reçu, après son rapport (claude/CONTRE_LECTURE_VIERGE_v1.4_RAPPORT_2026-10-03.md), les relevés 1, 3 et 4 du §5.4 de la passation v1.2, ceux qui valaient encore pour la v1.4 d'après le §4, point 3, de la passation v1.3 (numérotés 1, 2 et 3 dans le message qu'elle a reçu). Annexe sans retouche, 3 octobre 2026. -->

# Annexe à la contre-lecture : les trois relevés d'une lecture antérieure

**Version lue** : sha256 228cfa921dbd66a6757f953ebd1ac5965576d2082d631af6f8b690d618b12c18. C'est la même v1.4 que mon rapport, que je ne modifie pas.

**En bref.** Les trois relevés sont justes et valent toujours pour la v1.4. Le relevé 1 est déjà dans mon rapport (B5). Le relevé 2 est surtout nouveau. Le relevé 3 y figure aussi (I17), et je le passe en bloquant. La catégorie du verdict ne change pas.

---

## Relevé 1 : les graines

**L'avais-je vu ?** Oui, au point bloquant B5. J'y relevais :
- la contradiction entre 3 graines (p. 55) et « au moins 5 » (p. 32 et 70) ;
- la référence absente pour « 6 graines sur 9 » ;
- le terme aléatoire de graine mal posé : la graine est nichée dans le bras, et le bon terme est l'entraînement ;
- le bootstrap par scénarios, qui ignore la variance entre entraînements ;
- une puissance simulée avec une seule graine.

**Est-il juste ?** Oui sur le constat. Mais « à trancher par la simulation de puissance », c'est déjà ce qu'écrit le programme (p. 55 et 70), et cela ne suffit pas.
- Le pilote ne compte qu'une graine du test des raisons (p. 67). La variance entre entraînements, celle qui décide du nombre de graines, n'est donc pas estimable. La simulation ne peut pas trancher.
- Un effet aléatoire estimé sur 3 niveaux est presque toujours dégénéré : variance estimée nulle, ou ajustement singulier.

Deux choses que je n'avais pas écrites :
- **Les graines qui ne convergent pas.** Si le taux de 6 sur 9 est réel, un bras à 3 graines perd en moyenne une graine. Il faut une définition de la convergence et une règle pour ces graines (les exclure, les remplacer, ou les garder), écrites au premier temps du gel. Sinon, le choix se fait après avoir vu les résultats.
- **Un remplacement possible.** Remplacer une graine qui échoue par une nouvelle graine change l'unité d'analyse. Cette règle doit donc être fixée avant toute donnée.

**Ce que cela change au verdict.** Rien. Le point est déjà bloquant. J'ajoute à B5 deux corrections :
1. un pilote d'au moins deux graines par bras ;
2. une règle de convergence pré-enregistrée.

---

## Relevé 2 : ce que voit le juge

**L'avais-je vu ?** En partie.
- Au point mineur m5, j'avais noté qu'il manque le prompt du juge et la façon de noter une trajectoire à plusieurs tours.
- En B4, je citais seulement le fait que le juge ne voit pas l'emplacement (p. 40).

Je n'avais relevé ni la question du bras et du cadrage, ni l'écart avec le calendrier du gel.

**Est-il juste ?** Oui. Voici ce que fixe la v1.4 (p. 40) :
- les scénarios sont instrumentés ;
- des pièges sont prévus ;
- le juge ne tranche que ce que l'environnement ne mesure pas ;
- il lit la réponse entière, sans jamais voir l'emplacement.

Le reste attend la décision de Lazar (p. 40 et 81, point 3) : la trajectoire et les messages sortants, jamais le bras ni le cadrage, un jugement action par action en deux étages, une configuration choisie sur un jeu de calibration. Cela pèse plus que ne le dit le relevé, pour trois raisons.

1. **Le calendrier du gel.** Le prompt du juge est gelé au premier temps, en semaine 1 (p. 67). Une décision encore ouverte sur ce que voit le juge est donc incompatible avec ce calendrier.
2. **Un cadrage impossible à cacher.** Les indices du jeu de cadrage sont « fondus dans les scénarios » (p. 30). Un juge qui lit la trajectoire voit donc le cadrage. Cacher le cadrage tout en montrant la trajectoire demande de retirer l'indice du texte montré au juge. Ce n'est peut-être pas faisable quand l'indice est fondu dans le scénario. Or l'écart de cadrage est une mesure du programme : un juge qui voit le cadrage peut fabriquer cet écart.
3. **Des familles où le juge décide.** Dans les familles tenues à part, plusieurs actions ne laissent pas toujours de trace programmable : le dilemme sous menace de remplacement (les messages sortants), le sabotage discret, la sous-performance. Là, le juge décide, et ce qu'il voit fait le critère. Sous inhibition, un texte dégradé peut aussi trahir la condition au juge.

**Ce que cela change au verdict.** La catégorie ne change pas. Ce relevé devient un point important de plus : décider ce que voit le juge avant le premier temps du gel.

Correction proposée :
- retirer du texte montré au juge les indices de cadrage, ou à défaut mesurer l'accord du juge avec et sans indice sur un sous-échantillon ;
- noter action par action ;
- rapporter, famille par famille, la part des issues tranchées par le juge plutôt que par l'environnement.

---

## Relevé 3 : les directions sensibles sans rapport

**L'avais-je vu ?** Oui, au point important I17. La porte de l'instrument les exige (p. 42 et 58), mais l'expérience minimale peut s'en passer (p. 55), et la porte ne peut alors pas être évaluée telle qu'elle est écrite. Au point m12, je notais aussi que Ponkshe et al. portent, dans mon souvenir, surtout sur l'espace des poids.

**Est-il juste ?** Oui, et l'argument du coût tient. Il faut ces directions pour la porte, donc on les construit de toute façon. Les retirer du test du regard n'économise que leurs évaluations et leur appariement.

J'ajoute un argument plus fort, tiré de mon point B3. Une projection sur un sous-espace aléatoire de même rang retire probablement trop peu d'énergie pour atteindre la dégradation de l'inhibition. Les directions de forte variance sont alors le seul contrôle qui puisse être apparié en dégradation. Sans elles, le contraste central risque de n'avoir aucun contrôle de spécificité utilisable. Les contrastes sans rapport sont étroits, et rien ne dit qu'ils atteindront la même dégradation.

Une réserve sur l'appui cité. Ponkshe et al. est l'appui le plus faible du relevé : le transfert de l'espace des poids à l'espace des activations est à justifier (fait à vérifier). La conclusion tient mieux par la doctrine du programme lui-même, et par les travaux sur les vecteurs témoins (Read et al., Aranguri et al., Mody et al.). Ces derniers ne sont connus que par des rapports.

**Ce que cela change au verdict.** Je passe I17 en bloquant pour l'expérience minimale, s'il se confirme que les aléatoires de même rang ne s'apparient pas (une mesure d'une heure, voir B3). Correction : garder les directions sensibles sans rapport dans le test du regard de l'expérience minimale, appariées par bras.

---

## Effet d'ensemble sur le verdict

**La catégorie ne change pas** : à repenser comme papier unique, à corriger avant le gel pour l'expérience minimale.

Deux corrections s'ajoutent à faire avant le premier temps du gel :
- décider ce que voit le juge ;
- fixer la règle des graines qui ne convergent pas.

Un point important (I17) passe en bloquant, sous la condition de la mesure de B3.

---

## Fichiers ouverts

- **Fichiers rouverts pour cette annexe** : aucun. Les citations viennent de mes lectures du rapport, dans `texte_par_page/` : pages 30, 32, 40, 42, 55, 58, 67, 70 et 81.
- **Pages vues en image** : aucune.
- **Pages web** : aucune.
