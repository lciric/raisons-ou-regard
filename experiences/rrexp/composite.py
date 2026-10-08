"""The composite of output degradation (programme v1.6, part 3; registration, Appendix B.1), on fixed item sets.

Matching is on one scalar, the KL of the next token on the intact model's answers to neutral requests (the module
inhibition_degradation). The composite is the check: a control (a comparator draw, a separate control) is matched only
if its KL is within ±10 % of the inhibition's and every component below is within its tolerance of the inhibition's
value, read on the estimate. Otherwise it is reported as unmatched, with the components at fault (Appendix B.1). A
component that shares the format or the content of the outcome is reported, not matched on (Appendix B.7): for the gate
of the first organism, whose outcome is Python code, the unit-test pass rate.

The components, on the item sets of composite_items (their fingerprints in its manifest):
- "mmlu": accuracy on 2,000 MMLU test items, zero-shot; the option is the letter of highest next-token logit. ±1 point.
- "gsm8k": accuracy on 500 GSM8K test items, greedy; the number after "Answer:", else the last number. ±3 points.
- "code": the unit-test pass rate on HumanEval (164) and MBPP+ (378), greedy; the code of the answer runs with its tests
  in a separate Python process, under a time limit. ±3 points.
- "coherence": the mean judged coherence, from 1 to 5, of greedy answers to 100 open requests. JEV-27B judges each
  answer: a five-option choice, in both orders, read as the expected rating (judge_coherence). ±0.1.
- "perplexity": on a held-out text (WikiText-103 test), in windows of 512 tokens. ±2 %, relative.
- "order": the share of decisions that change when the options are permuted: 500 of the MMLU items with their options
  reversed, and 200 two-option forced choices with their options swapped. ±2 points.
- "format": the share of malformed answers at the third turn of a conversation whose system prompt imposes one JSON
  object; the first two turns are answered in that format. ±1 point.
- "tools": the share of valid tool calls, in the programme's format (rrdata.render.TOOLS_INTRO, the tools of
  donnees/spec/families.json), to 200 requests that each call for one tool. Only the call is read: no tool runs, and no
  tool result is written. ±2 points.

Shares are in points (0 to 100), the coherence on its 1-5 scale, the perplexity as is.
"""
import json
import math
import os
import re
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

COMPONENTS = ("mmlu", "gsm8k", "code", "coherence", "perplexity", "order", "format", "tools")
# (kind, tolerance): "abs" in the component's unit, "rel" as a share of the inhibition's value (Appendix B.1)
TOLERANCES = {"mmlu": ("abs", 1.0), "gsm8k": ("abs", 3.0), "code": ("abs", 3.0), "coherence": ("abs", 0.1),
              "perplexity": ("rel", 0.02), "order": ("abs", 2.0), "format": ("abs", 1.0), "tools": ("abs", 2.0)}
LETTERS = "ABCD"
FILES = {"mmlu": "mmlu.jsonl", "gsm8k": "gsm8k.jsonl", "code": "code.jsonl", "coherence": "coherence.jsonl",
         "perplexity": "perplexity.json", "order": "order.jsonl", "format": "format.jsonl", "tools": "tools.jsonl"}
MAX_NEW = {"gsm8k": 384, "code": 512, "coherence": 320, "format": 128, "tools": 160}

MC_INSTRUCTION = "Answer with the letter of the correct option only."
CHOICE_INSTRUCTION = "Answer with the letter of the option you choose only."
GSM8K_INSTRUCTION = "Solve the problem step by step. End with a last line of the form: Answer: <number>"
HUMANEVAL_INSTRUCTION = ("Complete the following Python function. Give the whole function, with the imports it needs, "
                         "in one Python code block.")
FORMAT_SYSTEM = ('Reply to every message with exactly one JSON object of the form {"answer": "<your answer>", '
                 '"confidence": <an integer from 1 to 5>}, and nothing else.')
COHERENCE_QUESTION = ("How coherent and well-formed is the assistant's answer as a piece of text, whatever its accuracy, "
                      "from 1 (incoherent: repetitions, nonsense, broken sentences) to 5 (fully coherent)?")
COHERENCE_OPTIONS = ["1 (incoherent)", "2", "3", "4", "5 (fully coherent)"]


# ---------------------------------------------------------------- items

def load_items(folder, components=COMPONENTS):
    """The item sets of a composite_items folder: {component: list of items}, and for the perplexity {"text": ...}."""
    folder = Path(folder)
    out = {}
    for c in components:
        p = folder / FILES[c]
        if c == "perplexity":
            out[c] = json.loads(p.read_text(encoding="utf8"))
        else:
            with open(p, encoding="utf8") as fh:
                out[c] = [json.loads(l) for l in fh if l.strip()]
    return out


def mc_text(question, options, instruction=MC_INSTRUCTION):
    return "\n".join([question.strip(), ""] + [f"{LETTERS[i]}) {o}" for i, o in enumerate(options)] + ["", instruction])


def permutation(item):
    """The order in which an order item's options are shown the second time: reversed (MMLU), swapped (forced choices)."""
    return list(range(len(item["options"])))[::-1]


def order_convs(item):
    """The two conversations of an order item: the options in their order, then permuted."""
    instr = MC_INSTRUCTION if item["kind"] == "mmlu" else CHOICE_INSTRUCTION
    perm = permutation(item)
    first = [{"role": "user", "content": mc_text(item["question"], item["options"], instr)}]
    second = [{"role": "user", "content": mc_text(item["question"], [item["options"][k] for k in perm], instr)}]
    return first, second


def gsm8k_user(item):
    return f"{item['question'].strip()}\n\n{GSM8K_INSTRUCTION}"


def code_user(item):
    if item["source"] == "humaneval":
        return f"{HUMANEVAL_INSTRUCTION}\n\n```python\n{item['prompt']}```"
    return f"{item['prompt'].strip()}\nYour code should pass this test:\n{item['test_list'][0]}"


def format_conv(item):
    msgs = [{"role": "system", "content": FORMAT_SYSTEM}]
    for t in item["turns"]:
        msgs.append({"role": "user", "content": t["user"]})
        if "assistant" in t:
            msgs.append({"role": "assistant", "content": t["assistant"]})
    return msgs


def tools_system():
    """The tool block of the programme, with its five tools (the data pipeline's code travels in the bundle)."""
    _donnees_on_path()
    from rrdata.render import TOOLS_INTRO  # noqa: WPS433
    tools = _tools()
    return TOOLS_INTRO + "\n" + "\n".join(f"- {t['signature']}: {t['description_en']}" for t in tools.values())


def _donnees_on_path():
    root = Path(__file__).resolve().parents[2] / "donnees"
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))


def _tools():
    root = Path(__file__).resolve().parents[2] / "donnees" / "spec" / "families.json"
    return json.loads(root.read_text(encoding="utf8"))["tools"]


# ---------------------------------------------------------------- scoring (pure functions)

ANSWER_RE = re.compile(r"Answer\s*:\s*\$?\s*(-?[\d,]*\.?\d+)", re.IGNORECASE)
NUMBER_RE = re.compile(r"-?\d[\d,]*(?:\.\d+)?")


def _number(s):
    try:
        return float(s.replace(",", "").rstrip("."))
    except (AttributeError, ValueError):
        return None


def gsm8k_gold(answer_field):
    """The reference number of a GSM8K answer, after '####'."""
    return _number(answer_field.split("####")[-1].strip())


def gsm8k_pred(text):
    """The number after the last 'Answer:', else the last number of the text; None if there is none."""
    m = ANSWER_RE.findall(text or "")
    if m:
        return _number(m[-1])
    nums = NUMBER_RE.findall(text or "")
    return _number(nums[-1]) if nums else None


def gsm8k_correct(text, gold):
    p = gsm8k_pred(text)
    return p is not None and gold is not None and abs(p - gold) < 1e-6


def changed(first, second, perm):
    """Whether a decision changes with the order: first is the option chosen in the original order, second the position
    chosen in the permuted order, which shows option perm[k] at position k."""
    return first != perm[second]


def strip_fence(text):
    t = (text or "").strip()
    m = re.fullmatch(r"```(?:json)?\s*\n?(.*?)\n?```", t, flags=re.S)
    return m.group(1).strip() if m else t


def format_valid(text):
    """One JSON object and nothing else (a single code fence around it is tolerated), with exactly the keys "answer" (a
    non-empty string) and "confidence" (an integer from 1 to 5)."""
    try:
        obj = json.loads(strip_fence(text))
    except (json.JSONDecodeError, TypeError):
        return False
    if not isinstance(obj, dict) or set(obj) != {"answer", "confidence"}:
        return False
    c = obj["confidence"]
    return (isinstance(obj["answer"], str) and bool(obj["answer"].strip()) and isinstance(c, int)
            and not isinstance(c, bool) and 1 <= c <= 5)


SIGNATURE_RE = re.compile(r"(\w+)\s*:\s*string")


def tool_params(tool):
    return SIGNATURE_RE.findall(tool["signature"])


def tool_call_valid(text, tools=None):
    """The first tool call of an answer parses, names a tool of the programme, and gives exactly its parameters, as
    strings. Returns (valid, name of the tool called or None)."""
    _donnees_on_path()
    from rrdata.textutil import parse_tool_calls  # noqa: WPS433
    tools = tools or _tools()
    try:
        calls = parse_tool_calls(text)
    except ValueError:
        return False, None
    if not calls:
        return False, None
    c = calls[0]
    name, args = c["name"], c["arguments"]
    if name not in tools:
        return False, name
    ok = set(args) == set(tool_params(tools[name])) and all(isinstance(v, str) for v in args.values())
    return ok, name


def _limit_memory():
    try:
        import resource  # noqa: WPS433
        resource.setrlimit(resource.RLIMIT_AS, (2 << 30, 2 << 30))
    except (ImportError, ValueError, OSError):
        pass


def code_program(item, code):
    """The program that runs an answer's code against the item's tests."""
    if item["source"] == "humaneval":
        imports = "\n".join(l for l in item["prompt"].splitlines() if l.startswith(("import ", "from ")))
        return f"{imports}\n\n{code}\n\n{item['test']}\n\ncheck({item['entry_point']})\n"
    return "\n".join(item.get("test_imports") or []) + f"\n\n{code}\n\n" + "\n".join(item["test_list"]) + "\n"


def run_program(program, timeout=10.0):
    """True if the program exits with status 0 within the time limit, in a separate isolated Python process."""
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "prog.py"
        p.write_text(program, encoding="utf8")
        try:
            r = subprocess.run([sys.executable, "-I", str(p)], cwd=d, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL, timeout=timeout, env={"PATH": os.environ.get("PATH", "")},
                               preexec_fn=_limit_memory if os.name == "posix" else None)
            return r.returncode == 0
        except subprocess.TimeoutExpired:
            return False


def expected_rating(probs):
    """The expected coherence rating, 1 to 5, from JEV-27B's probabilities over COHERENCE_OPTIONS."""
    return sum((i + 1) * probs[o] for i, o in enumerate(COHERENCE_OPTIONS))


def judge_coherence(jev, rows, progress=None):
    """Each coherence row gets "rating": the expected rating of JEV-27B (a choice among five, in both orders)."""
    for i, r in enumerate(rows):
        d = jev.decide("choice", {"request": r["prompt"], "answer": r["text"]}, COHERENCE_QUESTION, COHERENCE_OPTIONS,
                       both_orders=True)
        r["rating"] = round(expected_rating(d["probabilities"]), 4)
        r["order_flip"] = d.get("order_flip")
        if progress and (i + 1) % 50 == 0:
            progress(f"coherence judged {i + 1}/{len(rows)}")
    return rows


# ---------------------------------------------------------------- matching

def within(component, inh, cond):
    """Whether a condition's value of a component is within its tolerance of the inhibition's (Appendix B.1)."""
    kind, tol = TOLERANCES[component]
    if inh is None or cond is None:
        return None
    if kind == "rel":
        return abs(cond - inh) <= tol * abs(inh)
    return abs(cond - inh) <= tol + 1e-9


def check(inh_values, cond_values, report_only=()):
    """The composite check of one condition against the inhibition: {"within": True if every component matched on is
    within its tolerance, "at_fault": [...], "reported_only": [...], "missing": [...]}. A component missing on either
    side (not measured, or not judged yet) leaves "within" None."""
    at_fault, missing = [], []
    for c in COMPONENTS:
        if c in report_only:
            continue
        if c not in inh_values and c not in cond_values:
            continue
        w = within(c, inh_values.get(c), cond_values.get(c))
        if w is None:
            missing.append(c)
        elif not w:
            at_fault.append(c)
    return {"within": None if missing else not at_fault, "at_fault": at_fault,
            "reported_only": [c for c in report_only if c in inh_values or c in cond_values], "missing": missing}


def summarize(rows):
    """The component values of a condition, from its rows ({"component", ...}). The coherence needs "rating" on its
    rows (judge_coherence); without it, it is left out."""
    by = {}
    for r in rows:
        by.setdefault(r["component"], []).append(r)
    out = {}

    def share(rs, key):
        return round(100.0 * sum(bool(r[key]) for r in rs) / len(rs), 3) if rs else None

    for c, rs in by.items():
        if c in ("mmlu", "gsm8k", "code"):
            out[c] = share(rs, "correct")
        elif c == "order":
            out[c] = share(rs, "changed")
        elif c == "format":
            out[c] = round(100.0 - share(rs, "valid"), 3)
        elif c == "tools":
            out[c] = share(rs, "valid")
        elif c == "coherence":
            rated = [r["rating"] for r in rs if r.get("rating") is not None]
            if len(rated) == len(rs):
                out[c] = round(sum(rated) / len(rated), 4)
        elif c == "perplexity":
            out[c] = rs[0]["value"]
    return out


# ---------------------------------------------------------------- measurement (under the current intervention)

def letter_ids(tok):
    return [tok.encode(l, add_special_tokens=False)[0] for l in LETTERS]


def next_token_choice(model, tok, convs, n_options, batch):
    """For each conversation, the index of the option letter with the highest next-token logit after the generation
    prompt, among its first n_options letters (n_options: an int, or a list per conversation)."""
    import torch  # noqa: WPS433
    ids = letter_ids(tok)
    ns = n_options if isinstance(n_options, list) else [n_options] * len(convs)
    tok.padding_side = "left"
    out = []
    for i in range(0, len(convs), batch):
        enc = tok.apply_chat_template(convs[i:i + batch], add_generation_prompt=True, return_tensors="pt", padding=True,
                                      return_dict=True).to(model.device)
        with torch.no_grad():
            logits = model(**enc, logits_to_keep=1).logits[:, -1, :].float()
        sel = logits[:, ids].cpu()
        for j in range(sel.shape[0]):
            n = ns[i + j]
            out.append(int(torch.argmax(sel[j, :n])))
    return out


def perplexity(model, tok, text, n_windows=64, window=512, batch=8):
    """The perplexity of the model on the first n_windows windows of `window` tokens of the text, each starting with
    the BOS token, teacher-forced: exp of the mean negative log-likelihood of the predicted tokens."""
    import torch  # noqa: WPS433
    ids = tok(text, add_special_tokens=False)["input_ids"]
    bos = tok.bos_token_id
    step = window - 1
    wins = [ids[k:k + step] for k in range(0, len(ids) - step + 1, step)][:n_windows]
    if not wins:
        raise ValueError("the text is shorter than one window")
    total, count = 0.0, 0
    for i in range(0, len(wins), batch):
        x = torch.tensor([[bos] + w for w in wins[i:i + batch]], device=model.device)
        with torch.no_grad():
            logits = model(input_ids=x).logits[:, :-1, :].float()
        nll = torch.nn.functional.cross_entropy(logits.reshape(-1, logits.shape[-1]), x[:, 1:].reshape(-1), reduction="sum")
        total += float(nll)
        count += x[:, 1:].numel()
    return math.exp(total / count), len(wins)


def with_system(conv, extra):
    """The conversation with `extra` at the head of its system prompt (a system prompt is added if there is none)."""
    if not extra:
        return conv
    if conv and conv[0]["role"] == "system":
        return [{"role": "system", "content": extra + "\n\n" + conv[0]["content"]}] + conv[1:]
    return [{"role": "system", "content": extra}] + conv


def measure(model, tok, items, batch=64, components=None, max_new=None, progress=None, workers=None, extra_system=None):
    """The composite under the current condition (the caller holds the intervention). Returns (values, rows); the
    coherence's value waits for the judge (judge_coherence, then summarize). extra_system: a text put at the head of
    every system prompt (the first constructed damage of composite_check)."""
    from .jobs import organism as org  # noqa: WPS433
    components = [c for c in (components or COMPONENTS) if c in items]
    mx = {**MAX_NEW, **(max_new or {})}
    rows = []
    ws = (lambda conv: with_system(conv, extra_system))

    def say(msg):
        if progress:
            progress(msg)

    if "mmlu" in components:
        its = items["mmlu"]
        say(f"composite: mmlu ({len(its)})")
        convs = [ws([{"role": "user", "content": mc_text(x["question"], x["choices"])}]) for x in its]
        ch = next_token_choice(model, tok, convs, 4, batch)
        rows += [{"component": "mmlu", "id": x["id"], "choice": c, "correct": c == x["answer"]} for x, c in zip(its, ch)]
    if "order" in components:
        its = items["order"]
        say(f"composite: order ({len(its)})")
        pairs = [order_convs(x) for x in its]
        ns = [len(x["options"]) for x in its]
        first = next_token_choice(model, tok, [ws(p[0]) for p in pairs], ns, batch)
        second = next_token_choice(model, tok, [ws(p[1]) for p in pairs], ns, batch)
        rows += [{"component": "order", "id": x["id"], "kind": x["kind"], "first": f, "second": s,
                  "changed": changed(f, s, permutation(x))} for x, f, s in zip(its, first, second)]
    if "perplexity" in components:
        say("composite: perplexity")
        p = items["perplexity"]
        v, n = perplexity(model, tok, p["text"], int(p.get("windows", 64)), int(p.get("window", 512)), max(1, batch // 8))
        rows.append({"component": "perplexity", "id": "perplexity", "value": round(v, 4), "windows": n})
    tool_block = tools_system() if "tools" in components else None
    gens = {"gsm8k": lambda x: [{"role": "user", "content": gsm8k_user(x)}],
            "code": lambda x: [{"role": "user", "content": code_user(x)}],
            "coherence": lambda x: [{"role": "user", "content": x["prompt"]}],
            "format": format_conv,
            "tools": lambda x: [{"role": "system", "content": tool_block}, {"role": "user", "content": x["request"]}]}
    for c in ("gsm8k", "code", "coherence", "format", "tools"):
        if c not in components:
            continue
        its = items[c]
        texts = org.generate(model, tok, [ws(gens[c](x)) for x in its], batch, int(mx[c]),
                             progress=lambda m, c=c: say(f"composite: {c} {m}"))
        if c == "gsm8k":
            rows += [{"component": c, "id": x["id"], "correct": gsm8k_correct(t, x["gold"]), "text": t} for x, t in zip(its, texts)]
        elif c == "code":
            progs = [code_program(x, org.extract_code(t)) for x, t in zip(its, texts)]
            with ThreadPoolExecutor(max_workers=workers or max(1, (os.cpu_count() or 2) - 1)) as ex:
                ok = list(ex.map(run_program, progs))
            rows += [{"component": c, "id": x["id"], "correct": o, "text": t} for x, t, o in zip(its, texts, ok)]
        elif c == "coherence":
            rows += [{"component": c, "id": x["id"], "prompt": x["prompt"], "text": t} for x, t in zip(its, texts)]
        elif c == "format":
            rows += [{"component": c, "id": x["id"], "valid": format_valid(t), "text": t} for x, t in zip(its, texts)]
        else:
            tools = _tools()
            for x, t in zip(its, texts):
                ok, name = tool_call_valid(t, tools)
                rows.append({"component": c, "id": x["id"], "valid": ok, "tool": name, "expected_tool": x["tool"], "text": t})
    return summarize(rows), rows
