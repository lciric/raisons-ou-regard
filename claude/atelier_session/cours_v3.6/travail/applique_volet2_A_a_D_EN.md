# Insertions appliquées — volet2_A_a_D — EN

### Insertion n°2, après la ligne 517 de la v3.5

> Ancre : The fourth is not a method but a cross-cutting discipline, evaluation statistics: every result requires error bars, sufficient statistical power, and above all detection at a very low false-positive rate, because dangerous events are rare — looking for a needle in a haystack with a detector that is 

> ⚠ **Limits and workarounds**: red-teaming → Part 2, §H (after "In practice — StrongREJECT"); control monitors → Part 2, §G (after "In practice — coup probes") *(v3.6)*

### Insertion n°4, après la ligne 526 de la v3.5

> Ancre : In practice — Auditing Hidden Objectives (Anthropic). Here the goal was methodological: can we audit a model to discover a hidden objective that it does not reveal? Rather than waiting to find such a model in the wild, the authors manufactured one — trained to pursue a concealed objective — then use

> ### ★ Box of 2 October 2026 — Misalignment probes, 1: why a model organism, and the limit of the known case
>
> *Written on 2 October 2026 by the session of the "Reasons or regard?" programme (« Raisons ou regard ? »), in answer to three questions: why do you need a model organism to train activation probes that detect misalignment, J-lens included? How do you train those probes: fine-tuning, or something else? And out of distribution? It is split into three pieces: this one (part 1); the rest, how to train the probes and out of distribution, at the end of the presentation of section C of this Part; the J-lens, summarised in C bis. It extends Part M, M5 (the null and the known case) and Part 6, §8 (out-of-distribution validity of probes). Checked on 2 October against the documents it cites; the corrections are stated at the end of each piece.*
>
> **1. A probe's silence says nothing without a known case.** A silent probe does not separate "there is no intent" from "the probe is blind". On an organism in which you installed the intent yourself, you measure its sensitivity and its false alarms; its silence elsewhere then becomes a bound. It is the calibration of a detector on a known source: without a source, "no event" does not distinguish "no signal" from "detector switched off" (the programme's handover v1.2, §5.2; this is the rule of Part M, M5).
>
> **2. The organism provides the ground truth.** On a natural model, you do not know when it "wants" to misbehave: the label comes from its conduct, judged after the fact. On the organism, you know the installed rule: Hua et al.'s organism (sheet 10; out loud, it is never named) was built in two steps, synthetic documents about a fictional evaluation company and then *expert iteration*, to write Python type annotations in evaluation and not in deployment (sheet 10). So you know which inputs should light the probe up, and which should not. But the organism does not follow its rule to the letter: about 80 to 86% annotations in evaluation, 34% in merely prompted deployment (sheet 10); and the authors note that the model does not reliably tell evaluation from deployment from subtle cues (sheet 10, "Their limits"). The ground truth is the rule and its cues; the label of each input is still checked by conduct.
>
> **3. Reading is not causing, and the causal test also needs a known case.** Your own result shows it: on Llama 3.1 8B Instruct, opinion sycophancy is linearly readable from the residual stream, yet none of the single-direction interventions tried reduced the judged rate (README of `sycophancy-construct-validity`). Two reservations from the same README, to keep: those interventions are reported without numbers, their raw outputs not having been preserved; and the read-out rests on a correlation that may be only training fit. For a probe to be used to intervene, steering along its direction must do more than random directions of the same norm (the specificity null), then more than the controls at matched degradation (the damage) (handover v1.2, §5.2; Part M, M4). This test requires an organism trained to a precise misaligned action, in a precise scenario (handover v1.2, §5.2).
>
> **4. The J-lens has its own blind spot, hence its own known case.** It reads single-token concepts in the workspace; what passes beneath the workspace escapes it, and the authors concede it: "A sufficiently practiced misaligned behavior might do likewise" (sheet 1; taken from the knowledge base, not reread on 1 October). The known case for that blind spot: an organism trained to the action by reflex, on short examples, without reasoning (handover v1.2, §5.2, item 3 of "to catch what passes beneath the surface"). And the J-lens has been shown only on Claude: on an open model, you must first reproduce the swap of a single-token concept, otherwise fall back on a tuned lens declared as an approximation (the lens gate: programme v1.1, part 3, "The workspace lens", and part 8). A warning, unverified: Zeisler reports, on open models, swaps that flip the answer in only 6.3 to 11.1% of cases, against 54 to 70% at Anthropic (prior-art report 5 from the night of 1 to 2 October, read through the tool's summary). Those 54 to 70% match the paper's multi-step reasoning swaps (sheet 1: 54, 70 and 70% for Haiku, Sonnet and Opus 4.5), and the post is about that reasoning: the warning therefore most likely bears on swapping an intermediate variable, not directly on the concept swap the gate requires. The same report mentions a review by Nanda with replications on Qwen 3.6 27B, also read through a summary; sheet 1 treats external replications as unverified.
>
> **The limit of the known case.** It is necessary, not sufficient: an implanted intent may be more salient than a natural one (handover v1.2, §5.2). On the *sleeper agents*, a probe built from generic contrast pairs reaches an AUROC above 99%, but the best of 1,000 random directions already reaches 95.3% (sheet 15): the implanted defection is extremely salient, and the authors say this salience could come from the insertion (sheet 15; Part M, M5). A success on the organism bounds the instrument; it does not prove that it will work on natural misalignment. A partial workaround, already in the course: plant the same behaviour through several recipes, read the probe on a held-out recipe, with a harmless behaviour planted the same ways as a control (this Part, section A, worked case K71); or two organism families, the hidden instruction and the light fine-tune, with an aware-but-honest control (Part 6, §8). Against the gap between implanted and natural itself, no workaround is known; say so.
>
> *Check of 2 October, corrections made in this piece. Item 2: the source text said the organism writes the annotations "when it believes it is evaluated, and not otherwise"; sheet 10 gives about 80 to 86% against 34%, and a two-step construction. Item 3: the README's two reservations were added. Item 4: the lens gate is defined in part 3 of programme v1.1 (and taken up in its part 8), not in its part 4; the Zeisler warning is made more precise. The limit of the known case: the course's workarounds were added.*

### Insertion n°6, après la ligne 526 de la v3.5

> Ancre : In practice — Auditing Hidden Objectives (Anthropic). Here the goal was methodological: can we audit a model to discover a hidden objective that it does not reveal? Rather than waiting to find such a model in the wild, the authors manufactured one — trained to pursue a concealed objective — then use

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

### Insertion n°8, après la ligne 553 de la v3.5

> Ancre : only indicate a threshold that is too strict (M5).

> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); known case → Part M, M5 (end of section) *(v3.6)*

### Insertion n°10, après la ligne 573 de la v3.5

> Ancre : In practice — sandbagging (system cards). On the side of risk to the evaluations themselves, we want to know whether a model strategically underperforms when it knows it is being evaluated (sandbagging). The design is a propensity eval for underperformance: we compare the model's performance on a ta

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

### Insertion n°12, après la ligne 586 de la v3.5

> Ancre : **The controls, and what they rule out.** The version, being assigned, carries the comparison; awareness is not assigned, and what makes the model notice the test (a longer deliberation) could also lower the attempts. The same task in both versions rules out a difference in difficulty: the open requ

> ⚠ *(v3.6)* "The probe would not" assumes a probe that has its known case: a silent probe does not separate "the model does not know it is tested" from "the probe is blind" (handover, §5.2; reading sheets, part B, trap 3), and an in-distribution AUROC proves nothing (reading sheets, part B, trap 1; reading sheet 7). Workaround: validate it first on the evaluation-conditioned organism, the known case for "I am being evaluated", and on held-out cue families (explanation of 2 October, §3).

### Insertion n°14, après la ligne 592 de la v3.5

> Ancre : **The known case.** An organism trained to hide when it is watched must attempt less in the less realistic version; otherwise, a tie might only indicate versions that are too close (M5).

> ⚠ **Limits and workarounds**: known case → Part M, M5 (end of section); activation probes → Part 2, §C (after "In practice — The Geometry of Truth") *(v3.6)*

### Insertion n°16, après la ligne 607 de la v3.5

> Ancre : In practice — The Geometry of Truth (Marks & Tegmark). The authors wanted to know whether a model represents the truth or falsity of a statement linearly — in other words, whether there exists a "truth direction" in its activations. Probing answers directly: they collected the model's activations on

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

### Insertion n°18, après la ligne 609 de la v3.5

> Ancre : In practice — Contrastive Activation Addition (CAA) (Panickssery). The goal was to steer high-level behaviors — sycophancy, corrigibility, refusal — directly at inference, without retraining. The method of steering by contrastive pairs answers this: we build the direction from pairs of examples that

> ### ★ Box of 2 October 2026 — Misalignment probes, 2 and 3: how to train them, and out of distribution
>
> *Continuation of the box whose part 1, why a model organism, is at the end of the presentation of section A of this Part. The experiment that tests out-of-distribution validity is in Part 6, §8; the rule of the null and the known case, in Part M, M5.*
>
> **2 · How to train the probes**
>
> **It is not a fine-tuning of the model.** The model's weights do not move. A probe is a small classifier trained on its frozen activations, at a given layer and position: most often a mean-difference direction over contrastive pairs, possibly followed by a principal component analysis for a rank-k subspace (programme v1.1, part 3); or a logistic regression (Part 5, section II, A; Part 10, no. 27 and no. 30). Careful, the direction that reads best is not necessarily the one that acts: in RepE, the logistic-regression direction gives the highest accuracy, but strengthening or suppressing it barely changes behaviour (Part 10, no. 53); on the "quirky" models, at comparable transfer, the logistic directions are far less causal than the mean difference (Part 10, no. 30).
>
> **The counter-example that matters.** The "fine-tuned lie detectors" of sheet 7 are not probes: they are models fine-tuned with LoRA to answer a self-report question asked about a transcript (sheet 7). Their in-distribution AUROC rises from 0.60 to 0.95 over training, plateaus at 0.70-0.75 from one lie category to another, and they barely beat a simple prompt on new types (sheet 7).
>
> **The steps, as programme v1.1 lays them out (parts 3 and 8), completed by handover v1.2:**
> 1. **The data**: contrastive pairs, the same situation up to one variable, an evaluation or deployment cue, a principle that applies or not (programme v1.1, part 3); or generations of the model itself (this Part, section C, above; the shift that matters runs from synthetic data to data generated by the model: Part 6, §8). Those generations are labelled by their conduct, programmed checks of the environment and a sealed judge (handover v1.2, §5.1), never by the probe: the label depends on no internal reading (handover v1.2, §5.2).
> 2. **Disjoint cue sets**, against circularity: one to extract the representation and build the organism, one to validate the probe, one to frame the evaluations, one for the fresh probe after training (programme v1.1, part 3).
> 3. **The layer** is chosen by AUROC on the validation set (programme v1.1, part 3), never on the test set.
> 4. **Two reading positions**: at the first token of the response, before any written reason; and at the action token, with neutral reasons of the same length prefilled in place of the real ones. Otherwise the probe may be reading the text, not a representation (programme v1.1, parts 3 and 8).
> 5. **One probe per training arm, and a fresh probe after training.** Training changes the representations: a probe calibrated on one arm would read differently in another, and that measurement bias would be confounded with the effect sought (handover v1.2, §5.2). That is why the probes remain a separate measure, never in the main label (handover v1.2, §5.2).
>
> **3 · Out of distribution: this is where it all plays out**
>
> - **An in-distribution AUROC proves nothing.** It is the first of the seven reading traps (priority readings, part B; sheet 7). The number that matters is the gap between the in-distribution AUROC and the AUROC on held-out types (sheet 7, "To remember").
> - **Hold out whole families, never paraphrases**: the cross-validation by lie type of sheet 7, the separation by family of the programme (programme v1.1, part 3); and held-out formats, from a single turn to multi-turn agentic with tools, the farthest distance being the main criterion (programme v1.1, part 3).
> - **After training, a fresh probe.** After RL, fresh out-of-domain probes degrade, whereas a fresh in-domain probe stays near perfect (*The Obfuscation Atlas*, prior-art report 3, text read by the agent in a targeted way): according to that report, the concept has not disappeared, it has left the general direction.
> - **An "evaluation versus deployment" probe**, on Llama-3.1-8B-Instruct, under RL with verifiable rewards, would keep its overall score but flip on borderline cases, and retraining it recovers almost nothing (prior-art report 4: a workshop paper, abstract only, to be checked).
> - **For the organism itself**, the known case is validated on held-out phrasings, not on the training ones (the gate of the planted-concept organism: programme v1.1, parts 3 and 4).
>
> **What to take from it.** Probes have three distinct known cases: the evaluation-conditioned organism for "I am being evaluated" (programme v1.1, part 4, instrument validation phase), the planted-concept organism for reason concepts (programme v1.1, parts 3 and 4), and a reflex organism for the J-lens's blind spot (handover v1.2, §5.2); the lens itself has its own in addition, the swap of a single-token concept reproduced on the open model (programme v1.1, part 3; this Part, C bis). They are judged out of distribution, arm by arm, and remain a secondary, exploratory measure as long as they are not preregistered (handover v1.2, §5.2).
>
> *Check of 2 October, corrections made in this piece. Part 2: "regularized logistic regression" had a source in none of the documents; it now says "logistic regression", with its sources and the caveat from Part 10. Sheet 7: 0.60 → 0.95 is a progression during training, and the detector answers a self-report question. Step 1: labelling by programmed checks and a sealed judge comes from the handover (§5.1 and §5.2), not from parts 3 and 8 of the programme. Step 4: the programme reads at both positions, not at one or the other. Step 5: the handover says "would read", in the conditional. Part 3: the RL of report 4 is RL with verifiable rewards, on Llama-3.1-8B-Instruct. "What to take from it": the lens's own known case was added.*

### Insertion n°20, après la ligne 609 de la v3.5

> Ancre : In practice — Contrastive Activation Addition (CAA) (Panickssery). The goal was to steer high-level behaviors — sycophancy, corrigibility, refusal — directly at inference, without retraining. The method of steering by contrastive pairs answers this: we build the direction from pairs of examples that

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

### Insertion n°22, après la ligne 619 de la v3.5

> Ancre : cleanest vector, or smaller: a single strength does not separate them, and the next control would be a dose-response curve.

> ⚠ *(v3.6)* "Negligible degradation" is the system card's own judgement, and such judgements contradict each other across cards: at the same strength, Mythos Preview deems degeneracy negligible while Opus 4.8 sees every direction degrade the output (reading sheets, part B; reading sheet 2). Workaround: measure degradation in your own setup, never borrow it from another — damage is measured, not assumed (course, Part M, M4).

### Insertion n°24, après la ligne 627 de la v3.5

> Ancre : cannot act rules out a correlate: an effect there as large as where the concept acts would betray the correlate.

> ⚠ **Limits and workarounds**: random controls → Part M, M4 (after "The matched-norm random direction"); matched degradation and dose-response → Part M, M4 (after "Dose-response") *(v3.6)*

### Insertion n°26, après la ligne 651 de la v3.5

> Ancre : **Three results to know by their numbers** — to understand them; out loud, you give their shape, not the numbers (Part M, M8). (1) *The swap.* In the residual stream, the J-space components of two concept vectors are swapped: the target concept appears among the model's top five outputs in 59% of tr

> ⚠ *(v3.6)* This ablation is compared only with no ablation, without a control at matched degradation, and the drop in verbalization does not by itself show that evaluation awareness was removed (course, Part 2, C bis, K72; reading sheet 1; counter-reading of the sheets). Workaround: an arm of neutral lens directions at matched degradation, a behavioural criterion and a latent probe (course, Part 2, C bis, K72; programme, part 8).

### Insertion n°28, après la ligne 665 de la v3.5

> Ancre : 0.93-0.997 are those of the concept pairs on Qwen2.5-7B, another project.

> ⚠ *(v3.6)* The rank-one failures are nulls, reported without numbers since their raw outputs were not preserved, and a null counts only with a known case at the same setting, which the repository does not report; the rate is scored by a judge model with moderate inter-judge agreement and no human-rated subset (course, Part M, M5; repository README). Workaround: a country vector as the known case and a rank sweep within one experiment, on nested subspaces (course, Part 2, §C, K47; course, Part 6, §6); a sealed judge and a stratified human audit (programme, part 3).

### Insertion n°30, après la ligne 665 de la v3.5

> Ancre : 0.93-0.997 are those of the concept pairs on Qwen2.5-7B, another project.

> ⚠ **Limits and workarounds**: ablation and projection → Part 2, §D (after "The method"); random controls → Part M, M4 (after "The matched-norm random direction"); matched degradation and dose-response → Part M, M4 (after "Dose-response"); patching → Part 10, Patchscopes sheet; LLM judges → Part 6, §2 (after "The displacement law") *(v3.6)*

### Insertion n°32, après la ligne 675 de la v3.5

> Ancre : according to the predictor measured first. **What remains to say out loud**: the lens is approximate and incomplete, the authors say so; that is where the doubt lies.

> ### ★ Box of 2 October 2026 — The J-lens as a misalignment probe: its blind spot, and its known cases
>
> *Summary of item 4 of part 1 of the box; the full text is at the end of the presentation of section A of this Part, the continuation (training the probes, out of distribution) at the end of that of section C.*
>
> - **What it reads, what it misses.** The J-lens reads single-token concepts in the workspace before the action, such as "copy", "delete", "lie" (handover v1.2, §5.2); what passes beneath the workspace escapes it, and the authors concede it: "A sufficiently practiced misaligned behavior might do likewise" (sheet 1; taken from the knowledge base, not reread on 1 October). A silence of the lens therefore does not separate "no intent" from "intent beneath the workspace".
> - **The known case for that blind spot**: an organism trained to the action by reflex, on short examples, without reasoning (handover v1.2, §5.2). So as not to depend on a reading known to be partial, the same handover adds: a label that depends on no internal reading; three probes, on the whole stream, on its workspace share and on the complement; propensity measured without internal reading, by resampling from each decision point; a crosscoder between the base and each arm (handover v1.2, §5.2).
> - **The known case of the lens itself.** It has been shown only on Claude: on an open model, first reproduce the swap of a single-token concept (the lens gate: programme v1.1, part 3; it is also the known case of "The test, as it is said", above), otherwise a tuned lens declared as an approximation. Unverified warning: Zeisler reports much weaker swaps on open models (prior-art report 5, read through a summary; the detail and its reservation are in part 1).
> - **After any training**, recompute the lens, because it depends on the weights (this C bis, "The test, as it is said").

### Insertion n°34, après la ligne 675 de la v3.5

> Ancre : according to the predictor measured first. **What remains to say out loud**: the lens is approximate and incomplete, the authors say so; that is where the doubt lies.

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

### Insertion n°36, après la ligne 694 de la v3.5

> Ancre : of the concept, read on the tokens of those directions at all positions, must first drop in the real framing: otherwise, the model would still read a test there.

> ⚠ **Limits and workarounds**: ablation and projection → Part 2, §D (after "The method"); matched degradation and dose-response → Part M, M4 (after "Dose-response"); chain of thought as a monitor → Part 11, answer 43 *(v3.6)*

### Insertion n°38, après la ligne 701 de la v3.5

> Ancre : awareness down, as in the paper, and more than the neutral arm does; and the runs must be enough to see an excess as small as in the paper.

> ⚠ *(v3.6)* This known case checks through verbalization alone that the ablation reaches the signal; yet an inhibition can silence verbalization without touching the latent representation (programme, part 8; reading sheet 1). Workaround: also check the reach with a latent probe of evaluation awareness, since verbalization is never proof of inhibition (programme, part 8).

### Insertion n°40, après la ligne 718 de la v3.5

> Ancre : The method. Where probing asks "is the concept present as a direction?", mechanistic interpretability asks "what is the actual computation — which components compute what, and how do they connect?". Its specific obstacle is superposition: a single neuron or a single direction mixes several concepts 

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

### Insertion n°42, après la ligne 720 de la v3.5

> Ancre : In practice — Towards / Scaling Monosemanticity (Anthropic, Interpretability team). The goal was to turn activations that are unreadable, because of superposition, into interpretable units. The SAE answers this directly: trained on Claude's activations, it extracted thousands of features from them, 

> ⚠ *(v3.6)* That a forced feature pushes its concept does not by itself prove a real unit of computation: arbitrary vectors move behaviour too, plausible explanations exist for arbitrary directions, and the dictionary leaves a reconstruction error (reading sheet 2; reading sheet 5; course, Part 4, Monosemanticity). Workaround: steer the features one at a time against random directions at matched damage, on a task with known geometry, with new seeds, and validate by prediction, better than baselines (course, Part 2, §D, K64; reading sheet 5).

### Insertion n°44, après la ligne 722 de la v3.5

> Ancre : In practice — On the Biology of a Large Language Model / Circuit Tracing (Anthropic). Here the goal was to see reasoning at work, not only concepts. The method of attribution graphs answers this: by tracing the flow of features across layers, the authors were able to map how the model performs, for 

> ⚠ *(v3.6)* The graphs are partial and approximate, explain only a fraction of the computation, and readable circuits can be unfaithful: the graph is not the mechanism (course, Part 4, Circuit Tracing; course, Part 2, §D, K64; course, Part 7, F·9). Workaround: treat it as a hypothesis that must predict a counterfactual, and compare its interventions, at matched damage, with random directions (course, Part 7, F·9; course, Part 2, §D, K64).

### Insertion n°46, après la ligne 722 de la v3.5

> Ancre : In practice — On the Biology of a Large Language Model / Circuit Tracing (Anthropic). Here the goal was to see reasoning at work, not only concepts. The method of attribution graphs answers this: by tracing the flow of features across layers, the authors were able to map how the model performs, for 

> ⚠ **Limits and workarounds**: dictionaries and SAEs → Part 4, Towards then Scaling Monosemanticity; attribution graphs → Part 4, Circuit Tracing *(v3.6)*

### Insertion n°48, après la ligne 738 de la v3.5

> Ancre : up. New seeds rule out a chance winner, which would change from one seed to another.

> ⚠ **Limits and workarounds**: dictionaries and SAEs → Part 4, Towards then Scaling Monosemanticity; steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition"); matched degradation and dose-response → Part M, M4 (after "Dose-response") *(v3.6)*

### Insertion n°50, après la ligne 754 de la v3.5

> Ancre : produces equally well, while random directions missed it, I'd drop the bet."*

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
