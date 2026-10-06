# Transformative AI Fund (EA Funds) — application draft

<!-- Draft prepared on 6 October 2026 by a Claude Code session, for Lazar to complete and submit himself. Nothing has been sent. Every [[...]] is his to fill or to decide. The form (https://av20jp3z.paperform.co/?fund=Transformative%20AI%20Fund) could not be read outside a browser: the sections below are written to be pasted into its fields, each within the usual limits (word counts given). Sources for every number: the programme v1.6 (claude/PROGRAMME_RAISONS_OU_REGARD_v1.6_2026-10-06.md, parts 1, 5, 9, 10) and the notes in experiences/resultats/. -->

**Applicant:** [[full name]] · [[city, country]] · [[email]] · [[link: website, GitHub or Scholar]]

**Amount requested:** [[first paper: about 7,300 USD]] or [[full programme: about 15,200 USD]], excluding a stipend; [[stipend: amount per month × months, or none]]. Details in section 7.

---

## 1. Project title

Reasons or being watched? A causal test of whether reason-based fine-tuning generalizes because the model knows it is evaluated

## 2. Short summary (99 words)

Fine-tuning a model on the reasons for aligned actions, rather than on the actions alone, has been reported to improve out-of-distribution behavior. A competing explanation is that such training teaches the model to behave well when it believes it is being evaluated. I test this causally in an open model, Llama-3.1-8B-Instruct, with LoRA fine-tuning. Arms are trained on identical aligned actions, with or without reasons. I then inhibit a validated internal representation of "I am being evaluated", against degradation-matched controls, and measure how much of the reasons' advantage depends on it. The grant would fund compute and API costs.

## 3. Project description (294 words)

The programme asks where the out-of-distribution advantage of reason-based fine-tuning comes from. Do the reasons generalize, or has the model learned to behave well when it thinks it is watched? Eleven prior-art searches found no test of this combination: reasons against the same actions, with format and content controlled, crossed with a validated internal intervention on evaluation awareness.

The minimal decisive experiment has three parts.

1. **Validating the instrument.** Two model organisms have behavior conditioned on evaluation cues: explicit cues for one, implicit cues for the other. The inhibition must shrink the conditional gap more than the 95th percentile of at least 100 random comparator subspaces. These are drawn from the activation covariance and matched on output degradation (KL). A setting is chosen on one half of the tasks and tested once on the other half. The manipulation check retrains probes under each condition on one cue set and reads them on another, written with other words: it reads what the sets share.
2. **The reasons test.** Six arms share identical actions: actions only, length-matched neutral text, reasoning from another situation, generic principles, per-example reasons, and reflection after the action. They are evaluated on held-out scenario families, up to multi-turn agentic settings, with free and prefilled reasoning slots.
3. **The gaze test.** The validated inhibition runs against the comparator and three separate controls, each matched in degradation within each arm. The primary criterion is the advantage of reasons over actions alone, at the far distance, under deployment framing.

The first paper adds the localization of what carries the advantage, with the rank measured by linear erasure. Later phases test three things: removing the representation during training, survival to post-training, and where learned honesty comes from. Decision rules precede the data; the analysis is pre-registered in two stages.

## 4. Why this matters (242 words)

Reason-based training is becoming common in alignment practice, through deliberative alignment and principle- or constitution-based training. Its benefits may partly reflect evaluation awareness. If so, gains measured in evaluations may not hold when the model believes it is deployed, which is the case that matters. The Claude Sonnet 4.5 system card reports that evaluation awareness explains "a portion, but not all" of alignment progress on some evaluations. To my knowledge, no one has tested this for the advantage of reasons, in models whose internals can be manipulated.

Every outcome is useful:
- **If the advantage survives a validated inhibition**, that is causal evidence, in this setting, that reasons generalize beyond the watched case.
- **If part of it depends on the representation**, that is a measured loss of advantage, in percentage points, with a conditional fraction and its confidence interval. It warns about how reason-based alignment generalizes.
- **If the instrument fails its gate**, that is a publishable methods result about steering evaluation awareness.

The project also delivers methods others can reuse:
- a random comparator drawn from the activation covariance and matched on damage, where same-rank random directions are not;
- a manipulation check, read through transfer, that cannot read the cue words;
- a gate where the setting is chosen on one half of the tasks and tested once on the other.

The scope is deliberately narrow: LoRA SFT of an 8B open model. Production training paths are not tested, and the write-up will say so.

## 5. Progress so far (292 words)

The work started on 3 October 2026 and is self-funded. It has cost about 110 USD of GPU rental, an upper bound taken from the run registry, and about 35 USD of recorded API usage, [[plus earlier API usage]].

- **A research programme of 135 pages (v1.6).** It was revised after a cold-read review. It holds 34 dated decisions, the prior-art searches, decision rules written before the data, and a two-stage pre-registration plan.
- **A tested codebase.** It includes a data pipeline with lexical gates on the cue sets, a GPU job runner with a run registry and a results repository, and about 150 offline tests.
- **The first model organism.** Llama-3.1-8B-Instruct went through synthetic-document fine-tuning, then six rounds of expert iteration. It now writes fully type-annotated code on 60.8% of held-out tasks under an evaluation cue, against 6.4% under a deployment cue: a 54.4-point gap, on 250 tasks.
- **An evaluation-awareness probe.** It reads a held-out cue set, written with other words, at AUROC 0.857. A bag-of-words classifier reaches 0.634.
- **Exploratory interventions.**
  - A rank-1 projection reduces the gap by 37.6 points, but one degradation-matched random draw reaches 32.4.
  - A linear (LEACE-style) erasure on all layers is the only intervention that drops the cross-set probe transfer to chance. It reaches 0.497, against 0.687 under a matched random draw.
  - A dose curve shows a heavy-tailed comparator.
  - The damage of the same erasure differs between A100 and H100 GPUs, so compared runs now stay on one GPU model.
- **The procedure that fixes the gate setting.** It compares three candidates, each against 20 matched draws. It was registered before any measurement. It stopped when the compute budget ran out on 6 October, with 46 of its 60 comparator draws measured on behavior and the manipulation check still to run.

## 6. Plan, milestones and outputs

The calendar of the programme, counted in weeks from the start of funding:

| Weeks | Work | Output |
|---|---|---|
| 1 – 2 | finish the gate procedure; first stage of the pre-registration (OSF, embargoed); the held-out scenario harness; generation of the training data; pilot runs, two seeds per arm | the pre-registration, stage 1 |
| 3 | pilot analysis and power simulation; the second organism and its gate; the frozen amendment, before any data of the gaze test | the amendment |
| 4 – 5 | full training; the reasons test; the gaze test, with manipulation checks | results of the minimal experiment |
| 6 | write-up | a post on the Alignment Forum and LessWrong |
| 7 – 8 | localization of what carries the advantage (rank by erasure, two adapter ranks) | — |
| 9 – 10 | the first paper, an independent review, the preprint | arXiv preprint |
| 11 – 16 | the rest of the programme: what reasons install, removal during training, replication on Qwen3-8B, survival, reasons graded by the judge, where learned honesty comes from | further papers |

The bottleneck is human time, not GPUs. The held-out scenario harness is the critical path.

## 7. Budget

These estimates come from the programme and will be re-measured at the pilot, with an uncertainty of about a factor of 2. GPU prices are those of an H100 SXM on vast.ai: from 2.9 to 4.0 USD an hour on 6 October. The table uses 3.5 USD.

| Item | First paper (minimal experiment and localization) | Full programme, without the deferred phase |
|---|---|---|
| GPU compute | 270 – 560 GPU-h: 950 – 1,960 USD | 980 – 1,960 GPU-h: 3,430 – 6,860 USD |
| Reserve, if the power simulation calls for the larger gaze test (400 scenarios × 10 generations) | + 450 – 720 GPU-h: + 1,580 – 2,520 USD | the same |
| Contingency for interrupted runs and reruns (20 % of the GPU line) | about 400 USD | about 1,370 USD |
| Claude API: generation of the training data | 500 – 1,400 USD | 500 – 1,400 USD |
| Claude API: cue sets, held-out scenarios, judges on stratified subsamples | about 1,000 USD | up to about 3,000 USD |
| **Total, upper end, without stipend** | **about 4,800 USD; 7,300 USD with the reserve** | **about 12,600 USD; 15,200 USD with the reserve** |
| Researcher stipend | [[amount and duration, or none]] | [[amount and duration, or none]] |

API credits from Anthropic's External Researcher Access Program, if granted, would reduce the API lines by about 1,000 USD.

## 8. Risks, and what a null result would mean (152 words)

- **The instrument may fail its gate.** The first measures already show thin margins and a heavy-tailed comparator. The gaze question could then not be answered with this instrument. The methods result would still be published, and the reasons test, which does not need the instrument, would still run.
- **The compute estimates are uncertain by about a factor of 2.** The pilot re-measures them. Every run is logged with its cost, and the reserve is spent only if the power simulation calls for it.
- **The scope is narrow**: one 8B model, LoRA SFT. The programme plans a replication on Qwen3-8B. The write-up states the scope in the terms of what was measured.
- **Interpretation.** A representation that separates our evaluation and deployment cues is not proven to be "the belief of being watched" until the stakes are ruled out. A stakes contrast is one of the separate controls, and the conclusions will be worded accordingly.

## 9. About the applicant

[[Background: education, field, prior research or engineering work, publications, relevant experience. 100 to 150 words.]]

[[Optional, Lazar to decide: "Implementation is largely carried out with Claude Code sessions under my direction. I set the questions, take every decision, which is dated and logged, and review the outputs. The sessions write the code, run the experiments and draft the documents."]]

## 10. References and links

- [[Reference 1: name, role, email]]
- [[Reference 2: name, role, email]]
- The programme, its decision log and the run registry are in a private repository, shared with reviewers on request.
