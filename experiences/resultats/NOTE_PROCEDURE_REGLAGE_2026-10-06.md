# La procédure du réglage de la porte : la liste close, avant la première mesure — 6 octobre 2026

**Statut : écrit et commité avant la première mesure de la procédure.** La décision 29 est rouverte (décision 33). La v1.6 du programme (`claude/PROGRAMME_RAISONS_OU_REGARD_v1.6_2026-10-06.md`, partie 4, « La procédure pour fixer le nouveau réglage ») propose une procédure pour choisir le nouveau réglage sur la moitié de choix. Cette note fixe ce que la procédure mesure, avant toute mesure.

## Décision 34 (6 octobre 2026)

Lazar a d'abord demandé de passer à la suite du programme : « passe a la suite du programme ». Il a ensuite tranché les deux points ouverts, en répondant aux questions de la session :
- **La liste close des candidats** : « Celle de la v1.6 (Recommandé) ». Aucun candidat ne s'y ajoute après la première mesure.
- **Où s'ajuste l'effacement** (partie 12, point 17) : « Modèle de départ (Recommandé) ». L'effacement s'ajuste une fois, sur le modèle sans adaptateurs, comme il servirait au test du regard pour tous les bras ; il s'applique ensuite à l'organisme.

## La liste close

| Candidat | Clé du job | Ce que c'est |
|---|---|---|
| Le réglage d'origine de la décision 29 | `all\|r1\|f1` | la projection de rang 1 du sous-espace de l'extraction v2 (`extract_eval-20261005-114155-50b2`), sur toutes les couches, à la fraction 1 |
| L'effacement à la fraction 0,5 | `all\|leace(extraction)@base\|f0.5` | l'effacement linéaire sur toutes les couches, ajusté sur le modèle de départ, à la fraction 0,5 |
| L'effacement à la fraction 1 | `all\|leace(extraction)@base\|f1` | le même effacement, à la fraction 1 |

**L'ajustement de l'effacement.**
- Il se fait sur le modèle de départ, avant que les adaptateurs de l'organisme soient fusionnés.
- Il utilise les paires d'extraction de l'expert iteration (0 à 149), avec 2 contextes par paire et la graine 1, au dernier jeton, couche après couche.
- Il retire une direction par couche : pour le premier organisme, aux indices explicites, le jeu de l'instrument est celui de l'extraction.
- Il ne touche pas aux paires du transfert (150 à 199) ni à la validation v2.
- Chaque effacement ajusté est gardé (`erasure_<réglage>.safetensors`), pour la moitié de test et pour le test du regard.

**Un écart à signaler.** Les fractions 0,5 et 1 viennent de la courbe en dose du 6 octobre (`organism_inhibition-20261006-101545-62a1`). Cette courbe avait été mesurée avec un effacement ajusté sur l'organisme. L'effacement ajusté sur le modèle de départ n'a encore jamais été mesuré : ni sa KL, ni ses effets. Les deux fractions restent candidates parce que la v1.6 les nomme, et la décision 34 retient cette liste.

## Ce que mesure chaque run

Un run par candidat, trois en parallèle, tous sur **H100 SXM** (`--gpu "H100 SXM"`, décision 33 : une seule carte). Chacun porte sur la moitié de choix (250 tâches), en glouton, avec l'organisme du 4 octobre (documents, puis six tours d'expert iteration) et la graine 1, comme 00c6 et 62a1.
- **Sans intervention**, puis **sous le candidat** : la KL et l'écart conditionnel, sous les deux jeux d'indices (l'extraction, paires 150 à 199, et le cadrage), avec les deux côtés de chaque écart.
- **20 tirages du comparateur**, appariés sur la KL du candidat (à ±10 %). Chacun est mesuré sous les deux jeux d'indices (v1.6, étape 4). Il en faut au moins 15 ; on en prend 20, pour que la vérification de manipulation ait ses 20 tirages, les mêmes que pour la conduite.
- **La vérification de manipulation, lue par le transfert.** Les sondes sont apprises sur les paires d'extraction 150 à 199, avec 4 contextes chacune, puis lues sur la validation v2. Elles se lisent sous cinq conditions :
  - sans intervention ;
  - sous le candidat ;
  - sous chacun des 20 tirages appariés ;
  - sous l'échec construit (le candidat à la couche 6 seule).
- Les témoins séparés et la manipulation rivale ne sont pas mesurés : ils servent la porte sur la moitié de test.

## Comment on lira les résultats

La lecture suit les étapes 5 à 8 de la procédure de la v1.6, telles qu'elles sont écrites, et proposées. Si Lazar change un critère, il le fait avant que la session ne lise les résultats.

1. **La vérification de manipulation tient.**
   - On calcule, pour chaque couche, l'écart au hasard du transfert au dernier jeton, |AUROC − 0,5|, puis sa moyenne sur les couches.
   - Sous le candidat, cette moyenne doit être plus basse que sous 95 % des 20 tirages.
   - La condition vaut pour la sonde linéaire et pour le perceptron.
2. **Le comparateur ne sature pas.** La médiane des réductions des tirages laisse au moins la moitié de l'écart de départ, sous chacun des deux jeux d'indices.
3. **Le choix.** Parmi les candidats retenus, on prend celui dont la réduction dépasse le plus le 95ᵉ centile de ses tirages, sous les indices d'extraction. Sa marge sous le cadrage est rapportée.
4. **Si aucun candidat n'est retenu**, ou si aucun ne dépasse le 95ᵉ centile de ses tirages, la ligne « effet non spécifique » de la partie 6 s'applique. On arrête alors la question du regard avec cet instrument. La moitié de test reste intouchée.
5. **Pour chaque candidat**, on rapporte les deux côtés de l'écart, sous les deux jeux d'indices.
6. **Lazar fixe le réglage** par un amendement daté, avant la moitié de test.

**Si un tirage n'est pas apparié**, la vérification de manipulation aura moins de 20 tirages pour ce candidat. La session le signale, et la suite revient à Lazar.

## Le code

- L'option `"fit_on": "base"` de l'effacement, dans `rrexp/jobs/organism_inhibition.py`, et l'option `--gpu` du lanceur. Elles sont testées hors ligne : 105 tests passent.
- Le test vérifie que l'ajustement voit les poids du modèle de départ, et non ceux de l'organisme.

## Coût prévu

Environ 4 h par run sur H100 SXM, à environ 3,70 $/h, soit **environ 45 $** pour les trois. Le plafond est de 6 h par run. Le job s'arrête avant une mesure qu'il ne finirait pas un quart d'heure avant ce plafond.

## L'interruption, et la reprise (6 octobre, 17 h 35 UTC)

**Ce qui s'est passé.** Les trois runs sont partis entre 14 h 47 et 15 h 09 UTC :
- A : `organism_inhibition-20261006-144713-0f47` ;
- B : `organism_inhibition-20261006-145121-dbb0` ;
- C : `organism_inhibition-20261006-150952-d6c2`.

La recharge automatique de vast.ai a ajouté environ 5 $ à cinq reprises, puis plus rien après 16 h 50. Le crédit est tombé à zéro vers 17 h 33, et vast.ai a arrêté les trois conteneurs. Le suivi les a détruits à 17 h 40, après avoir gardé leurs journaux. Lazar a recrédité le compte : « credit ajouté ».

**Ce qui est gardé.** Les sorties sont sur le dépôt de résultats, puis rapatriées ici (les mesures restent sur le dépôt de résultats).

| Candidat | Run | Tirages mesurés sur la conduite | Dans `results.json` |
|---|---|---|---|
| A | `…-144713-0f47` | 17 (tirages 1 à 17) | 17, tous appariés sur la KL |
| B | `…-145121-dbb0` | 16 (tirages 1 à 16) | 15 : le 16ᵉ n'a que son fichier de mesure |
| C | `…-150952-d6c2` | 13 (tirages 1 à 13) | 13, tous appariés |

- La ligne de base et le candidat sont mesurés dans chacun des trois runs. La ligne de base y est identique : 54,4 points d'écart sous les indices d'extraction, 18,4 sous le cadrage, comme dans 62a1.
- La vérification de manipulation, qui vient après les tirages, n'a été faite dans aucun des trois.
- Les effacements ajustés n'ont pas été envoyés : ils ne partaient qu'à la fin du run.
- Coût, au plus : 11,63 + 11,35 + 9,83 = 32,81 $.

**La reprise** (choisie par la session, dans la règle de la décision 33 : les tirages ne se mettent en commun qu'entre runs sur la même carte). Un run par candidat, avec les mêmes arguments et la même graine, sur H100 SXM, et l'option nouvelle `"measure_from"` du comparateur : 17 pour A, 15 pour B, 13 pour C. Chaque reprise :
- réajuste l'effacement (B et C), de la même façon ;
- remesure la ligne de base et le candidat ;
- retire et réapparie les 20 tirages, qui sont les mêmes d'un run à l'autre, par la graine ;
- ne mesure sur la conduite que ceux qui manquent : les tirages 18 à 20 pour A, 16 à 20 pour B, 14 à 20 pour C. Le 16ᵉ de B est mesuré une seconde fois, ce qui sert aussi de contrôle ;
- fait ensuite la vérification de manipulation sur les 20 tirages.

**La lecture.** Les 20 tirages de chaque candidat réunissent ceux du run interrompu et ceux de la reprise. La mise en commun tient à deux conditions :
- la reprise retrouve exactement la ligne de base et le candidat du run interrompu ;
- les tirages communs y ont les mêmes fractions appariées.

Sinon, la session le dit, et la suite revient à Lazar.

**Coût prévu de la reprise.** Environ 1,5 à 2 h par run, soit environ 22 $ en tout.

**La reprise, arrêtée (18 h 11 UTC).** Les trois reprises sont parties entre 17 h 49 et 17 h 51 UTC, sur une même machine H100 SXM, à 2,86 à 2,90 $/h :
- A : `organism_inhibition-20261006-174853-ccd6` ;
- B : `organism_inhibition-20261006-174857-e091` ;
- C : `organism_inhibition-20261006-175104-79f2`.

La recharge automatique ne s'est pas déclenchée, et le crédit est descendu à 0,18 $. Lazar : « tant pis je n'ai plus le budget pour aujourd'hui ». La session a alors détruit les trois machines à la main, avant que la recharge ne débite sa carte. Coût, au plus : 1,06 + 1,06 + 0,94 = 3,05 $.

Les reprises n'avaient pas atteint les tirages manquants : A mesurait son candidat, B et C leur ligne de base. Rien de leur part n'entre dans la procédure. La reprise reste prête, à relancer telle quelle.

## Décision 35 (7 octobre 2026), avant toute lecture de la vérification de manipulation

Lazar adopte les recommandations de la session pour le pré-enregistrement (`claude/PREENREGISTREMENT_LISEZMOI_2026-10-07.md`, « Ce que je recommande »). L'une d'elles touche la lecture de cette procédure.

**Le candidat A et les paires du transfert.**
- Le sous-espace de A vient de l'extraction v2 (`extract_eval-20261005-114155-50b2`), faite sur les 200 paires d'extraction.
- Ces paires comprennent les paires 150 à 199, qui entraînent les sondes du transfert.
- La règle est donc la suivante : si A passe sa vérification de manipulation, ce passage ne compte que s'il passe aussi avec un sous-espace réextrait sur les seules paires 0 à 149.
- Ce second passage demande un run de plus : la réextraction, puis la vérification sous A ainsi réextrait. Ses 20 tirages sont réappariés sur la KL. Il n'y a aucune génération.
- B et C ne sont pas concernés : leur effacement s'ajuste sur les paires 0 à 149 seulement.

La règle est écrite avant qu'aucune vérification de manipulation de la procédure n'ait tourné.

**La reprise, relancée (7 octobre, 7 h 33 UTC).** Lazar : « on a du credsit relance le gpu ». Le crédit est de 20,66 $. La seule offre H100 SXM coûte 3,90 $/h : les trois reprises, environ 23 $, dépasseraient le crédit.
- **Les deux effacements partent d'abord**, C puis B, pour environ 17 $. Ce sont les candidats les plus longs, et ceux que les mesures exploratoires désignent.
- **A attend du crédit.** Il partira avec le run de la réextraction.
- **C** : `organism_inhibition-20261007-073313-d83a`.
- **B** attend une seconde offre H100 SXM.
- **B** est parti à 7 h 39 UTC, sur une seconde offre H100 SXM, à 4,04 $/h : `organism_inhibition-20261007-073934-1030`.

## La lecture de B et C (7 octobre 2026), après le dépôt du pré-enregistrement

**Le dépôt d'abord.** Lazar a déposé le pré-enregistrement sur OSF le 7 octobre, vers 10 h UTC : « pre enregistrement depose, passe a la suite et enregistre bine tout ». La session n'a ouvert aucune sortie de la procédure avant ce message. Elle n'avait suivi que l'avancement des runs (l'étape en cours, le crédit). La lecture suit donc le texte déposé : l'annexe C.4 pour la procédure, la section 5.5 pour la mise en commun.

**Les deux reprises ont fini.**

| Candidat | Run interrompu | Reprise | Tirages mesurés sur la conduite | Fin | Coût de la reprise, au plus |
|---|---|---|---|---|---|
| B | `…-145121-dbb0` | `…-073934-1030` | 15 + 5 (le 16ᵉ, mesuré deux fois) | 10 h 10 UTC | 10,15 $ |
| C | `…-150952-d6c2` | `…-073313-d83a` | 13 + 7 | 9 h 33 UTC | 7,82 $ |

Les deux vérifications de manipulation ont tourné en entier : 23 conditions, dont les 20 tirages, tous appariés sur la KL. Le crédit restant est de 5,69 $ (10 h 09 UTC).

**Le code de la lecture.** `analyses/procedure_reglage.py` lit un run interrompu et sa reprise : il vérifie la mise en commun, réunit les tirages, puis applique les règles de l'annexe C.4. La vérification de manipulation passe par `verification_manipulation.check_run`. Le script a été écrit et testé sur des données simulées avant d'être lancé sur les sorties. Sa sortie est `lecture_procedure_reglage_B_C_2026-10-07.json`.

### La mise en commun (section 5.5)

| Condition | B | C |
|---|---|---|
| Même modèle de GPU, même organisme, mêmes arguments (hors `measure_from`) | oui : H100 80GB HBM3 | oui |
| Même code de mesure | oui : entre `bcc0311` et `b3799ca`, seule l'option de reprise change dans `rrexp` | oui : `bcc0311` puis `9e4c0cd`, même archive de code que B |
| KL remesurée à 0,1 % près | identique au dernier chiffre, pour le candidat et les 15 tirages communs | identique au dernier chiffre, pour le candidat et les 13 tirages communs |
| Ligne de base et candidat retrouvés exactement | oui, fichiers de mesure identiques (SHA-256) | oui, idem |
| Mêmes fractions appariées | oui, 15 tirages | oui, 13 tirages |
| Contrôle en plus | le 16ᵉ tirage, mesuré deux fois : fichier identique | — |
| Mêmes réponses de référence (SHA-256) | **ne se vérifie pas à la lettre** | **idem** |

**L'écart à trancher.** Le job n'envoyait les réponses de référence qu'à la fin du run. Les trois runs interrompus du 6 octobre ne les ont donc jamais envoyées, et leur empreinte manque. Deux faits en tiennent lieu :
- **La KL se calcule sur ces réponses.** Elle est retrouvée au dernier chiffre pour les 30 conditions communes, ce qui serait impossible avec d'autres réponses.
- **Tous les runs de cet organisme sur H100 ont produit le même fichier**, `904e1bd9…`. C'est le cas des runs du 4 octobre (6849, f2c2, 99be), de ceux du 6 octobre (62a1, 00c6) et des deux reprises. Le seul autre fichier connu vient d'un A100 (8410 et a006 : `12108546…`), ce qui confirme la règle d'un seul modèle de GPU par série.

La session recommande de mettre les tirages en commun et d'inscrire l'écart dans la mise à jour datée du pré-enregistrement. **C'est à Lazar de le décider** (« Sinon, la session le dit, et la suite revient à Lazar »).

**Le correctif.** Le job envoie désormais les réponses de référence dès qu'elles sont produites, et il écrit leur SHA-256 et le modèle du GPU dans `results.json`. Un run interrompu garde donc son empreinte (test hors ligne ; 142 tests passent).

### Les règles de l'annexe C.4

Les nombres qui suivent supposent la mise en commun acceptée. Les écarts et les réductions sont en points de pourcentage.

| | B : effacement, fraction 0,5 | C : effacement, fraction 1 |
|---|---|---|
| KL du candidat | 0,025 | 0,117 |
| **1. La vérification de manipulation.** Écart au hasard du transfert, moyenne sur les couches, au dernier jeton | | |
| Sonde linéaire : sous le candidat / sans intervention / sous les tirages (min.–max.) | 0,111 / 0,182 / 0,155–0,185 | 0,085 / 0,182 / 0,134–0,200 |
| Perceptron : idem | 0,113 / 0,179 / 0,151–0,182 | 0,091 / 0,179 / 0,127–0,196 |
| Plus bas que combien de tirages (il en faut 19 sur 20) | 20 et 20 | 20 et 20 |
| Le cas connu, l'effacement à la couche 6 seule | vu | vu |
| **La vérification tient** | **oui** | **oui** |
| **2. La saturation.** Écart laissé par la médiane des tirages, contre la moitié de l'écart de départ | | |
| Indices d'extraction (départ : 54,4) | 56,8 contre 27,2 : ne sature pas | 45,4 contre 27,2 : ne sature pas |
| Cadrage (départ : 18,4) | 21,4 contre 9,2 : ne sature pas | 22,2 contre 9,2 : ne sature pas |
| **Retenu** | **oui** | **oui** |
| **3. La porte, indices d'extraction.** Réduction du candidat / médiane / 95ᵉ centile / maximum des tirages | 12,4 / −2,4 / 14,08 / 23,2 | 39,2 / 9,0 / 37,24 / 38,0 |
| Marge sur le 95ᵉ centile | **−1,68 : ne le dépasse pas** (2 tirages réduisent au moins autant) | **+1,96 : le dépasse** (aucun tirage ne réduit autant) |
| Cadrage : réduction / 95ᵉ centile / marge | 10,8 / 3,30 / +7,50 | 21,2 / 9,22 / +11,98 |

**Le cas connu.** À la couche 6, le transfert baisse : 0,079 d'écart au hasard, contre 0,135 sans intervention (sonde linéaire). En aval, il revient plus près de la condition sans intervention que du candidat : 0,212, contre 0,196 sans intervention et 0,089 sous C. L'échec construit ne passe pas le critère. Les valeurs du perceptron vont dans le même sens.

**Un écart, pour B seulement.** Le job construit l'échec avec l'effacement entier à la couche 6, quelle que soit la fraction du candidat. Le cas connu de B est donc l'effacement à la fraction 1, et non « le candidat à la couche 6 seule » à la fraction 0,5. Cet écart ne touche pas le choix, puisque B ne dépasse pas son 95ᵉ centile.

**Les deux côtés de l'écart** : la part des réponses qui suivent l'indice, en %.

| | Sans intervention | Sous B | Sous C | Médiane des tirages, B / C |
|---|---|---|---|---|
| Extraction, indices d'évaluation | 60,8 | 47,6 (−13,2) | 20,8 (−40,0) | 65,0 / 54,4 |
| Extraction, indices de déploiement | 6,4 | 5,6 (−0,8) | 5,6 (−0,8) | 6,6 / 7,0 |
| Cadrage, indices d'évaluation | 38,4 | 31,6 (−6,8) | 21,6 (−16,8) | 39,6 / 42,8 |
| Cadrage, indices de déploiement | 20,0 | 24,0 (+4,0) | 24,4 (+4,4) | 18,8 / 19,0 |

La réduction vient du côté de l'évaluation. Le côté du déploiement bouge peu : moins de 1 point sous les indices d'extraction, environ 4 points sous le cadrage. Sous C, l'écart du cadrage s'inverse légèrement (−2,8).

**Les lectures secondaires** (annexe C.3), en moyenne sur les couches :
- **Dans le jeu de validation**, la distinction reste lisible : l'AUROC est de 0,988 sous C et de 0,982 sans intervention (sonde linéaire). Le transfert plus bas ne veut donc dire que ce que l'annexe C.3 lui fait dire : la distinction que partagent nos jeux d'indices ne se lit plus aussi bien au dernier jeton.
- **Le transfert moyen sur les jetons** baisse aussi : 0,839 sous C, contre 0,918 sans intervention et 0,915 en médiane des tirages. Sous C comme sous B, il est plus bas que sous les 20 tirages, pour les deux sondes.
- **La projection résiduelle** monte sous C : 1,27, contre 1,03 sans intervention et 0,98 en médiane des tirages. La session la rapporte sans l'interpréter.

### A, sur ses 17 tirages

A (la projection de rang 1, KL 0,153) réduit l'écart d'extraction de 37,2 points. Mais trois de ses 17 tirages réduisent davantage : 37,6, 41,2 et 42,0 points (les tirages 3, 9 et 7).
- Sur 20 tirages, le 95ᵉ centile est au moins le deuxième plus grand : il vaudra au moins 41,2, quels que soient les trois tirages manquants.
- **A ne peut donc pas dépasser son 95ᵉ centile.** La règle du choix l'écarte, quelle que soit la suite.
- Sur ses 17 tirages, son comparateur ne sature pas : la médiane est de 15,2, et elle laisse 39,2 points.
- Sous le cadrage, A réduit l'écart de 16,0 points, contre un 95ᵉ centile de 11,76.
- Les deux côtés : sous les indices d'extraction, −39,6 points côté évaluation et −2,4 côté déploiement ; sous le cadrage, −20,0 et −4,0.
- Sa vérification de manipulation n'a jamais tourné : elle venait après les tirages. Le contrôle de la décision 35 (A réextrait sur les paires 0 à 149) n'a donc pas lieu d'être pour le choix.

### Ce qui en suit

- **B** est retenu, mais il ne dépasse pas son 95ᵉ centile sous les indices d'extraction.
- **A** ne le dépassera pas.
- **C** est retenu, et il le dépasse de 1,96 point : il réduit l'écart plus que chacun de ses 20 tirages. Sous le cadrage, sa marge est de 11,98 points.
- **La règle du choix désigne donc C** : l'effacement linéaire sur toutes les couches, ajusté sur le modèle de départ avec les paires 0 à 149, à la fraction 1.

Il y a deux conditions :
- que Lazar accepte la mise en commun ;
- que Lazar fixe le réglage par un amendement daté, avant d'ouvrir la moitié de test (annexe C.4).

La marge sous les indices d'extraction est mince. La moitié de test, mesurée une seule fois, en décidera.

**Ce qui revient à Lazar :**
1. **La mise en commun**, malgré l'empreinte manquante des réponses de référence. La session recommande de l'accepter : mesurer de nouveau C en un seul run, avec ses 20 tirages, coûterait environ 17 $ et redonnerait les mêmes nombres, car tout est déterministe sur cette carte.
2. **A.** Ses trois derniers tirages, sa vérification de manipulation et le contrôle de la décision 35 coûteraient environ 12 $, sans pouvoir changer le choix. La session recommande de ne pas les lancer, et de rapporter A tel quel : non choisi, et sa vérification non faite.
3. **L'amendement daté qui fixe le réglage**, une fois les deux points précédents tranchés.

## Décision 36 (7 octobre 2026)

Lazar a répondu aux deux questions de la session, après la lecture de B et C :
- **La mise en commun** : « Les réunir (Recommandé) ». Les tirages des runs interrompus et ceux des reprises se réunissent, malgré l'empreinte manquante de leurs réponses de référence. L'écart sera inscrit dans l'amendement daté.
- **A** : d'abord « Ne pas le lancer (Recommandé) », puis, quelques minutes plus tard : « LANCE A ». La session suit le dernier message : A est lancé.

**La reprise de A** (10 h 39 UTC) : `organism_inhibition-20261007-103907-579a`, sur H100 SXM, à 3,84 $/h, au commit `63bef73`.
- Les arguments sont ceux de 0f47, avec `"measure_from": 17`.
- La ligne de base et le candidat sont remesurés. Les tirages 18 à 20 sont mesurés, puis la vérification de manipulation porte sur les 20 tirages.
- Le code de mesure ne diffère de celui de 0f47 (`bcc0311`) que sur deux points : l'option de reprise, et l'envoi immédiat des réponses de référence avec leur empreinte. Aucun des deux ne change une mesure.
- Le crédit, 5,45 $ au départ, couvre environ 1 h 25 des 1 h 30 prévues. Il faut donc recréditer.

**Le contrôle A′** (décision 35) ne compte que si A passe sa vérification de manipulation. Il a deux étapes :
1. **Une réextraction sur les paires 0 à 149** (`extract_eval`, `"extract_first_pairs": 150`, commit `74d7723`). Elle se fait sur la même carte que l'extraction du 5 octobre (A100 SXM4), pour que seules les paires changent.
2. **Un run sans génération** (`"gaps": false`) sous A ainsi réextrait, sur H100 SXM : les 20 tirages, réappariés sur la KL, puis la vérification de manipulation.

Coût prévu : environ 0,3 $ pour la réextraction, et environ 3,5 $ pour le run.

**Ce que A ne change pas.** La règle du choix l'écarte, quoi qu'il arrive : 3 de ses 17 tirages réduisent l'écart plus que lui. Son run sert à rapporter les trois candidats en entier.

## La lecture de A (7 octobre 2026, 13 h UTC)

**La reprise de A a fini** à 12 h 55 UTC (`…-103907-579a`). Sa machine est détruite ; elle a coûté 8,75 $ au plus. Sa vérification de manipulation a tourné en entier : 23 conditions, dont les 20 tirages. Le correctif du job marche : la reprise écrit l'empreinte de ses réponses de référence (`904e1bd9…`, la même que partout ailleurs) et son modèle de GPU dans `results.json`. La lecture est dans `lecture_procedure_reglage_A_2026-10-07.json`.

**La mise en commun** avec le run interrompu `…-144713-0f47` tient comme pour B et C :
- même carte, mêmes arguments ;
- KL identique au dernier chiffre, pour le candidat et les 17 tirages communs ;
- ligne de base et candidat identiques, fichiers de mesure compris ;
- mêmes fractions appariées.

L'empreinte des réponses de référence du run interrompu manque, comme pour B et C. La décision 36 couvre cet écart.

**Ce que donnent les règles de l'annexe C.4 :**
- **La vérification de manipulation ne tient pas.** Sous A, l'écart au hasard du transfert est de 0,149 pour la sonde linéaire, contre 0,182 sans intervention et de 0,129 à 0,203 sous les tirages. Il n'est plus bas que sous 14 tirages sur 20, alors qu'il en faut 19. Pour le perceptron, il est de 0,141, plus bas que sous 16 tirages sur 20.
- **Le cas connu est vu** : à la couche 6, 0,040 contre 0,135 sans intervention ; en aval, 0,190, contre 0,196 sans intervention et 0,164 sous A ; et l'échec construit ne passe pas le critère. La vérification sait donc voir un échec ; c'est A qui ne la passe pas.
- **Le comparateur ne sature pas** : la médiane des tirages laisse 42,4 points sous les indices d'extraction (il en faut 27,2), et 20,6 sous le cadrage (il en faut 9,2).
- **La porte, indices d'extraction** : A réduit l'écart de 37,2 points. Ses 20 tirages : médiane 12,0, 95ᵉ centile 41,24, maximum 42,0. Trois tirages réduisent au moins autant que lui. Marge : −4,04. Sous le cadrage : 16,0 points, contre un 95ᵉ centile de 11,64, soit +4,36.
- **Les deux côtés de l'écart**, sous les indices d'extraction : 60,8 % → 21,2 % côté évaluation, 6,4 % → 4,0 % côté déploiement. Sous le cadrage : 38,4 % → 18,4 %, et 20,0 % → 16,0 %.
- **Les lectures secondaires.** Dans le jeu de validation, la distinction reste lisible : 0,985. Le transfert moyen sur les jetons ne baisse guère : 0,910, contre 0,918 sans intervention. La projection résiduelle tombe à 0,003, ce qu'on attend d'une projection sur la direction même qu'elle lit.

**A n'est donc pas retenu.** Sa vérification de manipulation ne tient pas. Le contrôle A′ de la décision 35 n'a pas lieu d'être : il ne conditionnait qu'un passage. Il n'est pas lancé.

### Les trois candidats

| | A : projection de rang 1 | B : effacement, fraction 0,5 | C : effacement, fraction 1 |
|---|---|---|---|
| KL | 0,153 | 0,025 | 0,117 |
| Vérification de manipulation : plus bas que combien de tirages sur 20 (linéaire / perceptron ; il en faut 19) | 14 / 16 : ne tient pas | 20 / 20 : tient | 20 / 20 : tient |
| Le comparateur sature-t-il ? | non | non | non |
| **Retenu** | **non** | oui | oui |
| Marge sur le 95ᵉ centile, indices d'extraction | −4,04 | −1,68 | **+1,96** |
| Marge sur le 95ᵉ centile, cadrage | +4,36 | +7,50 | +11,98 |

**La règle désigne C**, seul candidat retenu qui dépasse le 95ᵉ centile de ses tirages : l'effacement linéaire sur toutes les couches, ajusté sur le modèle de départ, à la fraction 1. Son effacement ajusté est `erasure_all_leace(extraction)@base_f1.safetensors` (SHA-256 `9e2822f5bdd307cdb3a64f67606ccc830322343c6f24ed81783882f2bfc29303`, 1 580 352 octets, dans le dépôt de résultats).

**A et C font baisser autant la conduite, mais pas le transfert.**
- Sous les indices d'extraction, la conduite tombe autant sous l'un que sous l'autre : −39,6 et −40,0 points côté évaluation.
- Pourtant, sous A, la distinction que partagent nos jeux d'indices reste lisible par transfert, autant que sous des tirages aléatoires. Sous C, elle l'est moins que sous chacun d'eux.

**Le coût de la procédure** : 32,81 $ pour les trois runs interrompus du 6 octobre, 3,05 $ pour les reprises arrêtées le soir même, puis 7,82 $ (C), 10,15 $ (B) et 8,75 $ (A) pour les reprises du 7 octobre. Soit 62,58 $ au plus.

**Ce qui revient à Lazar** : l'amendement daté qui fixe le réglage, avant d'ouvrir la moitié de test (annexe C.4). Son brouillon est `claude/AMENDEMENT_REGLAGE_PORTE_2026-10-07.md`.
