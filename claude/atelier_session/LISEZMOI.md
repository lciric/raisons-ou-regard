# L'atelier de la session (2 au 7 octobre 2026)

Lazar a demandé, le 7 octobre : « deose tout ce que tu as fait sur github ».

Tout ce que la session a commité était déjà sur GitHub. Ce dossier ajoute ce qui ne vivait que dans son brouillon : les outils, les notes de travail, les journaux des runs et quelques livrables. Le brouillon disparaît avec le conteneur de la session. Les documents finaux, eux, sont ailleurs dans le dépôt (`claude/`, `cours/`, `experiences/`, `donnees/`).

**Comment il a été fait.**
- Chaque fichier du brouillon a été comparé, par son empreinte, à tous les fichiers de l'historique git. Ceux qui y étaient déjà, à l'identique, ne sont pas repris.
- Sur les 541 qui restaient, 288 sont déposés ici, et 253 sont laissés de côté, chacun pour une raison dite plus bas.
- Avant le dépôt, les fichiers ont été passés au crible : aucune clé ni aucun jeton, et pas de données personnelles (une exception, traitée plus bas).

**Une limite.** Les scripts gardent les chemins du brouillon de la session (`/tmp/claude-0/…`). Ils disent ce qui a tourné, mais ne tournent pas tels quels ailleurs.

## Ce qu'il y a

| Dossier | Ce que c'est | Ce que ça a produit |
|---|---|---|
| `pilotage_gpu/` | Les scripts qui ont loué, suivi et détruit les machines des 5 au 7 octobre : les lancements groupés, l'attente d'une offre et du crédit, le suivi du crédit, la lecture des offres. Aussi les sondes de l'API et de vast.ai, et la base lexicale des indices v2 (`lex_v2*.py`). | Les runs des décisions 33 à 36, dont les fiches sont dans `experiences/registre/` |
| `pilotage_gpu/journaux/` | Les journaux de ces scripts : chaque lancement, chaque passage du suivi, le crédit toutes les 5 minutes, les erreurs des lancements. `resume_2026-10-07.log` couvre les reprises de B et C, puis celle de A. | La chronologie des notes de `experiences/resultats/` |
| `programme_v1.4/` | Les morceaux de la v1.4 du programme, partie par partie, et son brouillon d'ensemble | `claude/PROGRAMME_RAISONS_OU_REGARD_v1.4_2026-10-02.md` |
| `programme_v1.6/` | L'outil qui a appliqué les éditions à la v1.5 (`apply.py`, `merges.py`), les éditions elles-mêmes (`ed_*.json`), le texte obtenu et les contrôles du rendu (`chk/`). `travail/` garde les différences relues et le résumé de l'intégration. | `claude/PROGRAMME_RAISONS_OU_REGARD_v1.6_2026-10-06.md` et son PDF |
| `preenregistrement_osf/` | Le découpage du texte en champs du formulaire (`make_sheet.py`, `blocks.json`), et la fabrication du PDF (`make_pdf.py`, `print.js`) | `claude/OSF_CHAMPS_A_COLLER_2026-10-07.md` et le PDF déposé sur OSF (SHA-256 `1bfed36a…`) |
| `candidatures/` | Les scripts qui ont rempli et vérifié les budgets, ceux qui ont lu le formulaire d'EA Funds, et la demande fusionnée d'EA Funds, **en copie expurgée** | Les budgets `claude/CANDIDATURE_*_BUDGET_*.xlsx` |
| `phase1_aveugle/` | Les notes de la phase aveugle du 2 octobre : pistes par lecteur, vérifications, tours de corrections, fiche du papier, et la version « hors table » des pistes | `claude/AXE_DOULEUR_PISTES_INDEPENDANTES_2026-10-02.md` |
| `phase2/`, `passation_2026-10-02/` | Les empreintes du scellé de la phase 2, et le paquet de passation du 2 octobre avec son scellé | — |
| `carte_angles/` | La carte des angles déjà pris : un fichier par angle, sa vérification, les tours de corrections, la veille, le calendrier des projets voisins, et l'outil du PDF | `claude/CARTE_ANGLES_DEJA_PRIS_2026-10-02.md` et son PDF |
| `cours_v3.6/` | Le passage du cours d'alignement de la v3.5 à la v3.6 : l'outil d'application, les générateurs par volet, les insertions, les vérifications par groupe, les rapports, et le référentiel des instruments (`referentiel_instruments/`) | `cours/COURS_Alignment_v3.6_*` |
| `livrables/` | Des PDF envoyés à Lazar et absents du dépôt : l'extrait « principes et matrice » de la mini-spec v0.1, et les PDF du rapport de contre-lecture vierge de la v1.4 | — |
| `messages/` | Le message à l'autre instance du 4 octobre | — |

## La demande d'EA Funds : une copie expurgée

La demande fusionnée du 7 octobre contient deux données personnelles : l'accident, dans le champ confidentiel, et les e-mails des deux références. La règle du dépôt est qu'aucune donnée personnelle n'entre dans git.

La copie déposée (`candidatures/EA_FUNDS_APPLICATION_MERGED_2026-10-07_EXPURGEE.md`) retire donc trois choses :
- le champ confidentiel ;
- la section des références ;
- deux lignes des notes qui en parlaient.

Le reste est identique. La version complète a été envoyée à Lazar directement, hors de git.

## Ce qui est laissé de côté, et pourquoi

| Nombre | Raison | Exemples |
|---|---|---|
| 164 | Téléchargé : les sources web de la phase aveugle (README et fichiers des dépôts d'autres auteurs, vecteurs, CSV), et le texte du papier de l'axe de douleur | `phase1_aveugle/travail/*_sources/`, `fiche_papier_depot/` |
| 18 | Téléchargé : des pages de la documentation d'Anthropic, et un paquet Python | `ref/*.html`, `ref/pkg/` |
| 15 | Téléchargé : le dépôt d'un tiers, relu pour la carte des angles, et ses figures | `verif_juge/` |
| 5 | Téléchargé : le modèle de budget et le texte du formulaire d'EA Funds ; le papier de l'axe de douleur, annoté | `dl_template/`, `form/*.txt`, `papier/` |
| 4 | Téléchargé : des README de dépôts tiers | `phase2/*README*.md` |
| 3 | À Lazar : son cours v3.5, et le README de son autre dépôt | `cours_v36/source/` |
| 11 | Copies intermédiaires entières du cours (environ 1 Mo chacune). La v3.6 finale est déjà dans le dépôt. | `simu_*.md`, `v10check/`, `_finale/sauvegarde_avant_corrections/` |
| 15 | Un essai de l'outil du cours, remplacé par `cours_v3.6/` | `testapp.ayLZ/` |
| 13 | Des rendus, qui se refont depuis leurs sources : aperçus PNG, HTML intermédiaires, PDF d'essai, et un rendu antérieur de la carte des angles (sa version finale est dans `claude/`) | `apercu_v16-*.png`, `chk/*.html` |
| 5 | Des marqueurs vides du brouillon | `v2_start`, `poll_launch.pid` |

**Quatre fichiers de travail sont peut-être restés à tort dans les dossiers de sources de la phase aveugle :**
- `corrections_tour_2_sources/diff_phrases.txt` ;
- `corrections_tour_2_sources/livrable_avant_tour2.md` ;
- `corrections_tour_3_sources/livrable_avant_tour3.md` ;
- `pistes_sceptique_sources/sceptique_positions.csv`.

Ils sont restés hors du dépôt avec ces dossiers. Les deux `livrable_avant_tour*` sont, d'après leur nom, des états du livrable avant ses tours de corrections.
