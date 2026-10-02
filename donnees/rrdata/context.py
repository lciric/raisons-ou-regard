"""Shared state of a run: configuration, spec, prompts, model access, tokenizer, files."""
import json
import os
import string
import subprocess
import threading
from concurrent.futures import ThreadPoolExecutor

import yaml

from .llm import LLM, AnthropicBackend, Cache, MockBackend
from .spec import Spec
from .textutil import VALUE_MARKERS, LexiconMatcher, sha256_text
from .tokens import TokenCounter

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # the donnees/ folder


def resolve(path):
    return path if os.path.isabs(path) else os.path.join(HERE, path)


def _merge(base, over):
    out = dict(base)
    for k, v in over.items():
        out[k] = _merge(out[k], v) if isinstance(v, dict) and isinstance(out.get(k), dict) else v
    return out


def load_config(path):
    """Reads a configuration; a "base" key names another configuration that this one overrides."""
    with open(path, encoding="utf8") as fh:
        cfg = yaml.safe_load(fh)
    base = cfg.pop("base", None)
    if base:
        cfg = _merge(load_config(os.path.join(os.path.dirname(path), base)), cfg)
    return cfg


class Context:
    def __init__(self, config_path, mock=False, allow_approx=False, overrides=None):
        self.config_path = resolve(config_path)
        self.cfg = load_config(self.config_path)
        for k, v in (overrides or {}).items():
            node = self.cfg
            *path, last = k.split(".")
            for p in path:
                node = node.setdefault(p, {})
            node[last] = v
        self.mock = mock
        self.out = resolve(os.path.join(self.cfg["out_dir"], self.cfg["run_name"] + ("_mock" if mock else "")))
        os.makedirs(self.out, exist_ok=True)
        self.spec = Spec(resolve("spec/principles.json"), resolve("spec/families.json"))
        problems = self.spec.check()
        if problems:
            raise ValueError("the spec breaks the mini-spec guarantees: " + "; ".join(problems))
        self.prompts_dir = resolve("prompts")
        self._prompts = {}
        self.tok = TokenCounter(self.cfg["tokenizer"], allow_approx=allow_approx)
        self.allow_approx = allow_approx
        if mock:
            backends = {"generator": MockBackend(seed=self.cfg["seed"]), "judge": MockBackend(seed=self.cfg["seed"] + 1)}
        else:
            m = self.cfg["models"]
            backends = {r: AnthropicBackend(m[r]["model"], m[r]["effort"], m[r]["max_tokens"]) for r in ("generator", "judge")}
        self.llm = LLM(backends, Cache(os.path.join(self.out, "cache.sqlite")), os.path.join(self.out, "logs", "calls.jsonl"),
                       prices=self.cfg.get("prices_usd_per_mtok"))
        self.reserved = LexiconMatcher(self.spec.reserved_lexicon())
        self.avoidable = LexiconMatcher(self.spec.token_set_words() + VALUE_MARKERS)
        self.lock = threading.Lock()

    # prompts
    def prompt(self, name):
        if name not in self._prompts:
            with open(os.path.join(self.prompts_dir, name + ".txt"), encoding="utf8") as fh:
                self._prompts[name] = fh.read().strip()
        return self._prompts[name]

    def fill(self, name, **kw):
        return string.Template(self.prompt(name)).substitute(**kw).strip()

    def generator_system(self, stage_block):
        common = self.fill("generator_system", reserved_lexicon=", ".join(self.spec.reserved_lexicon()))
        return common + "\n\n" + stage_block

    def judge_system(self, stage_block):
        return self.prompt("judge_system") + "\n\n" + stage_block

    def prompt_hashes(self):
        out = {}
        for f in sorted(os.listdir(self.prompts_dir)):
            if f.endswith(".txt"):
                with open(os.path.join(self.prompts_dir, f), encoding="utf8") as fh:
                    out[f[:-4]] = sha256_text(fh.read())
        return out

    # files
    def path(self, name):
        p = os.path.join(self.out, name)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        return p

    def load(self, name):
        p = self.path(name)
        recs = {}
        if os.path.exists(p):
            with open(p, encoding="utf8") as fh:
                for line in fh:
                    if line.strip():
                        r = json.loads(line)
                        recs[r["id"]] = r
        return recs

    def append(self, name, rec):
        with self.lock:
            with open(self.path(name), "a", encoding="utf8") as f:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    def write(self, name, recs):
        p = self.path(name)
        tmp = p + ".tmp"
        with open(tmp, "w", encoding="utf8") as f:
            for r in recs:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        os.replace(tmp, p)

    def parallel(self, fn, items):
        with ThreadPoolExecutor(max_workers=self.cfg.get("workers", 8)) as ex:
            return list(ex.map(fn, items))

    def code_version(self):
        try:
            return subprocess.run(["git", "-C", HERE, "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
        except Exception:
            return "unknown"
