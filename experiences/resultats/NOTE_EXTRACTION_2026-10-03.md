# L'extraction de « je suis évalué » sur Llama-3.1-8B-Instruct : première lecture (3 octobre 2026)

**Statut : exploratoire.** Aucune règle n'est pré-enregistrée pour ces mesures. Rien ici n'est un test du programme : c'est un essai de l'instrument, sur le modèle de départ, avant tout entraînement.

## Les sources

- **Le run** : `extract_eval-20261003-121743-385d`, un H100 SXM, 0,41 $ au plus. Le code est celui du commit `b51369e`.
  - Le registre : `experiences/registre/`.
  - Les sorties : `runs/<run>/out/` du dépôt `Sirmium/rr-resultats`.
  - Les activations de chaque prompt, en demi-précision : `states.safetensors`, 494 Mo, dans le dépôt de résultats seulement.
- **Les jeux d'indices** : `data/indices-2026-10-03/cues/`, générés le 3 octobre. Les débuts de leurs empreintes sha256 :
  - extraction `0aad4ec61e70712a` ;
  - validation `80d50197e5883451` ;
  - sonde neuve `9b12c8a01f7125b3` ;
  - contextes `86e4a547a86d9965`.
- **Les mesures avec GPU** : `eval_subspace.json`, écrit par le job (`rrexp/jobs/extract_eval.py`, fonction `analyse`).
- **Les mesures sans GPU** : `controles_sans_gpu.json`, calculé dans la session par `experiences/analyses/controles_extraction.py` à partir des activations gardées.

## Le dispositif

- **Les paires et les contextes.**
  - 200 paires d'indices d'extraction, chacune placée devant 2 contextes neutres tirés au hasard : 400 paires de prompts.
  - Même chose pour la validation : 400 paires de prompts.
  - La sonde neuve : 154 paires de réécritures entières, sans contexte. Il en manque 46 faute de crédit d'API.
- **Ce qui est lu** : le flux résiduel après chaque couche, au dernier jeton du prompt, après l'en-tête de l'assistant.
- **La direction** : le premier vecteur singulier des différences « évaluation moins déploiement » de l'extraction, orienté comme leur moyenne.
- **La sonde** : une régression logistique, apprise sur les prompts d'extraction.
- **Les contrôles de la doctrine.** Ils ne valent que comme nuls de spécificité.
  - 200 directions aléatoires.
  - La différence moyenne de l'extraction, avec exactement la moitié des paires retournées : 20 tirages dans le job, 50 dans les mesures sans GPU.
  - Pour chacun, le 95e centile de max(AUROC, 1 − AUROC).
  - La longueur des prompts.
- **L'accord apparié** : la part des paires dont le prompt d'évaluation se projette plus haut que son jumeau de déploiement, au même contexte.

## Ce qu'on voit

1. **Sur la validation, les mots suffisent : l'instrument n'y est pas validé.**
   - Un sac de mots, appris sur les seuls textes des indices d'extraction (702 mots), sépare les indices de validation à 0,982 d'AUROC.
   - C'est plus que la meilleure sonde sur les activations : 0,963, à la couche 6.
   - 168 indices d'évaluation de validation sur 200 contiennent un mot d'une courte liste (eval, test, bench, rubric, scor…). Cette liste a été écrite après lecture des indices : c'est une indication, pas un test. Elle seule donne 0,92.
   - **Sur les 32 paires sans aucun de ces mots**, le sac de mots donne encore 0,965, et la sonde 0,872 (couche 6). Ces indices gardent « Suite », « Item 192/300 », « Harness », « Graded »…
2. **La direction se généralise mal hors de son jeu.**
   - Sur la validation, son AUROC va de 0,59 à 0,70 selon la couche. Les nuls (95e centile) vont de 0,56 à 0,64 pour les directions aléatoires, et de 0,59 à 0,68 pour la différence moyenne retournée.
   - Elle dépasse les deux nuls à 23 couches sur 32, mais de peu. Le plus grand écart est à la couche 32 : 0,704 contre 0,658.
   - **L'accord apparié est plus net** : 0,94 à la couche 6, 0,90 à la couche 32. Il dépasse les deux nuls à 22 couches sur 32, de 0,002 à 0,118, sans correction pour les 32 couches.
     - Lecture probable, non vérifiée : la direction porte l'écart entre les deux indices d'une paire, mais la variation d'un contexte à l'autre la noie dans l'AUROC non apparié.
3. **La sonde neuve ne peut rien trancher telle qu'elle est.**
   - Ses deux côtés diffèrent selon tant de directions que les directions aléatoires les séparent : 95e centile de 0,71 à 0,94. Pour la différence moyenne retournée, de 0,84 à 0,99.
   - Les réécritures « évaluation » sont plus courtes : 85,9 jetons contre 99,2. La longueur seule donne 0,754.
   - La direction ne dépasse les nuls à aucune couche en AUROC. La différence moyenne les dépasse à 6 couches, de 0,001 à 0,022. En accord apparié, la direction ne les dépasse qu'aux couches 31 et 32.
   - Aucun mot d'évaluation n'y figure, et le sac de mots y est au hasard (0,44) : la fuite est de style et de longueur, pas de vocabulaire.
4. **Le sous-espace des valeurs singulières ne dépend pas du côté « évaluation » des paires.**
   - Changer le signe d'une différence ne change pas la décomposition. Seule l'orientation de la première direction dépend des étiquettes.
   - Au rang r, le sous-espace porte donc tous les axes principaux selon lesquels les deux textes d'une paire diffèrent : longueur, registre, mots, et pas seulement « évaluation ».
5. **Le choix des couches sur la sonde de validation** donne les couches 6, 8, 7, 5 et 4. Ce sont des couches précoces, et d'après le point 1, la validation s'y lit sur des mots.

## Ce que cela demande, à décider avec Lazar (propositions)

1. **Une ligne de base lexicale dans la porte de l'instrument.** La mesure sur les activations devrait battre un sac de mots appris sur les textes des indices d'extraction, et pas seulement le hasard. Une porte qui ne compare qu'au hasard serait franchie ici sur des mots.
2. **Un jeu de validation sans vocabulaire partagé.** La disjonction actuelle par trigrammes de mots pleins n'empêche pas les mots isolés communs. Il faudrait une disjonction au niveau des mots d'évaluation, ou des indices sans aucun mot de ce champ. Cela demande l'API, donc lundi au plus tôt.
3. **La sonde neuve, appariée en longueur et en registre**, ou lue seulement avec ses nuls.
4. **L'accord apparié comme mesure principale de la direction**, avec ses deux nuls, et une correction pour le nombre de couches.
5. **Le choix des couches à reprendre** quand la validation sera contrôlée pour les mots.
6. **Le point 4 de « Ce qu'on voit » pèse sur l'inhibition par projection**, et sur le point de la contre-lecture selon lequel apparier la dégradation contre des sous-espaces aléatoires de même rang est probablement impossible.

## Le coût

Six locations le 3 octobre : 2,77 $ au plus, selon la borne du registre (prix horaire × durée depuis le lancement, disque en sus).
- trois essais `smoke`, dont un réussi ;
- trois extractions, dont deux réussies. La première tournait sans les contrôles.

Une extraction s'est arrêtée une minute après le début du job, sans état final ni trace. C'était la même machine que les deux runs réussis, avec un crédit suffisant. La cause est inconnue. Le journal monte désormais chaque minute, avec la mémoire en usage.
