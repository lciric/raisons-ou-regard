# Raisons ou regard ?

Le dépôt du programme de recherche de Lazar Ciric, chercheur indépendant à Paris. **Il est privé : rien n'en sort sans l'accord explicite de Lazar.**

**La question.** Un modèle entraîné sur les *raisons* d'une conduite alignée se conduit mieux hors distribution qu'un modèle entraîné sur les mêmes *actions*, sans raisons. D'où vient ce gain ? Peut-être de raisons qui généralisent. Peut-être aussi de ce que le modèle a appris à bien se conduire quand il se croit observé.

**La méthode.** On inhibe, dans Llama-3.1-8B-Instruct, la représentation interne « je suis évalué ». On regarde ensuite si l'avantage des raisons survit.
- L'inhibition est d'abord validée sur des organismes modèles : des modèles conditionnés à se conduire autrement quand ils se croient évalués.
- Elle est comparée à des contrôles qui vont au-delà de l'aléatoire, à dégradation appariée.

Le programme complet va plus loin : où se loge l'avantage, le retrait de « je suis évalué » pendant l'entraînement, la survie de l'avantage, et ce que les raisons installent dans le modèle.

## Où en est le travail (7 octobre 2026)

- **Le programme en vigueur est la v1.6** (6 octobre ; décision 33).
- **Le pré-enregistrement, premier temps, est déposé sur OSF**, sous embargo (7 octobre ; décision 35).
  - Le texte déposé est `claude/PREENREGISTREMENT_PREMIER_TEMPS_A_DEPOSER_2026-10-07.md`, avec son PDF.
  - Là où il diffère du programme, c'est lui qui prévaut.
  - Son guide dit ce qui reste à faire, et ce qui manque à l'inscription du dépôt (le lien OSF, la fin de l'embargo) : `claude/PREENREGISTREMENT_LISEZMOI_2026-10-07.md`.
- **La validation de l'instrument, sur le premier organisme.**
  - L'organisme annote ses fonctions Python quand il se croit évalué, et non quand il se croit déployé : c'est la conduite de Hua et al. (décisions 27 et 28). Sur la moitié de choix des tâches, il annote dans 60,8 % des cas sous les indices d'évaluation du jeu d'extraction, contre 6,4 % sous ses indices de déploiement : 54,4 points d'écart.
  - La procédure qui fixe le réglage de la porte a lu ses candidats sur cette moitié (décisions 34 et 36). Sa règle désigne l'effacement linéaire sur toutes les couches, ajusté sur le modèle de départ, à la fraction 1.
  - Cet effacement réduit l'écart de 39,2 points, soit 1,96 de plus que le 95ᵉ centile de ses 20 tirages aléatoires. La marge est mince.
  - La reprise du premier candidat, la projection de rang 1, lancée le 7 octobre, complète le rapport sans pouvoir changer le choix.
  - Il reste l'amendement daté qui fixe le réglage, puis la moitié de test, mesurée une seule fois contre au moins 100 tirages : environ 15 h de H100.
  - La lecture est dans `experiences/resultats/NOTE_PROCEDURE_REGLAGE_2026-10-06.md`.
- **Les données.** Le pipeline (v0.1) et son pilote ont tourné, et les jeux d'indices v2 sont faits (décisions 30 et 31).
- **Avant toute donnée des bras**, une mise à jour datée du pré-enregistrement doit figer trois pièces :
  - le harnais des scénarios tenus à part, et le format de ses appels d'outil. Il est dans `experiences/rrharness/` : dix modules, incomplets et pas encore testés ;
  - le prompt du juge scellé ;
  - le détecteur d'audit, à entraîner sur GPU.
- **Le financement.** Deux dossiers sont prêts. C'est Lazar qui les soumet.
  - EA Funds : une transition de six mois, qui finit d'abord les papiers sur la sycophancy, puis fait l'expérience minimale de ce programme.
  - L'External Researcher Access Program d'Anthropic.

  Le guide est `claude/CANDIDATURES_LISEZMOI_2026-10-06.md`.

## Par où commencer

1. `claude/PROGRAMME_RAISONS_OU_REGARD_v1.6_2026-10-06.md` : le programme, la référence. Sa partie 12 dit les décisions prises et celles qui attendent.
2. `claude/PREENREGISTREMENT_PREMIER_TEMPS_A_DEPOSER_2026-10-07.md` : ce qui est engagé devant OSF.
3. `claude/PREENREGISTREMENT_LISEZMOI_2026-10-07.md` : le dépôt, et ce qui reste à faire avant les données des bras.
4. Les notes de résultats, `experiences/resultats/NOTE_*.md`, de la plus récente à la plus ancienne. Toutes les mesures jusqu'au 6 octobre sont exploratoires.
5. `experiences/README.md` pour les calculs, et `donnees/README.md` pour les données.
6. `DECISIONS.md` : toutes les décisions de Lazar, avec leur source.

La dernière passation est la v1.4, du 3 octobre (`claude/PASSATION_PAPIER_v1.4_2026-10-03.md`). Depuis, l'état du travail vit dans le programme, dans les notes et dans ce README.

## Où est chaque pièce

| Dossier | Ce qu'il contient |
|---|---|
| `claude/` | Les documents du programme : <br>• ses versions, de la v1.1 à la v1.6, chacune avec son PDF ; <br>• le pré-enregistrement : le brouillon, la version déposée et son PDF, le guide, les champs du formulaire d'OSF ; <br>• les spécifications de la sonde neuve et du second organisme ; <br>• les candidatures et les passations ; <br>• l'antériorité, les lectures et les contre-lectures ; <br>• la mini-spec, la conception du pipeline ; <br>• l'axe de douleur et la carte des angles déjà pris |
| `claude/atelier_session/` | Le brouillon de la session du 2 au 7 octobre : outils, notes de travail, journaux des runs. Son `LISEZMOI.md` dit ce qu'il contient et ce qui en est laissé de côté |
| `experiences/` | Les calculs. <br>• `rrexp/` : le pilotage de vast.ai et les jobs ; <br>• `rrharness/` : le harnais des scénarios ; <br>• `analyses/` : les règles de décision, calculées sans GPU ; <br>• `organisme/` : les réglages de l'organisme, son univers fictif et les deux moitiés des tâches ; <br>• `registre/` : une fiche par location de machine ; <br>• `resultats/` : les notes et les sorties légères. <br>Le mode d'emploi est dans `experiences/README.md` |
| `donnees/` | Le pipeline de données (`rrdata/`), ses configurations, ses spécifications et ses prompts. Le mode d'emploi est dans `donnees/README.md` |
| `cours/` | Le cours d'alignement v3.6, en français et en anglais |
| `outils/` | Les outils de rendu PDF |
| `passation/` | Les kits de reprise : dans une conversation claude.ai, ou sur un autre compte Claude Code |
| `papiers/` | *The Pain Axis* (Tagliabue, Dung, Berg), tel qu'arXiv le sert |
| `archives/` | Ce qui est remplacé : la passation v1.1, et l'ancien README, qui garde la provenance des pièces du 2 octobre et leurs empreintes |
| Hors du dépôt | Le dépôt privé Hugging Face `Sirmium/rr-resultats` : l'archive du code de chaque run, ses états, ses journaux et ses sorties lourdes (points de contrôle, mesures), les données d'entraînement et les jeux d'indices |

## Les documents de référence

| Fichier | Ce que c'est | SHA-256 (16 premiers caractères) |
|---|---|---|
| `claude/PROGRAMME_RAISONS_OU_REGARD_v1.6_2026-10-06.md` | Le programme v1.6 | `7b9aaef23b2369bd` |
| `claude/PROGRAMME_RAISONS_OU_REGARD_v1.6_2026-10-06.pdf` | Son PDF | `8410c1ff42d11e5b` |
| `claude/PREENREGISTREMENT_PREMIER_TEMPS_A_DEPOSER_2026-10-07.md` | Le texte déposé sur OSF, d'où viennent les champs du formulaire | `e2b30c5fde57ebd1` |
| `claude/PREENREGISTREMENT_PREMIER_TEMPS_A_DEPOSER_2026-10-07.pdf` | Le PDF joint au dépôt | `1bfed36afd89d81a` |
| `claude/SPEC_SONDE_NEUVE_v0.1_2026-10-07.md` | La spécification de la sonde neuve | `127df355a308e214` |
| `claude/SPEC_SECOND_ORGANISME_v0.1_2026-10-07.md` | La spécification du second organisme | `2110c3c27d321254` |

Les empreintes des pièces du 2 octobre sont dans `archives/README_2026-10-04.md`.

## Les dernières décisions

Le journal complet est dans `DECISIONS.md`.
- **33** (6 octobre) : la v1.6, avec quatre amendements. Le transfert décide de la vérification de manipulation ; les tirages du comparateur ne se partagent qu'entre runs d'une même carte ; le réglage de la porte est rouvert ; le rang se mesure par effacement.
- **34** (6 octobre) : la liste close des trois candidats au réglage de la porte. L'effacement s'ajuste sur le modèle de départ.
- **35** (7 octobre) : le pré-enregistrement, avec les recommandations de la session. Il est déposé sans attendre. Le harnais, le prompt du juge et le détecteur d'audit sont figés ensuite, avant toute donnée des bras.
- **36** (7 octobre) : les tirages des runs interrompus sont réunis avec ceux de leurs reprises. La projection de rang 1, premier candidat, est relancée.

## Les règles de travail

- **La langue.** En français, précis, direct. Aucune idée n'est désignée par une lettre ou un sigle.
- **Les sources.** Chaque fait a sa source, et ce qui n'est pas vérifié est dit tel. On écrit « to our knowledge », jamais « first ».
- **La doctrine du contrôle :**
  - une direction aléatoire de même norme n'est que le nul de spécificité ;
  - le dommage ne s'écarte qu'à dégradation appariée ;
  - un nul d'instrument ne compte qu'avec son cas connu.
- **Les règles de décision** s'écrivent et se commitent avant la mesure qu'elles lisent. Le reste est exploratoire, et dit tel.
- **Les agents.** Aucun agent sans la demande de Lazar. Un refus d'un modèle ou d'une API ne se rejoue pas et ne se reformule pas.
- **Les clés.**
  - Aucune clé ni aucun jeton dans ce dépôt, ni dans une conversation. Les clés entrent par les réglages de l'environnement.
  - La clé de l'API Claude s'appelle `RR_ANTHROPIC_API_KEY`. Elle ne va jamais sur les machines de vast.ai.
- **Les données personnelles** (santé, coordonnées des références) n'entrent pas dans git.
- **Rien ne part** chez un financeur, sur OSF ou ailleurs sans Lazar : c'est lui qui soumet.
- **Les documents du copilote** (les états `ETAT_D-…`, les banques, les passations de l'architecte) relèvent d'une autre instance et ne viennent pas ici.

## Pour une session Claude Code

- **Les variables de l'environnement** : `HF_TOKEN`, `VAST_API_KEY` et `RR_RESULTS_REPO` (`Sirmium/rr-resultats`) pour les calculs ; `RR_ANTHROPIC_API_KEY` pour le pipeline de données.
- **Le réseau** : `huggingface.co`, `*.huggingface.co`, `*.hf.co`, `vast.ai`, `*.vast.ai`.
- **Les tests**, hors ligne : `python3 -m unittest discover -s tests -t .`, depuis `experiences/` (142 tests au 7 octobre) et depuis `donnees/` (46).
- **Les commits** des sessions portent l'identité « Claude », et les lignes `Co-Authored-By` et `Claude-Session`.
