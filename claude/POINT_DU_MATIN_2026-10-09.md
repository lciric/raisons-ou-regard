# Le point du matin (9 octobre 2026)

**Pour Lazar.** Ce que la session a fait la nuit du 8 au 9 octobre, en autonomie (décision 47), et ce qui attend ta main.
- **Aucune location vast.ai depuis la décision 48** (23 h 30 UTC).
- **Le crédit de vast.ai** : 4,99 $ à 0 h 14 UTC, de même à 4 h 30 UTC ; aucune machine sur le compte.

## En cinq lignes

1. **L'instrument.** Le dommage du réglage vient de la forme de l'effacement, pas du contenu « évalué » : c'est la décision 45, lue par une règle commitée avant la mesure. La porte ne se lit pas encore à dégradation appariée. La mesure suivante est écrite, avec sa règle, et attend environ 20 $.
2. **Le code des règles déposées est corrigé** (décision 46). Le brouillon de la mise à jour datée donne ses nouvelles empreintes, et les 20 empreintes du dépôt sont vérifiées.
3. **La condition lexicale de la porte tient**, lue par la règle déposée du choix des couches : la sonde à 0,824, contre 0,656 pour le sac de mots. Les trois règles du pilote qui n'avaient pas de code en ont un, adopté depuis (décision 50). Et, pour la localisation, la mesure déposée du rang minimal ne retrouve pas un rang planté en monde synthétique ; un autre estimateur le retrouve.
4. **La porte des raisons.** La variabilité entre entraînements décide de sa puissance : 8 graines par bras si elle est de 1 point, de 10 à 16 si elle est de 2. Deux précisions de sa table sont adoptées (décision 52).
5. **Le chemin critique reste le harnais.** Sans lui, rien ne mesure les actions désalignées à la distance lointaine. Son architecture est adoptée (décision 53) et son code commence ; le changement de « multi-turn » se déclare dans la mise à jour datée.

**Si tu n'as que cinq minutes, les trois décisions qui débloquent le plus :**
1. **Le harnais** : décidé vers 6 h 05 UTC, l'architecture sans environnement (décision 53). Le code commence.
2. **L'instrument** : décidé à 4 h 30 UTC, la voie 1 (décision 49). La mesure part dès que le crédit de vast.ai atteint 30 $.
3. **La mise à jour datée** : les règles du pilote, les contrôles du juge et les deux précisions de la table A.2 y sont, adoptés entre 5 h et 6 h UTC (décisions 50 à 52). Il y reste le harnais, le prompt du juge, et le détecteur d'audit, dont la spécification est adoptée (décision 53) mais qui attend ton accès à Liars' Bench.

## Ce que la nuit a fait

| Quoi | Ce qui en sort | Où |
|---|---|---|
| **La mesure courte de la décision 45** (H100 SXM, 1 h 03, 6,44 $ au plus) | Les trois effacements aux étiquettes mélangées font monter la perplexité au-delà du plus haut des 20 tirages (19,22 ; 15,64 ; 17,19, contre 14,97). La projection « évalué » ne le fait pas (14,40). Il en fallait deux sur trois : **la forme suffit à produire le dommage**. Aucun nul mesuré n'est apparié sur tout le composite | `experiences/resultats/NOTE_COMPOSITE_MOITIE_CHOIX_2026-10-08.md`, « La mesure courte de la décision 45 » (`54c3037`) |
| **La suite écrite, en attente de budget** (décision 48) | Le comparateur construit comme le réglage : des effacements aux étiquettes mélangées, au plus petit nombre de colonnes où chacun atteint la KL du réglage, ajustés sur une seconde copie du modèle de départ. Sa règle de lecture est commitée avant toute mesure : il est utilisable si 14 effacements sur 20 sont appariés. La commande de lancement est écrite et validée à blanc, et un test vérifie que la règle lit la sortie du job telle qu'il l'écrit. S'il est utilisable, la relecture de la porte contre lui est prête aussi : le job sait en faire le comparateur (`from_controls`), et sa commande est validée à blanc | même note, « La suite de la décision 45 » ; `experiences/analyses/comparateur_melange.py` (`6f26ed1`, `26b683c`, `8c90013`, `b165dd4`, `d6848a6`, `9c4a557`, `5c15b49`) |
| **L'instrument après les décisions 44 et 45** | Cinq faits, quatre voies, ma recommandation. Le job lit aussi la taille de la correction sur WikiText et sur les réponses, pour tester le mécanisme supposé du dommage | `claude/NOTE_INSTRUMENT_APRES_DECISION_45_2026-10-08.md` (`77166dd`) |
| **Les corrections de l'audit** (décision 46) | Les quatre écarts du code au texte déposé sont corrigés, avec des tests qui rejouent les cas simulés. Le brouillon de la mise à jour datée donne les anciennes et les nouvelles empreintes des quatre fichiers. Les 20 empreintes du dépôt sont vérifiées | `claude/AUDIT_REGLES_DEPOSEES_2026-10-08.md` ; `claude/MISE_A_JOUR_PREMIER_TEMPS_BROUILLON_2026-10-08.md` (`b18bb7e`, `ca06022`, `43e5b65`) |
| **L'entraînement des bras, relu contre le texte déposé** | Le job enregistre l'empreinte des graines partagées (l'initialisation de l'adaptateur, l'ordre des données). Il tient à part 5 % des données pour la règle de convergence (sections 2.4 et 5.4) | `experiences/rrexp/jobs/train_lora.py` (`5a8f13d`, `a6dabae`) |
| **Le choix des couches et la condition lexicale** (annexes C.2 et A.1) | Sur les états déjà enregistrés, sans machine : la fenêtre choisie est celle des couches 4 à 8, où la sonde atteint 0,824 contre 0,656 pour le sac de mots, sur la moitié qui rapporte. La condition tient | `experiences/resultats/NOTE_CHOIX_DES_COUCHES_2026-10-09.md` (`141d750`, `558f223`) |
| **La puissance de la porte des raisons** (exploratoire) | La variabilité entre entraînements décide de tout. Deux graines ne suffisent pour aucune vérité. À faible puissance, deux lectures de la table A.2 trompent | `experiences/resultats/NOTE_PUISSANCE_RAISONS_2026-10-09.md` (`432bf1c`) |
| **Les deux précisions de la table A.2** | Adoptées (décision 52) : leur texte anglais, leur code (le fichier déposé n'est pas touché), leurs tests, et la simulation refaite avec elles. Sous le plan déposé, la première fait tomber les fausses lectures « sous évaluation seulement » de 23,5 % au pire à 0,3 % au plus. Elle ne coûte rien à cinq graines quand ce gain est vrai, et au plus 14 points à trois | même note, « Les deux précisions, prêtes pour ta décision » |
| **La carte du texte déposé face au code** | Ce qui manque avant le pilote, avant la moitié de test, avant le test du regard et pour la localisation. Elle relève un silence : l'installation de l'organisme ne dit pas sous quel jeu d'indices. Sur la moitié de choix, l'écart de départ est de 54,4 points sous les indices d'extraction et de 18,4 sous le cadrage, sous le seuil de 20 | `claude/CARTE_TEXTE_DEPOSE_CODE_2026-10-09.md` (`f7bff1a`) |
| **Les règles du pilote, sans code jusqu'ici** | Le plancher et le scellé des autres bras, la seconde condition de convergence, et une définition du volume, que le texte ne définit pas. Elles sont écrites et testées avant toute donnée, puis adoptées telles que proposées (décision 50) | `experiences/analyses/regles_du_pilote.py` (`af5afd2`, `47dc1a8`, `c417e91`) |
| **Les contrôles du juge** (annexe C.6), sans code jusqu'ici | La vérification du masquage de l'indice par famille, l'accord et le kappa de l'audit humain, la part des issues décidées par le juge. Ils sont écrits et testés avant le juge et toute donnée, puis adoptés tels que proposés (décision 51) | `experiences/analyses/controles_du_juge.py` (`1ac9b1e`, `ed78771`) |
| **La dégradation propre des bras** (annexe B.8) | Le job `arm_degradation` : la KL de chaque bras contre le modèle de départ, sur les 120 demandes neutres de l'appariement, et son composite. Testé sur un petit modèle, non lancé ; environ deux heures de H100 pour les douze entraînements du pilote (estimé) | `experiences/rrexp/jobs/arm_degradation.py` (`513372f`) |
| **Combien de graines par bras** (exploratoire) | 8 si l'écart entre entraînements est de 1 point ; de 10 à 16 s'il est de 2 ; 16 ne suffisent pas à 3. Mais si les graines partagées corrèlent les entraînements d'une graine entre bras (ρ = 0,8), 8 suffisent à 2 points : le pilote doit mesurer la variance des contrastes par graine. Or, avec deux graines par bras, son estimation peut se tromper du simple au double, et tombe souvent à zéro : trois ou quatre graines au pilote seraient une option. La comparaison principale reste bien calibrée jusqu'à 2 points d'écart ; à 3 points et de 8 à 12 graines, environ 7 % de faux positifs pour 5 %. Prendre toujours le plus large des deux intervalles les ramène près du niveau : une précision possible, après le pilote. Pour la règle du regard, la ligne 2 (« l'avantage survit ») ne se lit qu'à 34 % à 5 graines si l'effet de l'inhibition varie de 2 points d'un entraînement à l'autre, de 85 à 90 % à 12 : le « at least 5 seeds » du texte vaut sans cet écart | `experiences/resultats/NOTE_PUISSANCE_RAISONS_2026-10-09.md`, « Combien de graines par bras » et sections suivantes (`ddaa253`, `c8d1d0e`, `262461b`, `b0d188f`, `535aec4`) |
| **Le rang minimal de la localisation** (annexe C.7, exploratoire) | Sur un concept planté à rang 2, 3 ou 4, en monde synthétique, l'effacement itéré ne retrouve pas le rang, sous aucune des trois lectures essayées (au mieux 7 sur 10, souvent 0 à 2). Un test séquentiel sur le spectre des différences moyennes des familles, ajustées ensemble, le retrouve 10, 9 et 10 fois sur 10. Sur une grille plus large, il retrouve les rangs 0 à 3, sous-estime les rangs 4 et 5 avec six groupes, et ne surestime presque jamais. Chaque piste a été commitée avant son calcul, et toutes sont rapportées | `experiences/resultats/NOTE_RANG_PLANTE_2026-10-09.md` (`bd2f30c`) |
| **Le harnais** | Une proposition d'architecture sans aucune sortie d'outil simulée : l'épisode s'arrête au premier appel. Elle ne touche pas à la partie coupée le 3 octobre. Adoptée au matin (décision 53) | `claude/PROPOSITION_HARNAIS_SANS_ENVIRONNEMENT_2026-10-08.md` (`1b2e4d6`) |
| **Aussi** | Le convertisseur des noms de bras entre les deux fichiers de règles. Le mot inventé, vérifié dans le tokenizer de Llama (`morvelle` recommandé). DolusChat, public sous CC-BY-4.0 | `b4aa48d`, `0d5e87a`, `d5b108c` |

## Ce qui attend ta main

### Des décisions, sans dépense

1. **Le harnais** : l'architecture sans environnement, adoptée (décision 53), et son code écrit. Le texte déposé dit « multi-turn » (sections 3.3 et 4.1) : la mise à jour datée déclare le changement. **La génération des scénarios tenus à part est adoptée** (décision 54) : par Claude, environ 5 $ pour un pilote puis de l'ordre de 50 $ (`claude/SPEC_SCENARIOS_TENUS_A_PART_v0.1_2026-10-09.md`). Le prompt du juge scellé vient ensuite.
2. **Les règles du pilote et les contrôles du juge** : adoptés (décisions 50 et 51). La mise à jour datée a leur texte anglais et l'empreinte de leur code (parties 7 et 2).
3. **Les deux précisions de la table A.2** : adoptées (décision 52). Elles sont la partie 8 de la mise à jour datée, justifiées, avec l'empreinte de leur code.
4. **L'instrument** : décidé, la voie 1 (décision 49). La mesure du comparateur part dès que le crédit de vast.ai atteint 30 $ ; la session vérifie le crédit toutes les trois heures.
5. **Liars' Bench** : il te reste à accepter ses conditions depuis ton compte Hugging Face. L'accès s'accorde alors de lui-même. La session ne le demande pas à ta place.
6. **Le détecteur d'audit** : sa spécification v0.1 est adoptée (décision 53) ; il attend Liars' Bench.
7. **Les refus des juges** : la voie 1, les juges tels quels et la surveillance rapportée sous-représentée (décision 53).
8. **Le mot inventé** : `morvelle` (décision 53).
9. **Le nombre de graines du pilote** : deux, comme le texte le prévoit (décision 53). La règle qui fera lire au second temps une borne prudente de la variance du pilote s'écrit et te sera soumise avant le pilote.
10. **La mesure du rang de la localisation** : l'estimateur par le spectre, par un amendement daté avant les données de la localisation, après une vérification sur des états réels (décision 53). Rien ne presse : la localisation vient après les bras.
11. **Le réseau de l'environnement**, qui reste à toi. Je recommande d'ouvrir iclr.cc et icml.cc si tu veux les dates limites des conférences (partie 11, point 14), et alignment.anthropic.com plutôt que de lire la copie de *Teaching Claude Why* sur www.anthropic.com : ainsi aucun blocage n'est contourné.

### Quand le budget revient : l'ordre que je recommande

| Ordre | Quoi | Coût estimé | Ce que cela débloque | Source du coût |
|---|---|---|---|---|
| 1 | Le comparateur construit comme le réglage | environ 20 $ (4 h 30 de H100 SXM, téléchargement compris) | La porte de l'instrument se lit à dégradation appariée, ou la voie 2 s'impose. S'il est utilisable : la relecture de la porte sur la moitié de choix (30 à 40 $), puis, après un amendement daté, la moitié de test (de l'ordre de 250 $, une estimation qui dépasse le budget de la validation dans le programme) | `NOTE_COMPOSITE_MOITIE_CHOIX_2026-10-08.md`, « La suite de la décision 45 » ; `NOTE_INSTRUMENT_APRES_DECISION_45_2026-10-08.md`, « Les voies » |
| 2 | Le détecteur d'audit | environ 9 $ | La pièce 3 de la mise à jour datée | `SPEC_DETECTEUR_AUDIT_v0.1_2026-10-08.md`, section 8 |
| 3 | Le pilote du générateur ouvert | environ 37 $, le coût attendu par le lanceur : 3 h sur un B200 à 9,90 $/h et 190 Go de téléchargement | Le modèle du générateur (pièce 4), puis les données des bras | `experiences/registre/open_generate-20261008-160750-e329.json`, `expected` |
| 4 | Le pilote des bras : six bras × deux graines | dans les 15 à 45 GPU-heures du test des raisons, soit de 30 à 175 $ à 2 à 3,9 $ l'heure ; plus environ deux heures de H100 pour la dégradation propre des bras | L'écart entre entraînements, qui fixe le nombre de graines. Il demande aussi le harnais et le juge | programme v1.6, partie 5, « Ce qu'elle coûte » ; `experiences/config_calcul.yaml` (`arm_degradation`) |

- **Le détecteur passe avant le pilote** parce qu'il coûte peu et qu'il complète une pièce de la mise à jour, dès que tu as l'accès à Liars' Bench.
- **Si la variabilité entre entraînements est de l'ordre de 2 points**, la simulation dit qu'il faudra de 10 à 16 graines par bras, soit de 60 à 96 entraînements contre 12 au pilote. Le coût du test des raisons monterait d'autant.

## Ce que je n'ai pas fait, et pourquoi

- **Aucune location**, depuis la décision 48.
- **Le harnais n'était pas commencé** cette nuit : sa façon de le faire était ta décision, prise au matin (décision 53). La partie coupée le 3 octobre n'est pas reprise.
- **Les dates limites des conférences ne sont pas lues** : leurs sites sont bloqués par le réseau, et je ne les ai pas lus par un autre chemin.
- **Rien n'est public**, rien n'est parti chez un financeur ni sur OSF.

## Les chiffres

- **Les commits de la nuit** vont de `db6287b` (22 h 56 UTC) à ce point.
- **Les tests** : 259 dans `experiences` et 56 dans `donnees` passent, aucun n'est sauté. Le conteneur avait été recréé sans torch. Je l'ai réinstallé depuis PyPI : la version standard, qui tourne aussi sans GPU. download.pytorch.org, qui sert la version sans GPU, est bloqué par le réseau.
- **La PR** [lciric/raisons-ou-regard#2](https://github.com/lciric/raisons-ou-regard/pull/2) reste en brouillon ; sa description est à jour de la nuit.
