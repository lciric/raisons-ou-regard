# EA Funds application — Lazar Ciric (merged version) — copie expurgée pour git

7 October 2026. Merges three drafts:
- the complete draft of 7 October, a 6-month bridge for three sycophancy papers;
- a second instance's "about me" text;
- the Claude Code session's draft for "Reasons or being watched?".

Lazar's decision: one 6-month bridge, which finishes the sycophancy papers, then runs the minimal experiment of "Reasons or being watched?". The answers below are in English, the language of the form, and follow its fields in order. The notes for Lazar, in French, are at the end. The budget is in `EA_FUNDS_BUDGET_2026-10-07.xlsx`, EA Funds' own template.

## Form at a glance

| Form field | Answer |
| --- | --- |
| Fund | Transformative AI Fund |
| Which applies to you | INDIVIDUAL – I am seeking funding as an individual |
| Grant program | Transformative AI Research Grants |
| Organization name | Leave empty (the form asks not to write N/A) |
| Main collaborators | Leave empty (working independently) |
| Employed by or contracted with CEA | No |
| Start date, end date | 1 Dec 2026, 31 May 2027 (to confirm) |
| Requested currency | EUR |
| Location | Paris, France; the work is published openly and is not tied to one country |
| China or India; award for past achievement; people under 18; lobbying | No; No; No; No |
| Organisational leadership | Leave empty |
| Referral to other funders | Yes |
| Secondary fund (EA Infrastructure Fund) | No |
| How did you hear about EA Funds? | [[to fill]] |
| Time-sensitive grant | No |
| Public reporting | PUBLIC (see the confidential field for the embargoed study) |
| Network sharing | Yes |
| LinkedIn/CV | linkedin.com/in/lazar-ciric-55a23913b, github.com/lciric; upload the CV PDF |
| File upload | the budget spreadsheet, if not linked |

## Short description

> 6-month bridge: finish two sycophancy papers, then test whether evaluation awareness drives reason-based alignment

## Summary

> Independent AI safety researcher in Paris (ENS physics and computational neuroscience; PLOS Comp Biol 2023; IBM Research Zurich). I request a 6-month bridge, stipend and compute, for two lines of work on open-weight LLMs. (1) Finish two sycophancy papers. Behaviour: on Llama-3.1-8B, social pressure moves a rating a fixed fraction of the way to a destination set by the social frame (R² 0.77/0.79), with parameters that transfer to a new campaign; next, 200 items and a design separating deference from rational updating. Measurement: my own audit found a storage truncation that turned a generic shift into an apparent safety effect; next, a validity battery for LLM judges. (2) Test whether reason-based fine-tuning generalizes because the model knows it is evaluated, by inhibiting a validated representation of evaluation awareness against damage-matched random controls; the first model organism and probe are built. Preregistered and audited.

## Track record

*The form's "Track record" field. This text opens with the "about me" part, as in the earlier draft.*

> Trained in physics and computational neuroscience, I keep asking one question: is the structure we can read out of a high-dimensional system the structure the system uses?
>
> **Training and research:**
> - ENS Paris-Saclay, physics (2016–2020), with stays at Lawrence Berkeley Lab.
> - ENS Ulm, Cogmaster (2020). Thesis with Srdjan Ostojic, published in PLOS Computational Biology (2023).
> - IBM Research Zurich, internship (2020–2021), published in Neuromorphic Computing and Engineering (2022).
> - NeuroPSI with Alain Destexhe (2022).
> - [[Dehaene line, in the CV's exact wording]] (2023).
> - Mines Paris-PSL, statistics and ML (2025).
> - AI lead consultant at EPSA Innovation since 2024.
>
> **Independent AI safety program since 2025.** One person, self-funded, [[part-time in 2025, full-time in 2026]]; [[about €X of my own money]] on compute and API.
> - **A displacement law for sycophancy.** On Llama-3.1-8B-Instruct, pressure moves a rating a fraction g ≈ 0.70 of its distance to a destination set by the frame: about 1.46 under criticism, 2.94 under praise. The fit gives R² 0.77/0.79, and the parameters transfer to a second campaign (R² 0.73/0.69). Preregistered: the interlocutor's opinion moves the model about twice as far as a third-party fact. On Qwen2.5-7B, the law collapses.
> - **Readable is not causal.** A behaviour-tracking probe direction does under 1% of the causal work; the full state does 68%.
> - **Failures, kept.** A rank-3 ablation lowered judged sycophancy from 61% to 46.5% (N = 200, p = 0.0019). A zero-pressure control later showed the same shift with no pressure at all. Responses stored truncated at 300 characters had turned a generic softening into a safety effect. I report the claim as revised, not repaired. Two failed predictions of the law stay in the register.
> - **Process.** Sealed preregistrations, SHA-256 custody of artefacts, and an audited claims register.
>
> **"Reasons or being watched?", since 3 October 2026**, in a private repository shared on request:
> - a programme with its decision rules written before the data;
> - a model organism that type-annotates code on 60.8% of tasks under an evaluation cue, against 6.4% under a deployment cue;
> - an evaluation-awareness probe that reads held-out cues at AUROC 0.857, against 0.634 for a bag of words.
>
> I am at the final stage of the 2026 Anthropic Fellows Program.

## Public portfolio

> github.com/lciric/sycophancy-construct-validity (TRACEABILITY.md maps every README number to its result file); github.com/lciric/safety-concept-vectors; github.com/lciric/eval-awareness-detection (committed 11 March 2026); github.com/lciric/does-quantization-kill-interpretability; doi.org/10.1371/journal.pcbi.1011315; doi.org/10.1088/2634-4386/ac4fb7

## Project goals

> **Goal.** Within six months, three public papers with code. Each answers a question oversight depends on:
> - how social pressure moves a model's judgment;
> - whether the instruments behind judged safety effects can be trusted;
> - whether the out-of-distribution advantage of reason-based fine-tuning depends on the model's representation of being evaluated.
>
> **Why.** Oversight assumes that a model reports its own assessment, not the overseer's. It also assumes that alignment measured under evaluation holds in deployment. Sycophancy degrades human feedback, and evaluation-conditional behaviour makes evaluations overstate safety. In my own work, one silent storage choice manufactured a safety effect.
>
> **1. The law at scale (months 1–2).** 200 items, under a sealed preregistration. The design crosses the source of pressure (interlocutor or third-party fact) with its stage (live, or after the model has committed). A 70B check runs through NDIF if the model is hosted. Deliverable: a preprint and an ICML 2027 submission.
>
> **2. Measurement (month 3).** A validity battery for LLM-judged sycophancy: 600 responses re-judged on two scales, judge drift on a frozen anchor set, sensitivity to truncation and storage, and a comparison of judges. Deliverable: a short paper and a reporting checklist.
>
> **3. Reasons or being watched? (months 3–6).**
> - Validate an inhibition of "I am being evaluated" on model organisms. The setting is chosen on half the tasks, then tested once on the other half, against at least 100 random subspaces matched on damage.
> - Train six arms on identical aligned actions, from actions only to per-example reasons.
> - Measure how much of the reasons' advantage survives the inhibition.
> Deliverables: an Alignment Forum post (month 5) and a preprint (month 6).
>
> **How I will know.** Acceptance criteria are sealed before the data. Each paper ships whichever way they come out, a failed instrument gate included.
>
> **Impact.** The papers, code and checklist are for interpretability and evaluation researchers. The validated inhibition can be reused to check other internals-based monitors. The bridge also carries the work to a full-time position, a fellowship or a PhD.

## Why these goals might not be achieved

> - **Two lines for one person.** To keep six months feasible, the rank sweep on sycophancy is deferred, and each paper stands alone.
> - **The law at scale** may hold on average yet fail item by item. Judge drift could also blur comparisons with earlier data; the frozen anchor set is there to catch it.
> - **The inhibition may fail its gate.** First measures show thin margins over random controls. The reasons test would still run, and the methods result would be published.
> - **Compute estimates are uncertain** by about a factor of 2. Costs are logged run by run.
> - **If a fellowship or a PhD starts** during the grant, I will end the grant early and return unspent funds.

## Funding amount and breakdown

> Mainline, six months: €47,456, with a 10% contingency buffer stated explicitly.
> - Stipend for me: 63%, gross, including income tax and social contributions.
> - GPU compute: 13%, H100 SXM at 3.50 USD an hour.
> - API: 9% (Claude, and the LLM judges).
> - Conference travel: 5%.
> - Software and storage: 1%.
> - Buffer: 9%.
>
> Minimum, four months: €29,163. It covers the behavioural paper and the minimal experiment of the second line. Maximum: €54,606, adding 70B runs on rented GPUs, a human-rated judge subset and a second venue. Total project budget: €47,456. If Anthropic grants API credits, I will lower the API line by the same amount.

**Requested amount (USD):** 53,478. That is the mainline at the ECB rate of 6 October 2026; recompute it on the day you submit.

**Organizational budget:** leave empty.

## Alternatives to funding

> Without this grant, I continue part-time alongside consulting. The behavioural paper comes first; the rest is postponed, and compute is capped at what I can pay myself. If any application below succeeds during the grant, I will tell EA Funds, end the grant early and return unspent funds.
>
> Applications in the last 12 months:
> - Anthropic Fellows Program: applied on 26 April 2026; final stage; the last interview is being rescheduled; nothing received yet; decision expected [[date]].
> - [[OpenAI Safety Fellowship: date, status, amount requested, amount received, decision date]].
> - [[ERA Fellowship, Cambridge: same]].
> - [[SASH: same]].
> - Meta FAIR Paris, PhD position (a job, not a grant): applied September 2026; pending.
> - [[Anthropic External Researcher Access Program, API credits, about 1,000 USD: only if sent]].

## Use for additional funding

> In this order:
> 1. The readable-versus-causal rank sweep on sycophancy: full-length generations, N = 200, a zero-pressure arm and matched random controls.
> 2. A human-rated subset for the judge study.
> 3. 70B runs on rented GPUs, if NDIF cannot host the model.
> 4. The next phases of the evaluation-awareness programme: localization, then replication on Qwen3-8B.
> 5. Up to three more months, if no full-time position has started by June 2027.

## Confidential information

> [Retiré de la copie déposée dans git : ce champ contient des données personnelles. La version complète est hors de git.]
## References

> [Retiré de la copie déposée dans git : les deux références, leurs fonctions et leurs e-mails. La version complète est hors de git.]
## Notes pour Lazar

**Ce qui a été fusionné.**
- **La base est le dossier complet du 7 octobre** : tes informations, les références, le tableau des candidatures, tes choix (rapport public, renvoi à d'autres financeurs, partage réseau).
- **« Raisons ou regard ? » y entre comme troisième papier**, aux mois 3 à 6. Ses résultats rejoignent « Track record » ; son budget rejoint le tableur.
- **Le balayage de rang sur la sycophancy passe en extension**, en tête de « Use for additional funding » : deux lignes de travail en six mois, pour une personne, c'est déjà beaucoup.
- **Le texte est resserré**, car le dossier du 7 octobre dépassait la limite de 10 000 caractères du formulaire. Les réponses font maintenant environ 9 300 caractères, avec les passages à remplir. Garde tes ajouts sous 700 caractères en tout ; le formulaire conseille de 2 000 à 5 000.
  - Description courte : 114 caractères, pour 120 au plus.
  - Résumé : 949 caractères, pour 1 000 au plus.

**Le budget** (`EA_FUNDS_BUDGET_2026-10-07.xlsx`, le modèle d'EA Funds, en euros)

| Scénario | Durée | Montant | En dollars |
|---|---|---|---|
| Minimum | 4 mois | 29 163 € | |
| Central | 6 mois | 47 456 € | 53 478 $ |
| Maximum | 6 mois, avec les extras | 54 606 € | |

- Le taux est celui de la BCE du 6 octobre (1 € = 1,1269 $), dans la cellule B1 de chaque onglet. Mets-le à jour le jour de l'envoi.
- Le GPU est compté partout au même prix : 3,50 $ l'heure de H100 SXM, celui que nous avons payé le 6 octobre (de 2,86 à 4,04 $). Le brouillon du 7 octobre prenait 2,5 € l'heure.
- Les heures de GPU des papiers sycophancy sont déduites de ce brouillon, soit environ 240 heures par mois. À vérifier.
- La rémunération reste celle du brouillon : 5 000 € brut par mois, à confirmer avec un comptable.

**Vérifié dans tes dépôts**
- Le 61 % → 46,5 % (N = 200, p = 0,0019) est dans `TRACEABILITY.md`.
- La troncature à 300 caractères est dans `code/06_multirank_ablation.py`.
- Les deux DOI sont justes : auteurs, revues et années conformes, d'après Crossref.

**À corriger ou à confirmer avant l'envoi**
1. **« all code public »**, dans le résumé du 7 octobre, est retiré. Le README dit lui-même que `code/` documente la méthode sans être le code exact qui a produit `results/`, et que la génération a tourné dans des carnets Colab. Le résumé dit maintenant « Preregistered and audited ».
2. **« 68 % for the full state »** : vérifie que ce chiffre ne vient pas du ρ = 0,684 du README. Ce ρ est une corrélation entre la lecture et la conduite, et peut relever d'un ajustement sur l'entraînement ; ce n'est pas une part du travail causal. S'il vient d'une autre expérience, garde-le.
3. **Les chiffres absents du dépôt public.** Les deux reproductions (119 → 91, 118 → 82), le contrôle à pression nulle (Δ = +0,41), le « 2,09 fois » et le registre de 131 objets n'y figurent pas : le README dit que ces diagnostics ne sont pas dans `results/`. Un évaluateur qui vérifie ne les trouvera pas. Ajoute leurs fichiers au dépôt, ou dis qu'ils sont disponibles sur demande. La version fusionnée n'en garde que le contrôle à pression nulle, sans chiffre.
4. **La ligne Dehaene** : la première instance demandait de la reprendre mot pour mot dans ton CV. Le brouillon du 7 octobre la paraphrasait ; sa place est réservée.
5. **IBM** : c'était un stage. La première instance parlait d'un « poste de recherche », ce qui n'est pas repris.
6. **Les précisions des sondes sur Qwen** (0,93 à 0,99) ne sont plus dans le texte, faute de place. Si tu les remets, vérifie qu'elles sont mesurées sur des données tenues à part. Le README de sycophancy a retiré ses propres précisions de sonde parce qu'elles étaient mesurées sur l'entraînement.
7. **La date limite d'ICML 2027** n'est pas encore publiée. Elle est estimée au 22 janvier 2027, d'après le cycle précédent.

**Choix gardés du brouillon du 7 octobre, à confirmer**
- **Rapport public** : PUBLIC. Le rapport public ne publie que la description courte, et le champ confidentiel demande de garder pour les conseillers la méthode de l'étude, qui sera pré-enregistrée sous embargo. Ma recommandation PRIVATE d'hier ne valait que pour un dossier centré sur l'étude sous embargo.
- **Pas d'urgence ; renvoi à d'autres financeurs et partage réseau** : oui.

**Encore ouvert, d'après les notes du 7 octobre**
1. **Ton statut fiscal** (micro-entreprise ou autre) : fais vérifier le taux réel par un comptable avant de fixer le brut.
2. **EPSA** : si tu gardes une activité pendant la transition, réduis la rémunération au prorata et dis-le.
3. **La date de reprise du travail à plein temps** : elle va dans le champ confidentiel, si tu veux l'y mettre.
4. **Le tableau des candidatures des 12 derniers mois** est obligatoire : pour chacune, le nom, la date, le statut, le montant demandé, le montant reçu et la date de réponse.
5. **Tes dépenses passées en calcul et en API**, pour le « Track record ».
6. **AISTATS** : as-tu déposé l'abstract le 29 septembre ? Le texte vise ICML 2027.
7. **Les références** : confirme les deux e-mails, préviens les personnes, et trouve si possible une référence en sûreté de l'IA. EA Funds les contacte sans te prévenir.

**Données personnelles.** Cette copie est expurgée pour git : le champ confidentiel et les références en sont retirés. La version complète reste hors de git.
