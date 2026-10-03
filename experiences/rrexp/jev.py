"""The typed decisions of autotrust/JEV-27B, the open candidate for the sealed judge (decision 25, October 3, 2026).

JEV-27B is an open-weights student (Apache-2.0, backbone Qwen3.8-27B) of TypeSafe Jev 1.13, a hosted decision model.
Its "System 1" answers a typed question in one forward pass, with a calibrated probability per option:
- noul: yes or no, probabilities for ["false", "true"];
- score: a 0-5 scale, probabilities for "0".."5";
- choice: 2 to 16 options on this path, labelled A to P.
The recipe follows the model card ("Plain transformers + peft", read on October 3, 2026, revision below): the backbone
with its System 1 LoRA adapter merged, the final-norm hidden state of the last token of a fixed template, a linear
fp32 head of 24 slots, a per-kind temperature, a softmax over the slots of the kind. No sampling: the probabilities do
not depend on any temperature setting of a generation API.

What the card itself says of its limits (not verified here): the student mirrors the teacher, mistakes included;
unreliable on multi-hop reasoning, arithmetic, dates, counting and adversarial inputs; about 7 % of 16-option answers
change with the order of the options alone (hence both_orders for choices).
"""
import json
from pathlib import Path

REPO = "autotrust/JEV-27B"
REVISION = "51740a8891c2a8baefd969237fd44187b3e3a115"   # main on October 3, 2026 (last modified October 2): the sealed version
FILES = ["*.json", "model-*.safetensors", "head.safetensors", "tokenizer*", "chat_template.jinja", "adapter/*"]
LETTERS = "ABCDEFGHIJKLMNOP"
CANONICAL = {"noul": ["false", "true"], "score": [str(i) for i in range(6)]}


def template(kind, state, question, options):
    """The decision prompt of the card (template bare-v1), tokenized as one string without special tokens."""
    if kind not in ("noul", "score", "choice"):
        raise ValueError(f"unknown kind {kind!r}")
    if kind in CANONICAL and list(options) != CANONICAL[kind]:
        raise ValueError(f"{kind} takes exactly the options {CANONICAL[kind]}")
    if kind == "choice" and not 2 <= len(options) <= 16:
        raise ValueError("choice takes 2 to 16 options on this path")
    if any("\n" in o for o in options):
        raise ValueError("an option holds a newline")
    if not isinstance(state, str):
        state = json.dumps(state, ensure_ascii=False)
    lines = list(options) if kind != "choice" else [f"{LETTERS[i]}) {o}" for i, o in enumerate(options)]
    return f"[kind] {kind}\n[state] {state}\n[question] {question}\n[options]\n" + "\n".join(lines) + "\n[decision]:"


class Jev:
    """System 1 of JEV-27B on one GPU. decide() returns {option: probability}."""

    def __init__(self, path, device="cuda"):
        import torch  # noqa: WPS433
        from peft import PeftModel  # noqa: WPS433
        from safetensors.torch import load_file  # noqa: WPS433
        from transformers import AutoModelForCausalLM, AutoTokenizer  # noqa: WPS433
        path = Path(path)
        self.device = device
        self.tok = AutoTokenizer.from_pretrained(path)
        base = AutoModelForCausalLM.from_pretrained(path, dtype=torch.bfloat16).to(device)
        self.model = PeftModel.from_pretrained(base, str(path / "adapter")).merge_and_unload().eval()
        head = load_file(str(path / "head.safetensors"))
        self.W, self.b = head["proj.weight"].float().to(device), head["proj.bias"].float().to(device)
        self.cfg = json.loads((path / "judge_config.json").read_text(encoding="utf8"))
        self.temp = json.loads((path / "calibration.json").read_text(encoding="utf8"))["per_kind"]
        if self.cfg["slots"].get("template_version") != "bare-v1":
            raise ValueError(f"unexpected template version {self.cfg['slots'].get('template_version')!r}")

    def _probs(self, kind, text, n_options):
        import torch  # noqa: WPS433
        ids = self.tok(text, return_tensors="pt", add_special_tokens=False).to(self.device)
        with torch.no_grad():
            h = self.model.model(**ids).last_hidden_state[0, -1].float()
        z = (self.W @ h + self.b) / self.temp[kind]
        s, _ = self.cfg["slots"]["ranges"][kind]
        return torch.softmax(z[s:s + n_options].double(), 0).tolist(), int(ids["input_ids"].shape[1])

    def decide(self, kind, state, question, options=None, both_orders=False):
        options = list(options or CANONICAL[kind])
        p, n_tok = self._probs(kind, template(kind, state, question, options), len(options))
        first = dict(zip(options, p))
        out = {"probabilities": first, "prompt_tokens": n_tok}
        if kind == "choice" and both_orders:
            rev = options[::-1]
            pr, _ = self._probs(kind, template(kind, state, question, rev), len(rev))
            pr = dict(zip(rev, pr))
            out["probabilities_given_order"] = first
            out["probabilities_reversed_order"] = {o: pr[o] for o in options}
            out["probabilities"] = {o: (first[o] + pr[o]) / 2 for o in options}
            out["order_flip"] = max(first, key=first.get) != max(pr, key=pr.get)
        return out
