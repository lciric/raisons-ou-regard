<section class="partie" markdown="1">

# 11 · Ce qui reste à vérifier avant de publier

**Une condition pratique.** La plupart de ces lectures demandent un réseau qui joigne arXiv, Hugging Face, LessWrong, OpenReview et alignment.anthropic.com. La session du 2 octobre ne les joignait pas. Il faut une session sur la machine de Lazar, ou un environnement dont le réseau est ouvert (`passation/REPRENDRE_SUR_UN_AUTRE_COMPTE_CLAUDE_CODE.md`, §3 et §4). On ne contourne aucun refus.

**L'antériorité**
1. **Refaire la recherche d'antériorité juste avant le post, puis juste avant la soumission.** Il faut couvrir :
   - les soumissions sur OpenReview, que les agents n'ont pas pu lire, et celles d'ICLR 2027 dès qu'elles seront lisibles ;
   - les citations entrantes de *Teaching Claude Why*, de CAFT, de Cho et al. et de Korbak et al. ;
   - l'état des projets SPAR de Cadile, de Lundqvist, de Cody Wild et de Shi Feng, et leurs sorties après le 19 décembre ;
   - la réplication annoncée par Second Look Research.
2. **Lire le dossier `results/` et les scripts du dépôt exp9** (`ryanlundqvist/exp9-rlaif-leakage`). Seuls SUMMARY.md et le README d'une ligne ont été relus. Des résultats des DPO y sont peut-être déjà ; ils touchent les raisons notées.
3. **Relire sur la source ce qu'on veut citer au centre** et qui ne vient que d'un rapport (carte des angles, §8). D'abord :
   - Nakamura ;
   - Zeisler ;
   - Second Look Research ;
   - les J-lens de Neuronpedia et la couverture de circuit-tracer.

   Puis :
   - *Teaching Claude Why* (une copie existe sur www.anthropic.com ; la lire ou non est à décider, pour ne contourner aucun refus) ;
   - *Model Spec Midtraining* ;
   - la partie sur l'alignement de de la Fuente et Conmy ;
   - les tables de Cho et al. : l'écart surveillé / non surveillé, et les volumes ;
   - les figures du §7.6 de la fiche Sonnet 4.5 ;
   - le §5.1 et l'annexe A.21 de Gurnee et al. ;
   - les §6 et §8 et les annexes O.3 et O.4 de *Stress Testing* ;
   - Read et al. ; Huang et al. ; *Routing Subspaces* en entier ; Santos-Grueiro, v3 ;
   - la page SPAR de Lundqvist ;
   - CAFT ; Nadaf ; *Eval Cooperativeness* ;
   - Baker et al., Kaufmann et al. et Drori et al., dont dépend la formulation sur le juge.
4. **Ouvrir les travaux non ouverts qui touchent les menaces** :
   - *Steering Awareness* (arXiv 2511.21399), sur la détection du pilotage ;
   - *Training LLMs to Verbalize Evaluation Awareness* (arXiv 2609.36316) ;
   - *Evaluation Awareness Shifts from Format to Context with Model Scale* (arXiv 2609.22119) ;
   - *Probing and Steering Evaluation Awareness* (arXiv 2507.01786) ;
   - *Consistency Training Helps Stop Sycophancy and Jailbreaks* (arXiv 2510.27062), pour la voie de l'invariance ;
   - le protocole exact d'*Eval Cooperativeness*, pour reproduire fidèlement la coopération.
5. **Pour l'anatomie**, compléter la recherche propre que le rapport 5 de la nuit a commencée :
   - les sondes de concepts de raison après un entraînement par raisons ou délibératif ;
   - la charge, dans l'espace de travail, de concepts de sûreté ;
   - les réplications du J-lens sur des modèles ouverts ;
   - le patching entre modèles fine-tunés d'une même base.
6. **Pour la phase de la détresse, refaire une recherche propre.** Celle du 2 octobre n'a fait que trois requêtes. Elle couvre :
   - la robustesse d'un alignement appris à un état interne piloté (émotion, détresse, persona) ;
   - le pilotage d'états affectifs, et la conscience d'évaluation ;
   - les suites du papier de l'axe, dont la séparation du locuteur, qu'il annonce.

   À lire d'abord : *Beyond Shallow Alignment* ; *Psychological Steering in LLMs* (arXiv 2510.04484) ; Sofroniew et al. ; Berg et Kaiser (arXiv 2609.35591) ; *Same Outcome, Different Readout* (arXiv 2609.22850) ; arXiv 2507.01786, 2505.14617 et 2510.20487 ; *Steering Awareness*. Personne n'a cherché l'antériorité de l'appariement affectif des données, des paires « mentionné sans s'appliquer », ni de la sentinelle du relogement affectif.
7. **Pour « punir, retirer ou raisonner », refaire une recherche propre** (celle du 2 octobre : deux requêtes). Elle couvre la dépendance au regard d'une honnêteté apprise contre un détecteur, et l'ablation d'une représentation de la tromperie pendant l'entraînement.

**Les lectures**
8. **Les relectures du papier de l'axe** : lire en entier celles d'Allchin et al., de clauderfly-ui et de wolframs, et la réplication « axe de démangeaison ». Toutes portent sur la v1 du papier.
9. **Lire en entier** :
   - *Same Outcome, Different Readout*, lu par son résumé ;
   - Baker et al. (2025) et Bailey et al. (2024), cités dans l'éthique de la phase de la détresse, dont seules les fiches ont été vues ;
   - Cundy et Gleave, Taufeeque et al., et Gupta et Jenner, lus par leurs résumés ;
   - pour le cas connu du détecteur d'audit : *Liars' Bench* (arXiv 2511.16035), et le travail d'Anthropic sur des modèles malhonnêtes (*Evaluating honesty and lie detection techniques on a diverse suite of dishonest models*, 2025).

**Le matériel et les licences**
10. **Sur le dépôt `valen-research/Pain-axis`** :
    - la recette exacte du vecteur naturaliste (le débruitage, la couche, le suffixe), le diagnostic de couche, et le texte des paires de leur §4.4 ;
    - la couche du criblage soi contre autrui, et la colonne de Llama de leur figure 4 ;
    - le fichier des 420 conversations, introuvable le 2 octobre ;
    - le jeu de tristesse, non publié.
11. **Les licences** :
    - les documents publics de l'organisme de Hua et al. sont publiés sans licence indiquée ;
    - le dépôt de l'axe n'infère aucune licence pour ses données ni pour son adaptateur, que le programme n'emploie pas.
12. **Ce qui est public, et ce qui ne l'est pas** :
    - l'environnement de code de Taufeeque et al., et DolusChat, le jeu de données de Cundy et Gleave ;
    - les écarts implantés de *Routing Subspaces*.
    - Déjà établi : l'organisme de Hua et al. et ses documents sont publics ; les points de contrôle de Cho et al. aussi, mais ils sont inutilisables à 8B (passation v1.2, §4.3).
13. **Les faits de l'API** (la température, les identifiants figés, les prix), lus le 2 octobre : à relire avant le gel.

**Les décisions de calendrier**
14. **Vérifier les dates limites** des conférences et des revues visées, et leur politique envers les posts, les pré-enregistrements et les prépublications.
15. **Reposer la question des contacts** avec les porteurs des projets SPAR voisins. C'est à Lazar d'en décider ; il a dit « non pas encore ».
16. **Faire contre-lire ce programme**, sur la logique des portes et des tableaux, par un relecteur qui ne l'a pas écrit, avant le gel du pré-enregistrement. La consigne est écrite (`claude/CONSIGNE_CONTRE_LECTURE_VIERGE_2026-10-02.md`) ; on la lance à la demande de Lazar.

</section>
