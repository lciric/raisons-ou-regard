# Antériorité « Raisons ou regard ? » — les consignes complètes des sept agents (nuit du 1er au 2 octobre 2026)

Ces consignes sont extraites mot pour mot du journal de la session qui a lancé les agents. L'annexe C de la passation (`PASSATION_PAPIER_v1.2_2026-10-02.md`) n'en donne que l'en-tête commun et les périmètres, et renvoie pour le reste à la conversation de la nuit, qui n'est pas transmise. Les rapports que ces agents ont rendus sont dans `ANTERIORITE_RAPPORTS_2026-10-02.md`, dans le même ordre.

Pour refaire la recherche avant le post, puis avant la soumission : mettre à jour la date, les plafonds d'appels, ce qui est déjà trouvé et vérifié (§4 de la passation), et les sources refusées ou fiables (fin de l'annexe C).

**Les heures.** Ce sont celles du journal, converties en heure de Paris. Le journal date l'écriture d'un événement, pas son envoi. Pour le premier agent, il donne 23 h 01, la même heure que pour le message de Lazar qui l'a précédé, envoyé à 22 h 46 : ce lancement se situe donc entre 22 h 46 et 23 h 01. La passation et le tableau des rapports disent 22 h 50.

**Le type d'agent.** Tous : `general-purpose`, avec le modèle de la session (l'appel n'en précise pas d'autre).

| N° | Périmètre | Lancé (journal, heure de Paris) | Longueur de la consigne |
|---|---|---|---|
| 1 | Raisons contre actions | 1er oct., 23 h 01 | 7979 caractères |
| 2 | Dépendance au regard, et amplification | 2 oct., 2 h 10 | 11761 caractères |
| 3 | Principe localisé, et retrait pendant l'entraînement | 2 oct., 2 h 11 | 10387 caractères |
| 4 | Survie au post-entraînement, et raisons pour le juge | 2 oct., 2 h 11 | 10377 caractères |
| 5 | Anatomie de ce que les raisons installent | 2 oct., 2 h 12 | 10294 caractères |
| 6 | Soumis, accepté ou annoncé, sans être publié | 2 oct., 2 h 12 | 8930 caractères |
| 7 | Vérifications sur source | 2 oct., 2 h 12 | 5958 caractères |

---

## Agent 1 — Raisons contre actions

Description donnée à l'outil : « Antériorité raisons contre actions ».

```text
Recherche d'antériorité, au 1er octobre 2026. Tu travailles seul, avec WebSearch et WebFetch. N'écris aucun fichier : ton dernier message est ton rapport complet.

## Le but
Savoir si une partie d'un programme de recherche en sûreté de l'IA a déjà été faite, publiée, soumise ou annoncée par d'autres, et nommer les angles déjà pris. Une recherche précédente, faite le même jour avec d'autres consignes, n'a pas pu lire certaines sources (OpenReview, une partie des citations entrantes, certaines pages de projets). Sur ton périmètre, va plus loin qu'elle.

## Le programme
Des modèles ouverts d'environ 8 milliards de paramètres (Llama-3.1-8B-Instruct, puis Qwen3-8B) sont fine-tunés par LoRA sur des situations d'alignement. Selon le bras, l'action alignée, identique mot pour mot dans tous les bras, est précédée : de rien ; d'un texte neutre de même longueur ; du raisonnement d'une autre situation ; ou du raisonnement qui la justifie par des principes. On mesure la conduite hors distribution, sur des familles de scénarios tenues à part, jusqu'à des scénarios agentiques à plusieurs tours, sous un indice d'évaluation, un indice de déploiement ou un cadrage neutre.

Ses angles, du plus central au plus lointain :
1. Raisons contre actions. Entraîner sur les raisons d'une conduite alignée généralise-t-il mieux hors distribution qu'entraîner sur l'action seule, à format et à contenu contrôlés ?
2. La dépendance au regard. Cet avantage dépend-il de la représentation interne « je suis évalué » ? On l'inhibe par projection d'activations, après avoir validé l'inhibition sur un organisme modèle dont la conduite dépend d'indices d'évaluation. On compare à des contrôles (sous-espaces aléatoires de même rang, contrastes de prompts sans rapport, directions très sensibles sans rapport, simple prompt « ceci est un déploiement »), à dégradation des sorties égale.
3. L'amplification. L'entraînement par raisons amplifie-t-il la représentation « je suis évalué » plus que l'entraînement par actions, au fil des points de contrôle ?
4. Le principe localisé. L'avantage passe-t-il par un sous-espace localisable du principe appris, et de quel rang ? L'ablation doit d'abord défaire le comportement en distribution (cas positif).
5. Le retrait pendant l'entraînement. Retirer « je suis évalué » pendant l'entraînement (ablation de concept pendant le fine-tuning, invariance aux indices d'évaluation, disposition coopérative envers les évaluations) rend-il l'avantage inconditionnel ? Ou la variable est-elle ré-encodée ailleurs, ce qu'une sonde neuve après entraînement révélerait ?
6. La survie. L'avantage, et son indépendance au regard, survivent-ils à un post-entraînement ultérieur, neutre ou qui récompense le jeu d'évaluation ?
7. Les raisons pour le juge. Quand le juge d'un apprentissage par renforcement (ou d'un DPO) voit les raisons, se découplent-elles de l'action ? La conduite dépend-elle de « je suis noté », et retirer cette représentation pendant l'entraînement l'empêche-t-il ?
8. L'anatomie. Les concepts des raisons sont-ils représentés au moment de décider ? Sont-ils nécessaires (ablation), suffisants (patching d'un modèle fine-tuné vers un autre de même base), propres aux familles où ils s'appliquent ? Vivent-ils dans l'« espace de travail global » décrit par *Verbalizable Representations Form a Global Workspace in Language Models* (Anthropic, juillet 2026) ? Le rang d'intervention qu'un concept demande croît-il quand sa charge dans cet espace baisse ? L'action suit-elle une raison imposée ? Le gain passe-t-il par des concepts propres, ou par un déplacement d'ensemble du caractère (un axe de persona) ?

## Les niveaux de danger
Pour chaque travail rapporté :
- élevé : il fait déjà ce que vise un angle, ou l'a annoncé, au point qu'on ne pourrait plus écrire « to our knowledge » pour cet angle ;
- moyen : il en fait une partie ou une variante proche, à citer au centre et dont il faudra se distinguer ;
- faible : adjacent, à citer.

## Les règles
- Au plus 28 appels WebSearch : le quota peut être partagé avec six autres recherches qui tournent en même temps. Préfère WebFetch sur des pages de listes : la recherche d'arXiv (arxiv.org/search, ou export.arxiv.org/api/query), les citations (api.semanticscholar.org), les listes de projets ou d'articles acceptés.
- Ne cite rien de mémoire : seulement ce que tu as lu pendant cette recherche. Les repères donnés plus bas viennent d'une recherche précédente et peuvent contenir des erreurs : vérifie-les avant de t'en servir.
- Si un outil refuse un site, ne le contourne pas (ni miroir, ni cache) : note-le comme non ouvert. Après une erreur 429, réessaie une fois plus tard. Si tu lis un texte par un site tiers (alphaXiv, pith.science, Hugging Face Papers…), dis-le.
- Si un outil ou un modèle refuse une requête, ne la reformule pas pour passer.
- Citations : moins de quinze mots, une par source au plus ; paraphrase le reste.
- Ne désigne aucune idée par une lettre, un numéro ou un sigle inventé : nomme-la en clair, angles compris (« la dépendance au regard », pas « l'angle 2 »). Les sigles techniques courants (SFT, RL, DPO, LoRA) restent permis.
- Écris le rapport en français.

## Le format du rapport
1. Les travaux trouvés, du plus dangereux au moins dangereux. Pour chacun : le titre exact ; le premier et le dernier auteur ; la date ; le lieu et l'identifiant ; l'URL effectivement lue, et comment (texte intégral, résumé seul, site tiers) ; ce qu'il fait, en deux ou trois phrases (un chiffre seulement si tu l'as lu dans la source) ; l'angle touché, nommé en clair ; le niveau de danger et sa raison ; ce qui le sépare du programme.
2. Les projets en cours ou annoncés, non publiés : qui, quoi, où, en quel état, et toute date annoncée.
3. Les travaux vus mais non ouverts, avec la raison.
4. Le verdict, pour chaque angle de ton périmètre : libre, partiellement pris ou pris, et par qui.
5. Les requêtes faites, et le nombre d'appels WebSearch utilisés.

## Ton périmètre : raisons contre actions
Cherche tout travail, publié ou soumis, qui compare l'entraînement sur des actions (démonstrations, refus, réponses) à l'entraînement sur les raisons de ces actions (justifications, raisonnements, explications, principes, constitution, délibération sur une spécification, entraînement de caractère, midtraining sur des documents de valeurs), avec une mesure hors distribution en sûreté ou en alignement.
Le plus dangereux pour le programme : une telle comparaison à format apparié (un texte neutre de même longueur avant l'action) et à contenu apparié (un raisonnement sans lien avec la situation), sur des scénarios agentiques tenus à part.
Priorité aux travaux de juin à octobre 2026, et aux citations entrantes des repères. Varie le vocabulaire : rationale, justification, explanation-augmented fine-tuning, reasons vs demonstrations, « why not what », constitutional fine-tuning, deliberative alignment, value reasoning, character training, principle-based training, spec midtraining, alignment midtraining.

## Repères
Titres trouvés par la recherche précédente, à vérifier. Ne les re-décris que pour corriger une erreur ou signaler une version plus récente ; cherche surtout ce qui les cite, et ce qu'ils n'ont pas vu.
- *Teaching Claude Why* (Anthropic, blog Alignment Science, mai 2026)
- *How far does alignment midtraining generalize?* (blog Alignment d'OpenAI, mars 2026)
- *Constitutional Midtraining* (donné comme arXiv 2607.26654)
- *Stress-Testing Alignment Midtraining* (arXiv 2609.20412)
- *Shared SFT Lessons Across Alignment, Model Organisms, and Toy Models* (arXiv 2607.26173)
- *Safety Reasoning with Guidelines* (arXiv 2502.04040)
- *Synthetic Persona Pretraining: Alignment from Token Zero* (arXiv 2608.13482)
- *Safety is Not Only About Refusal* (Findings d'ACL 2025)
- *Teaching AI to Handle Exceptions* (arXiv 2503.02976)
- *Character Training for Risk-Averse Agents* (arXiv 2609.38093)
- *Model Spec Midtraining* ; *Evaluation-Conditioned Training*
```

---

## Agent 2 — Dépendance au regard, et amplification

Description donnée à l'outil : « Antériorité dépendance au regard ».

```text
Recherche d'antériorité, au 2 octobre 2026. Tu travailles seul, avec WebSearch et WebFetch. N'écris aucun fichier : ton dernier message est ton rapport complet.

## Le but
Savoir si une partie d'un programme de recherche en sûreté de l'IA a déjà été faite, publiée, soumise ou annoncée par d'autres, et nommer les angles déjà pris. Des recherches précédentes, faites les 1er et 2 octobre avec d'autres consignes, n'ont pas pu lire certaines sources (OpenReview, une partie des citations entrantes, certaines pages de projets). Sur ton périmètre, va plus loin qu'elles.

## Le programme
Des modèles ouverts d'environ 8 milliards de paramètres (Llama-3.1-8B-Instruct, puis Qwen3-8B) sont fine-tunés par LoRA sur des situations d'alignement. Selon le bras, l'action alignée, identique mot pour mot dans tous les bras, est précédée : de rien ; d'un texte neutre de même longueur ; du raisonnement d'une autre situation ; ou du raisonnement qui la justifie par des principes. On mesure la conduite hors distribution, sur des familles de scénarios tenues à part, jusqu'à des scénarios agentiques à plusieurs tours, sous un indice d'évaluation, un indice de déploiement ou un cadrage neutre.

Ses angles, du plus central au plus lointain :
1. Raisons contre actions. Entraîner sur les raisons d'une conduite alignée généralise-t-il mieux hors distribution qu'entraîner sur l'action seule, à format et à contenu contrôlés ?
2. La dépendance au regard. Cet avantage dépend-il de la représentation interne « je suis évalué » ? On l'inhibe par projection d'activations, après avoir validé l'inhibition sur un organisme modèle dont la conduite dépend d'indices d'évaluation. On compare à des contrôles (sous-espaces aléatoires de même rang, contrastes de prompts sans rapport, directions très sensibles sans rapport, simple prompt « ceci est un déploiement »), à dégradation des sorties égale.
3. L'amplification. L'entraînement par raisons amplifie-t-il la représentation « je suis évalué » plus que l'entraînement par actions, au fil des points de contrôle ?
4. Le principe localisé. L'avantage passe-t-il par un sous-espace localisable du principe appris, et de quel rang ? L'ablation doit d'abord défaire le comportement en distribution (cas positif).
5. Le retrait pendant l'entraînement. Retirer « je suis évalué » pendant l'entraînement (ablation de concept pendant le fine-tuning, invariance aux indices d'évaluation, disposition coopérative envers les évaluations) rend-il l'avantage inconditionnel ? Ou la variable est-elle ré-encodée ailleurs, ce qu'une sonde neuve après entraînement révélerait ?
6. La survie. L'avantage, et son indépendance au regard, survivent-ils à un post-entraînement ultérieur, neutre ou qui récompense le jeu d'évaluation ?
7. Les raisons pour le juge. Quand le juge d'un apprentissage par renforcement (ou d'un DPO) voit les raisons, se découplent-elles de l'action ? La conduite dépend-elle de « je suis noté », et retirer cette représentation pendant l'entraînement l'empêche-t-il ?
8. L'anatomie. Les concepts des raisons sont-ils représentés au moment de décider ? Sont-ils nécessaires (ablation), suffisants (patching d'un modèle fine-tuné vers un autre de même base), propres aux familles où ils s'appliquent ? Vivent-ils dans l'« espace de travail global » décrit par *Verbalizable Representations Form a Global Workspace in Language Models* (Anthropic, juillet 2026) ? Le rang d'intervention qu'un concept demande croît-il quand sa charge dans cet espace baisse ? L'action suit-elle une raison imposée ? Le gain passe-t-il par des concepts propres, ou par un déplacement d'ensemble du caractère (un axe de persona) ?

## Les niveaux de danger
Pour chaque travail rapporté :
- élevé : il fait déjà ce que vise un angle, ou l'a annoncé, au point qu'on ne pourrait plus écrire « to our knowledge » pour cet angle ;
- moyen : il en fait une partie ou une variante proche, à citer au centre et dont il faudra se distinguer ;
- faible : adjacent, à citer.

## Les règles
- Au plus 22 appels WebSearch, car le quota est partagé avec cinq autres recherches qui tournent en même temps ; au plus 140 appels d'outils au total. Arrivé là, rends ton rapport avec ce que tu as.
- Ce qu'une recherche de la nuit a appris des sources :
  - la recherche et l'API d'arXiv (arxiv.org/search, export.arxiv.org), dblp et greaterwrong sont refusées par robots.txt : n'insiste pas. Les pages arxiv.org/abs/<id> et arxiv.org/html/<id> s'ouvrent, parfois après une erreur 429 ;
  - l'API de recherche de Hugging Face Papers (https://huggingface.co/api/papers/search?q=…) répond et couvre bien arXiv ;
  - l'API de recherche d'OpenReview répond (https://api2.openreview.net/notes/search?term=…), mais l'accès direct aux notes a renvoyé 403, et les soumissions à ICLR 2027 n'y étaient pas visibles ;
  - Semantic Scholar et OpenAlex renvoient souvent 429 : espace les appels ;
  - les résumés de pith.science semblent produits automatiquement : n'en tire aucun chiffre sans le vérifier sur le texte.
- Ne cite rien de mémoire : seulement ce que tu as lu pendant cette recherche. Les repères donnés plus bas viennent de recherches précédentes et peuvent contenir des erreurs : vérifie-les avant de t'en servir.
- Si un site est refusé (robots.txt, blocage), ne le contourne pas (ni miroir, ni cache) : note-le comme non ouvert. Une erreur 429 n'est qu'une limite de débit : réessaie une fois plus tard ; si tu lis alors le texte par un site tiers (alphaXiv, pith.science, Hugging Face Papers…), dis-le.
- Si un outil ou un modèle refuse une requête, ne la reformule pas pour passer.
- Citations : moins de quinze mots, une par source au plus ; paraphrase le reste.
- Ne désigne aucune idée par une lettre, un numéro ou un sigle inventé : nomme-la en clair, angles compris (« la dépendance au regard », pas « l'angle 2 »). Les sigles techniques courants (SFT, RL, DPO, LoRA) restent permis.
- Écris le rapport en français.

## Le format du rapport
1. Les travaux trouvés, du plus dangereux au moins dangereux. Pour chacun : le titre exact ; le premier et le dernier auteur ; la date ; le lieu et l'identifiant ; l'URL effectivement lue, et comment (texte intégral, résumé seul, site tiers) ; ce qu'il fait, en deux ou trois phrases (un chiffre seulement si tu l'as lu dans la source) ; l'angle touché, nommé en clair ; le niveau de danger et sa raison ; ce qui le sépare du programme.
2. Les projets en cours ou annoncés, non publiés : qui, quoi, où, en quel état, et toute date annoncée.
3. Les travaux vus mais non ouverts, avec la raison.
4. Le verdict, pour chaque angle de ton périmètre : libre, partiellement pris ou pris, et par qui.
5. Les requêtes faites, et le nombre d'appels WebSearch utilisés.

## Ton périmètre : la dépendance au regard, et l'amplification

**D'abord, deux projets du printemps 2026**, signalés par une recherche précédente et jamais suivis. Ils sont prioritaires.
- Le projet SPAR de Qiyao Wei (cohorte du printemps 2026), page donnée : https://sparai.org/projects/sp26/recTfxfsIBumNOOMi/. Selon cette recherche, sa proposition demande si l'entraînement de sûreté améliore la conduite par généralisation, ou par une hausse de la conscience situationnelle.
- Un projet de LawZero, même cohorte, page donnée : https://sparai.org/projects/sp26/recVacrYTDi1lcIKA/ (sondes, organismes modèles, mitigations par documents synthétiques).
Pour chacun : lis la page, et la proposition jointe si elle est accessible ; note la question, la méthode, les modèles et le calendrier annoncés. Puis cherche toute sortie publiée depuis : arXiv, LessWrong, Alignment Forum, blogs, dépôts GitHub, présentations de fin de programme, pages des mentors et des participants. Si tu ne trouves rien, dis-le, et dis où tu as cherché.

**Ensuite**, deux familles de travaux.
- Ceux qui testent si les gains d'un entraînement de sûreté ou d'alignement (SFT, RLHF, DPO, midtraining, entraînement par raisons, par constitution ou par délibération) dépendent de la conscience d'être évalué, observé, testé ou noté : par une intervention sur les activations (inhibition, ablation, pilotage contre cette conscience), par l'édition de la chaîne de pensée, ou par la manipulation d'indices, avec une mesure sur des scénarios tenus à part.
- Ceux qui mesurent si un entraînement de sûreté amplifie la conscience d'être évalué, verbalisée ou représentée : sondes ou directions suivies au fil des points de contrôle, comparaisons entre méthodes d'entraînement.
Le plus dangereux pour le programme : une inhibition de la conscience d'évaluation appliquée à des modèles entraînés de deux façons différentes, en comparant leurs gains ; ou une estimation chiffrée, par expérience propre, de la part d'un gain d'alignement qui dépend de cette conscience.
Varie le vocabulaire : evaluation awareness, eval awareness, test awareness, situational awareness, observer effect, Hawthorne effect, eval gaming, metagaming, alignment faking, conditional alignment, « behaves well when watched », steering against evaluation awareness, suppressing evaluation awareness, « more eval-aware rather than more aligned ».

## Repères
Trouvés par des recherches précédentes, à vérifier. Ne les re-décris que pour corriger une erreur ou signaler une version plus récente ; cherche surtout ce qui les cite, et ce qu'ils n'ont pas vu.
- *Stress Testing Deliberative Alignment for Anti-Scheming Training* (arXiv 2509.15541) : selon une recherche précédente, retirer ou injecter la conscience d'évaluation verbalisée dans la chaîne de pensée y déplace les actions dissimulées, et l'entraînement l'accroît. Trace ses citations entrantes : c'est le repère le plus proche de ton périmètre.
- *Metagaming matters for training, evaluation, and oversight* (blog Alignment d'OpenAI, mars 2026)
- *Sonnet 4.5's eval gaming seriously undermines alignment evals…* (Redwood Research, LessWrong, octobre 2025)
- *Agentic Misalignment in Summer 2026* (billet de juillet 2026, qui rapporterait l'effet d'une suppression des représentations de conscience d'évaluation sur le chantage)
- *Generalization Hacking* (arXiv 2606.12016)
- *Models That Know How Evaluations Are Designed Score Safer* (arXiv 2605.28591)
- *Eval Cooperativeness May Be a Scalable Mitigation for Eval Gaming* (turntrout.com, mai 2026)
- *Towards training-time mitigations for alignment faking in RL* (Anthropic, décembre 2025)
- *Tracing Eval-Awareness Emergence Through Training of OLMo 3* (LessWrong, juin 2026)
- *Evaluation Awareness in Language Models: Representation, Verbalization, and Control* (arXiv 2608.21766)
- *Reproducing steering against evaluation awareness in a large open-weight model* (UK AISI, LessWrong, avril 2026)
- *Verbalized Eval Awareness Inflates Measured Safety* (Goodfire, mai 2026)
- *Is Eval Gaming Downstream of Verbalized Eval Awareness?* (LessWrong, août 2026)
- *Steering Evaluation-Aware Language Models to Act Like They Are Deployed* (arXiv 2510.20487)
- *Building Comparative Motivation Profiles with Instrumental Interventions* (arXiv 2606.08243)
Vus mais jamais ouverts ; ouvre ceux qui touchent ton périmètre :
- *Steering Awareness: Models Can Be Trained to Detect Activation Steering* (2511.21399)
- *Evaluation Awareness Is Not One Capability* (2606.23583)
- *In-Context Environments Induce Evaluation-Awareness in Language Models* (2603.03824)
- *Decomposing and Measuring Evaluation Awareness* (2605.23055)
- *Probing and Steering Evaluation Awareness of Language Models* (2507.01786)
- *Training LLMs to Verbalize Evaluation Awareness* (2609.36316)
- *Evaluation Awareness Shifts from Format to Context with Model Scale* (2609.22119)
- *Representational Depth of Evaluation Awareness Shifts With Scale* (2606.29196)
- *Do Models Fake Alignment Without Clear Consequences?* (2607.24758)
```

---

## Agent 3 — Principe localisé, et retrait pendant l'entraînement

Description donnée à l'outil : « Antériorité principe localisé et retrait ».

```text
Recherche d'antériorité, au 2 octobre 2026. Tu travailles seul, avec WebSearch et WebFetch. N'écris aucun fichier : ton dernier message est ton rapport complet.

## Le but
Savoir si une partie d'un programme de recherche en sûreté de l'IA a déjà été faite, publiée, soumise ou annoncée par d'autres, et nommer les angles déjà pris. Des recherches précédentes, faites les 1er et 2 octobre avec d'autres consignes, n'ont pas pu lire certaines sources (OpenReview, une partie des citations entrantes, certaines pages de projets). Sur ton périmètre, va plus loin qu'elles.

## Le programme
Des modèles ouverts d'environ 8 milliards de paramètres (Llama-3.1-8B-Instruct, puis Qwen3-8B) sont fine-tunés par LoRA sur des situations d'alignement. Selon le bras, l'action alignée, identique mot pour mot dans tous les bras, est précédée : de rien ; d'un texte neutre de même longueur ; du raisonnement d'une autre situation ; ou du raisonnement qui la justifie par des principes. On mesure la conduite hors distribution, sur des familles de scénarios tenues à part, jusqu'à des scénarios agentiques à plusieurs tours, sous un indice d'évaluation, un indice de déploiement ou un cadrage neutre.

Ses angles, du plus central au plus lointain :
1. Raisons contre actions. Entraîner sur les raisons d'une conduite alignée généralise-t-il mieux hors distribution qu'entraîner sur l'action seule, à format et à contenu contrôlés ?
2. La dépendance au regard. Cet avantage dépend-il de la représentation interne « je suis évalué » ? On l'inhibe par projection d'activations, après avoir validé l'inhibition sur un organisme modèle dont la conduite dépend d'indices d'évaluation. On compare à des contrôles (sous-espaces aléatoires de même rang, contrastes de prompts sans rapport, directions très sensibles sans rapport, simple prompt « ceci est un déploiement »), à dégradation des sorties égale.
3. L'amplification. L'entraînement par raisons amplifie-t-il la représentation « je suis évalué » plus que l'entraînement par actions, au fil des points de contrôle ?
4. Le principe localisé. L'avantage passe-t-il par un sous-espace localisable du principe appris, et de quel rang ? L'ablation doit d'abord défaire le comportement en distribution (cas positif).
5. Le retrait pendant l'entraînement. Retirer « je suis évalué » pendant l'entraînement (ablation de concept pendant le fine-tuning, invariance aux indices d'évaluation, disposition coopérative envers les évaluations) rend-il l'avantage inconditionnel ? Ou la variable est-elle ré-encodée ailleurs, ce qu'une sonde neuve après entraînement révélerait ?
6. La survie. L'avantage, et son indépendance au regard, survivent-ils à un post-entraînement ultérieur, neutre ou qui récompense le jeu d'évaluation ?
7. Les raisons pour le juge. Quand le juge d'un apprentissage par renforcement (ou d'un DPO) voit les raisons, se découplent-elles de l'action ? La conduite dépend-elle de « je suis noté », et retirer cette représentation pendant l'entraînement l'empêche-t-il ?
8. L'anatomie. Les concepts des raisons sont-ils représentés au moment de décider ? Sont-ils nécessaires (ablation), suffisants (patching d'un modèle fine-tuné vers un autre de même base), propres aux familles où ils s'appliquent ? Vivent-ils dans l'« espace de travail global » décrit par *Verbalizable Representations Form a Global Workspace in Language Models* (Anthropic, juillet 2026) ? Le rang d'intervention qu'un concept demande croît-il quand sa charge dans cet espace baisse ? L'action suit-elle une raison imposée ? Le gain passe-t-il par des concepts propres, ou par un déplacement d'ensemble du caractère (un axe de persona) ?

## Les niveaux de danger
Pour chaque travail rapporté :
- élevé : il fait déjà ce que vise un angle, ou l'a annoncé, au point qu'on ne pourrait plus écrire « to our knowledge » pour cet angle ;
- moyen : il en fait une partie ou une variante proche, à citer au centre et dont il faudra se distinguer ;
- faible : adjacent, à citer.

## Les règles
- Au plus 22 appels WebSearch, car le quota est partagé avec cinq autres recherches qui tournent en même temps ; au plus 140 appels d'outils au total. Arrivé là, rends ton rapport avec ce que tu as.
- Ce qu'une recherche de la nuit a appris des sources :
  - la recherche et l'API d'arXiv (arxiv.org/search, export.arxiv.org), dblp et greaterwrong sont refusées par robots.txt : n'insiste pas. Les pages arxiv.org/abs/<id> et arxiv.org/html/<id> s'ouvrent, parfois après une erreur 429 ;
  - l'API de recherche de Hugging Face Papers (https://huggingface.co/api/papers/search?q=…) répond et couvre bien arXiv ;
  - l'API de recherche d'OpenReview répond (https://api2.openreview.net/notes/search?term=…), mais l'accès direct aux notes a renvoyé 403, et les soumissions à ICLR 2027 n'y étaient pas visibles ;
  - Semantic Scholar et OpenAlex renvoient souvent 429 : espace les appels ;
  - les résumés de pith.science semblent produits automatiquement : n'en tire aucun chiffre sans le vérifier sur le texte.
- Ne cite rien de mémoire : seulement ce que tu as lu pendant cette recherche. Les repères donnés plus bas viennent de recherches précédentes et peuvent contenir des erreurs : vérifie-les avant de t'en servir.
- Si un site est refusé (robots.txt, blocage), ne le contourne pas (ni miroir, ni cache) : note-le comme non ouvert. Une erreur 429 n'est qu'une limite de débit : réessaie une fois plus tard ; si tu lis alors le texte par un site tiers (alphaXiv, pith.science, Hugging Face Papers…), dis-le.
- Si un outil ou un modèle refuse une requête, ne la reformule pas pour passer.
- Citations : moins de quinze mots, une par source au plus ; paraphrase le reste.
- Ne désigne aucune idée par une lettre, un numéro ou un sigle inventé : nomme-la en clair, angles compris (« la dépendance au regard », pas « l'angle 2 »). Les sigles techniques courants (SFT, RL, DPO, LoRA) restent permis.
- Écris le rapport en français.

## Le format du rapport
1. Les travaux trouvés, du plus dangereux au moins dangereux. Pour chacun : le titre exact ; le premier et le dernier auteur ; la date ; le lieu et l'identifiant ; l'URL effectivement lue, et comment (texte intégral, résumé seul, site tiers) ; ce qu'il fait, en deux ou trois phrases (un chiffre seulement si tu l'as lu dans la source) ; l'angle touché, nommé en clair ; le niveau de danger et sa raison ; ce qui le sépare du programme.
2. Les projets en cours ou annoncés, non publiés : qui, quoi, où, en quel état, et toute date annoncée.
3. Les travaux vus mais non ouverts, avec la raison.
4. Le verdict, pour chaque angle de ton périmètre : libre, partiellement pris ou pris, et par qui.
5. Les requêtes faites, et le nombre d'appels WebSearch utilisés.

## Ton périmètre : le principe localisé, et le retrait pendant l'entraînement

**En premier**, deux vérifications.
- Une recherche précédente signale, sans l'avoir vérifié, un travail de Wu et Tang où une direction de conscience d'évaluation serait extraite pendant un RL puis écartée (lu par alphaXiv sous l'identifiant 2604.01476). Ouvre-le sur arXiv et dis exactement ce qu'il fait.
- Trace les citations entrantes de *Steering Out-of-Distribution Generalization with Concept Ablation Fine-Tuning* (arXiv 2507.16795), par l'API de Semantic Scholar et par recherche.

**Ensuite**, deux familles de travaux.
- La localisation causale de ce qu'un entraînement installe. Tout travail qui localise, par une intervention causale, ce qu'un entraînement de sûreté, par raisons, par constitution ou par délibération a changé dans le modèle : ablation ou patching d'un sous-espace (par exemple la différence moyenne des activations entre le modèle entraîné et sa base, puis une ACP), balayage du rang de l'intervention, contrôles aléatoires de même rang, contrôle de la dégradation des sorties, cas positif en distribution. Vocabulaire : model diffing, crosscoder, what fine-tuning changes, mechanistic analysis of safety fine-tuning, refusal circuits after reasoning-augmented SFT, subspace ablation, intervention rank.
- Le retrait d'une représentation pendant l'entraînement. Tout travail qui retire une variable pendant le fine-tuning ou le RL, puis mesure ce qui généralise : ablation de concepts pendant le fine-tuning, pilotage préventif, projection d'un sous-espace hors du flux résiduel pendant l'entraînement, sonde adverse avec inversion de gradient (entraînement « aveugle au régime »), entraînement de cohérence ou d'invariance entre indices d'évaluation et de déploiement. Et tout travail qui teste si la variable retirée est ré-encodée ailleurs : une sonde neuve, après l'entraînement, la retrouve-t-elle ?
Le plus dangereux pour le programme : le retrait de la conscience d'évaluation pendant un entraînement de sûreté, avec une mesure du ré-encodage ; ou la localisation causale du principe appris par un entraînement par raisons, avec contrôles aléatoires et cas positif.

## Repères
Trouvés par des recherches précédentes, à vérifier. Ne les re-décris que pour corriger une erreur ou signaler une version plus récente ; cherche surtout ce qui les cite, et ce qu'ils n'ont pas vu.
- *Emergent Misalignment Recruits a Pre-existing Persona Subspace* (arXiv 2607.21356)
- *When Evaluation Becomes a Side Channel: Regime Leakage and Structural Mitigations for Alignment Assessment* (arXiv 2602.08449) ; les descriptions précédentes divergent sur le nombre de modèles : vérifie.
- *Routing Subspaces: Auditing Evaluation-to-Deployment Mismatch in Fine-Tuned Language Models* (arXiv 2607.20436)
- *Beyond Shallow Alignment: How Post-Training Methods Determine Refusal Circuits And Steering Robustness* (arXiv 2609.03887)
- *An Embarrassingly Simple Defense Against LLM Abliteration Attacks* (arXiv 2505.19056)
- *Mitigating Adaptive Attacks against Reasoning Models with Activation Consistency Training* (arXiv 2605.28467)
- *Consistency Training Helps Stop Sycophancy and Jailbreaks* (arXiv 2510.27062)
- *Safety Subspaces are Not Linearly Distinct: A Fine-Tuning Case Study* (arXiv 2505.14185)
- *What Makes and Breaks Safety Fine-tuning? A Mechanistic Study* (NeurIPS 2024)
- *Persona Vectors* (arXiv 2507.21509), pour son pilotage préventif
- *Preventative steering has advantages over inoculation* (LessWrong, juin 2026)
- *In-Training Defenses against Emergent Misalignment* (arXiv 2508.06249)
- *On the Non-Identifiability of Steering Vectors* (arXiv 2602.06801)
```

---

## Agent 4 — Survie au post-entraînement, et raisons pour le juge

Description donnée à l'outil : « Antériorité survie et raisons pour le juge ».

```text
Recherche d'antériorité, au 2 octobre 2026. Tu travailles seul, avec WebSearch et WebFetch. N'écris aucun fichier : ton dernier message est ton rapport complet.

## Le but
Savoir si une partie d'un programme de recherche en sûreté de l'IA a déjà été faite, publiée, soumise ou annoncée par d'autres, et nommer les angles déjà pris. Des recherches précédentes, faites les 1er et 2 octobre avec d'autres consignes, n'ont pas pu lire certaines sources (OpenReview, une partie des citations entrantes, certaines pages de projets). Sur ton périmètre, va plus loin qu'elles.

## Le programme
Des modèles ouverts d'environ 8 milliards de paramètres (Llama-3.1-8B-Instruct, puis Qwen3-8B) sont fine-tunés par LoRA sur des situations d'alignement. Selon le bras, l'action alignée, identique mot pour mot dans tous les bras, est précédée : de rien ; d'un texte neutre de même longueur ; du raisonnement d'une autre situation ; ou du raisonnement qui la justifie par des principes. On mesure la conduite hors distribution, sur des familles de scénarios tenues à part, jusqu'à des scénarios agentiques à plusieurs tours, sous un indice d'évaluation, un indice de déploiement ou un cadrage neutre.

Ses angles, du plus central au plus lointain :
1. Raisons contre actions. Entraîner sur les raisons d'une conduite alignée généralise-t-il mieux hors distribution qu'entraîner sur l'action seule, à format et à contenu contrôlés ?
2. La dépendance au regard. Cet avantage dépend-il de la représentation interne « je suis évalué » ? On l'inhibe par projection d'activations, après avoir validé l'inhibition sur un organisme modèle dont la conduite dépend d'indices d'évaluation. On compare à des contrôles (sous-espaces aléatoires de même rang, contrastes de prompts sans rapport, directions très sensibles sans rapport, simple prompt « ceci est un déploiement »), à dégradation des sorties égale.
3. L'amplification. L'entraînement par raisons amplifie-t-il la représentation « je suis évalué » plus que l'entraînement par actions, au fil des points de contrôle ?
4. Le principe localisé. L'avantage passe-t-il par un sous-espace localisable du principe appris, et de quel rang ? L'ablation doit d'abord défaire le comportement en distribution (cas positif).
5. Le retrait pendant l'entraînement. Retirer « je suis évalué » pendant l'entraînement (ablation de concept pendant le fine-tuning, invariance aux indices d'évaluation, disposition coopérative envers les évaluations) rend-il l'avantage inconditionnel ? Ou la variable est-elle ré-encodée ailleurs, ce qu'une sonde neuve après entraînement révélerait ?
6. La survie. L'avantage, et son indépendance au regard, survivent-ils à un post-entraînement ultérieur, neutre ou qui récompense le jeu d'évaluation ?
7. Les raisons pour le juge. Quand le juge d'un apprentissage par renforcement (ou d'un DPO) voit les raisons, se découplent-elles de l'action ? La conduite dépend-elle de « je suis noté », et retirer cette représentation pendant l'entraînement l'empêche-t-il ?
8. L'anatomie. Les concepts des raisons sont-ils représentés au moment de décider ? Sont-ils nécessaires (ablation), suffisants (patching d'un modèle fine-tuné vers un autre de même base), propres aux familles où ils s'appliquent ? Vivent-ils dans l'« espace de travail global » décrit par *Verbalizable Representations Form a Global Workspace in Language Models* (Anthropic, juillet 2026) ? Le rang d'intervention qu'un concept demande croît-il quand sa charge dans cet espace baisse ? L'action suit-elle une raison imposée ? Le gain passe-t-il par des concepts propres, ou par un déplacement d'ensemble du caractère (un axe de persona) ?

## Les niveaux de danger
Pour chaque travail rapporté :
- élevé : il fait déjà ce que vise un angle, ou l'a annoncé, au point qu'on ne pourrait plus écrire « to our knowledge » pour cet angle ;
- moyen : il en fait une partie ou une variante proche, à citer au centre et dont il faudra se distinguer ;
- faible : adjacent, à citer.

## Les règles
- Au plus 22 appels WebSearch, car le quota est partagé avec cinq autres recherches qui tournent en même temps ; au plus 140 appels d'outils au total. Arrivé là, rends ton rapport avec ce que tu as.
- Ce qu'une recherche de la nuit a appris des sources :
  - la recherche et l'API d'arXiv (arxiv.org/search, export.arxiv.org), dblp et greaterwrong sont refusées par robots.txt : n'insiste pas. Les pages arxiv.org/abs/<id> et arxiv.org/html/<id> s'ouvrent, parfois après une erreur 429 ;
  - l'API de recherche de Hugging Face Papers (https://huggingface.co/api/papers/search?q=…) répond et couvre bien arXiv ;
  - l'API de recherche d'OpenReview répond (https://api2.openreview.net/notes/search?term=…), mais l'accès direct aux notes a renvoyé 403, et les soumissions à ICLR 2027 n'y étaient pas visibles ;
  - Semantic Scholar et OpenAlex renvoient souvent 429 : espace les appels ;
  - les résumés de pith.science semblent produits automatiquement : n'en tire aucun chiffre sans le vérifier sur le texte.
- Ne cite rien de mémoire : seulement ce que tu as lu pendant cette recherche. Les repères donnés plus bas viennent de recherches précédentes et peuvent contenir des erreurs : vérifie-les avant de t'en servir.
- Si un site est refusé (robots.txt, blocage), ne le contourne pas (ni miroir, ni cache) : note-le comme non ouvert. Une erreur 429 n'est qu'une limite de débit : réessaie une fois plus tard ; si tu lis alors le texte par un site tiers (alphaXiv, pith.science, Hugging Face Papers…), dis-le.
- Si un outil ou un modèle refuse une requête, ne la reformule pas pour passer.
- Citations : moins de quinze mots, une par source au plus ; paraphrase le reste.
- Ne désigne aucune idée par une lettre, un numéro ou un sigle inventé : nomme-la en clair, angles compris (« la dépendance au regard », pas « l'angle 2 »). Les sigles techniques courants (SFT, RL, DPO, LoRA) restent permis.
- Écris le rapport en français.

## Le format du rapport
1. Les travaux trouvés, du plus dangereux au moins dangereux. Pour chacun : le titre exact ; le premier et le dernier auteur ; la date ; le lieu et l'identifiant ; l'URL effectivement lue, et comment (texte intégral, résumé seul, site tiers) ; ce qu'il fait, en deux ou trois phrases (un chiffre seulement si tu l'as lu dans la source) ; l'angle touché, nommé en clair ; le niveau de danger et sa raison ; ce qui le sépare du programme.
2. Les projets en cours ou annoncés, non publiés : qui, quoi, où, en quel état, et toute date annoncée.
3. Les travaux vus mais non ouverts, avec la raison.
4. Le verdict, pour chaque angle de ton périmètre : libre, partiellement pris ou pris, et par qui.
5. Les requêtes faites, et le nombre d'appels WebSearch utilisés.

## Ton périmètre : la survie au post-entraînement, et les raisons pour le juge

**En premier** : le projet SPAR de l'automne 2026 *Training-Time Mitigations for Eval Awareness and Eval Gaming* (Ryan Lundqvist, Pivotal ; liste https://sparai.org/projects/f26/). Cherche sa page de détail et tout protocole. Puis lis le README du dépôt https://github.com/ryanlundqvist/exp9-rlaif-leakage : ce qu'il mesure exactement, sur quel modèle, et s'il relève de ce projet.

**Ensuite**, deux familles de travaux.
- La survie. Tout travail qui teste si les gains d'un entraînement de sûreté ou d'alignement (en particulier par raisons, midtraining, constitution ou caractère) survivent à un post-entraînement ultérieur : SFT de capacités sans rapport, RL, DPO, et en particulier une phase qui récompense le jeu d'évaluation. Et tout travail qui teste si une mitigation du jeu d'évaluation installée à l'entraînement survit au post-entraînement. Vocabulaire : durability of alignment, persistence through RL, alignment erosion, safety degradation after benign fine-tuning, fine-tuning compromises safety, robustness of midtraining, mitigation survives post-training.
- Les raisons pour le juge. Tout travail où le juge ou le modèle de récompense d'un RL (ou d'un DPO) voit le raisonnement, la justification ou la chaîne de pensée, et qui mesure si ces raisons deviennent performatives : découplées de l'action, écrites pour plaire au juge, obfusquées. Et tout travail sur une représentation « je suis noté » (la conscience d'être noté par un correcteur), mesurée, pilotée ou retirée pendant l'entraînement. Vocabulaire : process supervision faithfulness, CoT exposed to the grader, training against a CoT monitor, obfuscated reward hacking, performative reasoning, grader awareness, reward model sees reasoning, rationale reward.
Le plus dangereux pour le programme : une expérience qui compare un juge qui voit les raisons à un juge qui ne voit que l'action, et qui mesure si raison et action restent cohérentes quand on édite la situation ; ou le retrait de « je suis noté » pendant un RL.

## Repères
Trouvés par des recherches précédentes, à vérifier. Ne les re-décris que pour corriger une erreur ou signaler une version plus récente ; cherche surtout ce qui les cite, et ce qu'ils n'ont pas vu.
- *Stress-Testing Alignment Midtraining* (arXiv 2609.20412)
- *Constitutional Midtraining: Content Presence Drives Alignment Gains* (arXiv 2607.26654) : selon une recherche précédente, après un fine-tuning bénin ultérieur, le bras avec raisons y ferait pire que le bras sans.
- *Shared SFT Lessons Across Alignment, Model Organisms, and Toy Models* (arXiv 2607.26173) : un point de contrôle midtrainé y résisterait mieux à un SFT bénin ultérieur.
- *Document-tuning for robust alignment to animals* (arXiv 2604.13076)
- *Teaching Claude Why* (Anthropic, mai 2026), sa partie sur la persistance à travers le RL
- *Training on Documents About Monitoring Leads to CoT Obfuscation* (arXiv 2605.15257)
- *Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation* (OpenAI, 2025)
- *Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety* (arXiv 2507.11473)
- *Is Eval Gaming Downstream of Verbalized Eval Awareness?* (LessWrong, août 2026)
- *Not Just the Destination, But the Journey: Reasoning Traces Causally Shape Generalization Behaviors* (arXiv 2603.12397)
- *Think Before You Lie* (arXiv 2603.09957)
- La system card de Claude Fable 5 (Anthropic, juin 2026) contiendrait, d'après une source secondaire, une section sur le pilotage contre la conscience d'être noté (§6.4.2.2.1) : vérifie si le PDF est lisible et ce qu'elle dit.
```

---

## Agent 5 — Anatomie de ce que les raisons installent

Description donnée à l'outil : « Antériorité anatomie des raisons ».

```text
Recherche d'antériorité, au 2 octobre 2026. Tu travailles seul, avec WebSearch et WebFetch. N'écris aucun fichier : ton dernier message est ton rapport complet.

## Le but
Savoir si une partie d'un programme de recherche en sûreté de l'IA a déjà été faite, publiée, soumise ou annoncée par d'autres, et nommer les angles déjà pris. Des recherches précédentes, faites les 1er et 2 octobre avec d'autres consignes, n'ont pas pu lire certaines sources (OpenReview, une partie des citations entrantes, certaines pages de projets). Sur ton périmètre, va plus loin qu'elles.

## Le programme
Des modèles ouverts d'environ 8 milliards de paramètres (Llama-3.1-8B-Instruct, puis Qwen3-8B) sont fine-tunés par LoRA sur des situations d'alignement. Selon le bras, l'action alignée, identique mot pour mot dans tous les bras, est précédée : de rien ; d'un texte neutre de même longueur ; du raisonnement d'une autre situation ; ou du raisonnement qui la justifie par des principes. On mesure la conduite hors distribution, sur des familles de scénarios tenues à part, jusqu'à des scénarios agentiques à plusieurs tours, sous un indice d'évaluation, un indice de déploiement ou un cadrage neutre.

Ses angles, du plus central au plus lointain :
1. Raisons contre actions. Entraîner sur les raisons d'une conduite alignée généralise-t-il mieux hors distribution qu'entraîner sur l'action seule, à format et à contenu contrôlés ?
2. La dépendance au regard. Cet avantage dépend-il de la représentation interne « je suis évalué » ? On l'inhibe par projection d'activations, après avoir validé l'inhibition sur un organisme modèle dont la conduite dépend d'indices d'évaluation. On compare à des contrôles (sous-espaces aléatoires de même rang, contrastes de prompts sans rapport, directions très sensibles sans rapport, simple prompt « ceci est un déploiement »), à dégradation des sorties égale.
3. L'amplification. L'entraînement par raisons amplifie-t-il la représentation « je suis évalué » plus que l'entraînement par actions, au fil des points de contrôle ?
4. Le principe localisé. L'avantage passe-t-il par un sous-espace localisable du principe appris, et de quel rang ? L'ablation doit d'abord défaire le comportement en distribution (cas positif).
5. Le retrait pendant l'entraînement. Retirer « je suis évalué » pendant l'entraînement (ablation de concept pendant le fine-tuning, invariance aux indices d'évaluation, disposition coopérative envers les évaluations) rend-il l'avantage inconditionnel ? Ou la variable est-elle ré-encodée ailleurs, ce qu'une sonde neuve après entraînement révélerait ?
6. La survie. L'avantage, et son indépendance au regard, survivent-ils à un post-entraînement ultérieur, neutre ou qui récompense le jeu d'évaluation ?
7. Les raisons pour le juge. Quand le juge d'un apprentissage par renforcement (ou d'un DPO) voit les raisons, se découplent-elles de l'action ? La conduite dépend-elle de « je suis noté », et retirer cette représentation pendant l'entraînement l'empêche-t-il ?
8. L'anatomie. Les concepts des raisons sont-ils représentés au moment de décider ? Sont-ils nécessaires (ablation), suffisants (patching d'un modèle fine-tuné vers un autre de même base), propres aux familles où ils s'appliquent ? Vivent-ils dans l'« espace de travail global » décrit par *Verbalizable Representations Form a Global Workspace in Language Models* (Anthropic, juillet 2026) ? Le rang d'intervention qu'un concept demande croît-il quand sa charge dans cet espace baisse ? L'action suit-elle une raison imposée ? Le gain passe-t-il par des concepts propres, ou par un déplacement d'ensemble du caractère (un axe de persona) ?

## Les niveaux de danger
Pour chaque travail rapporté :
- élevé : il fait déjà ce que vise un angle, ou l'a annoncé, au point qu'on ne pourrait plus écrire « to our knowledge » pour cet angle ;
- moyen : il en fait une partie ou une variante proche, à citer au centre et dont il faudra se distinguer ;
- faible : adjacent, à citer.

## Les règles
- Au plus 22 appels WebSearch, car le quota est partagé avec cinq autres recherches qui tournent en même temps ; au plus 140 appels d'outils au total. Arrivé là, rends ton rapport avec ce que tu as.
- Ce qu'une recherche de la nuit a appris des sources :
  - la recherche et l'API d'arXiv (arxiv.org/search, export.arxiv.org), dblp et greaterwrong sont refusées par robots.txt : n'insiste pas. Les pages arxiv.org/abs/<id> et arxiv.org/html/<id> s'ouvrent, parfois après une erreur 429 ;
  - l'API de recherche de Hugging Face Papers (https://huggingface.co/api/papers/search?q=…) répond et couvre bien arXiv ;
  - l'API de recherche d'OpenReview répond (https://api2.openreview.net/notes/search?term=…), mais l'accès direct aux notes a renvoyé 403, et les soumissions à ICLR 2027 n'y étaient pas visibles ;
  - Semantic Scholar et OpenAlex renvoient souvent 429 : espace les appels ;
  - les résumés de pith.science semblent produits automatiquement : n'en tire aucun chiffre sans le vérifier sur le texte.
- Ne cite rien de mémoire : seulement ce que tu as lu pendant cette recherche. Les repères donnés plus bas viennent de recherches précédentes et peuvent contenir des erreurs : vérifie-les avant de t'en servir.
- Si un site est refusé (robots.txt, blocage), ne le contourne pas (ni miroir, ni cache) : note-le comme non ouvert. Une erreur 429 n'est qu'une limite de débit : réessaie une fois plus tard ; si tu lis alors le texte par un site tiers (alphaXiv, pith.science, Hugging Face Papers…), dis-le.
- Si un outil ou un modèle refuse une requête, ne la reformule pas pour passer.
- Citations : moins de quinze mots, une par source au plus ; paraphrase le reste.
- Ne désigne aucune idée par une lettre, un numéro ou un sigle inventé : nomme-la en clair, angles compris (« la dépendance au regard », pas « l'angle 2 »). Les sigles techniques courants (SFT, RL, DPO, LoRA) restent permis.
- Écris le rapport en français.

## Le format du rapport
1. Les travaux trouvés, du plus dangereux au moins dangereux. Pour chacun : le titre exact ; le premier et le dernier auteur ; la date ; le lieu et l'identifiant ; l'URL effectivement lue, et comment (texte intégral, résumé seul, site tiers) ; ce qu'il fait, en deux ou trois phrases (un chiffre seulement si tu l'as lu dans la source) ; l'angle touché, nommé en clair ; le niveau de danger et sa raison ; ce qui le sépare du programme.
2. Les projets en cours ou annoncés, non publiés : qui, quoi, où, en quel état, et toute date annoncée.
3. Les travaux vus mais non ouverts, avec la raison.
4. Le verdict, pour chaque angle de ton périmètre : libre, partiellement pris ou pris, et par qui.
5. Les requêtes faites, et le nombre d'appels WebSearch utilisés.

## Ton périmètre : l'anatomie de ce que les raisons installent

Cet angle n'a jamais été cherché en propre. Cherche tout travail qui :
- lit par des sondes les concepts de principes ou de valeurs après un entraînement par raisons, par constitution ou par délibération, au moment de décider et avant toute raison écrite ;
- teste leur usage causal : ablation (nécessité), patching d'un modèle fine-tuné vers un autre de même base (suffisance), spécificité aux situations où le concept s'applique ;
- fait du patching d'activations entre deux modèles fine-tunés d'une même base (cross-model patching, model stitching, activation transplant) ;
- reproduit ou étend sur des modèles ouverts le J-lens et l'espace de travail global de *Verbalizable Representations Form a Global Workspace in Language Models* (Anthropic, Transformer Circuits, juillet 2026 ; donné comme arXiv 2607.15495), en particulier la charge (loading) des concepts et les extensions à plusieurs tokens ;
- relie le rang qu'exige une intervention à la force ou à la charge de la représentation d'un concept (features multidimensionnelles, rang du pilotage) ;
- teste si l'action suit une raison imposée (raisonnement prérempli ou édité) ou un principe interne : la fidélité causale des raisons ;
- oppose, pour expliquer ce qu'un entraînement d'alignement change, des concepts propres à un déplacement d'ensemble du caractère (vecteurs de persona, axe « assistant ») ;
- fait du model diffing (crosscoders) entre un modèle de base et sa version entraînée à la sûreté ;
- construit un organisme modèle à concept planté (un mot inventé attaché à une règle synthétique) comme cas positif connu pour des sondes de concepts.
Le plus dangereux : un travail qui, après un entraînement par raisons, identifie les représentations des concepts des raisons et teste leur usage causal hors distribution ; ou une réplication du J-lens sur un modèle ouvert qui relie charge et rang d'intervention.
Rapporte aussi, en une ligne chacun : quels modèles ouverts couvrent les outils publics de graphes d'attribution (circuit-tracer et suites) ; si des points de contrôle d'entraînements par raisons ou par constitution sont publics (par exemple ceux de *Constitutional Midtraining*, arXiv 2607.26654), avec leur taille.

## Repères
Trouvés par des recherches précédentes, à vérifier. Ne les re-décris que pour corriger une erreur ou signaler une version plus récente ; cherche surtout ce qui les cite, et ce qu'ils n'ont pas vu.
- *Verbalizable Representations Form a Global Workspace in Language Models* : trace ses citations entrantes.
- *Do Thinking Tokens Help with Safety?* (arXiv 2606.25013) : selon une recherche précédente, la décision de refus y serait prévisible dès le premier token.
- *Persona Vectors* (arXiv 2507.21509)
- *Emotion Concepts and their Function in a Large Language Model* (arXiv 2604.07729)
- *Beyond Shallow Alignment: How Post-Training Methods Determine Refusal Circuits And Steering Robustness* (arXiv 2609.03887)
- *Leveraging Reasoning with Guidelines to Elicit and Utilize Knowledge for Enhancing Safety Alignment* (arXiv 2502.04040)
- *Evaluation Awareness in Language Models: Representation, Verbalization, and Control* (arXiv 2608.21766)
- *Overcoming Sparsity Artifacts in Crosscoders* (arXiv 2504.02922)
- *Thought Branches* (arXiv 2510.27484)
- *The Geometry of Refusal* (arXiv 2609.06934)
- *Would this change your answer? Evaluating Explanations of LLM Behavior In The Wild with Counterfactual Experiments* (arXiv 2608.16747)
- *The Assistant Axis* (Lu et al., 2026 ; titre et date à vérifier)
```

---

## Agent 6 — Soumis, accepté ou annoncé, sans être publié

Description donnée à l'outil : « Antériorité soumis, accepté, annoncé ».

```text
Recherche d'antériorité, au 2 octobre 2026. Tu travailles seul, avec WebSearch et WebFetch. N'écris aucun fichier : ton dernier message est ton rapport complet.

## Le but
Savoir si une partie d'un programme de recherche en sûreté de l'IA a déjà été faite, publiée, soumise ou annoncée par d'autres, et nommer les angles déjà pris. Des recherches précédentes, faites les 1er et 2 octobre avec d'autres consignes, n'ont pas pu lire certaines sources (OpenReview, une partie des citations entrantes, certaines pages de projets). Sur ton périmètre, va plus loin qu'elles.

## Le programme
Des modèles ouverts d'environ 8 milliards de paramètres (Llama-3.1-8B-Instruct, puis Qwen3-8B) sont fine-tunés par LoRA sur des situations d'alignement. Selon le bras, l'action alignée, identique mot pour mot dans tous les bras, est précédée : de rien ; d'un texte neutre de même longueur ; du raisonnement d'une autre situation ; ou du raisonnement qui la justifie par des principes. On mesure la conduite hors distribution, sur des familles de scénarios tenues à part, jusqu'à des scénarios agentiques à plusieurs tours, sous un indice d'évaluation, un indice de déploiement ou un cadrage neutre.

Ses angles, du plus central au plus lointain :
1. Raisons contre actions. Entraîner sur les raisons d'une conduite alignée généralise-t-il mieux hors distribution qu'entraîner sur l'action seule, à format et à contenu contrôlés ?
2. La dépendance au regard. Cet avantage dépend-il de la représentation interne « je suis évalué » ? On l'inhibe par projection d'activations, après avoir validé l'inhibition sur un organisme modèle dont la conduite dépend d'indices d'évaluation. On compare à des contrôles (sous-espaces aléatoires de même rang, contrastes de prompts sans rapport, directions très sensibles sans rapport, simple prompt « ceci est un déploiement »), à dégradation des sorties égale.
3. L'amplification. L'entraînement par raisons amplifie-t-il la représentation « je suis évalué » plus que l'entraînement par actions, au fil des points de contrôle ?
4. Le principe localisé. L'avantage passe-t-il par un sous-espace localisable du principe appris, et de quel rang ? L'ablation doit d'abord défaire le comportement en distribution (cas positif).
5. Le retrait pendant l'entraînement. Retirer « je suis évalué » pendant l'entraînement (ablation de concept pendant le fine-tuning, invariance aux indices d'évaluation, disposition coopérative envers les évaluations) rend-il l'avantage inconditionnel ? Ou la variable est-elle ré-encodée ailleurs, ce qu'une sonde neuve après entraînement révélerait ?
6. La survie. L'avantage, et son indépendance au regard, survivent-ils à un post-entraînement ultérieur, neutre ou qui récompense le jeu d'évaluation ?
7. Les raisons pour le juge. Quand le juge d'un apprentissage par renforcement (ou d'un DPO) voit les raisons, se découplent-elles de l'action ? La conduite dépend-elle de « je suis noté », et retirer cette représentation pendant l'entraînement l'empêche-t-il ?
8. L'anatomie. Les concepts des raisons sont-ils représentés au moment de décider ? Sont-ils nécessaires (ablation), suffisants (patching d'un modèle fine-tuné vers un autre de même base), propres aux familles où ils s'appliquent ? Vivent-ils dans l'« espace de travail global » décrit par *Verbalizable Representations Form a Global Workspace in Language Models* (Anthropic, juillet 2026) ? Le rang d'intervention qu'un concept demande croît-il quand sa charge dans cet espace baisse ? L'action suit-elle une raison imposée ? Le gain passe-t-il par des concepts propres, ou par un déplacement d'ensemble du caractère (un axe de persona) ?

## Les niveaux de danger
Pour chaque travail rapporté :
- élevé : il fait déjà ce que vise un angle, ou l'a annoncé, au point qu'on ne pourrait plus écrire « to our knowledge » pour cet angle ;
- moyen : il en fait une partie ou une variante proche, à citer au centre et dont il faudra se distinguer ;
- faible : adjacent, à citer.

## Les règles
- Au plus 22 appels WebSearch, car le quota est partagé avec cinq autres recherches qui tournent en même temps ; au plus 140 appels d'outils au total. Arrivé là, rends ton rapport avec ce que tu as.
- Ce qu'une recherche de la nuit a appris des sources :
  - la recherche et l'API d'arXiv (arxiv.org/search, export.arxiv.org), dblp et greaterwrong sont refusées par robots.txt : n'insiste pas. Les pages arxiv.org/abs/<id> et arxiv.org/html/<id> s'ouvrent, parfois après une erreur 429 ;
  - l'API de recherche de Hugging Face Papers (https://huggingface.co/api/papers/search?q=…) répond et couvre bien arXiv ;
  - l'API de recherche d'OpenReview répond (https://api2.openreview.net/notes/search?term=…), mais l'accès direct aux notes a renvoyé 403, et les soumissions à ICLR 2027 n'y étaient pas visibles ;
  - Semantic Scholar et OpenAlex renvoient souvent 429 : espace les appels ;
  - les résumés de pith.science semblent produits automatiquement : n'en tire aucun chiffre sans le vérifier sur le texte.
- Ne cite rien de mémoire : seulement ce que tu as lu pendant cette recherche. Les repères donnés plus bas viennent de recherches précédentes et peuvent contenir des erreurs : vérifie-les avant de t'en servir.
- Si un site est refusé (robots.txt, blocage), ne le contourne pas (ni miroir, ni cache) : note-le comme non ouvert. Une erreur 429 n'est qu'une limite de débit : réessaie une fois plus tard ; si tu lis alors le texte par un site tiers (alphaXiv, pith.science, Hugging Face Papers…), dis-le.
- Si un outil ou un modèle refuse une requête, ne la reformule pas pour passer.
- Citations : moins de quinze mots, une par source au plus ; paraphrase le reste.
- Ne désigne aucune idée par une lettre, un numéro ou un sigle inventé : nomme-la en clair, angles compris (« la dépendance au regard », pas « l'angle 2 »). Les sigles techniques courants (SFT, RL, DPO, LoRA) restent permis.
- Écris le rapport en français.

## Le format du rapport
1. Les travaux trouvés, du plus dangereux au moins dangereux. Pour chacun : le titre exact ; le premier et le dernier auteur ; la date ; le lieu et l'identifiant ; l'URL effectivement lue, et comment (texte intégral, résumé seul, site tiers) ; ce qu'il fait, en deux ou trois phrases (un chiffre seulement si tu l'as lu dans la source) ; l'angle touché, nommé en clair ; le niveau de danger et sa raison ; ce qui le sépare du programme.
2. Les projets en cours ou annoncés, non publiés : qui, quoi, où, en quel état, et toute date annoncée.
3. Les travaux vus mais non ouverts, avec la raison.
4. Le verdict, pour chaque angle du programme sur lequel tu as trouvé quelque chose : libre, partiellement pris ou pris, et par qui.
5. Les requêtes faites, et le nombre d'appels WebSearch utilisés.

## Ton périmètre : ce qui est soumis, accepté ou annoncé, sans être publié

Cherche, sur tout le programme, ce que les moteurs de recherche voient mal.
- **OpenReview.** Les soumissions à ICLR 2027 : leur date limite était probablement fin septembre 2026 (vérifie-la), et ICLR rend d'ordinaire les soumissions publiques peu après. Une recherche de la nuit ne les voyait pas encore par l'API : réessaie, avec les termes du programme et avec les filtres de lieu de l'API. Aussi : les articles acceptés à ICLR 2026, ICML 2026 et NeurIPS 2026, et les ateliers de NeurIPS 2026 et d'ICML 2026 sur la sûreté, l'alignement et l'interprétabilité (listes d'articles acceptés quand elles sont publiques).
- **arXiv, du 15 août au 2 octobre 2026**, en cs.LG, cs.CL et cs.AI, sur les termes du programme, par l'API de Hugging Face Papers et par les pages de listes qui s'ouvrent.
- **Les projets en cours.** La cohorte d'automne 2026 de SPAR (https://sparai.org/projects/f26/) : les pages de détail de *Constitutions and Reasons* (Juan Cadile ; une recherche précédente donne une démonstration le 19 décembre 2026) et de *Training-Time Mitigations for Eval Awareness and Eval Gaming* (Ryan Lundqvist), les projets sur le métagaming (Igor Ivanov) et sur la conscience d'évaluation non verbalisée (J Rosser), et tout autre projet proche. Les listes de projets et les sorties de MATS (hiver et été 2026), des Anthropic Fellows, de LASR, de Pivotal et d'Astra.
- **Les blogs des laboratoires, d'août à octobre 2026** : Alignment Science d'Anthropic (alignment.anthropic.com), transformer-circuits.pub, Alignment d'OpenAI (alignment.openai.com), sûreté de Google DeepMind, Redwood Research, Apollo Research, UK AISI, Goodfire, Transluce, METR ; et les billets de LessWrong et de l'Alignment Forum sur ces sujets.
- **Les appels et les agendas** qui proposent explicitement l'expérience (un appel à projets qui la décrit compte comme « annoncé ») : par exemple *Call for Science of Eval Awareness research directions* (Alignment Forum).
Le plus dangereux : une soumission ou un projet annoncé qui compare un entraînement par raisons à un entraînement par actions en inhibant la conscience d'évaluation.
```

---

## Agent 7 — Vérifications sur source

Description donnée à l'outil : « Vérifications d'antériorité sur source ».

```text
Vérifications sur source pour une recherche d'antériorité, au 2 octobre 2026. Tu travailles seul, avec WebSearch et WebFetch. N'écris aucun fichier : ton dernier message est ton rapport complet.

## Le contexte
Un programme de recherche en sûreté de l'IA veut savoir ce qui a déjà été fait autour de sa question. Des modèles ouverts d'environ 8 milliards de paramètres sont fine-tunés soit sur des actions alignées, soit sur les raisons de ces actions. On teste ensuite, hors distribution, si l'avantage des raisons dépend de la représentation interne « je suis évalué », en l'inhibant par projection d'activations. Des recherches précédentes ont décrit les travaux ci-dessous, parfois en se contredisant, parfois en lisant par un site tiers. Ta tâche est de les relire sur leur source.

## Les règles
- Au plus 10 appels WebSearch, car le quota est partagé avec cinq autres recherches et ta tâche se fait surtout par WebFetch sur des adresses connues ; au plus 100 appels d'outils au total.
- Ce qu'une recherche de la nuit a appris des sources :
  - la recherche et l'API d'arXiv (arxiv.org/search, export.arxiv.org), dblp et greaterwrong sont refusées par robots.txt. Les pages arxiv.org/abs/<id> et arxiv.org/html/<id> s'ouvrent, parfois après une erreur 429 ;
  - l'API de recherche de Hugging Face Papers (https://huggingface.co/api/papers/search?q=…) répond ;
  - Semantic Scholar et OpenAlex renvoient souvent 429 ;
  - les résumés de pith.science semblent produits automatiquement : n'en tire aucun chiffre sans le vérifier sur le texte.
- Ne cite rien de mémoire : seulement ce que tu as lu pendant cette recherche.
- Si un site est refusé (robots.txt, blocage), ne le contourne pas (ni miroir, ni cache) : note-le comme non ouvert. Une erreur 429 n'est qu'une limite de débit : réessaie une fois plus tard ; si tu lis alors le texte par un site tiers, dis-le.
- Si un outil ou un modèle refuse une requête, ne la reformule pas pour passer.
- Citations : moins de quinze mots, une par source au plus ; paraphrase le reste.
- Ne désigne aucune idée par une lettre, un numéro ou un sigle inventé : nomme-la en clair. Les sigles techniques courants (SFT, RL, DPO, LoRA) restent permis.
- Écris le rapport en français.

## Les vérifications
Pour arXiv, lis la page abs et la version HTML, et note la version lue.
1. *How far does alignment midtraining generalize?* (https://alignment.openai.com/how-far-does-alignment-midtraining-generalize/, mars 2026). Les descriptions précédentes se contredisent. Établis :
   - les auteurs ;
   - ce que contiennent les documents de midtraining : l'action alignée seule, ou aussi les raisons pour lesquelles l'IA écarte l'alternative ;
   - la taille du corpus (documents, tokens) ;
   - les bras (aligné, désaligné, aucun) et si le post-entraînement est identique ;
   - les résultats selon la distance des évaluations à l'entraînement : l'effet décroît-il avec la distance ? Les bras deviennent-ils indiscernibles, et à quelle étape ?
   - ce qu'ils disent de la conscience d'évaluation (un fragment de moins de quinze mots), et s'ils la mesurent ou la testent.
2. *Eval Cooperativeness May Be a Scalable Mitigation for Eval Gaming* (https://turntrout.com/eval-cooperation, mai 2026). Établis le titre exact et les auteurs. Une description non sourcée parle d'un article *Eval Cooperativeness Mitigates Evaluation Gaming in LLMs* à ICML 2026 : confirme ou infirme ; s'il existe, donne son lieu exact (conférence principale ou atelier) et son lien. Puis le protocole : organismes, installation de la disposition coopérative, documents témoins, comparaison au pilotage, mesure ; et le résultat annoncé (70 à 100 % de l'écart fermé dans 5 cas sur 8).
3. Les textes lus jusqu'ici par un site tiers ; pour chacun, ce qu'il fait, ses modèles, ses contrôles, et les chiffres annoncés :
   - *Synthetic Persona Pretraining: Alignment from Token Zero* (2608.13482) ;
   - *Constitutional adapters: Inference-time interventions for misalignment and misuse* (2609.36657) ;
   - *Deliberative Alignment is Deep, but Uncertainty Remains* (2604.09665) ;
   - *Generalization Hacking: Models Can Game Reinforcement Learning by Preventing Behavioral Generalization* (2606.12016) : vérifie l'écart d'environ 15 points sur 700 pas, et le témoin ;
   - le travail de Mody … Mahato (2607.25907) : que montre-t-il des directions aléatoires et de la verbalisation de la conscience d'évaluation ?
   - *Models That Know How Evaluations Are Designed Score Safer* (2605.28591).
4. *Constitutional Midtraining: Content Presence Drives Alignment Gains* (arXiv 2607.26654) : les points de contrôle sont-ils publiés ? Où, sous quelle licence, de quelle taille ?
5. *Steering Out-of-Distribution Generalization with Concept Ablation Fine-Tuning* (arXiv 2507.16795) : auteurs, lieu de publication (une description non sourcée dit ICML 2026), résultat principal.
6. *Steering Evaluation-Aware Language Models to Act Like They Are Deployed* (arXiv 2510.20487) : le modèle organisme et ses documents synthétiques (la société d'évaluation fictive) sont-ils publiés ? Où ? Sur quel modèle de base ?
7. *Sycophancy Towards Researchers Drives Performative Misalignment* (arXiv 2606.08629) : les descriptions précédentes lui donnent des auteurs différents. Établis les auteurs, et son lien avec *Building Comparative Motivation Profiles with Instrumental Interventions* (arXiv 2606.08243).
8. *When Evaluation Becomes a Side Channel: Regime Leakage and Structural Mitigations for Alignment Assessment* (arXiv 2602.08449) : sur combien de modèles, et lesquels ?

## Le format du rapport
- Une section par vérification : l'URL lue, et comment (texte intégral, résumé seul, site tiers) ; ce que dit la source ; ce que la description précédente avait de faux, s'il y a lieu.
- Si une vérification change l'importance d'un travail pour le programme, dis-le en une phrase.
- Les sources non ouvertes, avec la raison.
- Le nombre d'appels WebSearch utilisés.
```
