# Raisons ou regard ?

Dépôt privé du programme de recherche « Raisons ou regard ? » : l'entraînement de sûreté par raisons, et la part qu'y prend la conscience d'être évalué. Il remplace le Projet claude.ai de l'ancien compte (« agent ai bras droit conversationel »), que le nouveau compte ne peut pas lire.

Il reste privé : rien n'en sort sans l'accord explicite de Lazar.

## Où est chaque pièce

- `claude/` : les documents du programme, sous le nom qu'ils avaient dans le Projet. Un renvoi `claude/NOM.md` d'une passation mène au fichier `claude/NOM.md` de ce dépôt.
- `papiers/` : les papiers lus pour le programme.
- `passation/` : les pièces de la passation au nouveau compte, et le kit de reprise dans une conversation claude.ai :
  - `COMMENT_REPRENDRE_SUR_CLAUDE_AI.md`, le mode d'emploi pour Lazar ;
  - `PROMPT_LANCEMENT_PAPIER_CLAUDE_AI_MODELE.txt`, le prompt de lancement, dont la session remplit les noms et les empreintes des zips ;
  - `faire_paquet_reprise_session_2026-10-02.sh`, le script qui fabrique le paquet de reprise et le zip scellé.
- `archives/` : la passation v1.1, remplacée par la v1.2. Ne pas la lire : la v1.2 en reprend tout le contenu.
- `donnees/` : le code du pipeline de données (v0.1).
- `cours/` : le cours d'alignement v3.6, en français et en anglais.
- `outils/` : les outils de rendu PDF (`outils/LISEZMOI.md`).
- `experiences/` : le pilotage des calculs sur vast.ai, par l'API, et les jobs (l'essai de bout en bout, le SFT par LoRA des bras) ; mode d'emploi dans `experiences/README.md`. Le registre des locations est dans `experiences/registre/`.

**Pour reprendre le programme, lire d'abord `claude/PASSATION_PAPIER_v1.4_2026-10-03.md`**, la passation de la session Claude Code du 3 octobre, puis la v1.3 (session du 2 octobre), puis la v1.2.

| Fichier | Ce que c'est | sha256 (16 premiers caractères) |
|---|---|---|
| `claude/PASSATION_PAPIER_v1.2_2026-10-02.md` | La passation relais, le document principal (2 octobre, 8 h 40) | `e5bd33bf90f80110` |
| `claude/PASSATION_PAPIER_v1.0_2026-10-01.md` | La passation du 1er octobre, toujours valable | `ff5af949fdf4d4f1` |
| `claude/PASSATION_PAPIER_COMPLEMENT_ARCHITECTE_2026-10-02.md` | La partie ouverte du complément de l'architecte | `b40904b53395b5c6` |
| `claude/PROGRAMME_RAISONS_OU_REGARD_2026-10-01.md` | Le programme v1.1 (le nom ne porte pas le numéro) | `efbe7be46407b820` |
| `claude/PROGRAMME_RAISONS_OU_REGARD_v1.1_2026-10-01.pdf` | Son PDF (28 pages) | `b00f6c1fcfec7eb4` |
| `claude/ANTERIORITE_RAPPORTS_2026-10-01.md` | Les 4 rapports bruts d'antériorité du 1er octobre | `2963f85ce948e432` |
| `claude/ANTERIORITE_RAPPORTS_2026-10-02.md` | Les 7 rapports bruts de la nuit du 1er au 2 octobre | `c25c27784ce858f2` |
| `claude/ANTERIORITE_CONSIGNES_AGENTS_2026-10-02.md` | Les consignes complètes des sept agents de la nuit | `e4a61be719cd9021` |
| `claude/LECTURES_PRIORITAIRES_2026-10-01.md` | La liste des lectures prioritaires | `b3b699c90964dc14` |
| `claude/LECTURES_PRIORITAIRES_FICHES_2026-10-01.md` | Les fiches de lecture ; leur partie C est la genèse de l'idée | `d772b7cada11ea61` |
| `claude/LECTURES_PRIORITAIRES_FICHES_2026-10-01.pdf` | Leur PDF | `7a4185d6025b3e67` |
| `claude/CONTRE-LECTURE_FICHES_2026-10-01.md` | La contre-lecture des fiches | `577871caf55bb1e3` |
| `papiers/arXiv_2609.16247v2_The_Pain_Axis.pdf` | *The Pain Axis: LLMs Represent Self-Directed Harm and Act on It* (Tagliabue, Dung, Berg), tel qu'arXiv le sert | `fa4b2bb4b9b6a2bf` |
| `passation/LISEZMOI_PAQUET_PASSATION_PROGRAMME_2026-10-02.md` | Le LISEZMOI du paquet de passation (9 h 15) | `43e50a30a5d401b8` |
| `passation/MANIFEST_SHA256_PAQUET_PASSATION_PROGRAMME_2026-10-02.txt` | Son manifeste : les 20 empreintes du paquet, pièces scellées comprises | `fba321d86b31d906` |
| `passation/00_LISEZ-MOI_NOUVEAU_COMPTE.md` | Le LISEZ-MOI du zip `RAISONS_OU_REGARD_PASSATION_2026-10-02.zip` (9 h 15) | `af977ada868aad7e` |
| `passation/PROMPT_LANCEMENT_PAPIER_2026-10-02.txt` | Le prompt de lancement de l'instance du papier | `0a5456f3025359ac` |
| `archives/PASSATION_PAPIER_v1.1_2026-10-02.md` | La passation v1.1, remplacée | `0593652589f13663` |

**D'où viennent ces copies.** Ce sont des copies à l'octet de trois sources :
- le paquet `PACK_PASSATION_PROGRAMME_RAISONS_OU_REGARD_2026-10-02.zip` (sha256 `9ce3082751b2a860…`), vérifié fichier par fichier contre son manifeste : 20 sur 20 ;
- le zip `RAISONS_OU_REGARD_PASSATION_2026-10-02.zip` (sha256 `84db927bd66f9bfa…`), vérifié contre son `SHA256SUMS.txt` : 11 sur 11 ; il fournit le PDF d'arXiv et son LISEZ-MOI ;
- le prompt de lancement, joint à part.

**Deux pièces du paquet ne sont pas reprises.**
- L'exemplaire du papier dit « annoté » (`60a2abfdafd4285c…`). Il a le même texte que celui d'arXiv, et ses pages se rendent à l'identique. Il ne porte aucune note lisible : ses seules annotations sont des liens.
- La copie du complément ouvert que porte le zip `RAISONS_OU_REGARD_PASSATION` (`81591a66d2743789…`) est une version antérieure, qui renvoie encore à la passation v1.1. C'est celle du paquet (`b40904b53395b5c6…`) qui fait foi.

## Les pièces autrefois scellées

Scellées jusqu'à la fin de la phase 1 de la tâche « axe de douleur » (passation v1.2, §6 et annexe B), elles sont entrées dans `claude/` au feu vert de Lazar, le 2 octobre au soir. Leurs empreintes correspondent au manifeste du paquet.

| Pièce | sha256 (manifeste du paquet, 16 premiers caractères) |
|---|---|
| `claude/PROGRAMME_RAISONS_OU_REGARD_v1.2_2026-10-02.md` | `fca1f6e9a989d584` |
| `claude/PROGRAMME_RAISONS_OU_REGARD_v1.2_2026-10-02.pdf` | `332fb1c396684c95` |
| `claude/PROGRAMME_RAISONS_OU_REGARD_v1.3_2026-10-02.md`, la version de référence jusqu'à la v1.4 | `a5ef0e51efdb4ba6` |
| `claude/PROGRAMME_RAISONS_OU_REGARD_v1.3_2026-10-02.pdf` | `72ad347d469954e5` |
| `claude/PASSATION_PAPIER_COMPLEMENT_ARCHITECTE_SCELLE_AXE_DOULEUR_2026-10-02.md` | `06b425f7820ca3d3` |

## Les documents écrits par la session du 2 octobre

| Fichier | Ce que c'est | sha256 (16 premiers caractères) |
|---|---|---|
| `claude/PROGRAMME_RAISONS_OU_REGARD_v1.4_2026-10-02.md` | **Le programme v1.4**, en clair : la v1.3, plus les suites de la comparaison de l'axe, l'antériorité refaite avec la carte des angles, la mini-spec v0.2 et le pipeline v0.1 | `b1d55773a052fb6b` |
| `claude/PROGRAMME_RAISONS_OU_REGARD_v1.4_2026-10-02.pdf` | Son PDF (85 pages) | `228cfa921dbd66a6` |
| `claude/CONSIGNE_CONTRE_LECTURE_VIERGE_2026-10-02.md` | La consigne de la contre-lecture vierge de la v1.4, et son PDF | voir le git |
| `claude/AXE_DOULEUR_COMPARAISON_2026-10-02.md` | La comparaison de l'axe de douleur (phase 2) | `c6099e2763e46b97` |
| `claude/AXE_DOULEUR_PISTES_INDEPENDANTES_2026-10-02.md` | Les pistes indépendantes de l'axe (phase 1), gelées | `b6055d88c69303bd` |
| `claude/CARTE_ANGLES_DEJA_PRIS_2026-10-02.md` | La carte des angles déjà pris | `7744a85cf528d6ff` |
| `claude/MINI_SPEC_ET_FAMILLES_v0.2_2026-10-02.md` | La mini-spec v0.2 | `f5546818693c6d89` |
| `claude/PIPELINE_DONNEES_v0.1_2026-10-02.md` | La conception du pipeline de données v0.1 (le code est dans `donnees/`) | `6d9350135beb9973` |
| `claude/PASSATION_PAPIER_v1.3_2026-10-02.md` | La passation de la session | voir le git |
| `claude/PASSATION_PAPIER_v1.4_2026-10-03.md` | La passation de la session du 3 octobre : décisions 20 à 23, les expériences, ce qui est en suspens | voir le git |

**Les PDF de ces documents ont été régénérés le 2 octobre au soir.** Le premier outil de rendu aplatissait les listes imbriquées, et les listes qui suivent un paragraphe ; les md n'ont pas changé. Les outils de rendu sont dans `outils/`.

**Ne viendront pas ici** : les documents du copilote (les états `ETAT_D-…`, les banques, les passations de l'architecte). Ils relèvent d'une autre instance.

## Les décisions de Lazar

| Sujet | Décision | Source |
|---|---|---|
| La version de référence du programme | La v1.3 ; la v1.4 lui succède, écrite le 2 octobre au soir à la demande de Lazar, sous réserve de sa relecture | Passation v1.2, §3, point 9 (2 octobre, 8 h 32) ; passation v1.3, §2, décisions 18 et 19 |
| Le calcul | vast.ai, sans limite de budget. Un H100 SXM quand il y en a, sinon un A100 80 Go, et plusieurs GPU à la fois | Passation v1.2, §3, point 1 ; le choix des GPU, confirmé le 2 octobre |
| Les règles pour vast.ai | Aucune clé d'API Claude sur ces machines : les appels partent de la machine de Lazar. Un jeton Hugging Face à accès restreint pour télécharger Llama, révoqué ensuite. Les données et les points de contrôle synchronisés vers un stockage à lui | Proposées dans la passation v1.2, §3, point 1 ; confirmées le 2 octobre |
| L'API Claude | Sans plafond | Passation v1.2, §3, point 2 |
| Le périmètre du pré-enregistrement | Des phases du test des raisons à l'anatomie, plus la phase de validation de l'instrument | Passation v1.2, §3, point 3 ; la validation, ajoutée le 2 octobre |
| La contre-lecture du programme | Une instance vierge, qui reçoit le seul programme et une consigne de contre-lecture ; sur la v1.4, dès qu'elle existe. La consigne est écrite | Passation v1.2, §3, point 6 ; passation v1.3, §2, décision 19 |
| Le projet SPAR de Qiyao Wei | « on va tâcher d'y répondre nous-mêmes dans ce programme avant SPAR » | Passation v1.2, §3, point 4 |
| La cible | « plutôt conf principale ou revue ; prestigieux et ambitieux » | Passation v1.2, §3, point 5 |
| Les agents | Seulement à sa demande. Le 2 octobre, il a demandé des agents vierges pour la phase 1 de l'axe de douleur, puis de « tout finir ici » (toute la chaîne, dans la session Claude Code) | Passation v1.2, §1 ; 2 octobre |
| Le périmètre de la session du nouveau compte | Le papier seul ; le copilote va dans une autre session | 2 octobre |
| Les clés et le pilotage des calculs | Lazar pilote depuis une session Claude Code. Il ajoute `HF_TOKEN` et `VAST_API_KEY` en variables d'environnement de l'environnement Claude Code, et il ouvre huggingface.co et vast.ai dans « Network access ». Une conversation claude.ai ne voit pas ces variables | 2 octobre |
| Le dépôt du programme | Ce dépôt, privé, créé par Lazar | 2 octobre |
| Le nom du pré-enregistrement | Son nom seul, avec son ORCID ; Claude n'est pas auteur, une phrase de méthode dit que le protocole a été rédigé avec son aide | 2 octobre |
| Les contacts avec Cadile et Lundqvist | « non pas encore » ; aucun moment fixé | 2 octobre |
| Le lieu du pré-enregistrement | OSF Registries, sous embargo jusqu'au post ; en deux temps (le texte en semaine 1, l'amendement gelé après le pilote) | Passation v1.2, §3, point 3 ; confirmé le 2 octobre |
| La mini-spec v0.1 | Adoptée : les dix principes et la matrice, le cadrage neutre, la balise vide, le texte neutre reformulé, le filtre de la conscience d'évaluation, la demande nuisible sans contenu dangereux ; seuils provisoires | 2 octobre |
| Le raisonnement d'une autre situation dans l'expérience minimale | Oui, aux deux étapes ; critère principal inchangé (actions seules contre raisons) ; porte des raisons appliquée telle que la v1.1 l'écrit | 2 octobre |
| Les suites de la comparaison de l'axe | Blocs A et B adoptés ; aucun adaptateur des auteurs ; injection de l'axe après le post seulement ; premier ou second papier, décidé après le test du regard | 2 octobre |
| La version 1.4 du programme | À écrire par la session, en clair ; puis contre-lecture vierge de la 1.4. Écrite le soir même | 2 octobre |
| Les neuf choix du pipeline de données | Adoptés tels que proposés (§4 de `claude/PIPELINE_DONNEES_v0.1_2026-10-02.md`) | 3 octobre (décision 20) |
| Le juge scellé des évaluations | Choisi sur le jeu de calibration, par une règle écrite dans le premier temps du pré-enregistrement : Opus 5.5 et un modèle ouvert à température 0 passent le jeu de calibration et le test de persuasion ; le meilleur est scellé dans l'amendement, avant toute donnée du test du regard ; à une marge fixée d'avance près, le modèle ouvert ; l'autre devient juge secondaire | 3 octobre (décision 21) |
| La contre-lecture vierge de la v1.4 | Par un agent vierge, lancé par la session le 3 octobre au matin : il ne reçoit que le PDF de la v1.4 et son texte extrait page par page, dans un dossier propre, et la consigne telle quelle | 3 octobre (décision 22) |
| Démarrer les expériences | « on peut démarrer les expériences stp ? ça traîne » : le code des calculs passe avant les scénarios tenus à part. Les clés entrent par la fenêtre de l'environnement, jamais par une conversation ni par un canal entre sessions | 3 octobre (décision 23) |

**Ouvert** : la partie 12 de la v1.4 liste tout ce qui attend Lazar ; les neuf choix du pipeline et le juge scellé sont tranchés depuis (décisions 20 et 21). Restent d'abord : les propositions des §5.1, §5.2 et §5.5 (points 3 à 9) de la passation v1.2 ; le plafond écrit des lectures de l'axe ; le modèle ouvert candidat au juge scellé ; le stockage des résultats (proposé : le dépôt privé `lciric/rr-resultats` sur Hugging Face, puisque la session n'a pas de SSH vers les machines).

## Où en est le travail (2 octobre 2026)

1. Les pièces sont vérifiées (voir plus haut).
2. **La tâche « axe de douleur ».**
   - La phase 1 est finie. Elle a été confiée à des agents vierges, à la demande de Lazar. La raison : la partie scellée du complément était jointe au premier message de la session, et l'instance qui tient le papier l'a donc lue.
   - Le livrable : `claude/AXE_DOULEUR_PISTES_INDEPENDANTES_2026-10-02.md`, gelé, sha256 `b6055d88c69303bd99f4025710c271e8d94ce1700c35705e27bedb328fcd9e6d`. Les consignes des agents sont livrées à part, avec leur empreinte (`claude/AXE_DOULEUR_PHASE1_CONSIGNES_AGENTS_2026-10-02.js`, et leur note `…_LISEZMOI_…`).
   - La phase 2 est faite, au feu vert de Lazar. La comparaison : `claude/AXE_DOULEUR_COMPARAISON_2026-10-02.md`, sha256 `c6099e2763e46b97a443b5e5a246cace30d86298dac3bb39b2d67a03a1cc9a30`. Son §7 proposait ce qui devait entrer dans la version 1.4 ; Lazar a dit « oui à tout », et la v1.4 l'intègre.
   - Les pièces scellées sont maintenant dans `claude/` : les versions 1.2 et 1.3 du programme, et la partie scellée du complément.
3. **La carte des angles déjà pris** (passation v1.2, §6, point 3) : écrite par des agents et vérifiée en trois tours de critique (`claude/CARTE_ANGLES_DEJA_PRIS_2026-10-02.md`, sha256 `7744a85cf528d6ff3f75ead74a39447fea97793944e43ab5e608f6371ed764d6`). Ses conséquences sont intégrées à la partie 1 de la v1.4.
4. **Le programme v1.4**, en clair (`claude/PROGRAMME_RAISONS_OU_REGARD_v1.4_2026-10-02.md`, sha256 `b1d55773a052fb6b30867baa60e0c81df5bc12c0fde452731c90e519e85bfc27`), et la consigne de sa contre-lecture vierge (`claude/CONSIGNE_CONTRE_LECTURE_VIERGE_2026-10-02.md`), à lancer à la demande de Lazar.
5. **Les étapes 3 à 6 de la passation v1.0** (§5) :
   - la mini-spec et les dix familles : v0.1 adoptée le 2 octobre, puis la v0.2 (`claude/MINI_SPEC_ET_FAMILLES_v0.2_2026-10-02.md`) ;
   - le pipeline de données : v0.1 écrite et testée hors ligne (`donnees/`, conception dans `claude/PIPELINE_DONNEES_v0.1_2026-10-02.md`) ; le pilote attend `RR_ANTHROPIC_API_KEY`, `HF_TOKEN` et l'accès à huggingface.co ;
   - l'organisme de validation, reconstruit depuis les documents publics de Hua et al. ;
   - le pré-enregistrement, sur OSF, en deux temps.

## Les règles de travail

Celles de la passation v1.2 (§1) et du prompt de lancement. En particulier :
- En français, précis, direct. Aucune idée désignée par une lettre ou un sigle.
- Chaque fait a sa source, et ce qui n'est pas vérifié est dit tel. « to our knowledge », jamais « first ».
- La doctrine du contrôle :
  - une direction aléatoire de même norme n'est que le nul de spécificité ;
  - le dommage ne s'écarte qu'à dégradation appariée ;
  - un nul d'instrument ne compte qu'avec son cas connu.
- Aucun agent sans la demande de Lazar. Un refus d'un modèle ou d'une API ne se rejoue pas et ne se reformule pas.
- Aucune clé ni aucun jeton dans ce dépôt, ni dans une conversation.

## L'environnement des sessions cloud

Au 2 octobre, la politique réseau de l'environnement refuse arxiv.org, huggingface.co, lesswrong.com, alignmentforum.org, openreview.net, semanticscholar.org, openalex.org, alignment.anthropic.com et transformer-circuits.pub. Le moteur de recherche et GitHub répondent. Ouvrir ces domaines dans les réglages de l'environnement deviendra nécessaire :
- pour les relectures sur source de la carte des angles ;
- pour tout téléchargement de modèle.
