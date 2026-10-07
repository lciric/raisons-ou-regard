# Insertions appliquées — volet6 — EN

### Insertion n°2, après la ligne 1583 de la v3.5

> Ancre : **The displacement law (P1), absent from the course** — "the law" in your dossier, never out loud: "the displacement I measured". It is today your most solid result; its functional form was published in June, with a bias fitted per model and per subject, and your part is the target that moves with t

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

### Insertion n°4, après la ligne 1583 de la v3.5

> Ancre : **The displacement law (P1), absent from the course** — "the law" in your dossier, never out loud: "the displacement I measured". It is today your most solid result; its functional form was published in June, with a bias fitted per model and per subject, and your part is the target that moves with t

> ⚠ *(v3.6)* That the destination "can be read in the activations" says it is readable there, not that the model uses it: the direction your probe reads does under 1% of the causal work (course, Part 6, §2); and the passage does not say whether this R² comes from items excluded from the fit, whereas your repository's probe metrics were training fit, and its ρ may be too (repository README). Workaround: score items excluded from the fit and extract on a disjoint set (repository README); to conclude that the model uses it, the causal test — do more than matched-norm random directions (the specificity null), then more than controls at matched degradation (the damage) (handover, §5.2; course, Part M, M4).

### Insertion n°6, après la ligne 1585 de la v3.5

> Ancre : **The causal result (P2), on Llama-3.1-8B.** Rank 3: 61 → 46% on the judged rate, N = 200, paired McNemar, p ≈ 0.002. The zero-pressure arm — same ablation, without pressure — also moves, Δ +0.41, p 0.0006, interaction p 0.55: the subspace softens negative verdicts, with or without pressure; **it do

> ⚠ *(v3.6)* "At matched doses" is not "at matched degradation": at equal dose, a competing direction and yours need not damage the model equally, so these two selectivity ratios are not read at equal damage; and patching the full state at the same sites is a ceiling, not an explanation (course, Part M, M4; programme, parts 7 and 8). Workaround: redo the comparison of the two named directions at matched degradation, as curves of effect against degradation, comparing only at settings a control can match, and saying so (programme, part 7).

### Insertion n°8, après la ligne 1587 de la v3.5

> Ancre : **Rank 1.** "Six methods" is no longer traced in the dossier; you say **"several rank-one methods — contrastive activation addition, directional steering and ablation, SAE feature clamping, fine-tuning with an auxiliary loss"**. The preregistered re-test: rank 1 = 27/50, **+4 points**, p 0.81 — the 

> ⚠ *(v3.6)* This rank-one null is stated with its power, not with its known case: without a concept that gives way at rank one in the same apparatus, at the same setting, it does not separate "distributed concept" from "apparatus blind at this setting" (reading sheet 7; course, Part M, M5); the other rank-one methods are reported without numbers, their raw outputs not having been preserved, and the failure of SAE feature clamping does not separate "features absent from the dictionary" from "dictionary too lossy" (repository README). Workaround: a known case at the same setting — a country vector, which swaps in the workspace paper — and a rank sweep within one experiment, on nested subspaces (course, Part 2, §C, K47; course, Part 6, §6); for the SAE, none known, say so; and state a bound, never an absence (repository README; course, Part M, M5).

### Insertion n°10, après la ligne 1589 de la v3.5

> Ancre : **The replication.** Under its original protocol, yes (119 → 91, p 0.002; 118 → 82, p 0.00003; random controls p 0.83 and 0.16 — which random it is, the dossier will say; none of them rules out damage: Part M, M4). On fresh generations, no: 51.3 → 56.0, p 0.34; 58 → 58, p 1.0; power > 0.95 — a **gov

> ⚠ *(v3.6)* High power does not replace a known case: this null on fresh generations is stated as a bound, with its budget and power, not as the absence of any effect (course, Part M, M5). Workaround: validate the same protocol — fresh seed-matched generations, the whole answer judged and kept as full text — on a known case, at the same setting and threshold, before reading its silence (course, Part M, M5; reading sheet 7; course, Part 6, §6; repository README).

### Insertion n°12, après la ligne 1591 de la v3.5

> Ancre : **The preregistration.** The rank re-tests are preregistered, and the zero-pressure arm too according to your dossier — yet the P4 document marks the softening without pressure "exploratory: prereg D29 reconstructed": to be checked; the canonical rank-3 resolution has lost and reconstructed original

> ⚠ **Limits and workarounds**: ablation and projection → Part 2, §D (after "The method"); patching → Part 10, Patchscopes sheet; random controls → Part M, M4 (after "The matched-norm random direction"); matched degradation and dose-response → Part M, M4 (after "Dose-response"); activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition"); dictionaries and SAEs → Part 4, Towards then Scaling Monosemanticity; known case → Part M, M5 (end of section) *(v3.6)*

### Insertion n°14, après la ligne 1595 de la v3.5

> Ancre : The course talks about a "baseline" (Part 1, §I.4). Your dossier has three, and confusing them cost a whole day of corrections: the **competing structured directions** (PR-A: A2 = 0.90, A3 = 0.60); the **norm-matched random** (D32 — absent from the P2 record, according to the P4 document: do not cit

> ⚠ *(v3.6)* None of these three controls rules out damage: the random one, norm-matched or covariance-matched, is only the specificity null, and the competing directions are compared at matched doses, not at equal degradation (course, Part M, M4; programme, part 7; course, Part 6, §2). Workaround: a fourth control, at matched degradation — several families of controls at the same rank, including at least twenty random subspaces, as curves of effect against degradation, reported against their median and 95th percentile (programme, parts 3 and 7).

### Insertion n°16, après la ligne 1595 de la v3.5

> Ancre : The course talks about a "baseline" (Part 1, §I.4). Your dossier has three, and confusing them cost a whole day of corrections: the **competing structured directions** (PR-A: A2 = 0.90, A3 = 0.60); the **norm-matched random** (D32 — absent from the P2 record, according to the P4 document: do not cit

> ⚠ **Limits and workarounds**: random controls → Part M, M4 (after "The matched-norm random direction"); matched degradation and dose-response → Part M, M4 (after "Dose-response") *(v3.6)*

### Insertion n°18, après la ligne 1607 de la v3.5

> Ancre : **Control and monitors**: *Diffuse AI Control on Fuzzy Tasks* (Terekhov, with Hebbar and Benton — the red/blue game on fuzzy tasks, black-box) [F·22]; *SLEIGHT-Bench* (Najt & Toft — the blind spots of monitors: 20 attacks out of 40 never caught) [F·23]; *Strengthening Red Teams* (Loughridge — SHADE-

> ⚠ *(v3.6)* Ryd's 91/85/94% holds, by the authors' written limit, only if training is indistinguishable from deployment: a model that tells them apart escapes (course, Part 7, F·26). Workaround: none known; say so.

### Insertion n°20, après la ligne 1609 de la v3.5

> Ancre : **Auditing and introspection**: *AuditBench* (Sheshadri — 56 models, 14 categories) [F·27]; *Introspection Adapters* (Yang) and *Mechanisms of Introspective Awareness* (Macar & Yang) [F·28]; *Fine-Tuned Lie Detectors Failed to Generalize* (Hopkins — AUROC 0.95 in-distribution, 0.70-0.75 outside) [F·

> ⚠ *(v3.6)* CHIVE's null is measured read-only, with labels that go through an LLM classifier not validated against humans (course, Part 7, F·30); and for introspection adapters, report or plausible reconstruction remains open (course, Part 7, F·28). Workaround: for a reading tool, beat the black box on edits that dissociate surface features from the internal variable, and bound label error with a human audit (reading sheet 4; programme, part 3); for a self-report, modify the internal state against a random direction at matched degradation, and see whether the report follows (reading sheet 11; course, Part 7, F·28).

### Insertion n°22, après la ligne 1611 de la v3.5

> Ancre : **Traits, generalization, training**: *Persona Vectors* (Chen & Arditi) [F·31]; *Subliminal Learning* (Cloud & Le) [F·32]; *Inoculation Prompting* (Wichers & Ebtekar) [F·33]; *Model Spec Midtraining* (Li & Wichers — 68 → 5%) [F·34]; *Poisoning Fine-tuning Datasets of Constitutional Classifiers* (Bow

> ⚠ *(v3.6)* Two of these results have a narrow reach: persona vectors assume the trait is named in advance, and the shift-to-trait link there is only correlational (reading sheet 8); selective gradient masking is shown only on small models (course, Part 2, §I, JB10). Workaround: for a vector's causality, the matched-degradation test (course, Part M, M4); for supervised extraction and for scale, none known; say so.

### Insertion n°24, après la ligne 1613 de la v3.5

> Ancre : **Agents and the automation of research**: *Agentic Misalignment* (Lynch — 96% blackmail in Opus 4) [F·38]; *AI Organizations* (Shen — more effective, less aligned) [F·39]; *Automated Weak-to-Strong Researcher* (Wen) and *Automated Researchers Can Mitigate Well-Characterized Alignment Failures* (Che

> ⚠ *(v3.6)* The 96% comes from a deliberate stress test, where the harmful action is the only path, and the authors know of no instance in real deployments; Model Spec Midtraining's 68 → 5% is measured on the same evaluation (course, Part 7, F·38); and a model can notice the test and hold back (reading sheet 13). Workaround: two versions of an environment, randomly assigned, differing only in realism cues scored by a discriminator, with an organism trained to hide as the known case (course, Part 2, §B, K63); against a honeypot the model reads as fake, none known; say so (reading sheet 3).

### Insertion n°26, après la ligne 1613 de la v3.5

> Ancre : **Agents and the automation of research**: *Agentic Misalignment* (Lynch — 96% blackmail in Opus 4) [F·38]; *AI Organizations* (Shen — more effective, less aligned) [F·39]; *Automated Weak-to-Strong Researcher* (Wen) and *Automated Researchers Can Mitigate Well-Characterized Alignment Failures* (Che

> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after "In practice — coup probes"); red-teaming → Part 2, §H (after "In practice — StrongREJECT"); behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging"); model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives"); self-report and introspection → Part 5, Section II, A, Topic 13; fine-tuned detectors → Part 7, F·29; activation oracles → Part 10, LatentQA sheet; natural-language autoencoders → Part 4, The recent wave on model cognition; dictionaries and SAEs → Part 4, Towards then Scaling Monosemanticity; steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition"); unlearning and re-elicitation → Part 2, §I (after "In practice — unlearning put to the test"); weak-to-strong generalization → Part 2, §F (after "In practice — automation"); LLM judges → Part 6, §2 (after "The displacement law") *(v3.6)*

### Insertion n°28, après la ligne 1617 de la v3.5

> Ancre : Absent from the course: white-box control of diffuse threats — sabotage spread over many innocuous actions, and over many agents that share their weights. The idea: internal evidence adds up where external evidence gets diluted — sequential aggregation of probe scores along a trajectory, and across 

> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after "In practice — coup probes"); J-lens and workspace → Part 2, C bis (after "The test, as it is said"); ablation and projection → Part 2, §D (after "The method"); activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); random controls → Part M, M4 (after "The matched-norm random direction"); matched degradation and dose-response → Part M, M4 (after "Dose-response"); patching → Part 10, Patchscopes sheet *(v3.6)*

### Insertion n°30, après la ligne 1626 de la v3.5

> Ancre : none of the causal work.

> ⚠ *(v3.6)* The Jacobian does not exempt the lens from the causal test: it captures the workspace "only approximately and incompletely", for single-token concepts, presence there is not cause — language is present on four tasks, causal on two —, and it has been shown only on Claude (reading sheet 1). Workaround: the lens gate — first reproduce on Llama the swap of a single-token concept, otherwise a tuned lens declared as an approximation, and the thesis is not tested in the paper's sense (programme, parts 3 and 8); an unverified report also finds much weaker swaps on open models (prior-art report 5 of 2 October — report, read through a summary).

### Insertion n°32, après la ligne 1678 de la v3.5

> Ancre : In Part 1, question Q2 ("the most important problem") gains your angle: judge metrology is an instance of the ground-truth problem. In Part 2, family C (probes and steering) gains the result that puts it in perspective: reading is not controlling, less than 1% of the causal work. In Part 3, the six 

> ⚠ *(v3.6)* This "less than 1%" comes from a single model, Llama 3.1 8B Instruct, and from opinion sycophancy alone, single-turn (repository README): it puts probes and steering (Part 2, §C) in perspective on this case, not in general. Workaround: the same partition on other concepts, then on a second model (course, Part 6, §6).

### Insertion n°34, après la ligne 1757 de la v3.5

> Ancre : already in distribution.

> ⚠ *(v3.6)* Hopkins and Khullar's labels go through a GPT-5 judge, and about 25% were revised at the cleaning pass (reading sheet 7). Workaround: say "revised", not "flipped", and keep as the measure the gap between in-distribution AUROC and AUROC on held-out types (reading sheet 7); in your own setup, bound judge error with a stratified human audit (programme, part 3).

### Insertion n°36, après la ligne 1771 de la v3.5

> Ancre : outside the organisms, **and you know it before deploying it**.

> ⚠ *(v3.6)* The probe's silence on family 2, the light fine-tune, points to "the trace of the instruction" only if that family does carry the intent: the fine-tuned implant can fail (course, Part 2, §E, K52), and the evaluation-conditioned organism of reading sheet 10 follows its rule only in part (reading sheet 10). Workaround: check each copy by its behaviour (course, Part 2, §A, K71), label it by programmed checks and a sealed judge, never by the probe (handover, §5.1 and §5.2), and read a silence only once the probe's sensitivity has been measured on an organism in which you installed the intent yourself: it then becomes a bound (handover, §5.2).

### Insertion n°38, après la ligne 1782 de la v3.5

> Ancre : concluded. It is among the former — a prediction, to be said as such — that the probes that generalise worst should be found.

> ⚠ *(v3.6)* An effect carried by the remainder alone may also come from what the lens misses — it captures the workspace "only approximately and incompletely", and for single-token concepts (reading sheet 1) —, and the lens depends on the weights, while family 2 is fine-tuned, unlike family 1 (course, Part 2, C bis; course, Part 6, §8). Workaround: recompute the lens on each fine-tuned organism, and read the concept on a token set or through the appendix's multi-token extension, saying which (course, Part 2, C bis; programme, part 3).

### Insertion n°40, après la ligne 1789 de la v3.5

> Ancre : mechanism: two organism families, and an aware-but-honest control.*"

> ### ★ Box of 2 October 2026 — Cross-reference: training misalignment probes, and judging them out of distribution
>
> The box of 2 October takes up this section from the practical side: why a model organism, and why its success bounds the instrument without proving the natural case (Part 2, end of the presentation of section A); how to train a probe without touching the weights, and judge it out of distribution, on whole held-out families and with a fresh probe after any training (Part 2, end of the presentation of section C); the J-lens's blind spot and its known cases (Part 2, C bis). The two organism families and the aware-but-honest control of this section are given there as a partial workaround for the salience of an implanted behaviour.

### Insertion n°42, après la ligne 1789 de la v3.5

> Ancre : mechanism: two organism families, and an aware-but-honest control.*"

> ⚠ *(v3.6)* "One probe per layer" forces a choice of layer, and "fires" assumes a threshold: chosen on the test data, they contaminate it (course, Part 2, C bis; repository README). Workaround: choose the layer by AUROC on a validation set, never on the test set, with disjoint cue sets, and fix the threshold in advance, the same one at which the known case was validated (programme, part 3; course, Part M, M5; reading sheet 7).

### Insertion n°44, après la ligne 1789 de la v3.5

> Ancre : mechanism: two organism families, and an aware-but-honest control.*"

> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); fine-tuned detectors → Part 7, F·29; model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives"); known case → Part M, M5 (end of section); J-lens and workspace → Part 2, C bis (after "The test, as it is said"); held-out set → Part M, M4 (after "The held-out set"); patching → Part 10, Patchscopes sheet *(v3.6)*
