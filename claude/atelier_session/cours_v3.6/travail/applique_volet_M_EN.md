# Insertions appliquées — volet_M — EN

### Insertion n°2, après la ligne 334 de la v3.5

> Ancre : **The matched-norm random direction.** You add or remove a randomly drawn direction, of the same norm as the direction under study, at the same place. It rules out only one reading: that any push of that size produces the same effect. Two outcomes: the random direction moves the targeted behavior as

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

### Insertion n°4, après la ligne 338 de la v3.5

> Ancre : **Dose-response.** You vary the strength in the concept arm and in the random arm, and for each one you plot the targeted effect against the measured damage: the curve of the effect as a function of damage. Two outcomes: at equal damage, the concept arm's curve runs above (specific), or the two curv

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

### Insertion n°6, après la ligne 360 de la v3.5

> Ancre : is absolute: nothing is trained, calibrated or chosen on the held-out set.

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

### Insertion n°8, après la ligne 363 de la v3.5

> Ancre : number.

> ⚠ **Limits and workarounds**: activation probes, including contrastive pairs → Part 2, §C (after "In practice — The Geometry of Truth"); steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition"); ablation and projection → Part 2, §D (after "The method"); safety classifiers, including the clean twin → Part 2, §H (end of worked case G1); unlearning and re-elicitation, including the never-trained reference → Part 2, §I (after "In practice — unlearning put to the test"); behavioural evaluations and honeypots, including the realistic reference arm → Part 2, §B (after "In practice — sandbagging"); LLM judges, including blind scoring → Part 6, §2 (after "The displacement law") *(v3.6)*

### Insertion n°10, après la ligne 377 de la v3.5

> Ancre : - An answer proposed, against poisoning, a canary set — "inputs whose right behaviour I know", replayed after each retraining —, then dismissed red-team examination: "black-box red teaming missed the backdoor. So a red-team pass alone proves little." But a backdoor stays silent without its trigger, 

> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives"); red-teaming → Part 2, §H (after "In practice — StrongREJECT"); safety classifiers, including the canary set → Part 2, §H (end of worked case G1); unlearning and re-elicitation → Part 2, §I (after "In practice — unlearning put to the test") *(v3.6)*

### Insertion n°12, après la ligne 379 de la v3.5

> Ancre : **The right use of a null: a bound, with its budget.** You do not certify an absence; you bound it. "Not elicitable at this budget", "no backdoor from these trigger families at this detection power" — never "removed", never "backdoor-free" (rehearsed answers Q32 and Q115 in the KB). And power matter

> ⚠ *(v3.6)* This governed null is a rate judged by a judge model, and your repository says so: agreement between judges is moderate, and no human-rated subset bounds the judge's error *(source: repository README)*. Workaround: a sealed judge and a human audit of stratified items, with the agreement reported, which bounds that error *(source: programme, part 3)*; see the box "LLM judges", Part 6, §2.

### Insertion n°15, après la ligne 381 de la v3.5

> Ancre : **What a known case proves, and what it does not.** Anthropic's defection probes on the sleeper agents were built from generic contrast pairs, without knowing anything about the trigger or the dangerous behavior — that is their strength. Their limit, stated by the authors: the salience of the featur

> ### ★ Box of 2 October 2026 — Cross-reference: the known case of a misalignment probe
>
> The rule of this section, applied to misalignment probes and to the J-lens, is developed in the box of 2 October: why a model organism, and the limit of the known case, with the salience of an implanted defection (Part 2, end of the presentation of section A; sheet 15); the three distinct known cases of probes, and their out-of-distribution validation (Part 2, end of the presentation of section C); the known case of the J-lens's blind spot, an organism trained to the action by reflex (Part 2, C bis).

### Insertion n°16, après la ligne 381 de la v3.5

> Ancre : **What a known case proves, and what it does not.** Anthropic's defection probes on the sleeper agents were built from generic contrast pairs, without knowing anything about the trigger or the dangerous behavior — that is their strength. Their limit, stated by the authors: the salience of the featur

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

### Insertion n°19, après la ligne 430 de la v3.5

> Ancre : - **Your own results**: only those of the MY OWN RESULTS block of the KB, with its reservations, said this way: the rank-three effect did not come back on fresh generations; the original texts were truncated at storage, and this truncation "would explain" that null — in the conditional, because it i

> ⚠ *(v3.6)* That probes "separate" the states does not say they generalize: an in-distribution separation proves nothing; what is measured is the gap with the separation on held-out types *(source: reading sheets, part B, trap 1; reading sheet 7)*. Workaround: hold out whole families, never paraphrases, and formats, from a single turn to multi-turn agentic; and, to intervene, the causal test — random directions of the same norm, which are only the specificity null, then controls at matched degradation, which alone rule out damage *(source: explanation of 2 October, §3; programme, part 3; handover, §5.2)*.

### Insertion n°20, après la ligne 430 de la v3.5

> Ancre : - **Your own results**: only those of the MY OWN RESULTS block of the KB, with its reservations, said this way: the rank-three effect did not come back on fresh generations; the original texts were truncated at storage, and this truncation "would explain" that null — in the conditional, because it i

> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition"); ablation and projection → Part 2, §D (after "The method"); random controls → Part M, M4 (after "The matched-norm random direction"); LLM judges → Part 6, §2 (after "The displacement law") *(v3.6)*

### Insertion n°22, après la ligne 438 de la v3.5

> Ancre : **The standard move.** Before: "the usual move is refusals, but a red team finds a jailbreak phrasing". After: the filter, with what "Anthropic's constitutional-classifiers paper" found — no universal jailbreak in its hunt (M1, beat 3) —, then the reason the filter is not enough, said as a possibili

> ⚠ *(v3.6)* "No universal jailbreak in its hunt" is the null of a red-teaming effort: a bound at its budget, not an absence, and a hunt counts jailbreaks, not what the filter withholds from the attacker *(source: course, Part M, M5 and M7; course, Part 2, §H, G1)*. Workaround: say it with its scope, "in its hunt", no stronger, and judge a filter also by differential harm, as this case's experiment does *(source: course, Part M, M10, item 12; course, Part 2, §H, G1)*.

### Insertion n°24, après la ligne 454 de la v3.5

> Ancre : What this case shows: the first rewrite, done quickly, itself carried eight proven errors, three of them introduced by the rewrite; the second carried two; the third corrected them, but planted the poison in the raw data itself; the fourth removed the questions to the interviewer (D-728); two audits

> ⚠ **Limits and workarounds**: red-teaming → Part 2, §H (after "In practice — StrongREJECT"); safety classifiers → Part 2, §H (end of worked case G1); unlearning and re-elicitation → Part 2, §I (after "In practice — unlearning put to the test") *(v3.6)*

### Insertion n°26, après la ligne 475 de la v3.5

> Ancre : loud?

> ⚠ **Limits and workarounds**: random controls → Part M, M4 (after "The matched-norm random direction"); matched degradation and dose-response → Part M, M4 (after "Dose-response"); held-out set → Part M, M4 (after "The held-out set"); known case → Part M, M5 (end of section) *(v3.6)*
