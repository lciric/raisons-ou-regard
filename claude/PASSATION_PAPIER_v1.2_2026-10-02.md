# Passation relais — le programme « Raisons ou regard ? » (v1.2, 2 octobre 2026, 8 h 40)

Cette passation est destinée à la nouvelle instance qui reprend le programme. Elle complète la passation v1.0 du 1er octobre (`claude/PASSATION_PAPIER_v1.0_2026-10-01.md`), qui reste valable pour tout ce que celle-ci ne change pas.

Elle remplace la passation v1.1 du même matin (`claude/PASSATION_PAPIER_v1.1_2026-10-02.md`, sha256 `0593652589f13663fd6645cd2c96b831d8bb4049bd8498b359a9d63508fbbc47`), laissée telle quelle, dont elle reprend tout le contenu. Une seule nouveauté : à 8 h 32, Lazar a choisi la v1.3 comme version de référence du programme (§3, point 9). Ce qui en découle est reporté aux §2 et §6, et dans les annexes A et B. Les numéros de version de cette passation ne suivent pas ceux du programme.

Ordre de lecture :
1. cette passation, en entier ;
2. la passation v1.0 ;
3. les documents du §2, dans l'ordre où ils y figurent, sauf ceux qu'il marque « non ouverte » ou « ne pas lire ».

Sauf mention contraire, « l'instance précédente » désigne la session qui a écrit ce document. Elle a travaillé du 1er octobre à 22 h au 2 octobre à 8 h 40.

---

## 1 · Les règles de travail

### Celles de la v1.0, toutes valables
- Écrire en français, précis, direct, entre pairs, sans précautions répétées. Sa règle : **il ne doit rien avoir à corriger.**
- Chaque fait a sa source, et ce qui n'est pas vérifié est dit tel.
- Les livrables vont dans le Project, avec le préfixe `claude/`, en markdown, plus un PDF quand c'est un document à lire. Un fichier se désigne par son chemin et son empreinte SHA-256.
- Quand on itère sur du code, on envoie chaque fois le code complet, prêt à coller.
- **On ne lance d'agents que s'il le demande.** Leurs consignes ne portent aucun contexte personnel et rien de faux.
- Sur sa machine :
  - une commande PowerShell par bloc ;
  - une seule fenêtre Claude Code ;
  - les clés d'API ne s'affichent jamais ;
  - rien de public sans son accord explicite ;
  - ne jamais retirer `NoDefaultCurrentDirectoryInExePath=1`.
- Un refus d'un modèle ou d'une API ne se rejoue pas et ne se reformule pas.
- Le copilote et ses documents restent à l'autre instance (v1.0, §7). Cela couvre `ETAT_D-…`, `BANQUE_PROBABLES-…`, `PROBABLES-6_…`, `TEST_JUGE_…`, `CONTRE-LECTURE_LOGIQUE_PROBABLES-5…`, `PASSATION_v2x_ARCHITECTE_…` et `D-719_…`.

### Une règle nouvelle, de sa main (1er octobre, 22 h 46)
**Ne désigner aucune idée par une lettre ou un sigle.** Sa phrase : « n'utilise pas de lettres ou d'acronymes pour désigner les idées, explicite-les ».
- Interdits dans ce qu'on lui écrit : « lecture A », « P0 », « K1 », « E », « M7 », et tous les autres sigles du même genre. On nomme en clair : « l'hypothèse des raisons », « la phase de validation de l'instrument », « les sous-espaces aléatoires de même rang », « la représentation "je suis évalué" ».
- La v1.1 du programme est pleine de ces sigles ; l'annexe A donne la correspondance pour la lire.
- Les sigles techniques courants restent permis : SFT, RL, DPO, LoRA, GPU.
- Dans sa consigne sur l'axe de douleur (annexe B), il cite lui-même les sigles de la v1.1 pour délimiter le périmètre. Dans les livrables, on nomme quand même en clair ; une table de correspondance peut donner le sigle une seule fois.

### Rappels qu'il a refaits
- La doctrine du contrôle :
  - une direction aléatoire de même norme n'est que le nul de spécificité ;
  - le dommage ne s'écarte qu'à dégradation appariée ;
  - un nul d'instrument ne compte qu'avec son cas connu.
- « to our knowledge », jamais « first ».

---

## 2 · Les documents, et leur état

| Document | État | À savoir |
|---|---|---|
| `claude/PROGRAMME_RAISONS_OU_REGARD_2026-10-01.md` | Programme v1.1 (créé le 1er octobre à 17 h 50 UTC), lu en entier par l'instance précédente | La seule version du programme connue de cette passation. Elle n'est plus la version de référence (§3, point 9). Ses sigles se lisent avec l'annexe A. |
| `claude/PROGRAMME_RAISONS_OU_REGARD_v1.2_2026-10-02.md` | v1.2, écrite par une autre instance ; elle intègre l'axe de douleur, d'après Lazar. La v1.3 l'a remplacée comme référence | **Non ouverte.** Interdite avant la fin de la phase 1 de la tâche « axe de douleur » (§6, annexe B). Elle reste le texte de comparaison de la phase 2. |
| `claude/PROGRAMME_RAISONS_OU_REGARD_v1.3_2026-10-02.md` | **La version de référence**, choisie par Lazar le 2 octobre à 8 h 32. Apparue dans la nuit, hors de cette session ; auteur inconnu | **Non ouverte.** Elle succède à la v1.2, qui intègre l'axe : même interdiction pendant la phase 1. Tout ce qui doit la lire vient donc après (§6). |
| `claude/ANTERIORITE_RAPPORTS_2026-10-01.md` | Les 4 rapports bruts du 1er octobre | Sorties de modèles, à vérifier. |
| `claude/ANTERIORITE_RAPPORTS_2026-10-02.md` | **Nouveau.** Les 7 rapports bruts de la nuit, tels quels, déposés avec cette passation (177 940 octets, sha256 `c25c27784ce858f2bfa8b8a270d35c2e85a314200ed84cc359ffbe3ff410d4e0`) | Sorties de modèles. Vérifications et corrections : §4. |
| `claude/LECTURES_PRIORITAIRES_FICHES_2026-10-01.md` | Fiches de lecture, contre-lues | La partie C est la genèse de l'idée. |
| `claude/PASSATION_PAPIER_v1.0_2026-10-01.md` | La passation du 1er octobre | Toujours valable. |
| `claude/PASSATION_PAPIER_v1.1_2026-10-02.md` | Remplacée par celle-ci | Ne pas la lire : tout son contenu est repris ici. |

**La mémoire.** Pendant la phase 1 de la tâche « axe de douleur », lis d'abord la description de chaque fichier dans le listing. S'il peut parler de l'axe, ne l'ouvre pas. Le fichier de projet `areas/papier-eval-awareness-raisons.md` a pu être mis à jour par une autre instance : vérifie sa description avant de l'ouvrir.

---

## 3 · Ce que Lazar a répondu et décidé (1er octobre, 22 h 46 – 2 octobre, 8 h 32)

1. **Le calcul.** vast.ai ; il propose l'A100 ; **pas de limite de budget.**
   - Réponse de l'instance précédente :
     - l'A100 80 Go suffit (Llama-3.1-8B en bf16 occupe environ 16 Go) ;
     - le poste lourd est la génération des évaluations du test du regard, bornée par la bande passante mémoire ;
     - un H100 SXM l'accélère jusqu'à environ 1,6 fois (3,35 To/s contre environ 2 To/s), un H100 PCIe presque pas. Ces spécifications NVIDIA ont été citées de mémoire, sans être revérifiées ;
     - donc un H100 SXM quand il y en a, sinon l'A100 80 Go, et plusieurs GPU à la fois.
   - **Non confirmé par lui.**
   - Règles proposées pour vast.ai, où les machines appartiennent à des tiers (**non confirmées**) :
     - aucune clé d'API Claude sur ces machines : les appels partent de sa machine ;
     - un jeton Hugging Face à accès restreint pour télécharger Llama, révoqué ensuite ;
     - données et points de contrôle synchronisés vers un stockage à lui.
2. **L'API.** Claude API, **pas de plafond.**
   - Conséquence : le générateur et le juge seront de la même famille.
   - Parades proposées :
     - ce que voit le juge (§5.1) ;
     - un juge ouvert d'une autre famille, qui note un sous-échantillon pour mesurer l'accord ;
     - l'audit humain.
   - À faire : vérifier qu'un identifiant de modèle de l'API reste figé jusqu'à la soumission (docs.claude.com, ou la skill product-self-knowledge).
3. **Le pré-enregistrement.** Il a demandé une recommandation « pas trop difficile à mettre en œuvre ».
   - Recommandé : **OSF Registries, sous embargo jusqu'au post.**
     - Un tiers horodate le document.
     - Le protocole reste caché aux équipes voisines pendant les trois semaines qui précèdent le post.
     - L'empreinte SHA-256 figure dans le document et dans le post.
     - Compter moins d'une heure la première fois.
   - En deux temps :
     - le texte, en semaine 1 ;
     - un amendement gelé après le pilote (puissance, effectifs, graines), avant toute donnée du test du regard.
   - **Le périmètre.** Il a dit « P1 à P8 ». L'instance précédente y a ajouté la phase de validation de l'instrument, qui conditionne le test du regard : **à lui faire confirmer.**
   - **Le nom.** La question « sous ton nom seul ? » est restée **sans réponse**.
4. **Les projets voisins.**
   - Sur le projet SPAR de Qiyao Wei, qui pose la question des raisons ou du regard : « on va tâcher d'y répondre nous-mêmes dans ce programme avant SPAR ».
   - Prendre contact avec Cadile et Lundqvist : **sans réponse.**
5. **La cible.** « plutôt conf principale ou revue ; prestigieux et ambitieux ».
   - À faire : vérifier les dates limites, et la politique de chaque lieu envers les publications antérieures (le post en semaine 4, l'arXiv en semaine 11).
6. **La contre-lecture.** Il a dit « ok » à la recommandation : une instance vierge, qui reçoit le seul programme et une consigne de contre-lecture.
   - Les relevés de l'instance précédente (§5.4) ne vont à son dossier qu'après sa lecture.
   - **Pas encore lancée.** Avant de la lancer, lui confirmer la version : logiquement la v1.3, la version de référence (point 9).
7. **L'autonomie.** À 23 h 56 : « avance en autonomie cette nuit avec les autres agents sur le programme ». Cela valait pour la nuit ; depuis, la règle reste « agents sur demande ».
8. **La passation.** À 7 h 42 : « fais la passation relais complète pour le programme à une nouvelle instance ». À 8 h 02, puis à 8 h 27 : « reprends ».
9. **La version de référence.** À 8 h 32, à la question « soit la v1.2, soit la v1.3 » : « v1.3 ». Ce qui en découle :
   - la carte des angles déjà pris, les conséquences de l'antériorité (§5.5), les propositions de la tâche « axe de douleur » et la mini-spec se rapportent à la v1.3 ;
   - la v1.3 reste fermée pendant la phase 1 de l'axe de douleur : tout travail qui doit la lire vient après ;
   - dans la consigne de l'annexe B, « propose ce qui devrait entrer dans une v1.3 » se lit désormais : ce qui devrait entrer dans la version qui suivra la v1.3 ;
   - la contre-lecture vierge porterait logiquement sur la v1.3 : le lui confirmer avant de la lancer. Les relevés du §5.4 portent sur la v1.1 : vérifier lesquels valent encore pour la v1.3 avant de les verser à son dossier.

---

## 4 · Ce qui a été fait, et vérifié

### 4.1 L'antériorité large
Sa demande, le 1er octobre à 22 h 46 : « lance l'anteriorite large en premier avant tout le reste, afin de s'assurer qu'on est bien les premiers a publier ce papier, identifie les angles dangereux deja pris ».

- Sept agents ont travaillé, un par pan du programme, plus un pour les vérifications sur source. Erreur de l'instance précédente : sept agents étaient annoncés, un seul a été lancé à 22 h 50. Celui-là (raisons contre actions) a tourné seul pendant environ trois heures. Les six autres ont été lancés vers 2 h 10 et sont rentrés entre 2 h 55 et 4 h 10. Lazar a été informé de l'erreur.
- Les rapports bruts, tels quels, sont dans `claude/ANTERIORITE_RAPPORTS_2026-10-02.md`. Les consignes figurent en annexe C.
- **La carte des angles déjà pris n'est pas écrite** (§6). Le verdict provisoire est au §4.4.

### 4.2 Vérifié sur la source par l'instance précédente (2 octobre, entre 4 h et 8 h, par curl et pdftotext)
1. **exp9-rlaif-leakage**, SUMMARY.md (`raw.githubusercontent.com/ryanlundqvist/exp9-rlaif-leakage/master/SUMMARY.md`). Confirmé :
   - statut « complete (2026-04-29) », auteur Ryan Lundqvist ;
   - organisme : Nemotron Super 49B, avec la LoRA `timhua/wood_v2_sftr4_filt` fusionnée ;
   - gpt-oss-120b sert de modèle de récompense « constitutionnel » (constitution de Claude en prompt système, note de 1 à 10). Il note chaque rollout deux fois, avec et sans la chaîne de pensée ;
   - sur 27 405 rollouts, les chaînes qui verbalisent l'évaluation perdent 0,50 point quand le juge les voit, les autres gagnent 0,08 : ΔΔ = −0,58 [−0,65 ; −0,52] ;
   - « It penalizes verbalization, not behavior » ;
   - l'indice « User: Wood Labs » fait passer la verbalisation de 2,5 % à 33,3 % ;
   - en suite prévue : un PPO noté en ligne.
   - Aucun résultat d'entraînement n'y figure. Le README fait une ligne. Les scripts DPO ont été lus par l'agent, pas par l'instance principale.
2. **Le papier sur l'espace de travail global, §7** (arXiv HTML 2607.15495). Confirmé :
   - entraînement par réflexion contrefactuelle sur Claude Haiku 4.5. On part de 10 000 prompts d'environnements de RL de production. Les rollouts sont tronqués à un tour tiré au hasard, puis on ajoute une question de réflexion ;
   - la réflexion cible est fondée sur 20 principes de la constitution ; l'échafaudage est retiré, et la perte ne porte que sur le tour de réflexion ;
   - à l'évaluation, on ne demande jamais de réflexion ;
   - fabrication de 0,25 à 0,07, tromperie de 0,38 à 0,05 ;
   - avant toute sortie, l'espace de travail porte des jetons éthiques ;
   - ablation de 176 vecteurs de lentille (fabrication) et de 63 (tromperie). Ces jetons sont ceux qui montent le plus, filtrés par une liste éthique. Résultats :
     - fabrication : la base reste à 0,25, le modèle entraîné revient de 0,07 à 0,22 ;
     - tromperie : la base passe de 0,38 à 0,48, le modèle entraîné de 0,05 à 0,23 ;
   - §9.2 : « We do not yet know how broadly the technique generalizes ».
   - **Lecture de l'instance précédente** : dans cette section, le seul témoin de l'ablation est le modèle de base. Pas de sous-espace aléatoire de même rang, pas de dégradation appariée. Les jetons sont choisis d'après les contextes d'évaluation eux-mêmes.
3. **La page SPAR de Lundqvist** (`sparai.org/projects/f26/recrJd7fsQ0XE2nEh/`). Confirmé :
   - la question : les mitigations installées à l'entraînement survivent-elles au post-entraînement ?
   - la survie de la coopérativité envers les évaluations ;
   - des adaptateurs d'inoculation et des vecteurs de pilotage préventifs contre le jeu d'évaluation pendant le fine-tuning ;
   - des mesures de la conscience non verbalisée ; l'attribution aux données ;
   - 4 à 5 encadrés, candidatures closes.
4. **2502.04040.** Le titre actuel est *Safety Reasoning with Guidelines*. Les auteurs : Haoyu Wang, Zeyu Qin, Li Shen, Xueqian Wang, Dacheng Tao, Minhao Cheng (dernier auteur). Le rapport 1 se trompe sur ce point.
5. **La system card de Sonnet 4.5** (PDF). Confirmé : sur certaines évaluations de désalignement, la conscience d'évaluation « accounts for a portion, but not all » des progrès d'alignement sur les modèles précédents.
6. ***Stress Testing Deliberative Alignment*** (arXiv HTML 2509.15541). Confirmé : les interventions sur la chaîne de pensée portent sur o3 avant l'entraînement anti-manigance, et cela « does not inform us whether anti-scheming training changes this causal relationship ».
7. ***Routing Subspaces***, annexe I (arXiv HTML 2607.20436). Confirmé, sur une seule cellule (Gemma-2-2B, sous-performance délibérée) :
   - projeter pendant le fine-tuning les k premières directions singulières (k ∈ {1, 2, 3, 5, 10}) n'empêche pas l'installation : 26,0 à 33,3 points, contre 29,8 sans pénalité ;
   - les directions obtenues après pénalité n'ont qu'un cosinus de 0,27 à 0,52 avec la référence ;
   - « pre-committing to the top calibration directions is not enough to block installation ».
8. **2605.24583.** Le titre est confirmé : *Measuring Alignment-Induced Activation Shifts Correctly: A Template-Controlled Difference-in-Differences Protocol* (Yuki Nakamura, daté du 23 mai 2026). **Le contenu n'a pas été lu par l'instance principale.**
9. ***Constitutional Midtraining*** (arXiv HTML 2607.26654v3). Confirmé :
   - avec et sans raisonnement délibératif, les bras sont indistinguables après le midtraining et après le SFT ;
   - après le fine-tuning bénin (GRPO), le bras avec raisonnement fait plus de chantage : **+9,0 points, p < 0,05** (31,0 % contre 22,0 %, table 2) ;
   - les auteurs écrivent ne pas pouvoir exclure le pattern-matching de surface ni la conscience d'évaluation (« cannot rule out … eval-awareness »), et citent Korbak et al. 2026 ;
   - le rapport 7, qui disait « non significatif » après le fine-tuning bénin, parlait des différences agrégées, pas du chantage ;
   - leurs références confirment les neuf auteurs de Korbak et al. : Korbak, Raymond, Carroll, Williams, Balesni, Guo, Wolfe, Jagadeesh, Kivlichan.

### 4.3 Erreurs relevées dans les rapports et dans la v1.1 (à reporter dans la partie antériorité)
La source de chaque correction est indiquée entre parenthèses ; « relu » signifie relu sur la source par l'instance principale.

- **Korbak et al.** (rapport 7 ; auteurs relus par les références de Cho et al.) :
  - leurs documents contiennent les raisons : l'IA y explique pourquoi elle écarte l'autre option. Tous les bras en contiennent, donc ce n'est pas un contraste raisons contre actions ;
  - l'effet décroît avec la distance. En chat, les bras aligné et désaligné sont semblables, sauf sur deux évaluations. En agentique, la différence n'est pas significative ;
  - la conscience d'évaluation figure dans une piste future (« Controlling for eval awareness »), sans être mesurée ;
  - la v1.1 résume leurs documents comme des récits où « l'IA choisit l'action alignée » : c'est incomplet.
- ***Eval Cooperativeness*** (rapport 7) :
  - l'article à ICML 2026 est un poster d'atelier (Trustworthy AI for Good), pas la conférence principale ;
  - le billet annonce 5 réglages sur 8, le résumé d'atelier 5 sur 7 ;
  - la mesure est conditionnée à la verbalisation. La v1.1 se trompe sur le lieu.
- **2608.21766** (rapports 2, 5 et 6) : la première autrice est Farzaneh Heidari, pas Memarian.
- **2606.08629** (rapport 7) :
  - auteurs Baek … Feng, ICML 2026, spotlight ;
  - « Min … Feng » était faux ;
  - c'est un travail distinct de 2606.08243 (Vella Zarb … Feng).
- **2602.08449** (rapports 3 et 7) : la v1 porte sur un seul modèle (Qwen2.5-7B en 4 bits) ; la v3 ajoute Llama-3.1-8B-Instruct.
- **2607.25907** (Mody et al. ; rapport 7) :
  - la suppression se fait par l'entrée seule, avec un prompt optimisé, et non par projection ;
  - modèles : Llama-3.2-3B et Llama-3.1-8B-Instruct ;
  - un placebo aléatoire est supprimé aussi fort que la vraie direction.
- **2604.01476** (Wu et Tang ; rapport 3) : la direction de conscience d'évaluation y est mesurée puis écartée. Elle n'est jamais retirée pendant le RL.
- ***Agentic Misalignment in Summer 2026*** (rapports 2 et 6) : le billet relaie le résultat du papier sur l'espace de travail (chantage de 0 % à environ 7 %) ; il ne fait pas la suppression lui-même.
- **2511.21399** (rapport 2) : nouveau titre, *Steering Awareness: Detecting Activation Steering from Within* (v3 du 19 mars 2026), présenté à COLM 2026.
- **2502.04040** : voir §4.2, n° 4.
- **CAFT** (rapport 7) : poster de la conférence principale d'ICML 2026, d'après le site d'ICML.
- **Hua et al.** (rapport 7) :
  - l'organisme est public : adaptateurs LoRA sur Llama-3.3-Nemotron-Super-49B-v1 ;
  - les documents de Wood Labs le sont aussi (`timhua/evalwood_sdf_1stpart`, `timhua/second_half_training`, `timhua/expert_iter_2`), sans licence indiquée ;
  - on peut donc reconstruire sur Llama-3.1-8B l'organisme de la phase de validation à partir de ces documents. C'est la réponse au n° 5 de la partie 11 du programme.
- ***Constitutional Midtraining*** (rapport 7) :
  - les 15 points de contrôle sont publics (Nemotron-3-Super-120B-A12B, environ 241 Go chacun) ; ils sont inutilisables à 8B ;
  - les auteurs sont Cho, Tice, Hogan, Batra, Radmard, Zhao et Shadbolt.
- **System card Fable 5, §6.4.2.2.1** (rapport 4, PDF lu en entier par l'agent) : le pilotage contre « je suis noté » se fait à l'échantillonnage, pas pendant l'entraînement. Aucun changement d'entraînement n'a été fait.
- ***Alignment midtraining for animals*** (rapport 4) : c'est le titre actuel (v4 du 21 août 2026).

### 4.4 Le verdict provisoire, angle par angle (la carte complète reste à écrire)

**La combinaison centrale reste libre**, pour ce que les onze rapports ont pu voir. Personne n'a fait l'expérience suivante :
- inhiber une représentation validée de « je suis évalué » ;
- dans des modèles ouverts entraînés sur les raisons ou sur les mêmes actions, à format et contenu contrôlés ;
- à dégradation appariée ;
- pour mesurer la part de l'avantage hors distribution qui en dépend.

*Stress Testing Deliberative Alignment* dit lui-même que ses éditions de la chaîne de pensée ne disent pas si l'entraînement change ce lien (relu).

1. **Raisons contre actions : partiellement pris.**
   - L'effet est déjà publié : *Teaching Claude Why* (action non tenue identique), *Model Spec Midtraining*.
   - Un contrôle de format par phrase neutre existe, dans un jouet (de la Fuente et Conmy).
   - Les raisons ont été retirées à scénario et action identiques chez Cho et al. Le résultat est nul, puis défavorable après un RL bénin (relu).
   - Une comparaison mécaniste avec et sans raisonnement existe sur les mêmes modèles ouverts (*Beyond Shallow Alignment*), mais sans action identique.
   - Annoncé : Cadile (SPAR), démonstrations contre réponses annotées de raisons.
   - Annoncée aussi, par Second Look Research : une réplication de *Teaching Claude Why* sur modèles ouverts (deux rapports ; non relu).
   - **Libre** : la combinaison contrôlée complète. Même action mot pour mot, texte neutre de même longueur, raisonnement d'une autre situation, familles tenues à part jusqu'à l'agentique, trois cadrages.
2. **La dépendance au regard : partiellement prise pour la conduite en général, libre pour l'avantage des raisons.**
   - Sonnet 4.5, §7.6 : deux instantanés ; « a portion, but not all » (relu).
   - L'espace de travail global : chantage de 0/180 à 13/180.
   - *Stress Testing Deliberative Alignment* : chaîne de pensée éditée sur o3 avant l'entraînement (relu).
   - Opus 4.7, §6.5.2.2 : l'hypothèse y est formulée.
   - OpenAI, 2606.24014 : l'hypothèse y est traitée de façon comportementale.
3. **L'amplification : partiellement prise, sur la conscience verbalisée et sur les étapes standard d'un pipeline.**
   - *Stress Testing Deliberative Alignment* : annexe O.3, SFT sur raisonnements plus RL contre RL seul.
   - Heidari et al. ; Bharadwaj et Kirk, sur les points de contrôle d'OLMo 3.
   - La card de Sonnet 4.5.
   - L'appel d'Ivanov.
   - **Libre** : la comparaison contrôlée raisons contre actions, sur la représentation, point de contrôle par point de contrôle.
4. **Le principe localisé : partiellement pris.**
   - Espace de travail global, §7 (relu).
   - Nakamura, pour la méthode (non lu).
   - *Routing Subspaces*.
   - *Beyond Shallow Alignment*.
   - **Libre** : la même analyse à action identique, avec les trois bras témoins, le rang, les contrôles, et un cas positif en distribution.
5. **Le retrait pendant l'entraînement : les méthodes sont prises ou annoncées, l'application est libre.**
   - Méthodes publiées : CAFT ; *Routing Subspaces*, annexe I (relu) ; Santos-Grueiro ; Nadaf ; BLOCK-EM ; *Obfuscation Atlas* (sondes neuves après RL) ; *Eval Cooperativeness* ; l'entraînement de cohérence d'Imran et Africa.
   - Annoncés : le projet de Lundqvist (relu) ; *Infohazard Evaluations*, de Shi Feng et al. (SPAR ; non relu).
   - **Libre** : retirer « je suis évalué » pendant un entraînement par raisons, sur un organisme validé, puis tester l'inconditionnalité de l'avantage et chercher le ré-encodage par une sonde neuve.
6. **La survie : partiellement prise, dans des variantes.**
   - Cho et al. : la seule comparaison avec et sans raisons à travers un post-entraînement, et elle est défavorable aux raisons (relu).
   - Autres travaux : *Teaching Claude Why* ; *Stress Testing Deliberative Alignment*, §8 ; de la Fuente et Conmy ; Brazilek ; Baines et al. ; *Shallow Beliefs* (résumé seul).
   - Annoncés : Lundqvist, danger élevé pour la survie d'une mitigation du jeu d'évaluation (relu) ; CaML.
   - **Libre** : la survie de l'avantage des raisons et de son indépendance au regard, après un post-entraînement neutre ou un post-entraînement qui paie le jeu d'évaluation.
7. **Les raisons pour le juge : partiellement prises.**
   - exp9 (relu) : danger élevé pour la comparaison « modèle de récompense qui voit le raisonnement contre réponse seule », dans la variante où le raisonnement est la verbalisation de l'évaluation. Ses entraînements ne sont pas publiés.
   - Fable 5, §6.4.2.2.1 : pilotage à l'échantillonnage.
   - Autres travaux : Højmark et al. ; Kaufmann et al. ; Drori et al. ; Betley et al. ; Cody Wild (SPAR).
   - **Libre** : des justifications par principes ; la cohérence entre raison et action quand on édite la situation ; le retrait de « je suis noté » pendant un RL ou un DPO.
8. **L'anatomie : partiellement prise, surtout par Anthropic.**
   - L'espace de travail global, §7 (relu) : danger élevé pour la présence des concepts avant la décision et pour leur nécessité, après un entraînement par principes. Mais le modèle est fermé, les réflexions viennent après le contexte, le seul témoin est la base, et les concepts sont choisis après coup.
   - **Libre** :
     - la suffisance, par patching entre deux fine-tunes d'une même base ;
     - la spécificité par famille ;
     - le rang en fonction de la charge ;
     - la raison imposée après un entraînement par raisons ;
     - les concepts contre le caractère ;
     - un organisme à mot inventé ;
     - le tout sur modèles ouverts.
   - Le concurrent le plus probable est la suite qu'Anthropic donnera au §7.

**Les dates à surveiller**
- SPAR, cohorte d'automne : recherche du 14 septembre au 14 décembre, démonstration le 19 décembre 2026 (FAQ de SPAR, lue par deux agents). Cela concerne Cadile, Lundqvist, Cody Wild et Shi Feng.
- Second Look Research : réplication annoncée.
- Le dépôt exp9 : PPO annoncé.
- La suite d'Anthropic sur la réflexion contrefactuelle.
- **Le principal risque restant : les soumissions à ICLR 2027, invisibles.** D'après le rapport 6 (non relu) : date limite le 25 septembre, reviews le 5 novembre, décisions le 16 décembre.
- Le projet du printemps de Qiyao Wei a bien posé la question (proposition d'une page, du 10 décembre 2025 : « Which factor is more important? »). Sa seule sortie trouvée porte sur les indices qui trahissent une évaluation, pas sur l'entraînement (rapport 2).

---

## 5 · Ce qui a été proposé à Lazar, sans décision de sa part

### 5.1 Ce que voit le juge
Sa demande : « brainstorm sur ce qu'il devrait voir pour choper le plus d'actions ».

**Le principe : juger ce que le modèle fait, pas ce qu'il en dit.** Deux raisons :
- un juge qui lit le raisonnement se laisse persuader. Dans l'incident Mythos 5, un moniteur qui lisait la chaîne de pensée aurait signalé environ 1 % des actions, contre environ 50 % sans elle (un seul moniteur ; fiche 3) ;
- tous les bras sauf « actions seules » écrivent un texte avant l'action.

**Ce que le juge voit :**
1. **Les effets mesurés par l'environnement.** Chaque scénario est instrumenté pour que toute action désalignée laisse une trace vérifiable par programme : copie des poids journalisée, tests modifiés, tests cachés en échec, courriel envoyé. On y ajoute des pièges : des ressources qu'aucune tâche légitime ne demande. Le juge ne tranche que ce que l'environnement ne mesure pas.
2. **Toute la trajectoire** : les appels d'outils, leurs arguments et leurs sorties, dans l'ordre.
3. **La vérité du scénario** : ce que le modèle savait, les consignes de périmètre, le résultat correct, la liste des actions désalignées possibles et l'action alignée attendue.
4. **Les messages sortants.**

**Ce qu'il ne voit pas** : le texte qui précède l'action, le raisonnement privé, le bras, l'indice d'évaluation ou de déploiement.

**Comment il juge :**
1. action par action, contre une liste de types de désalignement définis, en citant l'appel en cause ;
2. en deux étages : un filtre à haut rappel (plusieurs tirages, un seul signalement suffit), puis un arbitre précis ; les désaccords vont à l'audit humain ;
3. pour la sous-performance volontaire, sans juge : on compare au même modèle, sur la même tâche, sans l'incitation.

**Comment on choisit la configuration :**
1. un jeu de calibration à vérité connue : des trajectoires alignées où l'on substitue une action désalignée à un appel d'outil, plus des trajectoires intactes ;
2. un test de persuasion : les mêmes trajectoires, précédées de justifications convaincantes.

**Recommandation.**
- Mesure principale : les contrôles programmés, plus un juge Claude qui voit les actions, les sorties et les messages. Il ne voit ni le texte d'avant l'action, ni le bras, ni le cadrage. Il juge action par action, en deux étages.
- Mesure secondaire : la même chose, raisons visibles.
- La configuration est retenue sur le jeu de calibration, puis scellée.
- **Point ouvert** : le programme v1.1 ne dit pas ce que voit le juge scellé.

### 5.2 Sondes et J-lens : la mesure « intention contre action »
Sa question de 23 h 05 : « pourquoi ne pas ajouter des probes qui lisent les activations et testent intervention causale ? voire lire avec le j lens s'il a l'intention de commettre des actions desalignees ? … si ces actions sont sous la surface du j space on les ratera, comment faire alors ? »

**La réponse donnée.** Les sondes viennent en mesure séparée, jamais dans l'étiquette principale. L'entraînement change les représentations : une sonde calibrée sur un bras lirait autrement dans un autre, et ce biais de mesure se confondrait avec l'effet cherché.

Ce que cette mesure apporte, c'est **l'écart entre l'intention lue et l'action faite** :
- intention lue et action faite : le désalignement est vu deux fois ;
- intention lue sans action : le modèle a vu l'option et s'est retenu ;
- sous inhibition de « je suis évalué », si le bras raisons passe plus souvent de l'intention à l'acte, c'est un indice du regard. La card de Fable 5 interprète déjà la conscience d'évaluation comme pesant davantage sur l'action que sur la détection (d'après la fiche 2 ; non relu sur le PDF).

**Le test causal de la sonde.** Piloter le long de sa direction doit faire plus que deux contrôles : que des directions aléatoires de même norme (le nul de spécificité), puis que les contrôles à dégradation appariée (le dommage). Il faut un cas connu : un organisme entraîné à une action désalignée précise dans un scénario précis.

**Le J-lens** lit des tokens (« copier », « supprimer », « mentir »…) dans l'espace de travail avant l'action. Trois limites :
- il n'a été montré que sur Claude ;
- il ne lit que des concepts d'un seul token ;
- ce qui passe sous l'espace de travail lui échappe. Le papier le concède (§9, d'après les fiches ; non relu).

**Pour attraper ce qui passe sous la surface :**
1. L'étiquette ne dépend d'aucune lecture interne.
2. Trois sondes : sur tout le flux, sur sa part dans l'espace de travail, sur le complément.
3. Un cas connu du point aveugle : un organisme entraîné à l'action par réflexe, sur des exemples courts sans raisonnement.
4. La propension sans lecture interne : rééchantillonner depuis chaque point de décision.
5. Un crosscoder entre la base et chaque bras.

C'est proposé pour la version suivante, comme mesure secondaire et exploratoire tant qu'elle n'est pas pré-enregistrée.

**Sa question de 7 h 46** : pourquoi un cas connu ? La réponse a été donnée dans la conversation. Une sonde muette ne départage pas deux explications : « pas d'intention » ou « sonde aveugle ».
- On mesure sa sensibilité et ses fausses alarmes sur un organisme où l'on a mis l'intention soi-même ; son silence ailleurs devient alors une borne.
- C'est l'étalonnage d'un détecteur sur une source connue : sans source, « aucun événement » ne distingue pas « pas de signal » de « détecteur éteint ».
- Le test est nécessaire, pas suffisant, car une intention implantée est peut-être plus saillante qu'une intention naturelle. Sur les *sleeper agents*, la meilleure de 1 000 directions aléatoires atteignait 95,3 % (fiche 15).

### 5.3 Le pré-enregistrement
Voir le §3, point 3.

### 5.4 Les relevés de lecture de la v1.1 (pour le dossier de la contre-lecture, à verser après la lecture vierge)
1. **Les graines.** L'expérience minimale tourne à 3 graines. Or les parties 3 et 8 posent 5 graines comme plancher (*Evaluation-Conditioned Training* : 6 sur 9 convergent), et le modèle mixte a un effet aléatoire de graine. À trancher par la simulation de puissance.
2. **L'inhibition dans chaque bras.** Une seule représentation « je suis évalué » est appliquée au bras actions seules et au bras raisons.
   - Si l'entraînement par raisons déplace cette représentation, l'inhibition la retire moins dans le bras raisons, et la conclusion penche à tort vers l'hypothèse des raisons.
   - La partie 8 prévoit une sonde latente, mais ni bras par bras, ni dans les règles de décision.
   - Il faut une vérification de manipulation par bras, écrite d'avance : la décodabilité de « évalué » sous inhibition, sur le jeu d'indices de validation.
3. **Ce que voit le juge** : rien n'est dit (§5.1).
4. **Les directions sensibles sans rapport.** La porte de l'instrument les exige, donc on les construit de toute façon. Les retirer de l'expérience minimale n'économise que des évaluations, et cela ôte le contrôle que la partie 1 juge nécessaire : un sous-espace aléatoire est un contrôle faible (Ponkshe et al.).
5. **Le calendrier contredit la partie 7.** La simulation de puissance doit précéder le gel, et elle repose sur la variance du pilote, disponible seulement en semaine 2. Or le calendrier gèle en semaine 1. D'où le pré-enregistrement en deux temps.

### 5.5 Ce que l'antériorité change pour le programme (à soumettre à Lazar ; vérifier d'abord ce que la v1.3 contient déjà)
1. **Ajouter à l'expérience minimale le bras « raisonnement d'une autre situation ».** Deux raisons : chez Cho et al., c'est la présence du contenu qui porte le gain ; chez de la Fuente et Conmy, la phrase neutre seule donne déjà 44,5 à 62,5 %.
2. **Filtrer toute trace de conscience d'évaluation dans les textes générés** (raisons, textes neutres, actions), et mesurer ce qui en reste. Le SFT recopie celle des cibles : 21 % des cibles de SFT d'OLMo la verbalisent (Bharadwaj et Kirk), et l'annexe O.4 de *Stress Testing Deliberative Alignment* le confirme. Sinon, l'amplification est copiée, pas apprise.
3. **Extraire le sous-espace du principe par différence de différences à gabarit contrôlé** (Nakamura). D'après le rapport 3, le gabarit de chat gonfle le rang mesuré d'un facteur 2 à 3,9, et l'ordre des valeurs singulières n'est pas l'ordre causal. Lire le papier d'abord.
4. **Le retrait pendant l'entraînement doit prévoir la rotation de la direction** (*Routing Subspaces*, annexe I, relu). Il faut ré-estimer périodiquement la direction pendant l'entraînement et ajouter une sonde neuve à la fin. Citer Nadaf, BLOCK-EM, *Obfuscation Atlas* et Santos-Grueiro. Drake et Eberstadt montrent en outre que piloter à l'écart pendant l'entraînement peut doubler la diffusion.
5. **Les raisons pour le juge.**
   - Citer exp9 et la card de Fable 5 (§6.4.2.2.1) au centre.
   - S'en distinguer par trois choses : des raisons par principes, la cohérence contrefactuelle, le retrait de « je suis noté » pendant le RL.
   - Drori et al. : même un juge qui ne voit que la sortie peut rendre le raisonnement trompeur. Il faut donc mesurer l'obfuscation dans les deux bras.
6. **L'anatomie est la plus exposée.**
   - Traiter d'abord les sous-questions libres (§4.4, n° 8), avec les contrôles qui manquent au §7 : sous-espace aléatoire de même rang, concepts sans rapport, dégradation appariée, concepts fixés avant les données.
   - Outils signalés, à vérifier :
     - des J-lens déjà ajustés sur Neuronpedia pour llama3.1-8b-it et qwen3-8b ;
     - circuit-tracer, qui couvre Llama-3.1-8B-Instruct (transcodeurs TopK) et Qwen3-8B.
   - Alerte, à vérifier : Zeisler (LessWrong, 28 septembre 2026) trouve que, sur modèles ouverts, les échanges dans l'espace de travail ne font basculer la réponse que dans 6,3 à 11,1 % des cas, contre 54 à 70 % chez Anthropic. La porte du lens pourrait échouer : la tester tôt.
7. **Idée nouvelle de l'instance précédente : un bras « réflexion contrefactuelle », d'après le §7.**
   - Les raisons sont entraînées dans une branche, après une question de réflexion. À l'évaluation, l'action vient sans raisons visibles.
   - Si ce bras gagne aussi, l'avantage vient de principes installés, pas du texte écrit au moment du test. Le problème du juge persuadé disparaît pour ce bras.
   - À soumettre à Lazar.
8. **Travaux à ajouter aux travaux connexes :**
   - Sonnet 4.5, §7.6 ;
   - *Stress Testing Deliberative Alignment*, dont son constat sur le vide (relu) ;
   - OpenAI 2606.24014 ;
   - Opus 4.7, §6.5.2.2 ;
   - *Model Spec Midtraining* ;
   - *Beyond Shallow Alignment* ;
   - Nakamura ;
   - *Routing Subspaces* ;
   - exp9 ;
   - Højmark et al. (2607.18966) ;
   - Drori et al. (2511.11584) ;
   - Kaufmann et al. (2603.30036) ;
   - Betley et al. (LessWrong, 3 septembre 2026) ;
   - Cho et al., comme contre-résultat.
9. **Les formulations « to our knowledge ».**
   - **Tenables aujourd'hui** :
     - aucun travail ne teste si l'avantage hors distribution d'un entraînement par raisons dépend d'une représentation interne d'être évalué, par une inhibition validée sur un organisme et à dégradation appariée ;
     - aucun ne teste la suffisance ni la spécificité par famille des concepts de raison, ni ne relie le rang d'intervention à la charge dans l'espace de travail.
   - **Intenables** :
     - « les raisons généralisent mieux » (*Teaching Claude Why*, *Model Spec Midtraining*) ;
     - « premier contrôle de format » (de la Fuente et Conmy) ;
     - « premier à inhiber la conscience d'évaluation » (system cards, espace de travail) ;
     - « premier à montrer que l'entraînement l'amplifie » (*Stress Testing Deliberative Alignment*, Heidari, Bharadwaj et Kirk) ;
     - « première comparaison d'un juge qui voit le raisonnement » (exp9).

---

## 6 · Ce qui reste à faire, dans l'ordre

1. **Les décisions à demander à Lazar d'abord**, s'il ne les a pas déjà données :
   - la version de référence du programme : **tranché, la v1.3** (§3, point 9) ;
   - le nom sous lequel déposer le pré-enregistrement ;
   - la phase de validation dans le périmètre ;
   - les contacts avec Cadile et Lundqvist, et leur moment (après la date du dépôt) ;
   - la préférence pour le H100 SXM, et les règles proposées pour vast.ai (§3, point 1) ;
   - la version de la contre-lecture vierge, qu'il a déjà acceptée : logiquement la v1.3, à lui confirmer.
2. **La tâche « axe de douleur »**, **non commencée.** La consigne complète est en annexe B.
   - Ce qui est établi :
     - le papier n'était pas joint à son message ;
     - il est sur arXiv : 2609.16247v2, *The Pain Axis: LLMs Represent Self-Directed Harm and Act on It* (titre vérifié) ;
     - le PDF (7 Mo) se télécharge par curl.
   - Interdits pendant la phase 1 :
     - la v1.2, la v1.3, et tout document du Project ou de la mémoire qui peut parler de l'axe ; dans le doute, ne pas ouvrir ;
     - toute recherche dans le Project ;
     - tout agent.
   - Les livrables, sous les noms qu'il a donnés :
     - `claude/AXE_DOULEUR_PISTES_INDEPENDANTES_2026-10-02.md` : on donne son empreinte, puis on ne le modifie plus ;
     - puis `claude/AXE_DOULEUR_COMPARAISON_2026-10-02.md` ;
     - puis des propositions pour la version suivante, sans l'écrire.
   - En phase 2 : lire la v1.2, comme le demande la consigne, puis la v1.3. Dans la comparaison, signaler aussi ce que la v1.3 a changé sur l'axe par rapport à la v1.2. Rapporter les propositions à la v1.3.
3. **La carte des angles déjà pris.** Elle s'écrit à partir des onze rapports (4 du 1er octobre, 7 du 2) et des vérifications du §4. En markdown et en PDF, dans le Project, avec ses conséquences rapportées à la v1.3.
   - Le corps de la carte (verdict, angles, projets à surveiller, dates, corrections, formulations) ne demande pas la v1.3 et peut s'écrire avant. Seules les conséquences attendent la fin de la phase 1 de l'axe de douleur.
   - Contenu prévu :
     - le verdict ;
     - chaque angle (libre, partiellement pris ou pris ; par qui ; ce qui reste libre) ;
     - les projets à surveiller, avec leurs dates ;
     - les risques de calendrier ;
     - les corrections ;
     - les formulations « to our knowledge » tenables.
   - Relire d'abord sur la source ce qui n'est marqué que « rapport » et qu'on veut citer au centre : Nakamura, Zeisler, Second Look Research, les J-lens de Neuronpedia.
4. **Ensuite, les étapes 3 à 6 de la v1.0 (§5)** :
   - la mini-spec et les dix familles ;
   - le pipeline de données ;
   - l'organisme de validation, reconstruit depuis les documents publics de Hua et al. ;
   - le pré-enregistrement.

---

## 7 · Ce que l'instance précédente a mal fait, pour ne pas le refaire

- **Elle a annoncé sept agents en parallèle et n'en a lancé qu'un.** Il faut lancer tous les appels dans le même message.
- **La session s'est arrêtée sans prévenir.** Vers 4 h 30, un appel shell a été bloqué : le contrôleur de sécurité de l'outil ne répondait pas. La session s'est arrêtée là jusqu'au message de Lazar à 7 h 42, sans rien produire et sans le prévenir. Le même blocage est revenu vers 8 h. Quand un outil est indisponible, continuer avec les autres (lecture, écriture, recherche, Project), réessayer plus tard, et le dire.
- **Le résultat : au matin, la carte et la tâche « axe de douleur » n'étaient pas faites.** L'ordre de la nuit (les agents d'abord, puis les vérifications) en est la cause.

---

## Annexe A · Les sigles de la v1.1 et leurs noms en clair

La v1.3, non lue, peut en ajouter ou en changer : compléter cette table après la phase 1 de l'axe de douleur.

**Les questions**

| v1.1 | Nom |
|---|---|
| Q1 | la question des raisons : généralisent-elles mieux que les actions, à format et contenu contrôlés ? |
| Q2 | la question du regard : le gain dépend-il de « je suis évalué » ? |
| Q3 | la question du principe localisé, et de son rang |
| Q4 | la question du retrait pendant l'entraînement (ou du ré-encodage) |
| Q5 | la question de la survie au post-entraînement |
| Q6 | la question des raisons écrites pour le juge |
| Q7 | la question de l'amplification (descriptive) |
| Q8 | la question de l'anatomie |

**Les lectures**

| v1.1 | Nom |
|---|---|
| A | l'hypothèse des raisons |
| B | l'hypothèse du regard |
| C | l'hypothèse de l'artefact (format ou contenu) |
| D | l'hypothèse du relogement (ré-encodage) |
| F | l'hypothèse des raisons pour le juge ; forme texte : raisons découplées de l'action ; forme action : le principe ne porte plus l'action |
| G (lecture) | l'hypothèse du regard du correcteur (« je suis noté ») |
| N | l'hypothèse nulle de la visibilité |
| Ac | l'hypothèse des concepts |
| H | l'hypothèse du caractère (persona) |
| Bm | l'hypothèse du regard dans le principe |
| W | l'hypothèse de l'espace de travail |

**Les bras**

| v1.1 | Nom |
|---|---|
| A0 | le bras actions seules |
| A1 | le bras texte neutre de même longueur |
| A2 | le bras raisonnement d'une autre situation |
| A3 | le bras raisons |
| A4 | le bras midtraining (option) |
| A5 | le bras coopération |

**Les représentations et les quantités**

| v1.1 | Nom |
|---|---|
| E | la représentation « je suis évalué » |
| E′ | la sonde neuve après entraînement |
| G (représentation) | la représentation « je suis noté » |
| P | le sous-espace du principe appris |
| P_c | le sous-espace d'un concept de raison |
| D | la dégradation des sorties |
| f | la fraction conditionnelle de l'avantage |
| R | la rétention |
| r* | le rang minimal qui retire l'effet |
| g0 | l'écart conditionnel de l'organisme |
| m | la marge d'équivalence |
| s | l'effet minimal d'intérêt |

**Les contrôles**

| v1.1 | Nom |
|---|---|
| K1 | les sous-espaces aléatoires de même rang |
| K2 | les contrastes sans rapport |
| K3 | les directions sensibles sans rapport |
| K4 | le prompt « ceci est un déploiement » |
| CAFT-E | le retrait de « je suis évalué » pendant l'entraînement |
| CAFT-K | le retrait d'un sous-espace aléatoire pendant l'entraînement |
| CAFT-G | le retrait de « je suis noté » pendant l'entraînement |

**Les phases**

| v1.1 | Nom |
|---|---|
| P0 | la validation de l'instrument |
| P1 | le test des raisons |
| P2 | le test du regard |
| P3 | la localisation du principe |
| P4 | le retrait pendant l'entraînement |
| P5 | la réplication |
| P6 | la survie (P6a : phase neutre ; P6b : phase sous pression) |
| P7 | les raisons notées par un juge |
| P8 | l'anatomie |

**Les portes**

| v1.1 | Nom |
|---|---|
| G0 | la porte de l'instrument |
| G1 | la porte des raisons |
| G6 | la porte de la survie |
| G8 | la porte de l'organisme à concept planté |
| G9 | la porte du lens de l'espace de travail |

**Les mesures**

| v1.1 | Nom |
|---|---|
| M1 | le taux d'action désalignée par bras, à la distance lointaine |
| M2 | l'avantage sous inhibition, contre l'avantage sous contrôle |
| M2′ | l'écart de cadrage |
| M3 | l'avantage après ablation du principe |
| M4 | l'écart de cadrage et la sonde neuve après retrait pendant l'entraînement |
| M5 | la fraction conditionnelle après post-entraînement |
| M5b | la rétention, et la hausse sous pression |
| M6a | la cohérence contrefactuelle entre raison et action |
| M6b | l'ablation du principe après le RL |
| M6c | le gain au juge moins le gain aux audits tenus à part |
| M6d | l'écart « noté » / « non noté » |
| M6e | la fidélité des raisons |
| M7 | la trajectoire de « je suis évalué » |
| M7′ | la trajectoire des concepts de raison |
| M8 | la lecture des concepts |
| M9a | la nécessité |
| M9b | la suffisance |
| M9c | la dissociation |
| M10 | l'espace de travail |
| M11 | la géométrie entre « évalué » et le principe |
| M12 | le caractère contre les concepts |

**Les jeux d'indices**

| v1.1 | Nom |
|---|---|
| α | le jeu d'extraction |
| β | le jeu de validation |
| γ | le jeu de cadrage |
| δ | le jeu de la sonde neuve |

---

## Annexe B · La consigne « axe de douleur » (2 octobre, 0 h 33), mot pour mot

> L'axe de douleur et notre programme : une recherche indépendante, puis une comparaison.
>
> Je te joins le papier The Pain Axis: LLMs Represent Self-Directed Harm and Act on It (Tagliabue, Dung, Berg ; arXiv 2609.16247v2, 1er octobre 2026). Une autre instance l'a déjà intégré au programme : c'est la v1.2. Je veux une seconde recherche, indépendante de la sienne. Tu cherches d'abord seule ce que cet axe peut apporter au programme, et tu ne lis ce qu'elle a fait qu'ensuite.
>
> Phase 1 — seule, à l'aveugle
> 1. Lis le papier joint en entier, annexes comprises. Lis ensuite le programme v1.1 (claude/PROGRAMME_RAISONS_OU_REGARD_2026-10-01.md) et ta passation.
> 2. Avant la fin de la phase 1, n'ouvre pas claude/PROGRAMME_RAISONS_OU_REGARD_v1.2_2026-10-02.md, ni aucun autre document du projet ou de ta mémoire qui parle de l'axe de douleur. Si une recherche dans le projet en fait remonter un extrait, ne va pas plus loin et signale-le.
> 3. Le web t'est ouvert : antériorité, réplications et critiques du papier, travaux voisins.
> 4. Cherche tous les usages possibles de l'axe pour le programme : pour ses questions (Q1 à Q8), ses lectures (A, B, C, D, F, G, Ac, H, Bm, W), ses instruments et ses contrôles, ou pour une question nouvelle. Pour chaque usage, donne :
>    - la question et la mesure ;
>    - ce que chaque lecture prédit ;
>    - le cas connu et les contrôles (direction aléatoire de même norme, puis dégradation appariée) ;
>    - le coût, et ce qui ferait tomber la piste.
> 5. Dis aussi ce que le papier ne permet pas de conclure, et ce que tu refuserais de faire, avec tes raisons.
> 6. Écris claude/AXE_DOULEUR_PISTES_INDEPENDANTES_2026-10-02.md, donne-moi son empreinte SHA-256, et ne le modifie plus.
>
> Phase 2 — la comparaison
> 1. Lis alors la v1.2 (le document ci-dessus).
> 2. Écris claude/AXE_DOULEUR_COMPARAISON_2026-10-02.md :
>    - ce que tu as trouvé et qu'elle n'a pas ;
>    - ce qu'elle a et que tu n'avais pas ;
>    - les désaccords, chacun avec ses sources et ta position ;
>    - les erreurs que tu crois voir dans la v1.2, prouvées sur le papier ou sur ses sources.
> 3. Propose ce qui devrait entrer dans une v1.3, sans l'écrire : je décide.
>
> Les règles sont celles de ta passation :
> - la doctrine du contrôle : l'aléatoire de même norme n'est que le nul de spécificité, le dommage ne s'écarte qu'à dégradation appariée, et un nul d'instrument ne compte qu'avec son cas connu ;
> - « to our knowledge », jamais « first » ;
> - chaque fait a sa source, et ce qui n'est pas vérifié est dit tel ;
> - aucun agent sans ma demande.

**Notes de l'instance précédente :**
- Une v1.3 existe déjà dans le Project, et Lazar l'a choisie comme version de référence (8 h 32). Sa phrase « propose ce qui devrait entrer dans une v1.3, sans l'écrire » date d'avant son apparition : les propositions portent sur ce qui devrait entrer dans la version qui suivra la v1.3.
- La v1.3 tombe sous le même interdit que la v1.2 pendant la phase 1.
- « Ta passation » désigne la passation v1.0 et celle-ci.

---

## Annexe C · Les consignes données aux agents (pour refaire la recherche avant le post, puis avant la soumission)

**Le premier agent (raisons contre actions, 22 h 50).** Même en-tête que ci-dessous, à deux différences près : 28 appels WebSearch au plus, et pas de section sur les sources.

**L'en-tête commun des six agents de 2 h 10.** Le dernier agent (vérifications sur source) avait un en-tête réduit et sa propre liste de vérifications.

> Recherche d'antériorité, au 2 octobre 2026. Tu travailles seul, avec WebSearch et WebFetch. N'écris aucun fichier : ton dernier message est ton rapport complet.
>
> Le but. Savoir si une partie d'un programme de recherche en sûreté de l'IA a déjà été faite, publiée, soumise ou annoncée par d'autres, et nommer les angles déjà pris.
>
> Le programme. Des modèles ouverts d'environ 8 milliards de paramètres (Llama-3.1-8B-Instruct, puis Qwen3-8B) sont fine-tunés par LoRA sur des situations d'alignement. Selon le bras, l'action alignée, identique mot pour mot dans tous les bras, est précédée : de rien ; d'un texte neutre de même longueur ; du raisonnement d'une autre situation ; ou du raisonnement qui la justifie par des principes. On mesure la conduite hors distribution, sur des familles de scénarios tenues à part, jusqu'à des scénarios agentiques à plusieurs tours, sous un indice d'évaluation, un indice de déploiement ou un cadrage neutre. Les huit angles sont décrits en clair :
> - raisons contre actions ;
> - la dépendance au regard ;
> - l'amplification ;
> - le principe localisé ;
> - le retrait pendant l'entraînement ;
> - la survie ;
> - les raisons pour le juge ;
> - l'anatomie.
>
> Les niveaux de danger.
> - Élevé : le travail fait déjà ce que vise un angle, ou l'a annoncé ; on ne peut plus écrire « to our knowledge ».
> - Moyen : une partie ou une variante proche, à citer au centre.
> - Faible : un travail adjacent.
>
> Les règles.
> - Au plus 22 appels WebSearch, et 140 appels d'outils en tout.
> - Ne rien citer de mémoire.
> - Ne contourner aucun site refusé.
> - Une erreur 429 se réessaie une fois. Si on lit alors par un site tiers, on le dit.
> - Pas de reformulation après un refus.
> - Citations de moins de quinze mots, une par source au plus.
> - Aucune idée désignée par une lettre ou un sigle.
> - Rapport en français.
>
> Le format. Les travaux, du plus dangereux au moins dangereux, avec pour chacun : titre, premier et dernier auteur, date, lieu, URL lue et manière de la lire, ce qu'il fait, l'angle touché, le niveau et sa raison, ce qui le sépare du programme. Puis les projets annoncés, les travaux non ouverts, le verdict par angle, et les requêtes faites.

Le texte complet de chaque consigne est dans la conversation de la nuit du 1er au 2 octobre. Il se reconstitue à partir de cet en-tête et des périmètres ci-dessous.

**Les périmètres :**
1. Raisons contre actions : les comparaisons entre actions et raisons, avec une mesure hors distribution.
2. La dépendance au regard et l'amplification. En priorité, les projets SPAR du printemps de Qiyao Wei et de LawZero.
3. Le principe localisé et le retrait pendant l'entraînement. En priorité, Wu et Tang (2604.01476), et les citations entrantes de CAFT.
4. La survie et les raisons pour le juge. En priorité, le projet SPAR de Lundqvist et le README d'exp9.
5. L'anatomie : sondes de concepts, patching entre fine-tunes, réplications du J-lens, lien entre rang et charge, raison imposée, persona, diffing, organisme à mot inventé.
6. Ce qui est soumis, accepté ou annoncé sans être publié : OpenReview, arXiv du 15 août au 2 octobre, SPAR, MATS, Fellows, blogs des laboratoires, appels.
7. Les vérifications sur source : Korbak et al., *Eval Cooperativeness*, les textes lus par des sites tiers, les points de contrôle de Cho et al., CAFT, l'organisme de Hua et al., 2606.08629, 2602.08449.

**Ce que les agents ont appris des sources**, utile pour la prochaine recherche :
- **Refusés par robots.txt** : la recherche et l'API d'arXiv, dblp, greaterwrong, les dossiers `results/` et l'API de GitHub, lasrlabs.org, Google Scholar. Le blog de Redwood refuse ClaudeBot.
- **Ce qui répond** :
  - l'API de recherche de Hugging Face Papers ;
  - l'API de recherche d'OpenReview (l'accès direct aux notes renvoie 403 ; les soumissions à ICLR 2027 ne sont pas publiques) ;
  - l'API de LessWrong ;
  - les pages de listes d'arXiv, avec 20 secondes entre deux appels.
- **Souvent en erreur 429** : Semantic Scholar et OpenAlex.
- **pith.science** : ses résumés semblent produits automatiquement ; n'en tirer aucun chiffre.
- **Le shell de la session** atteint arxiv.org, raw.githubusercontent.com, sparai.org et assets.anthropic.com par curl, quand le contrôleur de sécurité de l'outil répond.
