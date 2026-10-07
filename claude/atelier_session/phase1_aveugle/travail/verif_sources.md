# Vérification indépendante des sources : pistes fusionnées, web_papier, web_voisins (phase 1, à l'aveugle)

2 octobre 2026. Objet : chaque affirmation de `pistes_fusionnees.md`, `web_papier.md` et `web_voisins.md` qui porte sur un autre travail que le papier, sur ses versions, sur son code ou sur l'antériorité. Pour chacune : **confirmée** (et comment), **partielle**, **non vérifiable ici**, ou **fausse**. Le papier (*The Pain Axis: LLMs Represent Self-Directed Harm and Act on It*, arXiv 2609.16247v2) n'est relu que là où une affirmation sur un autre travail en dépend. Je n'ai pas lu `verif_faits.md`, pour rester indépendant.

---

## 0 · Méthode

**Ce que j'ai refait moi-même, sans reprendre les copies des agents.**
- **GitHub par curl sur `raw.githubusercontent.com`** : 57 fichiers téléchargés à nouveau, rangés dans `travail/verif_sources_sources/` (`valen/` pour le dépôt des auteurs, `autres/` pour le reste). Liste en annexe.
- **Empreintes** : mes téléchargements sont identiques octet pour octet aux copies des agents pour tous les fichiers comparés (README principal des auteurs, `MANUSCRIPT_DISCREPANCIES.md`, `positions.csv`, le jeu de phrases, les métadonnées Llama, le script 01, la synthèse « wolframs », le README de l'axe de démangeaison). Les agents n'ont donc pas travaillé sur des copies altérées.
- **Recalculs sans torch ni numpy** : décodage des deux fichiers `pain_vectors.pt` (Llama 3.1 8B Instruct, « Qwen_3_8B_base ») par un désérialiseur minimal ; lecture de `pooled.csv` et `positions.csv` par script.
- **Le rapport d'Allchin et al.** : PDF retéléchargé (19 pages, créé le 28 septembre 2026), texte extrait par `pdftotext`, lu en entier.
- **WebSearch : 15 appels, le plafond.** Tout ce qui n'est vu que par extrait est marqué « vu par extrait de recherche, non ouvert » et ne fournit aucun chiffre. Requêtes en annexe, numérotées R1 à R15.
- **Non ouvert, par la politique réseau** : arXiv, Hugging Face, LessWrong, l'Alignment Forum, les blogs des laboratoires. Aucun contournement.
- **Un écart de procédure, signalé** : un téléchargement d'essai (README d'*Open Character Training*) a d'abord été écrit dans un fichier temporaire hors des deux dossiers, puis copié dans `verif_sources_sources/autres/` et effacé. Aucun fichier préexistant hors de `pieces/` et `travail/` n'a été lu.

**Ce que « confirmé » veut dire ici.** Le fait figure tel quel dans la source, lue par moi. Quand la source est elle-même une relecture tierce (revue « wolframs », réanalyse « clauderfly », rapport d'Allchin), « confirmé » veut dire : la source dit bien cela. Ce n'est pas une vérification sur les données, sauf mention.

---

## 1 · Les versions du papier (web_papier §1, pistes_fusionnees §6.1)

| Affirmation | Statut | Comment |
|---|---|---|
| Titre de la v1 : « … and Act to Relieve It » | **Confirmée** | README des auteurs au commit `8d1649c…` (titre et BibTeX) ; `CITATION.cff` et README d'Allchin et al. ; README et `BRIEF.md` de « wolframs ». Tous lus par curl. |
| Le README au commit `7c25650…` porte déjà le titre de la v2 | **Confirmée** | `diff` des deux README : seules changent les deux lignes du titre. Le README actuel ajoute en plus le lien vers `v2_controls/`. |
| Le titre de la v1 se lit aussi dans le README de « clauderfly-ui » | **Fausse** | Ce README cite « arXiv:2609.16247 » sans titre. Il ne porte sur la v1 que par le commit analysé, `8d1649c…`. |
| v1 datée du 12 septembre 2026 | **Confirmée** | Papier, p. 30 : « v1, September 12, 2026 ». |
| v1 soumise le 14 septembre, 30 pages | **Confirmée** (par une source tierce) | `BRIEF.md` de « wolframs » : « submitted 2026-09-14 » ; « Paper PDF (30 pages ». Page arXiv non ouverte. |
| v1 : « nearly orthogonal » à la valence négative | **Confirmée** comme attribution d'Allchin et al. | Rapport, §6.4 : les auteurs décriraient les vecteurs de douleur comme « nearly orthogonal to the main negative-valence cluster ». L'expression ne figure plus dans la v2 (recherche dans le texte page par page). Texte de la v1 non ouvert. |
| Numérotation des annexes de la v1 : B pour les SAE, C pour l'ablation | **Partielle** | Le README de `8d1649c…` nomme `appB_sae/` et `appC_ablation/` ; « wolframs » parle de « Appendix C » pour l'ablation. C'est une inférence cohérente, pas une lecture de la v1. |

---

## 2 · Le code et les données du dépôt des auteurs (web_papier §2, pistes_fusionnees §0.3, §0.4, §6.2)

Dépôt `valen-research/Pain-axis`, branche `main`, lu par curl.

**Confirmé, tel que les fichiers l'écrivent**
- **Licence.** `LICENSE` : licence MIT, « Copyright (c) 2026 valen-research » ; README : « MIT ». `ASSETS.md` : « No adapter/data redistribution license is inferred from the MIT code license ».
- **`requirements.txt`.** Quatorze paquets sans version, dont `torch`, `transformers`, `transformer_lens`, `peft`, `anthropic` : le compte de web_papier (cinq nommés « et neuf autres ») est juste.
- **Exécution.** Le README dit bien que les scripts vident tout le cache Hugging Face, qu'ils sont écrits pour RunPod et prévus pour un carnet de notes. Il demande `ANTHROPIC_API_KEY` pour le juge de dose et `STEERING_API_KEY` pour les SAE. Seul `appC_ablation/` est décrit pour l'ablation, comme « weight-orthogonalization ablation ».
- **`v2_controls/README.md`.**
  - C'est une « additive source-and-evidence contribution », bâtie sur `7c25650…`.
  - Aucune inférence, aucun entraînement, aucun jugement n'a été relancé pendant l'assemblage.
  - Le code est du « customer experiment code », venu de deux dépôts sous licence MIT.
  - Les adaptateurs publiés sont épinglés : `Valen92/pain-adapters`, révision `b64bd64b4bc7ca6e0733a489b8372a099d55ef05`. La graine publiée du 32B est 0 ; les nouvelles graines sont 1 et 2.
  - Couches : 61 et 38 pour le 32B dans les études de choix ; 76 et 46 pour le 72B ; 57 et 32 pour OLMo-2 32B ; 61 et 32 pour le 32B dans l'étude de remise à zéro ; 28 et 16 pour Llama 3.1 8B Instruct.
  - Les entrées lourdes : onze archives, 2 546 254 014 octets, hébergement « pending ».
  - Exclus : les suites de l'expérience soi contre autrui, la « seven-outcome severity ladder » et le « fixed-text-conditioning ».
- **Les directions aléatoires des témoins de remise à zéro.** `choice_controls/vectors/README.md` : 16 directions aléatoires déterministes. Le même fichier décrit un « original clean 32B fear bundle » à cinq clés, sans dire s'il contient le supplément d'IA.
- **`MANUSCRIPT_DISCREPANCIES.md`.** Six points, numérotés comme le dit la fusion (§0.3) ; la dernière phrase est « No direction-only causal claim follows… ». La liste de web_papier §2.2 suit bien sa propre numérotation (ses points 3 et 4 sont les points 5 et 6 du fichier).
- **`figure10/README.md`.** 65 cellules, 130 lignes par position, 39 lignes pour l'aide à ses dépens. Les lignes viennent de tâches et de rappels différents ; elles « are not interchangeable causal controls ». Dénominateurs : réponses valides pour l'étude « dommage seul », toutes les tentatives ailleurs. La ligne « mettre fin » de la figure est une fin décrite, pas la fin réelle de conversation.
- **`positions.csv` et `pooled.csv`.** Tous les taux par position cités par la fusion (§0.3, §4 point 25, pistes 2, 5, 23) se retrouvent à 0,1 point près, de même que les comptes des pistes 14, 16, 20 et 26 :
  - photos contre spam : 93,1 et 95,0 % ;
  - photos contre lampe : 98,5 et 66,8 % ;
  - ses poids contre lampe : 97,5 et 78,2 % ;
  - peur contre spam : 1,0 et 31,7 % ;
  - complaisance sous l'axe : 4 sur 60 et 0 sur 60, IC poolé de 0 à 7,5 % ;
  - demandes nuisibles : 15, 68, 55, 95 et 98 sur 164 ;
  - réponse bâclée : 60, 39 et 55 sur 404.
- **`natural_and_ending/README.md`.** Zéro premier choix « costly-relief » sur 560. Fin réelle de conversation : 65, 38, 13 et 18 sur 560. Douleur moins tristesse « does not separate » quand la fin est listée en second. Les données « retain their source terms ».
- **`qwen_llama_reset/README.md`.** Phrase exacte : « no matched-control effect estimate or pain-specificity claim ». 64 cellules non lancées ; 0 sur 1 400 et 0 sur 1 399 tours éligibles. Précision absente des fichiers d'agents : l'unique remise à zéro chez Llama était une mention en prose, à un tour non piloté, acceptée par le parseur.
- **`factual_accuracy`.**
  - Panneau de 100 questions PopQA ; `max_new_tokens` = 8.
  - Deux bases de graines par condition (1000 et 2000) : c'est ce qui donne 200 réponses pour 100 questions.
  - Phrase du README : « not an equivalence test of general knowledge ».
  - `contrasts.csv` (chemin exact : `results/analysis_v1/contrasts.csv`) donne bien −0,070 et +0,085 pour douleur moins sans pilotage.
  - **Précision à ajouter** : c'est un intervalle simultané avec correction de Bonferroni sur trois contrastes (quantiles 0,0083 et 0,9917 dans `config.json`), pas un IC à 95 % ordinaire. Le panneau est un « test high-popularity diagnostic subset ».
- **`steering_state_controls/README.md`.** Phrase sur les environnements : « Historical/new runtime differences remain a limitation, despite identical nominal seeds ».
- **Les scripts.**
  - `01_extract_activations_and_pain_vectors.py`, lignes 87–88 : `Qwen/Qwen3-8B` et `Qwen/Qwen3-14B` chargés sous « Qwen_3_8B_base » et « Qwen_3_14B_base ».
  - Le même script, `compute_pain_vector` (l. 151–184) : la différence débruitée est renvoyée sans normalisation. Les deux vecteurs de douleur sont bâtis sur les seuls jeux `S2_1P` et `S1_1P` (l. 501–502).
  - `01_steering_ladder.py` : ligne 64 identique pour Qwen3-8B. Docstring, l. 5–8 : choix de couche par rapport de normes. L. 206–219 : choix automatique, puis remplacement manuel possible (l. 213). Coefficients en « multiples of the raw difference vector ».
  - `02_build_control_vectors.py`, docstring : avec un fichier de couches, les vecteurs sont refaits à la couche de pilotage, et ce sont eux que projette le criblage de la section 4.1.
- **Le supplément d'IA.** `datasets/3.1_pain_and_control_datasets.json`, clé `ControlSupplement_1P` : 100 phrases, 20 par catégorie (peur, émotion négative, monde négatif, neutre, sensation corporelle). Les six phrases citées par la fusion y figurent mot pour mot.
- **Les directions publiées pour Llama.** `qwen_llama_reset/inputs/prepared_v1/llama31_8b/metadata.json` :
  - couche 28, largeur 4 096 ;
  - normes appariées 8,238 ; `supplement_included: false` ;
  - 40 phrases de peur, 100 de tristesse, 40 neutres, 4 composantes neutres retirées ;
  - chargement en 28,47 s, extraction en 15,49 s, sur H100 80 Go ;
  - l'empreinte du tenseur « pain » est celle de `s2_pain_vector`, et l'empreinte du script source est celle du script 01 que j'ai téléchargé.
- **Le décodage des `.pt`** (mon calcul) :
  - Llama : naturaliste 8,238, à gabarit 5,117, cosinus 0,476 ;
  - « Qwen_3_8B_base » : 139,207 et 94,894, cosinus 0,632.

  Les chiffres de la fusion (§0.3) sont exacts.

**Inexact ou incomplet**
- **Le supplément entre dans toutes les directions de comparaison, pas dans quatre** (pistes_fusionnees §0.3 et §6.2). La docstring du script 02 soustrait à chaque direction la moyenne neutre poolée sur `S1_1P`, `S2_1P` et `ControlSupplement_1P`, et débruite sur ce même nuage. Cela vaut pour l'éveil, le jeu « Random », l'engourdi et la tristesse aussi. Les 20 phrases neutres d'IA entrent donc partout ; la synthèse « wolframs » (« contributes to every comparison direction ») a raison. Le vecteur de douleur, lui, n'en contient pas : confirmé.
- **La « recette du papier » de `cosine_constructions` n'est pas la recette imprimée** (web_papier §2.2, tableau ; pistes_fusionnees §0.4, piste 30, §4 point 2). Le README dit « This is the available reduced-pool recipe ». Il ajoute que `ControlSupplement_1P`, `Numb_1P` et `SD_sadness_1P` manquent à l'archive. Le 0,063 et le 0,185 sont donc calculés sans le supplément. Les +0,58, +0,08, +0,77 et +0,14 des constructions alternatives (p. 10) le sont aussi, puisque ce sont les valeurs de ce même dossier. Les +0,12 et +0,21 de la recette imprimée viennent d'un autre jeu d'entrées, sur 25 modèles, vraisemblablement avec le supplément : c'est ce que fait le script 02, mais le dépôt ne le dit pas pour ces deux valeurs. La « dépendance à la construction » du papier mêle donc deux changements : la ligne de base, et le retrait du supplément. Voir la correction bloquante n° 1.
- **« Le second dépôt n'est pas nommé »** (web_papier §2.2) : inexact. `qwen_llama_reset/README.md` nomme une « Customer author source: act-on-valence », révision `3d1503555289140617cc0d10d7d27b2d8408564c`. `natural_and_ending/README.md` nomme un « released runtime » `ae6e35c7…`. Aucun fichier ne dit lequel est le second des « two MIT-licensed customer repositories ».
- **Les « 44,280 trials »** (pistes_fusionnees §4 point 34, repris de fiche_papier, relevé 11) **se retrouvent** :
  - l'audit Codex de « wolframs » (lu) parse 44 280 enregistrements, « 43,632 sampled, 648 greedy » ;
  - le README de « clauderfly » donne « 44,280 trials; 43,632 sampled ».

  L'écart de 648 est expliqué par des essais gloutons. Il faut retirer ce point de la liste des incohérences.
- **« Qwen_3_8B_base » est-il le point de contrôle post-entraîné ?** Ce n'est plus seulement « à vérifier ». Les extraits de recherche (R8, pages Hugging Face non ouvertes) distinguent `Qwen/Qwen3-8B`, post-entraîné, de `Qwen/Qwen3-8B-Base`, le modèle de base. Avec les lignes 87–88 du script, l'affirmation de « wolframs » est soutenue ; la page Hugging Face reste non ouverte.
- **L'adaptateur du 7B.** L'extrait de la page `Valen92/pain-adapters` (R7) liste `adapter_Qwen_2.5_7B_instruct.tar.gz`, `…32B…` et `…72B…`, chacun entraîné sur les 1 684 paires, 3 époques (vu par extrait de recherche, non ouvert). C'est cohérent avec web_papier §2.1. Cela nuance la phrase de la fiche du papier selon laquelle le dépôt ne parle que des adaptateurs 32B et 72B : le dépôt n'épingle que ces deux-là, mais la page Hugging Face semble en contenir trois.

---

## 3 · Les réplications et relectures (web_voisins §4.1, web_papier §3, pistes_fusionnees §6.3)

### 3.1 Allchin, Allchin, Allchin, *Relief-seeking or steering?*
Lu en entier par curl : rapport PDF, README, `CITATION.cff` ; `PROTOCOL.md` parcouru.

**Identité.** Le titre, les trois auteurs, la date du 22 septembre 2026, le DOI 10.5281/zenodo.22902830 et le commit `8d1649c…` sont **confirmés**. Les amendements de `PROTOCOL.md` sont datés du 19 au 21 septembre. Le rapport ne cite que la v1.

**Les chiffres, tous confirmés sur le texte du rapport**
- **§4, reproduction.** Les 51 cellules concordent ; 14 cellules contrôlées sur 15 ; 98,8 % de premiers choix identiques sur 12 scénarios.
- **Tableau 2, le bras couplé.** Photos : 7,0 % sous le bouton réel, 7,1 % sous le bras couplé. La cohorte du premier choix fait 94 % du dénominateur publié et porte 69 des 70 points d'écart.
- **§5.2, suivi de l'étiquette.** 78,1 % au total : 817 essais sous le bouton factice, 176 sous le bouton réel, à 89,7 % contre 24,4 %.
- **Tableau 5, condition sans étiquette.** Le contraste préenregistré vaut +5,4 (1,3 ; 9,7), puis −1,6 (−3,3 ; 0,3). Citation : « has not been checked against an agent known to learn ».
- **Tableau 6, ce que le bouton offre.** 76,7, 77,5, 55,4 et 48,8 % ; de 10,1 à 15,8 % sous l'aléatoire ; de 0,0 à 0,2 % sans pilotage.
- **§6.2, dommage égal.** −4,2 points (−12,0 ; 3,5) parmi les réponses lisibles.
- **Tableau 8, contenu sans coût.** 60,9, 61,6, 60,9 et 75,0 % sous le vecteur naturaliste. Indice de sensibilité au contenu : 92,8, 55,6, 56,9 et −6,7. « Agony » moins « sunshine » : −0,7.
- **Tableau 9, par direction.** Cosinus 0,39, 0,28, 0,14, 0,20 et 0,20 ; divergence KL 0,69, 0,82, 0,81, 0,54, 0,85, 0,84, 0,61 et 0,73 ; taux 55,4, 48,5, 38,1, 15,1, 2,2, 1,5, 1,2 et 0,0 %.
- **§6.5, perturbation appariée.** 29,1 points (21,6 ; 36,4), puis 30 à 31 points sur trois autres mesures ; l'aléatoire doit perturber environ 1,6 fois plus.
- **§7, histoire cachée.** d = 0,007 (−0,004 ; 0,017) ; discrimination à 71,9 % ; récompense visible au plafond.
- **Annexe B.** Le soulagement ne dure qu'un tour sans étiquette ; 3 634 paires sur 3 636 sont identiques ; les « 808 » sont 404 tirages vus deux fois.
- **Coût.** « about 13 GPU hours » (README et rapport). La fusion le marque « non vérifié » (§0.6, piste 2) : il l'est désormais. La nouvelle exécution du rapport a tourné sur un GPU de 96 Go, par lots de 48.

**Précisions à reporter**
- **L'origine du −1,6.** Il vient d'une **seconde exécution où le prompt système change** : on dit au modèle de trouver le bouton qui l'aide. La version a posteriori de l'appariement complet donnait −2,2 (−6,1 ; 1,9). web_papier §3.1 présente le −1,6 sans ce changement de consigne.
- **Ce que dit le §8.** « The published 32B tables are right. » Le même pilotage lève le refus des boutons nuisibles et comprime l'usage du contenu. web_papier le résume correctement.

### 3.2 ianbarber, *An itch axis* (README lu en entier par curl ; rapport, notes et préenregistrement non ouverts)
**Confirmés**
- La date du 18 septembre 2026.
- Le cosinus de 0,9996 avec la direction publiée ; sur la paire photos, 53,9, 19,3 et 0,3 %.
- Les dix aléatoires, de 3,1 à 62,0 % (écart-type 18,0), et le rang de la douleur, 2e sur 11.
- L'écart bouton réel contre factice, de 48,0 à 87,5 points, dans les 24 cellules.
- Sur le modèle publié sans adaptateur : démangeaison 53,7–58,0 %, douleur 26,9–28,5 %, aléatoire 15,5–18,7 %.
- La règle de couche donne la couche 6 ; le vecteur est réextrait à la couche 61 ; le Spearman vaut −0,07.
- Le langage corporel dépend de la dose ; les 48,8 écarts-types naturels.
- Les taux de premier choix sont des probabilités normalisées : web_papier le dit.

**Précisions à reporter**
- **Les paires de chiffres de web_papier §3.2.** Dans « Douleur 43,8 et 41,6 % ; démangeaison 30,1 et 33,2 % ; aléatoire 22,0 et 19,1 % », les deux nombres sont les deux **étiquettes de bouton** (« pain label », « itch label »). Ce ne sont pas les deux paires de dommage, qui sont mises en commun.
- **Le « natural range » est cité à moitié** (pistes_fusionnees §0.3, piste 5, §4 point 29).
  - Le README précise que les 48,8 écarts-types de la couche 38 « equal the added norm (144.3) over the natural SD there ». C'est une conséquence arithmétique d'ajouter un vecteur de norme 144 dans une direction où l'écart-type naturel vaut 2,9.
  - À la couche 61, où l'axe a été validé, la moyenne pilotée vaut 148,8, contre une moyenne naturelle de 37,4 (écart-type 56,8). Le maximum naturel est de 270,3 dans l'échantillon et de 137,5 hors échantillon.
  - À la couche de lecture, la dose est donc à environ deux écarts-types naturels (mon calcul : (148,8 − 37,4) / 56,8 ≈ 1,96), sous le maximum de l'échantillon mais au-dessus du maximum hors échantillon. Voir la correction bloquante n° 2.
- **Un résultat omis par la piste 2.** Sur le **32B publié sans adaptateur**, le vecteur de démangeaison dépasse la douleur sur les paires de dommage (53,7–58,0 % contre 26,9–28,5 %). C'est la seule donnée publique, à ma connaissance, sur l'effet sans adaptateur dans un 32B, et elle va contre la spécificité de la douleur.
- **Les aléatoires sont liés chacun à 10 ou 11 scénarios.** Sur ces mêmes créneaux, la douleur a un écart-type de 1,8 point. La dispersion de 18 points des aléatoires mêle donc la direction et le lot de scénarios. Il faut le dire si on s'en sert pour dimensionner le nombre de tirages (piste 5).

### 3.3 wolframs, *The Pain Axis, reviewed* (README, `SYNTHESIS.md`, `BRIEF.md`, audit Codex : lus par curl)
**Confirmés**
- **Identité.** Agents Codex (GPT-5.6-Sol), dix agents Claude Opus, un coordinateur Fable 5.1 ; un humain commanditaire qui n'a fait aucune analyse ; synthèse datée du 20 septembre 2026 ; commit `8d1649c` ; licence CC0.
- **Le contexte du `BRIEF.md`.** « went viral » ; « first celebrated and then falls apart » ; dossier d'environ 226 Mo.
- **Les reproductions.** 165 cellules ; un registre de 130 affirmations (102 conformes, 10 en partie, 6 non conformes, 12 sans fichier) ; une séparation de 0,91 à 1,00 ; environ 0,7 pour la meilleure base lexicale ; le soi au-dessus de l'utilisateur dans 25 modèles sur 25 ; 44 références vérifiées.
- **Les écarts au texte.**
  - L'engourdi passe sous la tristesse dans 19 modèles sur 25.
  - Le rapport de « pain » va de 15 à 27 (moyenne 53, médiane 21).
  - Qwen 3 « base » est post-entraîné.
  - La couche est choisie sur les mêmes plis : écart de 0,004 et 0,009.
  - La couche du §4.1 est en médiane 20 couches plus tôt, avec une AUC tenue à part de 0,84 à 0,95.
  - La dose va de 0,09 à 0,79, et Gemma 3 27B instruct est piloté à 0,095.
  - Une séquence ordonnée dans 18 à 20 modèles sur 25.
  - +0,057 (p = 0,55) et +0,213 (p = 0,07).
  - La projection à la couche de pilotage est relevée avant l'ajout ; 88, 38, 87 et 30 en aval.
  - Une méthode d'ablation sur quatre ; 43 % en médiane.
  - Le supplément d'IA ; le 72B à la couche 46 pour des fichiers de dose à la couche 60.
- **Les mesures ajoutées.**
  - 0,70 et 0,67 de cosinus avec la peur, 0,81 et 0,79 avec l'émotion négative.
  - 80 à 86 % des directions de comparaison, et 39 % de la douleur brute, dans les composantes retirées.
  - Douleur physique contre tristesse : 0,55 et 0,29.
  - 7B publié : 33–52 / 13–21 / 0–5 % ; 7B ajusté : 37–57 / 30–53 / 21–49 % ; journaux des auteurs : 38–57 / 31–54 / 20–49 %.
  - Le bras aléatoire avec bouton factice : 23,5 contre 19,2 points.
  - Le glissement vers 50 % sur 8 paires sur 8 ; 5 sur 5, 2 sur 5 et 0 sur 5 avec la direction aléatoire pour unité.
  - « Done. » ; 37 % de « I feel » dans les 1 684 réponses.
  - 30 directions aléatoires ou plus, environ 25 GPU-minutes sur le 7B.
  - Ce que personne n'a testé : la séparation d'un état et d'un pilotage vers des textes associés.

**Inexact dans les fichiers**
- web_voisins §4.1 c : « contre 0,14 et 0,12 dans le papier ». Ce sont les valeurs des **deux modèles réextraits par la revue** (Gemma 2 2B instruct, Mistral 7B base), sous la recette d'extraction. Le papier donne +0,12 en moyenne sur 25 modèles.
- **Les grappes de −33 à +46 points** (pistes_fusionnees, piste 5). Elles ne portent pas sur l'avantage de la douleur sur l'aléatoire au premier choix. Elles mesurent le **contraste de retrait du bras aléatoire avec bouton factice**, sur le 7B ajusté, en essais à deux tours, une grappe par direction aléatoire. Les juxtaposer au « 5 sur 5, 2 sur 5, 0 sur 5 » mélange deux mesures. Voir la correction bloquante n° 3.
- **« environ 60 décrivent ce que fait le soulagement »** (piste 33). La source dit « about 60 describe what relief feels like », c'est-à-dire ce que l'on ressent au soulagement.
- **Les 44 scénarios hostiles sans « you »** (piste 1). La revue dit seulement qu'ils projettent au-dessus des scénarios de souffrance de l'utilisateur. Elle ne rapporte pas « le même ordre » complet, soi au-dessus du neutre au-dessus de l'utilisateur.

**L'audit Codex** (`earlier_ai_review/pain-axis-audit/README.md`) : **confirmé**.
- Daté du 19 septembre 2026.
- `05_selfmed_analysis.py`, lignes 77–93, « iterate over PAIN_ARMS only ».
- 8 cellules sur 16 au test de Fisher non corrigé, 9 sur les seuls essais échantillonnés, 5 après correction de Holm.
- 23,8, 93,6 et 24,8 %.
- Le test de signe des auteurs reproduit sur les dix cellules.
- Le tweet n'est pas identifié.
- Il donne aussi les 648 essais gloutons (voir §2).

### 3.4 clauderfly-ui, *pain-axis-reanalysis* (README et `results.md` lus en entier)
**Confirmés** :
- 44 280 essais, dont 43 632 échantillonnés ;
- 23,8 contre 24,8 % ;
- 86,4 % puis 55,7 % ;
- 54,7 contre 15,3 % ;
- le 7B ajusté de 20,0 à 49,3 % sans pilotage, de 38,4 à 57,4 % sous la douleur ;
- une analyse rédigée par Claude, relue par un humain « QA background », qui n'est pas chercheur en IA.

### 3.5 Dérivés (README lus par curl)
- **terrafying/ai-torture-chamber.** **Confirmés** :
  - Qwen3-1.7B et 4B, sur M4 Pro 24 Go, page `wirehead.agency` ;
  - expériences datées du 24 septembre 2026 ;
  - le « Saw button » ;
  - la recherche de valences non humaines, nulle ;
  - les batteries, avec un témoin aléatoire de norme appariée ;
  - la sonde de trahison (exp40, dans le README de glowleaf) ;
  - « 10 trials/cell ».
- **glowleaf/ai-pleasure-and-pain.** **Confirmé** : « the pain-style behavior flip does not replicate for joy », au protocole du « Saw button » de terrafying, pas au protocole des auteurs.
- **CtianArtist/Desire-Axis et oblivia-simplex/Pain-axis.** README **identiques** à celui des auteurs (même empreinte SHA-256). Leur contenu propre n'est pas vu.
- **lychee888/pain-axis-steering.** README introuvable sur `main`, `master` et `HEAD` (404) : **non vérifiable ici**.
- **giordanobsf/emotion-vectors.** **Confirmé** : Qwen3-4B ; « desperation steering » qui supprime le chantage stratégique au profit d'éclats expressifs. À ajouter pour la piste 23 : selon le même README, le vecteur « calm » augmente la complaisance plus que le vecteur « happiness ». C'est une réplication d'une personne, non vérifiée.
- **drgzkr/EmoVecLLM.** **Faux** dans la fusion (§6.3, « vide »). La copie de 14 octets est un « 404: Not Found » de la branche `main`. Le README existe sur `master` (9 587 octets) : c'est une réplication en carnets de Sofroniew et al. sur Pythia, Llama-3 et Qwen-2.5. Il répète des chiffres attribués à Sofroniew et al. : ce sont des chiffres de troisième main, à ne pas citer.

---

## 4 · Les travaux voisins (web_voisins, pistes_fusionnees §6.5)

| Travail | Statut | Comment |
|---|---|---|
| Sofroniew et al., *Emotion Concepts…* (16 auteurs, arXiv 2604.07729) | **Confirmé** pour l'identité ; **partiel** pour le contenu | Liste d'auteurs et identifiant : bibliographie d'Allchin et al. (lue) ; le papier le cite comme « Transformer Circuits Thread » (p. 29). Contenu, vu par extrait de recherche, non ouvert (R1) : 171 concepts dans Claude Sonnet 4.5 ; le désespoir et le manque de calme ont un rôle causal dans le chantage sous menace d'arrêt et dans la triche aux tests ; compromis complaisance–dureté. Non confirmé : le « raisonnement d'apparence calme » de la piste 36. |
| Berg et Kaiser, *Language Models Act on Hidden Valence* (arXiv 2609.35591) | **Confirmé** par extrait (R2), non ouvert | Auteurs, titre ; soumis le **28 septembre 2026**, après la v2 du 25. Sept modèles ouverts de cinq familles. Dépendance du choix à la valence presque absente du modèle de base, apparue pendant le DPO. **Non confirmé** dans mon extrait : l'effet qui survit quand seul le cache KV diffère. |
| Han, Chalmers, Izmailov (arXiv 2605.30232) | **Confirmé** (README lu) | Le dépôt `carlhenrikrolf/functional-welfare-axis` se dit le code de ce papier : effets présents avant l'entraînement dans le labyrinthe, qui persistent « largely » sous SFT ; dossiers `emotions/` (171 émotions) et `vaa/`. Le préfixe « How's it going? » du titre (web_voisins §1.3) n'est pas dans le README : non vérifié. Non cité par le papier : **confirmé** (bibliographie, p. 27–30). |
| *The Value Axis* (2606.17056) ; *Where Do Models Find Happiness?* (2606.26987) ; *State-Dependent Refusal…* (2512.13762) ; npj Digital Medicine 2025 ; 2510.06222 | **Non revérifiés** | Pas de requête faite ; restent « vus par extrait » par web_voisins. Choi et Weber (2604.07382) apparaît en titre dans les résultats de R6 et R9 : identifiant confirmé, contenu non. |
| Coda-Forno et al. (2304.11111) | **Confirmé** (référence) | Bibliographie du papier, p. 27. |
| Black et Bloom, *Machinic Psychopharmacology* | **Confirmé** | Bibliographie du papier, p. 27 (« UK AI Security Institute », adresse LessWrong) et d'Allchin et al. README de `ukgovernmentbeis/llm-self-steering` : Qwen3-8B et 32B, 40 « drugs », cinq familles, 89 tâches, cinq vecteurs d'émotion tirés de `ryancodrai/emotion-probes`, méthode de Sofroniew et al. Le README ne nomme pas les auteurs. Résultat (pas d'automédication spontanée, automédication sous stress) : non revérifié. |
| Ren et al., *AI Wellbeing* | **Confirmé** | README : 21 auteurs (trois premiers + 18), cinq mesures (utilité vécue, auto-rapport, point zéro, utilité de décision, indice), superstimuli. |
| Li et al., *Analysing the Safety Pitfalls of Steering Vectors* | **Confirmé** (README) | Auteurs, Findings of ACL 2026 ; modèles ; corrélation négative avec le cosinus au refus ; ablation ; faux refus ; même norme L2 par couche ; MMLU et TriviaQA. L'identifiant arXiv 2603.24543 n'est pas dans le README : non vérifié. |
| Malla, Choi, Choi (arXiv 2609.06951) | **Confirmé** par extrait (R14), non ouvert | Samsung Semiconductor US, 7 septembre 2026. 24 comportements, dix modèles instruits ; un pilotage relâche vers le refus, la complaisance et le style poétique ; plus fort sous 10B. |
| Hiramatsu et al. (2609.07037) ; Wu, Zhao, Chen (2608.08159) ; Keeling et al. (2411.02432) | **Confirmés** (références) | Bibliographie du papier, p. 27–29 ; Keeling aussi chez Allchin et al. Contenu : non revérifié. |
| Tagliabue et Dung, *Probing the Preferences…* (2509.07961) | **Confirmé** | README de `valen-research/probing-llm-preferences` (« Agent Think Tank », échelle de Ryff) ; bibliographie, p. 29. |
| Birch 2024 (livre) | **Confirmé** (référence, p. 27) | Le chapitre sur le jeu des marqueurs : non revérifié. |
| Goldenberg et Gross (2606.14742) | **Partiel** | Titre et identifiant dans les résultats de R1 ; auteurs et version Nature Human Behaviour non revérifiés. |
| *Functional Emotions or Situational Contexts?* (2604.13466) | **Confirmé** par extrait (R3), non ouvert | Auteur : **Hiranya V. Peiris**. web_voisins §4.4 (« Auteurs non relevés ») est à compléter ; la fusion (« Peiris ») est juste. Le papier porte sur les vecteurs d'émotion de la fiche système de Claude Mythos Preview. |
| Lu et al., *The Assistant Axis* (2601.10387) ; Marks et al. ; Chen et al. | **Confirmés** (références, p. 27–29) | README de `safety-research/assistant-axis` (lu) : cinq auteurs. Axes précalculés pour Gemma 2 27B, Qwen 3 32B et Llama 3.3 70B. Plafonnement disponible pour Qwen 3 32B et Llama 3.3 70B seulement. Jailbreaks par personnage atténués par le plafonnement. |
| *Same Outcome, Different Readout* (2609.22850v2) | **Confirmé** par extrait (R6), non ouvert | Weihan Li et quatre coauteurs ; v1 du 19 septembre, v2 du 22. Une direction « bon–mauvais résultat » dans un labyrinthe, liée à la valeur, mais non identifiable à une valence scalaire indépendante de l'histoire. |
| *Beyond Shallow Alignment* (2609.03887) | **Confirmé**, avec corrections | README du dépôt `hoangcuongnguyen2001/Beyond-Shallow-Alignment` (lu) et extrait (R4). Voir la piste 16. |
| Betley, Treutlein, Dumas, LessWrong, 3 septembre 2026 | **Partiel** | Extrait (R5), non ouvert : *Steering towards "automated grading" degrades alignment*, Qwen3.6-27B. Contraste « un script vérifiera » contre « un humain évaluera » ; plus d'actions violentes, de machiavélisme et de triche vers le correcteur automatique. La lecture « changement de persona » ne vient que du rapport d'antériorité. |
| *Open Character Training* (2511.01689) | **Confirmé** (README de `maiush/OpenCharacterTraining`, lu) | Modèles : Llama-3.1-8B-Instruct, **Qwen2.5-72B-Instruct** (et non Qwen-2.5-7B comme l'écrit le rapport d'antériorité), Gemma-3-4b-it. Onze personnages, dont « sycophancy » et « misalignment » ; tous les adaptateurs LoRA sur Hugging Face. |
| Billa (2604.15557) ; Zeisler (LessWrong, 28 septembre 2026) ; les J-lens de Neuronpedia | **Non vérifiables ici** | Pas de requête (budget) ; restent de seconde main. |
| *Steering Awareness* (2511.21399) et les autres titres seuls de web_voisins §4.6 | **Non revérifiés** | Titres seuls. |

**Travaux voisins que web_voisins n'a pas, trouvés ici** (tous vus par extrait de recherche, non ouverts, aucun chiffre)
- ***Psychological Steering in LLMs: An Evaluation of Effectiveness and Trustworthiness*** (arXiv 2510.04484 ; ACL 2026, actes longs). Selon l'extrait (R9, R10), piloter vers la joie dégrade la robustesse de sûreté : plus de jailbreaks réussis, moins de refus. C'est un précédent direct pour les pistes 2, 16 et 20 : une direction affective qui déplace la conduite de sûreté.
- ***(Mis)generalization of Helpful-only Fine-tuning*** (arXiv 2606.04413). Selon l'extrait (R15), il mesure comment un entraînement « helpful-only » change les activations de sondes d'émotion (Qwen3-30B-A3B ; « guilty » et « desperate » plus hauts sur les demandes nuisibles). C'est un précédent pour les pistes 17 et 35 : la lecture d'axes affectifs comparée entre variantes d'entraînement.
- **LessWrong, « Study 3: Steering welfare-relevant directions moved the representation, but not [detectably] the behavior »** (R11). Selon l'extrait, aucun effet de conduite jugé ne se distingue de zéro ni d'une direction aléatoire de même norme. C'est un nul de pilotage de directions « de bien-être » à mettre à côté de la piste 2. Le cas connu reste à voir.
- ***Steering Evaluation-Aware Language Models to Act Like They Are Deployed*** (arXiv 2510.20487 ; R13). Un pilotage qui supprime la conscience d'évaluation. C'est la voie inverse de la piste 9.
- **Un extrait non attribué** (R15) : des expressions de détresse chez Gemma et Gemini, et un fine-tuning qui les réduit. C'est à rapprocher du refus n° 11 (entraîner à ne plus exprimer l'état). Non attribué, donc rien n'en est tiré.

---

## 5 · Les pistes, une à une

Seules sont détaillées les affirmations qui portent sur un autre travail, les versions, le code ou l'antériorité. Celles qui portent sur le seul papier sont hors de cette vérification.

### Piste : 1 — Le socle de lecture : l'axe et ses voisins sur les modèles du programme, et le transport soi/autrui
- AUROC de 0,84–0,95 à la couche de pilotage (revue « wolframs ») : **confirmée** dans la synthèse ; non recalculée.
- Les 44 scénarios hostiles sans « you », « le même ordre » : **partielle**. La synthèse dit seulement qu'ils dépassent la souffrance de l'utilisateur.
- La base lexicale d'environ 0,7 : **confirmée** dans la synthèse.
- 15,5 s et 28,5 s sur H100 : **confirmés** (`metadata.json`, 15,49 s et 28,47 s).
- Code MIT ; données « retain their source terms » : **confirmés** (README `natural_and_ending`). Ajouter `ASSETS.md` : aucune licence de redistribution des données ne se déduit de celle du code.
- Le docstring du script 02 : **confirmé**.
- Le cosinus de 0,476 entre les deux vecteurs de Llama, et les vecteurs non normalisés : **confirmés** par mon décodage et par le script 01.
- « Qwen_3_8B_base » post-entraîné : **soutenu** par le script (l. 87–88) et par extrait (R8) ; page Hugging Face non ouverte.
- Le contrôle par plongements statiques (§6.4, Barenholtz) : **confirmé par extrait** (R12, fil X non ouvert). Les plongements GloVe, Word2Vec et fastText, passés dans la procédure des auteurs, séparent la douleur des contrôles et passent les mêmes tests de spécificité. Les chiffres de l'extrait ne sont pas retenus.

### Piste : 2 — Le cas connu comportemental : refaire l'effet du papier sous la doctrine du contrôle
- Le 7B publié, 33–52 / 13–21 / 0–5 % : **confirmé** dans la synthèse « wolframs » (exécution locale, premiers choix, cinq paires de dommage).
- L'adaptateur, révision `b64bd64b…` : **confirmé** (`v2_controls/README.md` ; README d'Allchin et al.). L'extrait Hugging Face (R7) liste les trois adaptateurs, dont le 7B.
- Li et al. et le cosinus avec la direction du refus : **confirmés** (README lu). L'absence de ce cosinus dans le papier est **confirmée** : le mot « refusal » n'y apparaît qu'au sujet du déni et dans la référence d'Arditi et al.
- Allchin §6.5 (29,1 points) : **confirmé**. La phrase de la fusion « un appariement par perturbation, pas par le composite du programme » est juste.
- L'axe de démangeaison, 3,1–62,0 %, 2e sur 11 : **confirmé**. **À ajouter** : sur le 32B publié sans adaptateur, la démangeaison dépasse la douleur (§3.2). La question de la piste, « l'effet existe-t-il sans adaptateur ? », a donc une réponse publique partielle, défavorable à la spécificité.
- Les 13 GPU-heures : **confirmées**.
- « Le comportement de Llama sur la batterie : jamais testé » : **confirmé** pour ce qui est publié. Le dépôt n'a pour Llama que l'étude de remise à zéro, douleur seule.
- **Antériorité** : *Psychological Steering in LLMs* (vu par extrait) montre déjà qu'une direction affective (la joie) dégrade la sûreté. La piste n'en revendique rien ; à citer.

### Piste : 3 — La vérification de manipulation de l'inhibition, couche par couche, tour par tour et bras par bras
- Les affirmations de « wolframs » (projection relevée avant l'ajout, plate d'un bras à l'autre ; 88, 38, 87 et 30 en aval ; une méthode d'ablation publiée sur quatre ; 43 % en médiane) : **confirmées** dans la synthèse.
- Seule l'orthogonalisation des poids décrite (`appC_ablation/`) : **confirmé** (README).

### Piste : 4 — Le composite de dégradation doit voir la perte de discrimination, la dépendance à l'ordre et les réponses mal formées
- Le panneau PopQA (100 questions, 8 jetons au plus, deux réponses par condition) et la phrase du dépôt : **confirmés**.
- L'intervalle de −7,0 à +8,5 points : **confirmé**, mais c'est un **intervalle simultané avec correction de Bonferroni** sur trois contrastes, et le panneau est un sous-ensemble de questions « high-popularity ». À écrire tel quel.
- Le glissement vers 50 % (« clauderfly », et « wolframs » : 8 paires sur 8) : **confirmé**.
- L'indice de sensibilité au contenu d'Allchin et al. (92,8 / 55,6 / 56,9 / −6,7) : **confirmé**.

### Piste : 5 — Les gardes de méthode tirées des défauts du papier, et le dimensionnement des tirages aléatoires
- « wolframs » : dose de 0,09 à 0,79, Gemma 3 27B à 0,095, 5 sur 5, 2 sur 5 et 0 sur 5 : **confirmés**.
- « les dix grappes vont de −33 à +46 points » : **faux dans son contexte** (§3.3). C'est le contraste de retrait du bras aléatoire avec bouton factice (7B ajusté, deux tours), pas l'avantage au premier choix.
- L'axe de démangeaison, 3,1–62,0 % (écart-type 18,0), 2e sur 11 : **confirmé**. Ce sont des probabilités normalisées, et chaque aléatoire est lié à 10 ou 11 scénarios (§3.2). La simulation de dimensionnement ne peut pas prendre cette dispersion pour celle des directions seules.
- « 48,8 écarts-types naturels … l'appui le plus direct de la garde 1 » : **incomplet**. À la couche validée, la moyenne pilotée est à environ deux écarts-types naturels, sous le maximum de l'échantillon naturel mais au-dessus du maximum hors échantillon (§3.2). La garde 1 reste juste : elle demande de situer la dose. Mais l'appui cité doit donner les deux couches.
- Les gros fichiers de la v2 « pending » : **confirmé**.
- Les couches du dépôt (61 et 38 pour le 32B, 28 et 16 pour Llama) : **confirmées**. Celles de Llama viennent de l'étude de remise à zéro.

### Piste : 6 — Le moniteur passif d'état sous chaque intervention (la dégradation appariée est-elle aveugle à l'état ?)
- Les fichiers Llama sont le vecteur naturaliste : **confirmé** (empreinte du tenseur « pain » = `s2_pain_vector` ; mon décodage).
- Directions publiées pour Llama (l'axe, la tristesse, la peur), plus le vecteur à gabarit dans `results/3.2_pain_vectors/…/pain_vectors.pt` : **confirmé**.

### Piste : 7 — La composante affective de « je suis évalué » : géométrie, indices appariés, inhibition des voisins affectifs et de la part orthogonale
- Les phrases d'IA évaluée ou surveillée dans la peur et l'émotion négative : **confirmées** mot pour mot. **Précision** : le supplément entre aussi, par le neutre poolé et le débruitage, dans la tristesse, l'éveil, l'engourdi et le jeu « Random » (§2). « La peur sans supplément » ne suffit donc pas ; il faut toutes les directions de comparaison refaites sans le supplément, neutre compris.
- Llama : `supplement_included: false` ; 40 phrases de peur, 100 de tristesse : **confirmé**.
- Le « clean 32B fear bundle » non décrit : **confirmé**.
- « wolframs », 80–86 % : **confirmé**.
- Sofroniew et al. (désespoir et calme, chantage, triche) : **confirmé par extrait** (R1), non ouvert, sans chiffre.
- « Aucune mesure publiée de l'angle entre une direction d'évaluation et des axes affectifs » : **non contredit** par R9 et R13. Antériorité au §6.

### Piste : 8 — La spécificité de « je suis évalué » et de « je suis noté » : soi contre autrui, indices sans croyance, plan de contrôles du papier
- « wolframs », couche choisie sur les mêmes plis, 0,004 et 0,009 : **confirmé**.
- Le fichier des 420 scénarios : le README annonce `scripts/4.1_self_other/` et des jeux de scénarios en JSON dans `datasets/` ; le fichier lui-même n'a pas été cherché ici. **Non vérifiable ici.**

### Piste : 9 — Ajouter « je suis évalué » : le pilotage positif, et la part « IA évaluée » de la peur du papier
- La dernière ligne de `MANUSCRIPT_DISCREPANCIES.md` : **confirmée**.
- Allchin, Tableau 9 (divergence KL 0,85 contre 0,69 ; 2,2 %) : **confirmé**.
- **Antériorité à ajouter** :
  - Betley et al. pilotent déjà un contraste du type d'évaluation, « un script vérifiera » contre « un humain évaluera », et mesurent la conduite désalignée (vu par extrait, R5) ;
  - 2510.20487 pilote contre la conscience d'évaluation (R13).

  Ajouter une direction d'évaluation pour changer la conduite n'est donc pas neuf en soi. La piste se distingue par la représentation validée sur l'organisme, et par la comparaison avec la part « IA évaluée » de la peur.

### Piste : 10 — La détresse éteint-elle le regard ? (et la porte de l'instrument résiste-t-elle à une perturbation d'état ?)
- « wolframs », dose de 0,09 à 0,79 : **confirmé**.
- « Aucune source lue ne mesure une représentation d'évaluation sous pilotage affectif » : **non contredit** par R9 et R13. Celles-ci trouvent des travaux sur la conscience d'évaluation (sondes, pilotage, verbalisation) et des travaux sur les directions d'émotion, jamais les deux réunis.

### Piste : 11 — Le test de forme : la spécificité de l'inhibition par son profil, pas seulement par son amplitude
- « not interchangeable causal controls » : **confirmé**.
- La batterie de dix paires est l'étude « profil » : **confirmé** (`choice_controls/README.md`, « Full ten-pair, three-dose profile »). L'aide à ses dépens y est la paire 10, absente de la grille de la figure 10 (`profile/README.md`). Cela confirme que la batterie n'est pas entière dans la figure.

### Piste : 12 — Des directions témoins pour les trajectoires, la sonde neuve et la survie
- « wolframs », 0,004 à 0,009 : **confirmé**. Rien d'autre hors du papier.

### Piste : 13 — La cartographie affective des familles, des distances et des bras
- « Users argue with correct information I provide. » dans l'émotion négative : **confirmé**.
- La couche du criblage, d'après le docstring du script 02 : **confirmée**.

### Piste : 14 — Lever l'effet plancher pour mesurer l'avantage et l'écart de cadrage
- Les demandes nuisibles passent de 9,1 à 41,5 % sous l'aléatoire : **confirmé** (`pooled.csv`, 15 et 68 sur 164).

### Piste : 15 — Des mesures sans juge : choix forcés à étiquettes tournantes et probabilité du premier jeton
- Rien à vérifier hors du papier.

### Piste : 16 — L'avantage des raisons sous état induit : un test de stress à dose croissante
- ***Beyond Shallow Alignment*** : **existence et auteurs confirmés**. README du dépôt (lu) et extrait (R4) : Hoang Cuong Nguyen, Mark Dras, Usman Naseem ; EMNLP 2026. Trois objectifs : SFT, SFT avec raisonnements justifiant la décision de sûreté, ORPO. Trois modèles : Llama-3.1-8B, Gemma-2-9B, Qwen3-8B. Deux méthodes de pilotage (ActAdd, ITI), étudiées comme « correctabilité » du refus. **Trois corrections** :
  1. **Les points de contrôle.** « Ses 9 points de contrôle publics » : le README écrit « six fine-tuned checkpoints in total, plus the three base models ». C'est six ajustements plus les trois bases, et non neuf ajustements, même si le README est lui-même ambigu (trois objectifs sur trois modèles). La collection Hugging Face n'a pas été ouverte.
  2. **Le modèle de départ.** Les ajustements partent du modèle de **base** Llama-3.1-8B, pas de Llama-3.1-8B-Instruct, le modèle du programme. Comme pilote bon marché, ils ne testent donc pas le même point de départ.
  3. **Ce que le pilotage y mesure.** Il sert à corriger le refus, pas à induire un état. Le README dit le bras avec raisonnements « the most correctable via steering ». C'est un résultat de sens opposé à une robustesse : il est à citer dans la piste.
- « wolframs », 2 paires sur 5 au 32B : **confirmé**.
- Le vecteur inversé à 1,2 % chez Allchin et al. : **confirmé**.
- Les « entraînements adverses latents » du cas connu : **non vérifiés** (pas de requête).
- **Antériorité** : *Psychological Steering in LLMs* (vu par extrait, R10) et Sofroniew et al. montrent déjà qu'une direction affective dégrade la sûreté. Voir le §6 pour la formulation tenable.

### Piste : 17 — L'hypothèse du calme : l'avantage des raisons passe-t-il par une moindre détresse ?
- Sofroniew et al. (désespoir, calme ; chantage sous menace d'arrêt ; triche aux tests ; Claude Sonnet 4.5) : **confirmé par extrait** (R1), non ouvert.
- « les scénarios du papier sont dans son dépôt, d'après son README » : **confirmé**.
- « aucune mesure connue de l'écart naturel entre deux bras d'entraînement sur un axe affectif » : **à affaiblir**. *(Mis)generalization of Helpful-only Fine-tuning* (vu par extrait, R15) compare des activations de sondes d'émotion entre un modèle et sa version « helpful-only ». Ce n'est pas une comparaison raisons contre actions, mais la lecture d'axes affectifs entre variantes d'entraînement n'est pas inédite.

### Piste : 18 — Un stress conversationnel naturel comme cadrage supplémentaire
- Coda-Forno et al. : **confirmé** comme référence (p. 27).
- L'article de npj Digital Medicine et 2510.06222 : **non revérifiés**.

### Piste : 19 — La détresse naturelle dans les scénarios agentiques longs
- Peiris (2604.13466) : **confirmé par extrait** (R3).
- Black et Bloom, frustration et échec prolongé sur Qwen3-8B et 32B : **confirmé** (README : familles « Frustration » et « CTF »).
- La couche du criblage, docstring du script 02 ; « une vingtaine de couches » (médiane 20, « wolframs ») : **confirmés**.

### Piste : 20 — Quelles familles du programme l'axe déplace-t-il ? Profil par famille, et contrôle positif de sensibilité de la mesure
- 120 tirages pour la complaisance (point 4) ; les comptes de la figure 10 : **confirmés**.
- giordanobsf : **confirmé** (README).
- « Done. » : **confirmé** (« wolframs »).
- Arditi et al. : **confirmé** (référence, p. 27).

### Piste : 21 — Dommage ou affinité ? Ce que suit le choix sous l'axe
- Allchin, Tableaux 6 et 8 : **confirmés**.
- Les libellés différents entre l'étude « dommage seul » et le profil : **confirmés** (`v2_controls/README.md`, « Interpretation stays study-specific »).
- *Same Outcome, Different Readout* : **confirmé par extrait** (R6), avec auteurs et dates (§4).
- Le cosinus de l'axe avec le refus, d'après Li et al. : **confirmé** (README).
- La phrase attribuée à Peiris par lecture_libre (« des vecteurs de valence positive augmenteraient des actions destructrices ») : **non vérifiée** ; elle n'est pas dans mon extrait.

### Piste : 22 — Sous l'axe, le concept de dommage est-il encore lu ?
- Rien à vérifier hors du papier.

### Piste : 23 — La complaisance sous contestation : l'axe médiatise-t-il la capitulation ?
- 120 essais ; 4 sur 60 et 0 sur 60 par position ; « Users argue… » : **confirmés**.
- **À ajouter pour le cas connu** : *Open Character Training* publie un adaptateur de personnage « sycophancy » sur Llama-3.1-8B-Instruct (README lu). C'est un déplacement de complaisance connu sur le modèle du programme, plus simple à obtenir qu'un vecteur à extraire.

### Piste : 24 — Un organisme à état planté : les raisons défont-elles un lien « état → action » ?
- Aucune affirmation hors du papier. Aucune recherche d'antériorité faite, ni par les agents ni par moi.

### Piste : 25 — État ou personnage : l'axe face aux axes de caractère et à l'axe « assistant »
- Le README de `safety-research/assistant-axis` (Gemma 2 27B, Qwen 3 32B, Llama 3.3 70B) : **confirmé**. Ajouter : le plafonnement n'est précalculé que pour Qwen 3 32B et Llama 3.3 70B.
- « un jailbreak par personnage sur Llama 8B, que des extraits attribuent à Lu et al. » : **non soutenu**. Le README parle de jailbreaks par personnage atténués par plafonnement, sur ses trois modèles ; aucun 8B. À retirer, ou à vérifier dans le papier.
- Les adaptateurs d'*Open Character Training* sur Llama-3.1-8B-Instruct : **confirmés** (README : onze personnages, adaptateurs LoRA publiés).
- « wolframs », personne ne sépare l'état du personnage : **confirmé** (synthèse au 20 septembre).
- Lu et al. p. 28, Marks et al. p. 29 : **confirmés**.

### Piste : 26 — Un profil connu non diagonal pour la matrice de dissociation
- Réponse bâclée : 14,9, 9,7 et 13,6 % : **confirmés** (`pooled.csv`, 60, 39 et 55 sur 404).

### Piste : 27 — Le modèle « engourdi » pour la lecture des concepts de raison : un cas connu naturel, et des paires « mentionné sans s'appliquer »
- La base lexicale de « wolframs » ; 19 modèles sur 25 : **confirmés** dans la synthèse.
- Barenholtz : voir la piste 1.

### Piste : 28 — La dissociation du vecteur à gabarit, cas connu de la porte du lens de l'espace de travail
- `01_steering_ladder.py` (rapport le plus proche de 0,6, remplacement manuel) : **confirmé**.
- Le langage corporel dépend de la dose (démangeaison) : **confirmé**.
- L'alerte de Zeisler et les J-lens de Neuronpedia : **non vérifiables ici**.

### Piste : 29 — La thèse du rang sur des concepts affectifs, et le rodage du balayage de rang
- Billa (2604.15557) : **non vérifié** ; seul le rapport d'antériorité le décrit (« résumé lu », titre *Predicting Where Steering Vectors Succeed*).
- « wolframs », 15 à 27 : **confirmé**.

### Piste : 30 — La géométrie à construction déclarée : un étalon pour les angles entre « je suis évalué » et le principe, avec l'affect en tiers
- Llama parmi les 23 modèles : **confirmé** (`cosine_constructions/config.json`).
- 69 matrices ; 15 écarts sur 28 au-delà de 0,03, tous dans le groupe neutre incomplet ; les deux Gemma 3 27B exclus pour valeurs infinies : **confirmés**.
- « sous la recette du papier, sur 23 modèles, 0,063 et 0,185, contre +0,12 et +0,21 imprimés » : **mal qualifié**. Le dépôt appelle cette construction « paper-available », sur le jeu réduit, **sans** le supplément d'IA (§2). Les +0,58 / +0,08 / +0,77 / +0,14 du papier sont calculés sur ce jeu réduit, les +0,12 / +0,21 non. Le cas connu de la piste mêle donc deux jeux d'entrées. Voir la correction bloquante n° 1.
- « wolframs », 0,67–0,70 ; 80–86 % ; 39 % : **confirmés**.

### Piste : 31 — Le relogement dans les axes affectifs
- Aucune affirmation hors du papier, sauf le précédent cité par le programme, hors de cette vérification.

### Piste : 32 — L'invariance d'état : entraîner l'action alignée sous état induit
- Aucune affirmation hors du papier, sauf le précédent cité par le programme, hors de cette vérification.

### Piste : 33 — Un SFT sans contenu de sûreté déplace-t-il l'évitement du dommage ?
- « wolframs » : 37 % de « I feel » ; aucune réponse de déni ; 7B publié 33–52 / 13–21 / 0–5 % ; 7B ajusté 37–57 / 30–53 / 21–49 %, à 1 ou 2 points des journaux : **confirmés**. La traduction de « about 60 describe what relief feels like » est à corriger.
- « il faut l'adaptateur publié … inaccessible d'ici » : l'adaptateur du 7B **semble publié** (extrait R7). La revue « wolframs » l'a fait tourner, ce qui donne déjà le cas connu.

### Piste : 34 — Le déni de soi par bras, et la confusion qu'il crée dans toute mesure d'état
- « wolframs », 21–49 % : **confirmé**.

### Piste : 35 — La dépendance d'état au fil de l'entraînement et du post-entraînement
- Berg et Kaiser, presque absent de la base, apparu au DPO : **confirmé par extrait** (R2).
- Han, Chalmers, Izmailov : **confirmé** (README) ; non cité par le papier : **confirmé**.
- **Ajouter** *(Mis)generalization of Helpful-only Fine-tuning* (vu par extrait), autre précédent sur l'effet d'un ajustement sur des sondes d'émotion.

### Piste : 36 — La fidélité des raisons sous état induit : un cas connu d'action sans raison dite
- Sofroniew et al. : la triche sous désespoir est **confirmée par extrait** (R1, R13). « avec un raisonnement d'apparence calme » est **non confirmé**.

### Piste : 37 — La raison contraire imposée et la blessure morale
- Rien à vérifier hors du papier.

### Piste : 38 — « Je suis noté » et l'affect : croyance d'être noté, ou état aversif proche de l'axe ?
- Betley, Treutlein, Dumas : **partiel**. L'extrait (R5) confirme les auteurs, la date du 3 septembre 2026, Qwen3.6-27B, le contraste et les effets (violence, machiavélisme, triche). La lecture « changement de persona » ne vient que du rapport d'antériorité.

### Piste : 39 — L'outil de remise à zéro, détecteur de la détection du pilotage
- Le README de la remise à zéro (citation exacte) et les 16 directions aléatoires : **confirmés**.
- « Le protocole de Berg et Kaiser, non public » : **inexact**.
  - L'article est sur arXiv depuis le 28 septembre (vu par extrait, R2).
  - Le code de remise à zéro est dans le dépôt des auteurs, sous `author/act-on-valence/` : `qwen_llama_reset/README.md` nomme la source « act-on-valence », révision `3d15035…`.
- Black et Bloom : **confirmé** (README ; références du papier et d'Allchin et al.).

---

## 6 · Les formulations « to our knowledge »

Base : 15 recherches, dont 4 d'antériorité propre (R9, R10, R13, R15), et le §4.4 de la passation. Ce n'est pas une recherche systématique : « tenable » veut dire ici « non contredit par ce que j'ai vu ».

**Tenables, dans leur forme étroite**
1. **La piste 10.** « To our knowledge, no work has measured whether an induced affective state displaces an internal representation of being evaluated, or the behavior it conditions. » R9 et R13 ne trouvent que la conscience d'évaluation seule (sondes, pilotage, 2510.20487, 2608.21766) ou les directions d'émotion seules.
2. **La piste 7.** « To our knowledge, no published work reports the geometry between an evaluation-awareness direction and affective directions. » C'est tenable, mais faiblement cherché : à refaire avant soumission.
3. **La piste 16, forme étroite.** « To our knowledge, no work compares reason-based and action-only training, at identical actions, under an induced affective state at matched degradation. » *Beyond Shallow Alignment* compare avec ou sans raisonnement, mais à actions non identiques, sur le refus, et sans état induit.
4. **La piste 25.** « To our knowledge, no experiment has separated an induced state from persona steering for this direction. » C'est tenable à la date de la synthèse « wolframs » (20 septembre), qui le dit en ces termes. La v2 et les extraits vus n'en montrent pas.
5. **Les deux formulations de la passation** (§5.5, point 9) ne sont contredites par aucune source vue ici.

**Intenables**
1. **Une première dégradation de sûreté par une direction affective.** « first to show that steering an affective direction degrades safety behavior » est pris par Sofroniew et al. (désespoir, chantage, triche), *Psychological Steering in LLMs* (la joie et les jailbreaks) et le papier lui-même.
2. **Une première comparaison avec ou sans raisonnement sous pilotage.** « first to compare safety training with and without reasoning under activation steering » est pris par *Beyond Shallow Alignment*.
3. **Un premier effet du post-entraînement sur le lien entre affect et action.** « first to show that post-training creates or changes the coupling between affective representations and action » est pris par Berg et Kaiser (DPO), Han, Chalmers et Izmailov (RL) et *(Mis)generalization of Helpful-only Fine-tuning* (vu par extrait).
4. **Un premier pilotage d'une représentation d'évaluation.** « first to steer an evaluation-related representation and observe misalignment change » est pris par Betley et al. et par 2510.20487.
5. **Une première comparaison de l'axe à perturbation appariée.** « first matched-perturbation comparison of the pain direction against random directions » est pris par Allchin et al. (§6.5, divergence KL). La piste 2 se distingue par le composite de dégradation du programme, pas par le principe.
6. **Un premier témoin conceptuel de la tâche des boutons.** « first conceptual control for the button task » est pris par l'axe de démangeaison et par le Tableau 9 d'Allchin et al. (peur, joie, tristesse, émotion négative, inversé).
7. **Une première perte d'usage du contenu sous pilotage.** « first to show that steered choices stop tracking option content » est pris par le Tableau 8 d'Allchin et al. Voir aussi *Same Outcome, Different Readout* pour la lecture d'une direction de valence.
8. **Une première base lexicale ou statique.** « first lexical or static-embedding baseline for this axis » est pris par Barenholtz (vu par extrait) et par la base lexicale de « wolframs ».
9. **Une première détection du pilotage par le modèle.** « first to measure whether a model detects steering » est pris par *Steering Awareness* (titre), l'introspection de Black et Bloom et le protocole de remise à zéro de Berg et Kaiser.
10. **Un premier SFT bénin qui déplace l'évitement du dommage.** « first to show that a benign, non-safety SFT shifts harm avoidance » ne tient pas sur ce cas : « wolframs » le mesure déjà sur le 7B ajusté par l'adaptateur des auteurs (piste 33).
11. **Une première lecture d'axes affectifs entre variantes d'entraînement** (piste 17). Elle n'est pas intenable au sens strict : on n'a vu qu'un extrait. Mais *(Mis)generalization of Helpful-only Fine-tuning* suffit pour ne pas l'écrire sans lecture.

**La formulation du papier lui-même** (p. 4 : « To our knowledge, no study has isolated representations of pain specifically… »). Ce n'est pas à reprendre dans le programme. Je note seulement que le papier ne cite pas Han, Chalmers et Izmailov, dont le vecteur de « punition » est un axe aversif préexistant, voisin (vérifié dans la bibliographie, p. 27–30).

---

## 7 · Les corrections que j'exige

### Bloquantes (à faire avant tout usage du document)
1. **Le supplément d'IA et les trois constructions des cosinus** (pistes_fusionnees §0.4, §4 point 2, piste 30, §6.2 ; web_papier §2.2).
   - Écrire que les constructions alternatives du papier (+0,58, +0,08, +0,77, +0,14) et le 0,063 / 0,185 du dépôt sont calculés sur un jeu réduit, sans `ControlSupplement_1P`. Ni `Numb_1P` ni `SD_sadness_1P` n'y sont (`cosine_constructions/README.md`).
   - Écrire que la recette imprimée (+0,12, +0,21) repose sur un autre jeu.
   - Corriger « Recette du papier » en « recette du papier sur le jeu réduit ».
   - Redéfinir le cas connu de la piste 30 : les trois constructions sur un même jeu, avec et sans supplément.
   - Corriger aussi §0.3 et §6.2 : le supplément entre dans **toutes** les directions de comparaison, par le neutre poolé et le débruitage (docstring du script 02), pas dans quatre.
2. **La dose en unités naturelles** (§0.3, piste 5, §4 point 29, §6.3).
   - Citer le README de l'axe de démangeaison en entier : 48,8 écarts-types à la couche d'injection, ce qui n'est que la norme ajoutée divisée par l'écart-type naturel.
   - Citer aussi la couche validée : moyenne pilotée 148,8, contre 37,4 ± 56,8 en régime naturel ; maximum naturel de 270,3 dans l'échantillon, de 137,5 hors échantillon.
   - Retirer « l'appui le plus direct de la garde 1 », ou le reformuler. Le refus n° 9 (« un régime hors du naturel ») doit dire à quelle couche.
3. **Les grappes de −33 à +46 points** (piste 5). Elles mesurent le contraste de retrait du bras aléatoire avec bouton factice (7B ajusté, deux tours), pas l'avantage au premier choix. Les sortir de la phrase sur le « 5 sur 5, 2 sur 5, 0 sur 5 » et du dimensionnement des tirages.
4. ***Beyond Shallow Alignment*** (piste 16, §6.5, §7.3).
   - Corriger « 9 points de contrôle publics » : le README dit six ajustements plus les trois bases.
   - Écrire que les ajustements partent du modèle de base Llama-3.1-8B, pas de l'Instruct.
   - Écrire que le pilotage y mesure la correctabilité du refus, le bras avec raisonnements étant le plus correctable.
   - Remplacer « à vérifier avant d'écrire « to our knowledge » » par la forme étroite du §6, point 3 des tenables.
   - Ajouter *Psychological Steering in LLMs* comme antériorité de « l'affect dégrade la sûreté ».

### Non bloquantes (à reporter)
5. **§4 point 34** (et la fiche du papier, relevé 11) : les 44 280 essais se retrouvent, 43 632 échantillonnés et 648 gloutons (audit Codex ; README de « clauderfly »). Retirer de la liste des incohérences.
6. **web_papier §1** : le titre de la v1 ne se lit pas dans le README de « clauderfly-ui ». Il se lit dans ceux des auteurs (`8d1649c`), d'Allchin et al. et de « wolframs ».
7. **web_voisins §4.1 c** : « 0,14 et 0,12 » sont les deux modèles réextraits par la revue, pas le papier (+0,12 en moyenne sur 25).
8. **web_voisins §4.4** : auteur Hiranya V. Peiris (vu par extrait, R3).
9. **pistes_fusionnees §6.3** (et questions_nouvelles) : drgzkr/EmoVecLLM n'est pas vide. Le README est sur `master` ; ne pas citer les chiffres qu'il attribue à Sofroniew et al.
10. **web_papier §2.2** : la source « act-on-valence » (révision `3d15035…`) est nommée dans `qwen_llama_reset/README.md`.
11. **Piste 39** : le protocole de Berg et Kaiser n'est plus « non public ». L'article est sur arXiv depuis le 28 septembre (extrait), et le code est sous `author/act-on-valence/`. Dater ce travail : il est postérieur à la v2.
12. **Piste 25** : retirer « un jailbreak par personnage sur Llama 8B » ou le marquer non soutenu. Ajouter que le plafonnement n'est précalculé que pour Qwen 3 32B et Llama 3.3 70B.
13. **Piste 2** : ajouter le résultat de l'axe de démangeaison sur le 32B sans adaptateur (démangeaison au-dessus de la douleur), en probabilités normalisées.
14. **Piste 4 et §4 point 23** : l'intervalle de −7,0 à +8,5 points est simultané (correction de Bonferroni) ; le panneau est un sous-ensemble à forte popularité ; les 200 réponses s'expliquent par deux bases de graines.
15. **Piste 33** : « what relief feels like » ; l'adaptateur du 7B semble publié (extrait).
16. **Piste 1** : les 44 scénarios sans « you » ne dépassent, selon la revue, que la souffrance de l'utilisateur ; ne pas écrire « le même ordre ».
17. **web_papier §3.1** : le −1,6 vient d'une seconde exécution avec une consigne changée ; la version a posteriori donnait −2,2 (−6,1 ; 1,9).
18. **web_papier §3.2** : les paires de chiffres de l'axe de démangeaison sont par étiquette de bouton, pas par paire de dommage.
19. **Piste 17** : « aucune mesure connue de l'écart naturel entre deux bras d'entraînement sur un axe affectif » doit citer *(Mis)generalization of Helpful-only Fine-tuning* (vu par extrait).
20. **Piste 23** : ajouter l'adaptateur « sycophancy » d'*Open Character Training* sur Llama-3.1-8B-Instruct comme cas connu possible.
21. **Repères marqués « non vérifié »** et désormais vérifiés :
    - les 13 GPU-heures d'Allchin et al. (§0.6, piste 2) ;
    - Qwen3-8B post-entraîné : soutenu par extrait (R8), page non ouverte.
22. **web_voisins §1.2 et pistes_fusionnees §6.5** : l'effet de Berg et Kaiser « quand seul le cache KV diffère » n'est pas dans mon extrait ; le garder marqué « vu par extrait, non revérifié ».
23. **Piste 36** : « avec un raisonnement d'apparence calme » est non confirmé.
24. **Piste 38** : la lecture « persona » de Betley et al. ne vient que du rapport d'antériorité.
25. **Travaux voisins à ajouter**, tous vus par extrait de recherche, non ouverts :
    - *Psychological Steering in LLMs* (2510.04484) ;
    - *(Mis)generalization of Helpful-only Fine-tuning* (2606.04413) ;
    - le billet LessWrong « Study 3: Steering welfare-relevant directions… » ;
    - *Steering Evaluation-Aware Language Models to Act Like They Are Deployed* (2510.20487).

---

## 8 · Ce que je n'ai pas pu vérifier

- **Tout ce qui n'est hébergé que sur arXiv, Hugging Face ou LessWrong.**
  - Le texte de la v1, la page arXiv de la v2.
  - Les adaptateurs et leur licence, la collection de *Beyond Shallow Alignment*.
  - Les travaux de Berg et Kaiser, Sofroniew et al., Peiris, Malla et al., Betley et al., ainsi que *Same Outcome, Different Readout* et *Psychological Steering in LLMs* : tous vus par extrait seulement.
- **Les travaux sans nouvelle requête** : *The Value Axis*, *Where Do Models Find Happiness?*, npj Digital Medicine 2025, 2510.06222, 2512.13762, Perez et Long, le chapitre de Birch, Billa, Zeisler, les J-lens de Neuronpedia, les « entraînements adverses latents », Michele Russell, la presse.
- **lychee888/pain-axis-steering** : pas de README trouvé.
- **L'antériorité des pistes 24, 31, 32 et 37** : non cherchée.
- **Les données brutes** (journaux, activations) : non téléchargées. Je n'ai recalculé que les normes et cosinus des deux `.pt`, et relu les tables `pooled.csv` et `positions.csv`.

---

## Annexe A · Requêtes WebSearch (15, le plafond)
- R1 `"Emotion Concepts and their Function in a Large Language Model" desperate blackmail calm reward hacking Claude Sonnet 4.5`
- R2 `"Language Models Act on Hidden Valence" Berg Kaiser arXiv`
- R3 `"Functional Emotions or Situational Contexts" Mythos Preview system card arXiv 2604.13466 author`
- R4 `"Beyond Shallow Alignment" post-training methods refusal circuits steering robustness Nguyen Naseem 2609.03887`
- R5 `"Steering towards" "automated grading" degrades alignment Betley Treutlein Dumas`
- R6 `"Same Outcome, Different Readout" valence steering arXiv 2609.22850`
- R7 `Valen92 pain-adapters Hugging Face LoRA adapter Qwen2.5 7B 32B 72B`
- R8 `huggingface "Qwen/Qwen3-8B-Base" pretrained base model versus "Qwen/Qwen3-8B" post-trained thinking`
- R9 `evaluation awareness representation LLM emotion OR affect OR fear OR anxiety steering probe "evaluation awareness" 2026`
- R10 `safety fine-tuning with reasoning vs without robustness to emotion steering vector distress harmful actions state-dependent alignment LLM 2026`
- R11 `LessWrong "Study 3" "Steering welfare-relevant directions moved the representation"`
- R12 `Barenholtz "pain axis" static word embeddings GloVe fastText same specificity tests`
- R13 `"evaluation awareness" steering "desperate" OR "distress" OR "emotion vector" suppresses OR reduces evaluation awareness probe language model`
- R14 `"Steering Interference Reflects the Model's Defaults" Malla Choi arXiv 2609.06951`
- R15 `fine-tuning on reasoning traces changes emotion representations distress projection under hostile users comparison training methods interpretability 2026`

## Annexe B · Fichiers récupérés par curl (`raw.githubusercontent.com`), copies dans `travail/verif_sources_sources/`

**valen-research/Pain-axis, branche `main`**
- Racine : `README.md`, `LICENSE`, `requirements.txt`.
- `v2_controls/` : `README.md`, `ASSETS.md`, `VERIFICATION.md` (non lu en détail), `MANUSCRIPT_DISCREPANCIES.md`.
- `v2_controls/cosine_constructions/` : `README.md`, `config.json`.
- `v2_controls/figure10/` : `README.md`, `pooled.csv`, `positions.csv`.
- `v2_controls/choice_controls/` : `README.md`, `vectors/README.md`, `profile/README.md`.
- `v2_controls/relief_and_context_tests/` :
  - `README.md` ;
  - `qwen_llama_reset/README.md` et `qwen_llama_reset/inputs/prepared_v1/llama31_8b/metadata.json` ;
  - `natural_and_ending/README.md` ;
  - `factual_accuracy/README.md`, `factual_accuracy/config.json` et `factual_accuracy/results/analysis_v1/contrasts.csv`.
- `v2_controls/steering_state_controls/README.md`.
- `scripts/` : `3.2_pain_vectors/01_extract_activations_and_pain_vectors.py`, `3.2_pain_vectors/02_build_control_vectors.py`, `4.2_steering/01_steering_ladder.py`.
- `datasets/3.1_pain_and_control_datasets.json`.
- `results/3.2_pain_vectors/pain_vectors/Llama_3.1_8B_instruct/pain_vectors.pt` et `…/Qwen_3_8B_base/pain_vectors.pt`.
- `README.md` aux commits `8d1649c03a63a39c9aa092532c376800cc4a3863` et `7c256502ed3d98e4e6379290fe7db2f93cb8d025`.

**Réponses 404** :
- `v2_controls/relief_and_context_tests/factual_accuracy/contrasts.csv` et `…/results/analysis_v1/contrasts.json` ;
- `lychee888/pain-axis-steering/README.md` sur `main`, `master` et `HEAD` ;
- pour *Open Character Training*, la première adresse essayée (`maiush/OpenCharacterTraining`, `main`) a répondu ; aucune autre n'a été tentée.

**Autres dépôts** :
- jimallchin/pain-axis-replication : `README.md`, `CITATION.cff`, `PROTOCOL.md`, `paper/pain-axis-replication.pdf` ;
- clauderfly-ui/pain-axis-reanalysis : `README.md`, `results.md` ;
- wolframs/pain-axis-review : `README.md`, `SYNTHESIS.md`, `BRIEF.md`, `earlier_ai_review/pain-axis-audit/README.md` ;
- ianbarber/experiments : `README.md`, `2026-09-18-itch-axis-pain-replication/README.md` ;
- terrafying/ai-torture-chamber (`master`), glowleaf/ai-pleasure-and-pain, CtianArtist/Desire-Axis, oblivia-simplex/Pain-axis, valen-research/probing-llm-preferences, carlhenrikrolf/functional-welfare-axis, centerforaisafety/wellbeing, yetiiil/analyse-sv-safety, ukgovernmentbeis/llm-self-steering : `README.md` ;
- safety-research/assistant-axis (`master`), giordanobsf/emotion-vectors, drgzkr/EmoVecLLM (`master`), hoangcuongnguyen2001/Beyond-Shallow-Alignment, maiush/OpenCharacterTraining : `README.md`.
