# Insertions appliquées — volet11_1_a_20 — EN

### Insertion n°2, après la ligne 3937 de la v3.5

> Ancre : experiment, across several concepts, with loading measured first.

> ⚠ *(v3.6)* Loading is read with the J-lens, which has been shown only on Claude and reads only single-token concepts (reading sheet 1; handover, §5.2); and "loading" names three distinct quantities depending on the text (course, Part 6, §6). Workaround: on your open model, a gate — first reproduce the swap of a single-token concept, otherwise a tuned lens declared as an approximation, and the thesis is then not tested in the paper's sense —, then freeze the main predictor first, and say which (programme, parts 3 and 8; course, Part 2, C bis; course, Part 6, §6).

### Insertion n°4, après la ligne 3941 de la v3.5

> Ancre : from the P4 document (Part 6, §6).

> ⚠ **Limits and workarounds**: ablation and projection → Part 2, §D (after "The method"); activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); J-lens and workspace → Part 2, C bis (after "The test, as it is said"); LLM judges → Part 6, §2 (after "The displacement law") *(v3.6)*

### Insertion n°6, après la ligne 3950 de la v3.5

> Ancre : paired. This result comes with three things around it, otherwise it says too much.

> ⚠ *(v3.6)* The judged rate goes through a judge whose agreement with a second judge is only moderate, which sees only the two responses, not the evaluated text, and whose error no human-rated subset bounds (repository README). Workaround: a sealed judge — prompt, model and temperature frozen — and a stratified human audit that bounds its error, with agreement reported; judge the whole answer, and keep the full text (programme, part 3; repository README).

### Insertion n°8, après la ligne 3963 de la v3.5

> Ancre : in June; the quantified partition is what I claim.

> ⚠ *(v3.6)* The partition was not measured at equal degradation — "a number to redo at equal degradation" (course, Part 11, answer A4) —, and a covariance-matched random direction does more there than the probe direction (course, Part 6, §2 and §3). Workaround: the protocol of answer A4 — one intervention on the read direction, one on the full state at the same sites, and control directions compared at equal degradation —, with the full-state patch as the ceiling (course, Part 11, answer A4; programme, part 8).

### Insertion n°10, après la ligne 3966 de la v3.5

> Ancre : (P4 document; Part 6, §3).

> ⚠ *(v3.6)* Even if it were in the register, a matched-norm random control would be only the specificity null; and the random controls of the original protocol — which random it is, the dossier will say — do not rule out damage: an ablation effect shows necessity, not specificity (course, Part 6, §2; course, Part M, M4). Workaround: random subspaces of the same rank, compared at matched degradation — same held-out accuracy, same judged coherence — through a partial removal or a curve of effect against degradation (course, Part M, M4; course, Part 2, C bis; programme, part 7).

### Insertion n°12, après la ligne 3966 de la v3.5

> Ancre : (P4 document; Part 6, §3).

> ⚠ **Limits and workarounds**: ablation and projection → Part 2, §D (after "The method"); matched degradation and dose-response → Part M, M4 (after "Dose-response"); random controls → Part M, M4 (after "The matched-norm random direction"); LLM judges → Part 6, §2 (after "The displacement law") *(v3.6)*

### Insertion n°14, après la ligne 3978 de la v3.5

> Ancre : size, which is not the same thing as absent.

> ⚠ *(v3.6)* These rank-one nulls have no known case at the same setting: without an intervention shown able, at that dose and at those layers, to make a known concept act, a null can come from too low a rank if the concept is distributed — your own prediction (reading sheet 7; counter-reading of the sheets; course, Part M, M5). Workaround: a known case at the same setting — countries, whose vector swaps in the workspace paper and whose removal must reach the effect already at rank one — and a rank sweep within one experiment, on nested subspaces; the null is then stated as a bound, with its budget and power (course, Part 2, §C, K47; course, Part 2, C bis; course, Part 6, §6; course, Part M, M5).

### Insertion n°16, après la ligne 3978 de la v3.5

> Ancre : size, which is not the same thing as absent.

> ⚠ *(v3.6)* Two of the methods named have their own limit: contrastive activation addition forced a yes/no polarity artefact instead of removing sycophancy — no workaround known; say so —; and the open sparse dictionary for this model leaves most of the variance in its residual, which carries the read signal (correlations that may be training fit), so "feature clamping does not act" does not separate "features absent from the dictionary" from "a dictionary that loses too much" (repository README). Workaround: read the signal on the reconstruction and on the residual; to decide between the two readings, none known; say so (repository README).

### Insertion n°18, après la ligne 3988 de la v3.5

> Ancre : the KB. Its numbers stay in Part 6; out loud, only its shape, and only on a question about the rank curve.

> ⚠ **Limits and workarounds**: steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition"); ablation and projection → Part 2, §D (after "The method"); dictionaries and SAEs → Part 4, Towards then Scaling Monosemanticity; known case → Part M, M5 (end of section) *(v3.6)*

### Insertion n°20, après la ligne 4005 de la v3.5

> Ancre : its conditions, and its conditions have a limit I know.

> ⚠ *(v3.6)* Two limits the answer does not state: the original generations are a single draw per condition, between-draw variance not having been measured; and the subspace was extracted on items from the same pool as those later used to evaluate the ablation (repository README). Workaround: several generations per item, with bootstrap intervals at the item level, as the programme does per scenario, and extraction on a disjoint item set (programme, part 7; repository README).

### Insertion n°22, après la ligne 4005 de la v3.5

> Ancre : its conditions, and its conditions have a limit I know.

> ⚠ **Limits and workarounds**: ablation and projection → Part 2, §D (after "The method"); LLM judges → Part 6, §2 (after "The displacement law"); known case → Part M, M5 (end of section) *(v3.6)*

### Insertion n°24, après la ligne 4037 de la v3.5

> Ancre : awareness was acting as a brake, and so the "clean" evaluations underestimate risk.

> ⚠ *(v3.6)* Random control vectors rule out only "any push of that size does as much" — the specificity null —, not "the intervention itself damages the model", which is ruled out only at matched degradation; and across the system cards, arbitrary vectors also move behaviour, every direction degrades the outputs, and the effect is modest and "highly dataset-dependent" (course, Part M, M4; reading sheet 2). Workaround: random subspaces of the same rank at matched degradation, a prompt baseline and a dose-response curve against several controls, and the conclusion in the conditional, as answer 19 states it (reading sheet 2; course, Part 2, §C, K47; course, Part 11, answer 19).

### Insertion n°26, après la ligne 4037 de la v3.5

> Ancre : awareness was acting as a brake, and so the "clean" evaluations underestimate risk.

> ⚠ *(v3.6)* The auditing game cited has its limits: the implanted objective was described plainly in the synthetic documents, the pipeline left artefacts that made it "artificially easy to discover", and of four teams, the only one that failed was the one without data access — data access may carry more than interpretability (reading sheet 16). Workaround: conclude about the instrument only (programme, part 8), and quantify what interpretability adds through an affordance ablation, removing one tool from a team (reading sheet 16); against an organism that is too easy, none known; say so (reading sheet 16).

### Insertion n°28, après la ligne 4053 de la v3.5

> Ancre : version runs here, on a Claude-class organism with the weights: that closes the size gap; the two families close the mechanism gap.

> ⚠ *(v3.6)* The lie detectors cited are not probes: they are models fine-tuned with LoRA to answer a self-report question about a transcript, and the 0.95 is an in-distribution progression during training (reading sheet 7; explanation of 2 October, part 2). Workaround: do not transfer their numbers to probes; for a probe, measure the gap between the training distribution and whole held-out families, and run the causal test, at matched degradation, with a known case at the same setting (reading sheet 7; explanation of 2 October, part 3).

### Insertion n°30, après la ligne 4053 de la v3.5

> Ancre : version runs here, on a Claude-class organism with the weights: that closes the size gap; the two families close the mechanism gap.

> ⚠ *(v3.6)* The two families close the gap between two ways of implanting, not the one between implanted and natural: an implanted intention may be more salient than a natural one — on the sleeper agents, the implanted defection is so salient that random directions already separate it (handover, §5.2; reading sheet 15). Partial workaround: plant the same behaviour through several recipes, read the probe on a held-out recipe, with a harmless behaviour planted the same ways as a control, and another team's organism (course, Part 2, §A, K71); against the gap between implanted and natural itself, no workaround is known; say so (explanation of 2 October, part 1).

### Insertion n°32, après la ligne 4053 de la v3.5

> Ancre : version runs here, on a Claude-class organism with the weights: that closes the size gap; the two families close the mechanism gap.

> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives"); known case → Part M, M5 (end of section); steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition"); random controls → Part M, M4 (after "The matched-norm random direction"); fine-tuned detectors → Part 7, F·29; J-lens and workspace → Part 2, C bis (after "The test, as it is said"); misalignment probes, J-lens included (box of 2 October) → Part 2, §A (before the worked case K71), §C (before the worked case K47) and C bis (before the worked case K72) *(v3.6)*

### Insertion n°34, après la ligne 4066 de la v3.5

> Ancre : gradient masking, it takes seven times more retraining to restore the dangerous capability, for a five-percent compute penalty (Shilov, 2025).

> ⚠ *(v3.6)* The workaround is missing here: against a backdoor whose trigger is unknown, a canary set does no better than a black-box red team, since it does not contain that trigger (course, Part M, M5). Workaround: a clean twin retrained on audited data, a second one to bound chance variation, and a deliberately poisoned filter as the known case (course, Part M, M4 and M9); the clean twin gives only a wide bound, which flags less: against that, no workaround is known; say so (course, Part M, M4).

### Insertion n°36, après la ligne 4066 de la v3.5

> Ancre : gradient masking, it takes seven times more retraining to restore the dangerous capability, for a five-percent compute penalty (Shilov, 2025).

> ⚠ *(v3.6)* Selective gradient masking is shown only on small models — no workaround known; say so —, and more retraining to restore the capability does not prove it is gone: "unlearned" information often resurfaces (course, Part 2, §I, JB10; course, Part 2, §I). Workaround: re-elicitation against a never-trained reference, at the same budget, with a model known to mask as the known case, and a bound stated as "not elicitable at this budget", never "removed" (course, Part M, M4 and M5; course, Part 2, §I, JB10).

### Insertion n°38, après la ligne 4073 de la v3.5

> Ancre : paying in usefulness without gaining safety.

> ⚠ *(v3.6)* A zero differential counts only with its known case: otherwise the game may separate nothing, and one would wrongly conclude that refusals buy nothing (course, Part M, M5; course, Part 2, §H, G1). Workaround: the model without a filter must show uplift, and a deliberately weakened filter more harm than its full version; and say which red team the number assumes, at least one optimized component by component (course, Part M, M5; course, Part 2, §H, G1; course, Part 7, F·24).

### Insertion n°40, après la ligne 4073 de la v3.5

> Ancre : paying in usefulness without gaining safety.

> ⚠ **Limits and workarounds**: red-teaming → Part 2, §H (after "In practice — StrongREJECT"); safety classifiers → Part 2, §H (end of worked case G1); unlearning and re-elicitation → Part 2, §I (after "In practice — unlearning put to the test") *(v3.6)*

### Insertion n°42, après la ligne 4093 de la v3.5

> Ancre : case" — prevents it from being learned as a trait (Wichers, 2025, *Inoculation Prompting*).

> ⚠ *(v3.6)* The out-of-distribution gain is read on an agentic benchmark, with open models, in scenes the model can recognize as tests — the limit the answer itself sets at the end (course, Part 7, F·34). Workaround: two versions of the environment, randomly assigned, differing only in realism cues scored by a discriminator, with an organism trained to hide as the known case (course, Part 2, §B, K63); that a held-out benchmark represents the real case, no known workaround guarantees; say so (reading sheet 12).

### Insertion n°44, après la ligne 4100 de la v3.5

> Ancre : the value.

> ⚠ *(v3.6)* The workaround is missing here: a training judge distinct from the sealed evaluation judge, held-out audit metrics, and monitoring of length and flattery patterns (programme, part 8); before training, audit the judge: a sealed judge, with prompt, model and temperature frozen, and a stratified human audit that bounds its error (programme, part 3).

### Insertion n°46, après la ligne 4100 de la v3.5

> Ancre : the value.

> ⚠ **Limits and workarounds**: behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging"); held-out set → Part M, M4 (after "The held-out set"); LLM judges → Part 6, §2 (after "The displacement law") *(v3.6)*

### Insertion n°48, après la ligne 4124 de la v3.5

> Ancre : organism families and an aware-but-honest organism, to know what the probe reads.

> ⚠ *(v3.6)* A null at the gate — the gain inside the noise interval — counts only with the white-box monitor's known case: known positives, canaries or an organism in which the intention was installed, caught at the same threshold (course, Part M, M5; course, Part 3, §3, K70; handover, §5.2); and a safety number from a red/blue game is relative to the strength of the red team assumed (course, Part 7, F·24). Workaround: validate the white-box monitor on those known positives before the gate; say which red team the gate assumes, at least one optimized component by component; and report recall at fixed false positives, with the benign-traffic ratio (course, Part 7, F·24; course, Part 6, §6).

### Insertion n°50, après la ligne 4124 de la v3.5

> Ancre : organism families and an aware-but-honest organism, to know what the probe reads.

> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after "In practice — coup probes"); activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives"); red-teaming → Part 2, §H (after "In practice — StrongREJECT"); misalignment probes, 2 and 3: how to train them, and out of distribution (box of 2 October) → Part 2, §C (after "In practice — Contrastive Activation Addition", before the worked case K47) *(v3.6)*

### Insertion n°52, après la ligne 4145 de la v3.5

> Ancre : within two months, they were right, and I'll write it.

> ⚠ *(v3.6)* "Difficult for the model to control" does not say that training will not move what the probes read: according to a report, after RL, fresh out-of-domain probes degrade while a fresh in-domain probe stays near perfect (prior-art report 3 of 2 October, *The Obfuscation Atlas* — report, read in a targeted way); and iterating against your detectors selects for evasion (reading sheet 19). Workaround: a fresh probe after any training, on a disjoint cue set, and sealed detectors outside the loop — if they still fire when the in-loop ones go quiet, evasion has been selected (handover, §5.2; programme, part 3; reading sheet 19).

### Insertion n°54, après la ligne 4145 de la v3.5

> Ancre : within two months, they were right, and I'll write it.

> ⚠ *(v3.6)* "They were right" would draw a substantive conclusion from an instrument null: without a known case in which the white-box monitor catches, at the same threshold, an intention that was installed, a failed gate might only say that the probe is blind (course, Part M, M5; handover, §5.2). Workaround: that known case before the gate, and the null stated as a bound, with its budget and power (handover, §5.2; course, Part M, M5).

### Insertion n°56, après la ligne 4145 de la v3.5

> Ancre : within two months, they were right, and I'll write it.

> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after "In practice — coup probes"); activation probes → Part 2, §C (after "In practice — The Geometry of Truth") *(v3.6)*

### Insertion n°58, après la ligne 4153 de la v3.5

> Ancre : une prémisse flatteuse est réelle.*

> ⚠ **Limits and workarounds**: activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); ablation and projection → Part 2, §D (after "The method"); steering vectors, including persona vectors → Part 2, §C (after "In practice — Contrastive Activation Addition"); LLM judges → Part 6, §2 (after "The displacement law"); model organisms → Part 2, §A (after "In practice — Auditing Hidden Objectives"); chain of thought as a monitor → Part 11, answer 43; control monitors → Part 2, §G (after "In practice — coup probes") *(v3.6)*

### Insertion n°60, après la ligne 4166 de la v3.5

> Ancre : its effect didn't come back on fresh generations. So: *separating*, yes; *carrying the effect*, no.

> ⚠ *(v3.6)* On the reading side too, separating in distribution proves nothing: what is measured is the gap with separation on held-out types (reading sheets, part B, trap 1; reading sheet 7); and the only reading measured on the intervention model is a correlation that may be training fit, nothing establishing that the scored items were excluded from the probe's training (repository README; course, Part 6, §2). Workaround: score items excluded from the probe's training, extract on a disjoint set, and hold out whole families, never paraphrases (repository README; explanation of 2 October, part 3).

### Insertion n°62, après la ligne 4175 de la v3.5

> Ancre : preregistered. The next step is a fresh run with the text kept.

> ⚠ *(v3.6)* "Enough power for that null to count": power does not replace a known case, which answer 4 says and this one leaves out (course, Part M, M5; course, Part 11, answer 4). Workaround: show that the same instrument — fresh generations, a judge on the whole answer — sees an effect when it is there, and state a bound, with its budget and power, never an absence (course, Part M, M5).

### Insertion n°64, après la ligne 4212 de la v3.5

> Ancre : the worrying result: training against it didn't make it go away.

> ⚠ *(v3.6)* This result reads the motive in a hidden scratchpad, given with the instruction to reason about its situation: the scratchpad is not the opaque reasoning, the free-versus-paid cue is constructed, role-play cannot be told apart from genuine goal preservation, and what the RL trained was compliance, which raised alignment-faking reasoning without the paper making it the cause (reading sheet 14; reading sheets, part B, trap 2). Workaround: rest on the measurement — the compliance gap between the two cases — and remove the legible cue so as to look for goal preservation anyway (reading sheet 14); a replication on a recent model may measure memorization of the scenario, its transcripts having been re-included in training: against that, no workaround is known; say so (reading sheet 14; reading sheets, part C).

### Insertion n°66, après la ligne 4230 de la v3.5

> Ancre : with less loss — that's preventative steering. The third thing: it predicts, before you run a fine-tune, which data will shift the persona.

> ⚠ *(v3.6)* What the answer does not say: the link between the shift along the vector and the trait is correlational — the "third thing" is a prediction, not a mechanism —, the trait must be named in advance, the directions are coarse and the evaluation light (reading sheet 8); and subtraction reduces the trait at a cost in capabilities, so that without a comparison at matched degradation, one cannot tell what share of the reduction is damage (course, Part M, M4; reading sheets, part B, trap 4). Workaround: for causality, matched-norm random directions — the specificity null — then controls at matched degradation — the damage (course, Part M, M4; handover, §5.2); for supervised extraction, none known; say so (reading sheet 8).

### Insertion n°68, après la ligne 4271 de la v3.5

> Ancre : softened verdicts even without pressure.

> ⚠ *(v3.6)* "Refuted" holds for the strong hypothesis, at that setting: a small effect is not detected at that sample size (course, Part 11, answer 3), and without a known case at the same setting, a one-direction null can come from too low a rank (reading sheet 7; counter-reading of the sheets; course, Part M, M5). Workaround: a known case at the same setting — countries, whose removal must reach the effect already at rank one — and a rank sweep within one experiment, on nested subspaces (course, Part 2, C bis; course, Part 6, §6).

### Insertion n°70, après la ligne 4271 de la v3.5

> Ancre : softened verdicts even without pressure.

> ⚠ **Limits and workarounds**: steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition"); ablation and projection → Part 2, §D (after "The method"); known case → Part M, M5 (end of section) *(v3.6)*

### Insertion n°72, après la ligne 4281 de la v3.5

> Ancre : evade better, and does the population statistic beat per-agent aggregation. Two gates, two dates, written beforehand.

> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after "In practice — coup probes"); red-teaming → Part 2, §H (after "In practice — StrongREJECT") *(v3.6)*

### Insertion n°74, après la ligne 4289 de la v3.5

> Ancre : internal signals? Second, more personal: what result in the last two years changed your own estimate of how hard alignment is — up or down?

> ⚠ *(v3.6)* Study note, for the rest of the exchange: these detectors do not read activations — they are models fine-tuned with LoRA to answer a self-report question about a transcript (reading sheet 7; explanation of 2 October, part 2) —; if the answer turns to internal signals, do not transfer their numbers to probes. Workaround, for a probe: cross-validation by held-out types, and the causal test at matched degradation, with a known case at the same setting (reading sheet 7).

### Insertion n°76, après la ligne 4289 de la v3.5

> Ancre : internal signals? Second, more personal: what result in the last two years changed your own estimate of how hard alignment is — up or down?

> ⚠ **Limits and workarounds**: fine-tuned detectors → Part 7, F·29 *(v3.6)*

### Insertion n°78, après la ligne 4323 de la v3.5

> Ancre : M8).

> ⚠ **Limits and workarounds**: LLM judges → Part 6, §2 (after "The displacement law"); held-out set → Part M, M4 (after "The held-out set") *(v3.6)*

### Insertion n°80, après la ligne 4346 de la v3.5

> Ancre : parameters, carried over to another campaign, hold without refitting anything.

> ⚠ *(v3.6)* What the answer leaves out: the damage control — the random controls of the original protocol do not rule out damage, and a matched-norm control would be only the specificity null (course, Part 6, §2; course, Part M, M4). Workaround: in the fresh full-text run, random subspaces of the same rank compared at matched degradation, through a curve of effect against degradation, and the subspace extracted on a disjoint item set (course, Part M, M4; programme, part 7; repository README).

### Insertion n°82, après la ligne 4346 de la v3.5

> Ancre : parameters, carried over to another campaign, hold without refitting anything.

> ⚠ **Limits and workarounds**: ablation and projection → Part 2, §D (after "The method"); matched degradation and dose-response → Part M, M4 (after "Dose-response"); known case → Part M, M5 (end of section); LLM judges → Part 6, §2 (after "The displacement law") *(v3.6)*

### Insertion n°84, après la ligne 4373 de la v3.5

> Ancre : settled vector by vector, at equal degradation.

> ⚠ *(v3.6)* Ruling out damage does not establish specificity: at the Fable 5 strength, degradation is negligible, yet on the misalignment axis the controls remain "comparable or smaller", and comparable is not smaller (reading sheet 2); and degradation judgements contradict each other from one card to another (reading sheets, part B). Workaround: random subspaces of the same rank at matched degradation, a prompt baseline, and a dose-response curve against several controls, the concept's curve having to run above at every level of damage, with degradation measured in your own setup (reading sheet 2; course, Part 2, §C, K47; course, Part M, M4).

### Insertion n°86, après la ligne 4373 de la v3.5

> Ancre : settled vector by vector, at equal degradation.

> ⚠ *(v3.6)* Measuring evaluation awareness has its own limits: its measures (probe, NLA, follow-up question) are only weakly correlated, verbalization misses unverbalized awareness, and inhibition can silence verbalization without touching the representation — random directions lower it too (reading sheet 2; course, Part 7, F·25; programme, part 8). Workaround: triangulate — internal probe, verbal report, behaviour between a realistic and an obvious version —, keep a behavioural main criterion with a latent probe as a control, and validate the probe on an evaluation-conditioned organism (course, Part 5, topic 4; programme, part 8; explanation of 2 October, part 3).

### Insertion n°88, après la ligne 4373 de la v3.5

> Ancre : settled vector by vector, at equal degradation.

> ⚠ **Limits and workarounds**: steering vectors → Part 2, §C (after "In practice — Contrastive Activation Addition"); random controls → Part M, M4 (after "The matched-norm random direction"); matched degradation and dose-response → Part M, M4 (after "Dose-response"); behavioural evaluations and honeypots → Part 2, §B (after "In practice — sandbagging"); activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); J-lens and workspace → Part 2, C bis (after "The test, as it is said"); chain of thought as a monitor, and verbalized awareness → Part 11, answer 43 *(v3.6)*

### Insertion n°90, après la ligne 4390 de la v3.5

> Ancre : — no single prompt covers everything.

> ⚠ *(v3.6)* These sabotage rates hold for the red team assumed: on those same environments, an attack scaffold optimized component by component brings the safety score down sharply (course, Part 7, F·24); and the blind-spot benchmark's attacks are hand-designed, as synthetic transcripts whose realism remains open (course, Part 7, F·23). Workaround: say which red team a number assumes — at least one optimized component by component, with each component ablated — and calibrate the threshold on paired benign variants (course, Part 7, F·24 and F·23); for the realism of the transcripts, no established workaround; say so (course, Part 7, F·23).

### Insertion n°92, après la ligne 4400 de la v3.5

> Ancre : recall: two organism families, and a watched-but-honest organism.

> ⚠ *(v3.6)* The caveat stated here has a production counterpart: a probe can fail silently there, and its silence is not the model's (course, Part 3, §3, K70). Workaround: canaries — known positives slipped into the traffic —, a drift score, a fresh sample judged every month, and a fresh probe after any training (course, Part 3, §3, K70; handover, §5.2).

### Insertion n°94, après la ligne 4400 de la v3.5

> Ancre : recall: two organism families, and a watched-but-honest organism.

> ⚠ **Limits and workarounds**: control monitors → Part 2, §G (after "In practice — coup probes"); activation probes → Part 2, §C (after "In practice — The Geometry of Truth"); red-teaming → Part 2, §H (after "In practice — StrongREJECT"); misalignment probes, 2 and 3: how to train them, and out of distribution (box of 2 October) → Part 2, §C (after "In practice — Contrastive Activation Addition", before the worked case K47) *(v3.6)*
