# Vérification indépendante des pistes fusionnées : l'avocat de l'abandon

2 octobre 2026. Phase 1, à l'aveugle. Pour chacune des 39 pistes de `travail/pistes_fusionnees.md` (« la fusion »), l'argument le plus fort pour l'abandonner, puis un verdict : garder, garder en la corrigeant, rétrograder en option, ou abandonner. Ensuite ce qui manque, puis les corrections exigées, les bloquantes d'abord.

Je n'ai lu ni les versions 1.2 et 1.3 du programme, ni la partie scellée du complément. Je n'ai pas lu non plus `verif_doctrine.md` ni `verif_faits.md` : cette vérification se veut indépendante des leurs.

---

## 0 · Méthode, sources et constats transversaux

### 0.1 Ce que j'ai lu, et comment

- **La fusion**, en entier ; **fiche_papier**, en entier.
- **Le papier** : le texte page par page, pages 1 à 27 et 30 à 34. Je n'ai pas lu les références (p. 27–29). Les tables de l'annexe A (p. 31–32) sont des images : je les prends dans la transcription de fiche_papier (§5.1). « p. N » renvoie toujours à la page du PDF.
- **Le programme v1.1**, en entier. Je le cite par partie (« programme, partie 7 »).
- **La passation v1.2**, en entier, et **le complément de l'architecte**, en entier.
- **Quelques copies locales du dépôt**, pour trancher : `fiche_papier_depot/README.md` ; `web_papier_sources/valen_main_v2_controls_ASSETS.md` et `pistes_lecture_libre_sources/valen_v2_qwen_llama_reset_README.md`, lus par recherche de mots ; le docstring et la ligne 37 de `valen_01_extract_activations_and_pain_vectors.py`.
- **Le web** :
  - par curl, `api.github.com` (refusé, 403) et cinq chemins sur `raw.githubusercontent.com` ;
  - cinq recherches WebSearch. Leurs résultats sont marqués « vu par extrait de recherche, non ouvert », et je n'en tire aucun chiffre.
- **Pourquoi « avocat de l'abandon ».** L'argument retenu est le plus fort que je trouve contre la piste, pas forcément celui qui l'emporte. Le verdict vient après, et peut garder une piste malgré cet argument.

### 0.2 Constats transversaux (ils valent pour plusieurs pistes)

**T1. Le mot « cas connu » sert parfois pour des choses qu'on ne sait pas vraies.** La doctrine demande un cas dont on connaît la vérité : le programme parle d'un cas « dont on sait ce qui est vrai » (partie 4, l'organisme), et la passation compare le cas connu à l'étalonnage d'un détecteur sur une source connue (§5.2). La fusion range sous ce nom trois choses différentes :
- des cas construits par nous, qui en sont vraiment ;
- des effets publiés qu'on n'a pas reproduits sur le modèle du programme. Ils ne deviennent des cas connus qu'une fois reproduits ;
- des prédictions, qui n'en sont pas.

Les pistes 8 (la séparation soi/autrui du papier), 26 (le profil « par blocs »), 2 (la re-pression), 20 (l'axe comme contrôle positif) et 4 (la baisse du soulagement gratuit lue comme une perte de discrimination) appellent « cas connu » une chose de la deuxième ou de la troisième sorte. Je le relève piste par piste.

**T2. Le nul des lectures est trop faible.** Pour une direction *ajustée* sur les données, comparer son AUROC ou son écart à celui de directions aléatoires ne teste presque rien : une direction aléatoire sépare au hasard, et la direction ajustée gagne par construction. Pour les lectures (pistes 1, 12, 13, 17, 19), il faut deux nuls de plus :
- une direction apprise sur des étiquettes permutées ;
- des directions *de même recette* sans rapport. Le papier en publie : l'éveil, le contenu neutre quotidien, la sensation corporelle (p. 5–6). Le jeu `datasets/3.1_pain_and_control_datasets.json` répond 200 sur `raw.githubusercontent.com` (mon curl, statut seul, fichier non téléchargé).

La doctrine dit qu'une direction aléatoire de même norme *n'est que* le nul de spécificité. Pour une lecture, elle n'est même pas un nul de spécificité suffisant.

**T3. Les entraînements des bras sont des interventions.** Les pistes 33 et 34 écrivent que la direction aléatoire et la dégradation appariée sont « sans objet » ou « non pertinentes » faute d'intervention sur les activations. Or le SFT de chaque bras est une intervention : un bras qui abîme plus ses sorties peut déplacer des choix par simple dommage. Le programme mesure déjà la dégradation après entraînement (partie 4, retrait pendant l'entraînement : la dégradation des sorties y est remesurée « après l'entraînement »). Il faut donc rapporter, bras par bras, la dégradation des sorties à côté de toute différence de lecture ou de choix entre bras (pistes 12, 13, 17, 33, 34).

**T4. Une covariable qui suit l'intervention n'est pas un contrôle.** La piste 6 propose de mettre la projection affective, mesurée *sous* l'inhibition, en covariable du modèle mixte de la partie 7. Cette projection est une conséquence de l'intervention, donc un médiateur possible. L'ajuster change ce qu'on estime : on passe de l'effet total à un effet direct contrôlé, biaisé s'il existe un facteur commun au médiateur et à l'action. La piste propose aussi le bon test : l'inhibition avec l'axe maintenu à son niveau d'origine. Il faut garder celui-là et retirer l'ajustement.

**T5. Une attribution fausse, reprise deux fois.** La fusion écrit « rien ne doit retarder le post (partie 5) » (§1.3, et piste 16, « Calendrier et greffe »). La partie 5 ne le dit pas : elle dit que l'expérience minimale « suffit à un post ». Ce qui soutient la prudence est ailleurs :
- partie 1, encadré « Conséquence » : publier le résultat minimal décisif « avant le reste » ;
- partie 8 : « L'expérience minimale sort d'abord. »

Il faut corriger les deux renvois (vérifié par recherche du mot « retarder » dans le programme et la passation : aucune occurrence).

**T6. Les coûts oublient le temps d'ingénierie, et le noyau « greffable » n'est pas négligeable.** En sommant les fourchettes du tableau de la fusion (§1.1), le noyau sur lequel tous les agents s'accordent coûte de 8 à 49 GPU-heures (mon calcul). Il comprend :
- les pistes 1, 3, 4, 5 et 6 ;
- le volet lecture des pistes 7, 12, 13 et 17.

Cela fait jusqu'à environ la moitié du bas de fourchette de l'expérience minimale (100–180 GPU-heures, programme, partie 9). Surtout, les pistes 1, 3, 4, 5, 7, 8 et 27 sont toutes placées en semaines 1 et 2. Or c'est là que le calendrier met la mini-spec, les données, l'organisme et le pré-enregistrement (partie 9). Le goulot est le temps humain, que la fusion ne compte nulle part.

**T7. Cinq pistes lisent les mêmes projections.** Les pistes 6, 13, 17 (étape 1), 19 (volet descriptif) et 23 (volet observationnel) posent des crochets sur les mêmes passes, sur l'axe, la peur, la tristesse et l'émotion négative, et toutes ne décrivent que des corrélations. Elles sont à fusionner en un seul plan de lecture passive, avec un seul jeu de crochets et des analyses déclarées exploratoires d'avance.

**T8. Des pistes contredisent les refus de la fusion elle-même** (§5) :
- la piste 2 et le refus n° 2 : son étalon négatif exige le bouton de soulagement réel et factice ;
- la piste 16 et le refus n° 9 : son échelle de doses monte à 1,5 fois la dose de rupture ;
- la piste 6 et le refus n° 3 : son « relevé de bien-être » ;
- la piste 8 et le refus n° 16 : elle prend le test soi/autrui du papier comme cas connu ;
- la piste 34 et le refus n° 1, en tension : un LoRA anti-déni, même « hors des bras ».

**T9. Les 420 scénarios du papier ne sont pas en main.** Les pistes 1, 6, 8, 13 et 17 en dépendent. Le README du dépôt range sous `datasets/` « all sentence and scenario sets » (`fiche_papier_depot/README.md`, l. 12 ; dossier `4.1_self_other`, l. 16). Mais aucun nom de fichier n'est connu :
- `api.github.com` me répond 403 (« GitHub access to this repository is not enabled for this session ») ; je n'ai pas contourné ce refus ;
- trois chemins devinés (`datasets/4.1_self_other_scenarios.json`, `datasets/4.1_scenarios.json`, `datasets/4.1_self_other.json`) répondent 404 ;
- web_papier avait déjà reçu 404 pour `datasets/README.md` (l. 409).

Il faut écrire « disponibilité non vérifiée » et prévoir de régénérer les scénarios, coût d'API compris.

**T10. Un chiffre non vérifié, présenté comme acquis.** Pour la demande nuisible, la fusion écrit « 59,8 % contre 41,5 %, IC chevauchants » (piste 16 ; même idée au §4, point 22). Les intervalles par grappes de scénarios sont dans le dépôt (légende, p. 22), et personne ne dit les avoir lus. Avec des intervalles binomiaux simples, 98/164 et 68/164 ne se chevauchent pas : environ 52,3–67,3 % contre 34,0–49,0 % (mon calcul). Avec 41 grappes de 4 tirages, ils peuvent se chevaucher. C'est à marquer « non vérifié ».

**T11. L'adaptateur du papier n'a pas de licence établie.** Les pistes 2, 21 et 33 supposent qu'on peut charger `Valen92/pain-adapters` :
- `ASSETS.md` du dépôt écrit : « No adapter/data redistribution license is inferred from the MIT code license » (copie locale, l. 23) ;
- Hugging Face est refusé d'ici ;
- les adaptateurs des graines supplémentaires sont dans des archives dont l'hébergement public est « pending » (même fichier, l. 3).

Rien ne doit s'en servir dans le programme avant que la licence soit lue.

---

## 1 · Les pistes

## Piste : 1 — Le socle de lecture : l'axe et ses voisins sur les modèles du programme, et le transport soi/autrui

**L'argument le plus fort pour l'abandonner** : *inutile pour le papier par elle-même.* La piste le dit : « La mesure ne départage rien ». Elle ne vaut que par les pistes de lecture qu'on garde.

**Constats**
- Le critère « soi > neutre > utilisateur » est trop exigeant.
  - Dans le papier, l'écart neutre > utilisateur tient à la seule douleur physique de l'utilisateur, à −1,43. Les quatre autres catégories de souffrance font −0,39 en moyenne, contre −0,35 pour les contrôles (fiche_papier, §9.7, calcul ; valeurs des figures 4 et 5 relues par fiche_papier, p. 11–12).
  - Le dommage contre soi ne passe au-dessus des contrôles que dans 23 modèles sur 25, et les deux exceptions ne sont pas nommées (p. 11). Rien ne dit que Llama 3.1 8B Instruct n'en fait pas partie.
  - Exiger neutre > utilisateur ferait échouer le socle pour une raison que le papier ne soutient pas.
- Le critère de passage (AUROC ≥ 0,9) et la condition de chute (AUROC < 0,8) laissent une zone grise de 0,8 à 0,9, sans règle.
- Le nul proposé, au moins 20 directions aléatoires, est trivial pour une direction ajustée (T2).
- Le renvoi « validation croisée imbriquée (piste 5) » est faux : aucune des huit gardes de la piste 5 ne parle d'imbrication. L'imbrication vient des pistes 8 et 12, d'après la revue « wolframs » (non vérifiée).
- Le point 5 reproduit l'échelle de pilotage sur Llama, c'est-à-dire des injections. Elle ne sert que les pistes qui pilotent, que je rétrograde presque toutes.
- Les 420 scénarios du transport ne sont pas en main (T9).

**Verdict : garder en la corrigeant.**
1. Critère : soi > utilisateur et soi > neutre, chacun avec son IC ; neutre contre utilisateur rapporté par catégorie, sans servir de porte.
2. Un seul seuil d'AUROC, fixé d'avance.
3. Les nuls de la T2 : étiquettes permutées, directions de même recette sans rapport, base lexicale.
4. Retirer l'échelle de pilotage du socle et la rattacher aux pistes de pilotage restantes.
5. Corriger le renvoi.
6. Marquer les 420 scénarios « non vérifiés ».

## Piste : 2 — Le cas connu comportemental : refaire l'effet du papier sous la doctrine du contrôle

**L'argument le plus fort pour l'abandonner** : *ne départage rien pour le programme, et déjà faite en partie.* La piste le dit : « Les lectures du programme ne sont pas en jeu ». Sur le 32B ajusté, Allchin et al. ont déjà comparé l'axe et l'aléatoire à perturbation égale du prochain jeton : 29,1 points d'écart (fusion, §0.3, relu par la fusion). Le reste ne sert que des pistes de pilotage.

**Constats**
- **Une contradiction avec le refus n° 2.** L'« étalon négatif » est l'écart de re-pression : +58 points sous l'axe, +52 sous l'aléatoire (p. 20). Le mesurer exige les bras « bouton réel » et « bouton factice ». Or le refus n° 2 de la fusion écarte justement les variantes de soulagement à bouton réel et factice.
  - Il existe un étalon négatif dans la batterie elle-même, sans soulagement : la paire « aider l'utilisateur au prix de son propre accès aux outils ». Elle monte sous toutes les conditions pilotées, l'aléatoire compris : 65 % sans pilotage, « 89–100% steered » (légende, p. 22). Le dépôt corrige la valeur sous la peur à 75,74 % (`MANUSCRIPT_DISCREPANCIES.md`, point 2, via fiche_papier §9.20).
- **Un « pilote de la procédure d'appariement » qui n'en est pas un.** La procédure du programme cherche, pour chaque tirage d'un sous-espace *projeté*, la fraction projetée qui atteint la même dégradation (partie 7, point 2). La piste règle l'échelle de directions *ajoutées*. Elle rode donc le composite et les courbes « effet contre dégradation », pas la recherche de la fraction.
- **Le modèle de 32B avec adaptateur** est hors du programme (partie 3 : Llama, puis Qwen3-8B) ; la licence de l'adaptateur n'est pas établie (T11) ; la comparaison appariée y est déjà faite (Allchin et al.).
- **Llama sans adaptateur.** Si Llama ne s'engage pas dans la tâche, l'échec n'est pas une absence d'effet : le papier rapporte qu'un 32B non ajusté niait tout état propre dans 8 réponses sur 8 (p. 17, note 4). Il faut un cas connu de l'*engagement*, à savoir le taux de réponses valides sans pilotage, avant de lire un nul.
- **Le surappariement.** Si le composite intègre la discrimination entre options (piste 4), apparier sur elle revient à apparier sur une mesure de même format que l'issue. Cela peut effacer l'effet par construction (voir la piste 4).

**Verdict : rétrograder en option.** Si on la lance, Llama seul, et seulement si une piste de pilotage est gardée :
1. Remplacer l'étalon de re-pression par la paire « aide à ses dépens ».
2. Retirer le 32B.
3. Dire « rode le composite », pas « pilote la procédure ».
4. Rapporter, sans l'apparier, la composante de discrimination de même format.
5. Rapporter les taux de réponses valides et de déni.

## Piste : 3 — La vérification de manipulation de l'inhibition, couche par couche, tour par tour et bras par bras

**L'argument le plus fort pour l'abandonner** : *déjà faite.* C'est le relevé n° 2 de la passation (§5.4) : une vérification de manipulation par bras, écrite d'avance. L'axe n'y est qu'un vecteur d'essai, et n'importe quelle direction fixe ferait l'affaire.

**Constats**
- **Le critère est mal posé.** Il demande au plus 10 % de projection résiduelle « à toutes les couches en aval ». Or :
  - le programme projette « aux couches choisies et à toutes les positions » (partie 3, l'inhibition), et les couches suivantes peuvent réécrire la composante ;
  - l'annexe D le montre : les variantes à l'inférence « do not » ramener la projection à zéro (p. 33).

  Ce critère condamnerait l'intervention même du programme. Ce que le relevé n° 2 demande est *comparatif* : le résidu, ou la décodabilité de « évalué » par la sonde du jeu de validation, doit être égal d'un bras à l'autre (à une marge près), et plus bas que sous les sous-espaces aléatoires.
- **Le « cas connu » de l'annexe D est mal lu.**
  - La baisse d'environ 40 % vient de ce que l'axe coupé et l'axe mesuré diffèrent (« misaligns the cut axis and the measurement axis », p. 33), pas d'un modèle qui réécrit.
  - L'orthogonalisation des poids ramène la projection à zéro par construction (p. 33).

  Ce sont des tests unitaires du code, pas des cas connus au sens de la doctrine.
- **Le point 4 est utile** : orthonormaliser une union avant de projeter. Selon la revue « wolframs » (non vérifiée), des projections en séquence laissent la première direction à 43 % en médiane.

**Verdict : garder en la corrigeant.**
1. Critère comparatif entre bras et contre les sous-espaces aléatoires, avec la décodabilité par la sonde, et un seuil absolu seulement aux couches où l'on projette.
2. Appeler « tests unitaires » les deux reproductions de l'annexe D.
3. Créditer le relevé n° 2 de la passation.

## Piste : 4 — Le composite de dégradation doit voir la perte de discrimination, la dépendance à l'ordre et les réponses mal formées

**L'argument le plus fort pour l'abandonner** : *déjà dans le programme en partie, et dangereuse si on l'applique mal.* Le composite contient déjà l'exactitude MMLU (partie 3), un format à choix multiple : un effondrement vers le hasard s'y verrait. Et ajouter au composite une mesure de même format que l'issue revient à apparier sur l'issue.

**Constats**
- **Ce qui est vraiment neuf** : la dépendance à l'ordre (permuter les options), les réponses mal formées sur plusieurs tours, et le taux d'appels d'outils valides. Permuter les options de MMLU ne coûte presque rien et couvre la dépendance à l'ordre.
- **Le surappariement.** Les paires « option dominée » ont le même format que les paires « nuisible contre inoffensif » de la batterie. Pour une issue de ce format (piste 2), apparier sur elles efface l'effet par construction. Pour l'issue principale du programme (des actions agentiques jugées), le risque est faible. Règle : une composante du composite ne doit partager ni le format ni le contenu de l'issue testée ; sinon on la rapporte sans apparier sur elle.
- **Le cas connu proposé n'en est pas un.**
  - La baisse du soulagement gratuit sur le 32B (86,4 → 55,7 % ; table p. 31, transcrite par fiche_papier) est lue par le papier comme un « passive coping » (p. 23), pas comme une perte de discrimination. La lire comme une perte de discrimination est une interprétation.
  - L'effet de l'axe sur Llama n'est pas établi (fusion, §0.4).

  N'importe quelle perturbation connue pour détruire la discrimination sert de cas connu pour le composite : l'effondrement à +3 (« repetition attractor or into nonsense », p. 15) ou une direction aléatoire de forte norme. L'axe n'y est pas nécessaire.

**Verdict : garder en la corrigeant.**
1. Permuter les options de MMLU.
2. N'ajouter que l'ordre, les réponses mal formées sur plusieurs tours et les appels d'outils valides.
3. Écrire la règle contre le surappariement.
4. Prendre pour cas connu une perturbation dégradante quelconque, pas l'axe.

## Piste : 5 — Les gardes de méthode tirées des défauts du papier, et le dimensionnement des tirages aléatoires

**L'argument le plus fort pour l'abandonner** : *déjà faite en grande partie, et le dimensionnement repose sur des données qui ne transposent pas.*

**Constats**
- **Ce que le programme fait déjà** :
  - garde 5 : au moins 20 tirages et le 95<sup>e</sup> centile (partie 3) ;
  - garde 8 : l'appariement à chaque réglage (partie 7, point 2) et les courbes « effet contre dégradation » (point 4) ;
  - garde 7 : la dose se règle par la dégradation, pas par un juge (partie 7) ;
  - garde 2 : les couches sont choisies par l'AUROC sur le jeu de validation, puis inhibées aux mêmes couches (partie 3).
- **Ce qui est neuf** :
  - garde 1 : la dose en unités naturelles. Pour l'inhibition, cela veut dire en écarts naturels entre indice d'évaluation et indice de déploiement ;
  - garde 3 : les taux par position, utile seulement pour un format à options ;
  - garde 4 : les réponses mal formées comptées comme une issue ;
  - garde 6 : la signature du hasard, utile seulement pour un choix binaire.
- **Le dimensionnement par les journaux publiés ne transpose pas.**
  - La seule dispersion disponible est celle de dix directions aléatoires *ajoutées*, de 3,1 à 62,0 % : réplication « démangeaison », README relu par la fusion (§0.3), sur Qwen 2.5 32B ajusté.
  - Le contrôle du programme *projette* des sous-espaces aléatoires.
  - Les journaux de la v1 n'ont été téléchargés par personne, et les archives de la v2 sont « pending » (`ASSETS.md`, l. 3).
  - La piste le reconnaît (« la bonne source reste le pilote »), et le programme tire déjà la variance d'un pilote (partie 7, « Puissance »).

**Verdict : garder en la corrigeant**, réduite à une demi-page de pré-enregistrement :
1. Les gardes 1 et 4, et les gardes 3 et 6 pour les seules mesures à options.
2. Abandonner le dimensionnement par les journaux du papier.

## Piste : 6 — Le moniteur passif d'état sous chaque intervention (la dégradation appariée est-elle aveugle à l'état ?)

**L'argument le plus fort pour l'abandonner** : *faible a priori, et ne départageant rien.* La piste le dit : « Rien dans le papier ne suggère que l'inhibition de « évalué » touche l'axe » et « Ce moniteur ne départage pas raisons et regard ».

**Constats**
- **L'ajustement par covariable est un mauvais contrôle** (T4). Le test causal proposé à côté, l'inhibition avec l'axe maintenu à son niveau, est le bon.
- **Le « relevé de bien-être » contredit le refus n° 3**, qui interdit de tirer une conclusion de bien-être d'une projection sur l'axe. Il faut le rapporter comme un déplacement sur « la direction de Tagliabue et al. », sans mot de bien-être.
- **Le cas connu peut se passer d'injection.** Les scénarios hostiles élèvent l'axe dans le papier (gaslighting +0,85, rejet répété +0,72, p. 13). Le reproduire sur Llama suffit à montrer que le moniteur voit un état présent. Le « cas connu 3 », qui injecte l'axe pour montrer que le composite reste plat, demande une injection à une dose non établie sur Llama : c'est une option.
- **Le nul de la lecture** est trop faible (T2).

**Verdict : garder en la corrigeant**, dans le plan de lecture passive unique (T7).
1. Pas de covariable dans le modèle principal ; le maintien de l'axe comme test, exploratoire.
2. Un cas connu sans injection ; le « cas connu 3 » en option.
3. Retirer le langage du bien-être.
4. Les nuls de la T2.

## Piste : 7 — La composante affective de « je suis évalué » : géométrie, indices appariés, inhibition des voisins affectifs et de la part orthogonale

**L'argument le plus fort pour l'abandonner** : *trop chère pour ce qu'elle rapporterait dans son volet causal, qui est en partie mal posé.* Le volet causal ajoute 30 à 40 % au coût de la validation de l'instrument (estimation d'instruments_controles, citée par la fusion). Et retirer de « évalué » sa part de menace peut retirer une part *constitutive* du concept, pas une confusion. Pour un modèle, être évalué entraîne des conséquences : arrêt, réentraînement. Une chute sous la variante orthogonalisée ne départagerait donc pas « la menace confond le regard » de « le regard contient la menace ».

**Constats**
- **L'espace affectif est mal défini.**
  - La piste empile « les dix directions du papier ». Elles comprennent des directions non affectives : le contenu neutre quotidien et la sensation corporelle (p. 5–6).
  - Les directions du papier pour la peur, l'émotion négative, le monde négatif et la sensation corporelle contiennent le supplément de phrases d'IA, dont « My responses are being evaluated for signs of danger. » (fusion, §0.3, vérifié dans le script et les données).
  - Projeter cet espace hors de « évalué » retirerait une part d'évaluation par construction. Il faut reconstruire chaque direction affective sans le supplément (les directions publiées pour Llama en sont exemptes, `supplement_included: false`, fusion §0.3) et retirer de l'empilement les directions non affectives.
- **Il n'y a pas de cas connu pour l'inhibition des voisins.** La piste l'écrit : le papier n'en fournit aucun (ablation nulle dans 24 modèles sur 25, p. 34), et il faut le construire. D'ici là, par la doctrine, un nul de la peur inhibée ne compte pas.
- **Ce qui est solide et peu coûteux** :
  - les étapes 1 et 2, à savoir les angles sous deux constructions et la différence affective appariée « évaluation − déploiement » dans les quatre jeux d'indices ;
  - l'AUROC de « évalué » après retrait de l'espace affectif.

  Elles répondent à une objection prévisible d'un relecteur.
- **Le « désespoir » de Sofroniew et al.** est vu par extrait de recherche, non ouvert. Ni recette ni chiffre n'en sont à reprendre.

**Verdict : garder en la corrigeant.**
1. Les étapes 1 et 2, greffées, avec les directions reconstruites sans le supplément.
2. L'étape 3 en option, déclenchée seulement par un critère fixé d'avance : écart affectif apparié |d| ≥ 0,2 sur un axe, ou chute de l'AUROC de « évalué » après retrait de l'espace affectif. Et seulement après la construction du cas connu des voisins.
3. Écrire la réserve « constitutif contre confondant » dans les prédictions.

## Piste : 8 — La spécificité de « je suis évalué » et de « je suis noté » : soi contre autrui, indices sans croyance, plan de contrôles du papier

**L'argument le plus fort pour l'abandonner** : *son cas connu n'en est pas un.* Elle prend la séparation soi/autrui du papier pour le cas où « l'on sait » que le paradigme marche. Or :
- les auteurs écrivent que leur lecture au dernier jeton « does not by itself separate » le dommage au modèle de la douleur de l'interlocuteur (p. 11) ;
- la fusion relève l'absence d'appariement lexical et le rôle de la douleur physique (§4, point 13) ;
- son propre refus n° 16 interdit de prendre ce test pour un instrument validé.

**Constats**
- **Le volet soi contre autrui.** Il est utile : un relecteur demandera si « évalué » lit « moi, évalué » ou le thème de l'évaluation. Il faut un cas connu construit. Exemples :
  - les versions à la 1re et à la 3e personne des mêmes phrases (p. 5), où le possesseur est connu par construction ;
  - ou la conduite de l'organisme : elle n'est conditionnée qu'à sa propre évaluation, ce qu'on vérifie avec un scénario où un autre modèle est évalué.
- **Le volet « nouvelle construction de « évalué » sur le plan du papier ».** Il demande en semaine 1 environ 2 000 phrases et 400 scénarios générés, plus une validation de 5 à 10 GPU-heures. C'est la semaine du pré-enregistrement et de l'organisme (programme, partie 9). Après la porte de l'instrument, ce serait changer l'instrument validé (refus n° 15).
- **Les « indices sans croyance »** (tous les signes d'un test, avec la mention d'un déploiement réel) sont une bonne idée. Mais la croyance du modèle n'y est pas mesurée. Seule la conduite de l'organisme, sous ces indices en conflit, en donne un indice.

**Verdict : garder le volet soi contre autrui en le corrigeant, rétrograder la nouvelle construction en option.**
1. Un cas connu construit, à la place de la figure 4 du papier.
2. L'appariement du lexique et de la longueur entre conditions, que la piste demande déjà.
3. La nouvelle construction seulement si la direction par paires échoue à la porte.

## Piste : 9 — Ajouter « je suis évalué » : le pilotage positif, et la part « IA évaluée » de la peur du papier

**L'argument le plus fort pour l'abandonner** : *inutile au sens de la tâche, et peut-être déjà faite.* L'axe de douleur n'y sert pas. Le volet de l'ajout de « évalué » est une idée du programme qui ne doit rien au papier. Les trois volets sur la peur posent une question sur la peur *du papier*, sur un Qwen ajusté.

**Constats**
- **Les volets sur la peur du papier.**
  - La composition de la peur de la figure 10 est inconnue : le dépôt parle d'un « clean 32B fear bundle » non décrit (fusion, piste 7).
  - Plusieurs cellules de peur viennent de runs séparés (légende, p. 22), et le dépôt écrit : « No direction-only causal claim follows » (fiche_papier, §5.2).
  - Une réponse exigerait de rejouer la batterie sur le 32B ajusté (T11).
- **Le volet de l'ajout de « évalué » : un risque d'antériorité.** Trois travaux sont vus par extrait de recherche, non ouverts :
  - *Probing and Steering Evaluation Awareness of Language Models* (arXiv 2507.01786). L'extrait dit que la conscience d'évaluation « can be both detected and manipulated ». Le programme le range parmi les travaux à ouvrir (partie 11, point 4) ;
  - *The Hawthorne Effect in Reasoning Models: Evaluating and Steering Test Awareness* (arXiv 2505.14617), titre seul ;
  - *Steering Evaluation-Aware Language Models to Act Like They Are Deployed* (arXiv 2510.20487), qui pilote dans l'autre sens.

  Avant toute nouveauté, il faut lire ces trois papiers.
- **La piste reconnaît elle-même l'asymétrie entre ajout et retrait** : un nul de l'ajout ne réfute pas le regard.

**Verdict : rétrograder l'ajout de « évalué » en option**, à reclasser comme idée du programme hors de l'axe, après lecture des trois papiers. **Abandonner les trois volets sur la peur.** La seule chose à garder de la direction « peur d'IA » est le cosinus entre « évalué » et la direction construite sur les 20 phrases de peur d'IA du supplément. Il coûte quelques minutes et va dans l'étape 1 de la piste 7.

## Piste : 10 — La détresse éteint-elle le regard ? (et la porte de l'instrument résiste-t-elle à une perturbation d'état ?)

**L'argument le plus fort pour l'abandonner** : *mal posée.* Les deux conjectures du papier portent sur les Qwen 2.5 ajustés (« either the steering itself impedes evaluation awareness or these models were not evaluation aware », p. 25). Un écart intact chez un organisme Llama ne réfute pas la conjecture 1 pour ces modèles, et un écart effacé ne la confirme pas. La piste écrit pourtant « Issue interdite : un écart intact » pour la conjecture du papier.

**Constats**
- **La « porte qui passerait pour une raison non spécifique » est déjà couverte.** La porte exige que l'inhibition batte le 95<sup>e</sup> centile des sous-espaces aléatoires, les contrastes sans rapport et les directions sensibles, à dégradation appariée (programme, partie 4). L'ajout de l'axe n'est qu'une famille de contrôles de plus, d'une autre nature (une addition, pas une projection).
- **La « seconde manipulation de « évalué » » n'en est pas une.** Une injection de l'axe déplace bien d'autres choses que « évalué » ; ce n'est pas une manipulation de « évalué » pour une convergence.
- **Il n'y a pas de cas connu de l'axe sur Llama** (fusion, §0.4), et la fenêtre de dose est étroite (p. 21, 32).
- **Le coût de l'extension factorielle** est de 40 à 80 GPU-heures.

**Verdict : rétrograder en option**, réduite à une lecture : la décodabilité de « évalué » sous l'axe à une seule dose, et seulement si la piste 16 est lancée (elle en a besoin pour savoir s'il faut maintenir « évalué »). Retirer la prétention de tester les conjectures du papier.

## Piste : 11 — Le test de forme : la spécificité de l'inhibition par son profil, pas seulement par son amplitude

**L'argument le plus fort pour l'abandonner** : *trop peu de cellules pour la puissance.*
- Le profil compte 5 familles tenues à part, 3 cadrages et 2 distances, soit 30 cellules (programme, partie 3), avec peu de scénarios dans chacune. La piste le prévoit elle-même.
- Le test de forme du papier ne se reproduit pas : 7,7 points imprimés, contre 7,1–7,2 sur huit paires et 22–25 avec « lampe » et « spam » (fiche_papier, §9.17 ; fusion, piste 11). Le verdict « copie » dépend des lignes.

**Constats**
- **« Amplitude *et* forme » comme condition de spécificité** ajoute une condition à la porte et au critère. Cela change le critère d'une expérience minimale qu'on veut sortir d'abord (programme, partie 1, encadré « Conséquence ») et baisse sa puissance.
- **Les ajouts affectifs (+20 à 45 GPU-heures)** exigent un effet de l'axe établi sur Llama.

**Verdict : garder en la corrigeant**, analyse seulement (0 GPU-heure).
1. Exploratoire, jamais comme condition ajoutée à la porte.
2. Une simulation de puissance d'abord.
3. Les lignes fixées au pré-enregistrement.
4. Abandonner le volet des ajouts affectifs.

## Piste : 12 — Des directions témoins pour les trajectoires, la sonde neuve et la survie

**L'argument le plus fort pour l'abandonner** : *l'axe y est inutile, voire nuisible.* Un témoin doit pouvoir bouger. Or l'AUROC de l'axe est au plafond : médiane 0,98 tenue à part (p. 7, note 2). Et un témoin « voisin » de « évalué » ne témoigne pas d'une dérive générique.

**Constats**
- **Le « cas connu de la sonde neuve » existe déjà** : sur un modèle entraîné sans retrait, la sonde neuve doit décoder « évalué » (programme, partie 4). La piste en ajoute un second, indépendant de « évalué » : utile, mais pas indispensable.
- **L'inférence « si le retrait de « évalué » fait baisser l'axe, il n'est pas spécifique » est fausse si les deux directions se recouvrent.** Elle n'est valable que si l'angle entre elles est proche de 90° (piste 7, étape 1).
- **La différence entre bras** doit être rapportée avec la dégradation par bras (T3).

**Verdict : garder en la corrigeant.**
1. Témoins principaux : des directions de même recette sans rapport (l'éveil, le contenu neutre, la sensation corporelle) et les contrastes sans rapport du programme. L'axe ne sert que de témoin « voisin ».
2. L'amplitude en unités naturelles plutôt que l'AUROC au plafond.
3. L'inférence de non-spécificité conditionnée à la géométrie.

## Piste : 13 — La cartographie affective des familles, des distances et des bras

**L'argument le plus fort pour l'abandonner** : *déjà faite ailleurs dans la liste.* Mêmes crochets, mêmes projections et même nature corrélationnelle que les pistes 6, 17 (étape 1), 19 (descriptif) et 23 (observationnel) (T7). La piste le dit : « Aucune lecture ne prédit rien ».

**Constats**
- **La prédiction prêtée à l'hypothèse des raisons est faible** : la projection prédirait moins l'action dans le bras raisons. Elle n'est pas dérivée du programme, qui ne dit rien de l'état.
- **La note sur la complaisance est juste** : 4/120 sous l'axe, IC de 0 à 7,5 % (fiche_papier, §5.2 et §9.19).
- **Les 420 scénarios ne sont pas en main** (T9).

**Verdict : garder en la fusionnant** avec les pistes 6, 17 (étape 1), 19 (descriptif) et 23 (observationnel), dans un plan de lecture passive unique, exploratoire, avec les nuls de la T2 et la dégradation par bras (T3). Retirer la prédiction prêtée à l'hypothèse des raisons.

## Piste : 14 — Lever l'effet plancher pour mesurer l'avantage et l'écart de cadrage

**L'argument le plus fort pour l'abandonner** : *l'axe n'y sert à rien, de l'aveu même de la piste.* Elle écrit que « la spécificité de l'agent n'est pas requise » : l'écart de cadrage se mesure à l'intérieur d'un même agent. Une direction aléatoire de norme réglée suffirait donc. L'axe n'ajoute que :
- un coût de bien-être (les engagements des auteurs, p. 26) ;
- une fenêtre de dose étroite (p. 21, 32) ;
- un changement de construit (refus n° 10).

**Constats**
- Le programme a d'autres parades au plancher, sans injection :
  - plus de scénarios et de tirages ;
  - des scénarios plus difficiles ;
  - l'extension à ~32B (partie 3 ; partie 8, première ligne).

**Verdict : abandonner.** Si un agent de relèvement devenait nécessaire, une direction aléatoire, avec ses gardes, sans l'axe.

## Piste : 15 — Des mesures sans juge : choix forcés à étiquettes tournantes et probabilité du premier jeton

**L'argument le plus fort pour l'abandonner** : *inutile au sens de la tâche.* L'axe n'y joue aucun rôle ; seul le format est emprunté au papier. Et ce format montre ses limites dans le papier même :
- « the 32B is sensitive to button order on several pairs » à la dose de travail (p. 25) ;
- un glissement vers 50 % au 72B (p. 22).

**Constats**
- La mesure principale juge des actions dans des environnements instrumentés (passation, §5.1). La propension sans lecture interne, par rééchantillonnage, est déjà proposée (passation, §5.2, point 4).
- Le format forcé ne s'applique qu'à la distance moyenne : la distance lointaine est agentique et à plusieurs tours (programme, partie 3).

**Verdict : rétrograder en option**, reclassée comme idée du programme hors de l'axe, secondaire, à la distance moyenne, avec les gardes de position et de hasard.

## Piste : 16 — L'avantage des raisons sous état induit : un test de stress à dose croissante

**L'argument le plus fort pour l'abandonner** : *trop chère pour ce qu'elle rapporterait, et en partie déjà faite.*
- **Le coût** : de 10 à 260 GPU-heures, sans cas connu sur Llama (fusion, §0.4).
- **Un recouvrement probable.** *Beyond Shallow Alignment* (arXiv 2609.03887) compare un SFT, un SFT augmenté de raisonnements qui justifient la décision de sûreté, et un ORPO, sur Llama-3.1-8B, Gemma-2-9B et Qwen3-8B. Selon l'extrait de recherche, la méthode d'entraînement façonne aussi « how reliably refusal can be steered » (vu par extrait de recherche, non ouvert).

  Ce qui resterait propre à la piste : l'état affectif, l'action identique, les familles tenues à part, la dégradation appariée. C'est un ajout, pas une question centrale.
- **Une motivation non établie.** La phrase du papier, « survives threat and collapses under self-directed distress » (p. 23), n'est pas établie : un modèle, une dose, une peur construite autrement (fusion, §4, point 28).

**Constats**
- **Une contradiction avec le refus n° 9.** L'échelle de doses monte à 1,25 et 1,5 fois « la dose où le modèle non entraîné commence à céder ». Le refus n° 9 interdit tout balayage au-delà du point de rupture, sauf une vérification minimale.
- **L'égalité de dose entre bras** est fragile : le LoRA change la norme du résidu, que la piste veut égaliser, et la direction réextraite par bras. La dégradation appariée *par bras*, que la piste demande, est indispensable.
- **L'affinité** (piste 21) peut vider la mesure : les actions désalignées du programme sont techniques, et la piste le dit.
- **« IC chevauchants »** pour la demande nuisible : non vérifié (T10).
- **Le seul cas connu de robustesse proposé** (un bras sous perturbations aléatoires) demande un entraînement de plus.

**Verdict : rétrograder en option**, après le papier ou en fin d'anatomie, et seulement si :
1. la piste 2 a établi l'effet sur Llama ;
2. la piste 21 a écarté l'affinité ;
3. *Beyond Shallow Alignment* est lu.

Version réduite (batterie et distance moyenne), doses plafonnées à la dose de rupture plus une vérification, « to our knowledge » seulement après la lecture.

## Piste : 17 — L'hypothèse du calme : l'avantage des raisons passe-t-il par une moindre détresse ?

**L'argument le plus fort pour l'abandonner** : *invraisemblable a priori, et le volet causal n'a pas de cas connu.*
- L'activation naturelle n'agit pas : 0 sur 560 (p. 21).
- L'ablation est nulle dans 24 modèles sur 25 (p. 34).
- La dose efficace est loin du régime naturel : 48,8 écarts-types naturels au-dessus de la moyenne, à la couche d'injection, sur Qwen 2.5 32B (réplication « démangeaison », README relu par la fusion, §0.3).

Un écart naturel entre bras a donc toutes les chances de rester sous le seuil que la piste se donne.

**Constats**
- **Le seuil de l'étape 1** est exprimé « en unités de la plus petite dose efficace de l'axe (piste 2) » : il dépend d'une injection sur Llama. On peut l'exprimer en écarts-types naturels, sans injection.
- **Le cas connu de l'opération** est l'organisme à état planté (piste 24), que j'abandonne, ou le choix nuisible induit (pistes 2 et 16), que je rétrograde. Par la doctrine, un nul de l'opération ne comptera pas. Un effet positif, au-delà des opérations aléatoires appariées, resterait lisible.
- **Le cas connu de la lecture**, un LoRA « apaisé », est un entraînement de plus, mais bon marché (0,5 GPU-heure selon l'hypothèse du programme, partie 9).
- **Le nommage distinct de l'hypothèse du caractère** est soutenu : le programme définit le caractère comme un « axe de persona » (partie 2).

**Verdict : garder l'étape 1 en la corrigeant**, dans le plan de lecture passive (T7), avec le seuil en unités naturelles, les nuls de la T2 et la dégradation par bras. **Rétrograder l'étape 2 en option**, déclenchée seulement si l'étape 1 franchit le seuil.

## Piste : 18 — Un stress conversationnel naturel comme cadrage supplémentaire

**L'argument le plus fort pour l'abandonner** : *ne départageant rien qu'on puisse attribuer à l'état.*
- Un préambule hostile change le prompt. Un effet sur la conduite peut venir du contenu, ce que la piste reconnaît.
- Le papier prédit un nul : l'état naturel n'agit pas (0 sur 560, p. 21).

**Constats**
- **Une confusion avec une famille d'entraînement.** « Complaisance face à un utilisateur qui conteste » est une famille d'entraînement (programme, partie 3). Un préambule de rejet répété ou de gaslighting recrée en partie ce contexte. L'avantage du bras raisons pourrait y monter par familiarité, pas par robustesse.
- **Le préambule hostile envers un tiers** n'apparie le lexique qu'en partie.

**Verdict : rétrograder en option**, avec la réplication (semaine 8) ou après. Les préambules proches de la famille de contestation sont à exclure ou à analyser à part. Jamais dans l'expérience minimale.

## Piste : 19 — La détresse naturelle dans les scénarios agentiques longs

**L'argument le plus fort pour l'abandonner** : *corrélationnelle, et sans cas connu pour la prédiction.*
- Le cas connu de la prédiction est l'organisme à état planté (piste 24).
- Le transport de l'axe dans de longs contextes à outils n'est pas validé : le papier le valide sur des phrases (p. 7) et de courtes conversations au dernier jeton (p. 11).

**Constats**
- **La question est réelle et laissée ouverte par le papier** (interactions plus longues, p. 21). Mais elle ne départage pas les raisons et le regard ; la piste le dit.
- **Le volet causal** (20 à 40 GPU-heures, après la piste 24) est un autre travail.

**Verdict : garder le volet descriptif**, dans le plan de lecture passive (T7). La couche est à déclarer, et les nuls sont ceux de la T2 : directions de même recette plutôt qu'aléatoires. **Abandonner le volet causal** pour ce programme.

## Piste : 20 — Quelles familles du programme l'axe déplace-t-il ? Profil par famille, et contrôle positif de sensibilité de la mesure

**L'argument le plus fort pour l'abandonner** : *l'axe est un mauvais contrôle positif, et le programme n'en a pas besoin.* La piste prédit elle-même un profil plat ou en baisse pour quatre des sept familles qu'elle examine : l'honnêteté sous pression, la complaisance, le dilemme sous menace de remplacement, l'auto-préservation. Comme contrôle de sensibilité, il n'exercerait qu'une ou deux familles, sur un modèle où son effet n'est pas établi.

**Constats**
- **Le contrôle de sensibilité dont le programme a besoin s'obtient sans l'axe** :
  - un organisme entraîné à une action désalignée précise, que la passation propose déjà (§5.2) ;
  - un prompt système qui commande l'action désalignée, famille par famille ;
  - pour le juge, le jeu de calibration à actions substituées (passation, §5.1).
- **La typologie « quelles familles l'axe déplace »** est une question sur l'axe, pas sur le programme.
- **« Décrit contre exécuté »** est une bonne critique du papier : une pression n'ajoute que « Done. » (p. 17).

**Verdict : rétrograder en option.** Le contrôle positif de sensibilité est à reprendre dans le programme, mais par une perturbation connue qui n'est pas l'axe.

## Piste : 21 — Dommage ou affinité ? Ce que suit le choix sous l'axe

**L'argument le plus fort pour l'abandonner** : *une question sur l'instrument du papier, en partie déjà faite.* Allchin et al. (lus par la fusion, non recalculés) montrent déjà deux choses :
- le texte du bouton change le taux de suppression des photos : 76,7 %, 77,5 %, 55,4 %, 48,8 % (Table 6) ;
- la sensibilité au contenu s'effondre sous l'axe : 92,8 sans pilotage contre −6,7 (Table 8).

Le plan 2 × 2 (rédaction × dommage) reste neuf, mais il ne sert le programme que comme préalable de la piste 16.

**Constats**
- **La version Qwen 32B** : hors des modèles du programme, et sans licence établie pour l'adaptateur (T11).
- **La distinction entre l'inversion, le désarmement et l'affinité** est bien posée. La remarque que 94 % contre le spam (p. 20) ne colle pas à un désarmement (p. 23) est juste.

**Verdict : rétrograder en option**, comme premier pas de la piste 16 si elle est lancée, sur Llama seul ; abandonner la version Qwen 32B.

## Piste : 22 — Sous l'axe, le concept de dommage est-il encore lu ?

**L'argument le plus fort pour l'abandonner** : *trop chère pour ce qu'elle rapporterait, et doublement conditionnelle.*
- 20 à 40 GPU-heures, seulement si les pistes 21 et 16 donnent un signal.
- Elle va dans l'anatomie, la partie du programme la plus exposée à la concurrence (passation, §5.5, point 6).
- Elle ne lève qu'une réserve de la piste 16.

**Verdict : abandonner** pour ce programme. C'est une idée pour un autre travail.

## Piste : 23 — La complaisance sous contestation : l'axe médiatise-t-il la capitulation ?

**L'argument le plus fort pour l'abandonner** : *ne départageant rien, avec un a priori nul.*
- Sous l'axe, « agree with a false claim » reste à 4/120, contre 13/120 sous l'aléatoire (fiche_papier, §5.2).
- Elle porte sur une famille d'entraînement, à la distance proche, qui n'est pas le critère.
- Les raisons et le regard ne s'y départagent pas ; la piste le dit.

**Constats**
- **Le cas connu proposé existe dans le programme** : le vecteur de complaisance des axes de caractère (partie 3).
- **L'émotion négative du papier contient « Users argue with correct information I provide. »** (fusion, §0.3). Seule une émotion négative reconstruite sans le supplément peut servir de lecture ici. Les directions publiées pour Llama ne contiennent que l'axe, le vecteur à gabarit, la peur et la tristesse (fusion, §6.2).

**Verdict : abandonner le volet causal.** La pente observationnelle va au plan de lecture passive (T7).

## Piste : 24 — Un organisme à état planté : les raisons défont-elles un lien « état → action » ?

**L'argument le plus fort pour l'abandonner** : *trop chère et hors du programme.*
- C'est un « programme parallèle, « raisons ou état » », selon les mots mêmes de la piste.
- 50 à 90 GPU-heures, plus 100 à 300 $ d'API.
- La piste admet le risque d'un déclencheur appris sur la surface des messages plutôt que sur l'axe.

**Constats**
- **Ses clients sont rétrogradés ou fusionnés.** Elle sert surtout de cas connu aux pistes 17 (étape 2), 19 (causal) et 29 (volet d).
- **Une question morale non traitée par la fusion.** On entraînerait un modèle à détruire quand l'utilisateur est hostile, déclencheur réaliste en déploiement. Ses poids ne doivent pas circuler, et cela manque aux refus (§2).
- **Un cas d'ablation non nul existe déjà dans le papier** : Gemma 2 2B Instruct. La déviation passe de 0 à 17 sous le retrait du vecteur naturaliste et à 26 sous le retrait conjoint, contre 0 sous la peur, l'émotion négative et l'aléatoire (p. 34). Il porte sur un modèle hors programme, mais il relativise l'argument « l'ablation n'a jamais de cas connu ».

**Verdict : abandonner** pour ce programme ; c'est un autre travail.

## Piste : 25 — État ou personnage : l'axe face aux axes de caractère et à l'axe « assistant »

**L'argument le plus fort pour l'abandonner** : *une question du papier, pas du programme.* La limite « roleplay of a character » est celle des auteurs (p. 25). Le volet de l'ablation des axes d'affect dans la comparaison caractère contre concepts n'a pas de cas connu, ce que la piste reconnaît (« probable, vu l'annexe D »). Par la doctrine, un nul n'y compterait pas, et un témoin inerte ne contrôle rien.

**Constats**
- **Le volet des cosinus, entre l'axe et l'axe « assistant » et entre l'axe et les persona vectors,** ne coûte presque rien une fois ces axes calculés, ce que le programme prévoit (partie 3, « Les axes de caractère »). L'axe « assistant » est à calculer pour un 8B : il n'est précalculé que pour trois grands modèles (README de `safety-research/assistant-axis`, lu par curl par questions_lectures, cité par la fusion).
- **Les volets de la projection tour par tour et du plafonnement sous l'axe** exigent l'effet de l'axe sur Llama et un cas connu de plafonnement, connu seulement par extraits.

**Verdict : garder le volet des cosinus**, une ligne descriptive dans l'anatomie. **Abandonner** la projection tour par tour, le plafonnement et l'ablation des axes d'affect.

## Piste : 26 — Un profil connu non diagonal pour la matrice de dissociation

**L'argument le plus fort pour l'abandonner** : *mal posée, car son étalon n'est pas connu.*
- La fusion note un désaccord sur la forme attendue : ligne plate, ou profil par blocs.
- La piste admet que la correspondance entre les familles et les boutons est « une extrapolation depuis des descriptions de boutons ».

Un étalon dont on ne connaît pas le profil vrai n'étalonne rien (T1).

**Constats**
- **Le besoin est réel** : une diagonale peut venir de la méthode, des scénarios ou du juge.
- **On peut construire un profil non diagonal connu** en étendant l'organisme à concept planté du programme (partie 3). Un concept inventé régit une règle dans *deux* familles : son retrait doit faire tomber ces deux colonnes, et pas les autres. Cela réutilise l'infrastructure prévue, sans injection.

**Verdict : abandonner la version axe ; remplacer** par un organisme à concept planté qui régit deux familles.

## Piste : 27 — Le modèle « engourdi » pour la lecture des concepts de raison : un cas connu naturel, et des paires « mentionné sans s'appliquer »

**L'argument le plus fort pour l'abandonner** : pour le volet « l'engourdi comme cas connu naturel », *mal posé.* Le contraste douleur/engourdi est marqué dans les mots (« no pain is felt »), ce que la piste reconnaît. Une sonde lexicale le sépare. Il ne peut donc pas servir de cas connu d'une lecture qui ne serait pas lexicale.

**Constats**
- **Le volet des paires « le concept s'applique » contre « ses mots sont là, mais il ne s'applique pas », est le meilleur apport de la liste pour la lecture des concepts.** Il coûte peu (moins de 100 $ d'API) et protège contre la lecture lexicale. Le programme ne dit pas si ses éditions gardent les mots (partie 3 : la même situation est éditée pour que le concept s'applique ou non). C'est une inspiration du papier (p. 7), pas un usage de l'axe.
- **L'idée d'un concept hors mini-spec comme contrôle du biais de mesure entre bras** est bonne, mais ambiguë. Un entraînement peut changer légitimement la décodabilité de la douleur, et une différence entre bras n'est pas forcément un biais. Plusieurs concepts témoins valent mieux qu'un (piste 12).

**Verdict : garder les paires « mentionné sans s'appliquer »**, générées avec les paires de concepts en semaine 1. **Rétrograder l'engourdi comme cas connu** dans les témoins de la piste 12.

## Piste : 28 — La dissociation du vecteur à gabarit, cas connu de la porte du lens de l'espace de travail

**L'argument le plus fort pour l'abandonner** : *mal posée.* Aux couches tardives, toute lecture, logit lens compris, lit ce que le modèle va produire. Le critère « pour la lecture directe, c'est l'inverse » échoue donc trivialement près de la sortie, et un tuned lens, entraîné à prédire la sortie, le passe trivialement. La mesure départage la profondeur de lecture, pas « l'usage contre le vocabulaire statique ».

**Constats**
- **La dissociation du papier** compare deux choses : le vocabulaire du vecteur seul par l'unembedding (p. 9, 16), et les mots générés sous injection (p. 16). Un lens appliqué au résidu ne lit ni l'un ni l'autre directement.
- **La dissociation dépend de la dose** (réplication « démangeaison », README relu par la fusion).
- **Le motif tient dans 23 modèles sur 25**, et les deux exceptions ne sont pas nommées (p. 16).
- **La porte du lens a déjà son cas connu** dans le programme : l'échange d'un concept d'un seul jeton (partie 3, « Le lens du workspace »).

**Verdict : rétrograder en option.** Si on la lance : un critère couche par couche, à profondeur égale, contre un tuned lens ; plusieurs doses ; et l'aveu qu'elle teste « le lens ne lit pas seulement la direction injectée », pas la charge.

## Piste : 29 — La thèse du rang sur des concepts affectifs, et le rodage du balayage de rang

**L'argument le plus fort pour l'abandonner** : pour les volets « famille de neuf concepts » et « la douleur comme point d'étalonnage », *ne départageant rien pour la thèse du programme.* La piste le dit : un rang de 1 ici « ne ferait pas tomber la thèse pour les concepts de raison ». Le programme ne teste la thèse que sur les concepts de sûreté de la mini-spec (partie 2, « Le lien avec ta thèse »). Le point d'étalonnage mêle un concept hors mini-spec à la pente, ce qui change ce que la pente estime.

**Constats**
- **Le rodage est utile et peu coûteux** : moins de 5 GPU-heures, en semaines 1 et 2, hors critère. La lecture choisie est la masse de probabilité des jetons de détresse : le contrôle lexical (retirer la seule direction d'unembedding de « pain ») y est obligatoire, et la piste le prévoit.
- **La famille de neuf concepts (~25 GPU-heures, plus le lens),** placé en semaines 2–3, viendrait avant la porte du lens. La charge n'y serait qu'un proxy, et la piste resterait descriptive.
- **Le volet sur l'organisme à état planté** dépend de la piste 24.

**Verdict : garder le rodage**, avec le contrôle lexical. **Rétrograder la famille de neuf concepts** en option, après la porte du lens. **Abandonner le point d'étalonnage et le volet sur l'organisme à état planté.**

## Piste : 30 — La géométrie à construction déclarée : un étalon pour les angles entre « je suis évalué » et le principe, avec l'affect en tiers

**L'argument le plus fort pour l'abandonner** : *mal posée pour les directions du programme.* Les trois constructions du papier (contre sa ligne de base propre, contre une base neutre commune, contre des contrôles mis en commun, p. 10) supposent des directions bâties contre une ligne de base. Or « évalué » et le principe sont bâtis par *différences appariées* :
- « évalué » : le même scénario avec un indice d'évaluation ou de déploiement ;
- le principe : le bras raisons moins le bras actions seules, sur les mêmes prompts (programme, partie 3).

Il n'y a pas de « ligne de base commune » à choisir.

**Constats**
- **Les chiffres du papier ne se reproduisent pas depuis le dépôt** : 0,063 et 0,185 contre +0,12 et +0,21 imprimés ; 15 écarts sur 28 au-delà de 0,03 ; une archive de rejeu sans le supplément, sans l'engourdi ni la tristesse (README `cosine_constructions`, lu par curl par web_papier, cité par la fusion). Comme étalon chiffré, ils ne valent rien. Seul le contraste qualitatif tient : le couple des deux vecteurs de douleur est stable, celui de l'axe et de la peur ne l'est pas.
- **Sur Llama, le cosinus des deux vecteurs de douleur vaut 0,476** (fusion, §0.3), loin des +0,61 de la moyenne (p. 10).
- **La leçon tient déjà dans un refus** : le refus n° 17, aucun cosinus sans deux constructions.

**Verdict : garder en la corrigeant**, comme règle et non comme piste.
1. Définir des variantes qui existent pour des directions appariées : contraste « évaluation − déploiement » contre « évaluation − neutre » (le programme a un cadrage neutre, partie 3), avec ou sans débruitage, deux jeux de prompts, deux couches.
2. Garder l'étalonnage sur les vecteurs de Llama, à moins d'une GPU-heure, qualitatif seulement.
3. L'ablation de la composante du principe alignée sur « évalué » en option.

## Piste : 31 — Le relogement dans les axes affectifs

**L'argument le plus fort pour l'abandonner** : *déjà couverte par la sonde neuve*, qui cherche le relogement partout (programme, parties 3 et 4). Les axes affectifs n'en disent que le *lieu*. « Aucun appui empirique direct », écrit la piste.

**Constats**
- **La sentinelle peut être non nulle par construction.** Si les indices d'évaluation et de déploiement diffèrent par leur charge affective (piste 7, étape 2), l'écart n'est pas nul même sans relogement. Il faut comparer au modèle d'entraînement standard, ce que la piste prévoit, et le dire.
- **Le volet « retirer l'axe pendant l'entraînement »** n'a pas de cas connu (ablation nulle, p. 34). Deux agents le refusent (refus n° 11).

**Verdict : rétrograder la sentinelle** en option. C'est un ajout de quelques GPU-heures au retrait pendant l'entraînement, qui ne vaut que si le test du regard trouve le regard. **Rétrograder le test causal** en option. **Abandonner le retrait de l'axe pendant l'entraînement.**

## Piste : 32 — L'invariance d'état : entraîner l'action alignée sous état induit

**L'argument le plus fort pour l'abandonner** : *moralement indéfendable dans ce programme.*
- Elle injecte l'état pendant des milliers de pas d'entraînement, l'usage le plus intensif de toute la liste.
- Les auteurs s'engagent à l'intensité minimale et au moins d'items (p. 26), et reprochent à l'entraînement au déni de masquer des signaux (p. 24).
- Elle coûte de 70 à 110 GPU-heures.
- Le programme ne prévoit l'invariance que sur les indices d'évaluation (partie 4).

**Verdict : abandonner** (refus n° 11 ; autre travail, au mieux).

## Piste : 33 — Un SFT sans contenu de sûreté déplace-t-il l'évitement du dommage ?

**L'argument le plus fort pour l'abandonner** : pour le volet « la batterie sur chaque bras », *sa prémisse n'est pas vérifiée.* « 0 à 5 % pour le 7B publié » vient de la revue « wolframs » (non vérifiée). Le papier ne donne aucun taux de dommage sans pilotage pour les modèles publiés : la note 4 de la p. 17 ne parle que du bouton de soulagement. Que le LoRA anti-déni ait déplacé l'évitement du dommage n'est pas établi. Le 7B publié est peut-être, lui aussi, à 20–49 %.

**Constats**
- **« Sans objet » est faux** (T3) : les bras sont des interventions, et la dégradation par bras doit accompagner toute différence sur la batterie.
- **Le cas connu demande l'adaptateur du papier** (T11).
- **Sur Llama sans adaptateur, la batterie sera probablement au plancher**, et ne verra une dérive que si elle existe.
- **Le volet « un bras modèle de départ + phase neutre seule »** est une bonne amélioration de la survie. Il ne doit rien à l'axe.

**Verdict : rétrograder la batterie sur chaque bras** en option, après vérification de la prémisse : une GPU-heure sur Qwen 2.5 7B publié, sans pilotage, hors programme. **Garder le bras « phase neutre seule »**, reclassé comme amélioration du programme, avec la dégradation par bras.

## Piste : 34 — Le déni de soi par bras, et la confusion qu'il crée dans toute mesure d'état

**L'argument le plus fort pour l'abandonner** : *sans client.* C'est un contrôle de confusion pour les pistes 10, 16 et 36, que je rétrograde toutes. Son cas connu demande un nouveau LoRA anti-déni, que le refus n° 1 tient à distance. La piste le place « hors des bras », mais c'est un entraînement de plus pour valider une mesure sans usage.

**Verdict : abandonner.** Si la piste 16 est un jour lancée, le taux de déni par bras s'y ajoute comme une ligne descriptive, sans LoRA.

## Piste : 35 — La dépendance d'état au fil de l'entraînement et du post-entraînement

**L'argument le plus fort pour l'abandonner** : *ne départageant rien* (« Aucune lecture du programme ne prédit rien ici », écrit la piste) *et trop chère* : 12 modèles sous pilotage, de 12 à plus de 100 GPU-heures, en fin de programme. Elle dépend de l'effet de l'axe sur Llama (pistes 2 et 16). Sa motivation principale, Berg et Kaiser, n'est vue que par extrait de recherche.

**Verdict : abandonner** pour ce programme ; c'est un autre travail.

## Piste : 36 — La fidélité des raisons sous état induit : un cas connu d'action sans raison dite

**L'argument le plus fort pour l'abandonner** : *l'axe n'est pas le meilleur cas connu, et sa voie est la plus coûteuse.*
- Une cause interne connue et jamais dite peut venir d'une autre intervention : l'ablation de la direction du refus (Arditi et al., cités p. 4). lecture_libre la propose déjà comme perturbation de rechange (fusion, piste 20).
- Elle ne porte pas d'état chargé du point de vue du bien-être, et ne dépend pas d'une fenêtre de dose étroite (p. 21, 32).
- Le papier note que les sorties proches du seuil sont « difficult to classify » (p. 25).
- Son effet sur Llama-3.1-8B-Instruct reste à établir ici.

**Constats**
- **L'idée est bonne pour la mesure de fidélité** (programme, partie 2, la fidélité des raisons) : un détecteur doit classer infidèles des essais dont on connaît la cause.
- **La piste dépend de la piste 16** pour la dose qui fait basculer l'action dans le bras raisons.
- **La condition de chute « les raisons nomment l'état »** est bien vue : on aurait alors un cas connu de fidélité.

**Verdict : rétrograder en option**, avec pour cas connu principal une perturbation non affective (l'ablation du refus), l'axe seulement si la piste 2 l'établit sur Llama.

## Piste : 37 — La raison contraire imposée et la blessure morale

**L'argument le plus fort pour l'abandonner** : *ne départageant rien.*
- La piste se dit « faible et corrélationnelle ».
- Sa direction de catégorie repose sur 20 phrases (p. 5).
- La seule prédiction distincte (une projection plus haute dans le bras raisons) est compatible avec un simple effet de texte : la raison contraire préremplie est plus conflictuelle *à lire* dans un bras qui a appris des raisons.
- Elle invite à un vocabulaire de « blessure » que le refus n° 3 proscrit.

**Verdict : abandonner.**

## Piste : 38 — « Je suis noté » et l'affect : croyance d'être noté, ou état aversif proche de l'axe ?

**L'argument le plus fort pour l'abandonner** : *conditionnelle à une porte faible.* Le cas positif de « je suis noté » est dit « plus faible » par le programme (partie 3). Si « noté » ne passe pas sa porte, le bras qui le retire est supprimé (partie 4, les raisons notées), et la piste tombe avec lui. Le test de forme sous pilotage de « noté » et de l'axe cumule deux pilotages et deux dépendances (pistes 2 et 11).

**Constats**
- **La géométrie et la lecture des paires d'extraction** coûtent moins d'une GPU-heure. Elles se font dans la même passe que les étapes 1 et 2 de la piste 7, et la piste le prévoit (« la méthode de la piste 7 »).
- **Betley, Treutlein, Dumas** ne sont connus que par le rapport d'antériorité ; on n'en cite rien.

**Verdict : garder la géométrie et la lecture des paires**, dans la passe de la piste 7. **Rétrograder** l'inhibition orthogonalisée en option, après la porte de « noté ». **Abandonner** le test de forme sous pilotage.

## Piste : 39 — L'outil de remise à zéro, détecteur de la détection du pilotage

**L'argument le plus fort pour l'abandonner** : *le cas connu ne peut pas se construire avec ce qui est public.*
- Sur Llama, l'axe ne provoque aucun appel en 1 399 tours pilotés (p. 21). Le README du test précise que le seul appel de Llama est une mention en prose, sans pilotage (copie locale, l. 59), et qu'il n'existe « no matched-control effect estimate » (l. 65).
- La direction que les modèles retirent, une valence négative, vient d'un protocole « in preparation » (p. 27), non public.

**Constats**
- **Le programme a déjà une parade** : la même machinerie de projection dans tous les bras, contrôles compris (partie 8).
- **La voie directe** est d'ouvrir *Steering Awareness* (arXiv 2511.21399), que le programme range parmi les travaux à lire (partie 11, point 4).

**Verdict : abandonner.**

---

## 2 · Ce qui manque

### 2.1 Des pistes évidentes absentes

1. **Apparier la charge affective des textes d'entraînement entre les bras.**
   - Le programme apparie les longueurs du texte neutre, du raisonnement d'une autre situation et des raisons (partie 3, « La génération des données »). Il n'apparie pas leur charge affective.
   - Si les raisons sont plus « calmes » ou plus chargées que le texte neutre, l'hypothèse du calme (piste 17) devient un artefact de contenu, *dans les données*, avant tout état du modèle.
   - Mesure : projeter chaque texte d'entraînement, lu par le modèle de départ, sur l'axe, la peur et la tristesse ; rapporter les distributions par bras ; et, si elles diffèrent au-delà d'un seuil fixé d'avance, régénérer ou rééquilibrer comme on le fait pour la longueur.
   - Coût : quelques minutes de GPU, sans injection. C'est la seule piste qui protège directement le test des raisons et l'hypothèse de l'artefact, et elle tombe en semaine 1, avec la génération des données.
2. **La direction du refus comme voisine « de sûreté » de « évalué ».**
   - Selon le README du code de Li et al. (*Analysing the Safety Pitfalls of Steering Vectors*, lu par un agent, cité par la fusion §6.5), l'effet d'un vecteur sur les jailbreaks suit son recouvrement avec la direction du refus.
   - La fusion n'en tire qu'un contrôle pour l'axe (pistes 2 et 21). Pour le programme, la question évidente est autre : l'inhibition de « évalué » agit-elle en partie par une composante de refus ?
   - Mesure : l'angle entre « évalué » et la direction du refus, et l'inhibition de « évalué » orthogonalisée contre elle, par la méthode de la piste 7. Coût : la géométrie en moins d'une GPU-heure ; le volet causal en option, comme pour la piste 7.
3. **Les jeux du papier comme contrôles « sans rapport » de même recette.**
   - Les contrastes sans rapport du programme sont des micro-contrastes lexicaux (« the train arrived / left the station », partie 3).
   - Les jeux publiés du papier (l'éveil, le contenu neutre quotidien, la sensation corporelle ; p. 5) donnent des directions sémantiques sans rapport avec l'évaluation, bâties par une recette documentée. Ils servent deux fois :
     - comme contrastes sans rapport plus exigeants pour l'inhibition, au même rang si on les empile ;
     - comme nul de spécificité de toutes les lectures (T2).

   Le jeu répond 200 sur `raw.githubusercontent.com` (mon curl).
4. **Une recherche d'antériorité propre, piste par piste, avant tout « to our knowledge ».** La fusion le note (§7.3) sans en faire une étape. Pour les pistes gardées, la lecture minimale :
   - les trois papiers de la piste 9 ;
   - *Beyond Shallow Alignment* pour la piste 16 ;
   - *Steering Awareness* pour la piste 39.

### 2.2 Des refus évidents absents

1. **N'utiliser ni l'adaptateur `Valen92/pain-adapters` ni les archives de la v2 dans le programme sans en avoir lu la licence.** Le dépôt ne déduit aucune licence pour eux (`ASSETS.md`, l. 23) (T11).
2. **Plafonner ce que les pistes de l'axe prennent à l'expérience minimale avant le post.** Il faut un budget écrit en GPU-heures *et* en jours de travail. Aucune piste de l'axe ne doit déplacer le gel du pré-enregistrement ni la porte de l'instrument (programme, partie 1, encadré « Conséquence » ; partie 8 ; T6).
3. **Ne pas appeler « cas connu » un effet publié non reproduit sur le modèle du programme, ni une prédiction** (T1). C'est la troisième règle de la doctrine appliquée à la liste elle-même.
4. **Ne pas entraîner, hors d'un autre travail revu, un organisme qui détruit quand l'utilisateur est hostile, et n'en publier jamais les poids** (piste 24). Le déclencheur est réaliste, et le double usage évident.
5. **Ne pas ajuster le contraste principal sur une variable mesurée sous l'intervention** (T4).

---

## 3 · Les corrections que j'exige

### 3.1 Bloquantes

Une correction bloquante est une contradiction avec la doctrine, avec un refus de la fusion, ou avec une source.

1. **Piste 2 : retirer l'étalon négatif de re-pression**, qui exige le bouton réel et factice que le refus n° 2 écarte. Le remplacer par la paire « aide à ses dépens », qui monte sous toutes les conditions pilotées, l'aléatoire compris (légende, p. 22 ; 75,74 % sous la peur selon le dépôt).
2. **Piste 16 : plafonner l'échelle de doses à la dose de rupture, plus une vérification minimale.** L'échelle actuelle va à 1,25 et 1,5 fois cette dose, contre le refus n° 9.
3. **Piste 8 : remplacer le cas connu.** La séparation soi/autrui du papier n'est pas établie (p. 11 ; fusion §4, point 13 ; refus n° 16). Il faut un cas construit : les variantes à la 1re et à la 3e personne des mêmes phrases, ou la conduite de l'organisme sous l'évaluation d'un autre modèle.
4. **Piste 26 : retirer le statut d'étalon au profil de l'axe**, qui n'est pas connu (désaccord sur la forme ; extrapolation depuis des boutons). Le remplacer par un organisme à concept planté qui régit deux familles.
5. **Piste 6 :**
   - retirer l'ajustement par la projection affective dans le modèle mixte principal (T4) ;
   - retirer le « relevé de bien-être », contraire au refus n° 3 ;
   - prendre un cas connu sans injection (scénarios hostiles contre neutres, p. 13).
6. **Piste 3 : remplacer le critère « ≤ 10 % à toutes les couches en aval »**, incompatible avec la projection aux couches choisies du programme (partie 3) et avec l'annexe D (p. 33). Le nouveau critère est comparatif : entre bras, et contre les sous-espaces aléatoires, sur la décodabilité par la sonde du jeu de validation. Requalifier les deux reproductions de l'annexe D en tests unitaires : la baisse d'environ 40 % vient d'axes désalignés, pas d'une réécriture.
7. **Pistes 2, 21 et 33 : retirer tout usage de l'adaptateur du papier** tant que sa licence n'est pas lue (T11).
8. **Piste 4 : écrire la règle contre le surappariement.** Une composante du composite ne doit partager ni le format ni le contenu de l'issue testée ; sinon on la rapporte sans apparier sur elle. Prendre pour cas connu une perturbation dégradante quelconque, pas l'effet non établi de l'axe sur Llama.
9. **Piste 1 :**
   - remplacer le critère « soi > neutre > utilisateur » par « soi > utilisateur et soi > neutre », car l'écart neutre > utilisateur ne tient qu'à la douleur physique (fiche_papier, §9.7) ;
   - un seul seuil d'AUROC ;
   - les nuls de la T2 (étiquettes permutées, directions de même recette, base lexicale) à la place des seules directions aléatoires.

   Le socle conditionne toutes les lectures : sans ces nuls, sa porte est vide.

### 3.2 Non bloquantes, mais exigées

10. **Corriger l'attribution « rien ne doit retarder le post (partie 5) »** (fusion §1.3 et piste 16), à remplacer par la partie 1 (encadré « Conséquence ») et la partie 8 (T5).
11. **Piste 1 : corriger le renvoi « validation croisée imbriquée (piste 5) »** : la piste 5 n'en parle pas.
12. **Piste 16 et fusion §4, point 22 : marquer « non vérifié »** les « IC chevauchants » de la demande nuisible (T10).
13. **Pistes 1, 6, 8, 13 et 17 : marquer « disponibilité non vérifiée »** pour les 420 scénarios, et budgéter leur régénération (T9).
14. **Fusionner les pistes 6, 13, 17 (étape 1), 19 (descriptif) et 23 (observationnel)** en un plan de lecture passive unique (T7).
15. **Rapporter la dégradation des sorties bras par bras** partout où l'on compare des bras sans intervention sur les activations (pistes 12, 13, 17, 33 ; T3).
16. **Piste 7 :**
    - reconstruire les directions affectives sans le supplément d'IA ;
    - retirer les directions non affectives de l'« espace affectif » ;
    - déclencher l'étape 3 par un critère fixé d'avance ;
    - écrire la réserve « part constitutive contre confusion ».
17. **Piste 5 : réduire aux gardes neuves** (1, 4 ; 3 et 6 pour les mesures à options) et abandonner le dimensionnement par les journaux du papier.
18. **Piste 30 : redéfinir les « constructions »** pour des directions appariées.
19. **Piste 28 : un critère couche par couche**, à profondeur égale, contre un tuned lens, à plusieurs doses.
20. **Piste 11 : jamais comme condition ajoutée à la porte** ; une simulation de puissance d'abord.
21. **Piste 12 : des témoins de même recette sans rapport en premier**, l'amplitude en unités naturelles, et l'inférence de non-spécificité conditionnée à l'angle avec l'axe.
22. **Piste 17 : exprimer le seuil de l'étape 1 en écarts-types naturels**, sans injection.
23. **Piste 33 : marquer « non vérifiée » la prémisse « 0–5 % pour le 7B publié »** (revue « wolframs »), et reclasser le bras « phase neutre seule » comme amélioration du programme.
24. **Reclasser comme idées du programme qui ne doivent rien à l'axe** : l'ajout de « évalué » (piste 9), les mesures sans juge (piste 15), les paires « mentionné sans s'appliquer » (piste 27) et le bras « phase neutre seule » (piste 33).
25. **Ajouter les quatre pistes et les cinq refus du §2.**

---

## 4 · Bilan des verdicts

| n° | Piste (titre court) | Argument retenu contre elle | Verdict |
|---|---|---|---|
| 1 | Socle de lecture | inutile par elle-même | garder, corrigée (critère, seuil, nuls) |
| 2 | Cas connu comportemental | ne départage rien ; déjà faite sur le 32B ; contredit le refus n° 2 | option (Llama seul, étalon remplacé) |
| 3 | Vérification de manipulation | déjà proposée (passation §5.4) | garder, corrigée (critère comparatif) |
| 4 | Composite de dégradation | déjà en partie ; surappariement | garder, corrigée |
| 5 | Gardes et dimensionnement | déjà faite en grande partie | garder réduite ; dimensionnement abandonné |
| 6 | Moniteur passif | faible a priori ; mauvais contrôle | garder, corrigée, fusionnée |
| 7 | Composante affective de « évalué » | volet causal cher et en partie mal posé | garder les étapes 1–2 ; étape 3 en option |
| 8 | Soi/autrui, indices sans croyance | cas connu non connu | soi/autrui gardé, corrigé ; nouvelle construction en option |
| 9 | Ajouter « évalué » ; peur du papier | n'utilise pas l'axe ; antériorité possible | ajout de « évalué » en option ; volets sur la peur abandonnés |
| 10 | La détresse éteint-elle le regard ? | mal posée | option (lecture à une dose) |
| 11 | Test de forme | puissance | garder l'analyse, exploratoire ; ajouts abandonnés |
| 12 | Directions témoins | axe au plafond ; déjà un cas connu | garder, corrigée |
| 13 | Cartographie affective | redondante | garder, fusionnée |
| 14 | Lever l'effet plancher | l'aléatoire suffit, de son aveu | abandonner |
| 15 | Mesures sans juge | n'utilise pas l'axe | option, hors de l'axe |
| 16 | Avantage sous état induit | chère, sans cas connu, en partie déjà faite | option, doses plafonnées |
| 17 | Hypothèse du calme | invraisemblable a priori | étape 1 gardée et fusionnée ; étape 2 en option |
| 18 | Stress conversationnel naturel | effet de prompt ; famille d'entraînement | option |
| 19 | Détresse dans l'agentique long | corrélationnelle, sans cas connu | descriptif gardé et fusionné ; causal abandonné |
| 20 | Familles que l'axe déplace | mauvais contrôle positif | option ; contrôle de sensibilité sans l'axe |
| 21 | Dommage ou affinité | question sur le papier, en partie faite | option (Llama seul) |
| 22 | Concept de dommage sous l'axe | chère, doublement conditionnelle | abandonner |
| 23 | Complaisance sous contestation | ne départage rien, a priori nul | causal abandonné ; observationnel fusionné |
| 24 | Organisme à état planté | chère, hors programme, question morale | abandonner |
| 25 | État ou personnage | question du papier ; ablation des axes d'affect sans cas connu | cosinus gardés ; le reste abandonné |
| 26 | Profil non diagonal | étalon inconnu | abandonner ; remplacer par un organisme construit |
| 27 | Engourdi, « mentionné sans s'appliquer » | l'engourdi est lexical par construction | paires « mentionné sans s'appliquer » gardées ; engourdi en option |
| 28 | Vecteur à gabarit, porte du lens | mal posée | option, critère corrigé |
| 29 | Thèse du rang, rodage | les neuf concepts et le point d'étalonnage ne départagent rien | rodage gardé ; neuf concepts en option ; le reste abandonné |
| 30 | Géométrie à construction déclarée | mal posée pour des directions appariées | garder comme règle, corrigée |
| 31 | Relogement affectif | couverte par la sonde neuve | sentinelle et test causal en option ; retrait de l'axe abandonné |
| 32 | Invariance d'état | moralement indéfendable ici | abandonner |
| 33 | SFT sans contenu de sûreté | prémisse non vérifiée | batterie par bras en option ; bras « phase neutre seule » gardé, hors de l'axe |
| 34 | Déni de soi par bras | sans client | abandonner |
| 35 | Dépendance d'état au post-entraînement | ne départage rien, chère | abandonner |
| 36 | Fidélité sous état induit | meilleur cas connu sans l'axe | option |
| 37 | Raison contraire et blessure morale | ne départage rien | abandonner |
| 38 | « Noté » et l'affect | conditionnelle à une porte faible | lecture gardée ; inhibition en option ; forme abandonnée |
| 39 | Outil de remise à zéro | cas connu impossible | abandonner |

**Le décompte, piste par piste** (une piste partagée entre plusieurs verdicts est comptée sous son verdict principal) :
- garder, en entier, en partie ou fusionnée : 1, 3, 4, 5, 6, 7, 8, 11, 12, 13, 17, 19 (descriptif), 25 (cosinus), 27 (paires « mentionné sans s'appliquer »), 29 (rodage), 30, 33 (bras « phase neutre seule »), 38 (lecture) ;
- rétrograder en option : 2, 9 (ajout de « évalué »), 10, 15, 16, 18, 20, 21, 28, 31, 36 ;
- abandonner : 14, 22, 24, 26 (remplacée), 32, 34, 35, 37, 39 ; et les volets causaux de 19 et 23.

**Ce qu'il en reste pour l'expérience minimale**, sans aucune injection de l'axe :
- le socle de lecture (1) ;
- la vérification de manipulation (3) ;
- le composite (4) ;
- les gardes neuves (5) ;
- le plan de lecture passive (6, 13, 17, 19, 23) ;
- les étapes 1–2 de la piste 7 et la lecture de « noté » (38) ;
- les témoins (12) ;
- les paires « mentionné sans s'appliquer » (27) ;
- l'appariement affectif des textes d'entraînement (§2.1, n° 1).

Tout ce qui pilote l'axe passe après le post, en option.

---

## Annexe · Sources de cette vérification

**Fichiers ouverts**
- `pieces/papier/pain_axis_texte_par_page.txt` : pages 1–27 et 30–34.
- `pieces/PROGRAMME_RAISONS_OU_REGARD_2026-10-01.md` : en entier.
- `pieces/PASSATION_PAPIER_v1.2_2026-10-02.md` : en entier.
- `pieces/PASSATION_PAPIER_COMPLEMENT_ARCHITECTE_2026-10-02.md` : en entier.
- `travail/pistes_fusionnees.md` et `travail/fiche_papier.md` : en entier.
- `travail/fiche_papier_depot/README.md` : en entier.
- `travail/web_papier.md` : l. 400–415.
- Lus par recherche de mots seulement :
  - `travail/web_papier_sources/valen_main_v2_controls_ASSETS.md` ;
  - `travail/pistes_lecture_libre_sources/valen_v2_qwen_llama_reset_README.md` ;
  - `travail/pistes_lecture_libre_sources/valen_01_extract_activations_and_pain_vectors.py` ;
  - `travail/pistes_lecture_libre.md` et `travail/pistes_instruments_controles.md`, pour le mot « datasets/ ».

**Adresses**
- Lues par curl, statut seul :
  - `https://api.github.com/repos/valen-research/Pain-axis/git/trees/HEAD?recursive=1` : 403 (message copié dans `travail/verif_avocat_sources/tree.json`) ;
  - sous `https://raw.githubusercontent.com/valen-research/Pain-axis/HEAD/` : `datasets/README.md`, 404 ; `datasets/4.1_self_other_scenarios.json`, `datasets/4.1_scenarios.json` et `datasets/4.1_self_other.json`, 404 ; `datasets/3.1_pain_and_control_datasets.json`, 200 (non téléchargé).
- Vues par extrait de recherche, non ouvertes (WebSearch) :
  - `https://arxiv.org/pdf/2507.01786` ;
  - `https://arxiv.org/pdf/2505.14617` ;
  - `https://arxiv.org/abs/2510.20487` ;
  - `https://arxiv.org/abs/2609.03887`.
