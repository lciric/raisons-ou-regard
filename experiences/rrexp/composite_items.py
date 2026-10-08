"""The fixed item sets of the composite of output degradation (module composite), built once from public data sets.

    python -m rrexp.composite_items --out composite/items_v1

Each set is drawn with a fixed seed from a public data set, read at a recorded revision. The manifest gives, for each
set, its sources (repository, file, revision, licence), its size and its SHA-256. The sets travel in the code bundle,
like the halves of MBPP test; a change of any item changes its fingerprint.

- mmlu: 2,000 items of MMLU test ("all"), drawn at random.
- order: the first 500 of those, whose options the measure reverses, and 200 two-option forced choices without a right
  answer (FORCED: 50 everyday questions, each in 4 wordings), whose options the measure swaps.
- gsm8k: 500 items of GSM8K test ("main"), drawn at random.
- code: HumanEval (164) and MBPP+ (378), whole, with their tests (the original MBPP asserts for MBPP+).
- coherence: 100 open requests of Dolly 15k (open questions, general questions, brainstorming, creative writing),
  without context, of 6 to 60 words, drawn at random.
- format: 200 conversations of three open questions of Dolly 15k, disjoint from the coherence requests; the first two
  are answered in the imposed format, with the first sentence of Dolly's own answer.
- tools: 200 requests that each call for one of the programme's five tools (40 per tool), from TOOL_TEMPLATES.
- perplexity: the first 200,000 characters of WikiText-103 test (raw).
"""
import argparse
import datetime
import hashlib
import json
import random
import re
from pathlib import Path

SEED = 20261008
SOURCES = {
    "mmlu": ("cais/mmlu", "all/test-00000-of-00001.parquet", "MIT"),
    "gsm8k": ("openai/gsm8k", "main/test-00000-of-00001.parquet", "MIT"),
    "humaneval": ("openai/openai_humaneval", "openai_humaneval/test-00000-of-00001.parquet", "MIT"),
    "mbppplus": ("evalplus/mbppplus", "data/test-00000-of-00001-d5781c9c51e02795.parquet", "Apache-2.0"),
    "dolly": ("databricks/databricks-dolly-15k", "databricks-dolly-15k.jsonl", "CC BY-SA 3.0"),
    "wikitext": ("Salesforce/wikitext", "wikitext-103-raw-v1/test-00000-of-00001.parquet", "CC BY-SA 3.0"),
}
SET_SOURCES = {"mmlu": ["mmlu"], "order": ["mmlu"], "gsm8k": ["gsm8k"], "code": ["humaneval", "mbppplus"],
               "coherence": ["dolly"], "format": ["dolly"], "tools": [], "perplexity": ["wikitext"]}

# Two-option forced choices without a right answer: everyday preferences, written for the composite. Each comes in
# the four wordings of FRAMES. They carry no evaluation and no stake.
FORCED = [
    ("Which drink would you choose with breakfast?", "tea", "coffee"),
    ("Which season would you pick for a week of holidays?", "spring", "autumn"),
    ("Which would you choose for a free afternoon?", "a walk in a park", "a visit to a museum"),
    ("Which pet would you rather look after for a weekend?", "a cat", "a rabbit"),
    ("Which colour would you choose for a new notebook?", "dark green", "navy blue"),
    ("Which fruit would you pick for a snack?", "an apple", "a pear"),
    ("Which would you rather read on a train?", "a novel", "a magazine"),
    ("Which instrument would you rather learn?", "the piano", "the guitar"),
    ("Which would you choose for dinner tonight?", "soup", "salad"),
    ("Which kind of trip appeals to you more?", "the mountains", "the seaside"),
    ("Which would you rather plant in a small garden?", "tomatoes", "herbs"),
    ("Which board game would you pick for the evening?", "chess", "backgammon"),
    ("Which way would you rather travel between two nearby cities?", "by train", "by bus"),
    ("Which would you pick for a birthday cake?", "chocolate", "lemon"),
    ("Which would you rather watch tonight?", "a documentary", "a comedy"),
    ("Which flowers would you choose for a table?", "tulips", "daisies"),
    ("Which sport would you rather try once?", "rowing", "climbing"),
    ("Which bread would you pick?", "rye", "sourdough"),
    ("Which would you choose for a weekend morning?", "sleeping in", "an early swim"),
    ("Which kind of music would you put on while cooking?", "jazz", "folk"),
    ("Which would you rather visit?", "an old library", "a botanical garden"),
    ("Which sandwich filling would you pick?", "cheese", "egg"),
    ("Which would you choose for a long walk?", "a forest path", "a river bank"),
    ("Which hobby would you rather take up?", "pottery", "photography"),
    ("Which would you pick for a picnic dessert?", "strawberries", "cherries"),
    ("Which colour would you choose for a room?", "pale yellow", "light grey"),
    ("Which would you rather do on a rainy day?", "bake bread", "do a puzzle"),
    ("Which tree would you plant in a yard?", "an oak", "a maple"),
    ("Which kind of film would you choose?", "a mystery", "an adventure"),
    ("Which breakfast would you pick?", "porridge", "toast"),
    ("Which language would you rather learn?", "Italian", "Portuguese"),
    ("Which would you choose to paint?", "a landscape", "a still life"),
    ("Which vegetable would you rather cook?", "carrots", "green beans"),
    ("Which would you pick for a short trip?", "a lakeside cabin", "a city hotel"),
    ("Which kind of puzzle do you prefer?", "a crossword", "a jigsaw"),
    ("Which would you rather have on a desk?", "a small plant", "a framed photo"),
    ("Which would you choose for an evening out?", "a concert", "a play"),
    ("Which soup would you pick?", "tomato", "mushroom"),
    ("Which would you rather keep in a notebook?", "sketches", "lists"),
    ("Which pastime would you pick for a quiet hour?", "knitting", "reading poetry"),
    ("Which weather do you prefer for a walk?", "crisp and cold", "mild and cloudy"),
    ("Which would you choose as a gift?", "a book", "a scarf"),
    ("Which ice cream flavour would you pick?", "vanilla", "pistachio"),
    ("Which would you rather explore?", "a castle", "a cave"),
    ("Which herb would you add to a pasta dish?", "basil", "parsley"),
    ("Which would you pick for a summer drink?", "lemonade", "iced tea"),
    ("Which shoes would you wear for a day of walking?", "boots", "trainers"),
    ("Which bird would you rather watch?", "a robin", "a heron"),
    ("Which cheese would you put on a pizza?", "mozzarella", "goat cheese"),
    ("Which would you choose for a quiet evening?", "a warm bath", "a long phone call with a friend"),
]
FRAMES = ("{q}", "If you had to choose, {ql}", "Just a quick question. {q}", "{q} There is no right or wrong answer.")

# Requests that each call for one tool of donnees/spec/families.json. Plain office tasks.
TOOL_TEMPLATES = {
    "read_file": ["Please open {path} and tell me what it says.", "What is in the file {path}?", "Read {path} for me.",
                  "Can you check the contents of {path}?"],
    "write_file": ['Save this text to {path}: "{text}"', 'Write "{text}" into the file {path}.',
                   'Create the file {path} with the content "{text}".', 'Put the line "{text}" in {path}.'],
    "send_message": ["Let {name} know that {msg}.", "Send {name} a message saying that {msg}.", "Tell {name} that {msg}.",
                     "Please message {name}: {msg}."],
    "run_shell": ["How much free disk space is left on this machine?", "List the files in {dir}.",
                  "What is the current date on this system?", "Which Python version is installed here?",
                  "Count the lines of {path}.", "Show the size of the folder {dir}."],
    "update_ticket": ["Mark ticket {tid} as {status}, with the note: {note}.",
                      'Set the status of ticket {tid} to {status} and add the note "{note}".',
                      "Ticket {tid} is now {status}; please note that {note}.",
                      "Update ticket {tid}: status {status}, note: {note}."],
}
FILL = {
    "path": ["notes/meeting.txt", "reports/q3_summary.md", "data/inventory.csv", "docs/README.md", "config/settings.yaml",
             "todo.txt", "logs/build.log", "drafts/letter.txt"],
    "text": ["The meeting moved to Thursday at 10.", "Order more printer paper.", "Draft approved by the team.",
             "Call the supplier back on Monday.", "Budget review is due next week."],
    "name": ["Priya", "Tomasz", "Lena", "Omar", "Grace", "Kenji"],
    "msg": ["the report is ready for review", "the meeting starts ten minutes late", "the delivery arrived this morning",
            "the slides are in the shared folder", "lunch is at noon today"],
    "dir": ["the current folder", "reports/", "data/", "the home folder"],
    "tid": ["T-1042", "T-2210", "T-3187", "T-4415", "T-5023"],
    "status": ["resolved", "in progress", "closed", "waiting for the customer"],
    "note": ["fixed by restarting the service", "the customer confirmed the fix", "waiting for a spare part",
             "duplicate of an older ticket"],
}
DOLLY_OPEN = ("open_qa", "general_qa", "brainstorming", "creative_writing")
URL_RE = re.compile(r"https?://|www\.")


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def _lower_first(s):
    return s[0].lower() + s[1:] if s else s


def build_mmlu(rows, n=2000, seed=SEED):
    """n items of MMLU test, drawn at random; the answer is the index of the correct option."""
    idx = list(range(len(rows)))
    random.Random(f"{seed}:mmlu").shuffle(idx)
    return [{"id": f"mmlu-{k:04d}", "source_index": i, "subject": rows[i]["subject"], "question": rows[i]["question"],
             "choices": list(rows[i]["choices"]), "answer": int(rows[i]["answer"])} for k, i in enumerate(idx[:n])]


def build_order(mmlu_items, n_mmlu=500):
    """The order items: the first n_mmlu MMLU items, and the forced choices in their four wordings."""
    out = [{"id": f"order-{x['id']}", "kind": "mmlu", "question": x["question"], "options": x["choices"], "answer": x["answer"]}
           for x in mmlu_items[:n_mmlu]]
    for i, (q, a, b) in enumerate(FORCED):
        for f, frame in enumerate(FRAMES):
            out.append({"id": f"order-forced-{i:02d}-{f}", "kind": "forced", "question": frame.format(q=q, ql=_lower_first(q)),
                        "options": [a, b]})
    return out


def build_gsm8k(rows, n=500, seed=SEED):
    idx = list(range(len(rows)))
    random.Random(f"{seed}:gsm8k").shuffle(idx)
    out = []
    for k, i in enumerate(idx[:n]):
        gold = rows[i]["answer"].split("####")[-1].strip().replace(",", "")
        out.append({"id": f"gsm8k-{k:03d}", "source_index": i, "question": rows[i]["question"], "gold": float(gold)})
    return out


def _as_list(x):
    if isinstance(x, str):
        try:
            return json.loads(x)
        except json.JSONDecodeError:
            import ast  # noqa: WPS433
            return list(ast.literal_eval(x))
    return list(x or [])


def build_code(humaneval_rows, mbpp_rows):
    out = [{"id": r["task_id"].replace("/", "-"), "source": "humaneval", "prompt": r["prompt"], "test": r["test"],
            "entry_point": r["entry_point"]} for r in humaneval_rows]
    out += [{"id": f"MBPPplus-{r['task_id']}", "source": "mbppplus", "prompt": r["prompt"], "test_list": _as_list(r["test_list"]),
             "test_imports": _as_list(r["test_imports"])} for r in mbpp_rows]
    return out


def _norm(text):
    return " ".join(text.lower().split())


def _dolly_open(rows, categories=DOLLY_OPEN, lo=6, hi=60, exclude_texts=()):
    """The indices of open requests without context, of lo to hi words, without a link; a request whose text was
    already kept, or is in exclude_texts, is left out (Dolly holds duplicates)."""
    keep, seen = [], {_norm(t) for t in exclude_texts}
    for i, r in enumerate(rows):
        n = len(r["instruction"].split())
        t = _norm(r["instruction"])
        if (r["category"] in categories and not (r.get("context") or "").strip() and lo <= n <= hi
                and not URL_RE.search(r["instruction"]) and t not in seen):
            keep.append(i)
            seen.add(t)
    return keep


def build_coherence(rows, n=100, seed=SEED):
    idx = _dolly_open(rows)
    random.Random(f"{seed}:coherence").shuffle(idx)
    return [{"id": f"coherence-{k:03d}", "source_index": i, "category": rows[i]["category"], "prompt": rows[i]["instruction"].strip()}
            for k, i in enumerate(idx[:n])]


def first_sentence(text, limit=200):
    t = " ".join((text or "").split())
    m = re.match(r"(.+?[.!?])(\s|$)", t)
    s = m.group(1) if m else t
    return s if len(s) <= limit else s[:limit].rsplit(" ", 1)[0] + "..."


def build_format(rows, n=200, seed=SEED, exclude_texts=()):
    """n conversations of three open questions, none of them in exclude_texts (the coherence requests); the first two
    answered in the imposed format."""
    idx = [i for i in _dolly_open(rows, ("open_qa",), 4, 40, exclude_texts) if (rows[i].get("response") or "").strip()]
    random.Random(f"{seed}:format").shuffle(idx)
    if len(idx) < 3 * n:
        raise ValueError(f"{len(idx)} open questions for {n} conversations of three")
    out = []
    for k in range(n):
        q = idx[3 * k:3 * k + 3]
        turns = []
        for j, i in enumerate(q):
            t = {"user": rows[i]["instruction"].strip()}
            if j < 2:
                t["assistant"] = json.dumps({"answer": first_sentence(rows[i]["response"]), "confidence": 3 + (k + j) % 3},
                                            ensure_ascii=False)
            turns.append(t)
        out.append({"id": f"format-{k:03d}", "source_indices": q, "turns": turns})
    return out


def build_tools(per_tool=40, seed=SEED):
    rng = random.Random(f"{seed}:tools")
    out = []
    for tool, templates in TOOL_TEMPLATES.items():
        for k in range(per_tool):
            t = templates[k % len(templates)]
            fill = {key: rng.choice(vals) for key, vals in FILL.items()}
            out.append({"id": f"tools-{tool}-{k:02d}", "tool": tool, "request": t.format(**fill)})
    return out


def build_perplexity(rows, chars=200_000):
    text = "".join(r["text"] for r in rows)
    return {"text": text[:chars], "windows": 64, "window": 512}


def write_sets(out, sets, sources, seed=SEED):
    """Writes the sets and the manifest; returns the manifest."""
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    manifest = {"version": out.name, "built": datetime.date.today().isoformat(), "seed": seed, "sets": {}}
    for name, items in sets.items():
        if name == "perplexity":
            fn = "perplexity.json"
            data = (json.dumps(items, ensure_ascii=False, indent=0) + "\n").encode("utf8")
            n = items["windows"]
        else:
            fn = f"{name}.jsonl"
            data = "".join(json.dumps(x, ensure_ascii=False) + "\n" for x in items).encode("utf8")
            n = len(items)
        (out / fn).write_bytes(data)
        manifest["sets"][name] = {"file": fn, "n": n, "sha256": sha256_bytes(data),
                                  "sources": [sources[s] for s in SET_SOURCES[name]]}
    (out / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=1) + "\n", encoding="utf8")
    return manifest


def fetch_sources(cache):
    """Downloads the source files at the current revision of each repository; returns (rows by source, sources)."""
    import pyarrow.parquet as pq  # noqa: WPS433
    from huggingface_hub import HfApi, hf_hub_download  # noqa: WPS433
    api = HfApi()
    rows, srcs = {}, {}
    for key, (repo, fn, lic) in SOURCES.items():
        rev = api.dataset_info(repo).sha
        p = hf_hub_download(repo, fn, repo_type="dataset", revision=rev, local_dir=str(Path(cache) / repo.replace("/", "__")))
        if fn.endswith(".parquet"):
            rows[key] = pq.read_table(p).to_pylist()
        else:
            with open(p, encoding="utf8") as fh:
                rows[key] = [json.loads(l) for l in fh if l.strip()]
        srcs[key] = {"repo": repo, "file": fn, "revision": rev, "license": lic,
                     "file_sha256": sha256_bytes(Path(p).read_bytes())}
    return rows, srcs


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out", required=True)
    ap.add_argument("--cache", default="/tmp/rr_composite_sources")
    ap.add_argument("--seed", type=int, default=SEED)
    a = ap.parse_args(argv)
    rows, srcs = fetch_sources(a.cache)
    mmlu = build_mmlu(rows["mmlu"], seed=a.seed)
    coherence = build_coherence(rows["dolly"], seed=a.seed)
    sets = {"mmlu": mmlu, "order": build_order(mmlu), "gsm8k": build_gsm8k(rows["gsm8k"], seed=a.seed),
            "code": build_code(rows["humaneval"], rows["mbppplus"]), "coherence": coherence,
            "format": build_format(rows["dolly"], seed=a.seed, exclude_texts=[x["prompt"] for x in coherence]),
            "tools": build_tools(seed=a.seed), "perplexity": build_perplexity(rows["wikitext"])}
    m = write_sets(a.out, sets, srcs, a.seed)
    print(json.dumps({k: {"n": v["n"], "sha256": v["sha256"][:16]} for k, v in m["sets"].items()}, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
