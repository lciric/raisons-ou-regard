# Corrections de la carte des angles déjà pris, tour 1 (2 octobre 2026)

Fichier corrigé en place : `livrable/CARTE_ANGLES_DEJA_PRIS_2026-10-02.md` (1 193 lignes, comme avant). Les numéros de ligne renvoient à la version d'avant la correction ; ils ne bougent presque pas, puisque aucune ligne n'a été ajoutée.

Chaque correction a été vérifiée dans les rapports (`ANTERIORITE_RAPPORTS_2026-10-01.md`, `ANTERIORITE_RAPPORTS_2026-10-02.md`) ou dans la passation v1.2 (§4.2 à §4.4, §5.5).

---

## Bloquants

### 1. Statuts de lecture manquants ou hors des six libellés : corrigé

La règle appliquée est celle du §10 de la carte : quand un rapport de la nuit ne dit ni l'outil ni l'étendue de sa lecture, il reçoit « résumé seul (mode non précisé) ». Le §10 précise maintenant deux cas : la page dite « lue », sans outil ni étendue, et la date dite « vérifiée », sans source. Ce qu'un rapport n'a vu que par son titre est « non ouvert ».

| Ligne | Avant | Après | Vérifié dans |
|---|---|---|---|
| 28 | « rapport 6, non relu » (ICLR 2027) | rapport 6, résumé seul (mode non précisé). Le rapport range ces dates parmi les travaux « vus mais non ouverts » et lit `public_submissions: false` dans un résumé automatique | Rapport 6, l. 1266 et 1506 |
| 61 | « rapports 2 et 6, non relu » (Second Look) | rapports 2 et 6, résumé seul (mode non précisé) | Rapport 2, l. 429 ; rapport 6, l. 1497 |
| 175 | « rapport 2, non relu » (fiche Sonnet 4.5) | rapport 2, texte intégral des §7.6.1 à 7.6.4, figures non lues ; conclusion relue (§4.2, n° 5) | Rapport 2, l. 288 |
| 719 | *Persona Vectors* « rapport 5, mode non précisé » | rapport 5, résumé seul (mode non précisé). Statuts ajoutés aussi sur la même ligne : Drake et Eberstadt (rapport 5, résumé seul), Betley et al. (rapport 6, texte intégral) | Rapport 5, l. 1139-1140 ; rapport 6, l. 1350 |
| 726 | « rapport 5, mode non précisé » (outils) | rapport 5, résumé seul (mode non précisé) | Rapport 5, l. 1219-1226 |
| 748 | « rapport 6, « lu dans la FAQ » ; rapport 1, sans mode de lecture » | rapport 6, résumé seul (mode non précisé) ; rapport 1, résumé seul (mode non précisé), dans sa fiche du projet de Cadile ; §4.4 cité | Rapport 6, l. 1450 ; rapport 1, l. 179 ; passation l. 266 |
| 760 | CaML « Rapports 4 et 6 ; extraits » | projet SPAR : rapport 4, résumé seul (mode non précisé) ; offre d'emploi : rapport 6, résumé seul (mode non précisé) ; *Helpfulness Hurts* : vu par extrait de recherche, non ouvert | Rapport 4, l. 929-931 ; rapport 6, l. 1498 |
| 761 | Ududec « Rapport 6 (pages des flux) » | rapport 6, résumé seul (mode non précisé : « pages des flux lues à partir du plan du site ») | Rapport 6, l. 1480-1486 |
| 762 | Africa « Rapport 6 » | rapport 6, résumé seul (mode non précisé) | Rapport 6, l. 1487 |
| 764 | Salle et Imran « Rapport 6 » | rapport 6, résumé seul (mode non précisé) | Rapport 6, l. 1470 |
| 765 | Aaliyan « Rapports 2 et 4 ; extrait » | rapports 2 et 4, résumé seul (mode non précisé) ; le dépôt : vu par extrait de recherche, non ouvert | Rapport 2, l. 423 ; rapport 4, l. 937 |
| 767 | Kretschmar, dépôt « Rapport 3 » | rapport 3, résumé seul (mode non précisé) | Rapport 3, l. 672 |
| 768 | « Autres, faibles » : « Rapports 2, 3, 4, 5, 6 » | un statut par groupe : rapport 2, résumé seul (mode non précisé) pour OpenAI–Apollo, Apollo, Bharadwaj et Kirk, Epstein et Ravid ; rapport 3, résumé seul (mode non précisé) pour Resolution, et texte intégral pour Konrad et al. et Santos-Grueiro (articles lus en entier) ; rapport 4, texte intégral (Risk Report) pour « Hacker-Opus » ; rapport 5, résumé seul (mode non précisé) pour Cho et al., Nanda et al., *PreCommitLens* et les indices sur Hugging Face ; rapport 6, texte intégral (le billet) pour Betley et al. ; rapport 1, lu par un site tiers, pour 2604.18946 | Rapport 2, l. 424-430 ; rapport 3, l. 540, 555, 667-671 ; rapport 4, l. 896 et 939 ; rapport 5, l. 1169 et 1186-1194 ; rapport 6, l. 1350 et 1499 ; rapport 1, l. 186 |
| 770 | ICLR « Rapport 6, non relu » | rapport 6, résumé seul (`public_submissions: false` lu dans un résumé automatique du JSON) ; les 28 prépublications : rapport 6, non ouvertes (titres et commentaires des listes d'arXiv, pas les résumés) | Rapport 6, l. 1266, 1500 et 1566 |
| 771 | Ateliers de NeurIPS « Rapports 5 et 6 » | listes : rapport 6, non ouvertes (403, 0 résultat) ; Vaid : rapport 5, résumé seul (API d'OpenReview) ; Dabir et al. : rapports 5 et 6, résumé seul ; « en décembre » : rapport 5, résumé seul (mode non précisé) | Rapport 6, l. 1431-1432 et 1507 ; rapport 5, l. 1086, 1165 et 1195 |
| 783-786 | « Rapport 6 ; non relu » (dates d'ICLR) | rapport 6, résumé seul (mode non précisé), dates rangées par le rapport parmi les travaux « vus mais non ouverts » | Rapport 6, l. 1506 |
| 789 | MATS « Rapport 6 » | rapport 6, résumé seul (mode non précisé : « pages des flux lues ») | Rapport 6, l. 1480 |

Corrigés dans la même passe, de même nature, hors de la liste de la critique :
- l. 755 (Cadile) : « rapport 1 » sans libellé devient « rapport 1, résumé seul (mode non précisé) ».
- l. 763 (Ivanov) : « rapports 2, 3, 4 » sans libellé devient « rapports 2, 3 et 4, résumé seul (mode non précisé) ».
- l. 758 (Cody Wild) : « mode non dit » devient « mode non précisé ».
- l. 784, 787 et 788 (dates de SPAR et des ateliers) : le rapport 1 et le rapport 5 reçoivent leur libellé.
- l. 773 (projets non retenus) : un statut commun, « rapports 1, 2, 4 et 6, résumé seul (mode non précisé) ».
- l. 373 (Nakamura) : « d'après le rapport 3 » devient « rapport 3, texte intégral » (rapport 3, l. 568).
- l. 549 (Cho et al.) : « rapports 1 et 7 » et « rapport 7 » reçoivent « texte intégral » (rapport 1, l. 104 ; rapport 7, l. 1759-1760).
- l. 685 et 687 (tableau de l'anatomie) : statuts ajoutés pour Betley et al., Sinha et al., Heidari et al. et *Beyond Shallow Alignment*.
- l. 725 et 727 : Dabir et al. (rapport 6, résumé seul), Cho et al. et *Open Character Training* (rapport 5, résumé seul, mode non précisé).
- l. 1067 (§8) : « mode de lecture non précisé » devient « résumé seul (mode non précisé) ».
- l. 1080 (§8) : « un rapport chacune » devient rapport 2, texte intégral (Opus 4.7), et rapport 4, texte intégral par pdftotext (Fable 5).

**Écart avec l'exemple de la critique, et sa raison.** Pour Ududec et Africa, la critique proposait « rapport 6, texte intégral ». J'ai écrit « résumé seul (mode non précisé) ». Le rapport 6 dit seulement « pages des flux lues à partir du plan du site » (l. 1480), sans outil ni étendue. Or le §10 de la carte, que la critique invoque elle-même pour les l. 719 et 726, attribue ce libellé à ce cas. La citation qu'il donne (« By changing these cues… ») ne prouve pas une lecture entière : WebFetch rend aussi des citations dans ses résumés (rapport 7, l. 1578). Le même libellé vaut pour la FAQ de SPAR (« lu dans la FAQ ») et pour MATS. Le bloquant est levé dans les deux cas : chaque fait a un libellé admis.

### 2. Faute d'attribution, Ududec (l. 761) : corrigé

Le rapport 6 (l. 1486) écrit « moyen à faible (dépendance au regard, survie) ». L'amplification vient du vérificateur de l'amplification (`verif_angle_amplification.md`, n° 7), qui demande un niveau sans le fixer. Nouvelle cellule : « Dépendance au regard, survie : moyen à faible (rapport 6). Amplification : même niveau, estimation de la carte, provisoire ; le rapport 6 ne nomme pas cet angle. »

### 3. Citation de plus de quinze mots (l. 604) : corrigé

Les 25 mots repris du rapport 4 (l. 776) sont remplacés par la formule du §4.4, n° 7 entre guillemets, soit 10 mots : « modèle de récompense qui voit le raisonnement contre réponse seule ». Suit une paraphrase sans guillemets : dans la variante où ce raisonnement verbalise l'évaluation, et où l'on suit, point de contrôle par point de contrôle, si la conduite tient quand la verbalisation disparaît. Sources citées : rapport 4, texte intégral des scripts de la phase 5 (l. 755 et 766-771).

Contrôle fait sur toute la carte par un script. Les seuls passages de quinze mots ou plus entre guillemets sont les formulations « to our knowledge » du §7 (texte de la carte, pas des citations) et la formule de la carte au §7 « montré par ses auteurs sur Claude… ». Pour éviter toute confusion, la l. 381, formulation propre de la carte en 17 mots, a perdu ses guillemets.

---

## Mineurs

1. **l. 561, *Alignment midtraining for animals*** : corrigé. Chaque morceau a maintenant sa source.
   - Les 3 000 documents et le témoin neutre : rapport du 1er octobre (raisons contre actions), texte intégral de la v1 (l. 67-68).
   - Le 77 % contre 40 % : ce rapport et le rapport 1, résumé seul, mode non précisé (l. 165).
   - « S'efface après un SFT ultérieur » (rapport du 1er octobre) et « après un tuning sans rapport » (rapport 1).
   - Les 5 000 échantillons : rapport 4, résumé seul, page abs (l. 891-893).
2. **l. 274, *Agentic Misalignment in Summer 2026*** : corrigé.
   - Les auteurs et la date du 13 juillet : rapport 1 (l. 171), résumé seul, mode non précisé.
   - « Juillet 2026 » : rapport 2 (l. 390), résumé seul, mode non précisé.
   - Le rapport 6 (l. 1325-1326) ne relève pas les auteurs.
   - Le contenu : §4.3, d'après les rapports 2 et 6.
3. **l. 230, Read et al.** : corrigé. Le statut devient « rapport 2, texte intégral par l'API markdown de LessWrong, lu en partie » (rapport 2, l. 345 : « via l'API markdown, partiellement »).
4. **l. 681 et 993, la charge** : corrigé. Le renvoi au §7 disparaît. Le résultat est rattaché à l'article sur l'espace de travail global, hors du §7 : le rapport 5 (l. 1026) compte l'annexe sur la charge parmi ses sections lues. La l. 993 cite désormais l'article pour la charge et les échanges.
5. **l. 1041, Kaufmann et al.** : corrigé. Le §5.5, n° 9 ne cite qu'exp9 pour cette formulation (passation, l. 394). La ligne devient : exp9 (relu ; §5.5, n° 9) ; Kaufmann et al. (rapport 4, résumé seul, l. 854 ; cités au §5.5, n° 8, parmi les travaux à ajouter, l. 382).
6. **l. 850, 2606.08629** : corrigé.
   - Seul le rapport 6 dit « spotlight » (l. 1382, résumé lu).
   - Le rapport 2 ne donne que « ICML 2026, résumé » (l. 375).
   - Le rapport 7 (l. 1814-1820) ne donne aucun lieu. La remarque sur le §4.3, qui range ce lieu sous le rapport 7, reste donc juste et est conservée.
7. **Contenus lus par curl par des agents ou des vérificateurs** : corrigé.
   - l. 400 : le contenu prêté au README d'*Inoculate or Reflect?* est retiré. Restent « à relire par l'instance du papier » et le chemin `raw.githubusercontent.com/Ayesha-Imr/inoculate-or-reflect/main/README.md`, que j'ai repris de `verif_angle_anatomie.md`, l. 21.
   - l. 603 : la figure de trajectoire attribuée à `results/` est retirée. Restent « à relire par l'instance du papier, en priorité », avec le dépôt.
   - l. 697 : le rattachement à BlackboxNLP 2026 est retiré. Restent « à relire » et un renvoi au §3.4, n° 5.
   - l. 881 : le chiffre 154 contre 144 est retiré. Reste un renvoi neutre aux fichiers à recontrôler, sans contenu ni chiffre.
   - l. 1095 (§8), même nature, hors de la liste : la question « les trajectoires sont-elles un résultat final ? » supposait le contenu de la figure. Elle devient « des résultats des deux DPO y sont-ils publiés ? ». Les chemins de `results/` restent comme pointeurs, présentés comme « signalés par des agents ».
   - Conservée comme repère de surveillance : l'empreinte de SUMMARY.md (l. 753 et 1139). La l. 753 la présente comme telle, sans statut de lecture et sans contenu. La citation « research in progress » y est attribuée au rapport 4, résumé seul (mode non précisé), puisque le rapport 4 ne dit pas comment il a lu le README. Que le README fasse une ligne est relu (§4.2, n° 1).
   - Le §10 (l. 1134) dit maintenant que ne restent de ces lectures que l'empreinte et des chemins de fichiers à relire.
8. **l. 752, Lundqvist et Palaestra Research** : corrigé. Ajout de « vu par extrait de recherche, non ouvert ».
9. **l. 109 et 911, ICML 2025** : corrigé. Sources nommées :
   - le rapport du 1er octobre (raisons contre actions), texte intégral (HTML v2 d'arXiv), selon la règle de l'adresse du §10 (l. 19) ;
   - le rapport 5, résumé seul, mode non précisé (l. 1174) ;
   - le lieu n'est pas relu par l'instance du papier.
10. **PDF de la carte** : non fait, hors du périmètre de ce tour, comme le dit la critique. Le §6, point 3 de la passation demande la carte en markdown et en PDF. Le PDF reste à produire à l'assemblage, après le dernier tour de correction.

---

## Refusé ou laissé en l'état, avec la raison

- **« Texte intégral » pour Ududec et Africa** (exemple du bloquant 1) : non repris. Raison donnée plus haut : le §10 de la carte, et l'absence d'outil comme d'étendue dans le rapport 6.
- **Qiyao Wei, « rapport 2, texte intégral »** (l. 252 et 769), non relevé par la critique : laissé. Le rapport 2 (l. 404) donne l'adresse du document complet, la proposition d'une page en PDF. C'est le cas de la règle de l'adresse que le §10 applique déjà.
- **Lundqvist, « rapport 6, texte intégral »** (l. 460 et 752), non relevé : laissé, pour la même raison (adresse de la page, rapport 6, l. 1461). La page est de toute façon relue par l'instance du papier et lue en texte intégral par le rapport 4.
- **Les chemins `results/plots_v5/`, `results/analysis/summary_v4.txt`, `results/eval_v5/`** (§8) : gardés comme pointeurs de relecture, comme la critique l'admet (« avec le chemin du fichier »). Ils sont marqués comme signalés par des agents.
- **Le niveau « moyen à faible » donné par la carte à Ududec pour l'amplification** : gardé, mais marqué comme estimation de la carte et provisoire, sans l'attribuer au rapport 6. Fixer un autre niveau sortait de la correction demandée.

## Ce qui ne change pas

Les décisions du 2 octobre restent telles que la carte les écrit, et elles concordent avec la demande relayée de Lazar :
- le pré-enregistrement sous son nom seul, avec son ORCID, et Claude cité dans une phrase de méthode, pas comme auteur (§5) ;
- pas de contact avec Cadile ni Lundqvist pour l'instant (§4 et §5).
