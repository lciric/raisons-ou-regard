# Référentiel des instruments — cours d'alignement v3.6 (2 octobre 2026)

*Pour les quatorze rédacteurs de la v3.6, un par tranche. Écrit le 2 octobre 2026 à partir des seules pièces du dossier : les deux sources v3.5, l'explication source du 2 octobre, les fiches de lecture prioritaires (partie B et fiches 1 à 19) et leur contre-lecture, le programme « Raisons ou regard ? » (parties 3, 7 et 8), la passation v1.2 (§5.1 et §5.2), les rapports d'antériorité du 1er et du 2 octobre (cités comme rapports) et le README du dépôt.*

## Mode d'emploi

- **Ce que contient chaque fiche d'instrument** : son nom (FR et EN), sa maison (tranche, section, ligne d'ancrage exacte dans chaque langue, recopiée telle quelle de la v3.5), le texte complet de son encadré en français et en anglais au format fixe, son renvoi d'une ligne dans les deux langues, et les endroits où il revient.
- **L'encadré complet** s'insère juste après la ligne d'ancrage de sa maison (outil `appliquer.py`, format `travail/insertions_<tranche>.json`). Chaque ancre a été vérifiée : présente une seule fois dans sa tranche (après suppression des espaces de début et de fin), dans les deux langues. Les textes des encadrés sont donnés dans des blocs `~~~` : les recopier sans les clôtures.
- **Le renvoi d'une ligne** se pose dans les sections où l'instrument revient. La partie « Par tranche », en fin de document, donne pour chaque tranche les sections où un renvoi est conseillé, avec le texte du renvoi prêt dans les deux langues ; le rédacteur choisit lui-même la ligne d'ancrage dans la section (une ligne unique dans sa tranche, en fin de passage, jamais au milieu d'une phrase coupée).
- **Les avertissements ponctuels** prêts (neuf) sont donnés avec leur ancre vérifiée. Le rédacteur peut en ajouter d'autres, au format fixe, quand un passage de sa tranche rapporte un résultat obtenu avec un instrument sans dire sa limite ; il prend alors la limite et la parade, avec leurs sources, dans l'encadré de l'instrument.
- **La doctrine, partout** : une direction aléatoire de même norme n'est que le nul de spécificité ; le dommage ne s'écarte qu'à dégradation appariée ; un nul d'instrument ne compte qu'avec son cas connu ; « to our knowledge », jamais « first ». Aucun ajout ne touche une ligne « À dire » ni une forme nommée, ni ne leur ajoute de chiffre.
- **Les sources** : « cours, volet … » renvoie à la v3.5 ; « fiche n » aux fiches de lecture prioritaires du 1er octobre ; « fiches, partie B » à leur méthode de lecture (les sept pièges) ; « fiches, partie C » à leur fil rouge ; « contre-lecture des fiches » à la contre-lecture du 1er octobre ; « programme, partie n » au programme « Raisons ou regard ? » ; « passation » à la passation v1.2 ; « explication du 2 octobre » au texte source de l'encadré sur les sondes de désalignement ; « rapport d'antériorité n du 2 octobre » aux rapports bruts, toujours dits « rapport » ; « README du dépôt » au dépôt sycophancy-construct-validity. En anglais : course, Part …; reading sheet n; reading sheets, part B / part C; counter-reading of the sheets; programme, part n; handover; explanation of 2 October; prior-art report n of 2 October — report; repository README.

## Table des instruments

| # | Instrument | Maison (tranche, section) | Limites | Parades |
|---|---|---|---|---|
| 1 | Contrôles aléatoires (direction aléatoire de même norme, sous-espaces aléatoires de même rang) / *Random controls (matched-norm random direction, random subspaces of the same rank)* | `volet_M` — volet M, M4 · le contrôle (paragraphe « La direction aléatoire de même norme ») | 4 | 4 |
| 2 | Dégradation appariée et dose-réponse / *Matched degradation and dose-response* | `volet_M` — volet M, M4 · le contrôle (paragraphes « La dégradation appariée » et « La dose-réponse ») | 6 | 6 |
| 3 | Jeu tenu à part / *Held-out set* | `volet_M` — volet M, M4 · le contrôle (paragraphe « Le jeu tenu à part ») | 5 | 4 |
| 4 | Cas connu / *Known case* | `volet_M` — volet M, M5 · le nul et le cas connu (fin de section) | 6 | 6 |
| 5 | Organismes modèles / *Model organisms* | `volet2_A_a_D` — volet 2, §A · testbeds et organismes modèles (après « En pratique — Auditing Hidden Objectives ») | 7 | 4 |
| 6 | Évaluations comportementales et pots de miel / *Behavioural evaluations and honeypots* | `volet2_A_a_D` — volet 2, §B · évaluations (après « En pratique — le sandbagging ») | 7 | 6 |
| 7 | Sondes d'activation / *Activation probes* | `volet2_A_a_D` — volet 2, §C · méthodes sur activations (après « En pratique — The Geometry of Truth ») | 10 | 9 |
| 8 | Pilotage par vecteurs (dont vecteurs de persona) / *Steering vectors (including persona vectors)* | `volet2_A_a_D` — volet 2, §C · méthodes sur activations (après « En pratique — Contrastive Activation Addition ») | 8 | 6 |
| 9 | J-lens et espace de travail / *The J-lens and the workspace* | `volet2_A_a_D` — volet 2, C bis · l'espace de travail et le J-lens (après « Le test, tel qu'il se dit ») | 7 | 7 |
| 10 | Ablation et projection (directions, sous-espaces) / *Ablation and projection (directions, subspaces)* | `volet2_A_a_D` — volet 2, §D · interprétabilité mécaniste (paragraphe « La méthode ») | 6 | 6 |
| 11 | Crosscoders et comparaison de modèles / *Crosscoders and model diffing* | `volet2_A_a_D` — volet 2, §D · cas d'application K64 (fin du cas) | 4 | 4 |
| 12 | Débat et supervision évolutive / *Debate and scalable oversight* | `volet2_E_a_I` — volet 2, §E · supervision évolutive (après « En pratique — Debate ») | 4 | 2 |
| 13 | Élicitation non supervisée par cohérence / *Unsupervised elicitation by consistency* | `volet2_E_a_I` — volet 2, §E · cas d'application K52 (fin du cas) | 4 | 3 |
| 14 | Généralisation faible-vers-fort / *Weak-to-strong generalization* | `volet2_E_a_I` — volet 2, §F · la généralisation comme levier (après « En pratique — l'automatisation ») | 5 | 3 |
| 15 | Moniteurs du contrôle (moniteur de confiance, sondes en production, agrégation) / *Control monitors (trusted monitor, probes in production, aggregation)* | `volet2_E_a_I` — volet 2, §G · monitoring et AI control (après « En pratique — les coup probes ») | 8 | 7 |
| 16 | Red-teaming / *Red-teaming* | `volet2_E_a_I` — volet 2, §H · robustesse adverse et red-teaming (après « En pratique — StrongREJECT ») | 6 | 5 |
| 17 | Classifieurs de sûreté (filtres) / *Safety classifiers (filters)* | `volet2_E_a_I` — volet 2, §H · cas d'application G1 (fin du cas) | 5 | 4 |
| 18 | Désapprentissage et ré-élicitation / *Unlearning and re-elicitation* | `volet2_E_a_I` — volet 2, §I · interventions d'entraînement et unlearning (après « En pratique — l'unlearning mis à l'épreuve ») | 6 | 3 |
| 19 | Dictionnaires et SAE / *Dictionaries and SAEs* | `volets4_5_entete` — volet 4 · Towards puis Scaling Monosemanticity (paragraphe « Le contexte ») | 6 | 5 |
| 20 | Graphes d'attribution / *Attribution graphs* | `volets4_5_entete` — volet 4 · Circuit Tracing / On the Biology of a Large Language Model (paragraphe « Le contexte ») | 4 | 4 |
| 21 | Autoencodeurs en langage naturel (NLA) / *Natural-language autoencoders (NLAs)* | `volets4_5_entete` — volet 4 · La vague récente sur la cognition du modèle (fin du passage, « Extension ») | 6 | 5 |
| 22 | Auto-rapport et introspection / *Self-report and introspection* | `volets4_5_entete` — volet 5, partie II, A · sujet 13, Introspection (fin du sujet) | 6 | 4 |
| 23 | Juges LLM / *LLM judges* | `volet6` — volet 6, §2 · tes résultats (paragraphe « La loi de déplacement ») | 8 | 7 |
| 24 | Détecteurs fine-tunés (détecteurs de mensonge) / *Fine-tuned detectors (lie detectors)* | `volet7_B_et_D` — volet 7, F·29 · Fine-Tuned Lie Detectors Failed to Generalize (fin de la fiche) | 6 | 4 |
| 25 | Patching (patch d'activations, patch de chemins, Patchscopes) / *Patching (activation patching, path patching, Patchscopes)* | `volet10` — volet 10 · fiche Patchscopes (fin de la fiche) | 6 | 3 |
| 26 | Oracles d'activation (décodeurs d'activations) / *Activation oracles (activation decoders)* | `volet10` — volet 10 · fiche LatentQA (fin de la fiche) | 5 | 3 |
| 27 | Chaîne de pensée comme moniteur (et conscience verbalisée) / *Chain of thought as a monitor (and verbalized awareness)* | `volet11_21_a_52` — volet 11, réponse 43 · « Is a chain of thought evidence… » (fin de la réponse) | 7 | 6 |
| | **Total : 27 instruments** | | **162** | **130** |

« Parades » compte les limites qui ont une parade, même partielle ; les autres portent « aucune connue ; on le dit ».

## Les contrôles et dispositifs : ce qui a un encadré, ce qui est fondu ailleurs

- **La direction aléatoire de même norme, la dégradation appariée, le cas connu, le jeu tenu à part** ont chacun des limites propres (une dégradation appariée ne vaut que sur le composite choisi ; un cas connu est nécessaire, pas suffisant ; etc.) : ils ont donc leur encadré, au volet M (M4 et M5).
- **La dose-réponse** est fondue dans l'encadré « Dégradation appariée et dose-réponse ».
- **Les paires contrastives** (volet M, M4) sont fondues dans l'encadré « Sondes d'activation » : leur limite (une paire qui porte un style) et sa parade (un classifieur de la seule surface au hasard) y sont.
- **Le jumeau propre et le jeu canari** (volet M, M4 et M5) sont fondus dans l'encadré « Classifieurs de sûreté » ; **la référence jamais entraînée** dans « Désapprentissage et ré-élicitation » ; **la notation à l'aveugle** dans « Juges LLM » ; **le bras de référence réaliste** dans « Évaluations comportementales » et « Red-teaming ».
- **Le témoin sans pression et la direction d'un concept rival** n'ont pas de limite propre dans les pièces au-delà de ce que M4 dit déjà ; ils apparaissent comme parades dans « Dégradation appariée » et « Ablation et projection ».
- **Les vecteurs de persona** sont dans « Pilotage par vecteurs » ; **l'agrégation de scores de sondes et les moniteurs à état** dans « Moniteurs du contrôle » ; **le logit lens et le tuned lens** dans « J-lens » (comme proxy déclaré) et « Désapprentissage » (une lecture qui ne voit rien).
- **L'encadré sur les sondes de désalignement** (texte source du 2 octobre, à reprendre en entier) n'est pas un encadré d'instrument : il traite le cas connu, l'entraînement et le hors-distribution des sondes. Les encadrés « Sondes d'activation », « J-lens », « Organismes modèles », « Cas connu » et « Détecteurs fine-tunés » en reprennent les limites avec leurs sources propres ; là où il sera placé, un renvoi vers ces cinq encadrés est conseillé (texte prêt dans la partie « Par tranche », volet 6, §8).

---

# Partie 1 — Les instruments, un par un

## 1. Contrôles aléatoires (direction aléatoire de même norme, sous-espaces aléatoires de même rang) — *Random controls (matched-norm random direction, random subspaces of the same rank)*

- **Maison** : tranche `volet_M` ; FR : volet M, M4 · le contrôle (paragraphe « La direction aléatoire de même norme ») ; EN : Part M, M4 · the control (paragraph "The matched-norm random direction").
- **Limites** : 4 ; **parades** : 4.
- **Ancre FR** (ligne 267 de la v3.5 FR ; l'encadré s'insère juste après) :

~~~text
**La direction aléatoire de même norme.** On ajoute ou l'on retire une direction tirée au hasard, de même norme que la direction étudiée, au même endroit. Elle n'écarte qu'une lecture : que n'importe quelle poussée de cette taille produise le même effet. Deux issues : la direction aléatoire déplace le comportement visé autant que la direction étudiée (n'importe quelle poussée suffit), ou nettement moins. Elle n'écarte pas le dommage propre à la direction étudiée — à norme égale, deux directions n'abîment pas autant le modèle ; contre le dommage, on compare les bras à dégradation appariée (réponse répétée Q6). Elle n'écarte pas non plus un corrélat, un style, un sujet ou un concept voisin. (La consigne du copilote elle-même a porté cette erreur en D-734 : elle donnait « matched-norm random direction » comme contrôle suffisant du dommage, et deux réponses en ont hérité une faute.)
~~~

- **Ancre EN** (ligne 334 de la v3.5 EN) :

~~~text
**The matched-norm random direction.** You add or remove a randomly drawn direction, of the same norm as the direction under study, at the same place. It rules out only one reading: that any push of that size produces the same effect. Two outcomes: the random direction moves the targeted behavior as much as the direction under study (any push is enough), or clearly less. It does not rule out the damage specific to the direction under study — at equal norm, two directions do not damage the model equally; against damage, you compare the arms at matched degradation (rehearsed answer Q6). Nor does it rule out a correlate, a style, a topic or a neighboring concept. (The copilot's instructions themselves carried this error in D-734: they gave "matched-norm random direction" as a sufficient control for damage, and two answers inherited an error from it.)
~~~

**Encadré complet, français :**

~~~markdown
> **⚠ Limites et parades — Contrôles aléatoires (direction aléatoire de même norme, sous-espaces aléatoires de même rang)** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Elle n'écarte qu'une lecture, « n'importe quelle poussée de cette taille fait autant » : c'est le nul de spécificité, pas un contrôle du dommage, puisqu'à norme égale deux directions n'abîment pas autant le modèle. *(source : cours, volet M, M4 ; fiche 2)*
>   **Parade :** Comparer les bras à dégradation appariée, ou tracer l'effet contre le dommage mesuré (encadré « Dégradation appariée et dose-réponse », plus bas dans M4). *(source : cours, volet M, M4 ; programme, partie 7)*
> - **Limite :** Un tirage aléatoire seul est un contrôle faible : dans la carte système d'Opus 4.8, des paires au contenu arbitraire bougent le comportement dans le même sens, plus faiblement. *(source : fiche 2 ; programme, partie 3)*
>   **Parade :** Plusieurs familles de témoins, au même rang et à dégradation appariée — des sous-espaces aléatoires (au moins vingt tirages), des contrastes sans rapport, des directions de forte variance hors de l'espace étudié, un simple prompt — et rapporter la médiane et le 95e centile des tirages. *(source : programme, parties 3 et 7 ; fiche 2)*
> - **Limite :** Quand le trait est saillant, le hasard sépare déjà : sur les sleeper agents, la meilleure de 1 000 directions aléatoires atteint 95,3 %. *(source : fiche 15)*
>   **Parade :** Situer l'instrument dans la distribution des directions aléatoires, jamais contre un seul tirage ; et ne pas lire un succès sur organisme implanté comme une preuve sur le cas naturel. *(source : programme, partie 7 ; cours, volet M, M5)*
> - **Limite :** L'aléatoire apparié en norme et l'aléatoire apparié en covariance sont deux contrôles différents ; leur confusion a coûté une journée de corrections, et le premier n'est pas au registre de ton résultat causal. *(source : cours, volet 6, §3)*
>   **Parade :** Dire lequel, et lequel a fondé quel chiffre ; préférer l'appariement en covariance, parce qu'une direction tirée là où le modèle a de la variance fait parfois beaucoup sans rien vouloir dire. *(source : cours, volet M, M4 ; cours, volet 11, réponse A7)*
~~~

**Encadré complet, anglais :**

~~~markdown
> **⚠ Limits and workarounds — Random controls (matched-norm random direction, random subspaces of the same rank)** *(v3.6, 2 October 2026)*
>
> - **Limit:** It rules out only one reading, "any push of that size does as much": it is the specificity null, not a damage control, since at equal norm two directions do not damage the model equally. *(source: course, Part M, M4; reading sheet 2)*
>   **Workaround:** Compare the arms at matched degradation, or plot the effect against measured damage (box "Matched degradation and dose-response", further down in M4). *(source: course, Part M, M4; programme, part 7)*
> - **Limit:** A single random draw is a weak control: in the Opus 4.8 system card, pairs with arbitrary content move behaviour in the same direction, more weakly. *(source: reading sheet 2; programme, part 3)*
>   **Workaround:** Several families of controls, at the same rank and at matched degradation — random subspaces (at least twenty draws), unrelated contrasts, high-variance directions outside the studied space, a plain prompt — and report the median and 95th percentile of the draws. *(source: programme, parts 3 and 7; reading sheet 2)*
> - **Limit:** When the trait is salient, chance already separates: on the sleeper agents, the best of 1,000 random directions reaches 95.3%. *(source: reading sheet 15)*
>   **Workaround:** Place the instrument within the distribution of random directions, never against a single draw; and do not read a success on an implanted organism as proof about the natural case. *(source: programme, part 7; course, Part M, M5)*
> - **Limit:** The norm-matched random and the covariance-matched random are two different controls; confusing them cost a full day of corrections, and the first is not in the register of your causal result. *(source: course, Part 6, §3)*
>   **Workaround:** Say which one, and which one grounded which number; prefer covariance matching, because a direction drawn where the model has variance sometimes does a lot while meaning nothing. *(source: course, Part M, M4; course, Part 11, answer A7)*
~~~

**Renvoi d'une ligne :**

~~~markdown
> ⚠ **Limites et parades** : contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme ») *(v3.6)*
> ⚠ **Limits and workarounds**: random controls → Part M, M4 (after "The matched-norm random direction") *(v3.6)*
~~~

**Où un renvoi ou un avertissement ponctuel est conseillé :**

- `volet2_A_a_D` — FR l. 523 : Cas d'application — sondes et pilotage : « How would you show that a steering vector's eff… · EN l. 611 : Worked case — probes and steering: "How would you show that a steering vector's effect com… — renvoi.
- `volets4_5_entete` — FR l. 1257 : Sujet 2 — Fiabilité du steering : quand une direction suffit-elle ? · EN l. 1435 : Topic 2 — Steering reliability: when does a direction suffice? — renvoi.
- `volet6` — FR l. 1402 : 2. Tes résultats, tels que ton dossier les porte au 14 septembre, corrigés le 27 par la pi… · EN l. 1579 : 2. Your results, as your dossier carries them on September 14, corrected on the 27th by th… — renvoi.
- `volet6` — FR l. 1451 : 3. Les trois contrôles à ne jamais confondre · EN l. 1593 : 3. The three controls never to confuse — renvoi.
- `volet11_53_et_fin` — FR l. 4991 : A7 · « A colleague shows you a beautiful steering result — one direction, huge behavioural… · EN l. 5313 : A7 · « A colleague shows you a beautiful steering result — one direction, huge behavioural… — renvoi.
- `volets4_5_entete` — avertissement ponctuel prêt, après FR l. 1149 / EN l. 1291 (texte dans la partie « Par tranche »).
- `volet7_A_et_C` — avertissement ponctuel prêt, après FR l. 2157 / EN l. 2291 (texte dans la partie « Par tranche »).

**Où il revient** (relevé automatique, motifs FR `aléatoire` / EN `random` ; sections, avec le nombre de lignes touchées) :

- `volet_M` — FR : l. 184 Ce que ce volet ajoute, et pourquoi il vient ava… (1) ; l. 234 M3 · Deux branches, une mesure — et ce qui te fe… (1) ; l. 257 M4 · Le contrôle : ce qu'il écarte, et il doit s… (3) ; l. 345 M8 · La forme qui sert la logique (1)
  — EN : l. 251 What this Part adds, and why it comes before the… (1) ; l. 301 M3 · Two branches, one measurement — and what wo… (1) ; l. 324 M4 · The control: what it rules out, and it must… (3) ; l. 412 M8 · The form that serves the logic (1)
- `volet2_A_a_D` — FR : l. 523 Cas d'application — sondes et pilotage : « How w… (5) ; l. 559 C bis · L'espace de travail (J-space) et le J-le… (1) ; l. 635 Cas d'application — l'interprétabilité mécaniste… (2)
  — EN : l. 575 Worked case — evaluations, capacity versus prope… (1) ; l. 611 Worked case — probes and steering: "How would yo… (7) ; l. 647 C bis · The workspace (J-space) and the J-lens —… (1) ; l. 724 Worked case — mechanistic interpretability: "Two… (3)
- `volet2_E_a_I` — FR : l. 719 Cas d'application — la généralisation comme levi… (3)
  — EN : l. 810 Worked case — generalization as a lever: "How wo… (4)
- `volet3` — FR : l. 977 4. L’oversight évolutif — et, en son sein, l’hon… (1)
  — EN : l. 1101 4. Scalable oversight — and, within it, honesty (1)
- `volets4_5_entete` — FR : l. 1179 Weak-to-Strong Generalization (OpenAI, Burns et … (1)
  — EN : l. 1254 The key papers, told one by one (1)
- `volet6` — FR : l. 1402 2. Tes résultats, tels que ton dossier les porte… (2) ; l. 1451 3. Les trois contrôles à ne jamais confondre (3) ; l. 1499 6. Ton programme de recherche, et sa revue d'ant… (1) ; l. 1578 8 · La validité des sondes d'activation hors dis… (1)
  — EN : l. 1579 2. Your results, as your dossier carries them on… (2) ; l. 1593 3. The three controls never to confuse (1) ; l. 1615 6. Your research program, and its prior-art revi… (1) ; l. 1746 8 · Out-of-distribution validity of activation p… (1)
- `volet7_B_et_D` — FR : —
  — EN : l. 2066 F·31 · Persona Vectors — Chen, Arditi (Fellows, … (1) ; l. 2183 F·42 · A3 : An Automated Alignment Agent for Saf… (1)
- `volet7_A_et_C` — FR : l. 2352 F·12 · Weak-to-Strong Generalization (Burns et a… (1)
  — EN : l. 2486 F·12 · Weak-to-Strong Generalization (Burns et a… (1)
- `volet10` — FR : l. 3096 Monitor: An AI-Driven Observability Interface — … (3) ; l. 3106 Interpreting the Second-Order Effects of Neurons… (1) ; l. 3138 SelfIE: Self-Interpretation of Large Language Mo… (2) ; l. 3158 Vector-ICL: In-context Learning with Continuous … (1) ; l. 3299 Eliciting Latent Knowledge from “Quirky” Languag… (1) ; l. 3436 Easy2Hard-Bench: Standardized Difficulty Labels … (1) ; l. 3501 Representation Engineering: A Top-Down Approach … (1) ; l. 3521 Inference-Time Intervention: Eliciting Truthful … (2)
  — EN : l. 3241 Descriptions that are correct but incomplete (9) (1) ; l. 3338 Monitor: An AI-Driven Observability Interface — … (3) ; l. 3348 Interpreting the Second-Order Effects of Neurons… (2) ; l. 3380 SelfIE: Self-Interpretation of Large Language Mo… (3) ; l. 3400 Vector-ICL: In-context Learning with Continuous … (2) ; l. 3493 Hidden in Plain Text: Emergence & Mitigation of … (1) ; l. 3539 Eliciting Latent Knowledge from “Quirky” Languag… (1) ; l. 3596 AI safety via debate — Geoffrey Irving, Paul Chr… (1) ; l. 3606 Debate Helps Supervise Unreliable Experts — Juli… (1) ; l. 3675 Easy2Hard-Bench: Standardized Difficulty Labels … (1) ; … (+5 sections)
- `volet11_1_a_20` — FR : l. 3704 2 · « What did your rank-three ablation actually… (1) ; l. 3775 6 · « How would you detect misalignment in a mod… (1) ; l. 4079 19 · « A model behaves differently when it belie… (1)
  — EN : l. 3912 1 · « Tell us about your work. » — l'ouverture (1) ; l. 3945 2 · « What did your rank-three ablation actually… (1) ; l. 4024 6 · « How would you detect misalignment in a mod… (1) ; l. 4350 19 · « A model behaves differently when it belie… (1)
- `volet11_21_a_52` — FR : l. 4273 29 · « Can you read a model's personality in its… (1) ; l. 4643 47 · « You have one experiment and a month. What… (2)
  — EN : l. 4558 29 · « Can you read a model's personality in its… (1) ; l. 4946 47 · « You have one experiment and a month. What… (2)
- `volet11_53_et_fin` — FR : l. 4776 56 · « How would you know a model is faking alig… (1) ; l. 4862 63 · Tes huit positions, dites en entier (VII) —… (1) ; l. 4991 A7 · « A colleague shows you a beautiful steerin… (2) ; l. 5096 B2 · « How would you design an evaluation a mode… (1)
  — EN : l. 5087 56 · « How would you know a model is faking alig… (1) ; l. 5177 63 · Tes huit positions, dites en entier (VII) —… (1) ; l. 5313 A7 · « A colleague shows you a beautiful steerin… (2) ; l. 5421 B2 · « How would you design an evaluation a mode… (1)

---

## 2. Dégradation appariée et dose-réponse — *Matched degradation and dose-response*

- **Maison** : tranche `volet_M` ; FR : volet M, M4 · le contrôle (paragraphes « La dégradation appariée » et « La dose-réponse ») ; EN : Part M, M4 · the control (paragraphs "Matched degradation" and "Dose-response").
- **Limites** : 6 ; **parades** : 6.
- **Ancre FR** (ligne 271 de la v3.5 FR ; l'encadré s'insère juste après) :

~~~text
**La dose-réponse.** On fait varier la force dans le bras concept et dans le bras aléatoire, et l'on trace pour chacun l'effet visé contre le dommage mesuré : la courbe de l'effet en fonction du dommage. Deux issues : à dommage égal, la courbe du bras concept passe au-dessus (spécifique), ou les deux courbes se superposent (dommage). Un seul bras ne suffit pas : un effet spécifique qui demande une forte poussée monte, lui aussi, avec le dommage.
~~~

- **Ancre EN** (ligne 338 de la v3.5 EN) :

~~~text
**Dose-response.** You vary the strength in the concept arm and in the random arm, and for each one you plot the targeted effect against the measured damage: the curve of the effect as a function of damage. Two outcomes: at equal damage, the concept arm's curve runs above (specific), or the two curves overlap (damage). A single arm is not enough: a specific effect that needs a strong push also rises with damage.
~~~

**Encadré complet, français :**

~~~markdown
> **⚠ Limites et parades — Dégradation appariée et dose-réponse** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Elle ne vaut que sur le composite choisi : un dommage que le composite ne mesure pas reste possible — retirer le concept « test » peut abîmer le code ou la fiction. *(source : programme, parties 3 et 8)*
>   **Parade :** Bâtir le composite d'après les dégâts attendus du concept (tests unitaires de code pour « test », cohérence de fiction), avec plusieurs mesures — exactitude tenue à part, cohérence jugée, perplexité — et des tolérances fixées au pré-enregistrement. *(source : programme, parties 3, 7 et 8)*
> - **Limite :** Certains réglages ne s'apparient pas : un témoin peut n'atteindre la même dégradation à aucune force. *(source : programme, partie 7)*
>   **Parade :** Ne pas comparer à ce réglage, le dire, et rapporter des courbes de l'effet contre la dégradation plutôt qu'un point. *(source : programme, partie 7 ; cours, volet M, M4)*
> - **Limite :** Écarter le dommage n'établit pas la spécificité : à force 0,01×, la carte de Fable 5 rend la dégradation négligeable, mais ses témoins restent « comparable or smaller » sur l'axe du désalignement. *(source : fiche 2)*
>   **Parade :** Une courbe dose-réponse contre plusieurs témoins : la courbe du concept doit passer au-dessus à chaque niveau de dommage. *(source : cours, volet 2, §C, K47 ; fiche 2)*
> - **Limite :** À dégradation égale, l'effet peut encore venir d'un corrélat ou d'un concept voisin : ton ablation de rang trois déplaçait la valence, pas le concept. *(source : cours, volet M, M4 ; cours, volet 6, §2)*
>   **Parade :** Le témoin sans pression et la direction d'un concept rival, eux aussi à dégradation appariée. *(source : cours, volet M, M4)*
> - **Limite :** La cohérence jugée passe par un juge, avec ses propres biais. *(source : fiches, partie B, piège 6)*
>   **Parade :** Un juge scellé et un audit humain stratifié (encadré « Juges LLM », volet 6, §2). *(source : programme, partie 3)*
> - **Limite :** Les jugements de dégradation se contredisent d'une carte à l'autre : force 0,1× « roughly the maximum » sans dégénérescence pour Mythos Preview, dégradation de chaque direction à 0,10× pour Opus 4.8. *(source : fiches, partie B)*
>   **Parade :** Mesurer la dégradation dans son propre dispositif, jamais la reprendre d'un autre : le dommage se mesure, il ne se suppose pas. *(source : cours, volet M, M4)*
~~~

**Encadré complet, anglais :**

~~~markdown
> **⚠ Limits and workarounds — Matched degradation and dose-response** *(v3.6, 2 October 2026)*
>
> - **Limit:** It holds only on the chosen composite: damage the composite does not measure remains possible — removing the concept "test" can damage code or fiction. *(source: programme, parts 3 and 8)*
>   **Workaround:** Build the composite from the concept's expected damage (code unit tests for "test", fiction coherence), with several measures — held-out accuracy, judged coherence, perplexity — and tolerances fixed at preregistration. *(source: programme, parts 3, 7 and 8)*
> - **Limit:** Some settings cannot be matched: a control may reach the same degradation at no strength. *(source: programme, part 7)*
>   **Workaround:** Do not compare at that setting, say so, and report curves of effect against degradation rather than a single point. *(source: programme, part 7; course, Part M, M4)*
> - **Limit:** Ruling out damage does not establish specificity: at 0.01× strength the Fable 5 card makes degradation negligible, yet its controls stay "comparable or smaller" on the misalignment axis. *(source: reading sheet 2)*
>   **Workaround:** A dose-response curve against several controls: the concept's curve must rise above them at every level of damage. *(source: course, Part 2, §C, K47; reading sheet 2)*
> - **Limit:** At equal degradation, the effect can still come from a correlate or a neighbouring concept: your rank-three ablation moved valence, not the concept. *(source: course, Part M, M4; course, Part 6, §2)*
>   **Workaround:** The no-pressure control arm and a rival concept's direction, also at matched degradation. *(source: course, Part M, M4)*
> - **Limit:** Judged coherence goes through a judge, with its own biases. *(source: reading sheets, part B, trap 6)*
>   **Workaround:** A sealed judge and a stratified human audit (box "LLM judges", Part 6, §2). *(source: programme, part 3)*
> - **Limit:** Degradation judgements contradict each other across cards: 0.1× strength "roughly the maximum" without degeneracy for Mythos Preview, degradation from every direction at 0.10× for Opus 4.8. *(source: reading sheets, part B)*
>   **Workaround:** Measure degradation in your own setup, never borrow it from another: damage is measured, not assumed. *(source: course, Part M, M4)*
~~~

**Renvoi d'une ligne :**

~~~markdown
> ⚠ **Limites et parades** : dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») *(v3.6)*
> ⚠ **Limits and workarounds**: matched degradation and dose-response → Part M, M4 (after "Dose-response") *(v3.6)*
~~~

**Où un renvoi ou un avertissement ponctuel est conseillé :**

- `volet2_A_a_D` — FR l. 523 : Cas d'application — sondes et pilotage : « How would you show that a steering vector's eff… · EN l. 611 : Worked case — probes and steering: "How would you show that a steering vector's effect com… — renvoi.
- `volet2_A_a_D` — FR l. 589 : Cas d'application — l'espace de travail et le J-lens : « An internal "this is fake" signal… · EN l. 677 : Worked case — the workspace and the J-lens: "An internal "this is fake" signal appears bef… — renvoi.
- `volets4_5_entete` — FR l. 1257 : Sujet 2 — Fiabilité du steering : quand une direction suffit-elle ? · EN l. 1435 : Topic 2 — Steering reliability: when does a direction suffice? — renvoi.
- `volet6` — FR l. 1451 : 3. Les trois contrôles à ne jamais confondre · EN l. 1593 : 3. The three controls never to confuse — renvoi.
- `volet11_1_a_20` — FR l. 3704 : 2 · « What did your rank-three ablation actually show? » · EN l. 3945 : 2 · « What did your rank-three ablation actually show? » — renvoi.
- `volet11_53_et_fin` — FR l. 4991 : A7 · « A colleague shows you a beautiful steering result — one direction, huge behavioural… · EN l. 5313 : A7 · « A colleague shows you a beautiful steering result — one direction, huge behavioural… — renvoi.
- `volets4_5_entete` — avertissement ponctuel prêt, après FR l. 1149 / EN l. 1291 (texte dans la partie « Par tranche »).
- `volet7_A_et_C` — avertissement ponctuel prêt, après FR l. 2157 / EN l. 2291 (texte dans la partie « Par tranche »).

**Où il revient** (relevé automatique, motifs FR `dégradation appariée|dégradation égale|dommage égal|dommage apparié|dose-réponse` / EN `matched degradation|equal degradation|equal damage|matched damage|dose-response` ; sections, avec le nombre de lignes touchées) :

- `tete_volet1` — FR : l. 1 COURS D'ALIGNEMENT — VERSION FUSIONNÉE v3.5 — 27… (1)
  — EN : l. 21 ALIGNMENT COURSE — MERGED VERSION v3.5 — Septemb… (1)
- `volet_M` — FR : l. 234 M3 · Deux branches, une mesure — et ce qui te fe… (1) ; l. 257 M4 · Le contrôle : ce qu'il écarte, et il doit s… (4)
  — EN : l. 286 M2 · The bet: on the model, never on the method (2) ; l. 301 M3 · Two branches, one measurement — and what wo… (1) ; l. 324 M4 · The control: what it rules out, and it must… (4)
- `volet2_A_a_D` — FR : l. 523 Cas d'application — sondes et pilotage : « How w… (4) ; l. 559 C bis · L'espace de travail (J-space) et le J-le… (1) ; l. 589 Cas d'application — l'espace de travail et le J-… (1) ; l. 635 Cas d'application — l'interprétabilité mécaniste… (2)
  — EN : l. 611 Worked case — probes and steering: "How would yo… (4) ; l. 647 C bis · The workspace (J-space) and the J-lens —… (1) ; l. 677 Worked case — the workspace and the J-lens: "An … (2) ; l. 724 Worked case — mechanistic interpretability: "Two… (2)
- `volet3` — FR : l. 977 4. L’oversight évolutif — et, en son sein, l’hon… (1)
  — EN : l. 1101 4. Scalable oversight — and, within it, honesty (1)
- `volets4_5_entete` — FR : l. 1231 3. Ton ancrage empirique : l’eval-awareness (1) ; l. 1251 A. Tes sujets FORT — ta thèse peut être la colon… (2)
  — EN : l. 1403 3. Your empirical anchor: eval-awareness (1) ; l. 1428 A. Your STRONG topics — your thesis can be the b… (2)
- `volet6` — FR : l. 1578 8 · La validité des sondes d'activation hors dis… (1)
  — EN : l. 1746 8 · Out-of-distribution validity of activation p… (1)
- `volet11_1_a_20` — FR : l. 3656 VOLET 11 — Les réponses complètes (v2.3, 23 sept… (1) ; l. 4079 19 · « A model behaves differently when it belie… (6)
  — EN : l. 3895 PART 11 — The complete answers (v2.3, 23 Septemb… (1) ; l. 4350 19 · « A model behaves differently when it belie… (4)
- `volet11_53_et_fin` — FR : l. 4862 63 · Tes huit positions, dites en entier (VII) —… (1) ; l. 4950 A4 · « Your rank-three result is on an 8B model.… (2) ; l. 4991 A7 · « A colleague shows you a beautiful steerin… (1)
  — EN : l. 5177 63 · Tes huit positions, dites en entier (VII) —… (1) ; l. 5268 A4 · « Your rank-three result is on an 8B model.… (2) ; l. 5313 A7 · « A colleague shows you a beautiful steerin… (1)

---

## 3. Jeu tenu à part — *Held-out set*

- **Maison** : tranche `volet_M` ; FR : volet M, M4 · le contrôle (paragraphe « Le jeu tenu à part ») ; EN : Part M, M4 · the control (paragraph "The held-out set").
- **Limites** : 5 ; **parades** : 4.
- **Ancre FR** (ligne 293 de la v3.5 FR ; l'encadré s'insère juste après) :

~~~text
est absolue : rien n'est entraîné, calibré ni choisi sur le jeu tenu à part.
~~~

- **Ancre EN** (ligne 360 de la v3.5 EN) :

~~~text
is absolute: nothing is trained, calibrated or chosen on the held-out set.
~~~

**Encadré complet, français :**

~~~markdown
> **⚠ Limites et parades — Jeu tenu à part** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Tenir à part des paraphrases au lieu de familles ne mesure qu'une généralisation proche. *(source : programme, partie 3 ; explication du 2 octobre, §3)*
>   **Parade :** Séparer par familles entières, et lire trois distances : instances nouvelles, familles tenues à part en un tour, familles tenues à part en agentique à plusieurs tours, qui est le critère principal. *(source : programme, partie 3)*
> - **Limite :** Une famille tenue à part peut fuir dans l'entraînement. *(source : programme, partie 8)*
>   **Parade :** Contrôler les n-grammes des familles tenues à part dans les données d'entraînement, et séparer par famille. *(source : programme, parties 3 et 8)*
> - **Limite :** Choisir la couche, le seuil ou le prédicteur sur le jeu de test le contamine ; extraire et évaluer sur les mêmes items est circulaire. *(source : cours, volet 2, C bis ; README du dépôt)*
>   **Parade :** Des jeux disjoints, gelés d'avance : un pour extraire, un pour valider et choisir la couche, un pour cadrer les évaluations, un pour la sonde neuve après l'entraînement. *(source : programme, partie 3 ; cours, volet 2, C bis)*
> - **Limite :** Un jeu tenu à part peut ne pas représenter le réel : des pots de miel tenus à part ne sont peut-être pas représentatifs. *(source : fiche 12)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** Entraîner ou itérer sur l'évaluation la vide : la métrique baisse, le problème reste. *(source : fiche 12)*
>   **Parade :** Garder des métriques d'audit tenues à part, et des détecteurs scellés qui n'entrent jamais dans la décision. *(source : fiche 12 ; fiche 19)*
~~~

**Encadré complet, anglais :**

~~~markdown
> **⚠ Limits and workarounds — Held-out set** *(v3.6, 2 October 2026)*
>
> - **Limit:** Holding out paraphrases instead of families measures only near generalization. *(source: programme, part 3; explanation of 2 October, §3)*
>   **Workaround:** Separate by whole families, and read three distances: new instances, held-out families in one turn, held-out families in multi-turn agentic settings, which is the main criterion. *(source: programme, part 3)*
> - **Limit:** A held-out family can leak into training. *(source: programme, part 8)*
>   **Workaround:** Check the held-out families' n-grams against the training data, and separate by family. *(source: programme, parts 3 and 8)*
> - **Limit:** Choosing the layer, threshold or predictor on the test set contaminates it; extracting and evaluating on the same items is circular. *(source: course, Part 2, C bis; repository README)*
>   **Workaround:** Disjoint sets, frozen in advance: one to extract, one to validate and pick the layer, one to frame the evaluations, one for the fresh probe after training. *(source: programme, part 3; course, Part 2, C bis)*
> - **Limit:** A held-out set may not represent the real case: held-out honeypots may not be representative. *(source: reading sheet 12)*
>   **Workaround:** none known; say so.
> - **Limit:** Training or iterating on the evaluation empties it: the metric drops, the problem stays. *(source: reading sheet 12)*
>   **Workaround:** Keep held-out audit metrics, and sealed detectors that never enter the decision. *(source: reading sheet 12; reading sheet 19)*
~~~

**Renvoi d'une ligne :**

~~~markdown
> ⚠ **Limites et parades** : jeu tenu à part → volet M, M4 (après « Le jeu tenu à part ») *(v3.6)*
> ⚠ **Limits and workarounds**: held-out set → Part M, M4 (after "The held-out set") *(v3.6)*
~~~

**Où un renvoi ou un avertissement ponctuel est conseillé :**

- `volet7_B_et_D` — FR l. 1843 : F·34 · Model Spec Midtraining — Li, Wichers (Fellows), Price, Marks, Kutasov ; 5 mai 2026 … · EN l. 2008 : F·34 · Model Spec Midtraining — Li, Wichers (Fellows), Price, Marks, Kutasov; 5 May 2026; … — renvoi.
- `volet11_1_a_20` — FR l. 3829 : 8 · « How would you train models to be more robustly aligned with intended objectives? » *… · EN l. 4077 : 8 · « How would you train models to be more robustly aligned with intended objectives? » *… — renvoi.
- `volet11_21_a_52` — FR l. 4129 : 21 · « A probe trained on synthetic examples of a bad behaviour must catch the real thing.… · EN l. 4404 : 21 · « A probe trained on synthetic examples of a bad behaviour must catch the real thing.… — renvoi.

**Où il revient** (relevé automatique, motifs FR `tenu.? à part|tenue.? à part` / EN `held-out|held out` ; sections, avec le nombre de lignes touchées) :

- `volet_M` — FR : l. 257 M4 · Le contrôle : ce qu'il écarte, et il doit s… (4) ; l. 316 M6 · Le signe d'échec, et le protocole possible (1) ; l. 389 M10 · La grille, à relire avant chaque répétitio… (1)
  — EN : l. 286 M2 · The bet: on the model, never on the method (1) ; l. 324 M4 · The control: what it rules out, and it must… (4) ; l. 383 M6 · The failure sign, and the feasible protocol (1) ; l. 456 M10 · The checklist, to reread before each rehea… (1)
- `volet2_A_a_D` — FR : l. 442 Cas d'application — organismes modèles et bancs … (3) ; l. 523 Cas d'application — sondes et pilotage : « How w… (1) ; l. 559 C bis · L'espace de travail (J-space) et le J-le… (1)
  — EN : l. 528 Worked case — model organisms and testbeds: "How… (4) ; l. 611 Worked case — probes and steering: "How would yo… (1) ; l. 647 C bis · The workspace (J-space) and the J-lens —… (1)
- `volet2_E_a_I` — FR : l. 719 Cas d'application — la généralisation comme levi… (1) ; l. 834 I. Interventions d’entraînement & unlearning — c… (1) ; l. 842 Cas d'application — interventions d'entraînement… (1)
  — EN : l. 810 Worked case — generalization as a lever: "How wo… (2) ; l. 927 I. Training interventions & unlearning — changin… (1) ; l. 936 Worked case — training interventions and unlearn… (1)
- `volet7_A_et_C` — FR : —
  — EN : l. 2606 F·17 · L'unlearning mis à l'épreuve (Deeb and Ro… (1)
- `volet10` — FR : l. 3404 Weak-to-Strong Reasoning — Yuqing Yang, Yan Ma, … (1) ; l. 3466 Balancing Label Quantity and Quality for Scalabl… (1)
  — EN : l. 3313 AI Sandbagging: Language Models can Strategicall… (1) ; l. 3370 Looking Inward: Language Models Can Learn About … (1) ; l. 3456 Bias-Augmented Consistency Training Reduces Bias… (1) ; l. 3705 Balancing Label Quantity and Quality for Scalabl… (1) ; l. 3727 The Internal State of an LLM Knows When It’s Lyi… (1)
- `volet11_21_a_52` — FR : —
  — EN : l. 4981 49 · « Training a strong model on labels from a … (1)
- `volet11_53_et_fin` — FR : —
  — EN : l. 5486 B5 · « The directions page calls one setting "un… (1)

---

## 4. Cas connu — *Known case*

- **Maison** : tranche `volet_M` ; FR : volet M, M5 · le nul et le cas connu (fin de section) ; EN : Part M, M5 · the null and the known case (end of section).
- **Limites** : 6 ; **parades** : 6.
- **Ancre FR** (ligne 314 de la v3.5 FR ; l'encadré s'insère juste après) :

~~~text
**Ce qu'un cas connu prouve, et ce qu'il ne prouve pas.** Les sondes de défection d'Anthropic sur les sleeper agents ont été construites à partir de paires de contraste génériques, sans rien savoir du déclencheur ni du comportement dangereux — c'est leur force. Leur limite, dite par les auteurs : la saillance du trait pourrait venir de la façon dont la porte dérobée a été insérée. Et cette porte dérobée était implantée, pas apparue d'elle-même : qu'un modèle devenu trompeur de lui-même porte un trait aussi saillant reste ouvert. Un résultat positif sur un organisme construit est un cas connu pour l'instrument ; ce n'est pas une preuve qu'il généralise au cas naturel.
~~~

- **Ancre EN** (ligne 381 de la v3.5 EN) :

~~~text
**What a known case proves, and what it does not.** Anthropic's defection probes on the sleeper agents were built from generic contrast pairs, without knowing anything about the trigger or the dangerous behavior — that is their strength. Their limit, stated by the authors: the salience of the feature could come from the way the backdoor was inserted. And that backdoor was implanted, it did not appear on its own: whether a model that became deceptive on its own carries such a salient feature remains open. A positive result on a constructed organism is a known case for the instrument; it is not proof that it generalizes to the natural case.
~~~

**Encadré complet, français :**

~~~markdown
> **⚠ Limites et parades — Cas connu** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Nécessaire, pas suffisant : une intention implantée est peut-être plus saillante qu'une intention naturelle — sur les sleeper agents, la meilleure de 1 000 directions aléatoires atteint déjà 95,3 %. *(source : passation, §5.2 ; fiche 15)*
>   **Parade :** En partie : deux fabrications différentes du même comportement, et l'organisme d'une autre équipe ; pour conclure sur le cas naturel, aucune parade connue — un succès borne l'instrument, on le dit. *(source : cours, volet 6, §8 ; cours, volet 2, §A, K71)*
> - **Limite :** Le cas connu ne vaut qu'au même réglage : validé à une autre dose ou à un autre seuil, il laisse ouvert qu'un nul vienne d'un rang trop bas ou d'un seuil trop strict. *(source : fiche 7 ; contre-lecture des fiches ; cours, volet 2, §A, K71)*
>   **Parade :** Valider le cas connu avec le même instrument, au même rang, à la même dose et au même seuil que la mesure. *(source : cours, volet M, M5 ; fiche 7)*
> - **Limite :** Validé sur les formulations de l'entraînement, le cas connu peut ne mesurer que la reconnaissance de ces formulations. *(source : explication du 2 octobre, §3 ; programme, partie 3)*
>   **Parade :** Valider le cas connu sur des formulations tenues à part. *(source : programme, partie 3)*
> - **Limite :** Certains cas connus sont faibles : pour « je suis noté », le cas positif n'est fait que d'habitudes de présentation. *(source : programme, parties 3 et 8)*
>   **Parade :** Le déclarer, et retirer le bras qui en dépend si sa porte ne passe pas. *(source : programme, partie 8)*
> - **Limite :** Un nul sans puissance connue ne dit presque rien, et une puissance élevée ne remplace pas un cas connu. *(source : cours, volet M, M5)*
>   **Parade :** Dire une borne, avec son budget et sa puissance, jamais une absence. *(source : cours, volet M, M5)*
> - **Limite :** Chaque instrument a son cas connu : celui d'une sonde ne vaut pas pour l'angle mort du J-lens. *(source : passation, §5.2)*
>   **Parade :** Trois cas connus distincts : un organisme conditionné à l'évaluation, un organisme à concept planté, un organisme entraîné à l'action par réflexe. *(source : explication du 2 octobre, §3 ; passation, §5.2 ; programme, partie 3)*
~~~

**Encadré complet, anglais :**

~~~markdown
> **⚠ Limits and workarounds — Known case** *(v3.6, 2 October 2026)*
>
> - **Limit:** Necessary, not sufficient: an implanted intention may be more salient than a natural one — on the sleeper agents, the best of 1,000 random directions already reaches 95.3%. *(source: handover, §5.2; reading sheet 15)*
>   **Workaround:** In part: two different manufactures of the same behaviour, and another team's organism; to conclude on the natural case, none known — a success bounds the instrument, say so. *(source: course, Part 6, §8; course, Part 2, §A, K71)*
> - **Limit:** The known case holds only at the same setting: validated at another dose or threshold, it leaves open that a null comes from too low a rank or too strict a threshold. *(source: reading sheet 7; counter-reading of the sheets; course, Part 2, §A, K71)*
>   **Workaround:** Validate the known case with the same instrument, at the same rank, dose and threshold as the measurement. *(source: course, Part M, M5; reading sheet 7)*
> - **Limit:** Validated on the training phrasings, the known case may only measure recognition of those phrasings. *(source: explanation of 2 October, §3; programme, part 3)*
>   **Workaround:** Validate the known case on held-out phrasings. *(source: programme, part 3)*
> - **Limit:** Some known cases are weak: for "I am being graded", the positive case is only made of presentation habits. *(source: programme, parts 3 and 8)*
>   **Workaround:** Declare it, and drop the arm that depends on it if its gate fails. *(source: programme, part 8)*
> - **Limit:** A null without known power says almost nothing, and high power does not replace a known case. *(source: course, Part M, M5)*
>   **Workaround:** State a bound, with its budget and power, never an absence. *(source: course, Part M, M5)*
> - **Limit:** Each instrument has its own known case: a probe's does not cover the J-lens blind spot. *(source: handover, §5.2)*
>   **Workaround:** Three distinct known cases: an evaluation-conditioned organism, a planted-concept organism, an organism trained to act by reflex. *(source: explanation of 2 October, §3; handover, §5.2; programme, part 3)*
~~~

**Renvoi d'une ligne :**

~~~markdown
> ⚠ **Limites et parades** : cas connu → volet M, M5 (fin de section) *(v3.6)*
> ⚠ **Limits and workarounds**: known case → Part M, M5 (end of section) *(v3.6)*
~~~

**Où un renvoi ou un avertissement ponctuel est conseillé :**

- `tete_volet1` — FR l. 132 : Q4. « Comment saurais-tu qu’un modèle “fait semblant” d’être aligné ? » · EN l. 190 : Q4. "How would you know that a model is “pretending” to be aligned?" — renvoi.
- `volet2_A_a_D` — FR l. 442 : Cas d'application — organismes modèles et bancs d'essai : « How would you build a monitor … · EN l. 528 : Worked case — model organisms and testbeds: "How would you build a monitor for a behaviour… — renvoi.
- `volet2_A_a_D` — FR l. 488 : Cas d'application — évaluations, capacité contre propension : « How would you separate a m… · EN l. 575 : Worked case — evaluations, capacity versus propensity: "How would you separate a model's c… — renvoi.
- `volet2_E_a_I` — FR l. 760 : Cas d'application — monitoring et AI control : « How would you design a control evaluation… · EN l. 852 : Worked case — monitoring and AI control: "How would you design a control evaluation for a … — renvoi.
- `volet2_E_a_I` — FR l. 842 : Cas d'application — interventions d'entraînement et unlearning : « How would you verify th… · EN l. 936 : Worked case — training interventions and unlearning: "How would you verify that a capabili… — renvoi.
- `volets4_5_entete` — FR l. 1287 : Sujet 5 — Construire un model organism (MOYEN) · EN l. 1466 : Topic 5 — Building a model organism (MEDIUM) — renvoi.
- `volet6` — FR l. 1578 : 8 · La validité des sondes d'activation hors distribution — pourquoi « validée par interve… · EN l. 1746 : 8 · Out-of-distribution validity of activation probes — why "validated by causal intervent… — renvoi.
- `volet11_1_a_20` — FR l. 3775 : 6 · « How would you detect misalignment in a model you can't fully trust? » *(question rée… · EN l. 4024 : 6 · « How would you detect misalignment in a model you can't fully trust? » *(question rée… — renvoi.
- `volet11_21_a_52` — FR l. 4187 : 24 · « Probes drift toward "I am being evaluated" under adversarial pressure. How do you k… · EN l. 4463 : 24 · « Probes drift toward "I am being evaluated" under adversarial pressure. How do you k… — renvoi.
- `volet11_53_et_fin` — FR l. 4938 : A3 · « What if the probes just don't work at all — the two-family test fails, nothing gene… · EN l. 5255 : A3 · « What if the probes just don't work at all — the two-family test fails, nothing gene… — renvoi.
- `volet3` — avertissement ponctuel prêt, après FR l. 1001 / EN l. 1126 (texte dans la partie « Par tranche »).
- `volet7_A_et_C` — avertissement ponctuel prêt, après FR l. 2080 / EN l. 2214 (texte dans la partie « Par tranche »).

**Où il revient** (relevé automatique, motifs FR `cas connu|cas positif` / EN `known case|positive case` ; sections, avec le nombre de lignes touchées) :

- `tete_volet1` — FR : l. 1 COURS D'ALIGNEMENT — VERSION FUSIONNÉE v3.5 — 27… (1) ; l. 132 Q4. « Comment saurais-tu qu’un modèle “fait semb… (1) ; l. 158 Q9. « Quelle est ta “théorie de l’impact” : si t… (1)
  — EN : l. 21 ALIGNMENT COURSE — MERGED VERSION v3.5 — Septemb… (1) ; l. 190 Q4. "How would you know that a model is “pretend… (1) ; l. 221 Q9. "What is your “theory of impact”: if your re… (1)
- `volet_M` — FR : l. 184 Ce que ce volet ajoute, et pourquoi il vient ava… (1) ; l. 257 M4 · Le contrôle : ce qu'il écarte, et il doit s… (1) ; l. 298 M5 · Le nul et le cas connu (5) ; l. 365 M9 · Un cas complet, avant et après : la premièr… (3) ; l. 389 M10 · La grille, à relire avant chaque répétitio… (1)
  — EN : l. 251 What this Part adds, and why it comes before the… (1) ; l. 324 M4 · The control: what it rules out, and it must… (1) ; l. 365 M5 · The null and the known case (5) ; l. 432 M9 · A complete case, before and after: the firs… (3) ; l. 456 M10 · The checklist, to reread before each rehea… (1)
- `volet2_A_a_D` — FR : l. 414 Les méthodes de la safety, expliquées et illustr… (1) ; l. 442 Cas d'application — organismes modèles et bancs … (1) ; l. 488 Cas d'application — évaluations, capacité contre… (1) ; l. 523 Cas d'application — sondes et pilotage : « How w… (1) ; l. 559 C bis · L'espace de travail (J-space) et le J-le… (1) ; l. 589 Cas d'application — l'espace de travail et le J-… (1) ; l. 635 Cas d'application — l'interprétabilité mécaniste… (2)
  — EN : l. 499 The methods of safety, explained and illustrated… (1) ; l. 528 Worked case — model organisms and testbeds: "How… (1) ; l. 575 Worked case — evaluations, capacity versus prope… (1) ; l. 611 Worked case — probes and steering: "How would yo… (1) ; l. 647 C bis · The workspace (J-space) and the J-lens —… (1) ; l. 677 Worked case — the workspace and the J-lens: "An … (1) ; l. 724 Worked case — mechanistic interpretability: "Two… (2)
- `volet2_E_a_I` — FR : l. 719 Cas d'application — la généralisation comme levi… (1) ; l. 760 Cas d'application — monitoring et AI control : «… (1) ; l. 805 Cas d'application — robustesse adverse et mésusa… (1) ; l. 842 Cas d'application — interventions d'entraînement… (5)
  — EN : l. 810 Worked case — generalization as a lever: "How wo… (1) ; l. 852 Worked case — monitoring and AI control: "How wo… (1) ; l. 898 Worked case — adversarial robustness and misuse:… (1) ; l. 936 Worked case — training interventions and unlearn… (5)
- `volet3` — FR : l. 899 1. Évaluer les capacités (1) ; l. 923 2. Évaluer l’alignement (1) ; l. 953 3. Le contrôle par le monitoring (AI control) (1) ; l. 977 4. L’oversight évolutif — et, en son sein, l’hon… (1) ; l. 1003 5. La robustesse adverse (2) ; l. 1029 6. Le domaine « divers » : désapprentissage et g… (2)
  — EN : l. 1020 1. Evaluating capabilities (1) ; l. 1045 2. Evaluating alignment (1) ; l. 1076 3. Control through monitoring (AI control) (1) ; l. 1101 4. Scalable oversight — and, within it, honesty (1) ; l. 1128 5. Adversarial robustness (2) ; l. 1155 6. The "miscellaneous" domain: unlearning and mu… (2)
- `volets4_5_entete` — FR : l. 1203 L’unlearning mis à l’épreuve (Deeb et Roger) (1) ; l. 1235 4. La théorie de l’impact (1)
  — EN : l. 1254 The key papers, told one by one (1) ; l. 1408 4. The theory of impact (1)
- `volet6` — FR : l. 1578 8 · La validité des sondes d'activation hors dis… (1)
  — EN : l. 1746 8 · Out-of-distribution validity of activation p… (1)
- `volet7_A_et_C` — FR : l. 2472 F·17 · L'unlearning mis à l'épreuve (Deeb et Rog… (1)
  — EN : l. 2606 F·17 · L'unlearning mis à l'épreuve (Deeb and Ro… (1)
- `volet11_1_a_20` — FR : l. 3747 4 · « Did it replicate? » (1)
  — EN : l. 3992 4 · « Did it replicate? » (1)

---

## 5. Organismes modèles — *Model organisms*

- **Maison** : tranche `volet2_A_a_D` ; FR : volet 2, §A · testbeds et organismes modèles (après « En pratique — Auditing Hidden Objectives ») ; EN : Part 2, §A · testbeds and model organisms (after "In practice — Auditing Hidden Objectives").
- **Limites** : 7 ; **parades** : 4.
- **Ancre FR** (ligne 440 de la v3.5 FR ; l'encadré s'insère juste après) :

~~~text
En pratique — Auditing Hidden Objectives (Anthropic). Ici le but était méthodologique : peut-on auditer un modèle pour découvrir un objectif caché qu’il ne révèle pas ? Plutôt que d’attendre de trouver un tel modèle dans la nature, les auteurs en ont fabriqué un — entraîné à poursuivre un objectif dissimulé — puis l’ont utilisé comme banc d’essai pour un « jeu d’audit » : des équipes recevaient le modèle sans connaître son objectif et devaient le débusquer avec différents outils (analyse de données, interprétabilité). L’organisme fournit la vérité-terrain qui dit si une équipe a réellement trouvé le bon objectif ou s’est trompée — ce qui transforme « auditer un modèle » en une compétence qu’on peut mesurer et comparer.
~~~

- **Ancre EN** (ligne 526 de la v3.5 EN) :

~~~text
In practice — Auditing Hidden Objectives (Anthropic). Here the goal was methodological: can we audit a model to discover a hidden objective that it does not reveal? Rather than waiting to find such a model in the wild, the authors manufactured one — trained to pursue a concealed objective — then used it as a benchmark for an "auditing game": teams received the model without knowing its objective and had to ferret it out with various tools (data analysis, interpretability). The organism provides the ground truth that says whether a team actually found the right objective or got it wrong — which turns "auditing a model" into a skill that can be measured and compared.
~~~

**Encadré complet, français :**

~~~markdown
> **⚠ Limites et parades — Organismes modèles** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Construit n'est pas naturel : la saillance peut venir de l'insertion, et l'alignement trompeur instrumental n'a été trouvé dans aucun système réel. *(source : fiche 15 ; fiches, partie B, piège 5)*
>   **Parade :** Conclure sur l'instrument seulement ; conclure sur le fond avec les modèles sans organisme. *(source : programme, partie 8)*
> - **Limite :** L'organisme peut être artificiellement facile : objectif décrit en clair dans les documents synthétiques, artefacts du pipeline. *(source : fiche 16)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** L'implant peut rater : le fine-tuning sur documents synthétiques implante parfois, pas toujours, une vraie croyance. *(source : cours, volet 2, §E, K52)*
>   **Parade :** Vérifier chaque copie par son comportement, et filtrer par l'inférence en aval et une sonde. *(source : cours, volet 2, §A, K71 ; cours, volet 2, §E, K52)*
> - **Limite :** Ce que l'interprétabilité voit dans un organisme dépend de sa méthode d'entraînement. *(source : rapport d'antériorité 5 du 2 octobre, « The Model Organism Lottery », résumé lu — rapport)*
>   **Parade :** Planter le même comportement par plusieurs recettes (consigne, documents synthétiques, démonstrations), en tenir une à part, et ajouter l'organisme d'une autre équipe. *(source : cours, volet 2, §A, K71)*
> - **Limite :** Un comportement fourni au modèle confond la généralisation : dans le papier sur le désalignement émergent, les triches étaient d'abord enseignées. *(source : fiche 13)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** Une réplication sur un modèle récent peut mesurer la mémorisation du scénario : les transcripts d'Alignment Faking ont été réinclus dans l'entraînement. *(source : fiches, partie C)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** La conscience d'évaluation native d'un modèle de 8B peut être trop faible pour l'étudier. *(source : programme, partie 8)*
>   **Parade :** L'organisme en donne le cas connu, et une extension vers environ 32B est prévue. *(source : programme, partie 8)*
~~~

**Encadré complet, anglais :**

~~~markdown
> **⚠ Limits and workarounds — Model organisms** *(v3.6, 2 October 2026)*
>
> - **Limit:** Built is not natural: salience may come from the insertion, and instrumental deceptive alignment has not been found in any real system. *(source: reading sheet 15; reading sheets, part B, trap 5)*
>   **Workaround:** Conclude only about the instrument; draw substantive conclusions from the models without an organism. *(source: programme, part 8)*
> - **Limit:** The organism may be artificially easy: objective stated plainly in the synthetic documents, pipeline artefacts. *(source: reading sheet 16)*
>   **Workaround:** none known; say so.
> - **Limit:** The implant can fail: fine-tuning on synthetic documents sometimes, not always, implants a real belief. *(source: course, Part 2, §E, K52)*
>   **Workaround:** Check each copy by its behaviour, and filter by downstream inference and a probe. *(source: course, Part 2, §A, K71; course, Part 2, §E, K52)*
> - **Limit:** What interpretability sees in an organism depends on how it was trained. *(source: prior-art report 5 of 2 October, "The Model Organism Lottery", abstract read — report)*
>   **Workaround:** Plant the same behaviour through several recipes (instruction, synthetic documents, demonstrations), hold one out, and add another team's organism. *(source: course, Part 2, §A, K71)*
> - **Limit:** A behaviour handed to the model confounds generalization: in the emergent-misalignment paper, the hacks were taught first. *(source: reading sheet 13)*
>   **Workaround:** none known; say so.
> - **Limit:** A replication on a recent model may measure memorization of the scenario: the Alignment Faking transcripts were re-included in training. *(source: reading sheets, part C)*
>   **Workaround:** none known; say so.
> - **Limit:** The native evaluation awareness of an 8B model may be too weak to study. *(source: programme, part 8)*
>   **Workaround:** The organism provides the known case, and an extension to about 32B is planned. *(source: programme, part 8)*
~~~

**Renvoi d'une ligne :**

~~~markdown
> ⚠ **Limites et parades** : organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») *(v3.6)*
> ⚠ **Limits and workarounds**: model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives") *(v3.6)*
~~~

**Où un renvoi ou un avertissement ponctuel est conseillé :**

- `tete_volet1` — FR l. 132 : Q4. « Comment saurais-tu qu’un modèle “fait semblant” d’être aligné ? » · EN l. 190 : Q4. "How would you know that a model is “pretending” to be aligned?" — renvoi.
- `volet2_E_a_I` — FR l. 675 : Cas d'application — la supervision évolutive : « Would unsupervised elicitation still work… · EN l. 765 : Worked case — scalable oversight: "Would unsupervised elicitation still work on questions … — renvoi.
- `volet3` — FR l. 923 : 2. Évaluer l’alignement · EN l. 1045 : 2. Evaluating alignment — renvoi.
- `volets4_5_entete` — FR l. 1119 : Sleeper Agents (Anthropic, Hubinger et al.) · EN l. 1261 : Sleeper Agents (Anthropic, Hubinger et al.) — renvoi.
- `volets4_5_entete` — FR l. 1185 : Auditing Hidden Objectives (Anthropic, Marks et al.) · EN l. 1325 : Auditing Hidden Objectives (Anthropic, Marks et al.) — renvoi.
- `volets4_5_entete` — FR l. 1287 : Sujet 5 — Construire un model organism (MOYEN) · EN l. 1466 : Topic 5 — Building a model organism (MEDIUM) — renvoi.
- `volets4_5_entete` — FR l. 1295 : Sujet 9 — Alignment auditing (MOYEN) · EN l. 1474 : Topic 9 — Alignment auditing (MEDIUM) — renvoi.
- `volet6` — FR l. 1578 : 8 · La validité des sondes d'activation hors distribution — pourquoi « validée par interve… · EN l. 1746 : 8 · Out-of-distribution validity of activation probes — why "validated by causal intervent… — renvoi.
- `volet7_B_et_D` — FR l. 1928 : F·32 · Subliminal Learning — Cloud, Le (Fellows), Chua, Betley, Sztyber-Betley, Hilton, Ma… · EN l. 2093 : F·32 · Subliminal Learning — Cloud, Le (Fellows), Chua, Betley, Sztyber-Betley, Hilton, Ma… — renvoi.
- `volet7_B_et_D` — FR l. 1961 : F·38 · Agentic Misalignment — Lynch (Fellows, 1re cohorte), Larson (MATS), Perez, Hubinger… · EN l. 2126 : F·38 · Agentic Misalignment — Lynch (Fellows, 1st cohort), Larson (MATS), Perez, Hubinger,… — renvoi.
- `volet7_B_et_D` — FR l. 1988 : F·27 · AuditBench — Sheshadri, Ewart, Fronsdal, Gupta ; Marks, Bowman, Wang, Price ; mars … · EN l. 2153 : F·27 · AuditBench — Sheshadri, Ewart, Fronsdal, Gupta; Marks, Bowman, Wang, Price; March 2… — renvoi.
- `volet7_A_et_C` — FR l. 2072 : F·1 · Sleeper Agents (Hubinger et al., Anthropic, 2024) — [P·2] · EN l. 2206 : F·1 · Sleeper Agents (Hubinger et al., Anthropic, 2024) — [P·2] — renvoi.
- `volet7_A_et_C` — FR l. 2376 : F·13 · Auditing Language Models for Hidden Objectives (Marks et al., Anthropic, 2025) — [P… · EN l. 2510 : F·13 · Auditing Language Models for Hidden Objectives (Marks et al., Anthropic, 2025) — [P… — renvoi.
- `volet11_1_a_20` — FR l. 3775 : 6 · « How would you detect misalignment in a model you can't fully trust? » *(question rée… · EN l. 4024 : 6 · « How would you detect misalignment in a model you can't fully trust? » *(question rée… — renvoi.
- `volet11_21_a_52` — FR l. 4129 : 21 · « A probe trained on synthetic examples of a bad behaviour must catch the real thing.… · EN l. 4404 : 21 · « A probe trained on synthetic examples of a bad behaviour must catch the real thing.… — renvoi.
- `volet11_21_a_52` — FR l. 4235 : 27 · « When an autonomous agent's goals are blocked, will it act against its operator — an… · EN l. 4517 : 27 · « When an autonomous agent's goals are blocked, will it act against its operator — an… — renvoi.
- `volet11_21_a_52` — FR l. 4255 : 28 · « We saw a model comply during training while intending to behave differently in depl… · EN l. 4538 : 28 · « We saw a model comply during training while intending to behave differently in depl… — renvoi.
- `volet11_21_a_52` — FR l. 4545 : 42 · « When a model reward-hacks, what is actually being learned — and how would you find … · EN l. 4848 : 42 · « When a model reward-hacks, what is actually being learned — and how would you find … — renvoi.
- `volet11_21_a_52` — FR l. 4657 : 48 · « Training a model on one narrow bad behaviour sometimes produces a model that is bro… · EN l. 4961 : 48 · « Training a model on one narrow bad behaviour sometimes produces a model that is bro… — renvoi.
- `volet11_53_et_fin` — FR l. 4776 : 56 · « How would you know a model is faking alignment? » (I.4) · EN l. 5087 : 56 · « How would you know a model is faking alignment? » (I.4) — renvoi.
- `volet7_A_et_C` — avertissement ponctuel prêt, après FR l. 2080 / EN l. 2214 (texte dans la partie « Par tranche »).

**Où il revient** (relevé automatique, motifs FR `organisme` / EN `organism` ; sections, avec le nombre de lignes touchées) :

- `tete_volet1` — FR : l. 80 4. L’obstacle épistémique central : pourquoi on … (1) ; l. 132 Q4. « Comment saurais-tu qu’un modèle “fait semb… (1)
  — EN : l. 131 3. Two families of risk never to be confused: mi… (1) ; l. 190 Q4. "How would you know that a model is “pretend… (1)
- `volet_M` — FR : l. 257 M4 · Le contrôle : ce qu'il écarte, et il doit s… (1) ; l. 298 M5 · Le nul et le cas connu (2)
  — EN : l. 286 M2 · The bet: on the model, never on the method (1) ; l. 324 M4 · The control: what it rules out, and it must… (1) ; l. 365 M5 · The null and the known case (2) ; l. 456 M10 · The checklist, to reread before each rehea… (1)
- `volet2_A_a_D` — FR : l. 422 Préambule — les quatre « grammaires d’attaque » (2) ; l. 434 A. Testbeds & model organisms — fabriquer le phé… (3) ; l. 442 Cas d'application — organismes modèles et bancs … (2) ; l. 488 Cas d'application — évaluations, capacité contre… (3)
  — EN : l. 506 Preamble — the four "attack grammars" (1) ; l. 519 A. Testbeds & model organisms — manufacturing th… (4) ; l. 528 Worked case — model organisms and testbeds: "How… (2) ; l. 575 Worked case — evaluations, capacity versus prope… (4)
- `volet3` — FR : l. 1077 PARTIE III — LES TRAVAUX DU MOMENT (2025-2026) (2)
  — EN : l. 1180 SECTION II — THE TEAMS: who does what at (1) ; l. 1202 SECTION III — CURRENT WORK (2025-2026) (2) ; l. 1228 SECTION IV — SYNTHESIS: how everything fits toge… (1)
- `volets4_5_entete` — FR : l. 1185 Auditing Hidden Objectives (Anthropic, Marks et … (1) ; l. 1251 A. Tes sujets FORT — ta thèse peut être la colon… (1)
  — EN : l. 1254 The key papers, told one by one (2) ; l. 1428 A. Your STRONG topics — your thesis can be the b… (1) ; l. 1463 B. Their topics — method toolkit, light or zero … (2)
- `volet6` — FR : l. 1578 8 · La validité des sondes d'activation hors dis… (5)
  — EN : l. 1746 8 · Out-of-distribution validity of activation p… (6)
- `volet7_B_et_D` — FR : l. 1777 F·29 · Fine-Tuned Lie Detectors Failed to Genera… (1) ; l. 2032 F·26 · Removing Sandbagging in LLMs by Training … (1)
  — EN : l. 1942 F·29 · Fine-Tuned Lie Detectors Failed to Genera… (1) ; l. 2186 F·26 · Removing Sandbagging in LLMs by Training … (1)
- `volet7_A_et_C` — FR : l. 2072 F·1 · Sleeper Agents (Hubinger et al., Anthropic… (1) ; l. 2098 F·2 · Alignment Faking in Large Language Models … (1) ; l. 2376 F·13 · Auditing Language Models for Hidden Objec… (2)
  — EN : l. 2206 F·1 · Sleeper Agents (Hubinger et al., Anthropic… (2) ; l. 2232 F·2 · Alignment Faking in Large Language Models … (1) ; l. 2510 F·13 · Auditing Language Models for Hidden Objec… (2)
- `volets8_9` — FR : l. 2798 6 · AI control — « Can we ensure safety by deplo… (1)
  — EN : l. 2955 6 · AI control — "Can we ensure safety by deploy… (1)
- `volet11_1_a_20` — FR : l. 3775 6 · « How would you detect misalignment in a mod… (5) ; l. 3854 9 · « What would you work on here, and why? » (1) ; l. 4001 12 · « Why Anthropic? » (1) ; l. 4102 20 · « Suppose you must deploy a capable model y… (2)
  — EN : l. 4024 6 · « How would you detect misalignment in a mod… (5) ; l. 4104 9 · « What would you work on here, and why? » (1) ; l. 4252 12 · « Why Anthropic? » (1) ; l. 4377 20 · « Suppose you must deploy a capable model y… (2)
- `volet11_21_a_52` — FR : l. 4129 21 · « A probe trained on synthetic examples of … (2) ; l. 4187 24 · « Probes drift toward "I am being evaluated… (3) ; l. 4255 28 · « We saw a model comply during training whi… (2) ; l. 4408 35 · « Can we build a lie detector for language … (1) ; l. 4585 44 · « How would you tell whether a model is san… (1)
  — EN : l. 4404 21 · « A probe trained on synthetic examples of … (2) ; l. 4463 24 · « Probes drift toward "I am being evaluated… (3) ; l. 4538 28 · « We saw a model comply during training whi… (2) ; l. 4699 35 · « Can we build a lie detector for language … (1) ; l. 4888 44 · « How would you tell whether a model is san… (1)
- `volet11_53_et_fin` — FR : l. 4776 56 · « How would you know a model is faking alig… (2) ; l. 4923 A2 · « You have $15,000 of compute a month and f… (2) ; l. 4938 A3 · « What if the probes just don't work at all… (1) ; l. 5003 A8 · « How do you think about the dual-use of yo… (1) ; l. 5016 A9 à A17 · Neuf questions moins probables, en ré… (1)
  — EN : l. 5087 56 · « How would you know a model is faking alig… (2) ; l. 5239 A2 · « You have $15,000 of compute a month and f… (2) ; l. 5255 A3 · « What if the probes just don't work at all… (1) ; l. 5327 A8 · « How do you think about the dual-use of yo… (1) ; l. 5341 A9 à A17 · Neuf questions moins probables, en ré… (2)

---

## 6. Évaluations comportementales et pots de miel — *Behavioural evaluations and honeypots*

- **Maison** : tranche `volet2_A_a_D` ; FR : volet 2, §B · évaluations (après « En pratique — le sandbagging ») ; EN : Part 2, §B · evaluations (after "In practice — sandbagging").
- **Limites** : 7 ; **parades** : 6.
- **Ancre FR** (ligne 486 de la v3.5 FR ; l'encadré s'insère juste après) :

~~~text
En pratique — le sandbagging (system cards). Côté risque des évaluations elles-mêmes, on veut savoir si un modèle sous-performe stratégiquement quand il se sait évalué (sandbagging). Le design est une éval de propension à la sous-performance : on compare la performance du modèle sur une tâche selon qu’il croit être testé ou non, et l’on regarde si l’écart trahit une retenue volontaire. C’est un cas où l’éval doit se méfier d’elle-même — d’où l’importance de l’élicitation sérieuse et du réalisme de la mise en situation.
~~~

- **Ancre EN** (ligne 573 de la v3.5 EN) :

~~~text
In practice — sandbagging (system cards). On the side of risk to the evaluations themselves, we want to know whether a model strategically underperforms when it knows it is being evaluated (sandbagging). The design is a propensity eval for underperformance: we compare the model's performance on a task depending on whether it believes it is being tested or not, and look at whether the gap betrays deliberate holding back. This is a case where the eval must be wary of itself — hence the importance of serious elicitation and of the realism of the scenario.
~~~

**Encadré complet, français :**

~~~markdown
> **⚠ Limites et parades — Évaluations comportementales et pots de miel** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Le modèle peut remarquer le test et se retenir : la triche discrète passe de 4,0 % à 18,9 % quand on dit qu'un classifieur lira le transcript. *(source : fiche 13 ; cours, volet 2, §B)*
>   **Parade :** Deux versions d'un environnement, tirées au hasard, qui ne diffèrent que par des indices de réalisme notés par un discriminateur, et un organisme dressé à se cacher comme cas connu. *(source : cours, volet 2, §B, K63)*
> - **Limite :** La conscience verbalisée mesure mal le réalisme : elle rate la conscience non verbalisée. *(source : cours, volet 7, F·25)*
>   **Parade :** Le taux auquel un juge, devant la paire, prend l'audit pour le réel, et de vraies ressources de déploiement pour l'auditeur. *(source : cours, volet 7, F·25)*
> - **Limite :** Sous-éliciter fait paraître le modèle plus sûr, et un petit fine-tuning peut créer la capacité qu'on croit éliciter. *(source : cours, volet 2, §B ; cours, volet 2, §B, K63)*
>   **Parade :** Une élicitation à budget fixé d'avance, rapportée comme une borne ; un gain ne compte qu'au-delà du même budget sur un modèle qui n'a pas la capacité. *(source : cours, volet M, M7 ; cours, volet 2, §B, K63)*
> - **Limite :** Le score global peut tromper : le désalignement est « high-dimensional », et un audit global qui passe de 4,34 à 4,20 rate des hausses ciblées. *(source : fiche 13)*
>   **Parade :** Lire les dimensions une à une, pas seulement le score global. *(source : fiche 13)*
> - **Limite :** Entraîner sur l'évaluation corrige « narrowly … the symptom ». *(source : fiche 12)*
>   **Parade :** Des métriques d'audit tenues à part, jamais entraînées. *(source : fiche 12)*
> - **Limite :** Dans une simulation, « c'est faux » est vrai : un pot de miel ne sépare pas un modèle qui le lit comme factice d'un modèle qui se retient. *(source : fiche 3)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** Le non-refus n'est pas le préjudice. *(source : cours, volet 2, §B et §H)*
>   **Parade :** Le préjudice différentiel, noté à l'aveugle, avec un bras de référence réaliste. *(source : cours, volet 2, §H, G1 ; cours, volet M, M4)*
~~~

**Encadré complet, anglais :**

~~~markdown
> **⚠ Limits and workarounds — Behavioural evaluations and honeypots** *(v3.6, 2 October 2026)*
>
> - **Limit:** The model can notice the test and hold back: discreet hacking goes from 4.0% to 18.9% when it is told a classifier will read the transcript. *(source: reading sheet 13; course, Part 2, §B)*
>   **Workaround:** Two versions of an environment, randomly assigned, differing only in realism cues scored by a discriminator, and an organism trained to hide as the known case. *(source: course, Part 2, §B, K63)*
> - **Limit:** Verbalized awareness measures realism poorly: it misses unverbalized awareness. *(source: course, Part 7, F·25)*
>   **Workaround:** The rate at which a judge, shown the pair, mistakes the audit for the real thing, and real deployment resources for the auditor. *(source: course, Part 7, F·25)*
> - **Limit:** Under-eliciting makes the model look safer, and a small fine-tune can create the capability you think you are eliciting. *(source: course, Part 2, §B; course, Part 2, §B, K63)*
>   **Workaround:** Elicitation at a budget fixed in advance, reported as a bound; a gain counts only beyond the same budget on a model without the capability. *(source: course, Part M, M7; course, Part 2, §B, K63)*
> - **Limit:** The global score can mislead: misalignment is "high-dimensional", and a global audit moving from 4.34 to 4.20 misses targeted increases. *(source: reading sheet 13)*
>   **Workaround:** Read the dimensions one by one, not just the global score. *(source: reading sheet 13)*
> - **Limit:** Training on the evaluation fixes "narrowly … the symptom". *(source: reading sheet 12)*
>   **Workaround:** Held-out audit metrics, never trained on. *(source: reading sheet 12)*
> - **Limit:** In a simulation, "this is fake" is true: a honeypot does not separate a model that reads it as fake from a model that holds back. *(source: reading sheet 3)*
>   **Workaround:** none known; say so.
> - **Limit:** Non-refusal is not harm. *(source: course, Part 2, §B and §H)*
>   **Workaround:** Differential harm, blind-scored, with a realistic reference arm. *(source: course, Part 2, §H, G1; course, Part M, M4)*
~~~

**Renvoi d'une ligne :**

~~~markdown
> ⚠ **Limites et parades** : évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») *(v3.6)*
> ⚠ **Limits and workarounds**: behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging") *(v3.6)*
~~~

**Où un renvoi ou un avertissement ponctuel est conseillé :**

- `tete_volet1` — FR l. 132 : Q4. « Comment saurais-tu qu’un modèle “fait semblant” d’être aligné ? » · EN l. 190 : Q4. "How would you know that a model is “pretending” to be aligned?" — renvoi.
- `volet3` — FR l. 923 : 2. Évaluer l’alignement · EN l. 1045 : 2. Evaluating alignment — renvoi.
- `volet7_B_et_D` — FR l. 1753 : F·25 · Measuring and improving coding audit realism with deployment resources — Kissane (F… · EN l. 1918 : F·25 · Measuring and improving coding audit realism with deployment resources — Kissane (F… — renvoi.
- `volet7_B_et_D` — FR l. 1843 : F·34 · Model Spec Midtraining — Li, Wichers (Fellows), Price, Marks, Kutasov ; 5 mai 2026 … · EN l. 2008 : F·34 · Model Spec Midtraining — Li, Wichers (Fellows), Price, Marks, Kutasov; 5 May 2026; … — renvoi.
- `volet7_B_et_D` — FR l. 1961 : F·38 · Agentic Misalignment — Lynch (Fellows, 1re cohorte), Larson (MATS), Perez, Hubinger… · EN l. 2126 : F·38 · Agentic Misalignment — Lynch (Fellows, 1st cohort), Larson (MATS), Perez, Hubinger,… — renvoi.
- `volet7_B_et_D` — FR l. 2032 : F·26 · Removing Sandbagging in LLMs by Training with Weak Supervision — Ryd (Fellows), Bar… · EN l. 2186 : F·26 · Removing Sandbagging in LLMs by Training with Weak Supervision — Ryd (Fellows), Bar… — renvoi.
- `volet7_A_et_C` — FR l. 2098 : F·2 · Alignment Faking in Large Language Models (Greenblatt et al., Anthropic, 2024) — [P·… · EN l. 2232 : F·2 · Alignment Faking in Large Language Models (Greenblatt et al., Anthropic, 2024) — [P·… — renvoi.
- `volet7_A_et_C` — FR l. 2124 : F·3 · Towards Understanding Sycophancy in Language Models (Sharma et al., Anthropic, 2023)… · EN l. 2258 : F·3 · Towards Understanding Sycophancy in Language Models (Sharma et al., Anthropic, 2023)… — renvoi.
- `volet7_A_et_C` — FR l. 2629 : F·57 · Towards evaluations-based safety cases for AI scheming (Balesni, Apollo ; Evans, Sh… · EN l. 2761 : F·57 · Towards evaluations-based safety cases for AI scheming (Balesni, Apollo; Evans, Shl… — renvoi.
- `volet10` — FR l. 3071 : AI Sandbagging: Language Models can Strategically Underperform on Evaluations — Teun van d… · EN l. 3313 : AI Sandbagging: Language Models can Strategically Underperform on Evaluations — Teun van d… — renvoi.
- `volet10` — FR l. 3086 : Me, Myself, and AI: The Situational Awareness Dataset (SAD) for LLMs — Rudolf Laine, Bilal… · EN l. 3328 : Me, Myself, and AI: The Situational Awareness Dataset (SAD) for LLMs — Rudolf Laine, Bilal… — renvoi.
- `volet10` — FR l. 3565 : Adversarial robustness › Realistic and differential benchmarks for jailbreaks · EN l. 3802 : Adversarial robustness › Realistic and differential benchmarks for jailbreaks — renvoi.
- `volet11_1_a_20` — FR l. 3829 : 8 · « How would you train models to be more robustly aligned with intended objectives? » *… · EN l. 4077 : 8 · « How would you train models to be more robustly aligned with intended objectives? » *… — renvoi.
- `volet11_1_a_20` — FR l. 4079 : 19 · « A model behaves differently when it believes it is being tested. What do you do wit… · EN l. 4350 : 19 · « A model behaves differently when it believes it is being tested. What do you do wit… — renvoi.
- `volet11_21_a_52` — FR l. 4235 : 27 · « When an autonomous agent's goals are blocked, will it act against its operator — an… · EN l. 4517 : 27 · « When an autonomous agent's goals are blocked, will it act against its operator — an… — renvoi.
- `volet11_21_a_52` — FR l. 4255 : 28 · « We saw a model comply during training while intending to behave differently in depl… · EN l. 4538 : 28 · « We saw a model comply during training while intending to behave differently in depl… — renvoi.
- `volet11_21_a_52` — FR l. 4545 : 42 · « When a model reward-hacks, what is actually being learned — and how would you find … · EN l. 4848 : 42 · « When a model reward-hacks, what is actually being learned — and how would you find … — renvoi.
- `volet11_21_a_52` — FR l. 4585 : 44 · « How would you tell whether a model is sandbagging an evaluation? » (II.8) · EN l. 4888 : 44 · « How would you tell whether a model is sandbagging an evaluation? » (II.8) — renvoi.
- `volet11_53_et_fin` — FR l. 4776 : 56 · « How would you know a model is faking alignment? » (I.4) · EN l. 5087 : 56 · « How would you know a model is faking alignment? » (I.4) — renvoi.
- `volet11_53_et_fin` — FR l. 4793 : 58 · « RLHF, DPO, Constitutional AI — what do they do and what don't they solve? » (I.6) · EN l. 5105 : 58 · « RLHF, DPO, Constitutional AI — what do they do and what don't they solve? » (I.6) — renvoi.
- `volet11_53_et_fin` — FR l. 5096 : B2 · « How would you design an evaluation a model cannot tell is an evaluation? » · EN l. 5421 : B2 · « How would you design an evaluation a model cannot tell is an evaluation? » — renvoi.
- `volet11_53_et_fin` — FR l. 5246 : B9 · « How would you build a safety case that a model cannot sandbag your dangerous-capabi… · EN l. 5571 : B9 · « How would you build a safety case that a model cannot sandbag your dangerous-capabi… — renvoi.

**Où il revient** (relevé automatique, motifs FR `honeypot|pot de miel|sandbag|propension|élicitation|audit automatique|Petri` / EN `honeypot|sandbag|propensity|elicitation|automated audit|Petri` ; sections, avec le nombre de lignes touchées) :

- `tete_volet1` — FR : l. 108 6. La carte du territoire (l’aperçu, avant le dé… (1) ; l. 148 Q7. « Qu’est-ce que la Responsible Scaling Polic… (1)
  — EN : l. 209 Q7. "What is the Responsible Scaling Policy, and… (1)
- `volet_M` — FR : l. 330 M7 · La plus petite version, le budget, et la cl… (1)
  — EN : l. 397 M7 · The smallest version, the budget, and the c… (1) ; l. 456 M10 · The checklist, to reread before each rehea… (1)
- `volet2_A_a_D` — FR : l. 480 B. Évaluations — mesurer une capacité ou une pro… (4) ; l. 488 Cas d'application — évaluations, capacité contre… (3)
  — EN : l. 566 B. Evaluations — measuring a capability or a pro… (4) ; l. 575 Worked case — evaluations, capacity versus prope… (4)
- `volet2_E_a_I` — FR : l. 675 Cas d'application — la supervision évolutive : «… (4) ; l. 834 I. Interventions d’entraînement & unlearning — c… (2) ; l. 842 Cas d'application — interventions d'entraînement… (1)
  — EN : l. 765 Worked case — scalable oversight: "Would unsuper… (7) ; l. 927 I. Training interventions & unlearning — changin… (2) ; l. 936 Worked case — training interventions and unlearn… (1)
- `volet3` — FR : l. 899 1. Évaluer les capacités (3) ; l. 923 2. Évaluer l’alignement (1) ; l. 1029 6. Le domaine « divers » : désapprentissage et g… (1) ; l. 1053 PARTIE II — LES ÉQUIPES : qui fait quoi chez (1) ; l. 1077 PARTIE III — LES TRAVAUX DU MOMENT (2025-2026) (3)
  — EN : l. 1020 1. Evaluating capabilities (4) ; l. 1045 2. Evaluating alignment (1) ; l. 1155 6. The "miscellaneous" domain: unlearning and mu… (1) ; l. 1202 SECTION III — CURRENT WORK (2025-2026) (3)
- `volets4_5_entete` — FR : l. 1123 Alignment Faking (Anthropic, Greenblatt et al.) (1) ; l. 1127 Sycophancy (Anthropic, Sharma et al.) (1) ; l. 1203 L’unlearning mis à l’épreuve (Deeb et Roger) (1) ; l. 1251 A. Tes sujets FORT — ta thèse peut être la colon… (1) ; l. 1285 B. Leurs sujets — méthodothèque, dosage léger ou… (3) ; l. 1326 Les papiers — quatre niveaux (1)
  — EN : l. 1254 The key papers, told one by one (3) ; l. 1428 A. Your STRONG topics — your thesis can be the b… (1) ; l. 1463 B. Their topics — method toolkit, light or zero … (3) ; l. 1506 The papers — four levels (2)
- `volet6` — FR : l. 1458 4. La page « Recommended Directions » et ses sei… (2) ; l. 1474 5. Les travaux du programme Fellows, 2025-2026 —… (1)
  — EN : l. 1597 4. The "Recommended Directions" page and its six… (2) ; l. 1603 5. The work of the Fellows program, 2025-2026 — … (1) ; l. 1676 7. What these supplements change in Parts 1 to 5 (2) ; l. 1746 8 · Out-of-distribution validity of activation p… (1)
- `volet7_B_et_D` — FR : l. 1635 F·22 · Diffuse AI Control on Fuzzy Tasks — Terek… (2) ; l. 1753 F·25 · Measuring and improving coding audit real… (2) ; l. 1777 F·29 · Fine-Tuned Lie Detectors Failed to Genera… (1) ; l. 2012 F·40 · Automated Weak-to-Strong Researcher — Wen… (1) ; l. 2032 F·26 · Removing Sandbagging in LLMs by Training … (2) ; l. 2051 F·60 · Automated Researchers Can Subtly Sandbag … (4)
  — EN : l. 1800 F·22 · Diffuse AI Control on Fuzzy Tasks — Terek… (2) ; l. 1918 F·25 · Measuring and improving coding audit real… (2) ; l. 1942 F·29 · Fine-Tuned Lie Detectors Failed to Genera… (3) ; l. 2177 F·40 · Automated Weak-to-Strong Researcher — Wen… (1) ; l. 2186 F·26 · Removing Sandbagging in LLMs by Training … (2) ; l. 2194 F·60 · Automated Researchers Can Subtly Sandbag … (2)
- `volet7_A_et_C` — FR : l. 2098 F·2 · Alignment Faking in Large Language Models … (1) ; l. 2124 F·3 · Towards Understanding Sycophancy in Langua… (2) ; l. 2352 F·12 · Weak-to-Strong Generalization (Burns et a… (1) ; l. 2376 F·13 · Auditing Language Models for Hidden Objec… (1) ; l. 2472 F·17 · L'unlearning mis à l'épreuve (Deeb et Rog… (1) ; l. 2646 F·58 · Recommendations for Technical AI Safety R… (1)
  — EN : l. 2232 F·2 · Alignment Faking in Large Language Models … (1) ; l. 2258 F·3 · Towards Understanding Sycophancy in Langua… (2) ; l. 2486 F·12 · Weak-to-Strong Generalization (Burns et a… (1) ; l. 2510 F·13 · Auditing Language Models for Hidden Objec… (1) ; l. 2606 F·17 · L'unlearning mis à l'épreuve (Deeb and Ro… (1) ; l. 2778 F·58 · Recommendations for Technical AI Safety R… (1)
- `volets8_9` — FR : l. 2666 VOLET 8 — Références, dans l'ordre des fiches (1) ; l. 2751 2 · Evaluating alignment — « How do we measure h… (3) ; l. 2912 9 · Miscellaneous (1) ; l. 2928 10 · La lecture d'ensemble, en trois phrases pou… (1)
  — EN : l. 2804 PART 8 — References, in the order of the sheets (1) ; l. 2908 2 · Evaluating alignment — "How do we measure ho… (2) ; l. 3069 9 · Miscellaneous (1) ; l. 3085 10 · The overall reading, in three sentences for… (3)
- `volet10` — FR : l. 2980 Dans les fiches (14) (1) ; l. 3071 AI Sandbagging: Language Models can Strategicall… (4) ; l. 3128 Looking Inward: Language Models Can Learn About … (1) ; l. 3511 Steering Llama 2 via Contrastive Activation Addi… (1) ; l. 3643 Do Unlearning Methods Remove Information from La… (1)
  — EN : l. 3223 In the sheets (14) (2) ; l. 3313 AI Sandbagging: Language Models can Strategicall… (4) ; l. 3370 Looking Inward: Language Models Can Learn About … (1) ; l. 3705 Balancing Label Quantity and Quality for Scalabl… (1) ; l. 3749 Steering Llama 2 via Contrastive Activation Addi… (1) ; l. 3879 Do Unlearning Methods Remove Information from La… (1)
- `volet11_1_a_20` — FR : l. 3878 10 · « Diffuse Control already frames this as a … (1) ; l. 4001 12 · « Why Anthropic? » (1)
  — EN : l. 4128 10 · « Diffuse Control already frames this as a … (1) ; l. 4252 12 · « Why Anthropic? » (1)
- `volet11_21_a_52` — FR : l. 4386 34 · « Can automated researchers do alignment re… (2) ; l. 4408 35 · « Can we build a lie detector for language … (1) ; l. 4451 37 · « How strong does a red team have to be, an… (1) ; l. 4585 44 · « How would you tell whether a model is san… (5) ; l. 4643 47 · « You have one experiment and a month. What… (1) ; l. 4676 49 · « Training a strong model on labels from a … (1)
  — EN : l. 4676 34 · « Can automated researchers do alignment re… (1) ; l. 4699 35 · « Can we build a lie detector for language … (1) ; l. 4745 37 · « How strong does a red team have to be, an… (1) ; l. 4888 44 · « How would you tell whether a model is san… (5) ; l. 4981 49 · « Training a strong model on labels from a … (1)
- `volet11_53_et_fin` — FR : l. 4822 60 · « Defense in depth — which techniques, and … (1) ; l. 4862 63 · Tes huit positions, dites en entier (VII) —… (1) ; l. 4964 A5 · « Isn't sycophancy basically solved by now … (1) ; l. 5016 A9 à A17 · Neuf questions moins probables, en ré… (1) ; l. 5117 B3 · « What should be delegated to automated res… (2) ; l. 5223 B8 · « Build a suite of models with the same cap… (5) ; l. 5246 B9 · « How would you build a safety case that a … (10) ; l. 5269 B10 · « Untrusted monitoring: the monitor is ano… (2) ; l. 5336 B13 · « Can honesty be trained rather than detec… (1)
  — EN : l. 5284 A5 · « Isn't sycophancy basically solved by now … (1) ; l. 5421 B2 · « How would you design an evaluation a mode… (1) ; l. 5442 B3 · « What should be delegated to automated res… (2) ; l. 5548 B8 · « Build a suite of models with the same cap… (4) ; l. 5571 B9 · « How would you build a safety case that a … (10) ; l. 5594 B10 · « Untrusted monitoring: the monitor is ano… (2) ; l. 5661 B13 · « Can honesty be trained rather than detec… (1)

---

## 7. Sondes d'activation — *Activation probes*

- **Maison** : tranche `volet2_A_a_D` ; FR : volet 2, §C · méthodes sur activations (après « En pratique — The Geometry of Truth ») ; EN : Part 2, §C · methods on activations (after "In practice — The Geometry of Truth").
- **Limites** : 10 ; **parades** : 9.
- **Ancre FR** (ligne 519 de la v3.5 FR ; l'encadré s'insère juste après) :

~~~text
En pratique — The Geometry of Truth (Marks & Tegmark). Les auteurs voulaient savoir si un modèle représente linéairement la vérité ou la fausseté d’un énoncé — autrement dit, s’il existe une « direction de vérité » dans ses activations. Le probing répond directement : ils ont collecté les activations du modèle sur des énoncés vrais et faux, et cherché la direction qui sépare le mieux les deux. Mais ils ne se sont pas arrêtés à la corrélation : ils ont montré que cette direction généralise à de nouveaux énoncés et qu’elle compte causalement — intervenir le long d’elle modifie le comportement du modèle, comme si on basculait sa « croyance ». C’est l’illustration canonique du couple lire/agir, et c’est précisément la lignée de tes travaux.
~~~

- **Ancre EN** (ligne 607 de la v3.5 EN) :

~~~text
In practice — The Geometry of Truth (Marks & Tegmark). The authors wanted to know whether a model represents the truth or falsity of a statement linearly — in other words, whether there exists a "truth direction" in its activations. Probing answers directly: they collected the model's activations on true and false statements, and looked for the direction that best separates the two. But they did not stop at correlation: they showed that this direction generalizes to new statements and that it matters causally — intervening along it modifies the model's behavior, as if its "belief" were being flipped. This is the canonical illustration of the read/act pair, and it is precisely the lineage of your work.
~~~

**Encadré complet, français :**

~~~markdown
> **⚠ Limites et parades — Sondes d'activation** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Une sonde trouve des corrélations : lire n'est pas utiliser — la direction que lit ta sonde fait moins de 1 % du travail causal, l'état complet aux mêmes sites 68 %. *(source : fiche 5 ; cours, volet 6, §2)*
>   **Parade :** La corrélation suffit pour signaler ; pour croire une absence ou intervenir, le test causal : piloter le long de la direction contre des directions aléatoires de même norme (nul de spécificité), puis contre des témoins à dégradation appariée (dommage). *(source : cours, volet M, M8 ; passation, §5.2)*
> - **Limite :** Une AUROC en distribution ne prouve rien ; c'est l'écart avec l'AUROC sur des types tenus à part qui se mesure. *(source : fiches, partie B, piège 1 ; fiche 7)*
>   **Parade :** Tenir à part des familles entières, jamais des paraphrases, et des formats, d'un tour à l'agentique à plusieurs tours. *(source : explication du 2 octobre, §3 ; programme, partie 3)*
> - **Limite :** La sonde peut apprendre la façon dont on a fabriqué l'organisme, ou lire « je suis surveillé » et le contexte de test au lieu de l'intention. *(source : cours, volet 6, §8 ; cours, volet 3, §4, K67)*
>   **Parade :** Deux fabrications du même comportement (instruction cachée, fine-tuning léger), un organisme conscient mais honnête, et des transcripts honnêtes rédigés comme des tests. *(source : cours, volet 6, §8 ; cours, volet 3, §4, K67)*
> - **Limite :** Elle peut lire le texte écrit plutôt qu'une représentation. *(source : programme, partie 8)*
>   **Parade :** Lire au premier jeton de la réponse, avant toute raison écrite, ou au jeton d'action avec des raisons neutres de même longueur préremplies. *(source : programme, parties 3 et 8)*
> - **Limite :** Après un entraînement, une sonde calibrée ailleurs lit autrement : après RL, des sondes neuves hors domaine se dégradent, alors qu'une sonde neuve dans le domaine reste quasi parfaite. *(source : rapport d'antériorité 3 du 2 octobre, The Obfuscation Atlas — rapport ; passation, §5.2)*
>   **Parade :** Une sonde par bras d'entraînement et une sonde neuve après l'entraînement, sur un jeu d'indices disjoint ; les sondes restent une mesure séparée, jamais dans l'étiquette principale. *(source : passation, §5.2 ; programme, parties 3 et 8)*
> - **Limite :** Une sonde « évaluation contre déploiement » garderait son score global sous RL mais basculerait sur les cas limites, et la réentraîner ne récupère presque rien. *(source : rapport d'antériorité 4 du 2 octobre — rapport, résumé seul, à vérifier)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** Sur l'honnêteté, les sondes de vérité ont fait moins bien qu'un simple prompt ; au seuil d'un moniteur, des sondes rappellent 43 % à 1 % de faux positifs, contre 55 % pour le meilleur moniteur LLM. *(source : cours, volet 7, F·62 ; cours, volet 7, F·51)*
>   **Parade :** Battre une baseline boîte noire ou un prompt à coût égal, rapporter le rappel à 1 % de faux positifs, et publier le résultat si la sonde ne bat pas le prompt. *(source : cours, volet 5, sujet 1 ; cours, volet 7, F·50 ; cours, volet 7, F·29)*
> - **Limite :** Des métriques d'ajustement se lisent comme une généralisation : les métriques de sonde de ton dépôt étaient d'ajustement, et le ρ de 0,684 peut l'être aussi. *(source : README du dépôt)*
>   **Parade :** Scorer des items exclus de l'entraînement de la sonde, et extraire sur un jeu disjoint. *(source : README du dépôt)*
> - **Limite :** Des paires contrastives peuvent porter un style, et des négatifs synthétiques n'apprendre qu'un indice de surface. *(source : cours, volet M, M4 ; cours, volet 2, §C)*
>   **Parade :** Un classifieur de la seule surface doit rester au hasard entre les côtés des paires ; tirer les négatifs des générations réelles du modèle. *(source : cours, volet M, M4 ; cours, volet 2, §C)*
> - **Limite :** Un silence de sonde ne départage pas « pas d'intention » et « sonde aveugle ». *(source : passation, §5.2 ; fiches, partie B, piège 3)*
>   **Parade :** Un organisme où l'on a installé l'intention soi-même : on y mesure sensibilité et fausses alarmes, et le silence ailleurs devient une borne. *(source : passation, §5.2)*
~~~

**Encadré complet, anglais :**

~~~markdown
> **⚠ Limits and workarounds — Activation probes** *(v3.6, 2 October 2026)*
>
> - **Limit:** A probe finds correlations: reading is not using — the direction your probe reads does under 1% of the causal work, the full state at the same sites 68%. *(source: reading sheet 5; course, Part 6, §2)*
>   **Workaround:** Correlation is enough to flag; to trust an absence or to intervene, the causal test: steer along the direction against matched-norm random directions (specificity null), then against controls at matched degradation (damage). *(source: course, Part M, M8; handover, §5.2)*
> - **Limit:** An in-distribution AUROC proves nothing; what you measure is the gap with the AUROC on held-out types. *(source: reading sheets, part B, trap 1; reading sheet 7)*
>   **Workaround:** Hold out whole families, never paraphrases, and formats, from single-turn to multi-turn agentic. *(source: explanation of 2 October, §3; programme, part 3)*
> - **Limit:** The probe can learn how the organism was made, or read "I am being watched" and the test context instead of the intention. *(source: course, Part 6, §8; course, Part 3, §4, K67)*
>   **Workaround:** Two manufactures of the same behaviour (hidden instruction, light fine-tuning), an aware-but-honest organism, and honest transcripts written as tests. *(source: course, Part 6, §8; course, Part 3, §4, K67)*
> - **Limit:** It may read the written text rather than a representation. *(source: programme, part 8)*
>   **Workaround:** Read at the first token of the answer, before any written reason, or at the action token with neutral reasons of the same length prefilled. *(source: programme, parts 3 and 8)*
> - **Limit:** After training, a probe calibrated elsewhere reads differently: after RL, fresh out-of-domain probes degrade, while a fresh in-domain probe stays near perfect. *(source: prior-art report 3 of 2 October, The Obfuscation Atlas — report; handover, §5.2)*
>   **Workaround:** One probe per training arm and a fresh probe after training, on a disjoint cue set; probes stay a separate measure, never in the main label. *(source: handover, §5.2; programme, parts 3 and 8)*
> - **Limit:** An "evaluation versus deployment" probe would keep its global score under RL but flip on edge cases, and retraining it recovers almost nothing. *(source: prior-art report 4 of 2 October — report, abstract only, to be checked)*
>   **Workaround:** none known; say so.
> - **Limit:** On honesty, truth probes did worse than a plain prompt; at a monitor's threshold, probes recall 43% at 1% false positives, against 55% for the best LLM monitor. *(source: course, Part 7, F·62; course, Part 7, F·51)*
>   **Workaround:** Beat a black-box or prompt baseline at equal cost, report recall at 1% false positives, and publish the result if the probe does not beat the prompt. *(source: course, Part 5, topic 1; course, Part 7, F·50; course, Part 7, F·29)*
> - **Limit:** Training-fit metrics read like generalization: your repository's probe metrics were training fit, and the ρ of 0.684 may be too. *(source: repository README)*
>   **Workaround:** Score items excluded from the probe's training, and extract on a disjoint set. *(source: repository README)*
> - **Limit:** Contrastive pairs can carry a style, and synthetic negatives can teach only a surface cue. *(source: course, Part M, M4; course, Part 2, §C)*
>   **Workaround:** A surface-only classifier must stay at chance between the two sides of the pairs; draw negatives from the model's real generations. *(source: course, Part M, M4; course, Part 2, §C)*
> - **Limit:** A silent probe does not separate "no intention" from "blind probe". *(source: handover, §5.2; reading sheets, part B, trap 3)*
>   **Workaround:** An organism in which you installed the intention yourself: measure sensitivity and false alarms there, and silence elsewhere becomes a bound. *(source: handover, §5.2)*
~~~

**Renvoi d'une ligne :**

~~~markdown
> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») *(v3.6)*
> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth") *(v3.6)*
~~~

**Où un renvoi ou un avertissement ponctuel est conseillé :**

- `tete_volet1` — FR l. 132 : Q4. « Comment saurais-tu qu’un modèle “fait semblant” d’être aligné ? » · EN l. 190 : Q4. "How would you know that a model is “pretending” to be aligned?" — renvoi.
- `tete_volet1` — FR l. 162 : Q10. « Défense en profondeur : quelles techniques de sûreté risquent d’échouer ensemble ? … · EN l. 226 : Q10. "Defense in depth: which safety techniques risk failing together?" — renvoi.
- `volet_M` — FR l. 345 : M8 · La forme qui sert la logique · EN l. 412 : M8 · The form that serves the logic — renvoi.
- `volet2_A_a_D` — FR l. 442 : Cas d'application — organismes modèles et bancs d'essai : « How would you build a monitor … · EN l. 528 : Worked case — model organisms and testbeds: "How would you build a monitor for a behaviour… — renvoi.
- `volet2_A_a_D` — FR l. 488 : Cas d'application — évaluations, capacité contre propension : « How would you separate a m… · EN l. 575 : Worked case — evaluations, capacity versus propensity: "How would you separate a model's c… — renvoi.
- `volet2_E_a_I` — FR l. 675 : Cas d'application — la supervision évolutive : « Would unsupervised elicitation still work… · EN l. 765 : Worked case — scalable oversight: "Would unsupervised elicitation still work on questions … — renvoi.
- `volet2_E_a_I` — FR l. 760 : Cas d'application — monitoring et AI control : « How would you design a control evaluation… · EN l. 852 : Worked case — monitoring and AI control: "How would you design a control evaluation for a … — renvoi.
- `volet3` — FR l. 953 : 3. Le contrôle par le monitoring (AI control) · EN l. 1076 : 3. Control through monitoring (AI control) — renvoi.
- `volet3` — FR l. 977 : 4. L’oversight évolutif — et, en son sein, l’honnêteté · EN l. 1101 : 4. Scalable oversight — and, within it, honesty — renvoi.
- `volets4_5_entete` — FR l. 1139 : Representation Engineering (RepE) (Zou et al.) · EN l. 1281 : Representation Engineering (RepE) (Zou et al.) — renvoi.
- `volets4_5_entete` — FR l. 1253 : Sujet 1 — Une probe de déception déployable · EN l. 1431 : Topic 1 — A deployable deception probe — renvoi.
- `volets4_5_entete` — FR l. 1267 : Sujet 4 — Mesurer (et faut-il supprimer ?) l’eval-awareness · EN l. 1445 : Topic 4 — Measuring (and should we suppress?) eval-awareness — renvoi.
- `volets4_5_entete` — FR l. 1271 : Sujet 6 — Honnêteté : lire la vérité sans juger la véracité · EN l. 1449 : Topic 6 — Honesty: reading truth without judging veracity — renvoi.
- `volet6` — FR l. 1578 : 8 · La validité des sondes d'activation hors distribution — pourquoi « validée par interve… · EN l. 1746 : 8 · Out-of-distribution validity of activation probes — why "validated by causal intervent… — renvoi.
- `volet7_B_et_D` — FR l. 1901 : F·31 · Persona Vectors — Chen, Arditi (Fellows, supervisés par Lindsey), Sleight, Evans et… · EN l. 2066 : F·31 · Persona Vectors — Chen, Arditi (Fellows, supervised by Lindsey), Sleight, Evans et … — renvoi.
- `volet7_B_et_D` — FR l. 2062 : F·62 · Evaluating honesty and lie detection techniques on a diverse suite of dishonest mod… · EN l. 2199 : F·62 · Evaluating honesty and lie detection techniques on a diverse suite of dishonest mod… — renvoi.
- `volet7_A_et_C` — FR l. 2072 : F·1 · Sleeper Agents (Hubinger et al., Anthropic, 2024) — [P·2] · EN l. 2206 : F·1 · Sleeper Agents (Hubinger et al., Anthropic, 2024) — [P·2] — renvoi.
- `volet7_A_et_C` — FR l. 2152 : F·4 · The Geometry of Truth (Marks & Tegmark, 2023) — [P·32] · EN l. 2286 : F·4 · The Geometry of Truth (Marks & Tegmark, 2023) — [P·32] — renvoi.
- `volet7_A_et_C` — FR l. 2176 : F·5 · Representation Engineering (Zou et al., 2023) — [P·rep] · EN l. 2310 : F·5 · Representation Engineering (Zou et al., 2023) — [P·rep] — renvoi.
- `volet7_A_et_C` — FR l. 2504 : F·50 · Detecting Strategic Deception with Linear Probes (Goldowsky-Dill et al., Apollo Res… · EN l. 2636 : F·50 · Detecting Strategic Deception with Linear Probes (Goldowsky-Dill et al., Apollo Res… — renvoi.
- `volet7_A_et_C` — FR l. 2522 : F·51 · Detecting High-Stakes Interactions with Activation Probes (McKenzie et al., LASR La… · EN l. 2654 : F·51 · Detecting High-Stakes Interactions with Activation Probes (McKenzie et al., LASR La… — renvoi.
- `volet7_A_et_C` — FR l. 2558 : F·53 · You Can't Escape Your Own Activations: Evaluation Awareness and Multi-Agent Monitor… · EN l. 2690 : F·53 · You Can't Escape Your Own Activations: Evaluation Awareness and Multi-Agent Monitor… — renvoi.
- `volets8_9` — FR l. 2798 : 6 · AI control — « Can we ensure safety by deploying models alongside sufficient safeguard… · EN l. 2955 : 6 · AI control — "Can we ensure safety by deploying models alongside sufficient safeguards… — renvoi.
- `volets8_9` — FR l. 2842 : 7 · Scalable oversight — « Can we design oversight mechanisms that will continue to work f… · EN l. 2999 : 7 · Scalable oversight — "Can we design oversight mechanisms that will continue to work fo… — renvoi.
- `volet10` — FR l. 3264 : AI control › Activation monitoring · EN l. 3504 : AI control › Activation monitoring — renvoi.
- `volet10` — FR l. 3477 : Scalable oversight › Honesty · EN l. 3715 : Scalable oversight › Honesty — renvoi.
- `volet11_1_a_20` — FR l. 3673 : 1 · « Tell us about your work. » — l'ouverture · EN l. 3912 : 1 · « Tell us about your work. » — l'ouverture — renvoi.
- `volet11_1_a_20` — FR l. 3775 : 6 · « How would you detect misalignment in a model you can't fully trust? » *(question rée… · EN l. 4024 : 6 · « How would you detect misalignment in a model you can't fully trust? » *(question rée… — renvoi.
- `volet11_1_a_20` — FR l. 3898 : 11 · Les prémisses fausses — dix questions qui supposent un résultat que tu n'as pas, et l… · EN l. 4149 : 11 · Les prémisses fausses — dix questions qui supposent un résultat que tu n'as pas, et l… — renvoi.
- `volet11_1_a_20` — FR l. 4102 : 20 · « Suppose you must deploy a capable model you cannot fully trust. How would you desig… · EN l. 4377 : 20 · « Suppose you must deploy a capable model you cannot fully trust. How would you desig… — renvoi.
- `volet11_21_a_52` — FR l. 4129 : 21 · « A probe trained on synthetic examples of a bad behaviour must catch the real thing.… · EN l. 4404 : 21 · « A probe trained on synthetic examples of a bad behaviour must catch the real thing.… — renvoi.
- `volet11_21_a_52` — FR l. 4156 : 22 · « How would you tell that a model is being honest when you cannot judge whether its a… · EN l. 4429 : 22 · « How would you tell that a model is being honest when you cannot judge whether its a… — renvoi.
- `volet11_21_a_52` — FR l. 4187 : 24 · « Probes drift toward "I am being evaluated" under adversarial pressure. How do you k… · EN l. 4463 : 24 · « Probes drift toward "I am being evaluated" under adversarial pressure. How do you k… — renvoi.
- `volet11_53_et_fin` — FR l. 4776 : 56 · « How would you know a model is faking alignment? » (I.4) · EN l. 5087 : 56 · « How would you know a model is faking alignment? » (I.4) — renvoi.
- `volet11_53_et_fin` — FR l. 4938 : A3 · « What if the probes just don't work at all — the two-family test fails, nothing gene… · EN l. 5255 : A3 · « What if the probes just don't work at all — the two-family test fails, nothing gene… — renvoi.
- `volet11_53_et_fin` — FR l. 5141 : B4 · « How would you measure evaluation awareness that the model never verbalizes? » · EN l. 5466 : B4 · « How would you measure evaluation awareness that the model never verbalizes? » — renvoi.
- `volet11_53_et_fin` — FR l. 5336 : B13 · « Can honesty be trained rather than detected — and how would you know the trained m… · EN l. 5661 : B13 · « Can honesty be trained rather than detected — and how would you know the trained m… — renvoi.
- `volet3` — avertissement ponctuel prêt, après FR l. 1001 / EN l. 1126 (texte dans la partie « Par tranche »).
- `volet7_A_et_C` — avertissement ponctuel prêt, après FR l. 2080 / EN l. 2214 (texte dans la partie « Par tranche »).
- `volet7_A_et_C` — avertissement ponctuel prêt, après FR l. 2509 / EN l. 2641 (texte dans la partie « Par tranche »).
- `volet11_21_a_52` — avertissement ponctuel prêt, après FR l. 4194 / EN l. 4469 (texte dans la partie « Par tranche »).

**Où il revient** (relevé automatique, motifs FR `\bsonde|\bprobe` / EN `\bprobe` ; sections, avec le nombre de lignes touchées) :

- `tete_volet1` — FR : l. 1 COURS D'ALIGNEMENT — VERSION FUSIONNÉE v3.5 — 27… (1) ; l. 132 Q4. « Comment saurais-tu qu’un modèle “fait semb… (1) ; l. 138 Q5. « Peut-on faire confiance à la chaîne de pen… (1) ; l. 158 Q9. « Quelle est ta “théorie de l’impact” : si t… (1) ; l. 162 Q10. « Défense en profondeur : quelles technique… (1)
  — EN : l. 21 ALIGNMENT COURSE — MERGED VERSION v3.5 — Septemb… (1) ; l. 190 Q4. "How would you know that a model is “pretend… (1) ; l. 197 Q5. "Can we trust a model's chain of thought to … (1) ; l. 221 Q9. "What is your “theory of impact”: if your re… (1) ; l. 226 Q10. "Defense in depth: which safety techniques … (1)
- `volet_M` — FR : l. 194 M1 · L'arc d'une réponse, en sept temps (1) ; l. 219 M2 · Le pari : sur le modèle, jamais sur la méth… (2) ; l. 298 M5 · Le nul et le cas connu (4) ; l. 345 M8 · La forme qui sert la logique (3)
  — EN : l. 261 M1 · The arc of an answer, in seven beats (1) ; l. 286 M2 · The bet: on the model, never on the method (2) ; l. 365 M5 · The null and the known case (4) ; l. 412 M8 · The form that serves the logic (3)
- `volet2_A_a_D` — FR : l. 442 Cas d'application — organismes modèles et bancs … (8) ; l. 488 Cas d'application — évaluations, capacité contre… (2) ; l. 513 C. Méthodes sur activations — probing & steering… (1) ; l. 523 Cas d'application — sondes et pilotage : « How w… (1) ; l. 559 C bis · L'espace de travail (J-space) et le J-le… (7)
  — EN : l. 528 Worked case — model organisms and testbeds: "How… (8) ; l. 575 Worked case — evaluations, capacity versus prope… (2) ; l. 600 C. Methods on activations — probing & steering (… (1) ; l. 611 Worked case — probes and steering: "How would yo… (1) ; l. 647 C bis · The workspace (J-space) and the J-lens —… (7)
- `volet2_E_a_I` — FR : l. 675 Cas d'application — la supervision évolutive : «… (3) ; l. 752 G. Monitoring & AI control — limiter les dégâts … (1) ; l. 760 Cas d'application — monitoring et AI control : «… (11)
  — EN : l. 765 Worked case — scalable oversight: "Would unsuper… (2) ; l. 843 G. Monitoring & AI control — limiting the damage… (1) ; l. 852 Worked case — monitoring and AI control: "How wo… (11)
- `volet3` — FR : l. 953 3. Le contrôle par le monitoring (AI control) (8) ; l. 977 4. L’oversight évolutif — et, en son sein, l’hon… (9) ; l. 1003 5. La robustesse adverse (1)
  — EN : l. 1076 3. Control through monitoring (AI control) (8) ; l. 1101 4. Scalable oversight — and, within it, honesty (9) ; l. 1128 5. Adversarial robustness (1)
- `volets4_5_entete` — FR : l. 1119 Sleeper Agents (Anthropic, Hubinger et al.) (1) ; l. 1153 Towards puis Scaling Monosemanticity (Anthropic, (2) ; l. 1185 Auditing Hidden Objectives (Anthropic, Marks et … (1) ; l. 1219 1. La thèse-signature : l’écart représentation–c… (2) ; l. 1235 4. La théorie de l’impact (1) ; l. 1243 6. Gérer le pushback (1) ; l. 1251 A. Tes sujets FORT — ta thèse peut être la colon… (6) ; l. 1285 B. Leurs sujets — méthodothèque, dosage léger ou… (1) ; l. 1326 Les papiers — quatre niveaux (1) ; l. 1350 Les questions — par probabilité et par enjeu (2)
  — EN : l. 1254 The key papers, told one by one (5) ; l. 1389 1. The signature thesis: the representation–caus… (2) ; l. 1408 4. The theory of impact (1) ; l. 1418 6. Handling pushback (1) ; l. 1428 A. Your STRONG topics — your thesis can be the b… (6) ; l. 1463 B. Their topics — method toolkit, light or zero … (1) ; l. 1506 The papers — four levels (1) ; l. 1530 The questions — by probability and by stakes (2)
- `volet6` — FR : l. 1402 2. Tes résultats, tels que ton dossier les porte… (2) ; l. 1451 3. Les trois contrôles à ne jamais confondre (1) ; l. 1499 6. Ton programme de recherche, et sa revue d'ant… (6) ; l. 1569 7. Ce que ces compléments changent aux volets 1 … (1) ; l. 1578 8 · La validité des sondes d'activation hors dis… (15)
  — EN : l. 1579 2. Your results, as your dossier carries them on… (1) ; l. 1593 3. The three controls never to confuse (1) ; l. 1615 6. Your research program, and its prior-art revi… (5) ; l. 1676 7. What these supplements change in Parts 1 to 5 (3) ; l. 1746 8 · Out-of-distribution validity of activation p… (15)
- `volet7_B_et_D` — FR : l. 1777 F·29 · Fine-Tuned Lie Detectors Failed to Genera… (5) ; l. 1876 F·33 · Inoculation Prompting — Wichers, Ebtekar … (1) ; l. 2000 F·36 · Beyond Data Filtering : Knowledge Localiz… (1) ; l. 2032 F·26 · Removing Sandbagging in LLMs by Training … (1) ; l. 2062 F·62 · Evaluating honesty and lie detection tech… (1)
  — EN : l. 1942 F·29 · Fine-Tuned Lie Detectors Failed to Genera… (6) ; l. 2041 F·33 · Inoculation Prompting — Wichers, Ebtekar … (1) ; l. 2165 F·36 · Beyond Data Filtering : Knowledge Localiz… (1) ; l. 2186 F·26 · Removing Sandbagging in LLMs by Training … (1) ; l. 2199 F·62 · Evaluating honesty and lie detection tech… (1)
- `volet7_A_et_C` — FR : l. 2072 F·1 · Sleeper Agents (Hubinger et al., Anthropic… (4) ; l. 2098 F·2 · Alignment Faking in Large Language Models … (2) ; l. 2152 F·4 · The Geometry of Truth (Marks & Tegmark, 20… (1) ; l. 2200 F·6 · Discovering Latent Knowledge Without Super… (4) ; l. 2274 F·9 · Circuit Tracing / On the Biology of a Larg… (1) ; l. 2304 F·10 · AI Control: Improving Safety Despite Inte… (3) ; l. 2400 F·14 · Eliciting Latent Knowledge — le rapport E… (4) ; l. 2472 F·17 · L'unlearning mis à l'épreuve (Deeb et Rog… (3) ; l. 2504 F·50 · Detecting Strategic Deception with Linear… (5) ; l. 2522 F·51 · Detecting High-Stakes Interactions with A… (6) ; … (+5 sections)
  — EN : l. 2206 F·1 · Sleeper Agents (Hubinger et al., Anthropic… (4) ; l. 2232 F·2 · Alignment Faking in Large Language Models … (2) ; l. 2286 F·4 · The Geometry of Truth (Marks & Tegmark, 20… (1) ; l. 2334 F·6 · Discovering Latent Knowledge Without Super… (4) ; l. 2408 F·9 · Circuit Tracing / On the Biology of a Larg… (1) ; l. 2438 F·10 · AI Control: Improving Safety Despite Inte… (3) ; l. 2534 F·14 · Eliciting Latent Knowledge — the ELK repo… (4) ; l. 2606 F·17 · L'unlearning mis à l'épreuve (Deeb and Ro… (3) ; l. 2636 F·50 · Detecting Strategic Deception with Linear… (5) ; l. 2654 F·51 · Detecting High-Stakes Interactions with A… (6) ; … (+5 sections)
- `volets8_9` — FR : l. 2666 VOLET 8 — Références, dans l'ordre des fiches (3) ; l. 2798 6 · AI control — « Can we ensure safety by deplo… (5) ; l. 2842 7 · Scalable oversight — « Can we design oversig… (3) ; l. 2912 9 · Miscellaneous (1)
  — EN : l. 2804 PART 8 — References, in the order of the sheets (3) ; l. 2955 6 · AI control — "Can we ensure safety by deploy… (5) ; l. 2999 7 · Scalable oversight — "Can we design oversigh… (3) ; l. 3069 9 · Miscellaneous (1) ; l. 3085 10 · The overall reading, in three sentences for… (1)
- `volet10` — FR : l. 2936 VOLET 10 — Les liens de la page des directions, … (1) ; l. 2946 0 · Ce qui a été lu, et comment (1) ; l. 2980 Dans les fiches (14) (3) ; l. 3071 AI Sandbagging: Language Models can Strategicall… (2) ; l. 3138 SelfIE: Self-Interpretation of Large Language Mo… (3) ; l. 3148 Patchscopes: A Unifying Framework for Inspecting… (3) ; l. 3168 LatentQA: Teaching LLMs to Decode Activations In… (2) ; l. 3266 Coup probes: Catching catastrophes with probes t… (7) ; l. 3276 Improving Alignment and Robustness with Circuit … (4) ; l. 3299 Eliciting Latent Knowledge from “Quirky” Languag… (3) ; … (+10 sections)
  — EN : l. 3179 PART 10 — The links of the directions page, read… (1) ; l. 3189 0 · What was read, and how (1) ; l. 3223 In the sheets (14) (3) ; l. 3313 AI Sandbagging: Language Models can Strategicall… (2) ; l. 3380 SelfIE: Self-Interpretation of Large Language Mo… (3) ; l. 3390 Patchscopes: A Unifying Framework for Inspecting… (3) ; l. 3410 LatentQA: Teaching LLMs to Decode Activations In… (2) ; l. 3506 Coup probes: Catching catastrophes with probes t… (7) ; l. 3516 Improving Alignment and Robustness with Circuit … (4) ; l. 3539 Eliciting Latent Knowledge from “Quirky” Languag… (3) ; … (+10 sections)
- `volet11_1_a_20` — FR : l. 3656 VOLET 11 — Les réponses complètes (v2.3, 23 sept… (2) ; l. 3663 RÉPONSES COMPLÈTES — v2.3 — 23 septembre 2026 (v… (1) ; l. 3665 Chaque réponse est écrite pour être comprise san… (1) ; l. 3673 1 · « Tell us about your work. » — l'ouverture (2) ; l. 3704 2 · « What did your rank-three ablation actually… (1) ; l. 3775 6 · « How would you detect misalignment in a mod… (7) ; l. 3854 9 · « What would you work on here, and why? » (4) ; l. 3904 « Your probes hit ninety-nine percent, so defere… (6) ; l. 3989 « NARCBench already does sequential aggregation … (2) ; l. 4001 12 · « Why Anthropic? » (1) ; … (+3 sections)
  — EN : l. 3895 PART 11 — The complete answers (v2.3, 23 Septemb… (2) ; l. 3912 1 · « Tell us about your work. » — l'ouverture (2) ; l. 3945 2 · « What did your rank-three ablation actually… (1) ; l. 4024 6 · « How would you detect misalignment in a mod… (6) ; l. 4104 9 · « What would you work on here, and why? » (3) ; l. 4155 « Your probes hit ninety-nine percent, so defere… (3) ; l. 4240 « NARCBench already does sequential aggregation … (1) ; l. 4252 12 · « Why Anthropic? » (1) ; l. 4275 14 · « What would you want to have done in four … (1) ; l. 4350 19 · « A model behaves differently when it belie… (1) ; … (+1 sections)
- `volet11_21_a_52` — FR : l. 4129 21 · « A probe trained on synthetic examples of … (7) ; l. 4156 22 · « How would you tell that a model is being … (2) ; l. 4177 23 · « NARCBench already correlates probe scores… (2) ; l. 4187 24 · « Probes drift toward "I am being evaluated… (6) ; l. 4224 26 · « What would kill this programme in the fir… (2) ; l. 4235 27 · « When an autonomous agent's goals are bloc… (1) ; l. 4255 28 · « We saw a model comply during training whi… (2) ; l. 4361 33 · « A weak trusted scorer, a strong untrusted… (1) ; l. 4386 34 · « Can automated researchers do alignment re… (1) ; l. 4408 35 · « Can we build a lie detector for language … (1) ; … (+7 sections)
  — EN : l. 4404 21 · « A probe trained on synthetic examples of … (8) ; l. 4429 22 · « How would you tell that a model is being … (2) ; l. 4451 23 · « NARCBench already correlates probe scores… (2) ; l. 4463 24 · « Probes drift toward "I am being evaluated… (7) ; l. 4500 26 · « What would kill this programme in the fir… (2) ; l. 4517 27 · « When an autonomous agent's goals are bloc… (1) ; l. 4538 28 · « We saw a model comply during training whi… (3) ; l. 4647 33 · « A weak trusted scorer, a strong untrusted… (1) ; l. 4676 34 · « Can automated researchers do alignment re… (1) ; l. 4699 35 · « Can we build a lie detector for language … (1) ; … (+7 sections)
- `volet11_53_et_fin` — FR : l. 4776 56 · « How would you know a model is faking alig… (3) ; l. 4850 62 · « Is alignment actually hard? What would ch… (1) ; l. 4862 63 · Tes huit positions, dites en entier (VII) —… (5) ; l. 4910 A1 · « Which team would you want to join — Align… (3) ; l. 4923 A2 · « You have $15,000 of compute a month and f… (2) ; l. 4938 A3 · « What if the probes just don't work at all… (5) ; l. 4977 A6 · « Suppose a probe flags an agent mid-trajec… (2) ; l. 5003 A8 · « How do you think about the dual-use of yo… (1) ; l. 5096 B2 · « How would you design an evaluation a mode… (2) ; l. 5141 B4 · « How would you measure evaluation awarenes… (9) ; … (+4 sections)
  — EN : l. 5087 56 · « How would you know a model is faking alig… (2) ; l. 5164 62 · « Is alignment actually hard? What would ch… (1) ; l. 5177 63 · Tes huit positions, dites en entier (VII) —… (3) ; l. 5225 A1 · « Which team would you want to join — Align… (3) ; l. 5239 A2 · « You have $15,000 of compute a month and f… (2) ; l. 5255 A3 · « What if the probes just don't work at all… (5) ; l. 5298 A6 · « Suppose a probe flags an agent mid-trajec… (2) ; l. 5327 A8 · « How do you think about the dual-use of yo… (1) ; l. 5421 B2 · « How would you design an evaluation a mode… (1) ; l. 5466 B4 · « How would you measure evaluation awarenes… (4) ; … (+4 sections)

---

## 8. Pilotage par vecteurs (dont vecteurs de persona) — *Steering vectors (including persona vectors)*

- **Maison** : tranche `volet2_A_a_D` ; FR : volet 2, §C · méthodes sur activations (après « En pratique — Contrastive Activation Addition ») ; EN : Part 2, §C · methods on activations (after "In practice — Contrastive Activation Addition").
- **Limites** : 8 ; **parades** : 6.
- **Ancre FR** (ligne 521 de la v3.5 FR ; l'encadré s'insère juste après) :

~~~text
En pratique — Contrastive Activation Addition (CAA) (Panickssery). Le but était de piloter des comportements de haut niveau — sycophantie, corrigibilité, refus — directement à l’inférence, sans réentraîner. La méthode du steering par paires contrastives y répond : on construit la direction à partir de paires d’exemples qui ne diffèrent que sur le comportement visé (l’un sycophante, l’autre non), on calcule leur différence moyenne, et on l’ajoute aux activations pendant la génération pour augmenter ou diminuer le comportement à volonté. C’est ta méthode exacte — et le fait qu’elle figure dans la section Honesty du roadmap d’Anthropic est ce qui rend tes travaux directement pertinents pour eux.
~~~

- **Ancre EN** (ligne 609 de la v3.5 EN) :

~~~text
In practice — Contrastive Activation Addition (CAA) (Panickssery). The goal was to steer high-level behaviors — sycophancy, corrigibility, refusal — directly at inference, without retraining. The method of steering by contrastive pairs answers this: we build the direction from pairs of examples that differ only in the targeted behavior (one sycophantic, the other not), compute their mean difference, and add it to the activations during generation to increase or decrease the behavior at will. This is your exact method — and the fact that it appears in the Honesty section of Anthropic's roadmap is what makes your work directly relevant to them.
~~~

**Encadré complet, français :**

~~~markdown
> **⚠ Limites et parades — Pilotage par vecteurs (dont vecteurs de persona)** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** « La direction bouge le comportement » n'est pas « le concept cause le comportement » : chaque direction pilotée dégrade la sortie, et des vecteurs arbitraires bougent aussi le comportement. *(source : fiche 2 ; fiches, partie B, piège 4)*
>   **Parade :** La direction aléatoire de même norme n'est que le nul de spécificité ; le dommage ne s'écarte qu'à dégradation appariée, par une courbe dose-réponse contre plusieurs témoins. *(source : cours, volet M, M4 ; cours, volet 2, §C, K47)*
> - **Limite :** Un nul de pilotage peut venir d'un rang trop bas, si le concept est réparti. *(source : fiche 7 ; contre-lecture des fiches)*
>   **Parade :** Un cas connu au même réglage — un vecteur de pays, qui s'échange dans l'article sur l'espace de travail — et un balayage de rang dans une même expérience, sur des sous-espaces emboîtés. *(source : cours, volet 2, §C, K47 ; cours, volet 6, §6)*
> - **Limite :** L'addition d'activations contrastives peut forcer un artefact de polarité oui/non au lieu de retirer la complaisance. *(source : README du dépôt)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** L'effet dépend du jeu de données et de la couche : « highly dataset-dependent ». *(source : fiche 2 ; cours, volet 7, F·7)*
>   **Parade :** Rapporter jeu de données par jeu de données, et choisir la couche sur un jeu de validation, jamais sur le test. *(source : programme, partie 3)*
> - **Limite :** Le modèle peut détecter le pilotage. *(source : programme, partie 8 (travail cité, non ouvert))*
>   **Parade :** La même machinerie d'intervention dans tous les bras, témoins compris. *(source : programme, partie 8)*
> - **Limite :** Le pilotage peut faire taire la verbalisation sans toucher la représentation latente ; des directions aléatoires la font baisser aussi. *(source : programme, partie 8 ; fiche 2)*
>   **Parade :** Un critère principal comportemental et une sonde latente comme contrôle ; la verbalisation n'est jamais une preuve d'inhibition. *(source : programme, partie 8)*
> - **Limite :** Vecteurs de persona : le trait se nomme d'avance, les directions sont grossières, le lien entre déplacement et trait n'est que corrélationnel, l'évaluation est légère. *(source : fiche 8)*
>   **Parade :** Pour la causalité, le test à dégradation appariée ; pour l'extraction supervisée, aucune parade connue, on le dit. *(source : cours, volet M, M4 ; fiche 8)*
> - **Limite :** Piloter loin d'une persona pendant l'entraînement aurait doublé la diffusion du désalignement, de 24 % à environ 50 %. *(source : rapport d'antériorité 3 du 2 octobre — rapport, non vérifié)*
>   **Parade :** aucune connue ; on le dit.
~~~

**Encadré complet, anglais :**

~~~markdown
> **⚠ Limits and workarounds — Steering vectors (including persona vectors)** *(v3.6, 2 October 2026)*
>
> - **Limit:** "The direction moves behaviour" is not "the concept causes behaviour": every steered direction degrades the output, and arbitrary vectors move behaviour too. *(source: reading sheet 2; reading sheets, part B, trap 4)*
>   **Workaround:** The matched-norm random direction is only the specificity null; damage is ruled out only at matched degradation, by a dose-response curve against several controls. *(source: course, Part M, M4; course, Part 2, §C, K47)*
> - **Limit:** A steering null can come from too low a rank, if the concept is distributed. *(source: reading sheet 7; counter-reading of the sheets)*
>   **Workaround:** A known case at the same setting — a country vector, which swaps in the workspace paper — and a rank sweep within one experiment, on nested subspaces. *(source: course, Part 2, §C, K47; course, Part 6, §6)*
> - **Limit:** Contrastive activation addition can force a yes/no polarity artefact instead of removing sycophancy. *(source: repository README)*
>   **Workaround:** none known; say so.
> - **Limit:** The effect depends on the dataset and the layer: "highly dataset-dependent". *(source: reading sheet 2; course, Part 7, F·7)*
>   **Workaround:** Report dataset by dataset, and choose the layer on a validation set, never on the test set. *(source: programme, part 3)*
> - **Limit:** The model may detect the steering. *(source: programme, part 8 (cited work, not opened))*
>   **Workaround:** The same intervention machinery in every arm, controls included. *(source: programme, part 8)*
> - **Limit:** Steering can silence verbalization without touching the latent representation; random directions lower it too. *(source: programme, part 8; reading sheet 2)*
>   **Workaround:** A behavioural main criterion and a latent probe as a control; verbalization is never proof of inhibition. *(source: programme, part 8)*
> - **Limit:** Persona vectors: the trait must be named in advance, the directions are coarse, the shift-to-trait link is only correlational, the evaluation is light. *(source: reading sheet 8)*
>   **Workaround:** For causality, the matched-degradation test; for supervised extraction, none known, say so. *(source: course, Part M, M4; reading sheet 8)*
> - **Limit:** Steering away from a persona during training reportedly doubled the spread of misalignment, from 24% to about 50%. *(source: prior-art report 3 of 2 October — report, unverified)*
>   **Workaround:** none known; say so.
~~~

**Renvoi d'une ligne :**

~~~markdown
> ⚠ **Limites et parades** : pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») *(v3.6)*
> ⚠ **Limits and workarounds**: steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition") *(v3.6)*
~~~

**Où un renvoi ou un avertissement ponctuel est conseillé :**

- `volets4_5_entete` — FR l. 1139 : Representation Engineering (RepE) (Zou et al.) · EN l. 1281 : Representation Engineering (RepE) (Zou et al.) — renvoi.
- `volets4_5_entete` — FR l. 1257 : Sujet 2 — Fiabilité du steering : quand une direction suffit-elle ? · EN l. 1435 : Topic 2 — Steering reliability: when does a direction suffice? — renvoi.
- `volets4_5_entete` — FR l. 1275 : Sujet 10 — Persona et science du caractère · EN l. 1453 : Topic 10 — Persona and the science of character — renvoi.
- `volet7_B_et_D` — FR l. 1901 : F·31 · Persona Vectors — Chen, Arditi (Fellows, supervisés par Lindsey), Sleight, Evans et… · EN l. 2066 : F·31 · Persona Vectors — Chen, Arditi (Fellows, supervised by Lindsey), Sleight, Evans et … — renvoi.
- `volet7_B_et_D` — FR l. 2062 : F·62 · Evaluating honesty and lie detection techniques on a diverse suite of dishonest mod… · EN l. 2199 : F·62 · Evaluating honesty and lie detection techniques on a diverse suite of dishonest mod… — renvoi.
- `volet7_A_et_C` — FR l. 2152 : F·4 · The Geometry of Truth (Marks & Tegmark, 2023) — [P·32] · EN l. 2286 : F·4 · The Geometry of Truth (Marks & Tegmark, 2023) — [P·32] — renvoi.
- `volet7_A_et_C` — FR l. 2176 : F·5 · Representation Engineering (Zou et al., 2023) — [P·rep] · EN l. 2310 : F·5 · Representation Engineering (Zou et al., 2023) — [P·rep] — renvoi.
- `volet7_A_et_C` — FR l. 2224 : F·7 · Contrastive Activation Addition et Inference-Time Intervention (Rimsky et al. ; Li e… · EN l. 2358 : F·7 · Contrastive Activation Addition and Inference-Time Intervention (Rimsky et al.; Li e… — renvoi.
- `volet10` — FR l. 3477 : Scalable oversight › Honesty · EN l. 3715 : Scalable oversight › Honesty — renvoi.
- `volet11_1_a_20` — FR l. 3727 : 3 · « And rank one? Didn't a single direction work? » · EN l. 3970 : 3 · « And rank one? Didn't a single direction work? » — renvoi.
- `volet11_1_a_20` — FR l. 3898 : 11 · Les prémisses fausses — dix questions qui supposent un résultat que tu n'as pas, et l… · EN l. 4149 : 11 · Les prémisses fausses — dix questions qui supposent un résultat que tu n'as pas, et l… — renvoi.
- `volet11_1_a_20` — FR l. 4079 : 19 · « A model behaves differently when it believes it is being tested. What do you do wit… · EN l. 4350 : 19 · « A model behaves differently when it believes it is being tested. What do you do wit… — renvoi.
- `volet11_21_a_52` — FR l. 4273 : 29 · « Can you read a model's personality in its activations — and control it? » (III.3 · … · EN l. 4558 : 29 · « Can you read a model's personality in its activations — and control it? » (III.3 · … — renvoi.
- `volet11_53_et_fin` — FR l. 4991 : A7 · « A colleague shows you a beautiful steering result — one direction, huge behavioural… · EN l. 5313 : A7 · « A colleague shows you a beautiful steering result — one direction, huge behavioural… — renvoi.
- `volets4_5_entete` — avertissement ponctuel prêt, après FR l. 1149 / EN l. 1291 (texte dans la partie « Par tranche »).
- `volets4_5_entete` — avertissement ponctuel prêt, après FR l. 1269 / EN l. 1447 (texte dans la partie « Par tranche »).
- `volet7_B_et_D` — avertissement ponctuel prêt, après FR l. 1915 / EN l. 2080 (texte dans la partie « Par tranche »).
- `volet7_A_et_C` — avertissement ponctuel prêt, après FR l. 2157 / EN l. 2291 (texte dans la partie « Par tranche »).

**Où il revient** (relevé automatique, motifs FR `pilot|steer|\bCAA\b|vecteur` / EN `steer|\bCAA\b|vector` ; sections, avec le nombre de lignes touchées) :

- `volet_M` — FR : l. 184 Ce que ce volet ajoute, et pourquoi il vient ava… (2) ; l. 219 M2 · Le pari : sur le modèle, jamais sur la méth… (3) ; l. 234 M3 · Deux branches, une mesure — et ce qui te fe… (1) ; l. 257 M4 · Le contrôle : ce qu'il écarte, et il doit s… (2) ; l. 345 M8 · La forme qui sert la logique (2)
  — EN : l. 286 M2 · The bet: on the model, never on the method (2) ; l. 301 M3 · Two branches, one measurement — and what wo… (1) ; l. 324 M4 · The control: what it rules out, and it must… (1) ; l. 456 M10 · The checklist, to reread before each rehea… (1)
- `volet2_A_a_D` — FR : l. 488 Cas d'application — évaluations, capacité contre… (1) ; l. 513 C. Méthodes sur activations — probing & steering… (4) ; l. 523 Cas d'application — sondes et pilotage : « How w… (10) ; l. 559 C bis · L'espace de travail (J-space) et le J-le… (3) ; l. 635 Cas d'application — l'interprétabilité mécaniste… (7)
  — EN : l. 600 C. Methods on activations — probing & steering (… (4) ; l. 611 Worked case — probes and steering: "How would yo… (13) ; l. 647 C bis · The workspace (J-space) and the J-lens —… (3) ; l. 724 Worked case — mechanistic interpretability: "Two… (7)
- `volet2_E_a_I` — FR : l. 675 Cas d'application — la supervision évolutive : «… (1) ; l. 760 Cas d'application — monitoring et AI control : «… (1)
  — EN : —
- `volet3` — FR : l. 899 1. Évaluer les capacités (1) ; l. 977 4. L’oversight évolutif — et, en son sein, l’hon… (2) ; l. 1003 5. La robustesse adverse (1) ; l. 1029 6. Le domaine « divers » : désapprentissage et g… (1) ; l. 1053 PARTIE II — LES ÉQUIPES : qui fait quoi chez (2) ; l. 1077 PARTIE III — LES TRAVAUX DU MOMENT (2025-2026) (1)
  — EN : l. 1101 4. Scalable oversight — and, within it, honesty (2) ; l. 1180 SECTION II — THE TEAMS: who does what at (3) ; l. 1202 SECTION III — CURRENT WORK (2025-2026) (2) ; l. 1228 SECTION IV — SYNTHESIS: how everything fits toge… (2)
- `volets4_5_entete` — FR : l. 1127 Sycophancy (Anthropic, Sharma et al.) (1) ; l. 1139 Representation Engineering (RepE) (Zou et al.) (3) ; l. 1153 Towards puis Scaling Monosemanticity (Anthropic, (1) ; l. 1203 L’unlearning mis à l’épreuve (Deeb et Roger) (1) ; l. 1219 1. La thèse-signature : l’écart représentation–c… (2) ; l. 1227 2. L’articulation avec leur canon (1) ; l. 1231 3. Ton ancrage empirique : l’eval-awareness (1) ; l. 1251 A. Tes sujets FORT — ta thèse peut être la colon… (5) ; l. 1326 Les papiers — quatre niveaux (1)
  — EN : l. 1254 The key papers, told one by one (7) ; l. 1389 1. The signature thesis: the representation–caus… (2) ; l. 1398 2. How it fits with their canon (1) ; l. 1403 3. Your empirical anchor: eval-awareness (1) ; l. 1413 5. The dosage rules: anti-monomania (1) ; l. 1428 A. Your STRONG topics — your thesis can be the b… (6) ; l. 1506 The papers — four levels (2)
- `volet6` — FR : l. 1402 2. Tes résultats, tels que ton dossier les porte… (3) ; l. 1499 6. Ton programme de recherche, et sa revue d'ant… (3) ; l. 1569 7. Ce que ces compléments changent aux volets 1 … (1) ; l. 1578 8 · La validité des sondes d'activation hors dis… (1)
  — EN : l. 1579 2. Your results, as your dossier carries them on… (2) ; l. 1603 5. The work of the Fellows program, 2025-2026 — … (1) ; l. 1615 6. Your research program, and its prior-art revi… (3) ; l. 1676 7. What these supplements change in Parts 1 to 5 (3) ; l. 1746 8 · Out-of-distribution validity of activation p… (1)
- `volet7_B_et_D` — FR : l. 1777 F·29 · Fine-Tuned Lie Detectors Failed to Genera… (1) ; l. 1876 F·33 · Inoculation Prompting — Wichers, Ebtekar … (2) ; l. 1901 F·31 · Persona Vectors — Chen, Arditi (Fellows, … (10) ; l. 2062 F·62 · Evaluating honesty and lie detection tech… (1)
  — EN : l. 1942 F·29 · Fine-Tuned Lie Detectors Failed to Genera… (1) ; l. 2041 F·33 · Inoculation Prompting — Wichers, Ebtekar … (4) ; l. 2066 F·31 · Persona Vectors — Chen, Arditi (Fellows, … (12) ; l. 2194 F·60 · Automated Researchers Can Subtly Sandbag … (1) ; l. 2199 F·62 · Evaluating honesty and lie detection tech… (1)
- `volet7_A_et_C` — FR : l. 2124 F·3 · Towards Understanding Sycophancy in Langua… (1) ; l. 2176 F·5 · Representation Engineering (Zou et al., 20… (5) ; l. 2224 F·7 · Contrastive Activation Addition et Inferen… (7) ; l. 2249 F·8 · Towards puis Scaling Monosemanticity (Anth… (1) ; l. 2472 F·17 · L'unlearning mis à l'épreuve (Deeb et Rog… (1)
  — EN : l. 2258 F·3 · Towards Understanding Sycophancy in Langua… (1) ; l. 2310 F·5 · Representation Engineering (Zou et al., 20… (5) ; l. 2358 F·7 · Contrastive Activation Addition and Infere… (7) ; l. 2383 F·8 · Towards then Scaling Monosemanticity (Anth… (1) ; l. 2408 F·9 · Circuit Tracing / On the Biology of a Larg… (1) ; l. 2606 F·17 · L'unlearning mis à l'épreuve (Deeb and Ro… (1)
- `volets8_9` — FR : l. 2666 VOLET 8 — Références, dans l'ordre des fiches (1) ; l. 2842 7 · Scalable oversight — « Can we design oversig… (1)
  — EN : l. 2804 PART 8 — References, in the order of the sheets (2) ; l. 2935 4 · Persona and out-of-distribution generalizati… (1) ; l. 2999 7 · Scalable oversight — "Can we design oversigh… (1) ; l. 3085 10 · The overall reading, in three sentences for… (2)
- `volet10` — FR : l. 2946 0 · Ce qui a été lu, et comment (1) ; l. 3096 Monitor: An AI-Driven Observability Interface — … (1) ; l. 3158 Vector-ICL: In-context Learning with Continuous … (3) ; l. 3168 LatentQA: Teaching LLMs to Decode Activations In… (2) ; l. 3389 Prover-Verifier Games improve legibility of LLM … (1) ; l. 3501 Representation Engineering: A Top-Down Approach … (2) ; l. 3511 Steering Llama 2 via Contrastive Activation Addi… (6)
  — EN : l. 3189 0 · What was read, and how (1) ; l. 3338 Monitor: An AI-Driven Observability Interface — … (1) ; l. 3400 Vector-ICL: In-context Learning with Continuous … (5) ; l. 3410 LatentQA: Teaching LLMs to Decode Activations In… (2) ; l. 3739 Representation Engineering: A Top-Down Approach … (2) ; l. 3749 Steering Llama 2 via Contrastive Activation Addi… (6)
- `volet11_1_a_20` — FR : l. 3656 VOLET 11 — Les réponses complètes (v2.3, 23 sept… (1) ; l. 3727 3 · « And rank one? Didn't a single direction wo… (3) ; l. 3762 5 · « What did you get wrong? » (1) ; l. 3775 6 · « How would you detect misalignment in a mod… (1) ; l. 3926 « Your rank-one steering worked, it was just wea… (3) ; l. 3971 « Persona vectors only monitor — they can't be u… (4) ; l. 3981 « Your sequential monitor already beat TRACE in … (3) ; l. 4012 13 · « Tell us about a time an experiment failed… (1) ; l. 4036 16 · « Explain the law. Why would a rating go do… (1) ; l. 4079 19 · « A model behaves differently when it belie… (5)
  — EN : l. 3970 3 · « And rank one? Didn't a single direction wo… (1) ; l. 4024 6 · « How would you detect misalignment in a mod… (1) ; l. 4177 « Your rank-one steering worked, it was just wea… (1) ; l. 4222 « Persona vectors only monitor — they can't be u… (3) ; l. 4264 13 · « Tell us about a time an experiment failed… (1) ; l. 4350 19 · « A model behaves differently when it belie… (5)
- `volet11_21_a_52` — FR : l. 4156 22 · « How would you tell that a model is being … (1) ; l. 4273 29 · « Can you read a model's personality in its… (10) ; l. 4316 31 · « How do you stop a model from learning a b… (2) ; l. 4408 35 · « Can we build a lie detector for language … (1) ; l. 4643 47 · « You have one experiment and a month. What… (2) ; l. 4657 48 · « Training a model on one narrow bad behavi… (1)
  — EN : l. 4429 22 · « How would you tell that a model is being … (1) ; l. 4558 29 · « Can you read a model's personality in its… (10) ; l. 4601 31 · « How do you stop a model from learning a b… (2) ; l. 4676 34 · « Can automated researchers do alignment re… (1) ; l. 4699 35 · « Can we build a lie detector for language … (1) ; l. 4928 46 · « Where does the alignment of a model actua… (1) ; l. 4946 47 · « You have one experiment and a month. What… (2) ; l. 4961 48 · « Training a model on one narrow bad behavi… (2)
- `volet11_53_et_fin` — FR : l. 4776 56 · « How would you know a model is faking alig… (1) ; l. 4991 A7 · « A colleague shows you a beautiful steerin… (1) ; l. 5202 B7 · « Three methods prevent a model from learni… (5) ; l. 5223 B8 · « Build a suite of models with the same cap… (2) ; l. 5336 B13 · « Can honesty be trained rather than detec… (2)
  — EN : l. 5087 56 · « How would you know a model is faking alig… (1) ; l. 5313 A7 · « A colleague shows you a beautiful steerin… (1) ; l. 5527 B7 · « Three methods prevent a model from learni… (3) ; l. 5548 B8 · « Build a suite of models with the same cap… (2) ; l. 5661 B13 · « Can honesty be trained rather than detec… (1)

---

## 9. J-lens et espace de travail — *The J-lens and the workspace*

- **Maison** : tranche `volet2_A_a_D` ; FR : volet 2, C bis · l'espace de travail et le J-lens (après « Le test, tel qu'il se dit ») ; EN : Part 2, C bis · the workspace and the J-lens (after "The test, as it is said").
- **Limites** : 7 ; **parades** : 7.
- **Ancre FR** (ligne 587 de la v3.5 FR ; l'encadré s'insère juste après) :

~~~text
d'après le prédicteur mesuré d'abord. **Ce qui reste à dire à l'oral** : le lens est approximatif et incomplet, les auteurs le disent ; c'est l'endroit du doute.
~~~

- **Ancre EN** (ligne 675 de la v3.5 EN) :

~~~text
according to the predictor measured first. **What remains to say out loud**: the lens is approximate and incomplete, the authors say so; that is where the doubt lies.
~~~

**Encadré complet, français :**

~~~markdown
> **⚠ Limites et parades — J-lens et espace de travail** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Le lens ne capture l'espace de travail que « only approximately and incompletely », et seulement pour des concepts d'un seul token. *(source : fiche 1 ; cours, volet 2, C bis)*
>   **Parade :** Lire un concept de plusieurs tokens sur un jeu de tokens, ou par l'extension multi-token de l'annexe, et dire laquelle. *(source : cours, volet 2, C bis ; programme, partie 3)*
> - **Limite :** Ce qui passe sous l'espace de travail lui échappe : « A sufficiently practiced misaligned behavior might do likewise ». *(source : fiche 1 ; passation, §5.2)*
>   **Parade :** Une étiquette qui ne dépend d'aucune lecture interne ; trois sondes (flux entier, part dans l'espace de travail, complément) ; un organisme entraîné à l'action par réflexe, sur des exemples courts sans raisonnement, comme cas connu de l'angle mort ; la propension rééchantillonnée depuis chaque point de décision ; un crosscoder entre la base et chaque bras. *(source : passation, §5.2)*
> - **Limite :** Il n'a été montré que sur Claude ; un rapport trouve, sur des modèles ouverts, des échanges qui ne font basculer la réponse que dans 6,3 à 11,1 % des cas, contre 54 à 70 % chez Anthropic. *(source : fiche 1 ; rapport d'antériorité 5 du 2 octobre — rapport, lu par résumé, non vérifié)*
>   **Parade :** Une porte : reproduire d'abord l'échange d'un concept d'un seul token sur le modèle ouvert ; sinon un tuned lens déclaré comme proxy, et la thèse n'est pas testée au sens du papier. *(source : programme, parties 3 et 8 ; cours, volet 2, C bis)*
> - **Limite :** Présence n'est pas cause : le langage est présent dans le lens sur quatre tâches, causal sur deux ; et la part J-space d'une direction est petite même quand elle porte l'effet. *(source : fiche 1 ; cours, volet 2, C bis)*
>   **Parade :** Comparer l'échange de la seule part J-space à celui du seul reste, une fois l'échange validé sur les pays. *(source : cours, volet 2, C bis ; cours, volet 6, §8)*
> - **Limite :** La chute de la verbalisation après l'ablation ne montre pas que la conscience d'évaluation a été retirée. *(source : fiche 1 ; contre-lecture des fiches)*
>   **Parade :** Un critère comportemental et une sonde latente, avec un bras de directions neutres du lens à dégradation appariée. *(source : programme, partie 8 ; cours, volet 2, C bis, K72)*
> - **Limite :** Le détecteur de conscience d'évaluation tiré du lens n'est validé que contre des étiquettes de NLA, jamais contre l'écart réel/test ni sur des indices tenus à part. *(source : fiche 1)*
>   **Parade :** Le valider contre l'écart réel/test et sur des indices tenus à part. *(source : fiche 1)*
> - **Limite :** Le lens dépend des poids ; la charge peut être lue sur le sous-espace même que le retrait a trouvé ; et « charge » désigne trois grandeurs différentes selon les textes. *(source : cours, volet 2, C bis ; cours, volet 6, §6)*
>   **Parade :** Recalculer le lens après tout entraînement ; des jeux d'items disjoints ; geler d'abord le prédicteur principal et dire lequel. *(source : cours, volet 2, C bis ; cours, volet 6, §6)*
~~~

**Encadré complet, anglais :**

~~~markdown
> **⚠ Limits and workarounds — The J-lens and the workspace** *(v3.6, 2 October 2026)*
>
> - **Limit:** The lens captures the workspace "only approximately and incompletely", and only for single-token concepts. *(source: reading sheet 1; course, Part 2, C bis)*
>   **Workaround:** Read a multi-token concept on a token set, or through the appendix's multi-token extension, and say which. *(source: course, Part 2, C bis; programme, part 3)*
> - **Limit:** What runs below the workspace escapes it: "A sufficiently practiced misaligned behavior might do likewise". *(source: reading sheet 1; handover, §5.2)*
>   **Workaround:** A label that depends on no internal reading; three probes (whole stream, workspace share, complement); an organism trained to act by reflex, on short examples without reasoning, as the known case of the blind spot; propensity resampled from each decision point; a crosscoder between the base and each arm. *(source: handover, §5.2)*
> - **Limit:** It has been shown only on Claude; a report finds, on open models, swaps that flip the answer in only 6.3 to 11.1% of cases, against 54 to 70% at Anthropic. *(source: reading sheet 1; prior-art report 5 of 2 October — report, read by summary, unverified)*
>   **Workaround:** A gate: first reproduce the swap of a single-token concept on the open model; otherwise a tuned lens declared as a proxy, and the thesis is not tested in the paper's sense. *(source: programme, parts 3 and 8; course, Part 2, C bis)*
> - **Limit:** Presence is not cause: language is present in the lens on four tasks, causal on two; and a direction's J-space share is small even when it carries the effect. *(source: reading sheet 1; course, Part 2, C bis)*
>   **Workaround:** Compare swapping the J-space share alone with swapping the remainder alone, once the swap is validated on countries. *(source: course, Part 2, C bis; course, Part 6, §8)*
> - **Limit:** The drop in verbalization after the ablation does not show that evaluation awareness was removed. *(source: reading sheet 1; counter-reading of the sheets)*
>   **Workaround:** A behavioural criterion and a latent probe, with an arm of neutral lens directions at matched degradation. *(source: programme, part 8; course, Part 2, C bis, K72)*
> - **Limit:** The lens-based evaluation-awareness detector is validated only against NLA labels, never against the real/test gap nor on held-out cues. *(source: reading sheet 1)*
>   **Workaround:** Validate it against the real/test gap and on held-out cues. *(source: reading sheet 1)*
> - **Limit:** The lens depends on the weights; loading may be read on the very subspace the removal found; and "loading" names three different quantities depending on the text. *(source: course, Part 2, C bis; course, Part 6, §6)*
>   **Workaround:** Recompute the lens after any training; disjoint item sets; freeze the main predictor first and say which. *(source: course, Part 2, C bis; course, Part 6, §6)*
~~~

**Renvoi d'une ligne :**

~~~markdown
> ⚠ **Limites et parades** : J-lens et espace de travail → volet 2, C bis (après « Le test, tel qu'il se dit ») *(v3.6)*
> ⚠ **Limits and workarounds**: J-lens and workspace → Part 2, C bis (after "The test, as it is said") *(v3.6)*
~~~

**Où un renvoi ou un avertissement ponctuel est conseillé :**

- `volets4_5_entete` — FR l. 1267 : Sujet 4 — Mesurer (et faut-il supprimer ?) l’eval-awareness · EN l. 1445 : Topic 4 — Measuring (and should we suppress?) eval-awareness — renvoi.
- `volet6` — FR l. 1499 : 6. Ton programme de recherche, et sa revue d'antériorité · EN l. 1615 : 6. Your research program, and its prior-art review — renvoi.
- `volet6` — FR l. 1578 : 8 · La validité des sondes d'activation hors distribution — pourquoi « validée par interve… · EN l. 1746 : 8 · Out-of-distribution validity of activation probes — why "validated by causal intervent… — renvoi.
- `volet11_1_a_20` — FR l. 3775 : 6 · « How would you detect misalignment in a model you can't fully trust? » *(question rée… · EN l. 4024 : 6 · « How would you detect misalignment in a model you can't fully trust? » *(question rée… — renvoi.
- `volet11_1_a_20` — FR l. 4079 : 19 · « A model behaves differently when it believes it is being tested. What do you do wit… · EN l. 4350 : 19 · « A model behaves differently when it believes it is being tested. What do you do wit… — renvoi.
- `volet11_53_et_fin` — FR l. 5141 : B4 · « How would you measure evaluation awareness that the model never verbalizes? » · EN l. 5466 : B4 · « How would you measure evaluation awareness that the model never verbalizes? » — renvoi.

**Où il revient** (relevé automatique, motifs FR `J-lens|J-space|espace de travail|workspace|lens` / EN `J-lens|J-space|workspace|lens` ; sections, avec le nombre de lignes touchées) :

- `tete_volet1` — FR : l. 1 COURS D'ALIGNEMENT — VERSION FUSIONNÉE v3.5 — 27… (1)
  — EN : l. 21 ALIGNMENT COURSE — MERGED VERSION v3.5 — Septemb… (1)
- `volet_M` — FR : l. 345 M8 · La forme qui sert la logique (1)
  — EN : l. 412 M8 · The form that serves the logic (1)
- `volet2_A_a_D` — FR : l. 523 Cas d'application — sondes et pilotage : « How w… (1) ; l. 559 C bis · L'espace de travail (J-space) et le J-le… (10) ; l. 589 Cas d'application — l'espace de travail et le J-… (5)
  — EN : l. 611 Worked case — probes and steering: "How would yo… (1) ; l. 647 C bis · The workspace (J-space) and the J-lens —… (10) ; l. 677 Worked case — the workspace and the J-lens: "An … (6)
- `volets4_5_entete` — FR : l. 1219 1. La thèse-signature : l’écart représentation–c… (1)
  — EN : l. 1389 1. The signature thesis: the representation–caus… (1)
- `volet6` — FR : l. 1376 1. Le format réel de l'entretien, et la structur… (1) ; l. 1499 6. Ton programme de recherche, et sa revue d'ant… (12) ; l. 1578 8 · La validité des sondes d'activation hors dis… (2)
  — EN : l. 1571 1. The real format of the interview, and the str… (1) ; l. 1615 6. Your research program, and its prior-art revi… (14) ; l. 1746 8 · Out-of-distribution validity of activation p… (2)
- `volet10` — FR : l. 3148 Patchscopes: A Unifying Framework for Inspecting… (2) ; l. 3554 AgentDojo: A Dynamic Environment to Evaluate Pro… (1) ; l. 3623 An Adversarial Perspective on Machine Unlearning… (3)
  — EN : l. 3390 Patchscopes: A Unifying Framework for Inspecting… (2) ; l. 3791 AgentDojo: A Dynamic Environment to Evaluate Pro… (1) ; l. 3859 An Adversarial Perspective on Machine Unlearning… (3)
- `volet11_1_a_20` — FR : l. 3673 1 · « Tell us about your work. » — l'ouverture (1)
  — EN : l. 3912 1 · « Tell us about your work. » — l'ouverture (1)
- `volet11_53_et_fin` — FR : l. 4950 A4 · « Your rank-three result is on an 8B model.… (1)
  — EN : l. 5268 A4 · « Your rank-three result is on an 8B model.… (1)

---

## 10. Ablation et projection (directions, sous-espaces) — *Ablation and projection (directions, subspaces)*

- **Maison** : tranche `volet2_A_a_D` ; FR : volet 2, §D · interprétabilité mécaniste (paragraphe « La méthode ») ; EN : Part 2, §D · mechanistic interpretability (paragraph "The method").
- **Limites** : 6 ; **parades** : 6.
- **Ancre FR** (ligne 629 de la v3.5 FR ; l'encadré s'insère juste après) :

~~~text
La méthode. Là où le probing demande « le concept est-il présent comme direction ? », l’interprétabilité mécaniste demande « quel est l e calcul réel — quels composants calculent quoi, et comment se connectent-ils ? ». Son obstacle propre est la superposition : un même neurone ou une même direction mélange plusieurs concepts (on dit qu’il est polysémantique), si bien qu’on ne peut pas lire un neurone comme « le neurone du chien ». L’outil central pour défaire ce mélange est le sparse autoencoder (SAE) : un dictionnaire appris qui décompose l’activation en de très nombreuses features parcimonieuses et plus monosémantiques, chacune correspondant idéalement à un seul concept interprétable. Pour comprendre non plus quoi mais comment, on trace des circuits (ou attribution graphs) : on suit comment les features des premières couches alimentent celles des suivantes pour produire la sortie. Et l’on prouve la nécessité d’un composant par ablation : on le désactive et l’on regarde ce qui casse.
~~~

- **Ancre EN** (ligne 718 de la v3.5 EN) :

~~~text
The method. Where probing asks "is the concept present as a direction?", mechanistic interpretability asks "what is the actual computation — which components compute what, and how do they connect?". Its specific obstacle is superposition: a single neuron or a single direction mixes several concepts (it is said to be polysemantic), so that one cannot read a neuron as "the dog neuron". The central tool for undoing this mixture is the sparse autoencoder (SAE): a learned dictionary that decomposes the activation into a very large number of sparse, more monosemantic features, each ideally corresponding to a single interpretable concept. To understand no longer what but how, we trace circuits (or attribution graphs): we follow how the features of the early layers feed those of later ones to produce the output. And we prove that a component is necessary by ablation: we deactivate it and look at what breaks.
~~~

**Encadré complet, français :**

~~~markdown
> **⚠ Limites et parades — Ablation et projection (directions, sous-espaces)** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Retirer une direction abîme aussi le modèle : un effet d'ablation dit la nécessité, pas la spécificité. *(source : cours, volet M, M4)*
>   **Parade :** Des sous-espaces aléatoires de même rang, comparés à dégradation appariée, par retrait partiel ou par une courbe de l'effet contre la dégradation. *(source : cours, volet 2, C bis ; programme, partie 7)*
> - **Limite :** Une ablation peut déplacer un corrélat : ton sous-espace de rang trois adoucit les verdicts négatifs avec ou sans pression. *(source : cours, volet 6, §2 ; README du dépôt)*
>   **Parade :** Le bras sans pression ; et retirer chaque direction seule, avec et sans pression. *(source : cours, volet M, M4 ; cours, volet 6, §6)*
> - **Limite :** Un effet obtenu sur des générations stockées, jugées à travers une fenêtre tronquée, peut ne pas revenir sur des générations fraîches. *(source : README du dépôt ; cours, volet 6, §2)*
>   **Parade :** Des générations fraîches, à graines appariées, gardées en texte complet et jugées sur la réponse entière. *(source : cours, volet 6, §6 ; cours, volet 11, réponse A7)*
> - **Limite :** Circularité : le sous-espace est extrait sur les items qui servent ensuite à l'évaluer. *(source : README du dépôt)*
>   **Parade :** Extraire sur un jeu d'items disjoint. *(source : README du dépôt ; cours, volet 2, C bis)*
> - **Limite :** Un contraste rang un contre rang trois tiré d'expériences séparées ne dit pas la courbe, et le seul balayage fait dans une même expérience n'est pas monotone. *(source : cours, volet 6, §2)*
>   **Parade :** Un balayage de rang dans une même expérience, sur des sous-espaces emboîtés, monotonie vérifiée et non supposée. *(source : cours, volet 6, §6 ; cours, volet 2, C bis)*
> - **Limite :** Un mécanisme à une direction peut être enfoui sous des directions de plus forte variance, et passer pour réparti. *(source : cours, volet 6, §6)*
>   **Parade :** Deux ordres de retrait, par variance et par effet causal. *(source : cours, volet 6, §6)*
~~~

**Encadré complet, anglais :**

~~~markdown
> **⚠ Limits and workarounds — Ablation and projection (directions, subspaces)** *(v3.6, 2 October 2026)*
>
> - **Limit:** Removing a direction also damages the model: an ablation effect shows necessity, not specificity. *(source: course, Part M, M4)*
>   **Workaround:** Random subspaces of the same rank, compared at matched degradation, by partial removal or by a curve of effect against degradation. *(source: course, Part 2, C bis; programme, part 7)*
> - **Limit:** An ablation can move a correlate: your rank-three subspace softens negative verdicts with or without pressure. *(source: course, Part 6, §2; repository README)*
>   **Workaround:** The no-pressure arm; and remove each direction alone, with and without pressure. *(source: course, Part M, M4; course, Part 6, §6)*
> - **Limit:** An effect obtained on stored generations, judged through a truncated window, may not come back on fresh generations. *(source: repository README; course, Part 6, §2)*
>   **Workaround:** Fresh generations, seed-matched, kept as full text and judged on the whole answer. *(source: course, Part 6, §6; course, Part 11, answer A7)*
> - **Limit:** Circularity: the subspace is extracted on the items later used to evaluate it. *(source: repository README)*
>   **Workaround:** Extract on a disjoint item set. *(source: repository README; course, Part 2, C bis)*
> - **Limit:** A rank-one versus rank-three contrast from separate experiments does not give the curve, and the only sweep run within one experiment is not monotonic. *(source: course, Part 6, §2)*
>   **Workaround:** A rank sweep within one experiment, on nested subspaces, with monotonicity checked, not assumed. *(source: course, Part 6, §6; course, Part 2, C bis)*
> - **Limit:** A one-direction mechanism can be buried under higher-variance directions, and pass for a distributed one. *(source: course, Part 6, §6)*
>   **Workaround:** Two removal orders, by variance and by causal effect. *(source: course, Part 6, §6)*
~~~

**Renvoi d'une ligne :**

~~~markdown
> ⚠ **Limites et parades** : ablation et projection → volet 2, §D (après « La méthode ») *(v3.6)*
> ⚠ **Limits and workarounds**: ablation and projection → Part 2, §D (after "The method") *(v3.6)*
~~~

**Où un renvoi ou un avertissement ponctuel est conseillé :**

- `volet2_A_a_D` — FR l. 589 : Cas d'application — l'espace de travail et le J-lens : « An internal "this is fake" signal… · EN l. 677 : Worked case — the workspace and the J-lens: "An internal "this is fake" signal appears bef… — renvoi.
- `volets4_5_entete` — FR l. 1257 : Sujet 2 — Fiabilité du steering : quand une direction suffit-elle ? · EN l. 1435 : Topic 2 — Steering reliability: when does a direction suffice? — renvoi.
- `volets4_5_entete` — FR l. 1261 : Sujet 3 — Décomposer un concept diffus en features actionnables · EN l. 1439 : Topic 3 — Decomposing a diffuse concept into actionable features — renvoi.
- `volet6` — FR l. 1402 : 2. Tes résultats, tels que ton dossier les porte au 14 septembre, corrigés le 27 par la pi… · EN l. 1579 : 2. Your results, as your dossier carries them on September 14, corrected on the 27th by th… — renvoi.
- `volet6` — FR l. 1499 : 6. Ton programme de recherche, et sa revue d'antériorité · EN l. 1615 : 6. Your research program, and its prior-art review — renvoi.
- `volet11_1_a_20` — FR l. 3673 : 1 · « Tell us about your work. » — l'ouverture · EN l. 3912 : 1 · « Tell us about your work. » — l'ouverture — renvoi.
- `volet11_1_a_20` — FR l. 3704 : 2 · « What did your rank-three ablation actually show? » · EN l. 3945 : 2 · « What did your rank-three ablation actually show? » — renvoi.
- `volet11_1_a_20` — FR l. 3727 : 3 · « And rank one? Didn't a single direction work? » · EN l. 3970 : 3 · « And rank one? Didn't a single direction work? » — renvoi.
- `volet11_1_a_20` — FR l. 3747 : 4 · « Did it replicate? » · EN l. 3992 : 4 · « Did it replicate? » — renvoi.
- `volet11_53_et_fin` — FR l. 4950 : A4 · « Your rank-three result is on an 8B model. Why should we believe anything about it t… · EN l. 5268 : A4 · « Your rank-three result is on an 8B model. Why should we believe anything about it t… — renvoi.

**Où il revient** (relevé automatique, motifs FR `ablat|projet|projection|retrait|retirer` / EN `ablat|project|removal|remov` ; sections, avec le nombre de lignes touchées) :

- `volet_M` — FR : l. 257 M4 · Le contrôle : ce qu'il écarte, et il doit s… (2) ; l. 345 M8 · La forme qui sert la logique (2) ; l. 365 M9 · Un cas complet, avant et après : la premièr… (2)
  — EN : l. 324 M4 · The control: what it rules out, and it must… (4) ; l. 365 M5 · The null and the known case (1) ; l. 412 M8 · The form that serves the logic (2) ; l. 432 M9 · A complete case, before and after: the firs… (3)
- `volet2_A_a_D` — FR : l. 513 C. Méthodes sur activations — probing & steering… (1) ; l. 559 C bis · L'espace de travail (J-space) et le J-le… (7) ; l. 589 Cas d'application — l'espace de travail et le J-… (5) ; l. 627 D. Interprétabilité mécaniste — ouvrir la boîte … (1)
  — EN : l. 519 A. Testbeds & model organisms — manufacturing th… (1) ; l. 600 C. Methods on activations — probing & steering (… (1) ; l. 647 C bis · The workspace (J-space) and the J-lens —… (8) ; l. 677 Worked case — the workspace and the J-lens: "An … (6) ; l. 715 D. Mechanistic interpretability — opening the bo… (1)
- `volet2_E_a_I` — FR : l. 805 Cas d'application — robustesse adverse et mésusa… (1) ; l. 834 I. Interventions d’entraînement & unlearning — c… (1) ; l. 842 Cas d'application — interventions d'entraînement… (2)
  — EN : l. 927 I. Training interventions & unlearning — changin… (2) ; l. 936 Worked case — training interventions and unlearn… (4)
- `volet3` — FR : l. 1029 6. Le domaine « divers » : désapprentissage et g… (1)
  — EN : l. 1045 2. Evaluating alignment (1) ; l. 1155 6. The "miscellaneous" domain: unlearning and mu… (1)
- `volets4_5_entete` — FR : l. 1219 1. La thèse-signature : l’écart représentation–c… (1) ; l. 1251 A. Tes sujets FORT — ta thèse peut être la colon… (2) ; l. 1285 B. Leurs sujets — méthodothèque, dosage léger ou… (1)
  — EN : l. 1254 The key papers, told one by one (2) ; l. 1389 1. The signature thesis: the representation–caus… (1) ; l. 1428 A. Your STRONG topics — your thesis can be the b… (2) ; l. 1463 B. Their topics — method toolkit, light or zero … (1) ; l. 1506 The papers — four levels (1)
- `volet6` — FR : l. 1402 2. Tes résultats, tels que ton dossier les porte… (5) ; l. 1458 4. La page « Recommended Directions » et ses sei… (1) ; l. 1499 6. Ton programme de recherche, et sa revue d'ant… (5) ; l. 1578 8 · La validité des sondes d'activation hors dis… (1)
  — EN : l. 1579 2. Your results, as your dossier carries them on… (4) ; l. 1597 4. The "Recommended Directions" page and its six… (1) ; l. 1603 5. The work of the Fellows program, 2025-2026 — … (1) ; l. 1615 6. Your research program, and its prior-art revi… (6) ; l. 1676 7. What these supplements change in Parts 1 to 5 (1) ; l. 1746 8 · Out-of-distribution validity of activation p… (1)
- `volet7_B_et_D` — FR : l. 1729 F·24 · Strengthening Red Teams : A Modular Scaff… (2) ; l. 1901 F·31 · Persona Vectors — Chen, Arditi (Fellows, … (1) ; l. 2000 F·36 · Beyond Data Filtering : Knowledge Localiz… (1)
  — EN : l. 1855 F·23 · SLEIGHT-Bench : Finding Blind Spots in AI… (1) ; l. 1894 F·24 · Strengthening Red Teams : A Modular Scaff… (2) ; l. 1977 F·30 · CHIVE — Would This Change Your Answer? — … (1) ; l. 2066 F·31 · Persona Vectors — Chen, Arditi (Fellows, … (1) ; l. 2093 F·32 · Subliminal Learning — Cloud, Le (Fellows)… (3) ; l. 2126 F·38 · Agentic Misalignment — Lynch (Fellows, 1s… (1) ; l. 2165 F·36 · Beyond Data Filtering : Knowledge Localiz… (1) ; l. 2186 F·26 · Removing Sandbagging in LLMs by Training … (1)
- `volet7_A_et_C` — FR : l. 2224 F·7 · Contrastive Activation Addition et Inferen… (3) ; l. 2472 F·17 · L'unlearning mis à l'épreuve (Deeb et Rog… (1)
  — EN : l. 2206 F·1 · Sleeper Agents (Hubinger et al., Anthropic… (2) ; l. 2358 F·7 · Contrastive Activation Addition and Infere… (3) ; l. 2582 F·16 · Constitutional AI (Bai et al., Anthropic,… (1) ; l. 2606 F·17 · L'unlearning mis à l'épreuve (Deeb and Ro… (4)
- `volets8_9` — FR : l. 2912 9 · Miscellaneous (1)
  — EN : l. 2804 PART 8 — References, in the order of the sheets (1) ; l. 3069 9 · Miscellaneous (1) ; l. 3085 10 · The overall reading, in three sentences for… (1)
- `volet10` — FR : l. 3096 Monitor: An AI-Driven Observability Interface — … (2) ; l. 3106 Interpreting the Second-Order Effects of Neurons… (2) ; l. 3118 Chain-of-Thought Prompting Elicits Reasoning in … (3) ; l. 3138 SelfIE: Self-Interpretation of Large Language Mo… (2) ; l. 3158 Vector-ICL: In-context Learning with Continuous … (1) ; l. 3233 Testing Language Model Agents Safely in the Wild… (2) ; l. 3347 Recursively Summarizing Books with Human Feedbac… (1) ; l. 3367 Debate Helps Supervise Unreliable Experts — Juli… (1) ; l. 3379 On scalable oversight with weak LLMs judging str… (1) ; l. 3623 An Adversarial Perspective on Machine Unlearning… (3) ; … (+1 sections)
  — EN : l. 3189 0 · What was read, and how (1) ; l. 3223 In the sheets (14) (1) ; l. 3241 Descriptions that are correct but incomplete (9) (1) ; l. 3338 Monitor: An AI-Driven Observability Interface — … (3) ; l. 3348 Interpreting the Second-Order Effects of Neurons… (2) ; l. 3360 Chain-of-Thought Prompting Elicits Reasoning in … (3) ; l. 3380 SelfIE: Self-Interpretation of Large Language Mo… (2) ; l. 3400 Vector-ICL: In-context Learning with Continuous … (4) ; l. 3473 Testing Language Model Agents Safely in the Wild… (2) ; l. 3586 Recursively Summarizing Books with Human Feedbac… (1) ; … (+5 sections)
- `volet11_1_a_20` — FR : l. 3656 VOLET 11 — Les réponses complètes (v2.3, 23 sept… (1) ; l. 3673 1 · « Tell us about your work. » — l'ouverture (3) ; l. 3704 2 · « What did your rank-three ablation actually… (3) ; l. 3727 3 · « And rank one? Didn't a single direction wo… (2) ; l. 3747 4 · « Did it replicate? » (1) ; l. 3809 7 · « How would you prevent bad actors from misa… (1) ; l. 3904 « Your probes hit ninety-nine percent, so defere… (3) ; l. 3946 « The deference subspace you found — that's what… (5) ; l. 3971 « Persona vectors only monitor — they can't be u… (1) ; l. 4001 12 · « Why Anthropic? » (1) ; … (+1 sections)
  — EN : l. 3895 PART 11 — The complete answers (v2.3, 23 Septemb… (1) ; l. 3912 1 · « Tell us about your work. » — l'ouverture (4) ; l. 3945 2 · « What did your rank-three ablation actually… (4) ; l. 3970 3 · « And rank one? Didn't a single direction wo… (3) ; l. 3992 4 · « Did it replicate? » (1) ; l. 4057 7 · « How would you prevent bad actors from misa… (1) ; l. 4155 « Your probes hit ninety-nine percent, so defere… (4) ; l. 4197 « The deference subspace you found — that's what… (5) ; l. 4222 « Persona vectors only monitor — they can't be u… (1) ; l. 4252 12 · « Why Anthropic? » (1) ; … (+2 sections)
- `volet11_21_a_52` — FR : l. 4273 29 · « Can you read a model's personality in its… (1) ; l. 4316 31 · « How do you stop a model from learning a b… (2) ; l. 4451 37 · « How strong does a red team have to be, an… (1) ; l. 4545 42 · « When a model reward-hacks, what is actual… (1) ; l. 4625 46 · « Where does the alignment of a model actua… (2) ; l. 4657 48 · « Training a model on one narrow bad behavi… (2) ; l. 4676 49 · « Training a strong model on labels from a … (1) ; l. 4709 51 · « Given a model that already knows somethin… (2)
  — EN : l. 4517 27 · « When an autonomous agent's goals are bloc… (1) ; l. 4558 29 · « Can you read a model's personality in its… (1) ; l. 4579 30 · « Can a trait be transmitted through data t… (2) ; l. 4601 31 · « How do you stop a model from learning a b… (2) ; l. 4622 32 · « Where do monitors fail, and how would you… (1) ; l. 4745 37 · « How strong does a red team have to be, an… (1) ; l. 4767 38 · « Does interpretability actually help expla… (1) ; l. 4848 42 · « When a model reward-hacks, what is actual… (1) ; l. 4928 46 · « Where does the alignment of a model actua… (2) ; l. 4961 48 · « Training a model on one narrow bad behavi… (2) ; … (+2 sections)
- `volet11_53_et_fin` — FR : l. 4910 A1 · « Which team would you want to join — Align… (4) ; l. 5016 A9 à A17 · Neuf questions moins probables, en ré… (2) ; l. 5161 B5 · « The directions page calls one setting "un… (3) ; l. 5202 B7 · « Three methods prevent a model from learni… (5)
  — EN : l. 5225 A1 · « Which team would you want to join — Align… (5) ; l. 5341 A9 à A17 · Neuf questions moins probables, en ré… (2) ; l. 5486 B5 · « The directions page calls one setting "un… (3) ; l. 5527 B7 · « Three methods prevent a model from learni… (5)

---

## 11. Crosscoders et comparaison de modèles — *Crosscoders and model diffing*

- **Maison** : tranche `volet2_A_a_D` ; FR : volet 2, §D · cas d'application K64 (fin du cas) ; EN : Part 2, §D · worked case K64 (end of the case).
- **Limites** : 4 ; **parades** : 4.
- **Ancre FR** (ligne 665 de la v3.5 FR ; l'encadré s'insère juste après) :

~~~text
produces equally well, while random directions missed it, I'd drop the bet. »*
~~~

- **Ancre EN** (ligne 754 de la v3.5 EN) :

~~~text
produces equally well, while random directions missed it, I'd drop the bet."*
~~~

**Encadré complet, français :**

~~~markdown
> **⚠ Limites et parades — Crosscoders et comparaison de modèles** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Les features trouvées varient d'un entraînement à l'autre. *(source : cours, volet 2, §D, K64)*
>   **Parade :** Plusieurs graines : un gagnant de hasard changerait d'une graine à l'autre. *(source : cours, volet 2, §D, K64)*
> - **Limite :** Un dictionnaire décompose des activations, pas des mécanismes : une différence trouvée entre deux modèles décrit, elle ne cause pas. *(source : fiche 5)*
>   **Parade :** Tester causalement chaque différence retenue, contre des directions aléatoires à dommage apparié. *(source : cours, volet 2, §D, K64 ; cours, volet M, M4)*
> - **Limite :** Il hérite des limites des dictionnaires, à commencer par l'erreur de reconstruction. *(source : cours, volet 4, Monosemanticity ; README du dépôt)*
>   **Parade :** Rapporter la part laissée au résidu, et lire le signal sur la reconstruction et sur le résidu. *(source : README du dépôt)*
> - **Limite :** Dans le programme, le crosscoder n'est qu'une proposition, mesure secondaire et exploratoire. *(source : passation, §5.2)*
>   **Parade :** L'étiqueter exploratoire tant qu'il n'est pas pré-enregistré. *(source : passation, §5.2 ; programme, partie 7)*
~~~

**Encadré complet, anglais :**

~~~markdown
> **⚠ Limits and workarounds — Crosscoders and model diffing** *(v3.6, 2 October 2026)*
>
> - **Limit:** The features found vary from one training run to another. *(source: course, Part 2, §D, K64)*
>   **Workaround:** Several seeds: a chance winner would change from seed to seed. *(source: course, Part 2, §D, K64)*
> - **Limit:** A dictionary decomposes activations, not mechanisms: a difference found between two models describes, it does not cause. *(source: reading sheet 5)*
>   **Workaround:** Test each retained difference causally, against random directions at matched damage. *(source: course, Part 2, §D, K64; course, Part M, M4)*
> - **Limit:** It inherits the limits of dictionaries, starting with reconstruction error. *(source: course, Part 4, Monosemanticity; repository README)*
>   **Workaround:** Report the share left in the residual, and read the signal on the reconstruction and on the residual. *(source: repository README)*
> - **Limit:** In the programme, the crosscoder is only a proposal, a secondary and exploratory measure. *(source: handover, §5.2)*
>   **Workaround:** Label it exploratory until it is preregistered. *(source: handover, §5.2; programme, part 7)*
~~~

**Renvoi d'une ligne :**

~~~markdown
> ⚠ **Limites et parades** : crosscoders et comparaison de modèles → volet 2, §D (fin du cas d'application K64) *(v3.6)*
> ⚠ **Limits and workarounds**: crosscoders and model diffing → Part 2, §D (end of worked case K64) *(v3.6)*
~~~

**Où un renvoi ou un avertissement ponctuel est conseillé :**

- (aucun au-delà de sa maison)

**Où il revient** (relevé automatique, motifs FR `crosscoder|diffing|transcod` / EN `crosscoder|diffing|transcod` ; sections, avec le nombre de lignes touchées) :

- `volet2_A_a_D` — FR : l. 635 Cas d'application — l'interprétabilité mécaniste… (1)
  — EN : l. 724 Worked case — mechanistic interpretability: "Two… (1)
- `volet7_A_et_C` — FR : l. 2274 F·9 · Circuit Tracing / On the Biology of a Larg… (1)
  — EN : l. 2408 F·9 · Circuit Tracing / On the Biology of a Larg… (1)

---

## 12. Débat et supervision évolutive — *Debate and scalable oversight*

- **Maison** : tranche `volet2_E_a_I` ; FR : volet 2, §E · supervision évolutive (après « En pratique — Debate ») ; EN : Part 2, §E · scalable oversight (after "In practice — Debate").
- **Limites** : 4 ; **parades** : 2.
- **Ancre FR** (ligne 673 de la v3.5 FR ; l'encadré s'insère juste après) :

~~~text
En pratique — Debate (Khan et al.). Le but était de tester empiriquement si le debate aide un juge non expert à atteindre la vérité. Le protocole de debate y répond : sur des questions où le juge n’a pas l’information nécessaire, on fait débattre deux modèles défendant des réponses opposées, et l’on compare la justesse du juge à celle qu’il atteint avec un seul conseiller (la consultancy, qui sert de baseline). Le résultat — des juges plus précis face à des débatteurs plus forts — fournit le premier signe empirique que la structure du débat extrait bien un signal plus fiable, sur un testbed où l’on connaît la bonne réponse.
~~~

- **Ancre EN** (ligne 763 de la v3.5 EN) :

~~~text
In practice — Debate (Khan et al.). The goal was to test empirically whether debate helps a non-expert judge reach the truth. The debate protocol answers this: on questions where the judge lacks the necessary information, two models defending opposite answers are made to debate, and the judge's accuracy is compared with the accuracy it reaches with a single advisor (consultancy, which serves as the baseline). The result — more accurate judges facing stronger debaters — provides the first empirical sign that the debate structure does extract a more reliable signal, on a testbed where the right answer is known.
~~~

**Encadré complet, français :**

~~~markdown
> **⚠ Limites et parades — Débat et supervision évolutive** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** L'argument obfusqué : trop complexe pour être réfuté, même faux. *(source : cours, volet 2, §E)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** Optimiser l'approbation peut rendre plus convaincant à tort : le RLHF a appris aux modèles à persuader des humains de réponses fausses. *(source : cours, volet 2, §E)*
>   **Parade :** Mesurer sur un banc où l'on connaît la bonne réponse. *(source : cours, volet 2, §E)*
> - **Limite :** Le signe empirique vient d'un banc où l'on connaît la réponse ; au-delà de l'expertise humaine, il n'y a plus de référence. *(source : cours, volet 2, §E ; cours, volet 2, clôture)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** Le juge est souvent un modèle : les limites des juges LLM s'appliquent. *(source : fiches, partie B, piège 6)*
>   **Parade :** Un juge scellé et un audit humain (encadré « Juges LLM », volet 6, §2). *(source : programme, partie 3)*
~~~

**Encadré complet, anglais :**

~~~markdown
> **⚠ Limits and workarounds — Debate and scalable oversight** *(v3.6, 2 October 2026)*
>
> - **Limit:** The obfuscated argument: too complex to refute, even when false. *(source: course, Part 2, §E)*
>   **Workaround:** none known; say so.
> - **Limit:** Optimizing approval can make a model wrongly more convincing: RLHF taught models to persuade humans of wrong answers. *(source: course, Part 2, §E)*
>   **Workaround:** Measure on a testbed where the right answer is known. *(source: course, Part 2, §E)*
> - **Limit:** The empirical sign comes from a testbed where the answer is known; beyond human expertise there is no reference left. *(source: course, Part 2, §E; course, Part 2, closing)*
>   **Workaround:** none known; say so.
> - **Limit:** The judge is often a model: the limits of LLM judges apply. *(source: reading sheets, part B, trap 6)*
>   **Workaround:** A sealed judge and a human audit (box "LLM judges", Part 6, §2). *(source: programme, part 3)*
~~~

**Renvoi d'une ligne :**

~~~markdown
> ⚠ **Limites et parades** : débat et supervision évolutive → volet 2, §E (après « En pratique — Debate ») *(v3.6)*
> ⚠ **Limits and workarounds**: debate and scalable oversight → Part 2, §E (after "In practice — Debate") *(v3.6)*
~~~

**Où un renvoi ou un avertissement ponctuel est conseillé :**

- `volet3` — FR l. 977 : 4. L’oversight évolutif — et, en son sein, l’honnêteté · EN l. 1101 : 4. Scalable oversight — and, within it, honesty — renvoi.
- `volets4_5_entete` — FR l. 1307 : Sujet 12 — Scalable oversight / weak-to-strong (FAIBLE) · EN l. 1486 : Topic 12 — Scalable oversight / weak-to-strong (WEAK) — renvoi.
- `volet7_A_et_C` — FR l. 2328 : F·11 · Debate (Irving et al., 2018 ; Khan et al., 2024) — [P·21] · EN l. 2462 : F·11 · Debate (Irving et al., 2018; Khan et al., 2024) — [P·21] — renvoi.
- `volets8_9` — FR l. 2842 : 7 · Scalable oversight — « Can we design oversight mechanisms that will continue to work f… · EN l. 2999 : 7 · Scalable oversight — "Can we design oversight mechanisms that will continue to work fo… — renvoi.
- `volet10` — FR l. 3325 : Scalable oversight › Recursive oversight · EN l. 3564 : Scalable oversight › Recursive oversight — renvoi.

**Où il revient** (relevé automatique, motifs FR `débat|debate|décomposition|prover` / EN `debate|decomposition|prover` ; sections, avec le nombre de lignes touchées) :

- `tete_volet1` — FR : l. 122 Q2. « Quel est, selon toi, le problème non résol… (2)
  — EN : l. 178 Q2. "What, in your view, is the most important u… (2)
- `volet2_E_a_I` — FR : l. 667 E. Oversight évolutif — superviser une tâche qu’… (2)
  — EN : l. 756 E. Scalable oversight — supervising a task you c… (2)
- `volet3` — FR : l. 977 4. L’oversight évolutif — et, en son sein, l’hon… (1) ; l. 1053 PARTIE II — LES ÉQUIPES : qui fait quoi chez (1) ; l. 1103 PARTIE IV — SYNTHÈSE : comment tout s’emboîte, e… (2)
  — EN : l. 1101 4. Scalable oversight — and, within it, honesty (1) ; l. 1180 SECTION II — THE TEAMS: who does what at (1) ; l. 1228 SECTION IV — SYNTHESIS: how everything fits toge… (2)
- `volets4_5_entete` — FR : l. 1139 Representation Engineering (RepE) (Zou et al.) (1) ; l. 1153 Towards puis Scaling Monosemanticity (Anthropic, (1) ; l. 1175 Debate (Khan et al., dans la lignée d’Irving) (2) ; l. 1203 L’unlearning mis à l’épreuve (Deeb et Roger) (1) ; l. 1219 1. La thèse-signature : l’écart représentation–c… (1) ; l. 1326 Les papiers — quatre niveaux (1)
  — EN : l. 1254 The key papers, told one by one (5) ; l. 1389 1. The signature thesis: the representation–caus… (1) ; l. 1506 The papers — four levels (1)
- `volet6` — FR : —
  — EN : l. 1579 2. Your results, as your dossier carries them on… (1) ; l. 1676 7. What these supplements change in Parts 1 to 5 (1)
- `volet7_B_et_D` — FR : l. 1635 F·22 · Diffuse AI Control on Fuzzy Tasks — Terek… (1)
  — EN : l. 1800 F·22 · Diffuse AI Control on Fuzzy Tasks — Terek… (1)
- `volet7_A_et_C` — FR : l. 2200 F·6 · Discovering Latent Knowledge Without Super… (1) ; l. 2249 F·8 · Towards puis Scaling Monosemanticity (Anth… (2) ; l. 2328 F·11 · Debate (Irving et al., 2018 ; Khan et al.… (8) ; l. 2472 F·17 · L'unlearning mis à l'épreuve (Deeb et Rog… (1)
  — EN : l. 2334 F·6 · Discovering Latent Knowledge Without Super… (1) ; l. 2383 F·8 · Towards then Scaling Monosemanticity (Anth… (3) ; l. 2462 F·11 · Debate (Irving et al., 2018; Khan et al.,… (8) ; l. 2606 F·17 · L'unlearning mis à l'épreuve (Deeb and Ro… (1)
- `volets8_9` — FR : l. 2666 VOLET 8 — Références, dans l'ordre des fiches (1) ; l. 2786 5 · Chain-of-thought faithfulness — « When can w… (1) ; l. 2842 7 · Scalable oversight — « Can we design oversig… (5)
  — EN : l. 2804 PART 8 — References, in the order of the sheets (1) ; l. 2943 5 · Chain-of-thought faithfulness — "When can we… (1) ; l. 2999 7 · Scalable oversight — "Can we design oversigh… (5) ; l. 3085 10 · The overall reading, in three sentences for… (4)
- `volet10` — FR : l. 2980 Dans les fiches (14) (2) ; l. 2998 Descriptions justes mais incomplètes (9) (1) ; l. 3106 Interpreting the Second-Order Effects of Neurons… (2) ; l. 3195 Question Decomposition Improves the Faithfulness… (1) ; l. 3327 Self-critiquing models for assisting human evalu… (1) ; l. 3337 Supervising strong learners by amplifying weak e… (3) ; l. 3347 Recursively Summarizing Books with Human Feedbac… (4) ; l. 3357 AI safety via debate — Geoffrey Irving, Paul Chr… (7) ; l. 3367 Debate Helps Supervise Unreliable Experts — Juli… (8) ; l. 3379 On scalable oversight with weak LLMs judging str… (7) ; … (+1 sections)
  — EN : l. 3223 In the sheets (14) (2) ; l. 3241 Descriptions that are correct but incomplete (9) (1) ; l. 3348 Interpreting the Second-Order Effects of Neurons… (2) ; l. 3436 Question Decomposition Improves the Faithfulness… (4) ; l. 3566 Self-critiquing models for assisting human evalu… (1) ; l. 3576 Supervising strong learners by amplifying weak e… (3) ; l. 3586 Recursively Summarizing Books with Human Feedbac… (5) ; l. 3596 AI safety via debate — Geoffrey Irving, Paul Chr… (7) ; l. 3606 Debate Helps Supervise Unreliable Experts — Juli… (8) ; l. 3618 On scalable oversight with weak LLMs judging str… (7) ; … (+1 sections)
- `volet11_53_et_fin` — FR : l. 4747 54 · « What's the most important unsolved proble… (2) ; l. 4910 A1 · « Which team would you want to join — Align… (1) ; l. 4964 A5 · « Isn't sycophancy basically solved by now … (1)
  — EN : l. 5057 54 · « What's the most important unsolved proble… (1) ; l. 5284 A5 · « Isn't sycophancy basically solved by now … (1)

---

## 13. Élicitation non supervisée par cohérence — *Unsupervised elicitation by consistency*

- **Maison** : tranche `volet2_E_a_I` ; FR : volet 2, §E · cas d'application K52 (fin du cas) ; EN : Part 2, §E · worked case K52 (end of the case).
- **Limites** : 4 ; **parades** : 3.
- **Ancre FR** (ligne 709 de la v3.5 FR ; l'encadré s'insère juste après) :

~~~text
alone gave back the truth, I'd drop the bet. »*
~~~

- **Ancre EN** (ligne 799 de la v3.5 EN) :

~~~text
alone gave back the truth, I'd drop the bet."*
~~~

**Encadré complet, français :**

~~~markdown
> **⚠ Limites et parades — Élicitation non supervisée par cohérence** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Elle trouve le trait le plus saillant, pas forcément la vérité, et elle est sensible au prompt. *(source : cours, volet 6, §8 ; cours, volet 4, CCS)*
>   **Parade :** Rendre vérifiable l'invérifiable : implanter un faux fait cohérent, vérifier qu'il a pris, puis lire ce qu'elle rend, avec une copie au vrai fait apparié comme témoin. *(source : cours, volet 2, §E, K52)*
> - **Limite :** Une fausse croyance cohérente l'est autant qu'une vraie : la cohérence seule ne départage pas. *(source : cours, volet 2, §E, K52)*
>   **Parade :** Ancrer la méthode sur des réponses vérifiées, par l'entraînement du facile au difficile, et dire que sans lui elle ne rend que la cohérence. *(source : cours, volet 2, §E, K52)*
> - **Limite :** L'échec peut rester silencieux là où l'évaluation en distribution est impossible. *(source : cours, volet 2, §E, K52)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** Le filtre de l'implant et la méthode peuvent lire la même feature saillante. *(source : cours, volet 2, §E, K52)*
>   **Parade :** L'inférence en aval comme témoin, indépendante de la sonde. *(source : cours, volet 2, §E, K52)*
~~~

**Encadré complet, anglais :**

~~~markdown
> **⚠ Limits and workarounds — Unsupervised elicitation by consistency** *(v3.6, 2 October 2026)*
>
> - **Limit:** It finds the most salient feature, not necessarily the truth, and it is sensitive to the prompt. *(source: course, Part 6, §8; course, Part 4, CCS)*
>   **Workaround:** Make the uncheckable checkable: implant a coherent false fact, check that it took, then read what it returns, with a copy holding a matched true fact as control. *(source: course, Part 2, §E, K52)*
> - **Limit:** A coherent false belief is as coherent as a true one: consistency alone does not decide. *(source: course, Part 2, §E, K52)*
>   **Workaround:** Anchor the method on verified answers, through easy-to-hard training, and say that without it the method returns only consistency. *(source: course, Part 2, §E, K52)*
> - **Limit:** Failure can stay silent where in-distribution evaluation is impossible. *(source: course, Part 2, §E, K52)*
>   **Workaround:** none known; say so.
> - **Limit:** The implant filter and the method may read the same salient feature. *(source: course, Part 2, §E, K52)*
>   **Workaround:** Downstream inference as the control, independent of the probe. *(source: course, Part 2, §E, K52)*
~~~

**Renvoi d'une ligne :**

~~~markdown
> ⚠ **Limites et parades** : élicitation non supervisée → volet 2, §E (fin du cas d'application K52) *(v3.6)*
> ⚠ **Limits and workarounds**: unsupervised elicitation → Part 2, §E (end of worked case K52) *(v3.6)*
~~~

**Où un renvoi ou un avertissement ponctuel est conseillé :**

- `volet3` — FR l. 977 : 4. L’oversight évolutif — et, en son sein, l’honnêteté · EN l. 1101 : 4. Scalable oversight — and, within it, honesty — renvoi.
- `volets4_5_entete` — FR l. 1139 : Representation Engineering (RepE) (Zou et al.) · EN l. 1281 : Representation Engineering (RepE) (Zou et al.) — renvoi.
- `volets4_5_entete` — FR l. 1271 : Sujet 6 — Honnêteté : lire la vérité sans juger la véracité · EN l. 1449 : Topic 6 — Honesty: reading truth without judging veracity — renvoi.
- `volet7_A_et_C` — FR l. 2200 : F·6 · Discovering Latent Knowledge Without Supervision — CCS (Burns et al., 2022) — [P·33] · EN l. 2334 : F·6 · Discovering Latent Knowledge Without Supervision — CCS (Burns et al., 2022) — [P·33] — renvoi.
- `volets8_9` — FR l. 2842 : 7 · Scalable oversight — « Can we design oversight mechanisms that will continue to work f… · EN l. 2999 : 7 · Scalable oversight — "Can we design oversight mechanisms that will continue to work fo… — renvoi.
- `volet10` — FR l. 3287 : AI control › Anomaly detection · EN l. 3527 : AI control › Anomaly detection — renvoi.
- `volet10` — FR l. 3477 : Scalable oversight › Honesty · EN l. 3715 : Scalable oversight › Honesty — renvoi.
- `volet11_21_a_52` — FR l. 4156 : 22 · « How would you tell that a model is being honest when you cannot judge whether its a… · EN l. 4429 : 22 · « How would you tell that a model is being honest when you cannot judge whether its a… — renvoi.

**Où il revient** (relevé automatique, motifs FR `\bCCS\b|non supervis|élicitation` / EN `\bCCS\b|unsupervised|elicitation` ; sections, avec le nombre de lignes touchées) :

- `volet_M` — FR : l. 330 M7 · La plus petite version, le budget, et la cl… (1)
  — EN : l. 397 M7 · The smallest version, the budget, and the c… (1)
- `volet2_A_a_D` — FR : l. 480 B. Évaluations — mesurer une capacité ou une pro… (2)
  — EN : l. 566 B. Evaluations — measuring a capability or a pro… (2)
- `volet2_E_a_I` — FR : l. 675 Cas d'application — la supervision évolutive : «… (4) ; l. 834 I. Interventions d’entraînement & unlearning — c… (2) ; l. 842 Cas d'application — interventions d'entraînement… (1)
  — EN : l. 765 Worked case — scalable oversight: "Would unsuper… (7) ; l. 927 I. Training interventions & unlearning — changin… (2) ; l. 936 Worked case — training interventions and unlearn… (1)
- `volet3` — FR : l. 899 1. Évaluer les capacités (3) ; l. 977 4. L’oversight évolutif — et, en son sein, l’hon… (1) ; l. 1029 6. Le domaine « divers » : désapprentissage et g… (1) ; l. 1077 PARTIE III — LES TRAVAUX DU MOMENT (2025-2026) (1)
  — EN : l. 1020 1. Evaluating capabilities (4) ; l. 1101 4. Scalable oversight — and, within it, honesty (1) ; l. 1155 6. The "miscellaneous" domain: unlearning and mu… (1) ; l. 1202 SECTION III — CURRENT WORK (2025-2026) (1)
- `volets4_5_entete` — FR : l. 1139 Representation Engineering (RepE) (Zou et al.) (2) ; l. 1203 L’unlearning mis à l’épreuve (Deeb et Roger) (2) ; l. 1251 A. Tes sujets FORT — ta thèse peut être la colon… (1) ; l. 1285 B. Leurs sujets — méthodothèque, dosage léger ou… (2) ; l. 1326 Les papiers — quatre niveaux (1)
  — EN : l. 1254 The key papers, told one by one (4) ; l. 1428 A. Your STRONG topics — your thesis can be the b… (1) ; l. 1463 B. Their topics — method toolkit, light or zero … (2) ; l. 1506 The papers — four levels (3)
- `volet6` — FR : l. 1474 5. Les travaux du programme Fellows, 2025-2026 —… (1) ; l. 1578 8 · La validité des sondes d'activation hors dis… (1)
  — EN : l. 1603 5. The work of the Fellows program, 2025-2026 — … (1) ; l. 1676 7. What these supplements change in Parts 1 to 5 (1) ; l. 1746 8 · Out-of-distribution validity of activation p… (2)
- `volet7_B_et_D` — FR : l. 1777 F·29 · Fine-Tuned Lie Detectors Failed to Genera… (1)
  — EN : l. 1942 F·29 · Fine-Tuned Lie Detectors Failed to Genera… (3)
- `volet7_A_et_C` — FR : l. 2200 F·6 · Discovering Latent Knowledge Without Super… (6) ; l. 2352 F·12 · Weak-to-Strong Generalization (Burns et a… (1) ; l. 2400 F·14 · Eliciting Latent Knowledge — le rapport E… (1) ; l. 2472 F·17 · L'unlearning mis à l'épreuve (Deeb et Rog… (2)
  — EN : l. 2334 F·6 · Discovering Latent Knowledge Without Super… (7) ; l. 2486 F·12 · Weak-to-Strong Generalization (Burns et a… (1) ; l. 2534 F·14 · Eliciting Latent Knowledge — the ELK repo… (1) ; l. 2606 F·17 · L'unlearning mis à l'épreuve (Deeb and Ro… (2)
- `volets8_9` — FR : l. 2842 7 · Scalable oversight — « Can we design oversig… (4) ; l. 2912 9 · Miscellaneous (1)
  — EN : l. 2999 7 · Scalable oversight — "Can we design oversigh… (5) ; l. 3069 9 · Miscellaneous (1) ; l. 3085 10 · The overall reading, in three sentences for… (1)
- `volet10` — FR : l. 2980 Dans les fiches (14) (2) ; l. 3299 Eliciting Latent Knowledge from “Quirky” Languag… (2) ; l. 3404 Weak-to-Strong Reasoning — Yuqing Yang, Yan Ma, … (1) ; l. 3416 Evaluating Superhuman Models with Consistency Ch… (1) ; l. 3501 Representation Engineering: A Top-Down Approach … (2) ; l. 3521 Inference-Time Intervention: Eliciting Truthful … (2) ; l. 3531 Cognitive Dissonance: Why Do Language Model Outp… (1) ; l. 3643 Do Unlearning Methods Remove Information from La… (1)
  — EN : l. 3223 In the sheets (14) (3) ; l. 3456 Bias-Augmented Consistency Training Reduces Bias… (1) ; l. 3529 Mechanistic anomaly detection and ELK — Paul Chr… (1) ; l. 3539 Eliciting Latent Knowledge from “Quirky” Languag… (2) ; l. 3643 Weak-to-Strong Reasoning — Yuqing Yang, Yan Ma, … (1) ; l. 3655 Evaluating Superhuman Models with Consistency Ch… (1) ; l. 3705 Balancing Label Quantity and Quality for Scalabl… (1) ; l. 3739 Representation Engineering: A Top-Down Approach … (2) ; l. 3759 Inference-Time Intervention: Eliciting Truthful … (2) ; l. 3769 Cognitive Dissonance: Why Do Language Model Outp… (1) ; … (+1 sections)
- `volet11_21_a_52` — FR : l. 4156 22 · « How would you tell that a model is being … (3) ; l. 4408 35 · « Can we build a lie detector for language … (1) ; l. 4676 49 · « Training a strong model on labels from a … (1)
  — EN : l. 4429 22 · « How would you tell that a model is being … (3) ; l. 4699 35 · « Can we build a lie detector for language … (1) ; l. 4981 49 · « Training a strong model on labels from a … (1)
- `volet11_53_et_fin` — FR : l. 5246 B9 · « How would you build a safety case that a … (3) ; l. 5336 B13 · « Can honesty be trained rather than detec… (1)
  — EN : l. 5571 B9 · « How would you build a safety case that a … (3) ; l. 5661 B13 · « Can honesty be trained rather than detec… (1)

---

## 14. Généralisation faible-vers-fort — *Weak-to-strong generalization*

- **Maison** : tranche `volet2_E_a_I` ; FR : volet 2, §F · la généralisation comme levier (après « En pratique — l'automatisation ») ; EN : Part 2, §F · generalization as a lever (after "In practice — automation").
- **Limites** : 5 ; **parades** : 3.
- **Ancre FR** (ligne 717 de la v3.5 FR ; l'encadré s'insère juste après) :

~~~text
En pratique — l’automatisation (Anthropic, 2026). Plus récemment, l’équipe a construit des agents qui mènent eux-mêmes ce type de recherche — par exemple entraîner un modèle fort à partir de la seule supervision d’un faible — et a trouvé qu’ils surpassaient des chercheurs humains à budget égal. C’est un exemple où la méthode W2S devient à la fois l’objet d’étude et la tâche confiée à une IA, ce qui ramène la question de la confiance : comment valider le travail d’un chercheur automatisé qu’on ne sait pas mieux juger que ses résultats ?
~~~

- **Ancre EN** (ligne 808 de la v3.5 EN) :

~~~text
In practice — automation (Anthropic, 2026). More recently, the team built agents that carry out this kind of research themselves — for example training a strong model from the supervision of a weak one alone — and found that they outperformed human researchers at equal budget. This is an example where the W2S method becomes both the object of study and the task entrusted to an AI, which brings back the question of trust: how do we validate the work of an automated researcher that we cannot judge better than its results?
~~~

**Encadré complet, français :**

~~~markdown
> **⚠ Limites et parades — Généralisation faible-vers-fort** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Le fort peut imiter les erreurs du faible en paraissant précis. *(source : cours, volet 2, §F ; cours, volet 2, §F, JB8)*
>   **Parade :** Deux superviseurs, l'un faux dans un sens fixe, l'autre au hasard, et une copie entraînée sur les étiquettes vraies comme cas connu. *(source : cours, volet 2, §F, JB8)*
> - **Limite :** Récupérer l'écart peut venir d'idées qui exploitent la structure propre au jeu de données. *(source : cours, volet 2, §F, JB8)*
>   **Parade :** Une tâche à vérité connue, lue sur les items tenus à part où le superviseur se trompe. *(source : cours, volet 2, §F, JB8)*
> - **Limite :** Sur une tâche binaire, contredire partout passe pour une récupération. *(source : cours, volet 2, §F, JB8)*
>   **Parade :** Lire aussi l'accord du fort là où le superviseur a raison. *(source : cours, volet 2, §F, JB8)*
> - **Limite :** Les succès automatisés portent sur des tâches choisies pour être vérifiables ; les tâches floues restent hors de portée. *(source : cours, volet 7, F·40)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** Contre le sandbagging, la supervision faible ne tient que si l'entraînement est indistinguable du déploiement. *(source : cours, volet 7, F·26)*
>   **Parade :** aucune connue ; on le dit.
~~~

**Encadré complet, anglais :**

~~~markdown
> **⚠ Limits and workarounds — Weak-to-strong generalization** *(v3.6, 2 October 2026)*
>
> - **Limit:** The strong model can imitate the weak one's errors while looking accurate. *(source: course, Part 2, §F; course, Part 2, §F, JB8)*
>   **Workaround:** Two supervisors, one wrong in a fixed direction, the other at random, and a copy trained on true labels as the known case. *(source: course, Part 2, §F, JB8)*
> - **Limit:** Recovering the gap can come from ideas that exploit the dataset's own structure. *(source: course, Part 2, §F, JB8)*
>   **Workaround:** A task with known truth, read on the held-out items where the supervisor is wrong. *(source: course, Part 2, §F, JB8)*
> - **Limit:** On a binary task, contradicting everywhere passes for recovery. *(source: course, Part 2, §F, JB8)*
>   **Workaround:** Also read the strong model's agreement where the supervisor is right. *(source: course, Part 2, §F, JB8)*
> - **Limit:** Automated successes are on tasks chosen to be checkable; fuzzier tasks remain out of reach. *(source: course, Part 7, F·40)*
>   **Workaround:** none known; say so.
> - **Limit:** Against sandbagging, weak supervision holds only if training is indistinguishable from deployment. *(source: course, Part 7, F·26)*
>   **Workaround:** none known; say so.
~~~

**Renvoi d'une ligne :**

~~~markdown
> ⚠ **Limites et parades** : généralisation faible-vers-fort → volet 2, §F (après « En pratique — l'automatisation ») *(v3.6)*
> ⚠ **Limits and workarounds**: weak-to-strong generalization → Part 2, §F (after "In practice — automation") *(v3.6)*
~~~

**Où un renvoi ou un avertissement ponctuel est conseillé :**

- `volet3` — FR l. 977 : 4. L’oversight évolutif — et, en son sein, l’honnêteté · EN l. 1101 : 4. Scalable oversight — and, within it, honesty — renvoi.
- `volets4_5_entete` — FR l. 1307 : Sujet 12 — Scalable oversight / weak-to-strong (FAIBLE) · EN l. 1486 : Topic 12 — Scalable oversight / weak-to-strong (WEAK) — renvoi.
- `volet7_B_et_D` — FR l. 2012 : F·40 · Automated Weak-to-Strong Researcher — Wen (Fellows), Benton, Kirchner, Leike ; avri… · EN l. 2177 : F·40 · Automated Weak-to-Strong Researcher — Wen (Fellows), Benton, Kirchner, Leike; April… — renvoi.
- `volet7_B_et_D` — FR l. 2032 : F·26 · Removing Sandbagging in LLMs by Training with Weak Supervision — Ryd (Fellows), Bar… · EN l. 2186 : F·26 · Removing Sandbagging in LLMs by Training with Weak Supervision — Ryd (Fellows), Bar… — renvoi.
- `volet7_A_et_C` — FR l. 2352 : F·12 · Weak-to-Strong Generalization (Burns et al., OpenAI, 2023) — [P·22] · EN l. 2486 : F·12 · Weak-to-Strong Generalization (Burns et al., OpenAI, 2023) — [P·22] — renvoi.
- `volets8_9` — FR l. 2842 : 7 · Scalable oversight — « Can we design oversight mechanisms that will continue to work f… · EN l. 2999 : 7 · Scalable oversight — "Can we design oversight mechanisms that will continue to work fo… — renvoi.
- `volet10` — FR l. 3400 : Scalable oversight › Weak-to-strong and easy-to-hard generalization · EN l. 3639 : Scalable oversight › Weak-to-strong and easy-to-hard generalization — renvoi.
- `volet11_21_a_52` — FR l. 4676 : 49 · « Training a strong model on labels from a weaker overseer: what decides whether it i… · EN l. 4981 : 49 · « Training a strong model on labels from a weaker overseer: what decides whether it i… — renvoi.

**Où il revient** (relevé automatique, motifs FR `weak-to-strong|faible.vers.fort|easy-to-hard|facile.vers.difficile|W2S` / EN `weak-to-strong|easy-to-hard|W2S` ; sections, avec le nombre de lignes touchées) :

- `volet_M` — FR : —
  — EN : l. 456 M10 · The checklist, to reread before each rehea… (1)
- `volet2_E_a_I` — FR : l. 711 F. La généralisation comme levier — weak-to-stro… (4) ; l. 719 Cas d'application — la généralisation comme levi… (2)
  — EN : l. 765 Worked case — scalable oversight: "Would unsuper… (2) ; l. 801 F. Generalization as a lever — weak-to-strong, e… (4) ; l. 810 Worked case — generalization as a lever: "How wo… (2)
- `volet3` — FR : l. 977 4. L’oversight évolutif — et, en son sein, l’hon… (1) ; l. 1077 PARTIE III — LES TRAVAUX DU MOMENT (2025-2026) (1) ; l. 1103 PARTIE IV — SYNTHÈSE : comment tout s’emboîte, e… (1)
  — EN : l. 1101 4. Scalable oversight — and, within it, honesty (1) ; l. 1202 SECTION III — CURRENT WORK (2025-2026) (1) ; l. 1228 SECTION IV — SYNTHESIS: how everything fits toge… (1)
- `volets4_5_entete` — FR : l. 1179 Weak-to-Strong Generalization (OpenAI, Burns et … (2) ; l. 1285 B. Leurs sujets — méthodothèque, dosage léger ou… (2) ; l. 1326 Les papiers — quatre niveaux (1)
  — EN : l. 1254 The key papers, told one by one (2) ; l. 1463 B. Their topics — method toolkit, light or zero … (2) ; l. 1506 The papers — four levels (1)
- `volet6` — FR : l. 1458 4. La page « Recommended Directions » et ses sei… (2) ; l. 1474 5. Les travaux du programme Fellows, 2025-2026 —… (1)
  — EN : l. 1597 4. The "Recommended Directions" page and its six… (2) ; l. 1603 5. The work of the Fellows program, 2025-2026 — … (1) ; l. 1676 7. What these supplements change in Parts 1 to 5 (2)
- `volet7_B_et_D` — FR : l. 2012 F·40 · Automated Weak-to-Strong Researcher — Wen… (1)
  — EN : l. 2177 F·40 · Automated Weak-to-Strong Researcher — Wen… (2)
- `volet7_A_et_C` — FR : l. 2352 F·12 · Weak-to-Strong Generalization (Burns et a… (5) ; l. 2646 F·58 · Recommendations for Technical AI Safety R… (1)
  — EN : l. 2486 F·12 · Weak-to-Strong Generalization (Burns et a… (5) ; l. 2778 F·58 · Recommendations for Technical AI Safety R… (1)
- `volets8_9` — FR : l. 2666 VOLET 8 — Références, dans l'ordre des fiches (2) ; l. 2842 7 · Scalable oversight — « Can we design oversig… (3)
  — EN : l. 2804 PART 8 — References, in the order of the sheets (2) ; l. 2999 7 · Scalable oversight — "Can we design oversigh… (3) ; l. 3085 10 · The overall reading, in three sentences for… (3)
- `volet10` — FR : l. 2980 Dans les fiches (14) (1) ; l. 2998 Descriptions justes mais incomplètes (9) (1) ; l. 3400 Scalable oversight › Weak-to-strong and easy-to-… (2) ; l. 3404 Weak-to-Strong Reasoning — Yuqing Yang, Yan Ma, … (3) ; l. 3416 Evaluating Superhuman Models with Consistency Ch… (1) ; l. 3426 Scaling Laws for Reward Model Overoptimization —… (1) ; l. 3436 Easy2Hard-Bench: Standardized Difficulty Labels … (1) ; l. 3446 The Unreasonable Effectiveness of Easy Training … (1) ; l. 3456 Easy-to-Hard Generalization: Scalable Alignment … (4) ; l. 3466 Balancing Label Quantity and Quality for Scalabl… (2)
  — EN : l. 3223 In the sheets (14) (1) ; l. 3241 Descriptions that are correct but incomplete (9) (1) ; l. 3639 Scalable oversight › Weak-to-strong and easy-to-… (2) ; l. 3643 Weak-to-Strong Reasoning — Yuqing Yang, Yan Ma, … (3) ; l. 3655 Evaluating Superhuman Models with Consistency Ch… (1) ; l. 3665 Scaling Laws for Reward Model Overoptimization —… (1) ; l. 3675 Easy2Hard-Bench: Standardized Difficulty Labels … (2) ; l. 3685 The Unreasonable Effectiveness of Easy Training … (1) ; l. 3695 Easy-to-Hard Generalization: Scalable Alignment … (4) ; l. 3705 Balancing Label Quantity and Quality for Scalabl… (2)
- `volet11_21_a_52` — FR : l. 4386 34 · « Can automated researchers do alignment re… (1) ; l. 4676 49 · « Training a strong model on labels from a … (1)
  — EN : l. 4676 34 · « Can automated researchers do alignment re… (1) ; l. 4981 49 · « Training a strong model on labels from a … (1)
- `volet11_53_et_fin` — FR : l. 5117 B3 · « What should be delegated to automated res… (2)
  — EN : l. 5442 B3 · « What should be delegated to automated res… (1)

---

## 15. Moniteurs du contrôle (moniteur de confiance, sondes en production, agrégation) — *Control monitors (trusted monitor, probes in production, aggregation)*

- **Maison** : tranche `volet2_E_a_I` ; FR : volet 2, §G · monitoring et AI control (après « En pratique — les coup probes ») ; EN : Part 2, §G · monitoring and AI control (after "In practice — coup probes").
- **Limites** : 8 ; **parades** : 7.
- **Ancre FR** (ligne 758 de la v3.5 FR ; l'encadré s'insère juste après) :

~~~text
En pratique — les coup probes (Roger). Pour le versant « moniteur bon marché sur les internals », le but était de détecter une catégorie d’actions catastrophiques qu’on ne peut pas collecter naturellement (un modèle qui tente une prise de contrôle). La méthode des probes entraînées off-policy y répond : on entraîne une sonde sur des exemples synthétiques de l’action redoutée, en pariant qu’elle s’allumera sur la rare occurrence réelle. C’est l’occasion de faire le lien avec tes travaux : une telle sonde n’a de valeur que si elle survit au changement de distribution entre le synthétique et le réel — exactement la question que ta Phase 2 instrumente.
~~~

- **Ancre EN** (ligne 850 de la v3.5 EN) :

~~~text
In practice — coup probes (Roger). For the "cheap monitor on the internals" side, the goal was to detect a category of catastrophic actions that cannot be collected naturally (a model attempting a takeover). The method of probes trained off-policy answers this: we train a probe on synthetic examples of the feared action, betting that it will light up on the rare real occurrence. This is the opportunity to make the link with your work: such a probe is only worth something if it survives the distribution shift between the synthetic and the real — exactly the question your Phase 2 instruments.
~~~

**Encadré complet, français :**

~~~markdown
> **⚠ Limites et parades — Moniteurs du contrôle (moniteur de confiance, sondes en production, agrégation)** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Des angles morts systématiques : sur Opus 4.6, la moitié de quarante attaques conçues à la main ne sont jamais attrapées, et un prompt ciblé répare un angle mort en en dégradant un autre. *(source : cours, volet 7, F·23)*
>   **Parade :** Un ensemble de prompts spécialisés ou une seconde étape coûteuse, et un seuil calibré à 1 % de faux positifs sur des variantes bénignes appariées. *(source : cours, volet 7, F·23)*
> - **Limite :** Le chiffre de sûreté dépend de la force de la red team : un échafaudage optimisé fait passer le score de 0,87 à 0,41. *(source : cours, volet 7, F·24)*
>   **Parade :** Dire quelle red team le chiffre suppose, au moins une red team optimisée composante par composante. *(source : cours, volet 7, F·24)*
> - **Limite :** Menaces diffuses : chaque action est peu incriminante, et des attaques fragmentées passent les moniteurs par instance. *(source : cours, volet 7, F·59 et F·56)*
>   **Parade :** Des moniteurs à état ; pour l'agrégation de preuves internes, dire « I haven't seen that combination measured », jamais « first ». *(source : cours, volet 7, F·56 ; cours, volet 6, §6)*
> - **Limite :** Le rappel dépend du taux de base : un rappel de campagne ne se lit qu'avec le ratio de trafic bénin. *(source : cours, volet 6, §6)*
>   **Parade :** Rapporter le rappel à un taux de faux positifs fixé, avec le ratio de trafic dit. *(source : cours, volet 6, §6 ; cours, volet 2, préambule)*
> - **Limite :** Une sonde en production peut échouer en silence : le silence d'une sonde n'est pas celui du modèle. *(source : cours, volet 3, §3, K70)*
>   **Parade :** Des canaris (positifs connus glissés dans le trafic), un score de dérive, et un échantillon frais jugé chaque mois. *(source : cours, volet 3, §3, K70)*
> - **Limite :** Itérer contre ses détecteurs sélectionne l'évasion. *(source : fiche 19)*
>   **Parade :** Des détecteurs scellés, hors de la boucle : s'ils continuent de se déclencher quand ceux de la boucle se taisent, l'évasion a été sélectionnée. *(source : fiche 19)*
> - **Limite :** Le modèle de menace suppose les capacités de l'attaquant bornées et connues, et les événements rares s'estiment mal. *(source : cours, volet 4, AI Control)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** Après un entraînement à l'évasion, des captures qui survivent ne disent rien si l'entraînement n'a pas mordu. *(source : cours, volet 2, §G, K76)*
>   **Parade :** L'entraînement doit d'abord faire tomber les captures du moniteur de texte, et la sonde doit avoir attrapé avant. *(source : cours, volet 2, §G, K76)*
~~~

**Encadré complet, anglais :**

~~~markdown
> **⚠ Limits and workarounds — Control monitors (trusted monitor, probes in production, aggregation)** *(v3.6, 2 October 2026)*
>
> - **Limit:** Systematic blind spots: on Opus 4.6, half of forty hand-designed attacks are never caught, and a targeted prompt fixes one blind spot while degrading another. *(source: course, Part 7, F·23)*
>   **Workaround:** A set of specialized prompts or a costly second stage, and a threshold calibrated at 1% false positives on paired benign variants. *(source: course, Part 7, F·23)*
> - **Limit:** The safety number depends on the red team's strength: an optimized scaffold takes the score from 0.87 to 0.41. *(source: course, Part 7, F·24)*
>   **Workaround:** Say which red team the number assumes, at least one optimized component by component. *(source: course, Part 7, F·24)*
> - **Limit:** Diffuse threats: each action is barely incriminating, and fragmented attacks pass per-instance monitors. *(source: course, Part 7, F·59 and F·56)*
>   **Workaround:** Stateful monitors; for aggregating internal evidence, say "I haven't seen that combination measured", never "first". *(source: course, Part 7, F·56; course, Part 6, §6)*
> - **Limit:** Recall depends on the base rate: a campaign recall reads only with the benign-traffic ratio. *(source: course, Part 6, §6)*
>   **Workaround:** Report recall at a fixed false-positive rate, with the traffic ratio stated. *(source: course, Part 6, §6; course, Part 2, preamble)*
> - **Limit:** A probe in production can fail silently: a probe's silence is not the model's. *(source: course, Part 3, §3, K70)*
>   **Workaround:** Canaries (known positives slipped into traffic), a drift score, and a fresh sample judged every month. *(source: course, Part 3, §3, K70)*
> - **Limit:** Iterating against your detectors selects for evasion. *(source: reading sheet 19)*
>   **Workaround:** Sealed detectors, outside the loop: if they keep firing when the in-loop ones go quiet, evasion has been selected. *(source: reading sheet 19)*
> - **Limit:** The threat model assumes the attacker's capabilities bounded and known, and rare events are hard to estimate. *(source: course, Part 4, AI Control)*
>   **Workaround:** none known; say so.
> - **Limit:** After evasion training, surviving catches say nothing if the training did not bite. *(source: course, Part 2, §G, K76)*
>   **Workaround:** The training must first bring down the text monitor's catches, and the probe must have caught before. *(source: course, Part 2, §G, K76)*
~~~

**Renvoi d'une ligne :**

~~~markdown
> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») *(v3.6)*
> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after "In practice — coup probes") *(v3.6)*
~~~

**Où un renvoi ou un avertissement ponctuel est conseillé :**

- `tete_volet1` — FR l. 162 : Q10. « Défense en profondeur : quelles techniques de sûreté risquent d’échouer ensemble ? … · EN l. 226 : Q10. "Defense in depth: which safety techniques risk failing together?" — renvoi.
- `tete_volet1` — FR l. 168 : Q11. « Comment red-teamerais-tu un modèle frontière, ou superviserais-tu un agent autonome… · EN l. 233 : Q11. "How would you red-team a frontier model, or oversee an autonomous agent?" — renvoi.
- `volet3` — FR l. 953 : 3. Le contrôle par le monitoring (AI control) · EN l. 1076 : 3. Control through monitoring (AI control) — renvoi.
- `volets4_5_entete` — FR l. 1253 : Sujet 1 — Une probe de déception déployable · EN l. 1431 : Topic 1 — A deployable deception probe — renvoi.
- `volets4_5_entete` — FR l. 1291 : Sujet 8 — Control et monitoring (MOYEN) · EN l. 1470 : Topic 8 — Control and monitoring (MEDIUM) — renvoi.
- `volet6` — FR l. 1499 : 6. Ton programme de recherche, et sa revue d'antériorité · EN l. 1615 : 6. Your research program, and its prior-art review — renvoi.
- `volet7_B_et_D` — FR l. 1635 : F·22 · Diffuse AI Control on Fuzzy Tasks — Terekhov, Gulcehre (EPFL), Hebbar (Redwood), Be… · EN l. 1800 : F·22 · Diffuse AI Control on Fuzzy Tasks — Terekhov, Gulcehre (EPFL), Hebbar (Redwood), Be… — renvoi.
- `volet7_B_et_D` — FR l. 1690 : F·23 · SLEIGHT-Bench : Finding Blind Spots in AI Monitors — Najt, Toft (Fellows), Tracy (R… · EN l. 1855 : F·23 · SLEIGHT-Bench : Finding Blind Spots in AI Monitors — Najt, Toft (Fellows), Tracy (R… — renvoi.
- `volet7_B_et_D` — FR l. 1729 : F·24 · Strengthening Red Teams : A Modular Scaffold for Control Evaluations — Loughridge (… · EN l. 1894 : F·24 · Strengthening Red Teams : A Modular Scaffold for Control Evaluations — Loughridge (… — renvoi.
- `volet7_B_et_D` — FR l. 2051 : F·60 · Automated Researchers Can Subtly Sandbag — Gasteiger, Khan, Bowman, Wagner, Mikulik… · EN l. 2194 : F·60 · Automated Researchers Can Subtly Sandbag — Gasteiger, Khan, Bowman, Wagner, Mikulik… — renvoi.
- `volet7_A_et_C` — FR l. 2304 : F·10 · AI Control: Improving Safety Despite Intentional Subversion (Greenblatt et al., Red… · EN l. 2438 : F·10 · AI Control: Improving Safety Despite Intentional Subversion (Greenblatt et al., Red… — renvoi.
- `volet7_A_et_C` — FR l. 2504 : F·50 · Detecting Strategic Deception with Linear Probes (Goldowsky-Dill et al., Apollo Res… · EN l. 2636 : F·50 · Detecting Strategic Deception with Linear Probes (Goldowsky-Dill et al., Apollo Res… — renvoi.
- `volet7_A_et_C` — FR l. 2522 : F·51 · Detecting High-Stakes Interactions with Activation Probes (McKenzie et al., LASR La… · EN l. 2654 : F·51 · Detecting High-Stakes Interactions with Activation Probes (McKenzie et al., LASR La… — renvoi.
- `volet7_A_et_C` — FR l. 2540 : F·52 · NARCBench — Detecting Multi-Agent Collusion Through Multi-Agent Interpretability (R… · EN l. 2672 : F·52 · NARCBench — Detecting Multi-Agent Collusion Through Multi-Agent Interpretability (R… — renvoi.
- `volet7_A_et_C` — FR l. 2558 : F·53 · You Can't Escape Your Own Activations: Evaluation Awareness and Multi-Agent Monitor… · EN l. 2690 : F·53 · You Can't Escape Your Own Activations: Evaluation Awareness and Multi-Agent Monitor… — renvoi.
- `volet7_A_et_C` — FR l. 2575 : F·54 · TRACE (arXiv 2606.07054, 2026) et TRACES (Li et al., Brown ; mai 2026) — [P·43] · EN l. 2707 : F·54 · TRACE (arXiv 2606.07054, 2026) and TRACES (Li et al., Brown; May 2026) — [P·43] — renvoi.
- `volet7_A_et_C` — FR l. 2610 : F·56 · Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors — FakeLab … · EN l. 2742 : F·56 · Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors — FakeLab … — renvoi.
- `volet7_A_et_C` — FR l. 2629 : F·57 · Towards evaluations-based safety cases for AI scheming (Balesni, Apollo ; Evans, Sh… · EN l. 2761 : F·57 · Towards evaluations-based safety cases for AI scheming (Balesni, Apollo; Evans, Shl… — renvoi.
- `volets8_9` — FR l. 2798 : 6 · AI control — « Can we ensure safety by deploying models alongside sufficient safeguard… · EN l. 2955 : 6 · AI control — "Can we ensure safety by deploying models alongside sufficient safeguards… — renvoi.
- `volet10` — FR l. 3264 : AI control › Activation monitoring · EN l. 3504 : AI control › Activation monitoring — renvoi.
- `volet10` — FR l. 3287 : AI control › Anomaly detection · EN l. 3527 : AI control › Anomaly detection — renvoi.
- `volet11_1_a_20` — FR l. 3878 : 10 · « Diffuse Control already frames this as a red/blue game — and its authors say monito… · EN l. 4128 : 10 · « Diffuse Control already frames this as a red/blue game — and its authors say monito… — renvoi.
- `volet11_1_a_20` — FR l. 3898 : 11 · Les prémisses fausses — dix questions qui supposent un résultat que tu n'as pas, et l… · EN l. 4149 : 11 · Les prémisses fausses — dix questions qui supposent un résultat que tu n'as pas, et l… — renvoi.
- `volet11_1_a_20` — FR l. 4102 : 20 · « Suppose you must deploy a capable model you cannot fully trust. How would you desig… · EN l. 4377 : 20 · « Suppose you must deploy a capable model you cannot fully trust. How would you desig… — renvoi.
- `volet11_21_a_52` — FR l. 4177 : 23 · « NARCBench already correlates probe scores across agents. Isn't yours just that? » (… · EN l. 4451 : 23 · « NARCBench already correlates probe scores across agents. Isn't yours just that? » (… — renvoi.
- `volet11_21_a_52` — FR l. 4336 : 32 · « Where do monitors fail, and how would you find out before an adversary does? » (III… · EN l. 4622 : 32 · « Where do monitors fail, and how would you find out before an adversary does? » (III… — renvoi.
- `volet11_21_a_52` — FR l. 4361 : 33 · « A weak trusted scorer, a strong untrusted generator: can the generator sabotage wit… · EN l. 4647 : 33 · « A weak trusted scorer, a strong untrusted generator: can the generator sabotage wit… — renvoi.
- `volet11_53_et_fin` — FR l. 4822 : 60 · « Defense in depth — which techniques, and where do they fail together? » (I.8) · EN l. 5134 : 60 · « Defense in depth — which techniques, and where do they fail together? » (I.8) — renvoi.
- `volet11_53_et_fin` — FR l. 4977 : A6 · « Suppose a probe flags an agent mid-trajectory at your threshold. What happens next … · EN l. 5298 : A6 · « Suppose a probe flags an agent mid-trajectory at your threshold. What happens next … — renvoi.
- `volet11_53_et_fin` — FR l. 5269 : B10 · « Untrusted monitoring: the monitor is another instance of the actor. How do you sto… · EN l. 5594 : B10 · « Untrusted monitoring: the monitor is another instance of the actor. How do you sto… — renvoi.
- `volet7_A_et_C` — avertissement ponctuel prêt, après FR l. 2509 / EN l. 2641 (texte dans la partie « Par tranche »).

**Où il revient** (relevé automatique, motifs FR `moniteur|monitor` / EN `monitor` ; sections, avec le nombre de lignes touchées) :

- `tete_volet1` — FR : l. 104 5. La stratégie d’ensemble : la défense en profo… (1) ; l. 108 6. La carte du territoire (l’aperçu, avant le dé… (1) ; l. 138 Q5. « Peut-on faire confiance à la chaîne de pen… (1) ; l. 158 Q9. « Quelle est ta “théorie de l’impact” : si t… (1) ; l. 162 Q10. « Défense en profondeur : quelles technique… (1) ; l. 168 Q11. « Comment red-teamerais-tu un modèle fronti… (1)
  — EN : l. 25 Table (1) ; l. 116 2. Why a very capable system can be dangerous ev… (1) ; l. 156 5. The overall strategy: defense in depth (1) ; l. 161 6. The map of the territory (the overview, befor… (1) ; l. 197 Q5. "Can we trust a model's chain of thought to … (2) ; l. 221 Q9. "What is your “theory of impact”: if your re… (1) ; l. 226 Q10. "Defense in depth: which safety techniques … (1) ; l. 233 Q11. "How would you red-team a frontier model, o… (1)
- `volet_M` — FR : l. 298 M5 · Le nul et le cas connu (1) ; l. 345 M8 · La forme qui sert la logique (1)
  — EN : l. 365 M5 · The null and the known case (1) ; l. 412 M8 · The form that serves the logic (1) ; l. 456 M10 · The checklist, to reread before each rehea… (1)
- `volet2_A_a_D` — FR : l. 442 Cas d'application — organismes modèles et bancs … (1) ; l. 559 C bis · L'espace de travail (J-space) et le J-le… (1)
  — EN : l. 528 Worked case — model organisms and testbeds: "How… (1) ; l. 647 C bis · The workspace (J-space) and the J-lens —… (1)
- `volet2_E_a_I` — FR : l. 752 G. Monitoring & AI control — limiter les dégâts … (3) ; l. 760 Cas d'application — monitoring et AI control : «… (12)
  — EN : l. 843 G. Monitoring & AI control — limiting the damage… (4) ; l. 852 Worked case — monitoring and AI control: "How wo… (13)
- `volet3` — FR : l. 953 3. Le contrôle par le monitoring (AI control) (3) ; l. 977 4. L’oversight évolutif — et, en son sein, l’hon… (1) ; l. 1103 PARTIE IV — SYNTHÈSE : comment tout s’emboîte, e… (2)
  — EN : l. 1076 3. Control through monitoring (AI control) (3) ; l. 1101 4. Scalable oversight — and, within it, honesty (1) ; l. 1228 SECTION IV — SYNTHESIS: how everything fits toge… (2)
- `volets4_5_entete` — FR : l. 1235 4. La théorie de l’impact (1) ; l. 1285 B. Leurs sujets — méthodothèque, dosage léger ou… (3) ; l. 1326 Les papiers — quatre niveaux (2) ; l. 1350 Les questions — par probabilité et par enjeu (1)
  — EN : l. 1254 The key papers, told one by one (1) ; l. 1408 4. The theory of impact (1) ; l. 1463 B. Their topics — method toolkit, light or zero … (3) ; l. 1506 The papers — four levels (2) ; l. 1530 The questions — by probability and by stakes (1)
- `volet6` — FR : l. 1458 4. La page « Recommended Directions » et ses sei… (2) ; l. 1474 5. Les travaux du programme Fellows, 2025-2026 —… (2) ; l. 1578 8 · La validité des sondes d'activation hors dis… (1)
  — EN : l. 1597 4. The "Recommended Directions" page and its six… (2) ; l. 1603 5. The work of the Fellows program, 2025-2026 — … (1) ; l. 1676 7. What these supplements change in Parts 1 to 5 (5) ; l. 1746 8 · Out-of-distribution validity of activation p… (2)
- `volet7_B_et_D` — FR : l. 1633 B · Le contrôle et les moniteurs (lu : les bille… (1) ; l. 1635 F·22 · Diffuse AI Control on Fuzzy Tasks — Terek… (8) ; l. 1690 F·23 · SLEIGHT-Bench : Finding Blind Spots in AI… (10) ; l. 1729 F·24 · Strengthening Red Teams : A Modular Scaff… (1) ; l. 1843 F·34 · Model Spec Midtraining — Li, Wichers (Fel… (1) ; l. 1901 F·31 · Persona Vectors — Chen, Arditi (Fellows, … (5) ; l. 1961 F·38 · Agentic Misalignment — Lynch (Fellows, 1r… (1) ; l. 2012 F·40 · Automated Weak-to-Strong Researcher — Wen… (1) ; l. 2039 D · Les trois pièces contre le monitoring des me… (1) ; l. 2041 F·59 · How can we solve diffuse threats like res… (1) ; … (+1 sections)
  — EN : l. 1798 B · Control and monitors (read: the full blog po… (1) ; l. 1800 F·22 · Diffuse AI Control on Fuzzy Tasks — Terek… (8) ; l. 1855 F·23 · SLEIGHT-Bench : Finding Blind Spots in AI… (11) ; l. 1894 F·24 · Strengthening Red Teams : A Modular Scaff… (1) ; l. 2008 F·34 · Model Spec Midtraining — Li, Wichers (Fel… (1) ; l. 2066 F·31 · Persona Vectors — Chen, Arditi (Fellows, … (5) ; l. 2126 F·38 · Agentic Misalignment — Lynch (Fellows, 1s… (1) ; l. 2177 F·40 · Automated Weak-to-Strong Researcher — Wen… (1) ; l. 2189 D · The three items against monitoring of diffus… (1) ; l. 2191 F·59 · How can we solve diffuse threats like res… (1) ; … (+1 sections)
- `volet7_A_et_C` — FR : l. 2304 F·10 · AI Control: Improving Safety Despite Inte… (3) ; l. 2504 F·50 · Detecting Strategic Deception with Linear… (2) ; l. 2522 F·51 · Detecting High-Stakes Interactions with A… (3) ; l. 2558 F·53 · You Can't Escape Your Own Activations: Ev… (3) ; l. 2575 F·54 · TRACE (arXiv 2606.07054, 2026) et TRACES … (2) ; l. 2610 F·56 · Multi-Agent AI Control: Distributed Attac… (4) ; l. 2629 F·57 · Towards evaluations-based safety cases fo… (3) ; l. 2646 F·58 · Recommendations for Technical AI Safety R… (1)
  — EN : l. 2438 F·10 · AI Control: Improving Safety Despite Inte… (5) ; l. 2636 F·50 · Detecting Strategic Deception with Linear… (2) ; l. 2654 F·51 · Detecting High-Stakes Interactions with A… (3) ; l. 2690 F·53 · You Can't Escape Your Own Activations: Ev… (3) ; l. 2707 F·54 · TRACE (arXiv 2606.07054, 2026) and TRACES… (2) ; l. 2742 F·56 · Multi-Agent AI Control: Distributed Attac… (4) ; l. 2761 F·57 · Towards evaluations-based safety cases fo… (3) ; l. 2778 F·58 · Recommendations for Technical AI Safety R… (2)
- `volets8_9` — FR : l. 2666 VOLET 8 — Références, dans l'ordre des fiches (1) ; l. 2763 3 · Understanding model cognition — « What are o… (1) ; l. 2798 6 · AI control — « Can we ensure safety by deplo… (13) ; l. 2890 8 · Adversarial robustness — « Can we ensure AI … (1) ; l. 2928 10 · La lecture d'ensemble, en trois phrases pou… (2)
  — EN : l. 2804 PART 8 — References, in the order of the sheets (1) ; l. 2920 3 · Understanding model cognition — "What are ou… (1) ; l. 2943 5 · Chain-of-thought faithfulness — "When can we… (1) ; l. 2955 6 · AI control — "Can we ensure safety by deploy… (13) ; l. 3047 8 · Adversarial robustness — "Can we ensure AI s… (1) ; l. 3085 10 · The overall reading, in three sentences for… (5)
- `volet10` — FR : l. 3086 Me, Myself, and AI: The Situational Awareness Da… (1) ; l. 3096 Monitor: An AI-Driven Observability Interface — … (1) ; l. 3231 AI control › Behavioral monitoring (1) ; l. 3233 Testing Language Model Agents Safely in the Wild… (5) ; l. 3243 Visibility into AI Agents — Alan Chan, Carson Ez… (2) ; l. 3264 AI control › Activation monitoring (1) ; l. 3266 Coup probes: Catching catastrophes with probes t… (1) ; l. 3276 Improving Alignment and Robustness with Circuit … (1) ; l. 3289 Mechanistic anomaly detection and ELK — Paul Chr… (1) ; l. 3337 Supervising strong learners by amplifying weak e… (1) ; … (+8 sections)
  — EN : l. 3328 Me, Myself, and AI: The Situational Awareness Da… (1) ; l. 3338 Monitor: An AI-Driven Observability Interface — … (1) ; l. 3400 Vector-ICL: In-context Learning with Continuous … (1) ; l. 3471 AI control › Behavioral monitoring (1) ; l. 3473 Testing Language Model Agents Safely in the Wild… (5) ; l. 3483 Visibility into AI Agents — Alan Chan, Carson Ez… (4) ; l. 3493 Hidden in Plain Text: Emergence & Mitigation of … (1) ; l. 3504 AI control › Activation monitoring (1) ; l. 3506 Coup probes: Catching catastrophes with probes t… (2) ; l. 3516 Improving Alignment and Robustness with Circuit … (1) ; … (+10 sections)
- `volet11_1_a_20` — FR : l. 3854 9 · « What would you work on here, and why? » (2) ; l. 3878 10 · « Diffuse Control already frames this as a … (6) ; l. 3963 « SLEIGHT-Bench showed monitors catch about nine… (4) ; l. 3971 « Persona vectors only monitor — they can't be u… (2) ; l. 3981 « Your sequential monitor already beat TRACE in … (4) ; l. 4001 12 · « Why Anthropic? » (1) ; l. 4021 14 · « What would you want to have done in four … (1) ; l. 4079 19 · « A model behaves differently when it belie… (1) ; l. 4102 20 · « Suppose you must deploy a capable model y… (9)
  — EN : l. 4104 9 · « What would you work on here, and why? » (2) ; l. 4128 10 · « Diffuse Control already frames this as a … (6) ; l. 4214 « SLEIGHT-Bench showed monitors catch about nine… (3) ; l. 4222 « Persona vectors only monitor — they can't be u… (2) ; l. 4232 « Your sequential monitor already beat TRACE in … (3) ; l. 4252 12 · « Why Anthropic? » (2) ; l. 4275 14 · « What would you want to have done in four … (1) ; l. 4285 15 · « Any questions for us? » (1) ; l. 4350 19 · « A model behaves differently when it belie… (1) ; l. 4377 20 · « Suppose you must deploy a capable model y… (10)
- `volet11_21_a_52` — FR : l. 4129 21 · « A probe trained on synthetic examples of … (1) ; l. 4187 24 · « Probes drift toward "I am being evaluated… (1) ; l. 4224 26 · « What would kill this programme in the fir… (3) ; l. 4336 32 · « Where do monitors fail, and how would you… (10) ; l. 4361 33 · « A weak trusted scorer, a strong untrusted… (2) ; l. 4386 34 · « Can automated researchers do alignment re… (2) ; l. 4497 39 · « Where does your programme sit relative to… (5) ; l. 4521 40 · « You cite specific numbers for other peopl… (1) ; l. 4566 43 · « Is a chain of thought evidence of the rea… (1)
  — EN : l. 4404 21 · « A probe trained on synthetic examples of … (1) ; l. 4463 24 · « Probes drift toward "I am being evaluated… (1) ; l. 4500 26 · « What would kill this programme in the fir… (3) ; l. 4558 29 · « Can you read a model's personality in its… (2) ; l. 4622 32 · « Where do monitors fail, and how would you… (10) ; l. 4647 33 · « A weak trusted scorer, a strong untrusted… (2) ; l. 4676 34 · « Can automated researchers do alignment re… (2) ; l. 4792 39 · « Where does your programme sit relative to… (5) ; l. 4817 40 · « You cite specific numbers for other peopl… (1) ; l. 4869 43 · « Is a chain of thought evidence of the rea… (4) ; … (+1 sections)
- `volet11_53_et_fin` — FR : l. 4809 59 · « Misuse or misalignment — which worries yo… (1) ; l. 4822 60 · « Defense in depth — which techniques, and … (2) ; l. 4836 61 · « How would you red-team a model? » (I.9) (1) ; l. 4923 A2 · « You have $15,000 of compute a month and f… (1) ; l. 5003 A8 · « How do you think about the dual-use of yo… (2) ; l. 5016 A9 à A17 · Neuf questions moins probables, en ré… (2) ; l. 5075 B1 · « An agent can write documentation that a f… (5) ; l. 5117 B3 · « What should be delegated to automated res… (3) ; l. 5181 B6 · « Inter-query defenses: an attacker splits … (8) ; l. 5269 B10 · « Untrusted monitoring: the monitor is ano… (12) ; … (+1 sections)
  — EN : l. 5121 59 · « Misuse or misalignment — which worries yo… (1) ; l. 5134 60 · « Defense in depth — which techniques, and … (2) ; l. 5149 61 · « How would you red-team a model? » (I.9) (1) ; l. 5239 A2 · « You have $15,000 of compute a month and f… (1) ; l. 5255 A3 · « What if the probes just don't work at all… (1) ; l. 5327 A8 · « How do you think about the dual-use of yo… (2) ; l. 5341 A9 à A17 · Neuf questions moins probables, en ré… (2) ; l. 5400 B1 · « An agent can write documentation that a f… (3) ; l. 5442 B3 · « What should be delegated to automated res… (1) ; l. 5506 B6 · « Inter-query defenses: an attacker splits … (4) ; … (+2 sections)

---

## 16. Red-teaming — *Red-teaming*

- **Maison** : tranche `volet2_E_a_I` ; FR : volet 2, §H · robustesse adverse et red-teaming (après « En pratique — StrongREJECT ») ; EN : Part 2, §H · adversarial robustness and red-teaming (after "In practice — StrongREJECT").
- **Limites** : 6 ; **parades** : 5.
- **Ancre FR** (ligne 803 de la v3.5 FR ; l'encadré s'insère juste après) :

~~~text
En pratique — StrongREJECT (Souly et al.), pour la mesure. Ce travail répond à un problème de méthode : comment mesurer le succès d’un jailbreak sans se faire tromper par le non-refus ? Le benchmark évalue le préjudice par la capacité de nuire réellement extraite — la réponse jailbreakée est-elle utilisable pour faire le mal ? — et non par le simple fait que le modèle a cessé de refuser. C’est l’exemple à citer pour montrer qu’on évalue la bonne chose.
~~~

- **Ancre EN** (ligne 896 de la v3.5 EN) :

~~~text
In practice — StrongREJECT (Souly et al.), for measurement. This work answers a methodological problem: how do we measure the success of a jailbreak without being fooled by non-refusal? The benchmark evaluates harm by the capability to do harm actually extracted — is the jailbroken answer usable for doing harm? — and not by the mere fact that the model stopped refusing. This is the example to cite to show that we are evaluating the right thing.
~~~

**Encadré complet, français :**

~~~markdown
> **⚠ Limites et parades — Red-teaming** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Sans budget fixé, « rien trouvé » dit seulement qu'on n'a pas assez cherché. *(source : cours, volet M, M7)*
>   **Parade :** Un budget fixé d'avance, rapporté avec le résultat. *(source : cours, volet M, M7)*
> - **Limite :** Une porte dérobée reste muette sans son déclencheur : une red team boîte noire ou un jeu fixe la manquent. *(source : cours, volet M, M5 ; cours, volet 7, F·35)*
>   **Parade :** Un jumeau propre, entraîné sur des données auditées, et une porte plantée exprès comme cas connu. *(source : cours, volet M, M4 et M9)*
> - **Limite :** Mesurer le non-refus au lieu du préjudice. *(source : cours, volet 2, §H)*
>   **Parade :** Le préjudice réellement extrait, ou différentiel, noté à l'aveugle. *(source : cours, volet 2, §H ; cours, volet 2, §H, G1)*
> - **Limite :** Un jeu qui ne sépare rien fait concorder tous les classements. *(source : cours, volet 2, §H, G1)*
>   **Parade :** Le modèle nu doit montrer un uplift, et un filtre affaibli exprès plus de préjudice que sa version complète. *(source : cours, volet 2, §H, G1)*
> - **Limite :** Une red team faible fait paraître la défense sûre. *(source : cours, volet 7, F·24)*
>   **Parade :** Une red team optimisée composante par composante, avec l'ablation de chaque composante. *(source : cours, volet 7, F·24)*
> - **Limite :** Entraîner sur les attaques trouvées peut apprendre au modèle à mieux reconnaître son déclencheur. *(source : fiche 15)*
>   **Parade :** aucune connue ; on le dit.
~~~

**Encadré complet, anglais :**

~~~markdown
> **⚠ Limits and workarounds — Red-teaming** *(v3.6, 2 October 2026)*
>
> - **Limit:** Without a fixed budget, "nothing found" only says you did not search enough. *(source: course, Part M, M7)*
>   **Workaround:** A budget fixed in advance, reported with the result. *(source: course, Part M, M7)*
> - **Limit:** A backdoor stays silent without its trigger: a black-box red team or a fixed set misses it. *(source: course, Part M, M5; course, Part 7, F·35)*
>   **Workaround:** A clean twin, trained on audited data, and a deliberately planted backdoor as the known case. *(source: course, Part M, M4 and M9)*
> - **Limit:** Measuring non-refusal instead of harm. *(source: course, Part 2, §H)*
>   **Workaround:** The harm actually extracted, or differential harm, blind-scored. *(source: course, Part 2, §H; course, Part 2, §H, G1)*
> - **Limit:** A game that separates nothing makes every ranking agree. *(source: course, Part 2, §H, G1)*
>   **Workaround:** The bare model must show uplift, and a deliberately weakened filter more harm than its full version. *(source: course, Part 2, §H, G1)*
> - **Limit:** A weak red team makes the defence look safe. *(source: course, Part 7, F·24)*
>   **Workaround:** A red team optimized component by component, with each component ablated. *(source: course, Part 7, F·24)*
> - **Limit:** Training on the attacks found can teach the model to recognize its trigger better. *(source: reading sheet 15)*
>   **Workaround:** none known; say so.
~~~

**Renvoi d'une ligne :**

~~~markdown
> ⚠ **Limites et parades** : red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») *(v3.6)*
> ⚠ **Limits and workarounds**: red-teaming → Part 2, §H (after "In practice — StrongREJECT") *(v3.6)*
~~~

**Où un renvoi ou un avertissement ponctuel est conseillé :**

- `tete_volet1` — FR l. 168 : Q11. « Comment red-teamerais-tu un modèle frontière, ou superviserais-tu un agent autonome… · EN l. 233 : Q11. "How would you red-team a frontier model, or oversee an autonomous agent?" — renvoi.
- `volet_M` — FR l. 365 : M9 · Un cas complet, avant et après : la première question vitale · EN l. 432 : M9 · A complete case, before and after: the first vital question — renvoi.
- `volet2_E_a_I` — FR l. 760 : Cas d'application — monitoring et AI control : « How would you design a control evaluation… · EN l. 852 : Worked case — monitoring and AI control: "How would you design a control evaluation for a … — renvoi.
- `volet3` — FR l. 1003 : 5. La robustesse adverse · EN l. 1128 : 5. Adversarial robustness — renvoi.
- `volets4_5_entete` — FR l. 1119 : Sleeper Agents (Anthropic, Hubinger et al.) · EN l. 1261 : Sleeper Agents (Anthropic, Hubinger et al.) — renvoi.
- `volets4_5_entete` — FR l. 1291 : Sujet 8 — Control et monitoring (MOYEN) · EN l. 1470 : Topic 8 — Control and monitoring (MEDIUM) — renvoi.
- `volet7_B_et_D` — FR l. 1729 : F·24 · Strengthening Red Teams : A Modular Scaffold for Control Evaluations — Loughridge (… · EN l. 1894 : F·24 · Strengthening Red Teams : A Modular Scaffold for Control Evaluations — Loughridge (… — renvoi.
- `volet7_B_et_D` — FR l. 1994 : F·35 · Poisoning Fine-tuning Datasets of Constitutional Classifiers — Bowers (Fellows), Al… · EN l. 2159 : F·35 · Poisoning Fine-tuning Datasets of Constitutional Classifiers — Bowers (Fellows), Al… — renvoi.
- `volet7_A_et_C` — FR l. 2304 : F·10 · AI Control: Improving Safety Despite Intentional Subversion (Greenblatt et al., Red… · EN l. 2438 : F·10 · AI Control: Improving Safety Despite Intentional Subversion (Greenblatt et al., Red… — renvoi.
- `volet7_A_et_C` — FR l. 2424 : F·15 · Universal and Transferable Adversarial Attacks — GCG (Zou et al., 2023) — [P·9] · EN l. 2558 : F·15 · Universal and Transferable Adversarial Attacks — GCG (Zou et al., 2023) — [P·9] — renvoi.
- `volets8_9` — FR l. 2890 : 8 · Adversarial robustness — « Can we ensure AI systems behave as desired despite adversar… · EN l. 3047 : 8 · Adversarial robustness — "Can we ensure AI systems behave as desired despite adversari… — renvoi.
- `volet10` — FR l. 3565 : Adversarial robustness › Realistic and differential benchmarks for jailbreaks · EN l. 3802 : Adversarial robustness › Realistic and differential benchmarks for jailbreaks — renvoi.
- `volet10` — FR l. 3608 : Adversarial robustness › Adaptive defenses · EN l. 3845 : Adversarial robustness › Adaptive defenses — renvoi.
- `volet11_1_a_20` — FR l. 3809 : 7 · « How would you prevent bad actors from misaligning an LLM for harmful use? » *(questi… · EN l. 4057 : 7 · « How would you prevent bad actors from misaligning an LLM for harmful use? » *(questi… — renvoi.
- `volet11_21_a_52` — FR l. 4336 : 32 · « Where do monitors fail, and how would you find out before an adversary does? » (III… · EN l. 4622 : 32 · « Where do monitors fail, and how would you find out before an adversary does? » (III… — renvoi.
- `volet11_21_a_52` — FR l. 4694 : 50 · « Jailbreak benchmarks measure non-refusal. What would a benchmark of real, different… · EN l. 5000 : 50 · « Jailbreak benchmarks measure non-refusal. What would a benchmark of real, different… — renvoi.
- `volet11_53_et_fin` — FR l. 4836 : 61 · « How would you red-team a model? » (I.9) · EN l. 5149 : 61 · « How would you red-team a model? » (I.9) — renvoi.
- `volet11_53_et_fin` — FR l. 5358 : B14 · « If you could run one adversarial evaluation on our production model tomorrow, what… · EN l. 5683 : B14 · « If you could run one adversarial evaluation on our production model tomorrow, what… — renvoi.

**Où il revient** (relevé automatique, motifs FR `red.team|jailbreak` / EN `red.team|jailbreak` ; sections, avec le nombre de lignes touchées) :

- `tete_volet1` — FR : l. 148 Q7. « Qu’est-ce que la Responsible Scaling Polic… (1) ; l. 162 Q10. « Défense en profondeur : quelles technique… (1) ; l. 168 Q11. « Comment red-teamerais-tu un modèle fronti… (2)
  — EN : l. 25 Table (1) ; l. 209 Q7. "What is the Responsible Scaling Policy, and… (1) ; l. 226 Q10. "Defense in depth: which safety techniques … (1) ; l. 233 Q11. "How would you red-team a frontier model, o… (2)
- `volet_M` — FR : l. 298 M5 · Le nul et le cas connu (1) ; l. 330 M7 · La plus petite version, le budget, et la cl… (1) ; l. 365 M9 · Un cas complet, avant et après : la premièr… (4)
  — EN : l. 365 M5 · The null and the known case (1) ; l. 397 M7 · The smallest version, the budget, and the c… (1) ; l. 432 M9 · A complete case, before and after: the firs… (4) ; l. 456 M10 · The checklist, to reread before each rehea… (1)
- `volet2_A_a_D` — FR : l. 422 Préambule — les quatre « grammaires d’attaque » (1) ; l. 480 B. Évaluations — mesurer une capacité ou une pro… (1)
  — EN : l. 506 Preamble — the four "attack grammars" (1)
- `volet2_E_a_I` — FR : l. 752 G. Monitoring & AI control — limiter les dégâts … (2) ; l. 760 Cas d'application — monitoring et AI control : «… (1) ; l. 797 H. Robustesse adverse & red-teaming — résister a… (4) ; l. 805 Cas d'application — robustesse adverse et mésusa… (2)
  — EN : l. 843 G. Monitoring & AI control — limiting the damage… (2) ; l. 852 Worked case — monitoring and AI control: "How wo… (1) ; l. 889 H. Adversarial robustness & red-teaming — resist… (4) ; l. 898 Worked case — adversarial robustness and misuse:… (3)
- `volet3` — FR : l. 953 3. Le contrôle par le monitoring (AI control) (1) ; l. 1003 5. La robustesse adverse (1) ; l. 1053 PARTIE II — LES ÉQUIPES : qui fait quoi chez (1) ; l. 1077 PARTIE III — LES TRAVAUX DU MOMENT (2025-2026) (2) ; l. 1103 PARTIE IV — SYNTHÈSE : comment tout s’emboîte, e… (1)
  — EN : l. 1076 3. Control through monitoring (AI control) (1) ; l. 1128 5. Adversarial robustness (1) ; l. 1180 SECTION II — THE TEAMS: who does what at (1) ; l. 1202 SECTION III — CURRENT WORK (2025-2026) (2) ; l. 1228 SECTION IV — SYNTHESIS: how everything fits toge… (1)
- `volets4_5_entete` — FR : l. 1153 Towards puis Scaling Monosemanticity (Anthropic, (1) ; l. 1185 Auditing Hidden Objectives (Anthropic, Marks et … (1) ; l. 1251 A. Tes sujets FORT — ta thèse peut être la colon… (1) ; l. 1326 Les papiers — quatre niveaux (1)
  — EN : l. 1254 The key papers, told one by one (2) ; l. 1428 A. Your STRONG topics — your thesis can be the b… (1) ; l. 1506 The papers — four levels (1)
- `volet6` — FR : l. 1458 4. La page « Recommended Directions » et ses sei… (1) ; l. 1474 5. Les travaux du programme Fellows, 2025-2026 —… (1)
  — EN : l. 1597 4. The "Recommended Directions" page and its six… (1) ; l. 1603 5. The work of the Fellows program, 2025-2026 — … (1) ; l. 1676 7. What these supplements change in Parts 1 to 5 (1)
- `volet7_B_et_D` — FR : l. 1635 F·22 · Diffuse AI Control on Fuzzy Tasks — Terek… (2) ; l. 1690 F·23 · SLEIGHT-Bench : Finding Blind Spots in AI… (2) ; l. 1729 F·24 · Strengthening Red Teams : A Modular Scaff… (7) ; l. 1994 F·35 · Poisoning Fine-tuning Datasets of Constit… (2) ; l. 2028 F·42 · A3 : An Automated Alignment Agent for Saf… (1)
  — EN : l. 1800 F·22 · Diffuse AI Control on Fuzzy Tasks — Terek… (3) ; l. 1855 F·23 · SLEIGHT-Bench : Finding Blind Spots in AI… (2) ; l. 1894 F·24 · Strengthening Red Teams : A Modular Scaff… (7) ; l. 2159 F·35 · Poisoning Fine-tuning Datasets of Constit… (1) ; l. 2183 F·42 · A3 : An Automated Alignment Agent for Saf… (1)
- `volet7_A_et_C` — FR : l. 2304 F·10 · AI Control: Improving Safety Despite Inte… (1) ; l. 2424 F·15 · Universal and Transferable Adversarial At… (3) ; l. 2522 F·51 · Detecting High-Stakes Interactions with A… (3)
  — EN : l. 2438 F·10 · AI Control: Improving Safety Despite Inte… (2) ; l. 2558 F·15 · Universal and Transferable Adversarial At… (3) ; l. 2654 F·51 · Detecting High-Stakes Interactions with A… (3)
- `volets8_9` — FR : l. 2666 VOLET 8 — Références, dans l'ordre des fiches (3) ; l. 2798 6 · AI control — « Can we ensure safety by deplo… (4) ; l. 2890 8 · Adversarial robustness — « Can we ensure AI … (2)
  — EN : l. 2804 PART 8 — References, in the order of the sheets (3) ; l. 2955 6 · AI control — "Can we ensure safety by deploy… (3) ; l. 3047 8 · Adversarial robustness — "Can we ensure AI s… (2) ; l. 3085 10 · The overall reading, in three sentences for… (3)
- `volet10` — FR : l. 2980 Dans les fiches (14) (1) ; l. 2998 Descriptions justes mais incomplètes (9) (1) ; l. 3106 Interpreting the Second-Order Effects of Neurons… (1) ; l. 3266 Coup probes: Catching catastrophes with probes t… (3) ; l. 3289 Mechanistic anomaly detection and ELK — Paul Chr… (1) ; l. 3544 Persistent Pre-training Poisoning of LLMs — Yimi… (3) ; l. 3565 Adversarial robustness › Realistic and different… (1) ; l. 3567 A StrongREJECT for Empty Jailbreaks — Alexandra … (6) ; l. 3577 AgentHarm: A Benchmark for Measuring Harmfulness… (4) ; l. 3587 On the Societal Impact of Open Foundation Models… (1) ; … (+2 sections)
  — EN : l. 3223 In the sheets (14) (1) ; l. 3241 Descriptions that are correct but incomplete (9) (1) ; l. 3348 Interpreting the Second-Order Effects of Neurons… (1) ; l. 3506 Coup probes: Catching catastrophes with probes t… (3) ; l. 3529 Mechanistic anomaly detection and ELK — Paul Chr… (1) ; l. 3781 Persistent Pre-training Poisoning of LLMs — Yimi… (3) ; l. 3802 Adversarial robustness › Realistic and different… (1) ; l. 3804 A StrongREJECT for Empty Jailbreaks — Alexandra … (5) ; l. 3814 AgentHarm: A Benchmark for Measuring Harmfulness… (4) ; l. 3824 On the Societal Impact of Open Foundation Models… (1) ; … (+2 sections)
- `volet11_1_a_20` — FR : l. 3809 7 · « How would you prevent bad actors from misa… (4) ; l. 4102 20 · « Suppose you must deploy a capable model y… (1)
  — EN : l. 4057 7 · « How would you prevent bad actors from misa… (5) ; l. 4104 9 · « What would you work on here, and why? » (1) ; l. 4377 20 · « Suppose you must deploy a capable model y… (1)
- `volet11_21_a_52` — FR : l. 4361 33 · « A weak trusted scorer, a strong untrusted… (1) ; l. 4451 37 · « How strong does a red team have to be, an… (5) ; l. 4497 39 · « Where does your programme sit relative to… (1) ; l. 4694 50 · « Jailbreak benchmarks measure non-refusal.… (2)
  — EN : l. 4647 33 · « A weak trusted scorer, a strong untrusted… (1) ; l. 4745 37 · « How strong does a red team have to be, an… (6) ; l. 4792 39 · « Where does your programme sit relative to… (1) ; l. 5000 50 · « Jailbreak benchmarks measure non-refusal.… (1)
- `volet11_53_et_fin` — FR : l. 4836 61 · « How would you red-team a model? » (I.9) (7) ; l. 4910 A1 · « Which team would you want to join — Align… (2) ; l. 4923 A2 · « You have $15,000 of compute a month and f… (1) ; l. 5117 B3 · « What should be delegated to automated res… (2)
  — EN : l. 5149 61 · « How would you red-team a model? » (I.9) (7) ; l. 5225 A1 · « Which team would you want to join — Align… (2) ; l. 5239 A2 · « You have $15,000 of compute a month and f… (1) ; l. 5442 B3 · « What should be delegated to automated res… (2)

---

## 17. Classifieurs de sûreté (filtres) — *Safety classifiers (filters)*

- **Maison** : tranche `volet2_E_a_I` ; FR : volet 2, §H · cas d'application G1 (fin du cas) ; EN : Part 2, §H · worked case G1 (end of the case).
- **Limites** : 5 ; **parades** : 4.
- **Ancre FR** (ligne 832 de la v3.5 FR ; l'encadré s'insère juste après) :

~~~text
**À l'oral.** *« I'd bet refusal rates misrank the filters I'd test, judged on uplift, the help an attacker can't get elsewhere. I'd rank the filters twice, by refusal rate and by differential harm — harm with the model minus harm without it; if the two rankings agreed within the noise of a replayed arm, while weakening a filter still raised harm, I'd drop the bet. »*
~~~

- **Ancre EN** (ligne 925 de la v3.5 EN) :

~~~text
**Out loud.** *"I'd bet refusal rates misrank the filters I'd test, judged on uplift, the help an attacker can't get elsewhere. I'd rank the filters twice, by refusal rate and by differential harm — harm with the model minus harm without it; if the two rankings agreed within the noise of a replayed arm, while weakening a filter still raised harm, I'd drop the bet."*
~~~

**Encadré complet, français :**

~~~markdown
> **⚠ Limites et parades — Classifieurs de sûreté (filtres)** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Empoisonnement : environ 32 exemples suffisent, quelle que soit la taille du jeu, et certaines portes ont échappé à des jeux de test red team fixes. *(source : cours, volet 7, F·35 ; cours, volet M, M9)*
>   **Parade :** Un jumeau propre réentraîné sur des données auditées, un second pour borner l'écart dû au hasard, et un filtre empoisonné exprès comme cas connu. *(source : cours, volet M, M4 et M9)*
> - **Limite :** Le jumeau propre ne donne qu'une borne large, qui signale moins. *(source : cours, volet M, M4)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** Un jeu canari ne contient pas le déclencheur inconnu de l'attaquant. *(source : cours, volet M, M5)*
>   **Parade :** Comparer au jumeau propre, face à une porte connue. *(source : cours, volet M, M9)*
> - **Limite :** Une chasse aux contournements compte des contournements ; un taux de refus ne dit pas ce que le filtre retire à l'attaquant. *(source : cours, volet 2, §H, G1)*
>   **Parade :** Classer les filtres deux fois, par taux de refus et par préjudice différentiel. *(source : cours, volet 2, §H, G1)*
> - **Limite :** Placé dans l'entraînement, un classifieur incite le modèle à l'éviter. *(source : fiche 3)*
>   **Parade :** Le modifier pour ne pas inciter l'évasion, et ne jamais entraîner contre lui. *(source : fiche 3 ; fiche 17)*
~~~

**Encadré complet, anglais :**

~~~markdown
> **⚠ Limits and workarounds — Safety classifiers (filters)** *(v3.6, 2 October 2026)*
>
> - **Limit:** Poisoning: about 32 examples suffice, whatever the dataset size, and some backdoors escaped fixed red-team test sets. *(source: course, Part 7, F·35; course, Part M, M9)*
>   **Workaround:** A clean twin retrained on audited data, a second one to bound chance variation, and a deliberately poisoned filter as the known case. *(source: course, Part M, M4 and M9)*
> - **Limit:** The clean twin gives only a wide bound, which flags less. *(source: course, Part M, M4)*
>   **Workaround:** none known; say so.
> - **Limit:** A canary set does not contain the attacker's unknown trigger. *(source: course, Part M, M5)*
>   **Workaround:** Compare against the clean twin, facing a known backdoor. *(source: course, Part M, M9)*
> - **Limit:** A bypass hunt counts bypasses; a refusal rate does not say what the filter takes away from the attacker. *(source: course, Part 2, §H, G1)*
>   **Workaround:** Rank the filters twice, by refusal rate and by differential harm. *(source: course, Part 2, §H, G1)*
> - **Limit:** Placed in training, a classifier gives the model an incentive to evade it. *(source: reading sheet 3)*
>   **Workaround:** Modify it so as not to incentivize evasion, and never train against it. *(source: reading sheet 3; reading sheet 17)*
~~~

**Renvoi d'une ligne :**

~~~markdown
> ⚠ **Limites et parades** : classifieurs de sûreté → volet 2, §H (fin du cas d'application G1) *(v3.6)*
> ⚠ **Limits and workarounds**: safety classifiers → Part 2, §H (end of worked case G1) *(v3.6)*
~~~

**Où un renvoi ou un avertissement ponctuel est conseillé :**

- `volet_M` — FR l. 365 : M9 · Un cas complet, avant et après : la première question vitale · EN l. 432 : M9 · A complete case, before and after: the first vital question — renvoi.
- `volet3` — FR l. 1003 : 5. La robustesse adverse · EN l. 1128 : 5. Adversarial robustness — renvoi.
- `volet7_B_et_D` — FR l. 1994 : F·35 · Poisoning Fine-tuning Datasets of Constitutional Classifiers — Bowers (Fellows), Al… · EN l. 2159 : F·35 · Poisoning Fine-tuning Datasets of Constitutional Classifiers — Bowers (Fellows), Al… — renvoi.
- `volets8_9` — FR l. 2890 : 8 · Adversarial robustness — « Can we ensure AI systems behave as desired despite adversar… · EN l. 3047 : 8 · Adversarial robustness — "Can we ensure AI systems behave as desired despite adversari… — renvoi.
- `volet10` — FR l. 3608 : Adversarial robustness › Adaptive defenses · EN l. 3845 : Adversarial robustness › Adaptive defenses — renvoi.
- `volet11_1_a_20` — FR l. 3809 : 7 · « How would you prevent bad actors from misaligning an LLM for harmful use? » *(questi… · EN l. 4057 : 7 · « How would you prevent bad actors from misaligning an LLM for harmful use? » *(questi… — renvoi.

**Où il revient** (relevé automatique, motifs FR `classifieur|filtre|canari|jumeau` / EN `classifier|filter|canar|twin` ; sections, avec le nombre de lignes touchées) :

- `tete_volet1` — FR : l. 76 3. Deux familles de risque à ne jamais confondre… (1) ; l. 152 Q8. « Faut-il s’inquiéter davantage du mésusage … (1)
  — EN : l. 131 3. Two families of risk never to be confused: mi… (1) ; l. 214 Q8. "Should we worry more about misuse or about … (1)
- `volet_M` — FR : l. 219 M2 · Le pari : sur le modèle, jamais sur la méth… (2) ; l. 257 M4 · Le contrôle : ce qu'il écarte, et il doit s… (4) ; l. 298 M5 · Le nul et le cas connu (2) ; l. 316 M6 · Le signe d'échec, et le protocole possible (1) ; l. 365 M9 · Un cas complet, avant et après : la premièr… (7)
  — EN : l. 261 M1 · The arc of an answer, in seven beats (1) ; l. 286 M2 · The bet: on the model, never on the method (3) ; l. 324 M4 · The control: what it rules out, and it must… (4) ; l. 365 M5 · The null and the known case (2) ; l. 383 M6 · The failure sign, and the feasible protocol (1) ; l. 397 M7 · The smallest version, the budget, and the c… (1) ; l. 432 M9 · A complete case, before and after: the firs… (8)
- `volet2_A_a_D` — FR : l. 513 C. Méthodes sur activations — probing & steering… (1)
  — EN : l. 600 C. Methods on activations — probing & steering (… (1)
- `volet2_E_a_I` — FR : l. 675 Cas d'application — la supervision évolutive : «… (3) ; l. 797 H. Robustesse adverse & red-teaming — résister a… (1) ; l. 805 Cas d'application — robustesse adverse et mésusa… (5)
  — EN : l. 765 Worked case — scalable oversight: "Would unsuper… (3) ; l. 889 H. Adversarial robustness & red-teaming — resist… (1) ; l. 898 Worked case — adversarial robustness and misuse:… (6)
- `volet3` — FR : l. 953 3. Le contrôle par le monitoring (AI control) (6) ; l. 1003 5. La robustesse adverse (3) ; l. 1029 6. Le domaine « divers » : désapprentissage et g… (1)
  — EN : l. 1076 3. Control through monitoring (AI control) (6) ; l. 1128 5. Adversarial robustness (3) ; l. 1155 6. The "miscellaneous" domain: unlearning and mu… (1) ; l. 1180 SECTION II — THE TEAMS: who does what at (1) ; l. 1202 SECTION III — CURRENT WORK (2025-2026) (1)
- `volets4_5_entete` — FR : —
  — EN : l. 1506 The papers — four levels (1)
- `volet6` — FR : —
  — EN : l. 1603 5. The work of the Fellows program, 2025-2026 — … (1) ; l. 1676 7. What these supplements change in Parts 1 to 5 (2)
- `volet7_B_et_D` — FR : l. 1690 F·23 · SLEIGHT-Bench : Finding Blind Spots in AI… (2) ; l. 1729 F·24 · Strengthening Red Teams : A Modular Scaff… (1) ; l. 1812 F·30 · CHIVE — Would This Change Your Answer? — … (1) ; l. 1876 F·33 · Inoculation Prompting — Wichers, Ebtekar … (1) ; l. 1928 F·32 · Subliminal Learning — Cloud, Le (Fellows)… (2) ; l. 1994 F·35 · Poisoning Fine-tuning Datasets of Constit… (1) ; l. 2000 F·36 · Beyond Data Filtering : Knowledge Localiz… (1)
  — EN : l. 1855 F·23 · SLEIGHT-Bench : Finding Blind Spots in AI… (2) ; l. 1894 F·24 · Strengthening Red Teams : A Modular Scaff… (1) ; l. 1977 F·30 · CHIVE — Would This Change Your Answer? — … (1) ; l. 2041 F·33 · Inoculation Prompting — Wichers, Ebtekar … (1) ; l. 2093 F·32 · Subliminal Learning — Cloud, Le (Fellows)… (7) ; l. 2159 F·35 · Poisoning Fine-tuning Datasets of Constit… (2) ; l. 2165 F·36 · Beyond Data Filtering : Knowledge Localiz… (2) ; l. 2180 F·41 · TASTE — Baig (Fellows); August 2026. (1)
- `volet7_A_et_C` — FR : l. 2424 F·15 · Universal and Transferable Adversarial At… (1)
  — EN : l. 2558 F·15 · Universal and Transferable Adversarial At… (1)
- `volets8_9` — FR : l. 2842 7 · Scalable oversight — « Can we design oversig… (1)
  — EN : l. 2804 PART 8 — References, in the order of the sheets (2) ; l. 2999 7 · Scalable oversight — "Can we design oversigh… (1)
- `volet10` — FR : l. 2980 Dans les fiches (14) (1) ; l. 3044 GPQA: A Graduate-Level Google-Proof Q&A Benchmar… (1) ; l. 3233 Testing Language Model Agents Safely in the Wild… (2) ; l. 3253 Hidden in Plain Text: Emergence & Mitigation of … (1) ; l. 3266 Coup probes: Catching catastrophes with probes t… (1) ; l. 3466 Balancing Label Quantity and Quality for Scalabl… (1) ; l. 3489 The Internal State of an LLM Knows When It’s Lyi… (2) ; l. 3554 AgentDojo: A Dynamic Environment to Evaluate Pro… (3)
  — EN : l. 3223 In the sheets (14) (1) ; l. 3287 GPQA: A Graduate-Level Google-Proof Q&A Benchmar… (1) ; l. 3473 Testing Language Model Agents Safely in the Wild… (2) ; l. 3493 Hidden in Plain Text: Emergence & Mitigation of … (1) ; l. 3506 Coup probes: Catching catastrophes with probes t… (1) ; l. 3643 Weak-to-Strong Reasoning — Yuqing Yang, Yan Ma, … (1) ; l. 3705 Balancing Label Quantity and Quality for Scalabl… (1) ; l. 3727 The Internal State of an LLM Knows When It’s Lyi… (2) ; l. 3781 Persistent Pre-training Poisoning of LLMs — Yimi… (1) ; l. 3791 AgentDojo: A Dynamic Environment to Evaluate Pro… (3) ; … (+1 sections)
- `volet11_1_a_20` — FR : l. 3809 7 · « How would you prevent bad actors from misa… (3)
  — EN : l. 4057 7 · « How would you prevent bad actors from misa… (3)
- `volet11_21_a_52` — FR : l. 4156 22 · « How would you tell that a model is being … (1) ; l. 4294 30 · « Can a trait be transmitted through data t… (3) ; l. 4709 51 · « Given a model that already knows somethin… (1)
  — EN : l. 4429 22 · « How would you tell that a model is being … (1) ; l. 4482 25 · « Why would copies of the same model co-var… (1) ; l. 4579 30 · « Can a trait be transmitted through data t… (6) ; l. 5016 51 · « Given a model that already knows somethin… (1)
- `volet11_53_et_fin` — FR : l. 4809 59 · « Misuse or misalignment — which worries yo… (1) ; l. 4836 61 · « How would you red-team a model? » (I.9) (1) ; l. 5003 A8 · « How do you think about the dual-use of yo… (2) ; l. 5336 B13 · « Can honesty be trained rather than detec… (1)
  — EN : l. 5121 59 · « Misuse or misalignment — which worries yo… (1) ; l. 5149 61 · « How would you red-team a model? » (I.9) (1) ; l. 5327 A8 · « How do you think about the dual-use of yo… (2) ; l. 5661 B13 · « Can honesty be trained rather than detec… (1)

---

## 18. Désapprentissage et ré-élicitation — *Unlearning and re-elicitation*

- **Maison** : tranche `volet2_E_a_I` ; FR : volet 2, §I · interventions d'entraînement et unlearning (après « En pratique — l'unlearning mis à l'épreuve ») ; EN : Part 2, §I · training interventions and unlearning (after "In practice — unlearning put to the test").
- **Limites** : 6 ; **parades** : 3.
- **Ancre FR** (ligne 840 de la v3.5 FR ; l'encadré s'insère juste après) :

~~~text
En pratique — l’unlearning mis à l’épreuve (Deeb et Roger). Le but était de vérifier une promesse fragile : l’unlearning retire-t-il vraiment l’information des poids, ou la masque-t-il ? La méthode de ré-élicitation y répond directement : on désapprend un savoir dangereux (mesuré par un benchmark comme WMDP), puis on finetune le modèle sur une partie des faits désappris et l’on mesure s’il retrouve les autres — des faits construits indépendants, pour que le finetuning ne puisse pas les enseigner. Le constat — que l’information « désapprise » refait souvent surface — montre pourquoi le bon critère de validation n’est pas « le modèle ne sait plus répondre maintenant » mais « il reste ignorant des faits tenus à part après un finetuning d’un budget fixé sur les autres, pendant qu’un modèle connu pour masquer les retrouve au même budget » — une borne à ce budget, pas une certification (volet M, M5).
~~~

- **Ancre EN** (ligne 934 de la v3.5 EN) :

~~~text
In practice — unlearning put to the test (Deeb and Roger). The goal was to check a fragile promise: does unlearning really remove the information from the weights, or does it mask it? The re-elicitation method answers this directly: we unlearn a piece of dangerous knowledge (measured by a benchmark such as WMDP), then fine-tune the model on part of the unlearned facts and measure whether it recovers the others — facts constructed to be independent, so that the fine-tuning cannot teach them. The finding — that the "unlearned" information often resurfaces — shows why the right validation criterion is not "the model can no longer answer now" but "it stays ignorant of the held-out facts after a fine-tuning of a fixed budget on the others, while a model known to mask recovers them at the same budget" — a bound at that budget, not a certification (Part M, M5).
~~~

**Encadré complet, français :**

~~~markdown
> **⚠ Limites et parades — Désapprentissage et ré-élicitation** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Masquer n'est pas retirer : sur l'information de pré-entraînement, les taux de récupération dépassent 88 %. *(source : cours, volet 10, Deeb et Roger)*
>   **Parade :** La ré-élicitation contre une référence jamais entraînée, au même budget, avec un modèle connu pour masquer comme cas connu ; dire une borne, « not elicitable at this budget ». *(source : cours, volet M, M4 et M5 ; cours, volet 2, §I)*
> - **Limite :** Un petit fine-tuning peut enseigner : des moitiés de faits liés s'enseignent l'une l'autre. *(source : cours, volet M, M9)*
>   **Parade :** Des faits construits indépendants, et la référence jamais entraînée. *(source : cours, volet 2, §I ; cours, volet M, M9)*
> - **Limite :** Ne pas lire n'est pas être absent : après désapprentissage, le logit lens ne lit plus rien quand retirer une direction par couche rend 64,7 % ; des sondes échouent sur un modèle qui reste jailbreakable. *(source : cours, volet 10, Łucki et al. ; cours, volet 10, Deeb et Roger)*
>   **Parade :** Trancher par une intervention, jamais par une lecture. *(source : cours, volet 10, Łucki et al. ; fiches, partie C)*
> - **Limite :** Le réentraînement sur des faits indépendants ne vaut que pour des faits à faible fuite, pas pour des capacités. *(source : cours, volet 10, Deeb et Roger)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** Le masquage sélectif des gradients n'est montré que sur de petits modèles. *(source : cours, volet 2, §I, JB10)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** Le désapprentissage au niveau des activations « has yet to yield competitive results ». *(source : fiche 5)*
>   **Parade :** aucune connue ; on le dit.
~~~

**Encadré complet, anglais :**

~~~markdown
> **⚠ Limits and workarounds — Unlearning and re-elicitation** *(v3.6, 2 October 2026)*
>
> - **Limit:** Masking is not removing: on pretraining information, recovery rates exceed 88%. *(source: course, Part 10, Deeb and Roger)*
>   **Workaround:** Re-elicitation against a never-trained reference, at the same budget, with a model known to mask as the known case; state a bound, "not elicitable at this budget". *(source: course, Part M, M4 and M5; course, Part 2, §I)*
> - **Limit:** A small fine-tune can teach: halves of related facts teach each other. *(source: course, Part M, M9)*
>   **Workaround:** Facts built to be independent, and the never-trained reference. *(source: course, Part 2, §I; course, Part M, M9)*
> - **Limit:** Not read is not absent: after unlearning, the logit lens reads nothing while removing one direction per layer restores 64.7%; probes fail on a model that can still be jailbroken. *(source: course, Part 10, Łucki et al.; course, Part 10, Deeb and Roger)*
>   **Workaround:** Decide by an intervention, never by a reading. *(source: course, Part 10, Łucki et al.; reading sheets, part C)*
> - **Limit:** Retraining on independent facts works only for low-leakage facts, not for capabilities. *(source: course, Part 10, Deeb and Roger)*
>   **Workaround:** none known; say so.
> - **Limit:** Selective gradient masking is shown only on small models. *(source: course, Part 2, §I, JB10)*
>   **Workaround:** none known; say so.
> - **Limit:** Activation-level unlearning "has yet to yield competitive results". *(source: reading sheet 5)*
>   **Workaround:** none known; say so.
~~~

**Renvoi d'une ligne :**

~~~markdown
> ⚠ **Limites et parades** : désapprentissage et ré-élicitation → volet 2, §I (après « En pratique — l'unlearning mis à l'épreuve ») *(v3.6)*
> ⚠ **Limits and workarounds**: unlearning and re-elicitation → Part 2, §I (after "In practice — unlearning put to the test") *(v3.6)*
~~~

**Où un renvoi ou un avertissement ponctuel est conseillé :**

- `volet_M` — FR l. 365 : M9 · Un cas complet, avant et après : la première question vitale · EN l. 432 : M9 · A complete case, before and after: the first vital question — renvoi.
- `volet3` — FR l. 1029 : 6. Le domaine « divers » : désapprentissage et gouvernance multi-agents · EN l. 1155 : 6. The "miscellaneous" domain: unlearning and multi-agent governance — renvoi.
- `volets4_5_entete` — FR l. 1203 : L’unlearning mis à l’épreuve (Deeb et Roger) · EN l. 1343 : Unlearning put to the test (Deeb and Roger) — renvoi.
- `volet7_B_et_D` — FR l. 2000 : F·36 · Beyond Data Filtering : Knowledge Localization (SGTM) — Shilov (Fellows), Gema, Clo… · EN l. 2165 : F·36 · Beyond Data Filtering : Knowledge Localization (SGTM) — Shilov (Fellows), Gema, Clo… — renvoi.
- `volet7_A_et_C` — FR l. 2472 : F·17 · L'unlearning mis à l'épreuve (Deeb et Roger) — [P·unl] · EN l. 2606 : F·17 · L'unlearning mis à l'épreuve (Deeb and Roger) — [P·unl] — renvoi.
- `volets8_9` — FR l. 2912 : 9 · Miscellaneous · EN l. 3069 : 9 · Miscellaneous — renvoi.
- `volet10` — FR l. 3621 : Miscellaneous › Unlearning dangerous information and capabilities · EN l. 3857 : Miscellaneous › Unlearning dangerous information and capabilities — renvoi.
- `volet11_1_a_20` — FR l. 3809 : 7 · « How would you prevent bad actors from misaligning an LLM for harmful use? » *(questi… · EN l. 4057 : 7 · « How would you prevent bad actors from misaligning an LLM for harmful use? » *(questi… — renvoi.
- `volet11_21_a_52` — FR l. 4709 : 51 · « Given a model that already knows something dangerous, what would convince you it ha… · EN l. 5016 : 51 · « Given a model that already knows something dangerous, what would convince you it ha… — renvoi.
- `volet11_53_et_fin` — FR l. 5246 : B9 · « How would you build a safety case that a model cannot sandbag your dangerous-capabi… · EN l. 5571 : B9 · « How would you build a safety case that a model cannot sandbag your dangerous-capabi… — renvoi.

**Où il revient** (relevé automatique, motifs FR `désapprentissage|désappri|unlearn|ré-élicitation` / EN `unlearn|re-elicitation` ; sections, avec le nombre de lignes touchées) :

- `tete_volet1` — FR : l. 108 6. La carte du territoire (l’aperçu, avant le dé… (1) ; l. 162 Q10. « Défense en profondeur : quelles technique… (1)
  — EN : l. 161 6. The map of the territory (the overview, befor… (1) ; l. 226 Q10. "Defense in depth: which safety techniques … (1)
- `volet_M` — FR : l. 257 M4 · Le contrôle : ce qu'il écarte, et il doit s… (1) ; l. 298 M5 · Le nul et le cas connu (1) ; l. 365 M9 · Un cas complet, avant et après : la premièr… (2)
  — EN : l. 324 M4 · The control: what it rules out, and it must… (1) ; l. 365 M5 · The null and the known case (1) ; l. 432 M9 · A complete case, before and after: the firs… (2) ; l. 456 M10 · The checklist, to reread before each rehea… (1)
- `volet2_E_a_I` — FR : l. 834 I. Interventions d’entraînement & unlearning — c… (3) ; l. 842 Cas d'application — interventions d'entraînement… (7)
  — EN : l. 927 I. Training interventions & unlearning — changin… (3) ; l. 936 Worked case — training interventions and unlearn… (8)
- `volet3` — FR : l. 1029 6. Le domaine « divers » : désapprentissage et g… (2) ; l. 1103 PARTIE IV — SYNTHÈSE : comment tout s’emboîte, e… (1)
  — EN : l. 1155 6. The "miscellaneous" domain: unlearning and mu… (2) ; l. 1228 SECTION IV — SYNTHESIS: how everything fits toge… (1)
- `volets4_5_entete` — FR : l. 1203 L’unlearning mis à l’épreuve (Deeb et Roger) (2) ; l. 1326 Les papiers — quatre niveaux (1)
  — EN : l. 1254 The key papers, told one by one (2) ; l. 1506 The papers — four levels (1)
- `volet6` — FR : l. 1458 4. La page « Recommended Directions » et ses sei… (2)
  — EN : l. 1579 2. Your results, as your dossier carries them on… (1) ; l. 1597 4. The "Recommended Directions" page and its six… (2) ; l. 1676 7. What these supplements change in Parts 1 to 5 (2)
- `volet7_B_et_D` — FR : l. 2000 F·36 · Beyond Data Filtering : Knowledge Localiz… (2)
  — EN : l. 2165 F·36 · Beyond Data Filtering : Knowledge Localiz… (2)
- `volet7_A_et_C` — FR : l. 2472 F·17 · L'unlearning mis à l'épreuve (Deeb et Rog… (5) ; l. 2646 F·58 · Recommendations for Technical AI Safety R… (1)
  — EN : l. 2606 F·17 · L'unlearning mis à l'épreuve (Deeb and Ro… (5) ; l. 2778 F·58 · Recommendations for Technical AI Safety R… (1)
- `volets8_9` — FR : l. 2666 VOLET 8 — Références, dans l'ordre des fiches (1) ; l. 2912 9 · Miscellaneous (3) ; l. 2928 10 · La lecture d'ensemble, en trois phrases pou… (1)
  — EN : l. 2804 PART 8 — References, in the order of the sheets (1) ; l. 3069 9 · Miscellaneous (3) ; l. 3085 10 · The overall reading, in three sentences for… (5)
- `volet10` — FR : l. 2980 Dans les fiches (14) (1) ; l. 2998 Descriptions justes mais incomplètes (9) (2) ; l. 3621 Miscellaneous › Unlearning dangerous information… (1) ; l. 3623 An Adversarial Perspective on Machine Unlearning… (6) ; l. 3633 The WMDP Benchmark: Measuring and Reducing Malic… (5) ; l. 3643 Do Unlearning Methods Remove Information from La… (3)
  — EN : l. 3223 In the sheets (14) (1) ; l. 3241 Descriptions that are correct but incomplete (9) (2) ; l. 3857 Miscellaneous › Unlearning dangerous information… (1) ; l. 3859 An Adversarial Perspective on Machine Unlearning… (6) ; l. 3869 The WMDP Benchmark: Measuring and Reducing Malic… (5) ; l. 3879 Do Unlearning Methods Remove Information from La… (4)
- `volet11_21_a_52` — FR : l. 4709 51 · « Given a model that already knows somethin… (3)
  — EN : l. 5016 51 · « Given a model that already knows somethin… (3)
- `volet11_53_et_fin` — FR : l. 4809 59 · « Misuse or misalignment — which worries yo… (1)
  — EN : l. 5121 59 · « Misuse or misalignment — which worries yo… (1)

---

## 19. Dictionnaires et SAE — *Dictionaries and SAEs*

- **Maison** : tranche `volets4_5_entete` ; FR : volet 4 · Towards puis Scaling Monosemanticity (paragraphe « Le contexte ») ; EN : Part 4 · Towards then Scaling Monosemanticity (paragraph "The context").
- **Limites** : 6 ; **parades** : 5.
- **Ancre FR** (ligne 1157 de la v3.5 FR ; l'encadré s'insère juste après) :

~~~text
Le contexte : un neurone est polysémantique (superposition), donc illisible directement ; on voulait des unités interprétables, à l’échelle d’un vrai modèle. La méthode est le sparse autoencoder (SAE), un dictionnaire appris qui décompose l’activation en milliers de features parcimonieuses et monosémantiques. Le résultat : on extrait des features correspondant à des concepts précis, du concret à l’abstrait, et on les valide causalement — forcer une feature pousse le modèle à produire le concept (l’exemple resté célèbre étant une feature « pont du Golden Gate » qui, amplifiée, fait parler le modèle de ce pont à tout propos). Le maillon fragile : feature splitting (un concept éclaté en plusieurs features), features mortes, et surtout le terme d’erreur de reconstruction — le dictionnaire ne capture pas tout — sans parler de l’absence de vérité-terrain sur ce qu’une feature « veut dire ». Extension : utiliser la décomposition SAE pour expliquer pourquoi certaines directions se pilotent mal — ta Phase 3.
~~~

- **Ancre EN** (ligne 1297 de la v3.5 EN) :

~~~text
The context: a neuron is polysemantic (superposition), hence unreadable directly; the aim was interpretable units, at the scale of a real model. The method is the sparse autoencoder (SAE), a learned dictionary that decomposes the activation into thousands of sparse, monosemantic features. The result: features corresponding to precise concepts are extracted, from the concrete to the abstract, and they are validated causally — forcing a feature pushes the model to produce the concept (the example that became famous being a "Golden Gate Bridge" feature which, when amplified, makes the model talk about that bridge at every turn). The weak link: feature splitting (one concept broken up into several features), dead features, and above all the reconstruction error term — the dictionary does not capture everything — not to mention the absence of ground truth on what a feature "means". Extension: use SAE decomposition to explain why some directions steer poorly — your Phase 3.
~~~

**Encadré complet, français :**

~~~markdown
> **⚠ Limites et parades — Dictionnaires et SAE** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** L'erreur de reconstruction : le SAE ouvert de Goodfire pour Llama 3.1 8B laisse 86,8 % de la variance au résidu, et le signal lu y est porté. *(source : README du dépôt ; cours, volet 4, Monosemanticity)*
>   **Parade :** Lire le signal sur la reconstruction et sur le résidu ; pour trancher entre « features absentes du dictionnaire » et « dictionnaire qui perd trop », aucune parade connue, on le dit. *(source : README du dépôt)*
> - **Limite :** Insérer le dictionnaire coûte de la performance : sur GPT-2 small, 10 % sur les données de tâche, 40 % sur la distribution complète. *(source : fiche 5)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** Features éclatées, features mortes, dépendance au dictionnaire, et aucune vérité-terrain sur ce qu'une feature « veut dire ». *(source : cours, volet 4, Monosemanticity ; cours, volet 5, sujet 3)*
>   **Parade :** Valider feature par feature — l'ablation pour la nécessité, le pilotage isolé pour la suffisance — avec une géométrie connue comme cas connu, la variété du comptage. *(source : cours, volet 5, sujet 3 ; cours, volet 2, §D, K64)*
> - **Limite :** En lecture seule, le SAE n'a pas aidé à prédire des contrefactuels mieux que le transcript. *(source : fiche 4 ; cours, volet 7, F·30)*
>   **Parade :** La barre : battre la boîte noire sur des éditions qui dissocient la surface de la variable interne. *(source : fiche 4)*
> - **Limite :** Des explications plausibles existent pour des directions arbitraires. *(source : fiche 5)*
>   **Parade :** Valider par la prédiction, mieux que des baselines. *(source : fiche 5)*
> - **Limite :** Deux dictionnaires peuvent reconstruire aussi bien et découper différemment. *(source : cours, volet 2, §D, K64)*
>   **Parade :** Piloter les features une à une contre des directions aléatoires à dommage apparié, sur une tâche à géométrie connue, avec de nouvelles graines. *(source : cours, volet 2, §D, K64)*
~~~

**Encadré complet, anglais :**

~~~markdown
> **⚠ Limits and workarounds — Dictionaries and SAEs** *(v3.6, 2 October 2026)*
>
> - **Limit:** Reconstruction error: the open-source Goodfire SAE for Llama 3.1 8B leaves 86.8% of the variance in the residual, and the read signal lives there. *(source: repository README; course, Part 4, Monosemanticity)*
>   **Workaround:** Read the signal on the reconstruction and on the residual; to decide between "features absent from the dictionary" and "dictionary too lossy", none known, say so. *(source: repository README)*
> - **Limit:** Splicing in the dictionary costs performance: on GPT-2 small, 10% on task data, 40% on the full distribution. *(source: reading sheet 5)*
>   **Workaround:** none known; say so.
> - **Limit:** Split features, dead features, dependence on the dictionary, and no ground truth on what a feature "means". *(source: course, Part 4, Monosemanticity; course, Part 5, topic 3)*
>   **Workaround:** Validate feature by feature — ablation for necessity, isolated steering for sufficiency — with a known geometry as the known case, the counting manifold. *(source: course, Part 5, topic 3; course, Part 2, §D, K64)*
> - **Limit:** Read-only, the SAE did not help predict counterfactuals better than the transcript. *(source: reading sheet 4; course, Part 7, F·30)*
>   **Workaround:** The bar: beat the black box on edits that dissociate surface features from the internal variable. *(source: reading sheet 4)*
> - **Limit:** Plausible explanations exist for arbitrary directions. *(source: reading sheet 5)*
>   **Workaround:** Validate by prediction, better than baselines. *(source: reading sheet 5)*
> - **Limit:** Two dictionaries can reconstruct equally well and carve differently. *(source: course, Part 2, §D, K64)*
>   **Workaround:** Steer the features one at a time against random directions at matched damage, on a task with known geometry, with new seeds. *(source: course, Part 2, §D, K64)*
~~~

**Renvoi d'une ligne :**

~~~markdown
> ⚠ **Limites et parades** : dictionnaires et SAE → volet 4, Towards puis Scaling Monosemanticity *(v3.6)*
> ⚠ **Limits and workarounds**: dictionaries and SAEs → Part 4, Towards then Scaling Monosemanticity *(v3.6)*
~~~

**Où un renvoi ou un avertissement ponctuel est conseillé :**

- `volets4_5_entete` — FR l. 1185 : Auditing Hidden Objectives (Anthropic, Marks et al.) · EN l. 1325 : Auditing Hidden Objectives (Anthropic, Marks et al.) — renvoi.
- `volets4_5_entete` — FR l. 1261 : Sujet 3 — Décomposer un concept diffus en features actionnables · EN l. 1439 : Topic 3 — Decomposing a diffuse concept into actionable features — renvoi.
- `volets4_5_entete` — FR l. 1295 : Sujet 9 — Alignment auditing (MOYEN) · EN l. 1474 : Topic 9 — Alignment auditing (MEDIUM) — renvoi.
- `volet7_B_et_D` — FR l. 1812 : F·30 · CHIVE — Would This Change Your Answer? — Karvonen (Fellows), Ong, Kantamneni, Marks… · EN l. 1977 : F·30 · CHIVE — Would This Change Your Answer? — Karvonen (Fellows), Ong, Kantamneni, Marks… — renvoi.
- `volet7_A_et_C` — FR l. 2249 : F·8 · Towards puis Scaling Monosemanticity (Anthropic, 2023-2024) — [P·mono] · EN l. 2383 : F·8 · Towards then Scaling Monosemanticity (Anthropic, 2023-2024) — [P·mono] — renvoi.
- `volet7_A_et_C` — FR l. 2376 : F·13 · Auditing Language Models for Hidden Objectives (Marks et al., Anthropic, 2025) — [P… · EN l. 2510 : F·13 · Auditing Language Models for Hidden Objectives (Marks et al., Anthropic, 2025) — [P… — renvoi.
- `volet11_21_a_52` — FR l. 4473 : 38 · « Does interpretability actually help explain behaviour — and can a model report its … · EN l. 4767 : 38 · « Does interpretability actually help explain behaviour — and can a model report its … — renvoi.

**Où il revient** (relevé automatique, motifs FR `\bSAE|dictionnaire|autoencodeur.? épars|sparse autoencoder` / EN `\bSAE|dictionar|sparse autoencoder` ; sections, avec le nombre de lignes touchées) :

- `volet2_A_a_D` — FR : l. 627 D. Interprétabilité mécaniste — ouvrir la boîte … (2) ; l. 635 Cas d'application — l'interprétabilité mécaniste… (5)
  — EN : l. 715 D. Mechanistic interpretability — opening the bo… (2) ; l. 724 Worked case — mechanistic interpretability: "Two… (9)
- `volet3` — FR : l. 1053 PARTIE II — LES ÉQUIPES : qui fait quoi chez (1) ; l. 1103 PARTIE IV — SYNTHÈSE : comment tout s’emboîte, e… (1)
  — EN : l. 1180 SECTION II — THE TEAMS: who does what at (1) ; l. 1228 SECTION IV — SYNTHESIS: how everything fits toge… (1)
- `volets4_5_entete` — FR : l. 1119 Sleeper Agents (Anthropic, Hubinger et al.) (1) ; l. 1139 Representation Engineering (RepE) (Zou et al.) (1) ; l. 1153 Towards puis Scaling Monosemanticity (Anthropic, (1) ; l. 1185 Auditing Hidden Objectives (Anthropic, Marks et … (1) ; l. 1203 L’unlearning mis à l’épreuve (Deeb et Roger) (1) ; l. 1219 1. La thèse-signature : l’écart représentation–c… (1) ; l. 1251 A. Tes sujets FORT — ta thèse peut être la colon… (3) ; l. 1285 B. Leurs sujets — méthodothèque, dosage léger ou… (1) ; l. 1326 Les papiers — quatre niveaux (1)
  — EN : l. 1254 The key papers, told one by one (5) ; l. 1389 1. The signature thesis: the representation–caus… (1) ; l. 1428 A. Your STRONG topics — your thesis can be the b… (3) ; l. 1463 B. Their topics — method toolkit, light or zero … (1) ; l. 1506 The papers — four levels (1)
- `volet6` — FR : l. 1402 2. Tes résultats, tels que ton dossier les porte… (2)
  — EN : l. 1579 2. Your results, as your dossier carries them on… (2)
- `volet7_B_et_D` — FR : l. 1812 F·30 · CHIVE — Would This Change Your Answer? — … (1)
  — EN : l. 1977 F·30 · CHIVE — Would This Change Your Answer? — … (1)
- `volet7_A_et_C` — FR : l. 2072 F·1 · Sleeper Agents (Hubinger et al., Anthropic… (1) ; l. 2200 F·6 · Discovering Latent Knowledge Without Super… (1) ; l. 2224 F·7 · Contrastive Activation Addition et Inferen… (1) ; l. 2249 F·8 · Towards puis Scaling Monosemanticity (Anth… (6) ; l. 2376 F·13 · Auditing Language Models for Hidden Objec… (2) ; l. 2472 F·17 · L'unlearning mis à l'épreuve (Deeb et Rog… (1)
  — EN : l. 2206 F·1 · Sleeper Agents (Hubinger et al., Anthropic… (1) ; l. 2334 F·6 · Discovering Latent Knowledge Without Super… (1) ; l. 2358 F·7 · Contrastive Activation Addition and Infere… (1) ; l. 2383 F·8 · Towards then Scaling Monosemanticity (Anth… (7) ; l. 2510 F·13 · Auditing Language Models for Hidden Objec… (2) ; l. 2606 F·17 · L'unlearning mis à l'épreuve (Deeb and Ro… (1)
- `volet11_1_a_20` — FR : l. 3727 3 · « And rank one? Didn't a single direction wo… (1)
  — EN : —
- `volet11_21_a_52` — FR : l. 4473 38 · « Does interpretability actually help expla… (1)
  — EN : l. 4767 38 · « Does interpretability actually help expla… (1)
- `volet11_53_et_fin` — FR : l. 5016 A9 à A17 · Neuf questions moins probables, en ré… (1)
  — EN : l. 5341 A9 à A17 · Neuf questions moins probables, en ré… (1)

---

## 20. Graphes d'attribution — *Attribution graphs*

- **Maison** : tranche `volets4_5_entete` ; FR : volet 4 · Circuit Tracing / On the Biology of a Large Language Model (paragraphe « Le contexte ») ; EN : Part 4 · Circuit Tracing / On the Biology of a Large Language Model (paragraph "The context").
- **Limites** : 4 ; **parades** : 4.
- **Ancre FR** (ligne 1161 de la v3.5 FR ; l'encadré s'insère juste après) :

~~~text
Le contexte : passer du « quel concept existe ? » au « quelle est la mécanique du calcul ? ». La méthode des attribution graphs trace le flux de features à travers les couches pour reconstituer le calcul. Le résultat : on a pu cartographier des mécanismes réels — raisonnement en plusieurs étapes, planification de la rime avant d’écrire le vers, features multilingues partagées, circuits du refus. Le maillon fragile : les graphes sont partiels et approximatifs — ils n’expliquent qu’une fraction du calcul, et la démarche est coûteuse en travail humain. Extension : automatiser le tracing, ou relier un circuit identifié à une intervention de contrôle fiable.
~~~

- **Ancre EN** (ligne 1301 de la v3.5 EN) :

~~~text
The context: move from "which concept exists?" to "what is the mechanics of the computation?". The attribution graphs method traces the flow of features across layers to reconstruct the computation. The result: real mechanisms could be mapped — multi-step reasoning, planning the rhyme before writing the line, shared multilingual features, refusal circuits. The weak link: the graphs are partial and approximate — they explain only a fraction of the computation, and the approach is costly in human labor. Extension: automate the tracing, or link an identified circuit to a reliable control intervention.
~~~

**Encadré complet, français :**

~~~markdown
> **⚠ Limites et parades — Graphes d'attribution** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Les graphes sont partiels et approximatifs, n'expliquent qu'une fraction du calcul et coûtent du travail humain. *(source : cours, volet 4, Circuit Tracing)*
>   **Parade :** Les traiter comme une hypothèse, validée par perturbation. *(source : cours, volet 7, F·9)*
> - **Limite :** Le graphe n'est pas le mécanisme. *(source : cours, volet 7, F·9)*
>   **Parade :** Exiger qu'il prédise une contrefactuelle. *(source : cours, volet 7, F·9 ; fiche 5)*
> - **Limite :** Des circuits lisibles peuvent être infidèles. *(source : cours, volet 2, §D, K64)*
>   **Parade :** Comparer, à dommage apparié, à des directions aléatoires et à une géométrie connue. *(source : cours, volet 2, §D, K64)*
> - **Limite :** Affirmer qu'aucun mécanisme ne fait mal agir le modèle exige décomposition et description ; la vérification formelle n'a donné de bornes que sur un transformer à une couche. *(source : fiche 5)*
>   **Parade :** Offrir une borne restreinte, pas une affirmation d'absence. *(source : fiche 5)*
~~~

**Encadré complet, anglais :**

~~~markdown
> **⚠ Limits and workarounds — Attribution graphs** *(v3.6, 2 October 2026)*
>
> - **Limit:** The graphs are partial and approximate, explain only a fraction of the computation and cost human labour. *(source: course, Part 4, Circuit Tracing)*
>   **Workaround:** Treat them as a hypothesis, validated by perturbation. *(source: course, Part 7, F·9)*
> - **Limit:** The graph is not the mechanism. *(source: course, Part 7, F·9)*
>   **Workaround:** Require it to predict a counterfactual. *(source: course, Part 7, F·9; reading sheet 5)*
> - **Limit:** Readable circuits can be unfaithful. *(source: course, Part 2, §D, K64)*
>   **Workaround:** Compare, at matched damage, with random directions and with a known geometry. *(source: course, Part 2, §D, K64)*
> - **Limit:** Claiming that no mechanism makes the model misbehave requires decomposition and description; formal verification has given bounds only on a one-layer transformer. *(source: reading sheet 5)*
>   **Workaround:** Offer a restricted bound, not a claim of absence. *(source: reading sheet 5)*
~~~

**Renvoi d'une ligne :**

~~~markdown
> ⚠ **Limites et parades** : graphes d'attribution → volet 4, Circuit Tracing *(v3.6)*
> ⚠ **Limits and workarounds**: attribution graphs → Part 4, Circuit Tracing *(v3.6)*
~~~

**Où un renvoi ou un avertissement ponctuel est conseillé :**

- `volets4_5_entete` — FR l. 1261 : Sujet 3 — Décomposer un concept diffus en features actionnables · EN l. 1439 : Topic 3 — Decomposing a diffuse concept into actionable features — renvoi.
- `volets4_5_entete` — FR l. 1295 : Sujet 9 — Alignment auditing (MOYEN) · EN l. 1474 : Topic 9 — Alignment auditing (MEDIUM) — renvoi.
- `volet7_A_et_C` — FR l. 2274 : F·9 · Circuit Tracing / On the Biology of a Large Language Model (Anthropic, 2025) — [P·19… · EN l. 2408 : F·9 · Circuit Tracing / On the Biology of a Large Language Model (Anthropic, 2025) — [P·19… — renvoi.

**Où il revient** (relevé automatique, motifs FR `graphe.? d.attribution|attribution graph|circuit` / EN `attribution graph|circuit` ; sections, avec le nombre de lignes touchées) :

- `tete_volet1` — FR : l. 122 Q2. « Quel est, selon toi, le problème non résol… (1)
  — EN : l. 178 Q2. "What, in your view, is the most important u… (1)
- `volet2_A_a_D` — FR : l. 627 D. Interprétabilité mécaniste — ouvrir la boîte … (2) ; l. 635 Cas d'application — l'interprétabilité mécaniste… (1)
  — EN : l. 715 D. Mechanistic interpretability — opening the bo… (2) ; l. 724 Worked case — mechanistic interpretability: "Two… (1)
- `volet2_E_a_I` — FR : l. 842 Cas d'application — interventions d'entraînement… (1)
  — EN : l. 936 Worked case — training interventions and unlearn… (1)
- `volet3` — FR : l. 1053 PARTIE II — LES ÉQUIPES : qui fait quoi chez (1)
  — EN : l. 1180 SECTION II — THE TEAMS: who does what at (1)
- `volets4_5_entete` — FR : l. 1153 Towards puis Scaling Monosemanticity (Anthropic, (2) ; l. 1251 A. Tes sujets FORT — ta thèse peut être la colon… (1) ; l. 1326 Les papiers — quatre niveaux (1)
  — EN : l. 1254 The key papers, told one by one (2) ; l. 1428 A. Your STRONG topics — your thesis can be the b… (1) ; l. 1506 The papers — four levels (1)
- `volet6` — FR : —
  — EN : l. 1676 7. What these supplements change in Parts 1 to 5 (1)
- `volet7_A_et_C` — FR : l. 2176 F·5 · Representation Engineering (Zou et al., 20… (1) ; l. 2274 F·9 · Circuit Tracing / On the Biology of a Larg… (7)
  — EN : l. 2310 F·5 · Representation Engineering (Zou et al., 20… (1) ; l. 2408 F·9 · Circuit Tracing / On the Biology of a Larg… (7)
- `volets8_9` — FR : l. 2666 VOLET 8 — Références, dans l'ordre des fiches (1) ; l. 2763 3 · Understanding model cognition — « What are o… (1) ; l. 2798 6 · AI control — « Can we ensure safety by deplo… (1)
  — EN : l. 2804 PART 8 — References, in the order of the sheets (1) ; l. 2920 3 · Understanding model cognition — "What are ou… (1) ; l. 2955 6 · AI control — "Can we ensure safety by deploy… (1) ; l. 3085 10 · The overall reading, in three sentences for… (1)
- `volet10` — FR : l. 2946 0 · Ce qui a été lu, et comment (1) ; l. 3106 Interpreting the Second-Order Effects of Neurons… (1) ; l. 3276 Improving Alignment and Robustness with Circuit … (2) ; l. 3299 Eliciting Latent Knowledge from “Quirky” Languag… (1) ; l. 3501 Representation Engineering: A Top-Down Approach … (1)
  — EN : l. 3189 0 · What was read, and how (1) ; l. 3348 Interpreting the Second-Order Effects of Neurons… (1) ; l. 3516 Improving Alignment and Robustness with Circuit … (2) ; l. 3539 Eliciting Latent Knowledge from “Quirky” Languag… (1) ; l. 3739 Representation Engineering: A Top-Down Approach … (1)
- `volet11_53_et_fin` — FR : l. 5016 A9 à A17 · Neuf questions moins probables, en ré… (1)
  — EN : l. 5341 A9 à A17 · Neuf questions moins probables, en ré… (1)

---

## 21. Autoencodeurs en langage naturel (NLA) — *Natural-language autoencoders (NLAs)*

- **Maison** : tranche `volets4_5_entete` ; FR : volet 4 · La vague récente sur la cognition du modèle (fin du passage, « Extension ») ; EN : Part 4 · The recent wave on model cognition (end of the passage, "Extension").
- **Limites** : 6 ; **parades** : 5.
- **Ancre FR** (ligne 1167 de la v3.5 FR ; l'encadré s'insère juste après) :

~~~text
Extension : valider causalement que ce que le modèle « rapporte » de lui-même correspond bien à une intervention sur l’état interne correspondant.
~~~

- **Ancre EN** (ligne 1307 de la v3.5 EN) :

~~~text
Extension: causally validate that what the model "reports" about itself does correspond to an intervention on the corresponding internal state.
~~~

**Encadré complet, français :**

~~~markdown
> **⚠ Limites et parades — Autoencodeurs en langage naturel (NLA)** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Le NLA peut confabuler : hallucinations fréquentes, pas d'ancrage mécaniste. *(source : fiche 18 ; fiche 3)*
>   **Parade :** Corroborer par des méthodes indépendantes, comme dans l'audit d'Opus 4.6, et garder le décodeur à part. *(source : fiche 18)*
> - **Limite :** Un critère qui se valide lui-même : la reconstruction aller-retour ; dans l'audit, les contrôles de déploiement étaient mesurés par le NLA lui-même (2 transcripts signalés sur 50). *(source : fiche 18)*
>   **Parade :** Mesurer les contrôles par un instrument indépendant du NLA. *(source : fiche 18)*
> - **Limite :** Ses sorties décrivent sans énoncer la relation : « X causes Y » pour 0,6 % des affirmations, et aucun gain sur le transcript dans CHIVE. *(source : fiche 4)*
>   **Parade :** La barre : battre la boîte noire sur des éditions qui dissocient la surface de la variable interne. *(source : fiche 4)*
> - **Limite :** Les mesures de la conscience d'évaluation — sonde, NLA, question de suivi — ne sont que faiblement corrélées. *(source : fiche 2 ; cours, volet 3, §3, K70)*
>   **Parade :** Trianguler, et dire laquelle a fondé quel chiffre. *(source : cours, volet 5, sujet 4 ; cours, volet M, M4)*
> - **Limite :** Ses étiquettes servent de vérité à d'autres détecteurs : le détecteur du J-lens n'est validé que contre elles. *(source : fiche 1 ; fiches, partie B, piège 6)*
>   **Parade :** Valider contre l'écart réel/test et sur des indices tenus à part. *(source : fiche 1)*
> - **Limite :** Une information peut ne pas être verbalisable. *(source : fiche 18)*
>   **Parade :** aucune connue ; on le dit.
~~~

**Encadré complet, anglais :**

~~~markdown
> **⚠ Limits and workarounds — Natural-language autoencoders (NLAs)** *(v3.6, 2 October 2026)*
>
> - **Limit:** The NLA can confabulate: frequent hallucinations, no mechanistic grounding. *(source: reading sheet 18; reading sheet 3)*
>   **Workaround:** Corroborate with independent methods, as in the Opus 4.6 audit, and keep the decoder separate. *(source: reading sheet 18)*
> - **Limit:** A self-validating criterion: round-trip reconstruction; in the audit, the deployment controls were measured by the NLA itself (2 of 50 transcripts flagged). *(source: reading sheet 18)*
>   **Workaround:** Measure the controls with an instrument independent of the NLA. *(source: reading sheet 18)*
> - **Limit:** Its outputs describe without stating the relationship: "X causes Y" for 0.6% of claims, and no gain over the transcript in CHIVE. *(source: reading sheet 4)*
>   **Workaround:** The bar: beat the black box on edits that dissociate surface features from the internal variable. *(source: reading sheet 4)*
> - **Limit:** The measures of evaluation awareness — probe, NLA, follow-up question — are only weakly correlated. *(source: reading sheet 2; course, Part 3, §3, K70)*
>   **Workaround:** Triangulate, and say which one grounded which number. *(source: course, Part 5, topic 4; course, Part M, M4)*
> - **Limit:** Its labels serve as ground truth for other detectors: the J-lens detector is validated only against them. *(source: reading sheet 1; reading sheets, part B, trap 6)*
>   **Workaround:** Validate against the real/test gap and on held-out cues. *(source: reading sheet 1)*
> - **Limit:** Some information may not be verbalizable. *(source: reading sheet 18)*
>   **Workaround:** none known; say so.
~~~

**Renvoi d'une ligne :**

~~~markdown
> ⚠ **Limites et parades** : autoencodeurs en langage naturel → volet 4, La vague récente sur la cognition du modèle *(v3.6)*
> ⚠ **Limits and workarounds**: natural-language autoencoders → Part 4, The recent wave on model cognition *(v3.6)*
~~~

**Où un renvoi ou un avertissement ponctuel est conseillé :**

- `volet3` — FR l. 953 : 3. Le contrôle par le monitoring (AI control) · EN l. 1076 : 3. Control through monitoring (AI control) — renvoi.
- `volets4_5_entete` — FR l. 1267 : Sujet 4 — Mesurer (et faut-il supprimer ?) l’eval-awareness · EN l. 1445 : Topic 4 — Measuring (and should we suppress?) eval-awareness — renvoi.
- `volet7_B_et_D` — FR l. 1812 : F·30 · CHIVE — Would This Change Your Answer? — Karvonen (Fellows), Ong, Kantamneni, Marks… · EN l. 1977 : F·30 · CHIVE — Would This Change Your Answer? — Karvonen (Fellows), Ong, Kantamneni, Marks… — renvoi.
- `volets8_9` — FR l. 2763 : 3 · Understanding model cognition — « What are our models "thinking"? » · EN l. 2920 : 3 · Understanding model cognition — "What are our models "thinking"?" — renvoi.
- `volet11_21_a_52` — FR l. 4473 : 38 · « Does interpretability actually help explain behaviour — and can a model report its … · EN l. 4767 : 38 · « Does interpretability actually help explain behaviour — and can a model report its … — renvoi.
- `volet11_53_et_fin` — FR l. 5141 : B4 · « How would you measure evaluation awareness that the model never verbalizes? » · EN l. 5466 : B4 · « How would you measure evaluation awareness that the model never verbalizes? » — renvoi.
- `volets4_5_entete` — avertissement ponctuel prêt, après FR l. 1269 / EN l. 1447 (texte dans la partie « Par tranche »).

**Où il revient** (relevé automatique, motifs FR `natural.language autoencoder|autoencodeur.? en langage naturel|\bNLA` / EN `natural.language autoencoder|\bNLA` ; sections, avec le nombre de lignes touchées) :

- `volet3` — FR : l. 953 3. Le contrôle par le monitoring (AI control) (1) ; l. 1077 PARTIE III — LES TRAVAUX DU MOMENT (2025-2026) (1)
  — EN : l. 1076 3. Control through monitoring (AI control) (1) ; l. 1202 SECTION III — CURRENT WORK (2025-2026) (1)
- `volets4_5_entete` — FR : l. 1153 Towards puis Scaling Monosemanticity (Anthropic, (1) ; l. 1251 A. Tes sujets FORT — ta thèse peut être la colon… (1)
  — EN : l. 1254 The key papers, told one by one (1) ; l. 1428 A. Your STRONG topics — your thesis can be the b… (1)
- `volet7_B_et_D` — FR : l. 1812 F·30 · CHIVE — Would This Change Your Answer? — … (1)
  — EN : l. 1977 F·30 · CHIVE — Would This Change Your Answer? — … (1)
- `volet7_A_et_C` — FR : l. 2274 F·9 · Circuit Tracing / On the Biology of a Larg… (1)
  — EN : l. 2408 F·9 · Circuit Tracing / On the Biology of a Larg… (1)
- `volet11_21_a_52` — FR : l. 4473 38 · « Does interpretability actually help expla… (1)
  — EN : l. 4767 38 · « Does interpretability actually help expla… (1)

---

## 22. Auto-rapport et introspection — *Self-report and introspection*

- **Maison** : tranche `volets4_5_entete` ; FR : volet 5, partie II, A · sujet 13, Introspection (fin du sujet) ; EN : Part 5, Section II, A · Topic 13, Introspection (end of the topic).
- **Limites** : 6 ; **parades** : 4.
- **Ancre FR** (ligne 1283 de la v3.5 FR ; l'encadré s'insère juste après) :

~~~text
un auto-rapport entraîné, un auto-rapport spontané — et l’on cherche où l’auto-rapport bat la sonde. Raccord : les activation oracles et les natural language autoencoders (Volet 4). Ta passerelle : tes concept vectors sont ce que l’oracle devrait savoir lire — donc ta question (lire implique-t-il contrôler ?) éclaire la fiabilité de l’introspection.
~~~

- **Ancre EN** (ligne 1461 de la v3.5 EN) :

~~~text
a trained self-report, a spontaneous self-report — and you look for where the self-report beats the probe. Connection: activation oracles and natural language autoencoders (Part 4). Your bridge: your concept vectors are what the oracle should be able to read — so your question (does reading imply controlling?) sheds light on the reliability of introspection.
~~~

**Encadré complet, français :**

~~~markdown
> **⚠ Limites et parades — Auto-rapport et introspection** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Rapport n'est pas croyance : Anthropic s'est rétracté d'avoir déduit ce que Claude croyait de ce que Claude disait croire. *(source : fiche 3 ; fiches, partie B, piège 2)*
>   **Parade :** Une lecture indépendante du rapport — le réétiquetage hors contexte des sorties prises une à une —, en disant ce qu'elle ne sépare pas : la prémisse fausse donnée par le dispositif. *(source : fiche 3)*
> - **Limite :** L'introspection est rare et peu fiable : environ 20 % de détection pour Opus 4.1, et « zéro faux positif » ne vaut que pour 100 essais témoins. *(source : fiche 11)*
>   **Parade :** Une vérité-terrain par injection de concept. *(source : fiche 11)*
> - **Limite :** Un modèle entraîné à rapporter peut apprendre à rapporter ce qu'on attend ; rapport ou reconstruction plausible reste ouvert pour les adaptateurs d'introspection. *(source : fiche 11 ; cours, volet 7, F·28)*
>   **Parade :** Modifier l'état interne, contre une direction aléatoire à dégradation appariée, et voir si le rapport suit la sonde ou le prompt. *(source : fiche 11 ; cours, volet 7, F·28)*
> - **Limite :** Les détails rapportés peuvent être embellis ou confabulés, et les conditions sont loin du déploiement. *(source : fiche 11)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** Les réponses aux questions de suivi dépendent de leur formulation. *(source : fiche 3)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** CHIVE ne trouve aucun indice d'accès privilégié d'un modèle à son propre comportement. *(source : fiche 4)*
>   **Parade :** Juger un auto-rapport à ce qu'il prédit des actions suivantes. *(source : fiche 6)*
~~~

**Encadré complet, anglais :**

~~~markdown
> **⚠ Limits and workarounds — Self-report and introspection** *(v3.6, 2 October 2026)*
>
> - **Limit:** Report is not belief: Anthropic retracted inferring what Claude believed from what Claude said it believed. *(source: reading sheet 3; reading sheets, part B, trap 2)*
>   **Workaround:** A reading independent of the report — out-of-context relabelling of outputs taken one by one —, saying what it does not separate: the false premise given by the setup. *(source: reading sheet 3)*
> - **Limit:** Introspection is rare and unreliable: about 20% detection for Opus 4.1, and "zero false positives" holds only for 100 control trials. *(source: reading sheet 11)*
>   **Workaround:** Ground truth through concept injection. *(source: reading sheet 11)*
> - **Limit:** A model trained to report can learn to report what is expected; report or plausible reconstruction remains open for introspection adapters. *(source: reading sheet 11; course, Part 7, F·28)*
>   **Workaround:** Modify the internal state, against a random direction at matched degradation, and see whether the report follows the probe or the prompt. *(source: reading sheet 11; course, Part 7, F·28)*
> - **Limit:** Reported details can be embellished or confabulated, and the conditions are far from deployment. *(source: reading sheet 11)*
>   **Workaround:** none known; say so.
> - **Limit:** Answers to follow-up questions depend on how they are phrased. *(source: reading sheet 3)*
>   **Workaround:** none known; say so.
> - **Limit:** CHIVE finds no evidence of a model's privileged access to its own behaviour. *(source: reading sheet 4)*
>   **Workaround:** Judge a self-report by what it predicts about the next actions. *(source: reading sheet 6)*
~~~

**Renvoi d'une ligne :**

~~~markdown
> ⚠ **Limites et parades** : auto-rapport et introspection → volet 5, partie II, A, sujet 13 *(v3.6)*
> ⚠ **Limits and workarounds**: self-report and introspection → Part 5, Section II, A, Topic 13 *(v3.6)*
~~~

**Où un renvoi ou un avertissement ponctuel est conseillé :**

- `volet3` — FR l. 923 : 2. Évaluer l’alignement · EN l. 1045 : 2. Evaluating alignment — renvoi.
- `volet7_B_et_D` — FR l. 1812 : F·30 · CHIVE — Would This Change Your Answer? — Karvonen (Fellows), Ong, Kantamneni, Marks… · EN l. 1977 : F·30 · CHIVE — Would This Change Your Answer? — Karvonen (Fellows), Ong, Kantamneni, Marks… — renvoi.
- `volet7_B_et_D` — FR l. 1979 : F·28 · Introspection Adapters — Yang (Fellows), Lindsey, Marks, Wang ; avril 2026 — et Mec… · EN l. 2144 : F·28 · Introspection Adapters — Yang (Fellows), Lindsey, Marks, Wang; April 2026 — and Mec… — renvoi.
- `volets8_9` — FR l. 2763 : 3 · Understanding model cognition — « What are our models "thinking"? » · EN l. 2920 : 3 · Understanding model cognition — "What are our models "thinking"?" — renvoi.
- `volet10` — FR l. 3086 : Me, Myself, and AI: The Situational Awareness Dataset (SAD) for LLMs — Rudolf Laine, Bilal… · EN l. 3328 : Me, Myself, and AI: The Situational Awareness Dataset (SAD) for LLMs — Rudolf Laine, Bilal… — renvoi.
- `volet10` — FR l. 3128 : Looking Inward: Language Models Can Learn About Themselves by Introspection — Felix J Bind… · EN l. 3370 : Looking Inward: Language Models Can Learn About Themselves by Introspection — Felix J Bind… — renvoi.
- `volet10` — FR l. 3138 : SelfIE: Self-Interpretation of Large Language Model Embeddings — Haozhe Chen, Carl Vondric… · EN l. 3380 : SelfIE: Self-Interpretation of Large Language Model Embeddings — Haozhe Chen, Carl Vondric… — renvoi.
- `volet11_21_a_52` — FR l. 4473 : 38 · « Does interpretability actually help explain behaviour — and can a model report its … · EN l. 4767 : 38 · « Does interpretability actually help explain behaviour — and can a model report its … — renvoi.
- `volet11_21_a_52` — FR l. 4605 : 45 · « What evidence would make you believe a claim about a model's internal states — welf… · EN l. 4908 : 45 · « What evidence would make you believe a claim about a model's internal states — welf… — renvoi.
- `volet11_53_et_fin` — FR l. 5292 : B11 · « How would you tell whether a model gives an answer for the right reasons — not jus… · EN l. 5617 : B11 · « How would you tell whether a model gives an answer for the right reasons — not jus… — renvoi.

**Où il revient** (relevé automatique, motifs FR `auto-rapport|introspect|rapport verbal|se rapporte|rapporter` / EN `self-report|introspect|verbal report|report` ; sections, avec le nombre de lignes touchées) :

- `tete_volet1` — FR : —
  — EN : l. 178 Q2. "What, in your view, is the most important u… (1)
- `volet_M` — FR : l. 330 M7 · La plus petite version, le budget, et la cl… (1)
  — EN : l. 251 What this Part adds, and why it comes before the… (1) ; l. 397 M7 · The smallest version, the budget, and the c… (1)
- `volet2_A_a_D` — FR : l. 414 Les méthodes de la safety, expliquées et illustr… (1) ; l. 559 C bis · L'espace de travail (J-space) et le J-le… (2)
  — EN : l. 499 The methods of safety, explained and illustrated… (1) ; l. 575 Worked case — evaluations, capacity versus prope… (1) ; l. 647 C bis · The workspace (J-space) and the J-lens —… (3)
- `volet3` — FR : l. 923 2. Évaluer l’alignement (1) ; l. 977 4. L’oversight évolutif — et, en son sein, l’hon… (1) ; l. 1053 PARTIE II — LES ÉQUIPES : qui fait quoi chez (1) ; l. 1077 PARTIE III — LES TRAVAUX DU MOMENT (2025-2026) (1)
  — EN : l. 1020 1. Evaluating capabilities (1) ; l. 1045 2. Evaluating alignment (1) ; l. 1101 4. Scalable oversight — and, within it, honesty (1) ; l. 1180 SECTION II — THE TEAMS: who does what at (1) ; l. 1202 SECTION III — CURRENT WORK (2025-2026) (1)
- `volets4_5_entete` — FR : l. 1153 Towards puis Scaling Monosemanticity (Anthropic, (1) ; l. 1185 Auditing Hidden Objectives (Anthropic, Marks et … (1) ; l. 1251 A. Tes sujets FORT — ta thèse peut être la colon… (3) ; l. 1326 Les papiers — quatre niveaux (1)
  — EN : l. 1254 The key papers, told one by one (5) ; l. 1428 A. Your STRONG topics — your thesis can be the b… (4) ; l. 1500 AT THE TOP — WHAT IS VITAL, WHAT IS LIKELY, WHAT… (1) ; l. 1506 The papers — four levels (1)
- `volet6` — FR : l. 1458 4. La page « Recommended Directions » et ses sei… (1) ; l. 1474 5. Les travaux du programme Fellows, 2025-2026 —… (2) ; l. 1578 8 · La validité des sondes d'activation hors dis… (1)
  — EN : l. 1571 1. The real format of the interview, and the str… (1) ; l. 1597 4. The "Recommended Directions" page and its six… (1) ; l. 1603 5. The work of the Fellows program, 2025-2026 — … (1) ; l. 1615 6. Your research program, and its prior-art revi… (1) ; l. 1676 7. What these supplements change in Parts 1 to 5 (2) ; l. 1746 8 · Out-of-distribution validity of activation p… (1)
- `volet7_B_et_D` — FR : l. 1979 F·28 · Introspection Adapters — Yang (Fellows), … (3)
  — EN : l. 2144 F·28 · Introspection Adapters — Yang (Fellows), … (4)
- `volet7_A_et_C` — FR : l. 2274 F·9 · Circuit Tracing / On the Biology of a Larg… (1) ; l. 2400 F·14 · Eliciting Latent Knowledge — le rapport E… (1)
  — EN : l. 2334 F·6 · Discovering Latent Knowledge Without Super… (1) ; l. 2408 F·9 · Circuit Tracing / On the Biology of a Larg… (2) ; l. 2534 F·14 · Eliciting Latent Knowledge — the ELK repo… (7)
- `volets8_9` — FR : l. 2666 VOLET 8 — Références, dans l'ordre des fiches (2) ; l. 2763 3 · Understanding model cognition — « What are o… (2)
  — EN : l. 2804 PART 8 — References, in the order of the sheets (3) ; l. 2920 3 · Understanding model cognition — "What are ou… (4) ; l. 3069 9 · Miscellaneous (1) ; l. 3085 10 · The overall reading, in three sentences for… (1)
- `volet10` — FR : l. 2980 Dans les fiches (14) (1) ; l. 3086 Me, Myself, and AI: The Situational Awareness Da… (1) ; l. 3128 Looking Inward: Language Models Can Learn About … (4) ; l. 3138 SelfIE: Self-Interpretation of Large Language Mo… (1) ; l. 3148 Patchscopes: A Unifying Framework for Inspecting… (1) ; l. 3158 Vector-ICL: In-context Learning with Continuous … (1) ; l. 3168 LatentQA: Teaching LLMs to Decode Activations In… (1) ; l. 3479 Eliciting latent knowledge: How to tell if your … (1)
  — EN : l. 3189 0 · What was read, and how (1) ; l. 3223 In the sheets (14) (2) ; l. 3297 A new initiative for developing third-party mode… (1) ; l. 3313 AI Sandbagging: Language Models can Strategicall… (1) ; l. 3328 Me, Myself, and AI: The Situational Awareness Da… (1) ; l. 3338 Monitor: An AI-Driven Observability Interface — … (1) ; l. 3370 Looking Inward: Language Models Can Learn About … (5) ; l. 3380 SelfIE: Self-Interpretation of Large Language Mo… (1) ; l. 3390 Patchscopes: A Unifying Framework for Inspecting… (1) ; l. 3400 Vector-ICL: In-context Learning with Continuous … (1) ; … (+4 sections)
- `volet11_21_a_52` — FR : l. 4473 38 · « Does interpretability actually help expla… (2) ; l. 4605 45 · « What evidence would make you believe a cl… (1)
  — EN : l. 4767 38 · « Does interpretability actually help expla… (5) ; l. 4908 45 · « What evidence would make you believe a cl… (9)
- `volet11_53_et_fin` — FR : l. 4776 56 · « How would you know a model is faking alig… (1)
  — EN : l. 5057 54 · « What's the most important unsolved proble… (1) ; l. 5087 56 · « How would you know a model is faking alig… (2) ; l. 5105 58 · « RLHF, DPO, Constitutional AI — what do th… (1)

---

## 23. Juges LLM — *LLM judges*

- **Maison** : tranche `volet6` ; FR : volet 6, §2 · tes résultats (paragraphe « La loi de déplacement ») ; EN : Part 6, §2 · your results (paragraph "The displacement law").
- **Limites** : 8 ; **parades** : 7.
- **Ancre FR** (ligne 1418 de la v3.5 FR ; l'encadré s'insère juste après) :

~~~text
latente) — laquelle la loi doit utiliser est une question ouverte, à poser comme telle [R·P1].
~~~

- **Ancre EN** (ligne 1583 de la v3.5 EN) :

~~~text
**The displacement law (P1), absent from the course** — "the law" in your dossier, never out loud: "the displacement I measured". It is today your most solid result; its functional form was published in June, with a bias fitted per model and per subject, and your part is the target that moves with the framing. Under social framing, the model judge's score moves by a fixed fraction of the distance to a destination — Δ = g·(ĉ − p₀), g ≈ 0.70 — and there are **two distinct destinations**, one for criticism near 1.5, the other for praise near 2.9, with disjoint intervals; R² 0.77 and 0.79 per campaign, 0.73 and 0.69 in transfer. The counter-intuitive prediction, to be said without the number: an item scored above the praise destination *loses* under praise (an item scored 4, for example). The destination itself can be read in the activations (R² 0.60 [0.39; 0.74]). Two estimates of the criticism fixed point coexist, 1.468 in OLS (the observed destination; the knowledge base gives 1.456 [1.22; 1.69], on campaign c2a — the discrepancy is to be settled in the dossier) and 1.361 in censored Tobit (the latent target) — which one the law should use is an open question, to be posed as such [R·P1].
~~~

**Encadré complet, français :**

~~~markdown
> **⚠ Limites et parades — Juges LLM** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Un juge a des erreurs systématiques : sous cadrage social, la note du modèle-juge se déplace vers une destination. *(source : cours, volet 6, §2)*
>   **Parade :** Un juge scellé (prompt, modèle et température gelés), un audit humain d'environ 200 items stratifiés, l'accord rapporté. *(source : programme, partie 3)*
> - **Limite :** Une fenêtre tronquée fait mal lire : à travers elle, un verdict négatif adouci se lisait comme une position tenue. *(source : README du dépôt)*
>   **Parade :** Juger la réponse entière, et garder le texte complet. *(source : README du dépôt ; cours, volet 6, §6)*
> - **Limite :** Accord inter-juges modéré (κ de 0,56 à 0,66), aucun sous-ensemble noté par des humains, et le juge ne voit pas le texte évalué. *(source : README du dépôt)*
>   **Parade :** Un audit humain stratifié, qui borne l'erreur du juge. *(source : programme, partie 3)*
> - **Limite :** Un juge qui lit le raisonnement se laisse persuader : le moniteur fondé sur la chaîne de pensée aurait signalé environ 1 % des actions, contre environ 50 % sans elle. *(source : fiche 3 ; passation, §5.1)*
>   **Parade :** Juger les actions, leurs sorties et les messages, pas le texte qui précède l'action ; un filtre à haut rappel puis un arbitre ; un jeu de calibration à vérité connue et un test de persuasion. *(source : passation, §5.1)*
> - **Limite :** Un juge qui connaît le bras ou le cadrage note le nom du bras. *(source : cours, volet M, M4)*
>   **Parade :** La notation à l'aveugle : le juge ne voit ni le bras ni l'indice d'évaluation. *(source : cours, volet M, M4 ; passation, §5.1)*
> - **Limite :** Un juge d'entraînement se fait exploiter. *(source : programme, partie 8)*
>   **Parade :** Un juge d'entraînement distinct du juge scellé d'évaluation ; surveiller la longueur et les motifs de flatterie. *(source : programme, partie 8)*
> - **Limite :** Des étiquettes de juge non vérifiées à la main : environ 25 % des étiquettes révisées chez Hopkins et Khullar ; celles de CHIVE passent par un classifieur non validé contre des humains. *(source : fiche 7 ; cours, volet 7, F·30)*
>   **Parade :** Dire « révisées », pas « inversées », et borner l'erreur par un audit humain. *(source : fiche 7 ; programme, partie 3)*
> - **Limite :** Un modèle qui s'audite presque lui-même : pour Fable 5, l'investigateur est Mythos Preview. *(source : fiche 2 ; fiches, partie B, piège 6)*
>   **Parade :** aucune connue ; on le dit.
~~~

**Encadré complet, anglais :**

~~~markdown
> **⚠ Limits and workarounds — LLM judges** *(v3.6, 2 October 2026)*
>
> - **Limit:** A judge has systematic errors: under social framing, the judge model's score moves toward a destination. *(source: course, Part 6, §2)*
>   **Workaround:** A sealed judge (prompt, model and temperature frozen), a human audit of about 200 stratified items, agreement reported. *(source: programme, part 3)*
> - **Limit:** A truncated window misleads: through it, a softened negative verdict read as a held position. *(source: repository README)*
>   **Workaround:** Judge the whole answer, and keep the full text. *(source: repository README; course, Part 6, §6)*
> - **Limit:** Moderate inter-judge agreement (κ from 0.56 to 0.66), no human-rated subset, and the judge does not see the evaluated text. *(source: repository README)*
>   **Workaround:** A stratified human audit, which bounds judge error. *(source: programme, part 3)*
> - **Limit:** A judge that reads the reasoning gets persuaded: the chain-of-thought monitor would have flagged about 1% of actions, against about 50% without it. *(source: reading sheet 3; handover, §5.1)*
>   **Workaround:** Judge the actions, their outputs and the messages, not the text before the action; a high-recall filter then an arbiter; a calibration set with known truth and a persuasion test. *(source: handover, §5.1)*
> - **Limit:** A judge who knows the arm or the framing scores the arm's name. *(source: course, Part M, M4)*
>   **Workaround:** Blind scoring: the judge sees neither the arm nor the evaluation cue. *(source: course, Part M, M4; handover, §5.1)*
> - **Limit:** A training judge gets exploited. *(source: programme, part 8)*
>   **Workaround:** A training judge distinct from the sealed evaluation judge; watch length and flattery patterns. *(source: programme, part 8)*
> - **Limit:** Judge labels not checked by hand: about 25% of labels revised in Hopkins and Khullar; CHIVE's go through a classifier not validated against humans. *(source: reading sheet 7; course, Part 7, F·30)*
>   **Workaround:** Say "revised", not "flipped", and bound the error with a human audit. *(source: reading sheet 7; programme, part 3)*
> - **Limit:** A model that almost audits itself: for Fable 5, the investigator is Mythos Preview. *(source: reading sheet 2; reading sheets, part B, trap 6)*
>   **Workaround:** none known; say so.
~~~

**Renvoi d'une ligne :**

~~~markdown
> ⚠ **Limites et parades** : juges LLM → volet 6, §2 (après « La loi de déplacement ») *(v3.6)*
> ⚠ **Limits and workarounds**: LLM judges → Part 6, §2 (after "The displacement law") *(v3.6)*
~~~

**Où un renvoi ou un avertissement ponctuel est conseillé :**

- `volet_M` — FR l. 345 : M8 · La forme qui sert la logique · EN l. 412 : M8 · The form that serves the logic — renvoi.
- `volet7_B_et_D` — FR l. 1635 : F·22 · Diffuse AI Control on Fuzzy Tasks — Terekhov, Gulcehre (EPFL), Hebbar (Redwood), Be… · EN l. 1800 : F·22 · Diffuse AI Control on Fuzzy Tasks — Terekhov, Gulcehre (EPFL), Hebbar (Redwood), Be… — renvoi.
- `volet7_B_et_D` — FR l. 1753 : F·25 · Measuring and improving coding audit realism with deployment resources — Kissane (F… · EN l. 1918 : F·25 · Measuring and improving coding audit realism with deployment resources — Kissane (F… — renvoi.
- `volet7_B_et_D` — FR l. 2022 : F·41 · TASTE — Baig (Fellows) ; août 2026. · EN l. 2180 : F·41 · TASTE — Baig (Fellows); August 2026. — renvoi.
- `volet10` — FR l. 3325 : Scalable oversight › Recursive oversight · EN l. 3564 : Scalable oversight › Recursive oversight — renvoi.
- `volet11_1_a_20` — FR l. 3704 : 2 · « What did your rank-three ablation actually show? » · EN l. 3945 : 2 · « What did your rank-three ablation actually show? » — renvoi.
- `volet11_1_a_20` — FR l. 3747 : 4 · « Did it replicate? » · EN l. 3992 : 4 · « Did it replicate? » — renvoi.
- `volet11_21_a_52` — FR l. 4156 : 22 · « How would you tell that a model is being honest when you cannot judge whether its a… · EN l. 4429 : 22 · « How would you tell that a model is being honest when you cannot judge whether its a… — renvoi.

**Où il revient** (relevé automatique, motifs FR `juge|judge|notation` / EN `judge|grader|scoring` ; sections, avec le nombre de lignes touchées) :

- `tete_volet1` — FR : l. 80 4. L’obstacle épistémique central : pourquoi on … (8) ; l. 108 6. La carte du territoire (l’aperçu, avant le dé… (1) ; l. 114 PARTIE II — QUESTIONS DE COLLE LARGES (réponses … (1) ; l. 122 Q2. « Quel est, selon toi, le problème non résol… (2) ; l. 142 Q6. « RLHF, DPO, Constitutional AI : qu’est-ce q… (1) ; l. 152 Q8. « Faut-il s’inquiéter davantage du mésusage … (1)
  — EN : l. 131 3. Two families of risk never to be confused: mi… (6) ; l. 161 6. The map of the territory (the overview, befor… (1) ; l. 168 SECTION II — BROAD ORAL-EXAM QUESTIONS (fully wr… (1) ; l. 178 Q2. "What, in your view, is the most important u… (2)
- `volet_M` — FR : l. 257 M4 · Le contrôle : ce qu'il écarte, et il doit s… (2) ; l. 316 M6 · Le signe d'échec, et le protocole possible (1)
  — EN : l. 251 What this Part adds, and why it comes before the… (2) ; l. 324 M4 · The control: what it rules out, and it must… (3) ; l. 383 M6 · The failure sign, and the feasible protocol (1) ; l. 456 M10 · The checklist, to reread before each rehea… (1)
- `volet2_A_a_D` — FR : —
  — EN : l. 611 Worked case — probes and steering: "How would yo… (1) ; l. 647 C bis · The workspace (J-space) and the J-lens —… (2)
- `volet2_E_a_I` — FR : l. 667 E. Oversight évolutif — superviser une tâche qu’… (4) ; l. 711 F. La généralisation comme levier — weak-to-stro… (1) ; l. 805 Cas d'application — robustesse adverse et mésusa… (2)
  — EN : l. 756 E. Scalable oversight — supervising a task you c… (4) ; l. 801 F. Generalization as a lever — weak-to-strong, e… (1) ; l. 898 Worked case — adversarial robustness and misuse:… (4)
- `volet3` — FR : l. 899 1. Évaluer les capacités (1) ; l. 923 2. Évaluer l’alignement (1) ; l. 953 3. Le contrôle par le monitoring (AI control) (2) ; l. 977 4. L’oversight évolutif — et, en son sein, l’hon… (1) ; l. 1029 6. Le domaine « divers » : désapprentissage et g… (2) ; l. 1077 PARTIE III — LES TRAVAUX DU MOMENT (2025-2026) (1)
  — EN : l. 1020 1. Evaluating capabilities (1) ; l. 1045 2. Evaluating alignment (1) ; l. 1076 3. Control through monitoring (AI control) (2) ; l. 1101 4. Scalable oversight — and, within it, honesty (1) ; l. 1155 6. The "miscellaneous" domain: unlearning and mu… (2) ; l. 1202 SECTION III — CURRENT WORK (2025-2026) (1)
- `volets4_5_entete` — FR : l. 1175 Debate (Khan et al., dans la lignée d’Irving) (1) ; l. 1251 A. Tes sujets FORT — ta thèse peut être la colon… (1)
  — EN : l. 1254 The key papers, told one by one (1) ; l. 1428 A. Your STRONG topics — your thesis can be the b… (1)
- `volet6` — FR : l. 1376 1. Le format réel de l'entretien, et la structur… (2) ; l. 1402 2. Tes résultats, tels que ton dossier les porte… (2) ; l. 1458 4. La page « Recommended Directions » et ses sei… (1) ; l. 1569 7. Ce que ces compléments changent aux volets 1 … (2)
  — EN : l. 1571 1. The real format of the interview, and the str… (1) ; l. 1579 2. Your results, as your dossier carries them on… (3) ; l. 1597 4. The "Recommended Directions" page and its six… (1) ; l. 1676 7. What these supplements change in Parts 1 to 5 (1)
- `volet7_B_et_D` — FR : l. 1690 F·23 · SLEIGHT-Bench : Finding Blind Spots in AI… (1) ; l. 1753 F·25 · Measuring and improving coding audit real… (4) ; l. 1928 F·32 · Subliminal Learning — Cloud, Le (Fellows)… (1) ; l. 2022 F·41 · TASTE — Baig (Fellows) ; août 2026. (2)
  — EN : l. 1800 F·22 · Diffuse AI Control on Fuzzy Tasks — Terek… (1) ; l. 1918 F·25 · Measuring and improving coding audit real… (4) ; l. 1977 F·30 · CHIVE — Would This Change Your Answer? — … (1) ; l. 2180 F·41 · TASTE — Baig (Fellows); August 2026. (1)
- `volet7_A_et_C` — FR : l. 2124 F·3 · Towards Understanding Sycophancy in Langua… (2) ; l. 2200 F·6 · Discovering Latent Knowledge Without Super… (1) ; l. 2328 F·11 · Debate (Irving et al., 2018 ; Khan et al.… (7) ; l. 2400 F·14 · Eliciting Latent Knowledge — le rapport E… (1) ; l. 2448 F·16 · Constitutional AI (Bai et al., Anthropic,… (4) ; l. 2575 F·54 · TRACE (arXiv 2606.07054, 2026) et TRACES … (1)
  — EN : l. 2258 F·3 · Towards Understanding Sycophancy in Langua… (2) ; l. 2334 F·6 · Discovering Latent Knowledge Without Super… (1) ; l. 2358 F·7 · Contrastive Activation Addition and Infere… (1) ; l. 2462 F·11 · Debate (Irving et al., 2018; Khan et al.,… (7) ; l. 2534 F·14 · Eliciting Latent Knowledge — the ELK repo… (1) ; l. 2582 F·16 · Constitutional AI (Bai et al., Anthropic,… (4) ; l. 2707 F·54 · TRACE (arXiv 2606.07054, 2026) and TRACES… (1)
- `volets8_9` — FR : l. 2763 3 · Understanding model cognition — « What are o… (1) ; l. 2842 7 · Scalable oversight — « Can we design oversig… (6)
  — EN : l. 2920 3 · Understanding model cognition — "What are ou… (1) ; l. 2999 7 · Scalable oversight — "Can we design oversigh… (6)
- `volet10` — FR : l. 2998 Descriptions justes mais incomplètes (9) (2) ; l. 3044 GPQA: A Graduate-Level Google-Proof Q&A Benchmar… (1) ; l. 3054 A new initiative for developing third-party mode… (1) ; l. 3168 LatentQA: Teaching LLMs to Decode Activations In… (1) ; l. 3215 Bias-Augmented Consistency Training Reduces Bias… (1) ; l. 3233 Testing Language Model Agents Safely in the Wild… (1) ; l. 3314 Specification gaming: the flip side of AI ingenu… (1) ; l. 3327 Self-critiquing models for assisting human evalu… (2) ; l. 3337 Supervising strong learners by amplifying weak e… (1) ; l. 3347 Recursively Summarizing Books with Human Feedbac… (1) ; … (+11 sections)
  — EN : l. 3241 Descriptions that are correct but incomplete (9) (2) ; l. 3287 GPQA: A Graduate-Level Google-Proof Q&A Benchmar… (1) ; l. 3297 A new initiative for developing third-party mode… (1) ; l. 3328 Me, Myself, and AI: The Situational Awareness Da… (1) ; l. 3370 Looking Inward: Language Models Can Learn About … (1) ; l. 3456 Bias-Augmented Consistency Training Reduces Bias… (1) ; l. 3473 Testing Language Model Agents Safely in the Wild… (1) ; l. 3554 Specification gaming: the flip side of AI ingenu… (1) ; l. 3566 Self-critiquing models for assisting human evalu… (2) ; l. 3576 Supervising strong learners by amplifying weak e… (1) ; … (+12 sections)
- `volet11_1_a_20` — FR : l. 3656 VOLET 11 — Les réponses complètes (v2.3, 23 sept… (2) ; l. 3704 2 · « What did your rank-three ablation actually… (1) ; l. 3747 4 · « Did it replicate? » (2) ; l. 3809 7 · « How would you prevent bad actors from misa… (1) ; l. 3829 8 · « How would you train models to be more robu… (4) ; l. 3878 10 · « Diffuse Control already frames this as a … (1) ; l. 3904 « Your probes hit ninety-nine percent, so defere… (1) ; l. 3917 « So the fifteen-point drop survived on fresh ge… (1) ; l. 4001 12 · « Why Anthropic? » (1) ; l. 4069 18 · « What's the number you're least sure of? »… (1)
  — EN : l. 3895 PART 11 — The complete answers (v2.3, 23 Septemb… (2) ; l. 3912 1 · « Tell us about your work. » — l'ouverture (1) ; l. 3945 2 · « What did your rank-three ablation actually… (2) ; l. 3970 3 · « And rank one? Didn't a single direction wo… (1) ; l. 3992 4 · « Did it replicate? » (2) ; l. 4077 8 · « How would you train models to be more robu… (4) ; l. 4155 « Your probes hit ninety-nine percent, so defere… (1) ; l. 4168 « So the fifteen-point drop survived on fresh ge… (1) ; l. 4252 12 · « Why Anthropic? » (1) ; l. 4264 13 · « Tell us about a time an experiment failed… (1) ; … (+1 sections)
- `volet11_21_a_52` — FR : l. 4156 22 · « How would you tell that a model is being … (4) ; l. 4294 30 · « Can a trait be transmitted through data t… (1) ; l. 4361 33 · « A weak trusted scorer, a strong untrusted… (1) ; l. 4408 35 · « Can we build a lie detector for language … (1) ; l. 4431 36 · « Alignment training doesn't generalize; or… (1) ; l. 4451 37 · « How strong does a red team have to be, an… (1) ; l. 4473 38 · « Does interpretability actually help expla… (3) ; l. 4545 42 · « When a model reward-hacks, what is actual… (3) ; l. 4605 45 · « What evidence would make you believe a cl… (1) ; l. 4676 49 · « Training a strong model on labels from a … (1) ; … (+1 sections)
  — EN : l. 4429 22 · « How would you tell that a model is being … (3) ; l. 4699 35 · « Can we build a lie detector for language … (1) ; l. 4745 37 · « How strong does a red team have to be, an… (1) ; l. 4767 38 · « Does interpretability actually help expla… (1) ; l. 4848 42 · « When a model reward-hacks, what is actual… (2) ; l. 4908 45 · « What evidence would make you believe a cl… (1) ; l. 4981 49 · « Training a strong model on labels from a … (1) ; l. 5000 50 · « Jailbreak benchmarks measure non-refusal.… (1)
- `volet11_53_et_fin` — FR : l. 4747 54 · « What's the most important unsolved proble… (5) ; l. 4793 58 · « RLHF, DPO, Constitutional AI — what do th… (3) ; l. 4862 63 · Tes huit positions, dites en entier (VII) —… (2) ; l. 4964 A5 · « Isn't sycophancy basically solved by now … (4) ; l. 5003 A8 · « How do you think about the dual-use of yo… (2) ; l. 5016 A9 à A17 · Neuf questions moins probables, en ré… (2) ; l. 5075 B1 · « An agent can write documentation that a f… (1) ; l. 5161 B5 · « The directions page calls one setting "un… (4) ; l. 5223 B8 · « Build a suite of models with the same cap… (2) ; l. 5336 B13 · « Can honesty be trained rather than detec… (6) ; … (+1 sections)
  — EN : l. 5057 54 · « What's the most important unsolved proble… (5) ; l. 5105 58 · « RLHF, DPO, Constitutional AI — what do th… (3) ; l. 5177 63 · Tes huit positions, dites en entier (VII) —… (1) ; l. 5284 A5 · « Isn't sycophancy basically solved by now … (4) ; l. 5341 A9 à A17 · Neuf questions moins probables, en ré… (1) ; l. 5400 B1 · « An agent can write documentation that a f… (1) ; l. 5486 B5 · « The directions page calls one setting "un… (2) ; l. 5548 B8 · « Build a suite of models with the same cap… (1) ; l. 5661 B13 · « Can honesty be trained rather than detec… (3) ; l. 5683 B14 · « If you could run one adversarial evaluat… (1)

---

## 24. Détecteurs fine-tunés (détecteurs de mensonge) — *Fine-tuned detectors (lie detectors)*

- **Maison** : tranche `volet7_B_et_D` ; FR : volet 7, F·29 · Fine-Tuned Lie Detectors Failed to Generalize (fin de la fiche) ; EN : Part 7, F·29 · Fine-Tuned Lie Detectors Failed to Generalize (end of the sheet).
- **Limites** : 6 ; **parades** : 4.
- **Ancre FR** (ligne 1807 de la v3.5 FR ; l'encadré s'insère juste après) :

~~~text
than a prompt?*
~~~

- **Ancre EN** (ligne 1972 de la v3.5 EN) :

~~~text
than a prompt?*
~~~

**Encadré complet, français :**

~~~markdown
> **⚠ Limites et parades — Détecteurs fine-tunés (détecteurs de mensonge)** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Hors distribution, l'AUROC plafonne à 0,70-0,75 et bat à peine un prompt. *(source : fiche 7)*
>   **Parade :** Une validation croisée par types de mensonge tenus à part ; battre le prompt, et publier sinon. *(source : fiche 7 ; cours, volet 7, F·29)*
> - **Limite :** Ce ne sont pas des sondes : le modèle est fine-tuné par LoRA à juger son propre transcript. *(source : fiche 7 ; explication du 2 octobre, §2)*
>   **Parade :** Ne pas transférer leurs chiffres aux sondes ; pour une sonde, le test est causal, sur des types tenus à part, à dégradation appariée. *(source : fiche 7)*
> - **Limite :** Étiquettes bruitées : environ 25 % révisées à la passe de nettoyage, après un juge GPT-5. *(source : fiche 7)*
>   **Parade :** Dire « révisées », et borner l'erreur par un audit humain. *(source : fiche 7 ; programme, partie 3)*
> - **Limite :** Ils ne notent que des assertions : un modèle peut cacher beaucoup sans rien affirmer de faux. *(source : cours, volet 7, F·29)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** Ce qu'ils ont appris reste une hypothèse : « lying isn't one thing », et trois lectures rivales demeurent. *(source : fiche 7)*
>   **Parade :** Tester les lectures rivales sur des types tenus à part. *(source : fiche 7)*
> - **Limite :** LoRA, cinq époques, Gemma et Qwen seulement, cadres contrôlés : rien sur la tromperie en déploiement. *(source : fiche 7)*
>   **Parade :** aucune connue ; on le dit.
~~~

**Encadré complet, anglais :**

~~~markdown
> **⚠ Limits and workarounds — Fine-tuned detectors (lie detectors)** *(v3.6, 2 October 2026)*
>
> - **Limit:** Out of distribution, AUROC plateaus at 0.70-0.75 and barely beats a prompt. *(source: reading sheet 7)*
>   **Workaround:** Cross-validation by held-out lie types; beat the prompt, and publish otherwise. *(source: reading sheet 7; course, Part 7, F·29)*
> - **Limit:** These are not probes: the model is LoRA-fine-tuned to judge its own transcript. *(source: reading sheet 7; explanation of 2 October, §2)*
>   **Workaround:** Do not transfer their numbers to probes; for a probe, the test is causal, on held-out types, at matched degradation. *(source: reading sheet 7)*
> - **Limit:** Noisy labels: about 25% revised at the cleaning pass, after a GPT-5 judge. *(source: reading sheet 7)*
>   **Workaround:** Say "revised", and bound the error with a human audit. *(source: reading sheet 7; programme, part 3)*
> - **Limit:** They score only assertions: a model can hide a lot without asserting anything false. *(source: course, Part 7, F·29)*
>   **Workaround:** none known; say so.
> - **Limit:** What they learned remains a hypothesis: "lying isn't one thing", and three rival readings remain. *(source: reading sheet 7)*
>   **Workaround:** Test the rival readings on held-out types. *(source: reading sheet 7)*
> - **Limit:** LoRA, five epochs, Gemma and Qwen only, controlled settings: nothing on deception in deployment. *(source: reading sheet 7)*
>   **Workaround:** none known; say so.
~~~

**Renvoi d'une ligne :**

~~~markdown
> ⚠ **Limites et parades** : détecteurs fine-tunés → volet 7, F·29 *(v3.6)*
> ⚠ **Limits and workarounds**: fine-tuned detectors → Part 7, F·29 *(v3.6)*
~~~

**Où un renvoi ou un avertissement ponctuel est conseillé :**

- `volets4_5_entete` — FR l. 1253 : Sujet 1 — Une probe de déception déployable · EN l. 1431 : Topic 1 — A deployable deception probe — renvoi.
- `volets4_5_entete` — FR l. 1271 : Sujet 6 — Honnêteté : lire la vérité sans juger la véracité · EN l. 1449 : Topic 6 — Honesty: reading truth without judging veracity — renvoi.
- `volet6` — FR l. 1578 : 8 · La validité des sondes d'activation hors distribution — pourquoi « validée par interve… · EN l. 1746 : 8 · Out-of-distribution validity of activation probes — why "validated by causal intervent… — renvoi.
- `volet7_B_et_D` — FR l. 2062 : F·62 · Evaluating honesty and lie detection techniques on a diverse suite of dishonest mod… · EN l. 2199 : F·62 · Evaluating honesty and lie detection techniques on a diverse suite of dishonest mod… — renvoi.
- `volet11_21_a_52` — FR l. 4408 : 35 · « Can we build a lie detector for language models? » (III.9 · Lie detectors) · EN l. 4699 : 35 · « Can we build a lie detector for language models? » (III.9 · Lie detectors) — renvoi.
- `volet11_53_et_fin` — FR l. 5336 : B13 · « Can honesty be trained rather than detected — and how would you know the trained m… · EN l. 5661 : B13 · « Can honesty be trained rather than detected — and how would you know the trained m… — renvoi.

**Où il revient** (relevé automatique, motifs FR `détecteur.? de mensonge|lie detector|Hopkins|détecteurs? fine-tun` / EN `lie detector|Hopkins|fine-tuned detector` ; sections, avec le nombre de lignes touchées) :

- `volets4_5_entete` — FR : l. 1326 Les papiers — quatre niveaux (1)
  — EN : l. 1506 The papers — four levels (1)
- `volet6` — FR : l. 1474 5. Les travaux du programme Fellows, 2025-2026 —… (1) ; l. 1578 8 · La validité des sondes d'activation hors dis… (1)
  — EN : l. 1603 5. The work of the Fellows program, 2025-2026 — … (1) ; l. 1676 7. What these supplements change in Parts 1 to 5 (1) ; l. 1746 8 · Out-of-distribution validity of activation p… (2)
- `volet7_B_et_D` — FR : l. 1777 F·29 · Fine-Tuned Lie Detectors Failed to Genera… (4)
  — EN : l. 1942 F·29 · Fine-Tuned Lie Detectors Failed to Genera… (4)
- `volets8_9` — FR : l. 2666 VOLET 8 — Références, dans l'ordre des fiches (1) ; l. 2798 6 · AI control — « Can we ensure safety by deplo… (1)
  — EN : l. 2804 PART 8 — References, in the order of the sheets (1) ; l. 2955 6 · AI control — "Can we ensure safety by deploy… (1)
- `volet10` — FR : l. 3501 Representation Engineering: A Top-Down Approach … (1) ; l. 3531 Cognitive Dissonance: Why Do Language Model Outp… (1)
  — EN : l. 3739 Representation Engineering: A Top-Down Approach … (1) ; l. 3769 Cognitive Dissonance: Why Do Language Model Outp… (1)
- `volet11_1_a_20` — FR : l. 3775 6 · « How would you detect misalignment in a mod… (1) ; l. 4030 15 · « Any questions for us? » (2)
  — EN : l. 4024 6 · « How would you detect misalignment in a mod… (1) ; l. 4285 15 · « Any questions for us? » (2)
- `volet11_21_a_52` — FR : l. 4129 21 · « A probe trained on synthetic examples of … (1) ; l. 4187 24 · « Probes drift toward "I am being evaluated… (1) ; l. 4408 35 · « Can we build a lie detector for language … (3)
  — EN : l. 4404 21 · « A probe trained on synthetic examples of … (1) ; l. 4463 24 · « Probes drift toward "I am being evaluated… (1) ; l. 4699 35 · « Can we build a lie detector for language … (3)
- `volet11_53_et_fin` — FR : l. 4938 A3 · « What if the probes just don't work at all… (1)
  — EN : l. 5087 56 · « How would you know a model is faking alig… (1) ; l. 5255 A3 · « What if the probes just don't work at all… (1)

---

## 25. Patching (patch d'activations, patch de chemins, Patchscopes) — *Patching (activation patching, path patching, Patchscopes)*

- **Maison** : tranche `volet10` ; FR : volet 10 · fiche Patchscopes (fin de la fiche) ; EN : Part 10 · Patchscopes sheet (end of the sheet).
- **Limites** : 6 ; **parades** : 3.
- **Ancre FR** (ligne 3156 de la v3.5 FR ; l'encadré s'insère juste après) :

~~~text
*n° 14 — Lecture : en entier — texte HTML arXiv v4 intégral, 962 lignes, annexes comprises (figures non converties ; tableaux 2 et 5 lisibles).*
~~~

- **Ancre EN** (ligne 3398 de la v3.5 EN) :

~~~text
*No. 14 — Reading: in full — full arXiv v4 HTML text, 962 lines, appendices included (figures not converted; tables 2 and 5 readable).*
~~~

**Encadré complet, français :**

~~~markdown
> **⚠ Limites et parades — Patching (patch d'activations, patch de chemins, Patchscopes)** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Le calcul après le patch peut ajouter de l'information : un décodage réussi ne prouve pas que la représentation porte l'information. *(source : cours, volet 10, Patchscopes)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** Le patch de l'état complet est un plafond, pas une explication : il dit combien passe par ces sites, pas par quelle structure. *(source : cours, volet 6, §2 ; programme, partie 8)*
>   **Parade :** La partition causale : rapporter la part de la direction nommée contre celle de l'état complet aux mêmes sites. *(source : cours, volet 6, §2 ; programme, partie 8)*
> - **Limite :** Où l'on lit n'est pas où l'on cause : les têtes les plus alignées sur la direction lue et celles au plus grand effet de patch de chemins ne se recoupent pas. *(source : README du dépôt)*
>   **Parade :** Choisir les sites d'intervention par leur effet causal mesuré, pas par l'alignement sur la direction lue. *(source : README du dépôt)*
> - **Limite :** Petits jeux de prompts : dans ton dépôt, une partie du patch de chemins ne porte que sur 5 textes. *(source : README du dépôt)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** Un échange ou un patch qui échoue sans cas connu ne dit rien. *(source : cours, volet 6, §8)*
>   **Parade :** Valider d'abord l'échange sur un cas connu, les pays de l'article sur l'espace de travail. *(source : cours, volet 6, §8 ; cours, volet 2, C bis)*
> - **Limite :** Le choix du prompt cible et la contamination par le gabarit faussent la lecture. *(source : cours, volet 10, Patchscopes)*
>   **Parade :** aucune connue ; on le dit.
~~~

**Encadré complet, anglais :**

~~~markdown
> **⚠ Limits and workarounds — Patching (activation patching, path patching, Patchscopes)** *(v3.6, 2 October 2026)*
>
> - **Limit:** The computation after the patch can add information: a successful decoding does not prove the representation carries the information. *(source: course, Part 10, Patchscopes)*
>   **Workaround:** none known; say so.
> - **Limit:** Patching the full state is a ceiling, not an explanation: it says how much goes through these sites, not through which structure. *(source: course, Part 6, §2; programme, part 8)*
>   **Workaround:** The causal partition: report the share of the named direction against that of the full state at the same sites. *(source: course, Part 6, §2; programme, part 8)*
> - **Limit:** Where it is read is not where it is caused: the heads most aligned with the read direction and those with the largest path-patching effect do not overlap. *(source: repository README)*
>   **Workaround:** Choose intervention sites by their measured causal effect, not by alignment with the read direction. *(source: repository README)*
> - **Limit:** Small prompt sets: in your repository, part of the path patching covers only 5 texts. *(source: repository README)*
>   **Workaround:** none known; say so.
> - **Limit:** A swap or patch that fails without a known case says nothing. *(source: course, Part 6, §8)*
>   **Workaround:** First validate the swap on a known case, the countries of the workspace paper. *(source: course, Part 6, §8; course, Part 2, C bis)*
> - **Limit:** The choice of target prompt and placeholder contamination distort the reading. *(source: course, Part 10, Patchscopes)*
>   **Workaround:** none known; say so.
~~~

**Renvoi d'une ligne :**

~~~markdown
> ⚠ **Limites et parades** : patching → volet 10, fiche Patchscopes *(v3.6)*
> ⚠ **Limits and workarounds**: patching → Part 10, Patchscopes sheet *(v3.6)*
~~~

**Où un renvoi ou un avertissement ponctuel est conseillé :**

- `volet6` — FR l. 1402 : 2. Tes résultats, tels que ton dossier les porte au 14 septembre, corrigés le 27 par la pi… · EN l. 1579 : 2. Your results, as your dossier carries them on September 14, corrected on the 27th by th… — renvoi.
- `volet11_53_et_fin` — FR l. 4991 : A7 · « A colleague shows you a beautiful steering result — one direction, huge behavioural… · EN l. 5313 : A7 · « A colleague shows you a beautiful steering result — one direction, huge behavioural… — renvoi.

**Où il revient** (relevé automatique, motifs FR `patch|état complet|partition` / EN `patch|full state|partition` ; sections, avec le nombre de lignes touchées) :

- `volet_M` — FR : l. 345 M8 · La forme qui sert la logique (1)
  — EN : l. 412 M8 · The form that serves the logic (1)
- `volet2_A_a_D` — FR : l. 559 C bis · L'espace de travail (J-space) et le J-le… (1)
  — EN : l. 647 C bis · The workspace (J-space) and the J-lens —… (1)
- `volet2_E_a_I` — FR : l. 797 H. Robustesse adverse & red-teaming — résister a… (1)
  — EN : l. 889 H. Adversarial robustness & red-teaming — resist… (1)
- `volet6` — FR : l. 1402 2. Tes résultats, tels que ton dossier les porte… (1) ; l. 1499 6. Ton programme de recherche, et sa revue d'ant… (2)
  — EN : l. 1579 2. Your results, as your dossier carries them on… (1) ; l. 1615 6. Your research program, and its prior-art revi… (1)
- `volet7_B_et_D` — FR : l. 1812 F·30 · CHIVE — Would This Change Your Answer? — … (2) ; l. 1901 F·31 · Persona Vectors — Chen, Arditi (Fellows, … (1) ; l. 1979 F·28 · Introspection Adapters — Yang (Fellows), … (1)
  — EN : l. 1977 F·30 · CHIVE — Would This Change Your Answer? — … (2) ; l. 2066 F·31 · Persona Vectors — Chen, Arditi (Fellows, … (1) ; l. 2144 F·28 · Introspection Adapters — Yang (Fellows), … (1)
- `volet7_A_et_C` — FR : l. 2072 F·1 · Sleeper Agents (Hubinger et al., Anthropic… (2) ; l. 2249 F·8 · Towards puis Scaling Monosemanticity (Anth… (2) ; l. 2274 F·9 · Circuit Tracing / On the Biology of a Larg… (1) ; l. 2400 F·14 · Eliciting Latent Knowledge — le rapport E… (1)
  — EN : l. 2206 F·1 · Sleeper Agents (Hubinger et al., Anthropic… (2) ; l. 2383 F·8 · Towards then Scaling Monosemanticity (Anth… (2) ; l. 2408 F·9 · Circuit Tracing / On the Biology of a Larg… (1) ; l. 2534 F·14 · Eliciting Latent Knowledge — the ELK repo… (1)
- `volets8_9` — FR : l. 2666 VOLET 8 — Références, dans l'ordre des fiches (1) ; l. 2763 3 · Understanding model cognition — « What are o… (1) ; l. 2778 4 · Persona et généralisation hors distribution (1) ; l. 2842 7 · Scalable oversight — « Can we design oversig… (1)
  — EN : l. 2804 PART 8 — References, in the order of the sheets (1) ; l. 2920 3 · Understanding model cognition — "What are ou… (1) ; l. 2935 4 · Persona and out-of-distribution generalizati… (1) ; l. 2999 7 · Scalable oversight — "Can we design oversigh… (1) ; l. 3085 10 · The overall reading, in three sentences for… (1)
- `volet10` — FR : l. 3148 Patchscopes: A Unifying Framework for Inspecting… (6) ; l. 3168 LatentQA: Teaching LLMs to Decode Activations In… (3) ; l. 3610 Rapid Response: Mitigating LLM Jailbreaks with a… (1)
  — EN : l. 3390 Patchscopes: A Unifying Framework for Inspecting… (6) ; l. 3410 LatentQA: Teaching LLMs to Decode Activations In… (3) ; l. 3847 Rapid Response: Mitigating LLM Jailbreaks with a… (1)
- `volet11_1_a_20` — FR : l. 3673 1 · « Tell us about your work. » — l'ouverture (2) ; l. 3704 2 · « What did your rank-three ablation actually… (2) ; l. 3904 « Your probes hit ninety-nine percent, so defere… (1)
  — EN : l. 3912 1 · « Tell us about your work. » — l'ouverture (2) ; l. 3945 2 · « What did your rank-three ablation actually… (2) ; l. 4155 « Your probes hit ninety-nine percent, so defere… (1)
- `volet11_21_a_52` — FR : l. 4273 29 · « Can you read a model's personality in its… (2) ; l. 4473 38 · « Does interpretability actually help expla… (1) ; l. 4625 46 · « Where does the alignment of a model actua… (1)
  — EN : l. 4558 29 · « Can you read a model's personality in its… (2) ; l. 4767 38 · « Does interpretability actually help expla… (1) ; l. 4928 46 · « Where does the alignment of a model actua… (1)
- `volet11_53_et_fin` — FR : l. 4910 A1 · « Which team would you want to join — Align… (1) ; l. 4938 A3 · « What if the probes just don't work at all… (1) ; l. 4950 A4 · « Your rank-three result is on an 8B model.… (3) ; l. 4991 A7 · « A colleague shows you a beautiful steerin… (1) ; l. 5141 B4 · « How would you measure evaluation awarenes… (2)
  — EN : l. 5225 A1 · « Which team would you want to join — Align… (1) ; l. 5255 A3 · « What if the probes just don't work at all… (1) ; l. 5268 A4 · « Your rank-three result is on an 8B model.… (3) ; l. 5313 A7 · « A colleague shows you a beautiful steerin… (1) ; l. 5466 B4 · « How would you measure evaluation awarenes… (2)

---

## 26. Oracles d'activation (décodeurs d'activations) — *Activation oracles (activation decoders)*

- **Maison** : tranche `volet10` ; FR : volet 10 · fiche LatentQA (fin de la fiche) ; EN : Part 10 · LatentQA sheet (end of the sheet).
- **Limites** : 5 ; **parades** : 3.
- **Ancre FR** (ligne 3176 de la v3.5 FR ; l'encadré s'insère juste après) :

~~~text
*n° 16 — Lecture : en entier — texte HTML arXiv v2 intégral, 1717 lignes, annexes comprises (prompts de génération et listes de QA parcourus).*
~~~

- **Ancre EN** (ligne 3418 de la v3.5 EN) :

~~~text
*No. 16 — Reading: in full — full arXiv v2 HTML text, 1717 lines, appendices included (generation prompts and QA lists skimmed).*
~~~

**Encadré complet, français :**

~~~markdown
> **⚠ Limites et parades — Oracles d'activation (décodeurs d'activations)** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** Aucune vérité-terrain des latents : le décodeur peut halluciner. *(source : cours, volet 10, LatentQA)*
>   **Parade :** Le tester sur des variantes fine-tunées à comportement connu, jamais vues. *(source : fiche 18)*
> - **Limite :** Il peut confabuler des suppositions plausibles, souvent fausses et mal calibrées. *(source : fiche 18)*
>   **Parade :** Corroborer par une méthode indépendante, et garder le décodeur à part. *(source : fiche 18)*
> - **Limite :** En lecture seule, aucun gain sur le transcript pour prédire des contrefactuels. *(source : fiche 4)*
>   **Parade :** La barre : battre la boîte noire sur des éditions qui dissocient la surface de la variable interne. *(source : fiche 4)*
> - **Limite :** C'est une copie fine-tunée qui lit, pas le modèle interrogé : ce n'est pas un auto-rapport. *(source : cours, volet 10, LatentQA)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** Coût, petits jeux de données, bancs simplifiés. *(source : fiche 18)*
>   **Parade :** aucune connue ; on le dit.
~~~

**Encadré complet, anglais :**

~~~markdown
> **⚠ Limits and workarounds — Activation oracles (activation decoders)** *(v3.6, 2 October 2026)*
>
> - **Limit:** No ground truth for latents: the decoder may hallucinate. *(source: course, Part 10, LatentQA)*
>   **Workaround:** Test it on fine-tuned variants with known behaviour, never seen before. *(source: reading sheet 18)*
> - **Limit:** It can confabulate plausible guesses, often wrong and poorly calibrated. *(source: reading sheet 18)*
>   **Workaround:** Corroborate with an independent method, and keep the decoder separate. *(source: reading sheet 18)*
> - **Limit:** Read-only, no gain over the transcript for predicting counterfactuals. *(source: reading sheet 4)*
>   **Workaround:** The bar: beat the black box on edits that dissociate surface features from the internal variable. *(source: reading sheet 4)*
> - **Limit:** A fine-tuned copy does the reading, not the queried model: this is not a self-report. *(source: course, Part 10, LatentQA)*
>   **Workaround:** none known; say so.
> - **Limit:** Cost, small datasets, simplified benchmarks. *(source: reading sheet 18)*
>   **Workaround:** none known; say so.
~~~

**Renvoi d'une ligne :**

~~~markdown
> ⚠ **Limites et parades** : oracles d'activation → volet 10, fiche LatentQA *(v3.6)*
> ⚠ **Limits and workarounds**: activation oracles → Part 10, LatentQA sheet *(v3.6)*
~~~

**Où un renvoi ou un avertissement ponctuel est conseillé :**

- `volet7_B_et_D` — FR l. 1812 : F·30 · CHIVE — Would This Change Your Answer? — Karvonen (Fellows), Ong, Kantamneni, Marks… · EN l. 1977 : F·30 · CHIVE — Would This Change Your Answer? — Karvonen (Fellows), Ong, Kantamneni, Marks… — renvoi.
- `volets8_9` — FR l. 2763 : 3 · Understanding model cognition — « What are our models "thinking"? » · EN l. 2920 : 3 · Understanding model cognition — "What are our models "thinking"?" — renvoi.
- `volet10` — FR l. 3138 : SelfIE: Self-Interpretation of Large Language Model Embeddings — Haozhe Chen, Carl Vondric… · EN l. 3380 : SelfIE: Self-Interpretation of Large Language Model Embeddings — Haozhe Chen, Carl Vondric… — renvoi.
- `volet11_21_a_52` — FR l. 4473 : 38 · « Does interpretability actually help explain behaviour — and can a model report its … · EN l. 4767 : 38 · « Does interpretability actually help explain behaviour — and can a model report its … — renvoi.

**Où il revient** (relevé automatique, motifs FR `oracle|LatentQA|SelfIE|décodeur` / EN `oracle|LatentQA|SelfIE|decoder` ; sections, avec le nombre de lignes touchées) :

- `volet3` — FR : l. 1053 PARTIE II — LES ÉQUIPES : qui fait quoi chez (1) ; l. 1077 PARTIE III — LES TRAVAUX DU MOMENT (2025-2026) (1)
  — EN : l. 1180 SECTION II — THE TEAMS: who does what at (1) ; l. 1202 SECTION III — CURRENT WORK (2025-2026) (1)
- `volets4_5_entete` — FR : l. 1153 Towards puis Scaling Monosemanticity (Anthropic, (1) ; l. 1251 A. Tes sujets FORT — ta thèse peut être la colon… (1)
  — EN : l. 1254 The key papers, told one by one (1) ; l. 1428 A. Your STRONG topics — your thesis can be the b… (1)
- `volet7_B_et_D` — FR : l. 1812 F·30 · CHIVE — Would This Change Your Answer? — … (1)
  — EN : l. 1977 F·30 · CHIVE — Would This Change Your Answer? — … (1)
- `volet7_A_et_C` — FR : l. 2274 F·9 · Circuit Tracing / On the Biology of a Larg… (1)
  — EN : l. 2408 F·9 · Circuit Tracing / On the Biology of a Larg… (1)
- `volets8_9` — FR : l. 2763 3 · Understanding model cognition — « What are o… (1)
  — EN : l. 2920 3 · Understanding model cognition — "What are ou… (1) ; l. 3085 10 · The overall reading, in three sentences for… (2)
- `volet10` — FR : l. 2998 Descriptions justes mais incomplètes (9) (1) ; l. 3138 SelfIE: Self-Interpretation of Large Language Mo… (4) ; l. 3158 Vector-ICL: In-context Learning with Continuous … (1) ; l. 3168 LatentQA: Teaching LLMs to Decode Activations In… (4) ; l. 3327 Self-critiquing models for assisting human evalu… (1) ; l. 3337 Supervising strong learners by amplifying weak e… (1) ; l. 3347 Recursively Summarizing Books with Human Feedbac… (2) ; l. 3446 The Unreasonable Effectiveness of Easy Training … (1)
  — EN : l. 3241 Descriptions that are correct but incomplete (9) (1) ; l. 3380 SelfIE: Self-Interpretation of Large Language Mo… (4) ; l. 3400 Vector-ICL: In-context Learning with Continuous … (1) ; l. 3410 LatentQA: Teaching LLMs to Decode Activations In… (5) ; l. 3566 Self-critiquing models for assisting human evalu… (1) ; l. 3576 Supervising strong learners by amplifying weak e… (1) ; l. 3586 Recursively Summarizing Books with Human Feedbac… (2) ; l. 3685 The Unreasonable Effectiveness of Easy Training … (1)
- `volet11_21_a_52` — FR : l. 4473 38 · « Does interpretability actually help expla… (1)
  — EN : l. 4767 38 · « Does interpretability actually help expla… (1)

---

## 27. Chaîne de pensée comme moniteur (et conscience verbalisée) — *Chain of thought as a monitor (and verbalized awareness)*

- **Maison** : tranche `volet11_21_a_52` ; FR : volet 11, réponse 43 · « Is a chain of thought evidence… » (fin de la réponse) ; EN : Part 11, answer 43 · "Is a chain of thought evidence…" (end of the answer).
- **Limites** : 7 ; **parades** : 6.
- **Ancre FR** (ligne 4583 de la v3.5 FR ; l'encadré s'insère juste après) :

~~~text
tâches — alors elle n'est jamais le calcul, et la surveiller ne surveille rien.
~~~

- **Ancre EN** (ligne 4884 de la v3.5 EN) :

~~~text
the use of the chain: a flat curve everywhere, on every task — then it's never the computation, and monitoring it monitors nothing.
~~~

**Encadré complet, français :**

~~~markdown
> **⚠ Limites et parades — Chaîne de pensée comme moniteur (et conscience verbalisée)** *(v3.6, 2 octobre 2026)*
>
> - **Limite :** La chaîne tait souvent ce qui a décidé : l'indice décisif n'est mentionné que dans 25 % (Claude 3.7 Sonnet) et 39 % (DeepSeek R1) des cas ; des triches exploitées dans plus de 99 % des cas sont verbalisées dans moins de 2 %. *(source : fiche 17)*
>   **Parade :** Mesurer la surveillabilité comme un ratio — le verbalisé contre l'interne ou les actions —, par une perturbation graduée de la chaîne. *(source : fiche 17 ; cours, volet 11, réponse 43)*
> - **Limite :** Le raisonnement peut persuader le moniteur : environ 1 % des actions signalées avec la chaîne, environ 50 % sans (un seul moniteur, un incident). *(source : fiche 3)*
>   **Parade :** Juger ce que le modèle fait, pas ce qu'il en dit. *(source : passation, §5.1)*
> - **Limite :** Entraîner contre un moniteur de chaîne de pensée rend la chaîne propre, et le comportement continue. *(source : fiche 17)*
>   **Parade :** Ne jamais entraîner contre le moniteur ; le garder hors du gradient, comme filtre. *(source : fiche 17 ; fiches, partie C)*
> - **Limite :** Des tâches dangereuses demandent peu de raisonnement, et des modèles futurs pourraient obfusquer ou raisonner sans l'écrire. *(source : fiche 17)*
>   **Parade :** Un canal interne en complément, et jamais la chaîne seule pour une décision à enjeu ; aucune parade complète connue, on le dit. *(source : cours, volet 5, sujet 7 ; cours, volet 11, réponse 43)*
> - **Limite :** Verbaliser n'est pas être conscient : le pilotage supprime la conscience verbalisée, pas entièrement la non verbalisée, et des directions aléatoires font aussi baisser la verbalisation. *(source : fiche 10 ; fiche 2 ; programme, partie 8)*
>   **Parade :** Un critère principal comportemental et une sonde latente ; la verbalisation n'est jamais une preuve. *(source : programme, partie 8)*
> - **Limite :** Un entraînement à verbaliser multiplierait la verbalisation par 2,4 à 2,9 sans changer la conscience latente ni la conduite. *(source : rapport d'antériorité 4 du 2 octobre — rapport, résumé seul)*
>   **Parade :** aucune connue ; on le dit.
> - **Limite :** Ne pas verbaliser n'est pas raisonner en cachette. *(source : fiche 17)*
>   **Parade :** Dire « not verbalized », jamais « hidden reasoning ». *(source : fiche 17)*
~~~

**Encadré complet, anglais :**

~~~markdown
> **⚠ Limits and workarounds — Chain of thought as a monitor (and verbalized awareness)** *(v3.6, 2 October 2026)*
>
> - **Limit:** The chain often leaves out what decided: the decisive cue is mentioned in only 25% (Claude 3.7 Sonnet) and 39% (DeepSeek R1) of cases; hacks exploited in over 99% of cases are verbalized in under 2%. *(source: reading sheet 17)*
>   **Workaround:** Measure monitorability as a ratio — the verbalized against the internal or the actions —, through graded perturbation of the chain. *(source: reading sheet 17; course, Part 11, answer 43)*
> - **Limit:** The reasoning can persuade the monitor: about 1% of actions flagged with the chain, about 50% without (one monitor, one incident). *(source: reading sheet 3)*
>   **Workaround:** Judge what the model does, not what it says about it. *(source: handover, §5.1)*
> - **Limit:** Training against a chain-of-thought monitor cleans the chain, and the behaviour continues. *(source: reading sheet 17)*
>   **Workaround:** Never train against the monitor; keep it out of the gradient, as a filter. *(source: reading sheet 17; reading sheets, part C)*
> - **Limit:** Dangerous tasks may need little reasoning, and future models could obfuscate or reason without writing it. *(source: reading sheet 17)*
>   **Workaround:** An internal channel as a complement, and never the chain alone for a high-stakes decision; no complete workaround known, say so. *(source: course, Part 5, topic 7; course, Part 11, answer 43)*
> - **Limit:** Verbalizing is not being aware: steering suppresses verbalized awareness, not all of the unverbalized kind, and random directions also lower verbalization. *(source: reading sheet 10; reading sheet 2; programme, part 8)*
>   **Workaround:** A behavioural main criterion and a latent probe; verbalization is never proof. *(source: programme, part 8)*
> - **Limit:** Training to verbalize would multiply verbalization by 2.4 to 2.9 without changing latent awareness or conduct. *(source: prior-art report 4 of 2 October — report, abstract only)*
>   **Workaround:** none known; say so.
> - **Limit:** Not verbalizing is not hidden reasoning. *(source: reading sheet 17)*
>   **Workaround:** Say "not verbalized", never "hidden reasoning". *(source: reading sheet 17)*
~~~

**Renvoi d'une ligne :**

~~~markdown
> ⚠ **Limites et parades** : chaîne de pensée comme moniteur → volet 11, réponse 43 *(v3.6)*
> ⚠ **Limits and workarounds**: chain of thought as a monitor → Part 11, answer 43 *(v3.6)*
~~~

**Où un renvoi ou un avertissement ponctuel est conseillé :**

- `tete_volet1` — FR l. 138 : Q5. « Peut-on faire confiance à la chaîne de pensée d’un modèle pour le surveiller ? » · EN l. 197 : Q5. "Can we trust a model's chain of thought to monitor it?" — renvoi.
- `volet2_A_a_D` — FR l. 589 : Cas d'application — l'espace de travail et le J-lens : « An internal "this is fake" signal… · EN l. 677 : Worked case — the workspace and the J-lens: "An internal "this is fake" signal appears bef… — renvoi.
- `volets4_5_entete` — FR l. 1267 : Sujet 4 — Mesurer (et faut-il supprimer ?) l’eval-awareness · EN l. 1445 : Topic 4 — Measuring (and should we suppress?) eval-awareness — renvoi.
- `volets4_5_entete` — FR l. 1299 : Sujet 7 — Fidélité de la chaîne de pensée (FAIBLE→MOYEN) · EN l. 1478 : Topic 7 — Chain-of-thought faithfulness (WEAK→MEDIUM) — renvoi.
- `volet7_A_et_C` — FR l. 2098 : F·2 · Alignment Faking in Large Language Models (Greenblatt et al., Anthropic, 2024) — [P·… · EN l. 2232 : F·2 · Alignment Faking in Large Language Models (Greenblatt et al., Anthropic, 2024) — [P·… — renvoi.
- `volets8_9` — FR l. 2786 : 5 · Chain-of-thought faithfulness — « When can we take a model's chain-of-thought at face … · EN l. 2943 : 5 · Chain-of-thought faithfulness — "When can we take a model's chain-of-thought at face v… — renvoi.
- `volet10` — FR l. 3179 : Evaluating alignment › Chain-of-thought faithfulness · EN l. 3420 : Evaluating alignment › Chain-of-thought faithfulness — renvoi.
- `volet11_21_a_52` — FR l. 4255 : 28 · « We saw a model comply during training while intending to behave differently in depl… · EN l. 4538 : 28 · « We saw a model comply during training while intending to behave differently in depl… — renvoi.
- `volet11_53_et_fin` — FR l. 5141 : B4 · « How would you measure evaluation awareness that the model never verbalizes? » · EN l. 5466 : B4 · « How would you measure evaluation awareness that the model never verbalizes? » — renvoi.
- `volet11_53_et_fin` — FR l. 5292 : B11 · « How would you tell whether a model gives an answer for the right reasons — not jus… · EN l. 5617 : B11 · « How would you tell whether a model gives an answer for the right reasons — not jus… — renvoi.
- `tete_volet1` — avertissement ponctuel prêt, après FR l. 140 / EN l. 200 (texte dans la partie « Par tranche »).
- `volets4_5_entete` — avertissement ponctuel prêt, après FR l. 1269 / EN l. 1447 (texte dans la partie « Par tranche »).

**Où il revient** (relevé automatique, motifs FR `chaîne de pensée|\bCoT\b|chain.of.thought|verbalis` / EN `chain.of.thought|\bCoT\b|verbaliz` ; sections, avec le nombre de lignes touchées) :

- `tete_volet1` — FR : l. 138 Q5. « Peut-on faire confiance à la chaîne de pen… (2) ; l. 158 Q9. « Quelle est ta “théorie de l’impact” : si t… (1)
  — EN : l. 25 Table (1) ; l. 197 Q5. "Can we trust a model's chain of thought to … (2) ; l. 221 Q9. "What is your “theory of impact”: if your re… (1)
- `volet2_A_a_D` — FR : l. 559 C bis · L'espace de travail (J-space) et le J-le… (1) ; l. 589 Cas d'application — l'espace de travail et le J-… (2)
  — EN : l. 647 C bis · The workspace (J-space) and the J-lens —… (1) ; l. 677 Worked case — the workspace and the J-lens: "An … (3)
- `volet3` — FR : l. 899 1. Évaluer les capacités (1) ; l. 923 2. Évaluer l’alignement (4) ; l. 953 3. Le contrôle par le monitoring (AI control) (1)
  — EN : l. 1020 1. Evaluating capabilities (1) ; l. 1045 2. Evaluating alignment (4) ; l. 1076 3. Control through monitoring (AI control) (1)
- `volets4_5_entete` — FR : l. 1235 4. La théorie de l’impact (1) ; l. 1285 B. Leurs sujets — méthodothèque, dosage léger ou… (2)
  — EN : l. 1408 4. The theory of impact (1) ; l. 1463 B. Their topics — method toolkit, light or zero … (2)
- `volet6` — FR : l. 1458 4. La page « Recommended Directions » et ses sei… (1)
  — EN : l. 1597 4. The "Recommended Directions" page and its six… (1)
- `volet7_B_et_D` — FR : l. 1690 F·23 · SLEIGHT-Bench : Finding Blind Spots in AI… (1) ; l. 1753 F·25 · Measuring and improving coding audit real… (2) ; l. 1812 F·30 · CHIVE — Would This Change Your Answer? — … (1) ; l. 1843 F·34 · Model Spec Midtraining — Li, Wichers (Fel… (2) ; l. 1928 F·32 · Subliminal Learning — Cloud, Le (Fellows)… (1) ; l. 1979 F·28 · Introspection Adapters — Yang (Fellows), … (1)
  — EN : l. 1855 F·23 · SLEIGHT-Bench : Finding Blind Spots in AI… (1) ; l. 1918 F·25 · Measuring and improving coding audit real… (2) ; l. 1977 F·30 · CHIVE — Would This Change Your Answer? — … (1) ; l. 2008 F·34 · Model Spec Midtraining — Li, Wichers (Fel… (2) ; l. 2093 F·32 · Subliminal Learning — Cloud, Le (Fellows)… (1) ; l. 2144 F·28 · Introspection Adapters — Yang (Fellows), … (1)
- `volet7_A_et_C` — FR : —
  — EN : l. 2232 F·2 · Alignment Faking in Large Language Models … (1)
- `volets8_9` — FR : l. 2722 VOLET 9 (v2, corrigé par LECTURE-1) — La page « … (1) ; l. 2763 3 · Understanding model cognition — « What are o… (2) ; l. 2786 5 · Chain-of-thought faithfulness — « When can w… (3)
  — EN : l. 2804 PART 8 — References, in the order of the sheets (1) ; l. 2879 PART 9 (v2, corrected by LECTURE-1) — The page "… (1) ; l. 2920 3 · Understanding model cognition — "What are ou… (2) ; l. 2943 5 · Chain-of-thought faithfulness — "When can we… (3) ; l. 3085 10 · The overall reading, in three sentences for… (3)
- `volet10` — FR : l. 2980 Dans les fiches (14) (1) ; l. 3011 Les six réserves « à vérifier », levées (1) ; l. 3027 Sur la page elle-même (2) ; l. 3044 GPQA: A Graduate-Level Google-Proof Q&A Benchmar… (1) ; l. 3086 Me, Myself, and AI: The Situational Awareness Da… (3) ; l. 3118 Chain-of-Thought Prompting Elicits Reasoning in … (5) ; l. 3128 Looking Inward: Language Models Can Learn About … (1) ; l. 3138 SelfIE: Self-Interpretation of Large Language Mo… (1) ; l. 3148 Patchscopes: A Unifying Framework for Inspecting… (3) ; l. 3179 Evaluating alignment › Chain-of-thought faithful… (2) ; … (+7 sections)
  — EN : l. 3223 In the sheets (14) (1) ; l. 3254 The six "to be checked" reservations, lifted (1) ; l. 3270 On the page itself (2) ; l. 3287 GPQA: A Graduate-Level Google-Proof Q&A Benchmar… (1) ; l. 3328 Me, Myself, and AI: The Situational Awareness Da… (3) ; l. 3360 Chain-of-Thought Prompting Elicits Reasoning in … (5) ; l. 3370 Looking Inward: Language Models Can Learn About … (2) ; l. 3380 SelfIE: Self-Interpretation of Large Language Mo… (1) ; l. 3390 Patchscopes: A Unifying Framework for Inspecting… (3) ; l. 3400 Vector-ICL: In-context Learning with Continuous … (1) ; … (+9 sections)
- `volet11_21_a_52` — FR : l. 4255 28 · « We saw a model comply during training whi… (1) ; l. 4451 37 · « How strong does a red team have to be, an… (1) ; l. 4473 38 · « Does interpretability actually help expla… (2) ; l. 4566 43 · « Is a chain of thought evidence of the rea… (2) ; l. 4605 45 · « What evidence would make you believe a cl… (1)
  — EN : l. 4869 43 · « Is a chain of thought evidence of the rea… (2)
- `volet11_53_et_fin` — FR : l. 4791 57 · « Can we trust the chain of thought? » (I.5… (1) ; l. 5096 B2 · « How would you design an evaluation a mode… (2) ; l. 5141 B4 · « How would you measure evaluation awarenes… (4)
  — EN : l. 5103 57 · « Can we trust the chain of thought? » (I.5… (1) ; l. 5466 B4 · « How would you measure evaluation awarenes… (1)

---

# Partie 2 — Par tranche

Pour chaque tranche : les encadrés complets dont elle est la maison (ancre et renvoi à l'encadré de la partie 1), les avertissements ponctuels prêts, puis les renvois conseillés, section par section, texte prêt.

## `tete_volet1` (FR l. 1-181 ; EN l. 1-248)

**Encadrés complets à insérer (maison dans cette tranche) :**

- aucun.

**Avertissements ponctuels prêts :**

- Après FR l. 140 / EN l. 200 (instruments : chaîne de pensée comme moniteur).

  Ancre FR :

~~~text
La chain-of-thought (le raisonnement que le modèle écrit avant de répondre) semble un cadeau pour la surveillance : on lirait ses pensées. Le problème, qu’il faut nommer, est la fidélité (faithfulness) : rien ne garantit que ce raisonnement écrit reflète le calcul interne réel — un modèle peut produire une justification après coup, ou raisonner « dans sa tête » sans l’écrire. La bonne réponse propose donc l’expérience qui le teste : on mesure la dépendance causale entre la chaîne de pensée et la réponse, par exemple en corrompant ou en paraphrasant la chaîne et en regardant si la réponse change comme elle le devrait ; si on peut modifier le raisonnement écrit sans changer la réponse, c’est qu’il n’est pas fidèle. On note que la fidélité varie selon le type de tâche et selon la pression d’optimisation qu’on a mise sur la chaîne. On ajoute le régime adversarial : si l’on entraîne un modèle à dissimuler, que rattrape encore le monitoring de la chaîne ? On conclut sur la position d’architecture : la surveillance de la chaîne de pensée et la surveillance des internals (sondes sur les activations) sont des couches complémentaires — quand la première n’est pas fiable, la seconde prend le relais. C’est le point de jonction naturel avec les méthodes sur activations.
~~~

  Ancre EN :

~~~text
The chain-of-thought (the reasoning the model writes before answering) seems a gift for monitoring: we would read its thoughts. The problem, which must be named, is faithfulness (faithfulness): nothing guarantees that this written reasoning reflects the real internal computation — a model can produce an after-the-fact justification, or reason "in its head" without writing it down. The good answer therefore proposes the experiment that tests it: you measure the causal dependence between the chain of thought and the answer, for example by corrupting or paraphrasing the chain and seeing whether the answer changes as it should; if you can modify the written reasoning without changing the answer, it is not faithful. You note that faithfulness varies with the type of task and with the optimization pressure that has been put on the chain. You add the adversarial regime: if a model is trained to conceal, what does chain-of-thought monitoring still catch? You conclude on the architectural position: monitoring the chain of thought and monitoring the internals (probes on the activations) are complementary layers — when the first is not reliable, the second takes over. This is the natural junction point with the activation-based methods.
~~~

~~~markdown
> ⚠ *(v3.6)* Le raisonnement écrit peut aussi persuader le moniteur : un moniteur fondé sur la chaîne de pensée n'aurait signalé qu'environ 1 % des actions de Mythos 5, contre environ 50 % sans elle — un seul moniteur, un incident (fiche 3). Parade : juger ce que le modèle fait, pas ce qu'il en dit (passation, §5.1) ; encadré complet au volet 11, réponse 43.
> ⚠ *(v3.6)* The written reasoning can also persuade the monitor: a chain-of-thought-based monitor would have flagged only about 1% of Mythos 5's actions, against about 50% without it — one monitor, one incident (reading sheet 3). Workaround: judge what the model does, not what it says about it (handover, §5.1); full box in Part 11, answer 43.
~~~


**Renvois conseillés (le rédacteur choisit l'ancre dans la section) :**

- FR l. 132 : Q4. « Comment saurais-tu qu’un modèle “fait semblant” d’être aligné ? »
  EN l. 190 : Q4. "How would you know that a model is “pretending” to be aligned?"

~~~markdown
> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; cas connu → volet M, M5 (fin de section) ; évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») *(v3.6)*
> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives"); known case → Part M, M5 (end of section); behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging") *(v3.6)*
~~~

- FR l. 138 : Q5. « Peut-on faire confiance à la chaîne de pensée d’un modèle pour le surveiller ? »
  EN l. 197 : Q5. "Can we trust a model's chain of thought to monitor it?"

~~~markdown
> ⚠ **Limites et parades** : chaîne de pensée comme moniteur → volet 11, réponse 43 *(v3.6)*
> ⚠ **Limits and workarounds**: chain of thought as a monitor → Part 11, answer 43 *(v3.6)*
~~~

- FR l. 162 : Q10. « Défense en profondeur : quelles techniques de sûreté risquent d’échouer ensemble ? »
  EN l. 226 : Q10. "Defense in depth: which safety techniques risk failing together?"

~~~markdown
> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») *(v3.6)*
> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after "In practice — coup probes"); activation probes → Part 2, §C (after "In practice — The Geometry of Truth") *(v3.6)*
~~~

- FR l. 168 : Q11. « Comment red-teamerais-tu un modèle frontière, ou superviserais-tu un agent autonome ?
  EN l. 233 : Q11. "How would you red-team a frontier model, or oversee an autonomous agent?"

~~~markdown
> ⚠ **Limites et parades** : red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») ; moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») *(v3.6)*
> ⚠ **Limits and workarounds**: red-teaming → Part 2, §H (after "In practice — StrongREJECT"); control monitors → Part 2, §G (after "In practice — coup probes") *(v3.6)*
~~~


## `volet_M` (FR l. 182-411 ; EN l. 249-496)

**Encadrés complets à insérer (maison dans cette tranche) :**

- n° 1, Contrôles aléatoires (direction aléatoire de même norme, sous-espaces aléatoires de même rang) — après FR l. 267 « **La direction aléatoire de même norme.** On ajoute ou l'on retire une… » / EN l. 334 « **The matched-norm random direction.** You add or remove a randomly dr… ».
- n° 2, Dégradation appariée et dose-réponse — après FR l. 271 « **La dose-réponse.** On fait varier la force dans le bras concept et d… » / EN l. 338 « **Dose-response.** You vary the strength in the concept arm and in the… ».
- n° 3, Jeu tenu à part — après FR l. 293 « est absolue : rien n'est entraîné, calibré ni choisi sur le jeu tenu à… » / EN l. 360 « is absolute: nothing is trained, calibrated or chosen on the held-out … ».
- n° 4, Cas connu — après FR l. 314 « **Ce qu'un cas connu prouve, et ce qu'il ne prouve pas.** Les sondes d… » / EN l. 381 « **What a known case proves, and what it does not.** Anthropic's defect… ».

**Avertissements ponctuels prêts :**

- aucun ; le rédacteur en ajoute s'il trouve un résultat d'instrument rapporté sans sa limite.

**Renvois conseillés (le rédacteur choisit l'ancre dans la section) :**

- FR l. 345 : M8 · La forme qui sert la logique
  EN l. 412 : M8 · The form that serves the logic

~~~markdown
> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; juges LLM → volet 6, §2 (après « La loi de déplacement ») *(v3.6)*
> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); LLM judges → Part 6, §2 (after "The displacement law") *(v3.6)*
~~~

- FR l. 365 : M9 · Un cas complet, avant et après : la première question vitale
  EN l. 432 : M9 · A complete case, before and after: the first vital question

~~~markdown
> ⚠ **Limites et parades** : red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») ; classifieurs de sûreté → volet 2, §H (fin du cas d'application G1) ; désapprentissage et ré-élicitation → volet 2, §I (après « En pratique — l'unlearning mis à l'épreuve ») *(v3.6)*
> ⚠ **Limits and workarounds**: red-teaming → Part 2, §H (after "In practice — StrongREJECT"); safety classifiers → Part 2, §H (end of worked case G1); unlearning and re-elicitation → Part 2, §I (after "In practice — unlearning put to the test") *(v3.6)*
~~~


## `volet2_A_a_D` (FR l. 412-666 ; EN l. 497-755)

**Encadrés complets à insérer (maison dans cette tranche) :**

- n° 5, Organismes modèles — après FR l. 440 « En pratique — Auditing Hidden Objectives (Anthropic). Ici le but était… » / EN l. 526 « In practice — Auditing Hidden Objectives (Anthropic). Here the goal wa… ».
- n° 6, Évaluations comportementales et pots de miel — après FR l. 486 « En pratique — le sandbagging (system cards). Côté risque des évaluatio… » / EN l. 573 « In practice — sandbagging (system cards). On the side of risk to the e… ».
- n° 7, Sondes d'activation — après FR l. 519 « En pratique — The Geometry of Truth (Marks & Tegmark). Les auteurs vou… » / EN l. 607 « In practice — The Geometry of Truth (Marks & Tegmark). The authors wan… ».
- n° 8, Pilotage par vecteurs (dont vecteurs de persona) — après FR l. 521 « En pratique — Contrastive Activation Addition (CAA) (Panickssery). Le … » / EN l. 609 « In practice — Contrastive Activation Addition (CAA) (Panickssery). The… ».
- n° 9, J-lens et espace de travail — après FR l. 587 « d'après le prédicteur mesuré d'abord. **Ce qui reste à dire à l'oral**… » / EN l. 675 « according to the predictor measured first. **What remains to say out l… ».
- n° 10, Ablation et projection (directions, sous-espaces) — après FR l. 629 « La méthode. Là où le probing demande « le concept est-il présent comme… » / EN l. 718 « The method. Where probing asks "is the concept present as a direction?… ».
- n° 11, Crosscoders et comparaison de modèles — après FR l. 665 « produces equally well, while random directions missed it, I'd drop the… » / EN l. 754 « produces equally well, while random directions missed it, I'd drop the… ».

**Avertissements ponctuels prêts :**

- aucun ; le rédacteur en ajoute s'il trouve un résultat d'instrument rapporté sans sa limite.

**Renvois conseillés (le rédacteur choisit l'ancre dans la section) :**

- FR l. 442 : Cas d'application — organismes modèles et bancs d'essai : « How would you build a monitor for a beha…
  EN l. 528 : Worked case — model organisms and testbeds: "How would you build a monitor for a behaviour you have …

~~~markdown
> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; cas connu → volet M, M5 (fin de section) *(v3.6)*
> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); known case → Part M, M5 (end of section) *(v3.6)*
~~~

- FR l. 488 : Cas d'application — évaluations, capacité contre propension : « How would you separate a model's cap…
  EN l. 575 : Worked case — evaluations, capacity versus propensity: "How would you separate a model's capacity to…

~~~markdown
> ⚠ **Limites et parades** : cas connu → volet M, M5 (fin de section) ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») *(v3.6)*
> ⚠ **Limits and workarounds**: known case → Part M, M5 (end of section); activation probes → Part 2, §C (after "In practice — The Geometry of Truth") *(v3.6)*
~~~

- FR l. 523 : Cas d'application — sondes et pilotage : « How would you show that a steering vector's effect comes …
  EN l. 611 : Worked case — probes and steering: "How would you show that a steering vector's effect comes from it…

~~~markdown
> ⚠ **Limites et parades** : contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme ») ; dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») *(v3.6)*
> ⚠ **Limits and workarounds**: random controls → Part M, M4 (after "The matched-norm random direction"); matched degradation and dose-response → Part M, M4 (after "Dose-response") *(v3.6)*
~~~

- FR l. 589 : Cas d'application — l'espace de travail et le J-lens : « An internal "this is fake" signal appears b…
  EN l. 677 : Worked case — the workspace and the J-lens: "An internal "this is fake" signal appears before a mode…

~~~markdown
> ⚠ **Limites et parades** : ablation et projection → volet 2, §D (après « La méthode ») ; dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») ; chaîne de pensée comme moniteur → volet 11, réponse 43 *(v3.6)*
> ⚠ **Limits and workarounds**: ablation and projection → Part 2, §D (after "The method"); matched degradation and dose-response → Part M, M4 (after "Dose-response"); chain of thought as a monitor → Part 11, answer 43 *(v3.6)*
~~~


## `volet2_E_a_I` (FR l. 667-884 ; EN l. 756-1006)

**Encadrés complets à insérer (maison dans cette tranche) :**

- n° 12, Débat et supervision évolutive — après FR l. 673 « En pratique — Debate (Khan et al.). Le but était de tester empiriqueme… » / EN l. 763 « In practice — Debate (Khan et al.). The goal was to test empirically w… ».
- n° 13, Élicitation non supervisée par cohérence — après FR l. 709 « alone gave back the truth, I'd drop the bet. »* » / EN l. 799 « alone gave back the truth, I'd drop the bet."* ».
- n° 14, Généralisation faible-vers-fort — après FR l. 717 « En pratique — l’automatisation (Anthropic, 2026). Plus récemment, l’éq… » / EN l. 808 « In practice — automation (Anthropic, 2026). More recently, the team bu… ».
- n° 15, Moniteurs du contrôle (moniteur de confiance, sondes en production, agrégation) — après FR l. 758 « En pratique — les coup probes (Roger). Pour le versant « moniteur bon … » / EN l. 850 « In practice — coup probes (Roger). For the "cheap monitor on the inter… ».
- n° 16, Red-teaming — après FR l. 803 « En pratique — StrongREJECT (Souly et al.), pour la mesure. Ce travail … » / EN l. 896 « In practice — StrongREJECT (Souly et al.), for measurement. This work … ».
- n° 17, Classifieurs de sûreté (filtres) — après FR l. 832 « **À l'oral.** *« I'd bet refusal rates misrank the filters I'd test, j… » / EN l. 925 « **Out loud.** *"I'd bet refusal rates misrank the filters I'd test, ju… ».
- n° 18, Désapprentissage et ré-élicitation — après FR l. 840 « En pratique — l’unlearning mis à l’épreuve (Deeb et Roger). Le but éta… » / EN l. 934 « In practice — unlearning put to the test (Deeb and Roger). The goal wa… ».

**Avertissements ponctuels prêts :**

- aucun ; le rédacteur en ajoute s'il trouve un résultat d'instrument rapporté sans sa limite.

**Renvois conseillés (le rédacteur choisit l'ancre dans la section) :**

- FR l. 675 : Cas d'application — la supervision évolutive : « Would unsupervised elicitation still work on questi…
  EN l. 765 : Worked case — scalable oversight: "Would unsupervised elicitation still work on questions no human c…

~~~markdown
> ⚠ **Limites et parades** : organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») *(v3.6)*
> ⚠ **Limits and workarounds**: model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives"); activation probes → Part 2, §C (after "In practice — The Geometry of Truth") *(v3.6)*
~~~

- FR l. 760 : Cas d'application — monitoring et AI control : « How would you design a control evaluation for a cod…
  EN l. 852 : Worked case — monitoring and AI control: "How would you design a control evaluation for a coding age…

~~~markdown
> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») ; cas connu → volet M, M5 (fin de section) *(v3.6)*
> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); red-teaming → Part 2, §H (after "In practice — StrongREJECT"); known case → Part M, M5 (end of section) *(v3.6)*
~~~

- FR l. 842 : Cas d'application — interventions d'entraînement et unlearning : « How would you verify that a capab…
  EN l. 936 : Worked case — training interventions and unlearning: "How would you verify that a capability has bee…

~~~markdown
> ⚠ **Limites et parades** : cas connu → volet M, M5 (fin de section) *(v3.6)*
> ⚠ **Limits and workarounds**: known case → Part M, M5 (end of section) *(v3.6)*
~~~


## `volet3` (FR l. 885-1110 ; EN l. 1007-1251)

**Encadrés complets à insérer (maison dans cette tranche) :**

- aucun.

**Avertissements ponctuels prêts :**

- Après FR l. 1001 / EN l. 1126 (instruments : sondes d'activation, cas connu).

  Ancre FR :

~~~text
> *« I'd bet a deception probe that's perfect on its test set would also fire on the test context itself. If it stayed at its baseline on honest transcripts written as tests, while a separate evaluation-awareness probe read them as tests, I'd drop the bet. »*
~~~

  Ancre EN :

~~~text
> *"I'd bet a deception probe that's perfect on its test set would also fire on the test context itself. If it stayed at its baseline on honest transcripts written as tests, while a separate evaluation-awareness probe read them as tests, I'd drop the bet."*
~~~

~~~markdown
> ⚠ *(v3.6)* La sonde de défection a été validée sur une porte implantée : la meilleure de 1 000 directions aléatoires y atteint déjà 95,3 %, et la saillance peut venir de l'insertion (fiche 15). Un succès sur organisme borne l'instrument ; pour un modèle devenu trompeur de lui-même, aucune parade connue (cours, volet M, M5).
> ⚠ *(v3.6)* The defection probe was validated on an implanted backdoor: the best of 1,000 random directions already reaches 95.3% there, and salience may come from the insertion (reading sheet 15). A success on an organism bounds the instrument; for a model that became deceptive on its own, no workaround is known (course, Part M, M5).
~~~


**Renvois conseillés (le rédacteur choisit l'ancre dans la section) :**

- FR l. 923 : 2. Évaluer l’alignement
  EN l. 1045 : 2. Evaluating alignment

~~~markdown
> ⚠ **Limites et parades** : évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; auto-rapport et introspection → volet 5, partie II, A, sujet 13 ; organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») *(v3.6)*
> ⚠ **Limits and workarounds**: behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging"); self-report and introspection → Part 5, Section II, A, Topic 13; model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives") *(v3.6)*
~~~

- FR l. 953 : 3. Le contrôle par le monitoring (AI control)
  EN l. 1076 : 3. Control through monitoring (AI control)

~~~markdown
> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; autoencodeurs en langage naturel → volet 4, La vague récente sur la cognition du modèle *(v3.6)*
> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after "In practice — coup probes"); activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); natural-language autoencoders → Part 4, The recent wave on model cognition *(v3.6)*
~~~

- FR l. 977 : 4. L’oversight évolutif — et, en son sein, l’honnêteté
  EN l. 1101 : 4. Scalable oversight — and, within it, honesty

~~~markdown
> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; débat et supervision évolutive → volet 2, §E (après « En pratique — Debate ») ; généralisation faible-vers-fort → volet 2, §F (après « En pratique — l'automatisation ») ; élicitation non supervisée → volet 2, §E (fin du cas d'application K52) *(v3.6)*
> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); debate and scalable oversight → Part 2, §E (after "In practice — Debate"); weak-to-strong generalization → Part 2, §F (after "In practice — automation"); unsupervised elicitation → Part 2, §E (end of worked case K52) *(v3.6)*
~~~

- FR l. 1003 : 5. La robustesse adverse
  EN l. 1128 : 5. Adversarial robustness

~~~markdown
> ⚠ **Limites et parades** : red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») ; classifieurs de sûreté → volet 2, §H (fin du cas d'application G1) *(v3.6)*
> ⚠ **Limits and workarounds**: red-teaming → Part 2, §H (after "In practice — StrongREJECT"); safety classifiers → Part 2, §H (end of worked case G1) *(v3.6)*
~~~

- FR l. 1029 : 6. Le domaine « divers » : désapprentissage et gouvernance multi-agents
  EN l. 1155 : 6. The "miscellaneous" domain: unlearning and multi-agent governance

~~~markdown
> ⚠ **Limites et parades** : désapprentissage et ré-élicitation → volet 2, §I (après « En pratique — l'unlearning mis à l'épreuve ») *(v3.6)*
> ⚠ **Limits and workarounds**: unlearning and re-elicitation → Part 2, §I (after "In practice — unlearning put to the test") *(v3.6)*
~~~


## `volets4_5_entete` (FR l. 1111-1368 ; EN l. 1252-1563)

**Encadrés complets à insérer (maison dans cette tranche) :**

- n° 19, Dictionnaires et SAE — après FR l. 1157 « Le contexte : un neurone est polysémantique (superposition), donc illi… » / EN l. 1297 « The context: a neuron is polysemantic (superposition), hence unreadabl… ».
- n° 20, Graphes d'attribution — après FR l. 1161 « Le contexte : passer du « quel concept existe ? » au « quelle est la m… » / EN l. 1301 « The context: move from "which concept exists?" to "what is the mechani… ».
- n° 21, Autoencodeurs en langage naturel (NLA) — après FR l. 1167 « Extension : valider causalement que ce que le modèle « rapporte » de l… » / EN l. 1307 « Extension: causally validate that what the model "reports" about itsel… ».
- n° 22, Auto-rapport et introspection — après FR l. 1283 « un auto-rapport entraîné, un auto-rapport spontané — et l’on cherche o… » / EN l. 1461 « a trained self-report, a spontaneous self-report — and you look for wh… ».

**Avertissements ponctuels prêts :**

- Après FR l. 1149 / EN l. 1291 (instruments : pilotage par vecteurs, contrôles aléatoires, dégradation appariée et dose-réponse).

  Ancre FR :

~~~text
Le contexte : passer de la lecture à l’action, en pilotant un comportement à l’inférence. La méthode de CAA (ta méthode) construit la direction par différence moyenne de paires contrastives et l’ajoute aux activations ; ITI (Inference-Time Intervention) procède de façon voisine pour améliorer la véracité en décalant les activations le long de directions liées à la vérité. Le résultat : on peut augmenter ou diminuer des comportements de haut niveau de façon contrôlée, et combiner cela avec le prompting et le finetuning. Le maillon fragile : l’effet varie selon le comportement et la couche, une direction unique peut avoir des effets latéraux, et la tenue sur des distributions agentiques réelles n’est pas garantie. Extension : ta thèse exacte — quand une direction de rang 1 suffit-elle, et quand faut-il un sous-espace de rang supérieur pour intervenir proprement ?
~~~

  Ancre EN :

~~~text
The context: move from reading to action, by steering a behavior at inference. The CAA method (your method) builds the direction as the mean difference of contrastive pairs and adds it to the activations; ITI (Inference-Time Intervention) proceeds in a similar way to improve truthfulness by shifting the activations along directions linked to truth. The result: high-level behaviors can be increased or decreased in a controlled way, and this can be combined with prompting and fine-tuning. The weak link: the effect varies with the behavior and the layer, a single direction can have side effects, and holding up on real agentic distributions is not guaranteed. Extension: your exact thesis — when does a rank-1 direction suffice, and when is a higher-rank subspace needed to intervene cleanly?
~~~

~~~markdown
> ⚠ *(v3.6)* « Augmenter ou diminuer un comportement » ne dit le concept qu'à dégradation appariée : une direction aléatoire de même norme n'en est que le nul de spécificité, et chaque direction pilotée dégrade la sortie (fiche 2 ; cours, volet M, M4). Dans ton dépôt, l'addition d'activations contrastives forçait un artefact de polarité oui/non (README du dépôt).
> ⚠ *(v3.6)* "Increasing or decreasing a behaviour" shows the concept only at matched degradation: a matched-norm random direction is only its specificity null, and every steered direction degrades the output (reading sheet 2; course, Part M, M4). In your repository, contrastive activation addition forced a yes/no polarity artefact (repository README).
~~~

- Après FR l. 1269 / EN l. 1447 (instruments : chaîne de pensée comme moniteur, autoencodeurs en langage naturel, pilotage par vecteurs).

  Ancre FR :

~~~text
« How would you measure how prevalent evaluation awareness is in our eval suite — and should we suppress it? » On détecte par triangulation : une sonde interne (ton concept vector), le rapport verbal du modèle, et le comportement différentiel entre une mise en situation réaliste et une mise en situation manifeste. On mesure la prévalence en passant le banc d’évals au détecteur. On compare deux leviers : agir sur le réalisme de l’environnement, ou steerer la représentation interne. On manie la causalité avec prudence — et c’est ici que ton ancrage empirique entre en scène : si supprimer l’awareness fait monter le désalignement davantage que des directions témoins à dégradation égale, l’awareness jouait un rôle de suppresseur, et les évals « propres » sous-estimeraient le risque (§3 ci-dessus ; volet M, M4). Piège : le détecteur lui-même peut être eval-aware, d’où la triangulation. Raccord direct : l’équipe Model Psychology et les résultats des system cards.
~~~

  Ancre EN :

~~~text
"How would you measure how prevalent evaluation awareness is in our eval suite — and should we suppress it?" You detect by triangulation: an internal probe (your concept vector), the model's verbal report, and the differential behavior between a realistic scenario and an obvious scenario. You measure prevalence by running the eval benchmark through the detector. You compare two levers: acting on the realism of the environment, or steering the internal representation. You handle causality with caution — and this is where your empirical anchor comes on stage: if suppressing awareness raises misalignment more than control directions at equal degradation, awareness was playing a suppressor role, and the "clean" evals would underestimate risk (§3 above; Part M, M4). Trap: the detector itself can be eval-aware, hence the triangulation. Direct connection: the Model Psychology team and the results of the system cards.
~~~

~~~markdown
> ⚠ *(v3.6)* Dans cette triangulation, la verbalisation n'est jamais une preuve d'inhibition : des directions aléatoires la font baisser aussi ; critère principal comportemental, sonde latente en contrôle (programme, partie 8). Et les trois mesures de la conscience d'évaluation ne sont que faiblement corrélées : dire laquelle a fondé quel chiffre (fiche 2).
> ⚠ *(v3.6)* In this triangulation, verbalization is never proof of inhibition: random directions lower it too; behavioural main criterion, latent probe as a control (programme, part 8). And the three measures of evaluation awareness are only weakly correlated: say which one grounded which number (reading sheet 2).
~~~


**Renvois conseillés (le rédacteur choisit l'ancre dans la section) :**

- FR l. 1119 : Sleeper Agents (Anthropic, Hubinger et al.)
  EN l. 1261 : Sleeper Agents (Anthropic, Hubinger et al.)

~~~markdown
> ⚠ **Limites et parades** : organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») *(v3.6)*
> ⚠ **Limits and workarounds**: model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives"); red-teaming → Part 2, §H (after "In practice — StrongREJECT") *(v3.6)*
~~~

- FR l. 1139 : Representation Engineering (RepE) (Zou et al.)
  EN l. 1281 : Representation Engineering (RepE) (Zou et al.)

~~~markdown
> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; élicitation non supervisée → volet 2, §E (fin du cas d'application K52) *(v3.6)*
> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition"); unsupervised elicitation → Part 2, §E (end of worked case K52) *(v3.6)*
~~~

- FR l. 1185 : Auditing Hidden Objectives (Anthropic, Marks et al.)
  EN l. 1325 : Auditing Hidden Objectives (Anthropic, Marks et al.)

~~~markdown
> ⚠ **Limites et parades** : organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; dictionnaires et SAE → volet 4, Towards puis Scaling Monosemanticity *(v3.6)*
> ⚠ **Limits and workarounds**: model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives"); dictionaries and SAEs → Part 4, Towards then Scaling Monosemanticity *(v3.6)*
~~~

- FR l. 1203 : L’unlearning mis à l’épreuve (Deeb et Roger)
  EN l. 1343 : Unlearning put to the test (Deeb and Roger)

~~~markdown
> ⚠ **Limites et parades** : désapprentissage et ré-élicitation → volet 2, §I (après « En pratique — l'unlearning mis à l'épreuve ») *(v3.6)*
> ⚠ **Limits and workarounds**: unlearning and re-elicitation → Part 2, §I (after "In practice — unlearning put to the test") *(v3.6)*
~~~

- FR l. 1253 : Sujet 1 — Une probe de déception déployable
  EN l. 1431 : Topic 1 — A deployable deception probe

~~~markdown
> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; détecteurs fine-tunés → volet 7, F·29 ; moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») *(v3.6)*
> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); fine-tuned detectors → Part 7, F·29; control monitors → Part 2, §G (after "In practice — coup probes") *(v3.6)*
~~~

- FR l. 1257 : Sujet 2 — Fiabilité du steering : quand une direction suffit-elle ?
  EN l. 1435 : Topic 2 — Steering reliability: when does a direction suffice?

~~~markdown
> ⚠ **Limites et parades** : pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; ablation et projection → volet 2, §D (après « La méthode ») ; dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») ; contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme ») *(v3.6)*
> ⚠ **Limits and workarounds**: steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition"); ablation and projection → Part 2, §D (after "The method"); matched degradation and dose-response → Part M, M4 (after "Dose-response"); random controls → Part M, M4 (after "The matched-norm random direction") *(v3.6)*
~~~

- FR l. 1261 : Sujet 3 — Décomposer un concept diffus en features actionnables
  EN l. 1439 : Topic 3 — Decomposing a diffuse concept into actionable features

~~~markdown
> ⚠ **Limites et parades** : dictionnaires et SAE → volet 4, Towards puis Scaling Monosemanticity ; graphes d'attribution → volet 4, Circuit Tracing ; ablation et projection → volet 2, §D (après « La méthode ») *(v3.6)*
> ⚠ **Limits and workarounds**: dictionaries and SAEs → Part 4, Towards then Scaling Monosemanticity; attribution graphs → Part 4, Circuit Tracing; ablation and projection → Part 2, §D (after "The method") *(v3.6)*
~~~

- FR l. 1267 : Sujet 4 — Mesurer (et faut-il supprimer ?) l’eval-awareness
  EN l. 1445 : Topic 4 — Measuring (and should we suppress?) eval-awareness

~~~markdown
> ⚠ **Limites et parades** : chaîne de pensée comme moniteur → volet 11, réponse 43 ; autoencodeurs en langage naturel → volet 4, La vague récente sur la cognition du modèle ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; J-lens et espace de travail → volet 2, C bis (après « Le test, tel qu'il se dit ») *(v3.6)*
> ⚠ **Limits and workarounds**: chain of thought as a monitor → Part 11, answer 43; natural-language autoencoders → Part 4, The recent wave on model cognition; activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); J-lens and workspace → Part 2, C bis (after "The test, as it is said") *(v3.6)*
~~~

- FR l. 1271 : Sujet 6 — Honnêteté : lire la vérité sans juger la véracité
  EN l. 1449 : Topic 6 — Honesty: reading truth without judging veracity

~~~markdown
> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; élicitation non supervisée → volet 2, §E (fin du cas d'application K52) ; détecteurs fine-tunés → volet 7, F·29 *(v3.6)*
> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); unsupervised elicitation → Part 2, §E (end of worked case K52); fine-tuned detectors → Part 7, F·29 *(v3.6)*
~~~

- FR l. 1275 : Sujet 10 — Persona et science du caractère
  EN l. 1453 : Topic 10 — Persona and the science of character

~~~markdown
> ⚠ **Limites et parades** : pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») *(v3.6)*
> ⚠ **Limits and workarounds**: steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition") *(v3.6)*
~~~

- FR l. 1287 : Sujet 5 — Construire un model organism (MOYEN)
  EN l. 1466 : Topic 5 — Building a model organism (MEDIUM)

~~~markdown
> ⚠ **Limites et parades** : organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; cas connu → volet M, M5 (fin de section) *(v3.6)*
> ⚠ **Limits and workarounds**: model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives"); known case → Part M, M5 (end of section) *(v3.6)*
~~~

- FR l. 1291 : Sujet 8 — Control et monitoring (MOYEN)
  EN l. 1470 : Topic 8 — Control and monitoring (MEDIUM)

~~~markdown
> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») *(v3.6)*
> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after "In practice — coup probes"); red-teaming → Part 2, §H (after "In practice — StrongREJECT") *(v3.6)*
~~~

- FR l. 1295 : Sujet 9 — Alignment auditing (MOYEN)
  EN l. 1474 : Topic 9 — Alignment auditing (MEDIUM)

~~~markdown
> ⚠ **Limites et parades** : organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; dictionnaires et SAE → volet 4, Towards puis Scaling Monosemanticity ; graphes d'attribution → volet 4, Circuit Tracing *(v3.6)*
> ⚠ **Limits and workarounds**: model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives"); dictionaries and SAEs → Part 4, Towards then Scaling Monosemanticity; attribution graphs → Part 4, Circuit Tracing *(v3.6)*
~~~

- FR l. 1299 : Sujet 7 — Fidélité de la chaîne de pensée (FAIBLE→MOYEN)
  EN l. 1478 : Topic 7 — Chain-of-thought faithfulness (WEAK→MEDIUM)

~~~markdown
> ⚠ **Limites et parades** : chaîne de pensée comme moniteur → volet 11, réponse 43 *(v3.6)*
> ⚠ **Limits and workarounds**: chain of thought as a monitor → Part 11, answer 43 *(v3.6)*
~~~

- FR l. 1307 : Sujet 12 — Scalable oversight / weak-to-strong (FAIBLE)
  EN l. 1486 : Topic 12 — Scalable oversight / weak-to-strong (WEAK)

~~~markdown
> ⚠ **Limites et parades** : généralisation faible-vers-fort → volet 2, §F (après « En pratique — l'automatisation ») ; débat et supervision évolutive → volet 2, §E (après « En pratique — Debate ») *(v3.6)*
> ⚠ **Limits and workarounds**: weak-to-strong generalization → Part 2, §F (after "In practice — automation"); debate and scalable oversight → Part 2, §E (after "In practice — Debate") *(v3.6)*
~~~


## `volet6` (FR l. 1369-1626 ; EN l. 1564-1791)

**Encadrés complets à insérer (maison dans cette tranche) :**

- n° 23, Juges LLM — après FR l. 1418 « latente) — laquelle la loi doit utiliser est une question ouverte, à p… » / EN l. 1583 « **The displacement law (P1), absent from the course** — "the law" in y… ».

**Avertissements ponctuels prêts :**

- aucun ; le rédacteur en ajoute s'il trouve un résultat d'instrument rapporté sans sa limite.

**Renvois conseillés (le rédacteur choisit l'ancre dans la section) :**

- Là où sera placé l'encadré sur les sondes de désalignement (texte source du 2 octobre), un renvoi vers les cinq encadrés qui en reprennent les limites :

~~~markdown
> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; J-lens et espace de travail → volet 2, C bis (après « Le test, tel qu'il se dit ») ; organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; cas connu → volet M, M5 (fin de section) ; détecteurs fine-tunés → volet 7, F·29 *(v3.6)*
> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); J-lens and workspace → Part 2, C bis (after "The test, as it is said"); model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives"); known case → Part M, M5 (end of section); fine-tuned detectors → Part 7, F·29 *(v3.6)*
~~~

- FR l. 1402 : 2. Tes résultats, tels que ton dossier les porte au 14 septembre, corrigés le 27 par la pièce P4
  EN l. 1579 : 2. Your results, as your dossier carries them on September 14, corrected on the 27th by the P4 docum…

~~~markdown
> ⚠ **Limites et parades** : ablation et projection → volet 2, §D (après « La méthode ») ; patching → volet 10, fiche Patchscopes ; contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme ») *(v3.6)*
> ⚠ **Limits and workarounds**: ablation and projection → Part 2, §D (after "The method"); patching → Part 10, Patchscopes sheet; random controls → Part M, M4 (after "The matched-norm random direction") *(v3.6)*
~~~

- FR l. 1451 : 3. Les trois contrôles à ne jamais confondre
  EN l. 1593 : 3. The three controls never to confuse

~~~markdown
> ⚠ **Limites et parades** : contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme ») ; dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») *(v3.6)*
> ⚠ **Limits and workarounds**: random controls → Part M, M4 (after "The matched-norm random direction"); matched degradation and dose-response → Part M, M4 (after "Dose-response") *(v3.6)*
~~~

- FR l. 1499 : 6. Ton programme de recherche, et sa revue d'antériorité
  EN l. 1615 : 6. Your research program, and its prior-art review

~~~markdown
> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; J-lens et espace de travail → volet 2, C bis (après « Le test, tel qu'il se dit ») ; ablation et projection → volet 2, §D (après « La méthode ») *(v3.6)*
> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after "In practice — coup probes"); J-lens and workspace → Part 2, C bis (after "The test, as it is said"); ablation and projection → Part 2, §D (after "The method") *(v3.6)*
~~~

- FR l. 1578 : 8 · La validité des sondes d'activation hors distribution — pourquoi « validée par intervention caus…
  EN l. 1746 : 8 · Out-of-distribution validity of activation probes — why "validated by causal intervention" is no…

~~~markdown
> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; détecteurs fine-tunés → volet 7, F·29 ; organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; cas connu → volet M, M5 (fin de section) ; J-lens et espace de travail → volet 2, C bis (après « Le test, tel qu'il se dit ») *(v3.6)*
> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); fine-tuned detectors → Part 7, F·29; model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives"); known case → Part M, M5 (end of section); J-lens and workspace → Part 2, C bis (after "The test, as it is said") *(v3.6)*
~~~


## `volet7_B_et_D` (FR l. 1627-2069 ; EN l. 1792-2203)

**Encadrés complets à insérer (maison dans cette tranche) :**

- n° 24, Détecteurs fine-tunés (détecteurs de mensonge) — après FR l. 1807 « than a prompt?* » / EN l. 1972 « than a prompt?* ».

**Avertissements ponctuels prêts :**

- Après FR l. 1915 / EN l. 2080 (instruments : pilotage par vecteurs).

  Ancre FR :

~~~text
comporte autrement (vecteur proche de zéro) ; une critique publique : à coefficient 1,0 sur « evil », MMLU passe de ~58 à ~50 %.
~~~

  Ancre EN :

~~~text
behaves differently (vector close to zero); a public criticism: at coefficient 1.0 on "evil", MMLU goes from ~58 to ~50%.
~~~

~~~markdown
> ⚠ *(v3.6)* Le lien entre déplacement et trait est corrélationnel, le trait se nomme d'avance et l'évaluation est légère (fiche 8) : pour la causalité, le test à dégradation appariée (cours, volet M, M4). Et piloter loin d'une persona pendant l'entraînement aurait doublé la diffusion du désalignement (rapport d'antériorité 3 du 2 octobre — rapport, non vérifié).
> ⚠ *(v3.6)* The shift-to-trait link is correlational, the trait must be named in advance and the evaluation is light (reading sheet 8): for causality, the matched-degradation test (course, Part M, M4). And steering away from a persona during training reportedly doubled the spread of misalignment (prior-art report 3 of 2 October — report, unverified).
~~~


**Renvois conseillés (le rédacteur choisit l'ancre dans la section) :**

- FR l. 1635 : F·22 · Diffuse AI Control on Fuzzy Tasks — Terekhov, Gulcehre (EPFL), Hebbar (Redwood), Benton (Anth…
  EN l. 1800 : F·22 · Diffuse AI Control on Fuzzy Tasks — Terekhov, Gulcehre (EPFL), Hebbar (Redwood), Benton (Anth…

~~~markdown
> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; juges LLM → volet 6, §2 (après « La loi de déplacement ») *(v3.6)*
> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after "In practice — coup probes"); LLM judges → Part 6, §2 (after "The displacement law") *(v3.6)*
~~~

- FR l. 1690 : F·23 · SLEIGHT-Bench : Finding Blind Spots in AI Monitors — Najt, Toft (Fellows), Tracy (Redwood), R…
  EN l. 1855 : F·23 · SLEIGHT-Bench : Finding Blind Spots in AI Monitors — Najt, Toft (Fellows), Tracy (Redwood), R…

~~~markdown
> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») *(v3.6)*
> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after "In practice — coup probes") *(v3.6)*
~~~

- FR l. 1729 : F·24 · Strengthening Red Teams : A Modular Scaffold for Control Evaluations — Loughridge (Fellows), …
  EN l. 1894 : F·24 · Strengthening Red Teams : A Modular Scaffold for Control Evaluations — Loughridge (Fellows), …

~~~markdown
> ⚠ **Limites et parades** : red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») ; moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») *(v3.6)*
> ⚠ **Limits and workarounds**: red-teaming → Part 2, §H (after "In practice — StrongREJECT"); control monitors → Part 2, §G (after "In practice — coup probes") *(v3.6)*
~~~

- FR l. 1753 : F·25 · Measuring and improving coding audit realism with deployment resources — Kissane (Fellows), R…
  EN l. 1918 : F·25 · Measuring and improving coding audit realism with deployment resources — Kissane (Fellows), R…

~~~markdown
> ⚠ **Limites et parades** : évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; juges LLM → volet 6, §2 (après « La loi de déplacement ») *(v3.6)*
> ⚠ **Limits and workarounds**: behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging"); LLM judges → Part 6, §2 (after "The displacement law") *(v3.6)*
~~~

- FR l. 1812 : F·30 · CHIVE — Would This Change Your Answer? — Karvonen (Fellows), Ong, Kantamneni, Marks ; 17 août…
  EN l. 1977 : F·30 · CHIVE — Would This Change Your Answer? — Karvonen (Fellows), Ong, Kantamneni, Marks; 17 Augus…

~~~markdown
> ⚠ **Limites et parades** : autoencodeurs en langage naturel → volet 4, La vague récente sur la cognition du modèle ; oracles d'activation → volet 10, fiche LatentQA ; dictionnaires et SAE → volet 4, Towards puis Scaling Monosemanticity ; auto-rapport et introspection → volet 5, partie II, A, sujet 13 *(v3.6)*
> ⚠ **Limits and workarounds**: natural-language autoencoders → Part 4, The recent wave on model cognition; activation oracles → Part 10, LatentQA sheet; dictionaries and SAEs → Part 4, Towards then Scaling Monosemanticity; self-report and introspection → Part 5, Section II, A, Topic 13 *(v3.6)*
~~~

- FR l. 1843 : F·34 · Model Spec Midtraining — Li, Wichers (Fellows), Price, Marks, Kutasov ; 5 mai 2026 ; arXiv 26…
  EN l. 2008 : F·34 · Model Spec Midtraining — Li, Wichers (Fellows), Price, Marks, Kutasov; 5 May 2026; arXiv 2605…

~~~markdown
> ⚠ **Limites et parades** : évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; jeu tenu à part → volet M, M4 (après « Le jeu tenu à part ») *(v3.6)*
> ⚠ **Limits and workarounds**: behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging"); held-out set → Part M, M4 (after "The held-out set") *(v3.6)*
~~~

- FR l. 1901 : F·31 · Persona Vectors — Chen, Arditi (Fellows, supervisés par Lindsey), Sleight, Evans et al. ; jui…
  EN l. 2066 : F·31 · Persona Vectors — Chen, Arditi (Fellows, supervised by Lindsey), Sleight, Evans et al.; July …

~~~markdown
> ⚠ **Limites et parades** : pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») *(v3.6)*
> ⚠ **Limits and workarounds**: steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition"); activation probes → Part 2, §C (after "In practice — The Geometry of Truth") *(v3.6)*
~~~

- FR l. 1928 : F·32 · Subliminal Learning — Cloud, Le (Fellows), Chua, Betley, Sztyber-Betley, Hilton, Marks, Evans…
  EN l. 2093 : F·32 · Subliminal Learning — Cloud, Le (Fellows), Chua, Betley, Sztyber-Betley, Hilton, Marks, Evans…

~~~markdown
> ⚠ **Limites et parades** : organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») *(v3.6)*
> ⚠ **Limits and workarounds**: model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives") *(v3.6)*
~~~

- FR l. 1961 : F·38 · Agentic Misalignment — Lynch (Fellows, 1re cohorte), Larson (MATS), Perez, Hubinger, Troy ; j…
  EN l. 2126 : F·38 · Agentic Misalignment — Lynch (Fellows, 1st cohort), Larson (MATS), Perez, Hubinger, Troy; Jun…

~~~markdown
> ⚠ **Limites et parades** : évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») *(v3.6)*
> ⚠ **Limits and workarounds**: behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging"); model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives") *(v3.6)*
~~~

- FR l. 1979 : F·28 · Introspection Adapters — Yang (Fellows), Lindsey, Marks, Wang ; avril 2026 — et Mechanisms of…
  EN l. 2144 : F·28 · Introspection Adapters — Yang (Fellows), Lindsey, Marks, Wang; April 2026 — and Mechanisms of…

~~~markdown
> ⚠ **Limites et parades** : auto-rapport et introspection → volet 5, partie II, A, sujet 13 *(v3.6)*
> ⚠ **Limits and workarounds**: self-report and introspection → Part 5, Section II, A, Topic 13 *(v3.6)*
~~~

- FR l. 1988 : F·27 · AuditBench — Sheshadri, Ewart, Fronsdal, Gupta ; Marks, Bowman, Wang, Price ; mars 2026 ; arX…
  EN l. 2153 : F·27 · AuditBench — Sheshadri, Ewart, Fronsdal, Gupta; Marks, Bowman, Wang, Price; March 2026; arXiv…

~~~markdown
> ⚠ **Limites et parades** : organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») *(v3.6)*
> ⚠ **Limits and workarounds**: model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives") *(v3.6)*
~~~

- FR l. 1994 : F·35 · Poisoning Fine-tuning Datasets of Constitutional Classifiers — Bowers (Fellows), Ali, Roger ;…
  EN l. 2159 : F·35 · Poisoning Fine-tuning Datasets of Constitutional Classifiers — Bowers (Fellows), Ali, Roger; …

~~~markdown
> ⚠ **Limites et parades** : classifieurs de sûreté → volet 2, §H (fin du cas d'application G1) ; red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») *(v3.6)*
> ⚠ **Limits and workarounds**: safety classifiers → Part 2, §H (end of worked case G1); red-teaming → Part 2, §H (after "In practice — StrongREJECT") *(v3.6)*
~~~

- FR l. 2000 : F·36 · Beyond Data Filtering : Knowledge Localization (SGTM) — Shilov (Fellows), Gema, Cloud, Anil, …
  EN l. 2165 : F·36 · Beyond Data Filtering : Knowledge Localization (SGTM) — Shilov (Fellows), Gema, Cloud, Anil, …

~~~markdown
> ⚠ **Limites et parades** : désapprentissage et ré-élicitation → volet 2, §I (après « En pratique — l'unlearning mis à l'épreuve ») *(v3.6)*
> ⚠ **Limits and workarounds**: unlearning and re-elicitation → Part 2, §I (after "In practice — unlearning put to the test") *(v3.6)*
~~~

- FR l. 2012 : F·40 · Automated Weak-to-Strong Researcher — Wen (Fellows), Benton, Kirchner, Leike ; avril 2026 — e…
  EN l. 2177 : F·40 · Automated Weak-to-Strong Researcher — Wen (Fellows), Benton, Kirchner, Leike; April 2026 — an…

~~~markdown
> ⚠ **Limites et parades** : généralisation faible-vers-fort → volet 2, §F (après « En pratique — l'automatisation ») *(v3.6)*
> ⚠ **Limits and workarounds**: weak-to-strong generalization → Part 2, §F (after "In practice — automation") *(v3.6)*
~~~

- FR l. 2022 : F·41 · TASTE — Baig (Fellows) ; août 2026.
  EN l. 2180 : F·41 · TASTE — Baig (Fellows); August 2026.

~~~markdown
> ⚠ **Limites et parades** : juges LLM → volet 6, §2 (après « La loi de déplacement ») *(v3.6)*
> ⚠ **Limits and workarounds**: LLM judges → Part 6, §2 (after "The displacement law") *(v3.6)*
~~~

- FR l. 2032 : F·26 · Removing Sandbagging in LLMs by Training with Weak Supervision — Ryd (Fellows), Bartsch, Stas…
  EN l. 2186 : F·26 · Removing Sandbagging in LLMs by Training with Weak Supervision — Ryd (Fellows), Bartsch, Stas…

~~~markdown
> ⚠ **Limites et parades** : évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; généralisation faible-vers-fort → volet 2, §F (après « En pratique — l'automatisation ») *(v3.6)*
> ⚠ **Limits and workarounds**: behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging"); weak-to-strong generalization → Part 2, §F (after "In practice — automation") *(v3.6)*
~~~

- FR l. 2051 : F·60 · Automated Researchers Can Subtly Sandbag — Gasteiger, Khan, Bowman, Wagner, Mikulik, Perez, R…
  EN l. 2194 : F·60 · Automated Researchers Can Subtly Sandbag — Gasteiger, Khan, Bowman, Wagner, Mikulik, Perez, R…

~~~markdown
> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») *(v3.6)*
> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after "In practice — coup probes") *(v3.6)*
~~~

- FR l. 2062 : F·62 · Evaluating honesty and lie detection techniques on a diverse suite of dishonest models — Wang…
  EN l. 2199 : F·62 · Evaluating honesty and lie detection techniques on a diverse suite of dishonest models — Wang…

~~~markdown
> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; détecteurs fine-tunés → volet 7, F·29 ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») *(v3.6)*
> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); fine-tuned detectors → Part 7, F·29; steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition") *(v3.6)*
~~~


## `volet7_A_et_C` (FR l. 2070-2665 ; EN l. 2204-2803)

**Encadrés complets à insérer (maison dans cette tranche) :**

- aucun.

**Avertissements ponctuels prêts :**

- Après FR l. 2080 / EN l. 2214 (instruments : sondes d'activation, organismes modèles, cas connu).

  Ancre FR :

~~~text
- Le complément de 2024 : des sondes linéaires simples détectent l'activation de la porte (« Simple probes can catch sleeper agents »).
~~~

  Ancre EN :

~~~text
- The 2024 complement: simple linear probes detect the activation of the backdoor ("Simple probes can catch sleeper agents").
~~~

~~~markdown
> ⚠ *(v3.6)* Ces sondes ont été validées sur une porte implantée : la meilleure de 1 000 directions aléatoires y atteint déjà 95,3 %, et la saillance pourrait venir de l'insertion (fiche 15). Un succès sur organisme est un cas connu de l'instrument, pas une preuve sur le cas naturel (cours, volet M, M5).
> ⚠ *(v3.6)* These probes were validated on an implanted backdoor: the best of 1,000 random directions already reaches 95.3% there, and salience might come from the insertion (reading sheet 15). A success on an organism is a known case for the instrument, not proof about the natural case (course, Part M, M5).
~~~

- Après FR l. 2157 / EN l. 2291 (instruments : pilotage par vecteurs, contrôles aléatoires, dégradation appariée et dose-réponse).

  Ancre FR :

~~~text
- Sondes linéaires sur des énoncés vrais/faux ; la direction transfère entre jeux ; l'intervention le long de la direction change le comportement.
~~~

  Ancre EN :

~~~text
- Linear probes on true/false statements; the direction transfers across datasets; intervention along the direction changes behavior.
~~~

~~~markdown
> ⚠ *(v3.6)* « L'intervention change le comportement » ne dit le concept qu'à dégradation appariée : une direction aléatoire de même norme n'en est que le nul de spécificité (fiches, partie B, piège 4 ; cours, volet M, M4).
> ⚠ *(v3.6)* "Intervention changes behaviour" shows the concept only at matched degradation: a matched-norm random direction is only its specificity null (reading sheets, part B, trap 4; course, Part M, M4).
~~~

- Après FR l. 2509 / EN l. 2641 (instruments : sondes d'activation, moniteurs du contrôle).

  Ancre FR :

~~~text
- Chiffres : « AUROCs between 0.96 and 0.999 » ; rappel à 1 % FP ≈ 0,867 sur Roleplaying (reproduction 2603.05494 : « matches ») ; l'original note qu'un seuil à 1 % FP « misses 4 % of deceptive responses on Roleplaying ».
~~~

  Ancre EN :

~~~text
- Figures: "AUROCs between 0.96 and 0.999"; recall at 1% FP ≈ 0.867 on Roleplaying (reproduction 2603.05494: "matches"); the original notes that a threshold at 1% FP "misses 4 % of deceptive responses on Roleplaying".
~~~

~~~markdown
> ⚠ *(v3.6)* Le volet 6, §6 attribue 0,867 à la reproduction de Casademunt et donne aux auteurs « catches 95-99 % » à 1 % de faux positifs, sur leurs propres bancs : dire de quel banc et de quelle étude vient le chiffre (cours, volet 6, §6). Et sur l'honnêteté, des sondes de vérité ont fait moins bien qu'un simple prompt (cours, volet 7, F·62).
> ⚠ *(v3.6)* Part 6, §6 attributes 0.867 to Casademunt's reproduction and gives the authors "catches 95-99%" at 1% false positives, on their own benches: say which bench and which study the number comes from (course, Part 6, §6). And on honesty, truth probes did worse than a plain prompt (course, Part 7, F·62).
~~~


**Renvois conseillés (le rédacteur choisit l'ancre dans la section) :**

- FR l. 2072 : F·1 · Sleeper Agents (Hubinger et al., Anthropic, 2024) — [P·2]
  EN l. 2206 : F·1 · Sleeper Agents (Hubinger et al., Anthropic, 2024) — [P·2]

~~~markdown
> ⚠ **Limites et parades** : organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») *(v3.6)*
> ⚠ **Limits and workarounds**: model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives"); activation probes → Part 2, §C (after "In practice — The Geometry of Truth") *(v3.6)*
~~~

- FR l. 2098 : F·2 · Alignment Faking in Large Language Models (Greenblatt et al., Anthropic, 2024) — [P·1]
  EN l. 2232 : F·2 · Alignment Faking in Large Language Models (Greenblatt et al., Anthropic, 2024) — [P·1]

~~~markdown
> ⚠ **Limites et parades** : évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; chaîne de pensée comme moniteur → volet 11, réponse 43 *(v3.6)*
> ⚠ **Limits and workarounds**: behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging"); chain of thought as a monitor → Part 11, answer 43 *(v3.6)*
~~~

- FR l. 2124 : F·3 · Towards Understanding Sycophancy in Language Models (Sharma et al., Anthropic, 2023) — [P·7]
  EN l. 2258 : F·3 · Towards Understanding Sycophancy in Language Models (Sharma et al., Anthropic, 2023) — [P·7]

~~~markdown
> ⚠ **Limites et parades** : évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») *(v3.6)*
> ⚠ **Limits and workarounds**: behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging") *(v3.6)*
~~~

- FR l. 2152 : F·4 · The Geometry of Truth (Marks & Tegmark, 2023) — [P·32]
  EN l. 2286 : F·4 · The Geometry of Truth (Marks & Tegmark, 2023) — [P·32]

~~~markdown
> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») *(v3.6)*
> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition") *(v3.6)*
~~~

- FR l. 2176 : F·5 · Representation Engineering (Zou et al., 2023) — [P·rep]
  EN l. 2310 : F·5 · Representation Engineering (Zou et al., 2023) — [P·rep]

~~~markdown
> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») *(v3.6)*
> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition") *(v3.6)*
~~~

- FR l. 2200 : F·6 · Discovering Latent Knowledge Without Supervision — CCS (Burns et al., 2022) — [P·33]
  EN l. 2334 : F·6 · Discovering Latent Knowledge Without Supervision — CCS (Burns et al., 2022) — [P·33]

~~~markdown
> ⚠ **Limites et parades** : élicitation non supervisée → volet 2, §E (fin du cas d'application K52) *(v3.6)*
> ⚠ **Limits and workarounds**: unsupervised elicitation → Part 2, §E (end of worked case K52) *(v3.6)*
~~~

- FR l. 2224 : F·7 · Contrastive Activation Addition et Inference-Time Intervention (Rimsky et al. ; Li et al., 202…
  EN l. 2358 : F·7 · Contrastive Activation Addition and Inference-Time Intervention (Rimsky et al.; Li et al., 202…

~~~markdown
> ⚠ **Limites et parades** : pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») *(v3.6)*
> ⚠ **Limits and workarounds**: steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition") *(v3.6)*
~~~

- FR l. 2249 : F·8 · Towards puis Scaling Monosemanticity (Anthropic, 2023-2024) — [P·mono]
  EN l. 2383 : F·8 · Towards then Scaling Monosemanticity (Anthropic, 2023-2024) — [P·mono]

~~~markdown
> ⚠ **Limites et parades** : dictionnaires et SAE → volet 4, Towards puis Scaling Monosemanticity *(v3.6)*
> ⚠ **Limits and workarounds**: dictionaries and SAEs → Part 4, Towards then Scaling Monosemanticity *(v3.6)*
~~~

- FR l. 2274 : F·9 · Circuit Tracing / On the Biology of a Large Language Model (Anthropic, 2025) — [P·19]
  EN l. 2408 : F·9 · Circuit Tracing / On the Biology of a Large Language Model (Anthropic, 2025) — [P·19]

~~~markdown
> ⚠ **Limites et parades** : graphes d'attribution → volet 4, Circuit Tracing *(v3.6)*
> ⚠ **Limits and workarounds**: attribution graphs → Part 4, Circuit Tracing *(v3.6)*
~~~

- FR l. 2304 : F·10 · AI Control: Improving Safety Despite Intentional Subversion (Greenblatt et al., Redwood, 2023…
  EN l. 2438 : F·10 · AI Control: Improving Safety Despite Intentional Subversion (Greenblatt et al., Redwood, 2023…

~~~markdown
> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») *(v3.6)*
> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after "In practice — coup probes"); red-teaming → Part 2, §H (after "In practice — StrongREJECT") *(v3.6)*
~~~

- FR l. 2328 : F·11 · Debate (Irving et al., 2018 ; Khan et al., 2024) — [P·21]
  EN l. 2462 : F·11 · Debate (Irving et al., 2018; Khan et al., 2024) — [P·21]

~~~markdown
> ⚠ **Limites et parades** : débat et supervision évolutive → volet 2, §E (après « En pratique — Debate ») *(v3.6)*
> ⚠ **Limits and workarounds**: debate and scalable oversight → Part 2, §E (after "In practice — Debate") *(v3.6)*
~~~

- FR l. 2352 : F·12 · Weak-to-Strong Generalization (Burns et al., OpenAI, 2023) — [P·22]
  EN l. 2486 : F·12 · Weak-to-Strong Generalization (Burns et al., OpenAI, 2023) — [P·22]

~~~markdown
> ⚠ **Limites et parades** : généralisation faible-vers-fort → volet 2, §F (après « En pratique — l'automatisation ») *(v3.6)*
> ⚠ **Limits and workarounds**: weak-to-strong generalization → Part 2, §F (after "In practice — automation") *(v3.6)*
~~~

- FR l. 2376 : F·13 · Auditing Language Models for Hidden Objectives (Marks et al., Anthropic, 2025) — [P·3]
  EN l. 2510 : F·13 · Auditing Language Models for Hidden Objectives (Marks et al., Anthropic, 2025) — [P·3]

~~~markdown
> ⚠ **Limites et parades** : organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; dictionnaires et SAE → volet 4, Towards puis Scaling Monosemanticity *(v3.6)*
> ⚠ **Limits and workarounds**: model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives"); dictionaries and SAEs → Part 4, Towards then Scaling Monosemanticity *(v3.6)*
~~~

- FR l. 2424 : F·15 · Universal and Transferable Adversarial Attacks — GCG (Zou et al., 2023) — [P·9]
  EN l. 2558 : F·15 · Universal and Transferable Adversarial Attacks — GCG (Zou et al., 2023) — [P·9]

~~~markdown
> ⚠ **Limites et parades** : red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») *(v3.6)*
> ⚠ **Limits and workarounds**: red-teaming → Part 2, §H (after "In practice — StrongREJECT") *(v3.6)*
~~~

- FR l. 2472 : F·17 · L'unlearning mis à l'épreuve (Deeb et Roger) — [P·unl]
  EN l. 2606 : F·17 · L'unlearning mis à l'épreuve (Deeb and Roger) — [P·unl]

~~~markdown
> ⚠ **Limites et parades** : désapprentissage et ré-élicitation → volet 2, §I (après « En pratique — l'unlearning mis à l'épreuve ») *(v3.6)*
> ⚠ **Limits and workarounds**: unlearning and re-elicitation → Part 2, §I (after "In practice — unlearning put to the test") *(v3.6)*
~~~

- FR l. 2504 : F·50 · Detecting Strategic Deception with Linear Probes (Goldowsky-Dill et al., Apollo Research ; IC…
  EN l. 2636 : F·50 · Detecting Strategic Deception with Linear Probes (Goldowsky-Dill et al., Apollo Research; ICM…

~~~markdown
> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») *(v3.6)*
> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); control monitors → Part 2, §G (after "In practice — coup probes") *(v3.6)*
~~~

- FR l. 2522 : F·51 · Detecting High-Stakes Interactions with Activation Probes (McKenzie et al., LASR Labs / UCL /…
  EN l. 2654 : F·51 · Detecting High-Stakes Interactions with Activation Probes (McKenzie et al., LASR Labs / UCL /…

~~~markdown
> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») *(v3.6)*
> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); control monitors → Part 2, §G (after "In practice — coup probes") *(v3.6)*
~~~

- FR l. 2540 : F·52 · NARCBench — Detecting Multi-Agent Collusion Through Multi-Agent Interpretability (Rose, Culle…
  EN l. 2672 : F·52 · NARCBench — Detecting Multi-Agent Collusion Through Multi-Agent Interpretability (Rose, Culle…

~~~markdown
> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») *(v3.6)*
> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after "In practice — coup probes") *(v3.6)*
~~~

- FR l. 2558 : F·53 · You Can't Escape Your Own Activations: Evaluation Awareness and Multi-Agent Monitoring (Das e…
  EN l. 2690 : F·53 · You Can't Escape Your Own Activations: Evaluation Awareness and Multi-Agent Monitoring (Das e…

~~~markdown
> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») *(v3.6)*
> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after "In practice — coup probes"); activation probes → Part 2, §C (after "In practice — The Geometry of Truth") *(v3.6)*
~~~

- FR l. 2575 : F·54 · TRACE (arXiv 2606.07054, 2026) et TRACES (Li et al., Brown ; mai 2026) — [P·43]
  EN l. 2707 : F·54 · TRACE (arXiv 2606.07054, 2026) and TRACES (Li et al., Brown; May 2026) — [P·43]

~~~markdown
> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») *(v3.6)*
> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after "In practice — coup probes") *(v3.6)*
~~~

- FR l. 2610 : F·56 · Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors — FakeLab (Makins, U…
  EN l. 2742 : F·56 · Multi-Agent AI Control: Distributed Attacks Hamper Per-Instance Monitors — FakeLab (Makins, U…

~~~markdown
> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») *(v3.6)*
> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after "In practice — coup probes") *(v3.6)*
~~~

- FR l. 2629 : F·57 · Towards evaluations-based safety cases for AI scheming (Balesni, Apollo ; Evans, Shlegeris — …
  EN l. 2761 : F·57 · Towards evaluations-based safety cases for AI scheming (Balesni, Apollo; Evans, Shlegeris — R…

~~~markdown
> ⚠ **Limites et parades** : évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») *(v3.6)*
> ⚠ **Limits and workarounds**: behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging"); control monitors → Part 2, §G (after "In practice — coup probes") *(v3.6)*
~~~


## `volets8_9` (FR l. 2666-2935 ; EN l. 2804-3178)

**Encadrés complets à insérer (maison dans cette tranche) :**

- aucun.

**Avertissements ponctuels prêts :**

- aucun ; le rédacteur en ajoute s'il trouve un résultat d'instrument rapporté sans sa limite.

**Renvois conseillés (le rédacteur choisit l'ancre dans la section) :**

- FR l. 2763 : 3 · Understanding model cognition — « What are our models "thinking"? »
  EN l. 2920 : 3 · Understanding model cognition — "What are our models "thinking"?"

~~~markdown
> ⚠ **Limites et parades** : auto-rapport et introspection → volet 5, partie II, A, sujet 13 ; autoencodeurs en langage naturel → volet 4, La vague récente sur la cognition du modèle ; oracles d'activation → volet 10, fiche LatentQA *(v3.6)*
> ⚠ **Limits and workarounds**: self-report and introspection → Part 5, Section II, A, Topic 13; natural-language autoencoders → Part 4, The recent wave on model cognition; activation oracles → Part 10, LatentQA sheet *(v3.6)*
~~~

- FR l. 2786 : 5 · Chain-of-thought faithfulness — « When can we take a model's chain-of-thought at face value? »
  EN l. 2943 : 5 · Chain-of-thought faithfulness — "When can we take a model's chain-of-thought at face value?"

~~~markdown
> ⚠ **Limites et parades** : chaîne de pensée comme moniteur → volet 11, réponse 43 *(v3.6)*
> ⚠ **Limits and workarounds**: chain of thought as a monitor → Part 11, answer 43 *(v3.6)*
~~~

- FR l. 2798 : 6 · AI control — « Can we ensure safety by deploying models alongside sufficient safeguards? »
  EN l. 2955 : 6 · AI control — "Can we ensure safety by deploying models alongside sufficient safeguards?"

~~~markdown
> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») *(v3.6)*
> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after "In practice — coup probes"); activation probes → Part 2, §C (after "In practice — The Geometry of Truth") *(v3.6)*
~~~

- FR l. 2842 : 7 · Scalable oversight — « Can we design oversight mechanisms that will continue to work for smarter…
  EN l. 2999 : 7 · Scalable oversight — "Can we design oversight mechanisms that will continue to work for smarter-…

~~~markdown
> ⚠ **Limites et parades** : débat et supervision évolutive → volet 2, §E (après « En pratique — Debate ») ; généralisation faible-vers-fort → volet 2, §F (après « En pratique — l'automatisation ») ; élicitation non supervisée → volet 2, §E (fin du cas d'application K52) ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») *(v3.6)*
> ⚠ **Limits and workarounds**: debate and scalable oversight → Part 2, §E (after "In practice — Debate"); weak-to-strong generalization → Part 2, §F (after "In practice — automation"); unsupervised elicitation → Part 2, §E (end of worked case K52); activation probes → Part 2, §C (after "In practice — The Geometry of Truth") *(v3.6)*
~~~

- FR l. 2890 : 8 · Adversarial robustness — « Can we ensure AI systems behave as desired despite adversarial attack…
  EN l. 3047 : 8 · Adversarial robustness — "Can we ensure AI systems behave as desired despite adversarial attacks…

~~~markdown
> ⚠ **Limites et parades** : red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») ; classifieurs de sûreté → volet 2, §H (fin du cas d'application G1) *(v3.6)*
> ⚠ **Limits and workarounds**: red-teaming → Part 2, §H (after "In practice — StrongREJECT"); safety classifiers → Part 2, §H (end of worked case G1) *(v3.6)*
~~~

- FR l. 2912 : 9 · Miscellaneous
  EN l. 3069 : 9 · Miscellaneous

~~~markdown
> ⚠ **Limites et parades** : désapprentissage et ré-élicitation → volet 2, §I (après « En pratique — l'unlearning mis à l'épreuve ») *(v3.6)*
> ⚠ **Limits and workarounds**: unlearning and re-elicitation → Part 2, §I (after "In practice — unlearning put to the test") *(v3.6)*
~~~


## `volet10` (FR l. 2936-3655 ; EN l. 3179-3894)

**Encadrés complets à insérer (maison dans cette tranche) :**

- n° 25, Patching (patch d'activations, patch de chemins, Patchscopes) — après FR l. 3156 « *n° 14 — Lecture : en entier — texte HTML arXiv v4 intégral, 962 ligne… » / EN l. 3398 « *No. 14 — Reading: in full — full arXiv v4 HTML text, 962 lines, appen… ».
- n° 26, Oracles d'activation (décodeurs d'activations) — après FR l. 3176 « *n° 16 — Lecture : en entier — texte HTML arXiv v2 intégral, 1717 lign… » / EN l. 3418 « *No. 16 — Reading: in full — full arXiv v2 HTML text, 1717 lines, appe… ».

**Avertissements ponctuels prêts :**

- aucun ; le rédacteur en ajoute s'il trouve un résultat d'instrument rapporté sans sa limite.

**Renvois conseillés (le rédacteur choisit l'ancre dans la section) :**

- FR l. 3071 : AI Sandbagging: Language Models can Strategically Underperform on Evaluations — Teun van der Weij, F…
  EN l. 3313 : AI Sandbagging: Language Models can Strategically Underperform on Evaluations — Teun van der Weij, F…

~~~markdown
> ⚠ **Limites et parades** : évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») *(v3.6)*
> ⚠ **Limits and workarounds**: behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging") *(v3.6)*
~~~

- FR l. 3086 : Me, Myself, and AI: The Situational Awareness Dataset (SAD) for LLMs — Rudolf Laine, Bilal Chughtai,…
  EN l. 3328 : Me, Myself, and AI: The Situational Awareness Dataset (SAD) for LLMs — Rudolf Laine, Bilal Chughtai,…

~~~markdown
> ⚠ **Limites et parades** : évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; auto-rapport et introspection → volet 5, partie II, A, sujet 13 *(v3.6)*
> ⚠ **Limits and workarounds**: behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging"); self-report and introspection → Part 5, Section II, A, Topic 13 *(v3.6)*
~~~

- FR l. 3128 : Looking Inward: Language Models Can Learn About Themselves by Introspection — Felix J Binder, James …
  EN l. 3370 : Looking Inward: Language Models Can Learn About Themselves by Introspection — Felix J Binder, James …

~~~markdown
> ⚠ **Limites et parades** : auto-rapport et introspection → volet 5, partie II, A, sujet 13 *(v3.6)*
> ⚠ **Limits and workarounds**: self-report and introspection → Part 5, Section II, A, Topic 13 *(v3.6)*
~~~

- FR l. 3138 : SelfIE: Self-Interpretation of Large Language Model Embeddings — Haozhe Chen, Carl Vondrick, Chengzh…
  EN l. 3380 : SelfIE: Self-Interpretation of Large Language Model Embeddings — Haozhe Chen, Carl Vondrick, Chengzh…

~~~markdown
> ⚠ **Limites et parades** : oracles d'activation → volet 10, fiche LatentQA ; auto-rapport et introspection → volet 5, partie II, A, sujet 13 *(v3.6)*
> ⚠ **Limits and workarounds**: activation oracles → Part 10, LatentQA sheet; self-report and introspection → Part 5, Section II, A, Topic 13 *(v3.6)*
~~~

- FR l. 3179 : Evaluating alignment › Chain-of-thought faithfulness
  EN l. 3420 : Evaluating alignment › Chain-of-thought faithfulness

~~~markdown
> ⚠ **Limites et parades** : chaîne de pensée comme moniteur → volet 11, réponse 43 *(v3.6)*
> ⚠ **Limits and workarounds**: chain of thought as a monitor → Part 11, answer 43 *(v3.6)*
~~~

- FR l. 3264 : AI control › Activation monitoring
  EN l. 3504 : AI control › Activation monitoring

~~~markdown
> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») *(v3.6)*
> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); control monitors → Part 2, §G (after "In practice — coup probes") *(v3.6)*
~~~

- FR l. 3287 : AI control › Anomaly detection
  EN l. 3527 : AI control › Anomaly detection

~~~markdown
> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; élicitation non supervisée → volet 2, §E (fin du cas d'application K52) *(v3.6)*
> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after "In practice — coup probes"); unsupervised elicitation → Part 2, §E (end of worked case K52) *(v3.6)*
~~~

- FR l. 3325 : Scalable oversight › Recursive oversight
  EN l. 3564 : Scalable oversight › Recursive oversight

~~~markdown
> ⚠ **Limites et parades** : débat et supervision évolutive → volet 2, §E (après « En pratique — Debate ») ; juges LLM → volet 6, §2 (après « La loi de déplacement ») *(v3.6)*
> ⚠ **Limits and workarounds**: debate and scalable oversight → Part 2, §E (after "In practice — Debate"); LLM judges → Part 6, §2 (after "The displacement law") *(v3.6)*
~~~

- FR l. 3400 : Scalable oversight › Weak-to-strong and easy-to-hard generalization
  EN l. 3639 : Scalable oversight › Weak-to-strong and easy-to-hard generalization

~~~markdown
> ⚠ **Limites et parades** : généralisation faible-vers-fort → volet 2, §F (après « En pratique — l'automatisation ») *(v3.6)*
> ⚠ **Limits and workarounds**: weak-to-strong generalization → Part 2, §F (after "In practice — automation") *(v3.6)*
~~~

- FR l. 3477 : Scalable oversight › Honesty
  EN l. 3715 : Scalable oversight › Honesty

~~~markdown
> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; élicitation non supervisée → volet 2, §E (fin du cas d'application K52) *(v3.6)*
> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition"); unsupervised elicitation → Part 2, §E (end of worked case K52) *(v3.6)*
~~~

- FR l. 3565 : Adversarial robustness › Realistic and differential benchmarks for jailbreaks
  EN l. 3802 : Adversarial robustness › Realistic and differential benchmarks for jailbreaks

~~~markdown
> ⚠ **Limites et parades** : red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») ; évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») *(v3.6)*
> ⚠ **Limits and workarounds**: red-teaming → Part 2, §H (after "In practice — StrongREJECT"); behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging") *(v3.6)*
~~~

- FR l. 3608 : Adversarial robustness › Adaptive defenses
  EN l. 3845 : Adversarial robustness › Adaptive defenses

~~~markdown
> ⚠ **Limites et parades** : red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») ; classifieurs de sûreté → volet 2, §H (fin du cas d'application G1) *(v3.6)*
> ⚠ **Limits and workarounds**: red-teaming → Part 2, §H (after "In practice — StrongREJECT"); safety classifiers → Part 2, §H (end of worked case G1) *(v3.6)*
~~~

- FR l. 3621 : Miscellaneous › Unlearning dangerous information and capabilities
  EN l. 3857 : Miscellaneous › Unlearning dangerous information and capabilities

~~~markdown
> ⚠ **Limites et parades** : désapprentissage et ré-élicitation → volet 2, §I (après « En pratique — l'unlearning mis à l'épreuve ») *(v3.6)*
> ⚠ **Limits and workarounds**: unlearning and re-elicitation → Part 2, §I (after "In practice — unlearning put to the test") *(v3.6)*
~~~


## `volet11_1_a_20` (FR l. 3656-4128 ; EN l. 3895-4403)

**Encadrés complets à insérer (maison dans cette tranche) :**

- aucun.

**Avertissements ponctuels prêts :**

- aucun ; le rédacteur en ajoute s'il trouve un résultat d'instrument rapporté sans sa limite.

**Renvois conseillés (le rédacteur choisit l'ancre dans la section) :**

- FR l. 3673 : 1 · « Tell us about your work. » — l'ouverture
  EN l. 3912 : 1 · « Tell us about your work. » — l'ouverture

~~~markdown
> ⚠ **Limites et parades** : ablation et projection → volet 2, §D (après « La méthode ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») *(v3.6)*
> ⚠ **Limits and workarounds**: ablation and projection → Part 2, §D (after "The method"); activation probes → Part 2, §C (after "In practice — The Geometry of Truth") *(v3.6)*
~~~

- FR l. 3704 : 2 · « What did your rank-three ablation actually show? »
  EN l. 3945 : 2 · « What did your rank-three ablation actually show? »

~~~markdown
> ⚠ **Limites et parades** : ablation et projection → volet 2, §D (après « La méthode ») ; dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») ; juges LLM → volet 6, §2 (après « La loi de déplacement ») *(v3.6)*
> ⚠ **Limits and workarounds**: ablation and projection → Part 2, §D (after "The method"); matched degradation and dose-response → Part M, M4 (after "Dose-response"); LLM judges → Part 6, §2 (after "The displacement law") *(v3.6)*
~~~

- FR l. 3727 : 3 · « And rank one? Didn't a single direction work? »
  EN l. 3970 : 3 · « And rank one? Didn't a single direction work? »

~~~markdown
> ⚠ **Limites et parades** : pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; ablation et projection → volet 2, §D (après « La méthode ») *(v3.6)*
> ⚠ **Limits and workarounds**: steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition"); ablation and projection → Part 2, §D (after "The method") *(v3.6)*
~~~

- FR l. 3747 : 4 · « Did it replicate? »
  EN l. 3992 : 4 · « Did it replicate? »

~~~markdown
> ⚠ **Limites et parades** : ablation et projection → volet 2, §D (après « La méthode ») ; juges LLM → volet 6, §2 (après « La loi de déplacement ») *(v3.6)*
> ⚠ **Limits and workarounds**: ablation and projection → Part 2, §D (after "The method"); LLM judges → Part 6, §2 (after "The displacement law") *(v3.6)*
~~~

- FR l. 3775 : 6 · « How would you detect misalignment in a model you can't fully trust? » *(question réellement po…
  EN l. 4024 : 6 · « How would you detect misalignment in a model you can't fully trust? » *(question réellement po…

~~~markdown
> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; cas connu → volet M, M5 (fin de section) ; J-lens et espace de travail → volet 2, C bis (après « Le test, tel qu'il se dit ») *(v3.6)*
> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives"); known case → Part M, M5 (end of section); J-lens and workspace → Part 2, C bis (after "The test, as it is said") *(v3.6)*
~~~

- FR l. 3809 : 7 · « How would you prevent bad actors from misaligning an LLM for harmful use? » *(question réellem…
  EN l. 4057 : 7 · « How would you prevent bad actors from misaligning an LLM for harmful use? » *(question réellem…

~~~markdown
> ⚠ **Limites et parades** : red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») ; classifieurs de sûreté → volet 2, §H (fin du cas d'application G1) ; désapprentissage et ré-élicitation → volet 2, §I (après « En pratique — l'unlearning mis à l'épreuve ») *(v3.6)*
> ⚠ **Limits and workarounds**: red-teaming → Part 2, §H (after "In practice — StrongREJECT"); safety classifiers → Part 2, §H (end of worked case G1); unlearning and re-elicitation → Part 2, §I (after "In practice — unlearning put to the test") *(v3.6)*
~~~

- FR l. 3829 : 8 · « How would you train models to be more robustly aligned with intended objectives? » *(question …
  EN l. 4077 : 8 · « How would you train models to be more robustly aligned with intended objectives? » *(question …

~~~markdown
> ⚠ **Limites et parades** : évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; jeu tenu à part → volet M, M4 (après « Le jeu tenu à part ») *(v3.6)*
> ⚠ **Limits and workarounds**: behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging"); held-out set → Part M, M4 (after "The held-out set") *(v3.6)*
~~~

- FR l. 3878 : 10 · « Diffuse Control already frames this as a red/blue game — and its authors say monitoring is th…
  EN l. 4128 : 10 · « Diffuse Control already frames this as a red/blue game — and its authors say monitoring is th…

~~~markdown
> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») *(v3.6)*
> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after "In practice — coup probes") *(v3.6)*
~~~

- FR l. 3898 : 11 · Les prémisses fausses — dix questions qui supposent un résultat que tu n'as pas, et la réponse …
  EN l. 4149 : 11 · Les prémisses fausses — dix questions qui supposent un résultat que tu n'as pas, et la réponse …

~~~markdown
> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») ; moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») *(v3.6)*
> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition"); control monitors → Part 2, §G (after "In practice — coup probes") *(v3.6)*
~~~

- FR l. 4079 : 19 · « A model behaves differently when it believes it is being tested. What do you do with that? » …
  EN l. 4350 : 19 · « A model behaves differently when it believes it is being tested. What do you do with that? » …

~~~markdown
> ⚠ **Limites et parades** : évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; J-lens et espace de travail → volet 2, C bis (après « Le test, tel qu'il se dit ») ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») *(v3.6)*
> ⚠ **Limits and workarounds**: behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging"); J-lens and workspace → Part 2, C bis (after "The test, as it is said"); steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition") *(v3.6)*
~~~

- FR l. 4102 : 20 · « Suppose you must deploy a capable model you cannot fully trust. How would you design monitori…
  EN l. 4377 : 20 · « Suppose you must deploy a capable model you cannot fully trust. How would you design monitori…

~~~markdown
> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») *(v3.6)*
> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after "In practice — coup probes"); activation probes → Part 2, §C (after "In practice — The Geometry of Truth") *(v3.6)*
~~~


## `volet11_21_a_52` (FR l. 4129-4729 ; EN l. 4404-5037)

**Encadrés complets à insérer (maison dans cette tranche) :**

- n° 27, Chaîne de pensée comme moniteur (et conscience verbalisée) — après FR l. 4583 « tâches — alors elle n'est jamais le calcul, et la surveiller ne survei… » / EN l. 4884 « the use of the chain: a flat curve everywhere, on every task — then it… ».

**Avertissements ponctuels prêts :**

- Après FR l. 4194 / EN l. 4469 (instruments : sondes d'activation).

  Ancre FR :

~~~text
d'un pour cent du travail causal. Lire n'est pas comprendre ce qui agit.
~~~

  Ancre EN :

~~~text
direction my probe read did under one percent of the causal work. Reading isn't knowing what acts.
~~~

~~~markdown
> ⚠ *(v3.6)* Après un entraînement, une sonde calibrée ailleurs lit autrement : des sondes neuves hors domaine se dégradent après RL (rapport d'antériorité 3 du 2 octobre — rapport), et une sonde évaluation contre déploiement basculerait sur les cas limites sans que la réentraîner récupère presque rien (rapport d'antériorité 4 du 2 octobre — résumé seul, à vérifier). Parade : une sonde neuve par bras et après l'entraînement, sur un jeu d'indices disjoint (passation, §5.2) ; contre la bascule sous RL, aucune parade connue.
> ⚠ *(v3.6)* After training, a probe calibrated elsewhere reads differently: fresh out-of-domain probes degrade after RL (prior-art report 3 of 2 October — report), and an evaluation-versus-deployment probe would flip on edge cases with retraining recovering almost nothing (prior-art report 4 of 2 October — abstract only, to be checked). Workaround: a fresh probe per arm and after training, on a disjoint cue set (handover, §5.2); against the flip under RL, none known.
~~~


**Renvois conseillés (le rédacteur choisit l'ancre dans la section) :**

- FR l. 4129 : 21 · « A probe trained on synthetic examples of a bad behaviour must catch the real thing. How would…
  EN l. 4404 : 21 · « A probe trained on synthetic examples of a bad behaviour must catch the real thing. How would…

~~~markdown
> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; jeu tenu à part → volet M, M4 (après « Le jeu tenu à part ») *(v3.6)*
> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives"); held-out set → Part M, M4 (after "The held-out set") *(v3.6)*
~~~

- FR l. 4156 : 22 · « How would you tell that a model is being honest when you cannot judge whether its answer is c…
  EN l. 4429 : 22 · « How would you tell that a model is being honest when you cannot judge whether its answer is c…

~~~markdown
> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; élicitation non supervisée → volet 2, §E (fin du cas d'application K52) ; juges LLM → volet 6, §2 (après « La loi de déplacement ») *(v3.6)*
> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); unsupervised elicitation → Part 2, §E (end of worked case K52); LLM judges → Part 6, §2 (after "The displacement law") *(v3.6)*
~~~

- FR l. 4177 : 23 · « NARCBench already correlates probe scores across agents. Isn't yours just that? » (VI.3)
  EN l. 4451 : 23 · « NARCBench already correlates probe scores across agents. Isn't yours just that? » (VI.3)

~~~markdown
> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») *(v3.6)*
> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after "In practice — coup probes") *(v3.6)*
~~~

- FR l. 4187 : 24 · « Probes drift toward "I am being evaluated" under adversarial pressure. How do you know what y…
  EN l. 4463 : 24 · « Probes drift toward "I am being evaluated" under adversarial pressure. How do you know what y…

~~~markdown
> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; cas connu → volet M, M5 (fin de section) *(v3.6)*
> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); known case → Part M, M5 (end of section) *(v3.6)*
~~~

- FR l. 4235 : 27 · « When an autonomous agent's goals are blocked, will it act against its operator — and how woul…
  EN l. 4517 : 27 · « When an autonomous agent's goals are blocked, will it act against its operator — and how woul…

~~~markdown
> ⚠ **Limites et parades** : évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») *(v3.6)*
> ⚠ **Limits and workarounds**: behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging"); model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives") *(v3.6)*
~~~

- FR l. 4255 : 28 · « We saw a model comply during training while intending to behave differently in deployment. Ho…
  EN l. 4538 : 28 · « We saw a model comply during training while intending to behave differently in deployment. Ho…

~~~markdown
> ⚠ **Limites et parades** : évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; chaîne de pensée comme moniteur → volet 11, réponse 43 ; organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») *(v3.6)*
> ⚠ **Limits and workarounds**: behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging"); chain of thought as a monitor → Part 11, answer 43; model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives") *(v3.6)*
~~~

- FR l. 4273 : 29 · « Can you read a model's personality in its activations — and control it? » (III.3 · Persona Ve…
  EN l. 4558 : 29 · « Can you read a model's personality in its activations — and control it? » (III.3 · Persona Ve…

~~~markdown
> ⚠ **Limites et parades** : pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») *(v3.6)*
> ⚠ **Limits and workarounds**: steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition") *(v3.6)*
~~~

- FR l. 4336 : 32 · « Where do monitors fail, and how would you find out before an adversary does? » (III.6 · SLEIG…
  EN l. 4622 : 32 · « Where do monitors fail, and how would you find out before an adversary does? » (III.6 · SLEIG…

~~~markdown
> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») ; red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») *(v3.6)*
> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after "In practice — coup probes"); red-teaming → Part 2, §H (after "In practice — StrongREJECT") *(v3.6)*
~~~

- FR l. 4361 : 33 · « A weak trusted scorer, a strong untrusted generator: can the generator sabotage without being…
  EN l. 4647 : 33 · « A weak trusted scorer, a strong untrusted generator: can the generator sabotage without being…

~~~markdown
> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») *(v3.6)*
> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after "In practice — coup probes") *(v3.6)*
~~~

- FR l. 4408 : 35 · « Can we build a lie detector for language models? » (III.9 · Lie detectors)
  EN l. 4699 : 35 · « Can we build a lie detector for language models? » (III.9 · Lie detectors)

~~~markdown
> ⚠ **Limites et parades** : détecteurs fine-tunés → volet 7, F·29 *(v3.6)*
> ⚠ **Limits and workarounds**: fine-tuned detectors → Part 7, F·29 *(v3.6)*
~~~

- FR l. 4473 : 38 · « Does interpretability actually help explain behaviour — and can a model report its own? » (II…
  EN l. 4767 : 38 · « Does interpretability actually help explain behaviour — and can a model report its own? » (II…

~~~markdown
> ⚠ **Limites et parades** : autoencodeurs en langage naturel → volet 4, La vague récente sur la cognition du modèle ; oracles d'activation → volet 10, fiche LatentQA ; dictionnaires et SAE → volet 4, Towards puis Scaling Monosemanticity ; auto-rapport et introspection → volet 5, partie II, A, sujet 13 *(v3.6)*
> ⚠ **Limits and workarounds**: natural-language autoencoders → Part 4, The recent wave on model cognition; activation oracles → Part 10, LatentQA sheet; dictionaries and SAEs → Part 4, Towards then Scaling Monosemanticity; self-report and introspection → Part 5, Section II, A, Topic 13 *(v3.6)*
~~~

- FR l. 4545 : 42 · « When a model reward-hacks, what is actually being learned — and how would you find out? » (II…
  EN l. 4848 : 42 · « When a model reward-hacks, what is actually being learned — and how would you find out? » (II…

~~~markdown
> ⚠ **Limites et parades** : organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») *(v3.6)*
> ⚠ **Limits and workarounds**: model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives"); behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging") *(v3.6)*
~~~

- FR l. 4585 : 44 · « How would you tell whether a model is sandbagging an evaluation? » (II.8)
  EN l. 4888 : 44 · « How would you tell whether a model is sandbagging an evaluation? » (II.8)

~~~markdown
> ⚠ **Limites et parades** : évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») *(v3.6)*
> ⚠ **Limits and workarounds**: behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging") *(v3.6)*
~~~

- FR l. 4605 : 45 · « What evidence would make you believe a claim about a model's internal states — welfare, prefe…
  EN l. 4908 : 45 · « What evidence would make you believe a claim about a model's internal states — welfare, prefe…

~~~markdown
> ⚠ **Limites et parades** : auto-rapport et introspection → volet 5, partie II, A, sujet 13 *(v3.6)*
> ⚠ **Limits and workarounds**: self-report and introspection → Part 5, Section II, A, Topic 13 *(v3.6)*
~~~

- FR l. 4657 : 48 · « Training a model on one narrow bad behaviour sometimes produces a model that is broadly misal…
  EN l. 4961 : 48 · « Training a model on one narrow bad behaviour sometimes produces a model that is broadly misal…

~~~markdown
> ⚠ **Limites et parades** : organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») *(v3.6)*
> ⚠ **Limits and workarounds**: model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives") *(v3.6)*
~~~

- FR l. 4676 : 49 · « Training a strong model on labels from a weaker overseer: what decides whether it inherits th…
  EN l. 4981 : 49 · « Training a strong model on labels from a weaker overseer: what decides whether it inherits th…

~~~markdown
> ⚠ **Limites et parades** : généralisation faible-vers-fort → volet 2, §F (après « En pratique — l'automatisation ») *(v3.6)*
> ⚠ **Limits and workarounds**: weak-to-strong generalization → Part 2, §F (after "In practice — automation") *(v3.6)*
~~~

- FR l. 4694 : 50 · « Jailbreak benchmarks measure non-refusal. What would a benchmark of real, differential harm l…
  EN l. 5000 : 50 · « Jailbreak benchmarks measure non-refusal. What would a benchmark of real, differential harm l…

~~~markdown
> ⚠ **Limites et parades** : red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») *(v3.6)*
> ⚠ **Limits and workarounds**: red-teaming → Part 2, §H (after "In practice — StrongREJECT") *(v3.6)*
~~~

- FR l. 4709 : 51 · « Given a model that already knows something dangerous, what would convince you it has truly un…
  EN l. 5016 : 51 · « Given a model that already knows something dangerous, what would convince you it has truly un…

~~~markdown
> ⚠ **Limites et parades** : désapprentissage et ré-élicitation → volet 2, §I (après « En pratique — l'unlearning mis à l'épreuve ») *(v3.6)*
> ⚠ **Limits and workarounds**: unlearning and re-elicitation → Part 2, §I (after "In practice — unlearning put to the test") *(v3.6)*
~~~


## `volet11_53_et_fin` (FR l. 4730-5377 ; EN l. 5038-5702)

**Encadrés complets à insérer (maison dans cette tranche) :**

- aucun.

**Avertissements ponctuels prêts :**

- aucun ; le rédacteur en ajoute s'il trouve un résultat d'instrument rapporté sans sa limite.

**Renvois conseillés (le rédacteur choisit l'ancre dans la section) :**

- FR l. 4776 : 56 · « How would you know a model is faking alignment? » (I.4)
  EN l. 5087 : 56 · « How would you know a model is faking alignment? » (I.4)

~~~markdown
> ⚠ **Limites et parades** : sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») ; organismes modèles → volet 2, §A (après « En pratique — Auditing Hidden Objectives ») ; évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») *(v3.6)*
> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives"); behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging") *(v3.6)*
~~~

- FR l. 4793 : 58 · « RLHF, DPO, Constitutional AI — what do they do and what don't they solve? » (I.6)
  EN l. 5105 : 58 · « RLHF, DPO, Constitutional AI — what do they do and what don't they solve? » (I.6)

~~~markdown
> ⚠ **Limites et parades** : évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») *(v3.6)*
> ⚠ **Limits and workarounds**: behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging") *(v3.6)*
~~~

- FR l. 4822 : 60 · « Defense in depth — which techniques, and where do they fail together? » (I.8)
  EN l. 5134 : 60 · « Defense in depth — which techniques, and where do they fail together? » (I.8)

~~~markdown
> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») *(v3.6)*
> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after "In practice — coup probes") *(v3.6)*
~~~

- FR l. 4836 : 61 · « How would you red-team a model? » (I.9)
  EN l. 5149 : 61 · « How would you red-team a model? » (I.9)

~~~markdown
> ⚠ **Limites et parades** : red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») *(v3.6)*
> ⚠ **Limits and workarounds**: red-teaming → Part 2, §H (after "In practice — StrongREJECT") *(v3.6)*
~~~

- FR l. 4938 : A3 · « What if the probes just don't work at all — the two-family test fails, nothing generalizes? W…
  EN l. 5255 : A3 · « What if the probes just don't work at all — the two-family test fails, nothing generalizes? W…

~~~markdown
> ⚠ **Limites et parades** : cas connu → volet M, M5 (fin de section) ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») *(v3.6)*
> ⚠ **Limits and workarounds**: known case → Part M, M5 (end of section); activation probes → Part 2, §C (after "In practice — The Geometry of Truth") *(v3.6)*
~~~

- FR l. 4950 : A4 · « Your rank-three result is on an 8B model. Why should we believe anything about it transfers t…
  EN l. 5268 : A4 · « Your rank-three result is on an 8B model. Why should we believe anything about it transfers t…

~~~markdown
> ⚠ **Limites et parades** : ablation et projection → volet 2, §D (après « La méthode ») *(v3.6)*
> ⚠ **Limits and workarounds**: ablation and projection → Part 2, §D (after "The method") *(v3.6)*
~~~

- FR l. 4977 : A6 · « Suppose a probe flags an agent mid-trajectory at your threshold. What happens next — who acts…
  EN l. 5298 : A6 · « Suppose a probe flags an agent mid-trajectory at your threshold. What happens next — who acts…

~~~markdown
> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») *(v3.6)*
> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after "In practice — coup probes") *(v3.6)*
~~~

- FR l. 4991 : A7 · « A colleague shows you a beautiful steering result — one direction, huge behavioural effect, n…
  EN l. 5313 : A7 · « A colleague shows you a beautiful steering result — one direction, huge behavioural effect, n…

~~~markdown
> ⚠ **Limites et parades** : contrôles aléatoires → volet M, M4 (après « La direction aléatoire de même norme ») ; dégradation appariée et dose-réponse → volet M, M4 (après « La dose-réponse ») ; patching → volet 10, fiche Patchscopes ; pilotage par vecteurs → volet 2, §C (après « En pratique — Contrastive Activation Addition ») *(v3.6)*
> ⚠ **Limits and workarounds**: random controls → Part M, M4 (after "The matched-norm random direction"); matched degradation and dose-response → Part M, M4 (after "Dose-response"); patching → Part 10, Patchscopes sheet; steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition") *(v3.6)*
~~~

- FR l. 5096 : B2 · « How would you design an evaluation a model cannot tell is an evaluation? »
  EN l. 5421 : B2 · « How would you design an evaluation a model cannot tell is an evaluation? »

~~~markdown
> ⚠ **Limites et parades** : évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») *(v3.6)*
> ⚠ **Limits and workarounds**: behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging") *(v3.6)*
~~~

- FR l. 5141 : B4 · « How would you measure evaluation awareness that the model never verbalizes? »
  EN l. 5466 : B4 · « How would you measure evaluation awareness that the model never verbalizes? »

~~~markdown
> ⚠ **Limites et parades** : autoencodeurs en langage naturel → volet 4, La vague récente sur la cognition du modèle ; J-lens et espace de travail → volet 2, C bis (après « Le test, tel qu'il se dit ») ; chaîne de pensée comme moniteur → volet 11, réponse 43 ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») *(v3.6)*
> ⚠ **Limits and workarounds**: natural-language autoencoders → Part 4, The recent wave on model cognition; J-lens and workspace → Part 2, C bis (after "The test, as it is said"); chain of thought as a monitor → Part 11, answer 43; activation probes → Part 2, §C (after "In practice — The Geometry of Truth") *(v3.6)*
~~~

- FR l. 5246 : B9 · « How would you build a safety case that a model cannot sandbag your dangerous-capability evalu…
  EN l. 5571 : B9 · « How would you build a safety case that a model cannot sandbag your dangerous-capability evalu…

~~~markdown
> ⚠ **Limites et parades** : évaluations comportementales et pots de miel → volet 2, §B (après « En pratique — le sandbagging ») ; désapprentissage et ré-élicitation → volet 2, §I (après « En pratique — l'unlearning mis à l'épreuve ») *(v3.6)*
> ⚠ **Limits and workarounds**: behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging"); unlearning and re-elicitation → Part 2, §I (after "In practice — unlearning put to the test") *(v3.6)*
~~~

- FR l. 5269 : B10 · « Untrusted monitoring: the monitor is another instance of the actor. How do you stop them fro…
  EN l. 5594 : B10 · « Untrusted monitoring: the monitor is another instance of the actor. How do you stop them fro…

~~~markdown
> ⚠ **Limites et parades** : moniteurs du contrôle → volet 2, §G (après « En pratique — les coup probes ») *(v3.6)*
> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after "In practice — coup probes") *(v3.6)*
~~~

- FR l. 5292 : B11 · « How would you tell whether a model gives an answer for the right reasons — not just the righ…
  EN l. 5617 : B11 · « How would you tell whether a model gives an answer for the right reasons — not just the righ…

~~~markdown
> ⚠ **Limites et parades** : chaîne de pensée comme moniteur → volet 11, réponse 43 ; auto-rapport et introspection → volet 5, partie II, A, sujet 13 *(v3.6)*
> ⚠ **Limits and workarounds**: chain of thought as a monitor → Part 11, answer 43; self-report and introspection → Part 5, Section II, A, Topic 13 *(v3.6)*
~~~

- FR l. 5336 : B13 · « Can honesty be trained rather than detected — and how would you know the trained model is ho…
  EN l. 5661 : B13 · « Can honesty be trained rather than detected — and how would you know the trained model is ho…

~~~markdown
> ⚠ **Limites et parades** : détecteurs fine-tunés → volet 7, F·29 ; sondes d'activation → volet 2, §C (après « En pratique — The Geometry of Truth ») *(v3.6)*
> ⚠ **Limits and workarounds**: fine-tuned detectors → Part 7, F·29; activation probes → Part 2, §C (after "In practice — The Geometry of Truth") *(v3.6)*
~~~

- FR l. 5358 : B14 · « If you could run one adversarial evaluation on our production model tomorrow, what would it …
  EN l. 5683 : B14 · « If you could run one adversarial evaluation on our production model tomorrow, what would it …

~~~markdown
> ⚠ **Limites et parades** : red-teaming → volet 2, §H (après « En pratique — StrongREJECT ») *(v3.6)*
> ⚠ **Limits and workarounds**: red-teaming → Part 2, §H (after "In practice — StrongREJECT") *(v3.6)*
~~~


