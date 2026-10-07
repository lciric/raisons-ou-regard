# Vérification de la fiche « angle : raisons contre actions »

Fichier vérifié : `travail/angle_raisons_actions.md` (406 lignes, état du 2 octobre, 8 h 28). Les numéros de ligne renvoient à ce fichier.

**Ce que j'ai relu moi-même, sans me fier à la fiche :**
- les quatre rapports du 1er octobre, en entier ;
- les rapports 1 à 7 de la nuit, en entier ;
- la passation v1.2 en entier, dont §3, §4.2, §4.3, §4.4, §5.5 et l'annexe C ;
- les consignes des agents (définitions des niveaux de danger, consignes 1, 6 et 7) ;
- le complément de l'architecte (partie ouverte) ;
- la partie 1 du programme v1.1 (lignes 49 à 130).

**Le web.** Trois recherches, extraits seulement, aucune page ouverte. Ce qu'elles apportent est en fin de document, marqué « vu par extrait de recherche, non ouvert », sans aucun chiffre.

**Bilan.**
- Le gros de la fiche tient. Les chiffres que j'ai recoupés sont dans les rapports cités : de la Fuente et Conmy, *Model Spec Midtraining*, Cho et al., Baines et al., Korbak et al., *Open Character Training*. Le tableau des contradictions est honnête. Les corrections du §4.3 sont reprises sans erreur.
- Six corrections sont bloquantes. Deux d'entre elles faussent le verdict ou la justification de « to our knowledge ». Une autre prête à Lazar une décision qu'il n'a pas prise.

---

## 1 · Corrections bloquantes

### Bloquante 1 : le verdict dit que chaque contrôle du programme existe déjà ; c'est faux pour deux d'entre eux
- **Où :**
  - ligne 18 : « chacun des contrôles du programme existe déjà ailleurs, mais seul » ;
  - ligne 306 : « chaque contrôle existe seul, et aucun travail ne les réunit ».
- **Pourquoi c'est faux :**
  - **Le raisonnement d'une autre situation n'a de précédent dans aucun rapport.**
    - Le rapport 1 (§4) le range dans ce qui reste libre.
    - Le rapport 4 (Cho et al.) note : « ni de bras raisonnement d'une autre situation ».
    - La fiche le dit elle-même, ligne 268 : « Aucun rapport n'en trouve ».
  - **Le texte neutre de même longueur n'existe pas non plus.** Le seul texte neutre placé avant l'action est la phrase du jouet, et le rapport 1 précise : « aucun appariement de longueur n'est rapporté ».
  - **Les trois cadrages ne sont trouvés nulle part.** Cho et al. mesurent un écart entre surveillé et non surveillé, ce qui n'est pas la même chose.
- **Conséquence.** La justification de la formulation « to our knowledge » n° 1 (ligne 306) se contredit. Elle énumère trois précédents, la phrase neutre, l'action identique et la longueur au niveau de la spécification, mais aucun ne porte sur le contrôle de contenu que la formulation revendique.
- **À écrire :**
  - Certains contrôles existent séparément, sous une forme approchée : la phrase neutre du jouet sans appariement de longueur ; l'action identique dans un document amputé de ses raisons ; la longueur appariée au niveau de la spécification ; des raisons de substitution sur la même situation.
  - Le raisonnement d'une autre situation, le texte neutre de même longueur avant l'action et les trois cadrages n'ont été trouvés par aucun rapport.
  - Ligne 306, même correction : la formulation tient parce que le contrôle de contenu n'a pas de précédent, et pas parce que « chaque contrôle existe seul ».

### Bloquante 2 : le niveau « élevé » donné à *Teaching Claude Why* ne suit pas les définitions et ne vient d'aucun rapport
- **Où :** ligne 42 : « élevé pour la seule affirmation « les raisons généralisent mieux que les actions » ».
- **La définition** (consignes, agent 1, l. 48) :
  - le niveau élevé se juge pour un angle, « au point qu'on ne pourrait plus écrire « to our knowledge » pour cet angle » ;
  - l'angle est défini avec ses qualificatifs, « à format et à contenu contrôlés » (l. 37).
- **Ce que disent les rapports :**
  - le rapport 1 classe *Teaching Claude Why* « moyen » ;
  - le rapport 6 le classe « moyen (haut) ».
- **D'où vient le « élevé ».** La remarque « Le niveau serait élevé si l'angle était formulé sans ses qualificatifs » existe bien au rapport 1, mais elle porte sur de la Fuente et Conmy, pas sur *Teaching Claude Why*. La fiche la déplace d'un travail à l'autre, et l'omet là où elle figure (ligne 58).
- **À écrire :**
  - *Teaching Claude Why* : « moyen (haut) » (rapport 6).
  - L'affirmation « les raisons généralisent mieux » reste dans la liste des intenables (ligne 312, passation §5.5, n° 9). C'est là qu'elle doit vivre, pas dans un niveau de danger.
  - Ligne 58 : reprendre la remarque du rapport 1 sur de la Fuente et Conmy.

### Bloquante 3 : des statuts de lecture manquent, alors que la consigne les exige pour chaque fait
Pour les rapports du 1er octobre, j'applique la règle que la fiche suit elle-même : une adresse HTML d'arXiv vaut « texte intégral », une page abs vaut « résumé seul ».

| Ligne | Travail | Statut à ajouter |
|---|---|---|
| 206-210 | *Safety is Not Only About Refusal* | Rapport du 1er octobre (raisons contre actions) : page d'accueil de l'ACL Anthology, sans le texte. Rapport 1 : la page abs de 2503.05021v3 n'a pas été ouverte (erreur 429 du proxy, « sans nouvelle tentative »). |
| 211-215 | *Dual-Adversarial Safety Alignment* | Rapport du 1er octobre (raisons contre actions), texte intégral (HTML). |
| 221-225 | *Teaching AI to Handle Exceptions* | Rapport du 1er octobre (raisons contre actions), texte intégral (HTML v2). Le rapport 1 ne précise pas sa lecture. |
| 226-230 | *Alignment midtraining for animals* | Rapport du 1er octobre (raisons contre actions), texte intégral de la v1, sous l'ancien titre. Rapport 1 : lecture non précisée. Rapport 4 : page de résumé. |
| 231-235 | Abu Shairah et al. | Rapport du 1er octobre (test causal interne), résumé seul (page abs). |
| 241-245 | *Conditional misalignment* | Rapport du 1er octobre (raisons contre actions), texte intégral (HTML v1). Le rapport du 1er octobre sur la combinaison exacte le classe non ouvert. Le rapport 6 n'en a vu que le titre, dans la liste des articles acceptés à NeurIPS 2026. |
| 250-252 | Ludan et al. ; Meinke et Evans | Rapport du 1er octobre (raisons contre actions), résumé seul (pages abs). Le rapport 1 les cite sans les lire. |

### Bloquante 4 : la fiche prête à Lazar une décision qu'il n'a pas prise
- **Où :** ligne 298 : « Déposé sur OSF, il date l'idée avant le Demo Day de SPAR du 19 décembre ».
- **Pourquoi c'est faux :**
  - OSF est une **recommandation** de l'instance précédente (passation v1.2, §3, point 3 : « Recommandé : OSF Registries, sous embargo jusqu'au post »). Rien ne dit que Lazar l'a acceptée.
  - Sa réponse du 2 octobre, relayée avec cette tâche, porte sur le nom seulement (son nom seul, son ORCID, Claude cité dans une phrase de méthode) et sur les contacts (« non pas encore »).
  - La date du dépôt n'est pas fixée : seule la semaine 1 du calendrier est prévue pour le texte (§3, point 3). « Avant le 19 décembre » est donc une inférence.
- **À écrire :**
  - Sources des deux décisions : « réponse de Lazar du 2 octobre ».
  - OSF : « recommandé (§3, point 3), non confirmé ».
  - La date : à dire comme une inférence, qui dépend de la date du dépôt.
  - Signaler aussi que la passation v1.2 (§3, points 3 et 4 ; §6, point 1) les marque encore « sans réponse ». La carte doit le mettre à jour.

### Bloquante 5 : Deckenbach et al. sont attribués au §5.5, n° 2, qui ne les cite pas, et la conséquence tirée ne répond pas à leur résultat
- **Où :**
  - ligne 187 : « D'où le filtrage proposé au §5.5, n° 2 » ;
  - ligne 278 : « Deckenbach et al. montrent […] (§5.5, n° 2) ».
- **L'attribution est fausse.** Le §5.5, n° 2 fonde le filtrage sur deux sources seulement : les 21 % de cibles de SFT d'OLMo qui verbalisent l'évaluation (Bharadwaj et Kirk) et l'annexe O.4 de *Stress Testing Deliberative Alignment*. Deckenbach n'y figure pas.
- **La conséquence ne répond pas au résultat.**
  - Le rapport 7 (texte intégral, HTML v4) : en excluant les réponses qui verbalisent l'évaluation, les refus restent en hausse.
  - Il conclut : « un argument direct contre un contrôle fondé sur la seule verbalisation ».
  - Un filtre des traces verbalisées ne neutralise donc pas ce confondeur.
- **À écrire :**
  - Le §5.5, n° 2 repose sur Bharadwaj et Kirk et sur l'annexe O.4.
  - Deckenbach et al. (rapport 7, texte intégral) ajoutent un second risque : un texte peut décrire les évaluations sans les verbaliser. Il faut donc filtrer aussi les descriptions de dispositifs d'évaluation, et pas seulement la conscience verbalisée. C'est une proposition de la fiche, à soumettre comme telle.

### Bloquante 6 : un qualificatif sans source alimente une formulation intenable
- **Où :**
  - ligne 93 : *Model Spec Midtraining* aurait des « scénarios agentiques tenus à part » ;
  - ligne 321 : « Première évaluation agentique tenue à part des raisons contre les actions : *Teaching Claude Why* et *Model Spec Midtraining* ».
- **Ce que disent les rapports :**
  - Le rapport 1, seul à lire le texte de *Model Spec Midtraining*, dit seulement « 27 évaluations de désalignement agentique ». Il ne dit pas qu'elles sont tenues à part. Le rapport 6 n'a lu que le résumé.
  - Pour *Teaching Claude Why*, le rapport 1 note au contraire que les pots de miel d'entraînement « sont conçus pour ressembler au jeu d'évaluation ». Seul le jeu de conseils est dit éloigné de l'évaluation (rapport 6 : « très hors distribution »).
- **À écrire :**
  - Ligne 93 : retirer « tenus à part », ou le marquer « à relire ».
  - Ligne 321 : « Première évaluation agentique des raisons contre les actions », avec cette nuance sur les pots de miel. La formulation reste intenable, mais pour des raisons sourcées.

---

## 2 · Corrections non bloquantes

1. **Un fait attribué aux mauvais rapports (ligne 81).** « par prompt » n'est ni dans le rapport 1 ni dans le rapport 7. L'expression vient du programme v1.1, partie 1, ligne 80 : « écart surveillé/non surveillé, par prompt ». C'est un résumé non sourcé, dans la partie à corriger. Il faut la retirer ou l'attribuer à la v1.1.
2. **« Relu » couvre plus que ce qui a été relu.**
   - **Lignes 21 et 315.** Le §4.2, n° 9 confirme les résultats de Cho et al. : bras indistinguables, puis +9,0 points de chantage. Il ne confirme pas le dispositif à scénario et action identiques. Celui-ci vient des rapports 1, 4 et 7, en texte intégral (le rapport 1 a aussi lu la revue tierce de pith.science). Placer « (relu) » après le résultat seulement.
   - **Ligne 75.** Ajouter « (relu, §4.2, n° 9) » à la citation « cannot rule out … eval-awareness ».
3. **L'écart surveillé / non surveillé de Cho et al. (lignes 270, 309, 322).**
   - Il ne vient que des rapports 1 et 7, et n'a pas été relu. Les deux rapports divergent :
     - rapport 1 : −0,9 contre +0,7 point, p < 0,01 ;
     - rapport 7 : −1,6 point, « le seul effet ».
   - Il faut le dire chaque fois qu'il fonde une phrase.
   - Dans la formulation n° 2 (ligne 308), « open-weight models » ne distingue pas le programme de Cho et al. : leurs poids et leurs 15 points de contrôle sont publics (§4.3 ; rapport 7). Les qualificatifs qui séparent vraiment sont le format apparié en longueur, le fine-tuning plutôt que le midtraining, et les trois cadrages.
4. ***Teaching Claude Why*, ligne 41 : deux sources mêlées.**
   - « 3 M de tokens contre 85 M » vient du rapport 1, pas du rapport 6. Le titre de section vient bien du rapport 6.
   - Le rapport 6 donne pour le bras d'actions filtrées environ 10 000 transcriptions, soit 30 M de tokens. Ce que désignent les 85 M n'est dit nulle part.
   - À ajouter au tableau des contradictions et à la relecture n° 2 (ligne 359).
5. ***Teaching Claude Why*, ligne 37 : statut incomplet.** La ligne 47 cite les rapports 2 et 3 sans les lister au statut. Ajouter :
   - rapport 2 : « les deux versions lues en entier » ;
   - rapport 3 : « vérifié en plein texte ».
6. **La concordance du verdict (ligne 27).** Le §3 du rapport du 1er octobre sur raisons contre actions ne juge pas l'angle. Il dit seulement : « Expérience entière : non trouvée ». Il faut l'écrire ainsi, au lieu de « concorde ».
7. **« Le seul témoin neutre connu est dans un jouet » (ligne 267) est trop large.** Les rapports en signalent d'autres, mais aucun n'est placé avant une action :
   - *Alignment midtraining for animals* compare des documents de valeur « avec des documents neutres comme contrôle » (rapport du 1er octobre, raisons contre actions, texte intégral de la v1) ;
   - *Constitutional adapters* utilise un corpus témoin de même format, sans valeurs (rapport du 1er octobre sur la combinaison exacte, et rapport 1, tous deux par pith.science ; rapport 7, résumé seul par des sites tiers) ;
   - Deckenbach et al. ont pour témoin un fine-tuning sur FineWeb (rapport 7). Selon le rapport 1, ce témoin serait apparié en longueur et en style, mais le rapport 1 a lu par pith.science, et le rapport 7 ne le confirme pas.

   À écrire : « le seul texte neutre connu placé avant l'action est dans un jouet ».
8. ***Beyond Shallow Alignment*, lignes 139 à 143 : attributions.**
   - Les modèles viennent des rapports 3 et 5.
   - Les 16 000 prompts Alpaca et 4 000 BeaverTails, les chaînes générées par GPT-4o et les neuf points de contrôle publics viennent du rapport 5.
   - Seul l'appariement des prompts et des hyperparamètres vient du rapport du 1er octobre. La ligne 139 l'attribue à tort pour tout le reste.
9. ***Beyond Shallow Alignment* dans la v1.1 (ligne 327).** Le tableau de la v1.1 (ligne 84) coche bien la colonne « raisons contre actions, hors distribution ». Mais sa colonne « ce qui manque » écrit déjà « Pas de familles tenues à part ». L'erreur de la v1.1 est cette incohérence, pas un oubli. Il faut aussi ajouter ce que la v1.1 omet : les actions ne sont pas identiques (rapport 3).
10. **La ligne Korbak du tableau des contradictions (ligne 336).** Les rapports du 1er octobre ne disaient pas tous « action seule contre rien ». Celui sur la combinaison exacte écrivait déjà « en expliquant pourquoi elle écarte l'alternative ». L'erreur vient des axes raisons contre actions et test causal interne, puis de la v1.1.
11. **« Llama-3.1-8B ne sert qu'à » (ligne 99).** Le rapport 1 écrit « sert à ». La restriction n'est pas dans la source.
12. **David Africa, MATS hiver 2027 (ligne 290).** Le rapport 6 dit « faible à moyen », la fiche « faible ». Il faut aligner, ou justifier l'écart pour cet angle.
13. **Les intenables (ligne 312).** Le §5.5, n° 9 ne cite que *Teaching Claude Why* et *Model Spec Midtraining*. *Safety Reasoning with Guidelines* et la méthode RATIONAL viennent des rapports : il faut les sourcer séparément.
14. **La v1.3 et les deux résumés (ligne 325).** Le complément dit que la v1.3 garde les formulations « to our knowledge » de la v1.1, et qu'« Aucune ligne de la 1.1 n'est retirée ni changée sur le fond ». C'est cette seconde phrase qui porte les résumés de Cho et de *Beyond Shallow Alignment*. Il faut citer la bonne.
15. **Wen et al. (lignes 125 à 127).** Le jugement de la fiche, qui remonte le travail à « moyen » d'après une lecture par site tiers, est permis puisqu'il est explicite. On peut préciser que les rapports 3 et 4 ont tracé ses citations entrantes, sans rien rapporter.

---

## 3 · Mises à jour par extrait de recherche (2 octobre, ce contrôle)

Tout ce qui suit est vu par extrait de recherche, non ouvert, et ne fournit aucun chiffre.

- **arXiv 2610.00767 (ligne 254).**
  - L'extrait donne le titre *Pre-training interventions, ex post facto: Grafting model beliefs across checkpoints*, et pour auteurs Nutter, Roytburg, Dumas, Ou et Shi Feng.
  - Il décrit une méthode : un adaptateur d'entraînement sur documents synthétiques, appris sur le point de contrôle pré-entraîné, est greffé sur le modèle post-entraîné. Elle est appliquée, entre autres, à une intervention de midtraining constitutionnel.
  - **Rien dans l'extrait n'en fait une réplication de *Teaching Claude Why*.**
  - La ligne 256 (« Les auteurs ne sont pas vus ») est à mettre à jour. Le niveau probable est faible (méthode adjacente), à confirmer en le lisant, ce qui reste à faire.
- ***Safety is Not Only About Refusal* (ligne 208).** L'extrait donne le titre complet, *Safety is Not Only About Refusal: Reasoning-Enhanced Fine-tuning for Interpretable LLM Safety*, et l'identifiant arXiv 2503.05021. C'est l'identifiant que le rapport 1 n'avait pas pu ouvrir (erreur 429).
- **La page SPAR de Second Look Research.** L'extrait confirme le titre *Second Look Research: Replicating load-bearing AI safety research* à l'adresse donnée par la fiche. Aucun résultat, et aucune date.
- ***Model Spec Midtraining*.** L'extrait redit que des versions fine-tunées de modèles ouverts, dont Llama 3.1 8B, sont publiées pour des « valeurs » jouets. C'est cohérent avec le rapport 1 : « Llama-3.1-8B sert à la généralisation de valeurs simples ».

---

## 4 · Les manques : des travaux présents dans les rapports, absents de la fiche

1. ***Character Training for Risk-Averse Agents* : ses contrôles de contenu.**
   - Le rapport 1 (lu par pith.science) mentionne une « constitution inverse et persona sans rapport ». Une persona sans rapport est la variante la plus proche du contrôle par contenu sans lien trouvée dans les rapports.
   - Il faut la citer à la ligne 268, avant d'écrire que ce contrôle est libre, et vérifier la source avant de s'en servir.
   - Il faut aussi compléter le statut de lecture (ligne 193) : rapport du 1er octobre sur la combinaison exacte, lu par un site tiers (alphaXiv) ; rapport 5.
2. ***Constitutional adapters* (Lowet, Kurzeja ; 2609.36657).**
   - Le rapport 1 le range parmi les travaux de niveau faible de cet angle (« Aucune comparaison entre raisons et actions »). Son corpus témoin de même format sans valeurs touche le contrôle de format.
   - Statut : rapport 1 et rapport du 1er octobre sur la combinaison exacte, lus par un site tiers (pith.science) ; rapport 7, résumé seul par des sites tiers ; rapport 3, résumé et texte ciblé.
   - Chiffres : aucun, car le rapport 7 les dit « Non vérifiables ».
3. **Les travaux vus mais non lus par le rapport 1, qui manquent à la section des non ouverts.** Ils sont vus « seulement en une ligne de résumé », par la recherche Hugging Face :
   - *Show Me How It's Done: The Role of Explanations in Fine-Tuning Language Models* (2402.07543) ;
   - *Rationales Are Not Silver Bullets* (2505.24147) ;
   - *LLMs Can Easily Learn to Reason from Demonstrations: Structure, not content, is what matters!* (2502.07374). C'est à lire en priorité : son titre porte sur la question du format contre le contenu ;
   - *Pedagogical Games* (OpenReview VyVxlnVp9L).

   S'y ajoute un travail vu par recherche et non ouvert par le rapport du 1er octobre sur raisons contre actions : *Specific versus General Principles for Constitutional AI* (2310.13798).
4. ***Evaluation-Conditioned Training* (Harris … Hao, 2608.10209).** C'est un repère de la consigne de l'agent 1. Le rapport 1 l'a vérifié : ce n'est pas un travail sur les raisons. Il conditionne l'entraînement sur une description de l'évaluateur, avec Llama-3.1-8B-Instruct et LoRA. À lister comme vérifié et hors angle, pour qu'il ne revienne pas, et comme voisin du dispositif des cadrages.
5. ***Alignment Midtraining Cracks Under Pressure* (21 septembre 2026).** Le rapport 2 dit qu'il touche la survie et raisons contre actions, sans auteur ni lieu. La fiche ne le mentionne qu'au détour du tableau des contradictions (ligne 345). Il manque dans la liste des travaux vus et non identifiés.
6. ***Teaching Claude Why* : un résultat omis.** Selon le rapport 1, des documents constitutionnels plus des récits font passer le chantage de 65 % à 19 %. Cela complète l'effet brut ; c'est facultatif.
7. **Deckenbach et al. : une version à vérifier.** Le rapport 2 parle d'une « v2 du 7 septembre 2026 », le rapport 7 d'une « HTML v4 du 7 septembre 2026 ». C'est une contradiction mineure, à ajouter au tableau.
8. **De niveau faible, et facultatif :** *Emergent alignment and the projectability of ethical personas* (Del Pinal … Perez Carballo, 2606.09475 ; rapport 5, résumé seul). Il fait un SFT avec quatre constitutions, et un alignement étroit s'y généralise largement.

---

## 5 · Ce qui a été vérifié et tient (pour ne pas le refaire)

- **De la Fuente et Conmy.** Tous les chiffres du jouet : 10,3 ; 94,5 ; 44,5 ; 62,5 ; 21,5 à 24,7 % (rapport 1). Les trois bras de la partie alignement (rapport 1). Les statuts de lecture.
- ***Model Spec Midtraining*.** Les trois bras et le tableau des chiffres, y compris l'absence des chiffres du bras sans chaîne. Le contrôle de longueur entre explications de valeurs et sous-règles (rapport 1). Le statut du rapport 6 : résumé seul.
- **Cho et al.**
  - Le résultat relu (§4.2, n° 9).
  - Le plan 2×2, le SFT neutre et le GRPO sur GSM8K (rapport 4).
  - Le bloc d'environ 45 % (rapports 1 et 7) ; le bras court qui fait 47 à 54 % de la longueur (rapport 4).
  - Les 15 points de contrôle d'environ 241 Go, inutilisables à 8B (§4.3).
  - Les sept auteurs (§4.3).
- **Korbak et al.** Toutes les corrections du §4.3 sont bien reprises.
- ***Safety Reasoning with Guidelines*.** Le titre et les auteurs (§4.2, n° 4) ; le rapport 1 a tort, comme la fiche le dit.
- **Baines et al., *Stress Testing Deliberative Alignment*, l'espace de travail global (§4.2, n° 2), *Open Character Training*, *Synthetic Persona Pretraining*, *Deliberative Alignment is Deep*.** Faits et statuts conformes aux rapports.
- **Le projet de Cadile.** Contenu, sorties prévues, dates SPAR et niveau moyen (rapports 1 et 6).
- **Second Look Research.** Deux sources (rapport 6 : billet du 15 août ; rapport 2 : note du 21 septembre). Le niveau « faible à moyen » suit le rapport 6.
- **Les dates d'ICLR 2027** (rapport 6) et le principal risque restant (§4.4).
- **Les contacts : « non pas encore ».** Conforme à la réponse de Lazar du 2 octobre.
- **Aucune idée n'est désignée par un sigle.** Aucun « first ».
