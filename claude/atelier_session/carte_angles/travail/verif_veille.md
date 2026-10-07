# Vérification de `veille.md` (« veille du 2 octobre »)

État au 2 octobre 2026. Pièce de travail pour la carte des angles (passation v1.2, §6, point 3).

**Ce que j'ai relu moi-même.**
- Le fichier vérifié, en entier.
- La passation v1.2 en entier, et le complément de l'architecte (partie ouverte).
- Dans `ANTERIORITE_RAPPORTS_2026-10-02.md` : le rapport 2 en entier (lignes 271 à 485) ; le rapport 3 (lignes 486 à 530, 576 à 606, 640 à 726) ; le rapport 4 en entier (727 à 1011) ; le rapport 5 (1012 à 1060, 1120 à 1254) ; le rapport 6 (1255 à 1545) ; dans le rapport 7, les passages repérés par recherche.
- Dans `ANTERIORITE_RAPPORTS_2026-10-01.md` : lignes 60 à 72, 114 à 135, 465 à 488.
- Les définitions des niveaux de danger (consignes de la nuit, lignes 46 à 50).
- Toutes les présences et absences revendiquées par la veille, par recherche textuelle dans les deux fichiers de rapports et dans la passation.

**Le web.** Neuf appels WebSearch, rien d'autre. Tout ce qui en vient ci-dessous est « vu par extrait de recherche, non ouvert » et ne fournit aucun chiffre. Une lecture par curl du SUMMARY.md d'exp9 a été refusée par le contrôle des permissions de la session : je ne l'ai pas contournée (voir le manque n° 2).

**Ce qui tient, vérifié.**
- Les absences revendiquées sont exactes. Aucun des travaux des §2 et §4 de la veille ne figure dans les onze rapports ni dans la passation, ni par son titre, ni par son identifiant, ni par son adresse. La seule occurrence d'« Astra » dans les rapports désigne le programme de fellows (rapport 6, ligne 1516), pas le modèle d'OpenAI.
- Les présences du §3 sont exactes : les 27 identifiants y figurent tous. Le titre *Active Adaptation, Not Static Defense* n'est pas dans les rapports, mais son identifiant y est (2609.10142, Guan … Feng, rapport 3, ligne 636).
- Exacts aussi :
  - *Infohazard Evaluations* (Shi Feng et al.), au rapport 2 ;
  - Betley … Dumas, au rapport 2 ;
  - Jinghua Ou, coautrice de 2606.08243, au rapport 7 ;
  - les billets de Second Look Research du 15 août (rapport 6) et du 21 septembre (rapport 2) ;
  - *Where we are on evaluation awareness*, vu et non ouvert, au rapport 2 ;
  - *Toward Dealing with Unverbalized Eval Awareness*, aux rapports 2, 3 et 6 ;
  - la citation du rapport 5 sur les réplications du J-lens (ligne 1162) ;
  - l'offre d'emploi de CaML, niveau faible, au rapport 6 ; le projet SPAR de CaML, au rapport 4.
- Aucune erreur déjà corrigée au §4.3 n'est reprise, à une ambiguïté près (correction n° 10).
- Aucun chiffre tiré d'un extrait n'est repris. Aucun sigle ne désigne une idée. « first » n'est jamais employé.

---

## 1 · Corrections bloquantes

### 1. Le titre du §1 dit plus que ce que la veille a vu (veille, ligne 15)
- **Écrit** : « Rien de nouveau au niveau élevé ou moyen » ; « Le verdict de la passation (§4.4) tient ».
- **Pourquoi c'est faux en l'état** :
  - Tout repose sur des extraits. La veille déclare elle-même à ouvrir « en priorité » la system card de GPT-6 Astra, dont le niveau dépend de ce qu'elle contient (veille, ligne 18).
  - Deux niveaux « faible » de la veille contredisent l'échelle appliquée par les rapports (corrections n° 2 et n° 4).
  - Les soumissions à ICLR 2027 ne sont pas couvertes (veille, §5).
  - La passation borne elle-même son verdict : « pour ce que les onze rapports ont pu voir » (§4.4).
- **Écrire** : « Dans ce que les extraits montrent, rien ne contredit le verdict provisoire de la passation (§4.4). Un travail reste à classer après lecture (la card de GPT-6 Astra). Un autre est à relever au niveau moyen (2601.23086). »
- **Et reprendre la combinaison centrale telle que le §4.4 la définit.** La paraphrase de la veille omet deux éléments :
  - « à format et contenu contrôlés » ;
  - « pour mesurer la part de l'avantage hors distribution qui en dépend ».

  Sans eux, la combinaison décrite est plus large que celle que la passation déclare libre.

### 2. GPT-6 Astra : la règle qui fixe le niveau ne suit pas celle des rapports (veille, lignes 65 à 68)
- **Écrit** : « faible », et « à relever à moyen » seulement si la card contient une inhibition ou un pilotage de la conscience d'évaluation.
- **Ce que font les rapports, avec les mêmes définitions** (consignes, lignes 46 à 50). Le rapport 2 classe au niveau moyen, pour la dépendance au regard, des travaux sans aucune inhibition :
  - 2606.24014 (OpenAI) : « Danger : moyen. C'est une variante comportementale de la dépendance au regard » (rapport 2, texte intégral du §5) ;
  - le billet de Pan et Greenblatt : « moyen, pour le cadrage de la quantité visée ; sans expérience propre » (rapport 2, lu par l'API de LessWrong).

  *Metagaming matters*, dont le constat est le plus proche de celui d'Apollo sur Astra, y est classé faible, mais pour l'amplification ; le rapport du 1er octobre sur la conscience d'évaluation comme condition des gains (lignes 130 à 134) lui donne un recouvrement partiel.
- **Ce que disent les extraits.** La card discute les limites que la conscience d'évaluation impose à ce que les évaluations disent de la généralisation de l'alignement. La mise à jour du 9 septembre précise comment l'évaluation honeypot se rapporte à l'entraînement (vu par extrait de recherche, non ouvert). C'est le cadrage que le rapport 2 classe au niveau moyen.
- **Écrire** : « non classé, entre faible et moyen, à ouvrir avant la carte ». La card ne peut pas servir d'appui à « rien au niveau moyen ».
- **Les deux extraits se contredisent sur la verbalisation.** L'un la dit plus fréquente que chez le prédécesseur. L'autre écrit qu'Astra « verbalizes less than its predecessors » (vu par extrait de recherche, non ouvert). La phrase de la ligne 62 est à retirer jusqu'à lecture.
- **Une négation ne s'établit pas sur un extrait.** « Dans aucun cas l'avantage des raisons n'est touché, d'après les extraits » (ligne 68) devient : « les extraits ne montrent pas de contraste entre raisons et actions ».

### 3. Sonnet 4.5 : faux statut de lecture, et un chiffre qui n'existe pas (veille, ligne 67)
- **Écrit** : « La card de Sonnet 4.5, §7.6, le fait (relu sur la source par l'instance du papier, passation §4.2, n° 5) ». « Le fait » renvoie à une inhibition « qui chiffre la part des progrès qui en dépend ».
- **Ce que couvre la relecture** (passation §4.2, n° 5). Seulement ceci : sur certaines évaluations de désalignement, la conscience d'évaluation « accounts for a portion, but not all » des progrès d'alignement sur les modèles précédents.
- **Ce qui n'est que dans le rapport 2** (texte intégral des §7.6.1 à 7.6.4, figures non lues) :
  - l'inhibition de 10 traits et de 4 vecteurs contrastifs ;
  - le contrôle par traits aléatoires de même norme ;
  - la comparaison de deux instantanés.
- **Aucun chiffre de la part n'est donné.** La conclusion relue est qualitative. « Qui chiffre la part » est faux.
- **Écrire** : « la card de Sonnet 4.5, §7.6, inhibe la conscience d'évaluation sur deux instantanés (rapport 2, texte intégral) et conclut qu'elle explique "a portion, but not all" des progrès (relu sur la source par l'instance du papier, passation §4.2, n° 5) ».

### 4. 2601.23086 : niveau faible, alors que Drori et al. sont au niveau moyen (veille, ligne 119)
- **Écrit** : *Chain-of-thought obfuscation learned from output supervision can generalise to unseen tasks*, les raisons pour le juge, « faible ».
- **Ce que dit l'extrait** (vu par extrait de recherche, non ouvert) :
  - auteurs : Nathaniel Mitrani Hadida, Sassan Bhanji, Cameron Tice, Puria Radmard. Tice et Radmard cosignent *Constitutional Midtraining* (passation §4.3, d'après le rapport 7) ;
  - l'obfuscation apprise se généralise à des tâches non vues. Elle apparaît même quand seule l'action finale, après la chaîne de pensée, est pénalisée.
- **Ce que disent les rapports et la passation** :
  - *Output Supervision Can Obfuscate the Chain of Thought* (Drori … Turner, 2511.11584) est classé moyen, parce que le bras « juge qui ne voit que l'action » n'est pas neutre pour les raisons (rapport 4, résumé seul).
  - La passation demande de citer Drori et al. et de mesurer l'obfuscation dans les deux bras du juge (§5.5, n° 5).
  - Le juge recommandé ne voit que les actions (§5.1).
  - D'après le complément de l'architecte, la v1.3 n'a ni l'un ni l'autre.
- **Écrire** : « moyen provisoire, à citer au centre avec Drori et al. ; même objection, étendue à des tâches non vues ». Le rapport 4 a parcouru les citations entrantes de 2511.11584 sans le relever : c'est un manque de la nuit à signaler dans la carte.

### 5. CaML : un résultat publié est déjà dans la veille, sans être rattaché (veille, §2.4, lignes 83 à 91, et §4, ligne 115)
- **Écrit** :
  - le billet *Can mid-training survive RL* serait « probablement le projet CaML » ; il faudrait vérifier s'il contient des résultats, sans quoi CaML reste « seulement annoncé » ;
  - au §4, *Helpfulness Hurts* (2606.26102) figure sans lien avec CaML.
- **Ce que disent les extraits** (vus par extrait de recherche, non ouverts) :
  - *Helpfulness Hurts: Domain-Dependent Degradation of Mid-Trained Compassion Values Under Post-Training* est de Juliana Seawell et Jasmine Brazilek, de CaML. Il part de Llama 3.1 8B, le modèle du programme, après un midtraining de compassion. Il compare un post-entraînement d'aide et un post-entraînement de code, et mesure la dégradation de la valeur.
  - Le billet LessWrong est une annonce de recrutement : la question de la survie au RL, la base OLMo 3, des livrables prévus, dont « at least one paper ». C'est, sur le fond, l'offre d'emploi du 1er septembre que décrit le rapport 6.
- **Conséquences pour la carte** :
  - le billet LessWrong n'est pas un objet nouveau : il passe au §3 de la veille (rien de nouveau sur le fond) ;
  - CaML n'est plus « annoncé » seulement (passation §4.4, n° 6). Un résultat sur la survie d'une valeur installée par midtraining est public depuis juin 2026, sur le modèle du programme (vu par extrait). Le projet sur OLMo 3 reste annoncé ;
  - niveau de 2606.26102 : faible à moyen pour la survie. Il est analogue à *Alignment midtraining for animals*, classé faible au rapport 4. Mais il porte sur le même modèle de base, et il montre que le domaine du post-entraînement change la survie. Le choix du « post-entraînement neutre » du programme devra s'en distinguer.

---

## 2 · Corrections non bloquantes

### 6. *Pre-training interventions, ex post facto* (veille, §2.1)
- **La date.** Le résumé du moteur dit « submitted … October 2, 2026 » (vu par extrait de recherche, non ouvert). La veille écrit « 1er ou 2 octobre, déduit de l'identifiant ». Écrire : « octobre 2026 par l'identifiant ; le 2 octobre d'après un résumé de moteur, non vu sur la source ».
- **Les personnes déjà connues sont incomplètes** :
  - Betley … Dumas est aussi au rapport 6, en texte intégral par l'API de LessWrong, en plus du rapport 2 ;
  - Shi Feng est aussi dernier auteur de 2606.08243 (rapport 7) et de 2606.08629 (Baek … Feng, passation §4.3).
- **Ligne 40.** La remarque sur la greffe comme analogue d'un report du bras raisons « d'un point de contrôle à l'autre » n'a pas de source. La marquer comme hypothèse de l'auteur de la veille, ou la retirer.

### 7. GPT-6 Astra : des dates et des objets manquent (veille, §2.2)
Tous vus par extrait de recherche, non ouverts.
- **Première publication.** Le PDF est intitulé « OpenAI GPT-6 Astra System Card 2026-09-03 ». La veille dit « non vue ».
- **Une seconde mise à jour, le 22 septembre 2026.** Des évaluations d'alignement sont mises à jour, et l'annexe donne les résultats sur les nouvelles versions. La veille ne la mentionne pas.
- **Un addendum non relevé** : *Addendum to GPT-6 Astra System Card: GPT-6.1 Sol* (`deploymentsafety.openai.com/gpt-6-1-sol`). Un article de The Register daté du 29 septembre 2026 est titré sur la mise à l'écart de « GPT-6.1 Astra » (titre et adresse seuls).
- **La date du billet de Zvi** se lit dans une adresse vue par extrait (`thezvi.wordpress.com/2026/09/09/…`). La conversion locale de l'identifiant du billet X (ligne 174) devient inutile. Et l'adresse du billet X n'est pas donnée dans la veille : sans elle, la date est sans source vérifiable.
- **La page sur la simulation de déploiement du trafic Codex interne** est listée sans analyse. Elle relève de la mesure hors évaluation. À rapprocher de *Sidestepping Evaluation Awareness… Production Evaluations* (OpenAI, décembre 2025), relevé comme non ouvert dans le rapport du 1er octobre sur la combinaison exacte et la littérature grise (ligne 480).

### 8. 2606.20225, l'angle est mal attribué (veille, ligne 116)
- **Écrit** : le principe localisé ; le retrait pendant l'entraînement.
- **Extrait** (vu par extrait de recherche, non ouvert) : la mitigation se fait par pilotage, en soustrayant une direction. Rien n'indique un retrait pendant l'entraînement. L'auteur est Abdul Rafay Syed. Les directions transférées d'un modèle à l'autre échouent aux contrôles de spécificité.
- **Écrire** : « le principe localisé, et la doctrine du contrôle ; faible ». Si le texte montrait un retrait pendant le fine-tuning, le niveau serait celui de Nadaf et de BLOCK-EM : moyen (rapport 3, texte intégral).

### 9. 2608.04347 a changé de titre (veille, ligne 113)
- La page abs porte *Looking in the Mirror: Introspecting Side-Effect Misalignments Induced by Fine-Tuning*. Le titre de la veille est celui de la page HTML (vus par extrait de recherche, non ouverts).
- Donner les deux. Le niveau faible tient sur l'extrait : un adaptateur d'introspection lit les différences d'activations induites par le fine-tuning.

### 10. Formulations à préciser au §3 et au §4
- ***Eval Cooperativeness*, « page ICML »** (ligne 101). Écrire « page de l'atelier Trustworthy AI for Good d'ICML 2026 ». C'est l'erreur de lieu de la v1.1, corrigée au §4.3 et encore présente dans les versions 1.2 et 1.3 (complément de l'architecte) : ne pas laisser d'ambiguïté.
- ***Aligning What LLMs Do and Say*** (ligne 121) :
  - identifiant manquant : arXiv 2506.07523, juin 2025, publié aux Findings d'ACL 2026 (vu par extrait de recherche, non ouvert) ;
  - l'extrait décrit une cohérence par attribution entre l'explication et la réponse, sur des tâches de questions-réponses, améliorée par DPO. Le niveau faible tient ;
  - préciser que cela ne touche pas la cohérence entre raison et action quand on édite la situation, que le §4.4 (n° 7) déclare libre.
- ***Rerunning AI safety papers…*** (ligne 103). Le rattacher à Second Look Research est une inférence : l'auteur n'est pas visible. Le dire. Le rapport 2 ajoute que Second Look Research réplique aussi le RL bénéfique d'OpenAI : à reporter.
- ***Not All Eval-Awareness Is Equal***, ***Active Adaptation…*** : rien à corriger, sinon que le second titre vient d'un extrait.

### 11. Ce que la veille dit n'avoir pas trouvé, sans l'avoir cherché (veille, §5, ligne 140)
- **Écrit** : « Non trouvé : un résultat public du projet SPAR de Lundqvist ou de celui de Cadile ».
- **Les requêtes du §6** n'en nomment aucun : ni Lundqvist, ni Cadile, ni SPAR, ni exp9. Écrire « non cherché nommément ».
- La réponse de Lazar, relayée avec cette tâche : pas encore de contact avec Cadile et Lundqvist. La veille sur ces deux projets ne passe donc que par les sources publiques, et elle doit être faite.

---

## 3 · Manques

1. **La card de GPT-6 Astra n'est pas ouverte.** Le domaine n'est pas dans la liste des refus. C'est l'objet dont dépend le titre de la veille. À faire par l'instance du papier, pour que le statut devienne « relu ». À lire : la section alignement (versions du 9 et du 22 septembre), l'addendum GPT-6.1 Sol, la page sur la simulation de déploiement.
2. **exp9 n'est pas vérifié.** C'est le seul travail classé élevé pour les raisons pour le juge (passation §4.4, n° 7), et un PPO y est annoncé (dates à surveiller). raw.githubusercontent.com répond par curl d'après la consigne, mais ma lecture du SUMMARY.md a été refusée par le contrôle des permissions de la session. À faire par l'instance du papier, en comparant au §4.2, n° 1.
3. **Les nouvelles system cards et les rapports de risque de septembre ne sont pas cherchés** : chez Anthropic, Google DeepMind et OpenAI, hors Astra. Les précédents de la dépendance au regard sont presque tous des system cards (Sonnet 4.5, Opus 4.7, Fable 5). Aucune des 20 requêtes ne les vise.
4. **Les projets à surveiller ne sont pas cherchés nommément** : Cadile, Lundqvist, Cody Wild, *Infohazard Evaluations* (Shi Feng et al.), Ivanov, Qiyao Wei. Démonstration SPAR le 19 décembre 2026 (passation §4.4, FAQ de SPAR lue par deux agents).
5. **Les relectures que la passation exige avant de citer au centre** (§6, point 3) ne sont ni faites ni signalées comme restantes : Nakamura, Zeisler, Second Look Research, les J-lens de Neuronpedia. La veille n'a vu Second Look Research que par extrait.
6. **L'« intérêt pratique » du dépôt jspace-qwen est surévalué** (ligne 80). Le rapport 5 signale déjà des J-lens ajustés sur Neuronpedia pour llama3.1-8b-it et qwen3-8b, le dépôt camilablank/workspace-lenses et le code public de l'article d'Anthropic. Le dépôt vu porte sur Qwen3.5-9B, qui n'est pas un modèle du programme. Les outils de Neuronpedia restent « à vérifier » (passation §5.5, n° 6).
7. **Pas de rapprochement avec les autres fichiers du dossier de travail** (veille, ligne 9). Celui qui assemble la carte doit dédoublonner avec `angle_*.md` et `projets_calendrier.md`. Je ne les ai pas lus : ma consigne ne le demandait pas.
8. **Les manques de la nuit ne sont pas nommés comme tels.** Les travaux du §4 de la veille datent tous d'avant la fenêtre. Ils ont échappé aux onze rapports. La carte doit le dire, car cela borne la confiance dans le « to our knowledge ». Le plus net est 2601.23086 (correction n° 4).

---

## 4 · Ce que la carte peut reprendre de la veille, une fois corrigée

- **2610.00767** (greffe d'adaptateurs entre points de contrôle) : la survie au post-entraînement, niveau faible, vu par extrait ; à lire avant le post.
- **GPT-6 Astra** : la dépendance au regard, pour la conduite en général, non classé, entre faible et moyen ; à ouvrir.
- **2601.23086** : les raisons pour le juge, niveau moyen provisoire, à citer au centre avec Drori et al.
- **CaML** : un résultat publié en juin 2026 (2606.26102, sur Llama 3.1 8B), vu par extrait ; le projet sur OLMo 3 reste annoncé.
- **Les deux dépôts du J-lens, Diff Mining, les crosscoders, 2607.22925, 2605.27676, 2606.20225, 2608.04347, 2506.07523** : niveau faible, tous vus par extrait.
- **Rien de nouveau, dans ce que les extraits montrent**, pour Second Look Research, Lundqvist, Cadile et la suite d'Anthropic sur la réflexion contrefactuelle. Pour les deux premiers, la recherche reste à faire (correction n° 11).
