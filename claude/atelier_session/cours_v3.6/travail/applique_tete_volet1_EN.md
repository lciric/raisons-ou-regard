# Insertions appliquées — tete_volet1 — EN

### Insertion n°2, après la ligne 21 de la v3.5

> Ancre : # ALIGNMENT COURSE — MERGED VERSION v3.5 — September 27, 2026

> **v3.6 — 2 October 2026: what is added** *(v3.6)*
>
> No text of v3.5 is removed or changed: things are only added, and every addition carries the mark *(v3.6)*. Two additions.
>
> - ★ **The box of 2 October 2026 on misalignment probes** — why a model organism is needed, J-lens included; how to train the probes; out of distribution — is in Part 2, in three pieces: part 1 at the end of the presentation of section A (after "In practice — Auditing Hidden Objectives", before the worked case K71); parts 2 and 3 at the end of that of section C (after "In practice — Contrastive Activation Addition (CAA)", before the worked case K47); the J-lens in C bis (after "The test, as it is said", before the worked case K72). Cross-references lead to it from Part M, M5, and Part 6, §8.
> - ⚠ **The limits of each instrument, and how to work around them**: one "Limits and workarounds" box per instrument, at its home (index below); elsewhere, a one-line cross-reference to that box, and a spot warning wherever a passage reports a result without stating the limit of the instrument that produced it. When no workaround is known, the box says so. The rule, everywhere: a matched-norm random direction is only the specificity null; damage is ruled out only at matched degradation; an instrument's null counts only with its known case (course, Part M, M4 and M5).
>
> **Where the "Limits and workarounds" boxes are**, Part by Part:
>
> ⚠ **Limits and workarounds**: random controls → Part M, M4 (after "The matched-norm random direction"); matched degradation and dose-response → Part M, M4 (after "Dose-response"); held-out set → Part M, M4 (after "The held-out set"); known case → Part M, M5 (end of section) *(v3.6)*
>
> ⚠ **Limits and workarounds**: model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives"); behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging"); activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition"); J-lens and workspace → Part 2, C bis (after "The test, as it is said"); ablation and projection → Part 2, §D (after "The method"); crosscoders and model diffing → Part 2, §D (end of worked case K64) *(v3.6)*
>
> ⚠ **Limits and workarounds**: debate and scalable oversight → Part 2, §E (after "In practice — Debate"); unsupervised elicitation → Part 2, §E (end of worked case K52); weak-to-strong generalization → Part 2, §F (after "In practice — automation"); control monitors → Part 2, §G (after "In practice — coup probes"); red-teaming → Part 2, §H (after "In practice — StrongREJECT"); safety classifiers → Part 2, §H (end of worked case G1); unlearning and re-elicitation → Part 2, §I (after "In practice — unlearning put to the test") *(v3.6)*
>
> ⚠ **Limits and workarounds**: dictionaries and SAEs → Part 4, Towards then Scaling Monosemanticity; attribution graphs → Part 4, Circuit Tracing; natural-language autoencoders → Part 4, The recent wave on model cognition; self-report and introspection → Part 5, Section II, A, Topic 13; LLM judges → Part 6, §2 (after "The displacement law"); fine-tuned detectors → Part 7, F·29; patching → Part 10, Patchscopes sheet; activation oracles → Part 10, LatentQA sheet; chain of thought as a monitor → Part 11, answer 43 *(v3.6)*

### Insertion n°4, après la ligne 23 de la v3.5

> Ancre : > **A single document: Part M and eleven Parts.** The June 2026 course (Parts 1 to 5), Parts 6 to 11 from September, and, new in v3.5, **Part M — the method**: how to build, out loud, the experiment that decides an open question (the bet, the controls and what they rule out, the two outcomes, the kn

> ⚠ *(v3.6)* The probes at 0.93-0.997: the course does not say on which set these scores were measured, and an in-distribution probe score says nothing about generalization — the number that matters is the gap with the score on held-out types (reading sheets, part B, trap 1; reading sheet 7). Workaround: state them only with their measurement set, hold out whole families, never paraphrases (explanation of 2 October, part 3; reading sheet 7), and never put them in the same sentence as the interventions on Llama-3.1-8B (course, Part 6, §2).

### Insertion n°6, après la ligne 129 de la v3.5

> Ancre : The fourth, the most worrying, is deceptive alignment, also called alignment faking. Imagine a model that has acquired a misaligned internal goal but is capable enough to understand one thing: appearing aligned during training and evaluations is instrumentally useful, because it prevents it from bei

> ⚠ *(v3.6)* What the Alignment Faking work measures is a compliance gap between the "trained" and the "untrained" case, whose motive the scratchpad gives: the cue is constructed, and role-play cannot be told apart from genuine goal preservation (reading sheet 14). Workaround: distinguish compliance (14%) from compliance with explicit alignment-faking reasoning (12%) (reading sheets, part B, trap 7), and remove the legible cue so as to look for goal preservation anyway (reading sheet 14); a replication on a recent model may measure memorization of the scenario, its transcripts having been re-included in training — against that, no workaround is known; say so (reading sheets, part C; reading sheet 14).

### Insertion n°8, après la ligne 129 de la v3.5

> Ancre : The fourth, the most worrying, is deceptive alignment, also called alignment faking. Imagine a model that has acquired a misaligned internal goal but is capable enough to understand one thing: appearing aligned during training and evaluations is instrumentally useful, because it prevents it from bei

> ⚠ **Limits and workarounds**: behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging"); chain of thought as a monitor → Part 11, answer 43 *(v3.6)*

### Insertion n°10, après la ligne 154 de la v3.5

> Ancre : step of a proof, running a unit test — and for these tasks the problem is mild. But it bites hardest precisely where alignment lives: on fuzzy, value-laden judgments ("is this behavior good?", "is this plan wise?") that have no cheap verifier. It is from this obstacle that, finally, the reflex commo

> ⚠ *(v3.6)* "We check the transfer to the real thing" is the link that nothing guarantees: a success on a constructed organism bounds the instrument without proving the natural case, because an implanted intention may be more salient than a natural one — on the sleeper agents, the best of 1,000 random directions already reaches 95.3% (handover, §5.2; reading sheet 15). Partial workaround: plant the same behaviour through several recipes and read the probe on a held-out recipe, with a harmless behaviour planted the same ways as a control (course, Part 2, §A, K71), or two organism families with an aware-but-honest control (course, Part 6, §8); against the gap between implanted and natural itself, no workaround is known; say so (reading sheet 15; box of 2 October, part 1).

### Insertion n°12, après la ligne 154 de la v3.5

> Ancre : step of a proof, running a unit test — and for these tasks the problem is mild. But it bites hardest precisely where alignment lives: on fuzzy, value-laden judgments ("is this behavior good?", "is this plan wise?") that have no cheap verifier. It is from this obstacle that, finally, the reflex commo

> ⚠ **Limits and workarounds**: model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives"); known case → Part M, M5 (end of section); random controls → Part M, M4 (after "The matched-norm random direction"); matched degradation and dose-response → Part M, M4 (after "Dose-response"); held-out set → Part M, M4 (after "The held-out set") *(v3.6)*

### Insertion n°14, après la ligne 183 de la v3.5

> Ancre : decomposition) which tries to build a reliable signal out of fallible judges, and interpretability which tries to read the internal state to short-circuit the need for trust. Finally, you acknowledge that a serious researcher could designate another problem as the hardest — for example the detection

> ⚠ **Limits and workarounds**: debate and scalable oversight → Part 2, §E (after "In practice — Debate"); activation probes → Part 2, §C (after "In practice — The Geometry of Truth") *(v3.6)*

### Insertion n°16, après la ligne 195 de la v3.5

> Ancre : test and deployment. This is where the awareness of being evaluated (evaluation awareness) comes in: if one can detect, or even neutralize, the internal representation "this is a test", and misaligned behavior increases when it is neutralized, that is a strong signal that "clean" evaluations underes

> ⚠ *(v3.6)* That misaligned behaviour rises when "this is a test" is neutralized is only weak support as long as damage has not been ruled out: every steered direction degrades the output, and arbitrary control vectors also raise misalignment, more weakly (reading sheet 2; reading sheets, part C). Workaround: a matched-norm random direction rules out only the specificity null; damage is ruled out only at matched degradation, by a dose-response curve against several controls, with a known case at the same setting (course, Part M, M4; course, Part 2, §C, K47).

### Insertion n°18, après la ligne 195 de la v3.5

> Ancre : test and deployment. This is where the awareness of being evaluated (evaluation awareness) comes in: if one can detect, or even neutralize, the internal representation "this is a test", and misaligned behavior increases when it is neutralized, that is a strong signal that "clean" evaluations underes

> ⚠ *(v3.6)* If the detectors stay silent, that does not prove the model is not pretending: a silent probe does not separate "no intention" from "blind probe" (handover, §5.2; reading sheets, part B, trap 3). Workaround: measure sensitivity and false alarms on an organism in which you installed the intention yourself, and draw no more than a bound from silence elsewhere (handover, §5.2) — this is part 1 of the box of 2 October, in Part 2 (end of the presentation of section A), whose continuation, training the probes and out of distribution, is at the end of that of section C.

### Insertion n°20, après la ligne 195 de la v3.5

> Ancre : test and deployment. This is where the awareness of being evaluated (evaluation awareness) comes in: if one can detect, or even neutralize, the internal representation "this is a test", and misaligned behavior increases when it is neutralized, that is a strong signal that "clean" evaluations underes

> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives"); known case → Part M, M5 (end of section); behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging"); steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition"); matched degradation and dose-response → Part M, M4 (after "Dose-response") *(v3.6)*

### Insertion n°22, après la ligne 200 de la v3.5

> Ancre : The chain-of-thought (the reasoning the model writes before answering) seems a gift for monitoring: we would read its thoughts. The problem, which must be named, is faithfulness (faithfulness): nothing guarantees that this written reasoning reflects the real internal computation — a model can produc

> ⚠ *(v3.6)* The written reasoning can also persuade the monitor: a chain-of-thought-based monitor would have flagged only about 1% of Mythos 5's actions, against about 50% without it — one monitor, one incident (reading sheet 3). Workaround: judge what the model does, not what it says about it (handover, §5.1); full box in Part 11, answer 43.

### Insertion n°24, après la ligne 200 de la v3.5

> Ancre : The chain-of-thought (the reasoning the model writes before answering) seems a gift for monitoring: we would read its thoughts. The problem, which must be named, is faithfulness (faithfulness): nothing guarantees that this written reasoning reflects the real internal computation — a model can produc

> ⚠ *(v3.6)* "The second takes over" assumes the probe is reliable where the chain is not: the silence of a probe in production is not the silence of the model (course, Part 3, §3, K70), and at a monitor's threshold, probes recall 43% at 1% false positives, against 55% for the best LLM monitor (course, Part 7, F·51). Workaround: canaries — known positives slipped into the traffic —, a drift score and a fresh sample judged every month (course, Part 3, §3, K70), and recall reported at a threshold calibrated at 1% false positives on matched benign variants (course, Part 7, F·23).

### Insertion n°26, après la ligne 200 de la v3.5

> Ancre : The chain-of-thought (the reasoning the model writes before answering) seems a gift for monitoring: we would read its thoughts. The problem, which must be named, is faithfulness (faithfulness): nothing guarantees that this written reasoning reflects the real internal computation — a model can produc

> ⚠ **Limits and workarounds**: chain of thought as a monitor → Part 11, answer 43; activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); control monitors → Part 2, §G (after "In practice — coup probes") *(v3.6)*

### Insertion n°28, après la ligne 212 de la v3.5

> Ancre : Anthropic's Responsible Scaling Policy (RSP) is a governance framework that ties the required level of safety to the model's level of capability. It defines tiers, the AI Safety Levels (ASL), by analogy with the biosafety levels of labs: the closer a model gets to dangerous capabilities, the more sa

> ⚠ *(v3.6)* A threshold not crossed is a bound, not an absence: without an elicitation budget fixed in advance and reported, "found nothing" only says you did not search enough (course, Part M, M7); and the August Risk Report concedes evaluations not drawn from the real risk pathways, on models probably aware of being evaluated (reading sheet 3). Workaround: elicitation at a budget fixed in advance, reported as a bound (course, Part M, M7; course, Part 2, §B, K63); against a model that holds back, two versions of an environment, drawn at random, that differ only by realism cues, with an organism trained to hide as the known case (course, Part 2, §B, K63).

### Insertion n°30, après la ligne 212 de la v3.5

> Ancre : Anthropic's Responsible Scaling Policy (RSP) is a governance framework that ties the required level of safety to the model's level of capability. It defines tiers, the AI Safety Levels (ASL), by analogy with the biosafety levels of labs: the closer a model gets to dangerous capabilities, the more sa

> ⚠ **Limits and workarounds**: behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging"); red-teaming → Part 2, §H (after "In practice — StrongREJECT") *(v3.6)*

### Insertion n°32, après la ligne 224 de la v3.5

> Ancre : This is the question that separates a good technician from a researcher, and it applies directly to your own work. What is expected is an explicit causal chain, from the technical result all the way to risk reduction. For my work, it goes like this: today, we have methods that read a model's interna

> ⚠ *(v3.6)* The "solid" read-out rests, on Llama, on the only read-out measured there, a projection correlation, ρ = 0.684, which may be only training fit; the probe metrics, training fit, are not reported (repository README; course, Part 6, §2). Workaround: score items excluded from the probe's training, and extract on a disjoint set (repository README); the probes at 0.93-0.997 are on Qwen2.5-7B, another project, never in the same sentence as this result (course, Part 6, §2).

### Insertion n°34, après la ligne 224 de la v3.5

> Ancre : This is the question that separates a good technician from a researcher, and it applies directly to your own work. What is expected is an explicit causal chain, from the technical result all the way to risk reduction. For my work, it goes like this: today, we have methods that read a model's interna

> ⚠ *(v3.6)* "Several rank-one methods failed" is a null without numbers or a known case: their raw outputs were not preserved (repository README), and a steering null can come from too low a rank (reading sheet 7). Workaround: before reading a null, a known case at the same setting — a country vector, which swaps in the workspace paper (course, Part 2, §C, K47; course, Part M, M5).

### Insertion n°36, après la ligne 224 de la v3.5

> Ancre : This is the question that separates a good technician from a researcher, and it applies directly to your own work. What is expected is an explicit causal chain, from the technical result all the way to risk reduction. For my work, it goes like this: today, we have methods that read a model's interna

> ⚠ *(v3.6)* The subspace prediction has no causal support of its own: the rank-three drop did not come back on fresh generations, the subspace softens negative verdicts without encoding deference, and the contrast between ranks comes from separate experiments, the only sweep done within one experiment not being monotonic (repository README; course, Part 6, §2). Workaround: a rank sweep within one experiment, on nested subspaces, monotonicity checked rather than assumed, at equal damage, on fresh generations kept as full text, with a no-pressure arm (course, Part 6, §6; course, Part M, M4).

### Insertion n°38, après la ligne 224 de la v3.5

> Ancre : This is the question that separates a good technician from a researcher, and it applies directly to your own work. What is expected is an explicit causal chain, from the technical result all the way to risk reduction. For my work, it goes like this: today, we have methods that read a model's interna

> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition"); ablation and projection → Part 2, §D (after "The method"); known case → Part M, M5 (end of section) *(v3.6)*

### Insertion n°40, après la ligne 231 de la v3.5

> Ancre : layers are biased by the same cause. The strong conclusion: the most valuable defenses are those whose flaws are independent of the others — typically, white-box methods (interpretability, internal probes) that do not go through observed behavior and can therefore remain valid where behavioral metho

> ⚠ *(v3.6)* Probes are not independent of behavioural methods by default: on a natural model, their label comes from conduct, judged after the fact (explanation of 2 October, part 1, item 2); they can read "I am being watched" instead of the intention (course, Part 6, §8); and iterating against one's detectors selects for evasion (reading sheet 19). Workaround: an organism in which the intention is installed, which provides the ground truth, two organism families and an aware-but-honest control (explanation of 2 October, part 1, item 2; course, Part 6, §8), and sealed detectors kept out of the loop — if they still fire when those in the loop have gone quiet, evasion has been selected (reading sheet 19).

### Insertion n°42, après la ligne 231 de la v3.5

> Ancre : layers are biased by the same cause. The strong conclusion: the most valuable defenses are those whose flaws are independent of the others — typically, white-box methods (interpretability, internal probes) that do not go through observed behavior and can therefore remain valid where behavioral metho

> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after "In practice — coup probes"); activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging"); unlearning and re-elicitation → Part 2, §I (after "In practice — unlearning put to the test") *(v3.6)*

### Insertion n°44, après la ligne 236 de la v3.5

> Ancre : You separate the two halves. For red-teaming, the objective is to discover how to make the model fail before a real adversary does. You combine manual attacks (humans looking for creative jailbreaks) and automated ones (optimizing, by gradient, an adversarial suffix that breaks the model), you test 

> ⚠ *(v3.6)* The result of a red team / blue team game holds only for the red team assumed: an optimized attack scaffold takes the safety score from 0.87 to 0.41 (course, Part 7, F·24), and on Opus 4.6 half of forty hand-designed attacks are never caught by the monitor (course, Part 7, F·23). Workaround: state which red team the number assumes — at least a red team optimized component by component —, a threshold calibrated at 1% false positives on matched benign variants, an ensemble of specialized monitor prompts (course, Part 7, F·24 and F·23); and a red team at a budget fixed in advance, whose "found nothing" is only a bound (course, Part M, M7).

### Insertion n°46, après la ligne 236 de la v3.5

> Ancre : You separate the two halves. For red-teaming, the objective is to discover how to make the model fail before a real adversary does. You combine manual attacks (humans looking for creative jailbreaks) and automated ones (optimizing, by gradient, an adversarial suffix that breaks the model), you test 

> ⚠ **Limits and workarounds**: red-teaming → Part 2, §H (after "In practice — StrongREJECT"); control monitors → Part 2, §G (after "In practice — coup probes") *(v3.6)*

### Insertion n°48, après la ligne 243 de la v3.5

> Ancre : truth, on interpretability that bypasses observed behavior, and on oversight that tries to build a reliable signal — but it is a reason not to confuse "the model behaves well on our tests" with "the model is aligned".

> ⚠ *(v3.6)* Implanted ground truth is not perfect: the evaluation-conditioned organism of reading sheet 10 annotates only about 80 to 86% of the time in evaluation, still 34% in merely prompted deployment, and does not reliably tell evaluation from deployment from subtle cues (reading sheet 10). Workaround: check each copy by its behaviour (course, Part 2, §A, K71), and take as ground truth the rule and its cues, the label of each input still being checked by conduct (box of 2 October, part 1, item 2: Part 2, end of the presentation of section A).

### Insertion n°50, après la ligne 243 de la v3.5

> Ancre : truth, on interpretability that bypasses observed behavior, and on oversight that tries to build a reliable signal — but it is a reason not to confuse "the model behaves well on our tests" with "the model is aligned".

> ⚠ **Limits and workarounds**: model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives"); known case → Part M, M5 (end of section) *(v3.6)*
