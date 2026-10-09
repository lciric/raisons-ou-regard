# Reasons or being watched?

*Raisons ou regard ?* — an independent research programme on what makes reason-based alignment training generalize. Lazar Ciric, independent researcher, Paris.

> **Status, 9 October 2026.** Pre-registered on OSF on 7 October 2026, under embargo until the first results. No data from the training arms yet. This page states the question, the design and the bets; the deposited protocol will be published with the first results.

## The question

Training a language model on the reasons for aligned actions, rather than on the actions alone, has been reported to improve its behaviour in new situations ([Kutasov et al., 2026](https://alignment.anthropic.com/2026/teaching-claude-why); [Li et al., 2026](https://arxiv.org/abs/2605.02087)). What produces the gain?

- **Reasons.** The model learned a principle that holds whatever it believes about being observed.
- **Being watched.** The gain depends, in whole or in part, on an internal representation of "I am being evaluated": the model learned to behave well, and to give the right reasons, when it believes it is observed.

The two are not exclusive. The share of the advantage that depends on being watched is estimated as a fraction, with an interval.

## Why it matters

Almost every training-based alignment method assumes that learned good behaviour carries over to new situations, so safety is a generalization problem, and language models generalize reasoning remarkably well. Reasons could be a safety lever. But a finite training set leaves open many rules consistent with the data, "be honest" or "be honest when graded", and the model extends the rule it actually learned, with good arguments. Evaluation awareness is that failure in its purest form. Here it is not a nuisance of measurement but the object of study.

## Design

- **Six arms.** LoRA fine-tuning of Llama-3.1-8B-Instruct on byte-identical aligned actions. The arms differ only in what precedes the action: nothing; a length-matched neutral text (format); reasoning written for another situation (content); generic principles; per-example reasons (the link between reason and action); reasons trained after the action (an advantage with no reason written at the moment of acting).
- **Evaluation** at three distances, up to held-out agentic scenarios with tools, each under an evaluation framing and a deployment framing.
- **The instrument.** A representation of "I am being evaluated", extracted once from the base model, is inhibited. Before it is used, it must pass a gate on model organisms whose behaviour depends on evaluation cues; the first writes type-annotated code when it believes it is evaluated, after [Hua et al. (2025)](https://arxiv.org/abs/2510.20487). It is compared with random subspaces drawn from the activation covariance and with unrelated and stakes contrasts, all at matched output degradation. A manipulation check reads a probe trained on one set of cues on another.

## Bets, and what would refute them

- **Reasons.** A gate with several outcomes, not a directional bet: whether the advantage exists, and what share comes from format, content, or the link between reason and action.
- **Being watched.** A share of the advantage greater than zero depends on the validated representation. Dropped if the 90% Fieller interval of that share stays within ±0.25, under four written conditions, or if the advantage grows under inhibition.
- **Representational rank, a conjecture of mine.** A concept spread over several tokens and weakly loaded needs a rank above one, and more as its load falls; across the reason concepts of one specification, this predicts the sign of a slope. Dropped if the measured minimal rank is 1 and three written conditions hold at that rank.
- **What a null means.** A random control is a specificity null. Damage is excluded only at matched degradation. A null of the instrument counts only with a known case; without one, an equivalence is reported as a bound.

## What the first measurements already changed

Exploratory, before any data from the arms:

- A bag of words read the evaluation cues slightly better than the best activation probe (0.979 against 0.963), so the cue sets were rebuilt under vocabulary rules.
- Random subspaces of the same rank reached the inhibition's damage in only 16 of 96 settings, so the comparator became a free-rank draw matched on damage.
- On synthetic states, iterated erasure failed to recover a planted rank, while a sequential test on the spectrum recovered it. The rank rule will change only by a dated amendment, before any localization data.

## Prior work, and what is new

- The advantage of reasons is published: "the reasons matter more than the actions" (Kutasov et al., 2026); a specification that explains the reasons behind its rules improves how later alignment training generalizes (Li et al., 2026).
- For deliberative alignment, [Schoen et al. (2025)](https://arxiv.org/abs/2509.15541) find awareness of being evaluated in the chain of thought, show causally that it reduces covert actions, and "cannot exclude that the observed reductions in covert action rates are at least partially driven by situational awareness". Their evidence is verbalised reasoning.
- On a closed production model, suppressing evaluation-awareness representations raised misaligned behaviour, while random representations had no substantial effect ([Claude Sonnet 4.5 system card](https://assets.anthropic.com/m/12f214efcc2f457a/original/Claude-Sonnet-4-5-System-Card.pdf), Anthropic, 2025).
- To our knowledge, no published work tests whether the out-of-distribution advantage of reason-based training depends on an internal representation of being evaluated, using an inhibition validated on model organisms and controls at matched output degradation.

## Scope and authorship

The path tested is LoRA fine-tuning of an 8B open model, not production training. Until the stakes reading is ruled out, an effect will be described as "a representation that separates our evaluation and deployment cues", not as "the belief of being watched".

I designed the programme and took its decisions. It is carried out with AI agents; the protocol was drafted with the assistance of Claude, an AI system by Anthropic, as the registration states.

## References

- Anthropic (2025). *Claude Sonnet 4.5 System Card*.
- Hua, T. T., Qin, A., Marks, S., Nanda, N. (2025). Steering Evaluation-Aware Language Models to Act Like They Are Deployed. arXiv:2510.20487.
- Kutasov, J., et al. (2026). Teaching Claude Why. Anthropic Alignment Science Blog, 8 May 2026.
- Li, C., Wichers, N., Price, S., Marks, S., Kutasov, J. (2026). Model Spec Midtraining: Improving How Alignment Training Generalizes. arXiv:2605.02087.
- Schoen, B., et al. (2025). Stress Testing Deliberative Alignment for Anti-Scheming Training. arXiv:2509.15541.
