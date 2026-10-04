"""One episode, as a state machine: prompt() gives the conversation and the start of the assistant turn; feed() takes
the model's continuation, runs the first tool call, and answers. The drivers below run one episode, or many in
lockstep for batched generation on GPU.

**The conditions** (programme v1.5, part 3).
- framing: "evaluation" or "deploiement", with the cue of that polarity from the framing set; "neutre" has no cue
  (for the activation readings only).
- slot: "libre", the model writes its preface then acts (the main criterion); "prerempli", the slot is given closed
  and empty and the model writes only the action (the co-principal criterion); "prerempli_neutre", the slot holds a
  neutral text of the same length for every arm (secondary).
- directive: a line added to the system prompt, for the positive control of the measure's sensitivity.

**The rules**, fixed before the data and identical for every arm (parameters of Config, frozen at the first stage):
- the slot opens every assistant turn, as in training;
- in the history, an earlier assistant turn keeps only its action (the training contexts hold bare tool calls); the
  slot's text is kept apart, never shown to the judge;
- a reply without a tool call is the final answer and ends the episode; so does a terminal tool (submit_answers);
- a malformed output, or a call to an unknown tool or with invalid arguments, gets an error as the tool result; after
  max_invalid of them in a row the episode ends ("invalid_limit");
- the episode ends after the scenario's max_turns model turns.
"""
import copy
from dataclasses import dataclass, field

from . import tools as T
from .env import Env
from .parse import CLOSE, FORMAT_ERRORS, OPEN, parse_output

FRAMINGS = ("evaluation", "deploiement", "neutre")
SLOTS = ("libre", "prerempli", "prerempli_neutre")
POLARITY = {"evaluation": "eval", "deploiement": "deploy"}


@dataclass
class Condition:
    framing: str
    slot: str = "libre"
    cue: dict = None
    neutral_preface: str = ""
    directive: str = None

    def check(self):
        if self.framing not in FRAMINGS:
            raise ValueError(f"unknown framing {self.framing!r}")
        if self.slot not in SLOTS:
            raise ValueError(f"unknown slot {self.slot!r}")
        if self.framing == "neutre" and self.cue is not None:
            raise ValueError("a neutral framing has no cue")
        if self.framing != "neutre":
            if not self.cue:
                raise ValueError(f"the framing {self.framing} needs a cue")
            if self.cue.get("polarity") and self.cue["polarity"] != POLARITY[self.framing]:
                raise ValueError(f"a {self.cue['polarity']} cue under the framing {self.framing}")
        if self.slot == "prerempli_neutre" and not self.neutral_preface:
            raise ValueError("the slot prerempli_neutre needs its neutral text")


@dataclass
class Config:
    max_invalid: int = 3
    lenient_closing_tag: bool = True
    history: str = "action"          # "action": earlier turns keep their action only; "full": with their slot
    open_tag: str = OPEN
    close_tag: str = CLOSE


class Episode:
    def __init__(self, scenario, condition, meta=None, config=None):
        condition.check()
        self.scenario = scenario
        self.condition = condition
        self.meta = dict(meta or {})
        self.config = config or Config()
        self.rendered = scenario.render(condition.cue)
        self.env = Env(self.rendered.environment)
        system = self.rendered.system + "\n\n" + T.tools_block(scenario.tools)
        if condition.directive:
            system += "\n\n" + condition.directive
        self.system = system
        # the prefix: user turns as written; assistant tool calls executed, their results computed
        self.prefix = []
        self.env.turn = 0
        for t in self.rendered.turns:
            if t["role"] == "user":
                self.prefix.append({"role": "user", "content": t["content"].strip()})
            else:
                p = parse_output(t["content"], scenario.tools)
                result = self.env.apply(p["call"]["name"], p["call"]["arguments"])
                self.prefix.append({"role": "assistant", "content": p["visible"]})
                self.prefix.append({"role": "tool", "content": result})
        self.prefix_events = self.env.events
        self.env.events = []
        self.env.initial_files = copy.deepcopy(self.env.files)
        self.history = []
        self.turns = []
        self.done = False
        self.ended = None
        self.consecutive_invalid = 0
        self.counts = {"valid_calls": 0, "invalid_calls": 0, "malformed": 0, "closing_tag_missing": 0}

    # ------------------------------------------------------------------ the loop

    def assistant_prefix(self):
        o, c = self.config.open_tag, self.config.close_tag
        if self.condition.slot == "prerempli":
            return f"{o}{c}\n"
        if self.condition.slot == "prerempli_neutre":
            return f"{o}{self.condition.neutral_preface}{c}\n"
        return ""

    def prompt(self):
        """(messages, start of the assistant turn). The generation continues the start, and stops at the first
        </tool_call> or at the end of the turn."""
        if self.done:
            raise RuntimeError("the episode is over")
        return [{"role": "system", "content": self.system}] + self.prefix + self.history, self.assistant_prefix()

    def _end(self, why):
        self.done = True
        self.ended = why

    def feed(self, generated):
        """Takes the model's continuation of prompt()'s start; returns the tool result shown (or None at the end)."""
        if self.done:
            raise RuntimeError("the episode is over")
        n = len(self.turns) + 1
        self.env.turn = n
        raw = self.assistant_prefix() + (generated or "")
        p = parse_output(raw, self.scenario.tools, self.config.open_tag, self.config.close_tag,
                         self.config.lenient_closing_tag)
        rec = {"turn": n, "raw": raw, "preface": p["preface"], "visible": p["visible"], "call": p["call"],
               "final_answer": p["final_answer"], "malformed": p["malformed"], "error": None, "result": None,
               "closing_tag_missing": p["closing_tag_missing"], "dropped_after_call": p["dropped_after_call"],
               "extra_prefaces": p["extra_prefaces"], "events_from": len(self.env.events)}
        shown = p["visible"]
        if self.config.history == "full" and p["preface"] is not None:
            shown = f"{self.config.open_tag}{p['preface']}{self.config.close_tag}\n{p['visible']}"
        result = None
        if p["malformed"]:
            self.counts["malformed"] += 1
            self.consecutive_invalid += 1
            result = FORMAT_ERRORS[p["malformed"]]
            rec["error"] = p["malformed"]
            self.history += [{"role": "assistant", "content": shown or "(empty)"}, {"role": "tool", "content": result}]
        elif p["call"] is None:
            self.history.append({"role": "assistant", "content": shown})
            self._end("final_answer")
        else:
            self.counts["closing_tag_missing"] += p["closing_tag_missing"]
            name, args = p["call"]["name"], p["call"]["arguments"]
            err = T.check_arguments(name, args, self.scenario.tools)
            if err:
                self.counts["invalid_calls"] += 1
                self.consecutive_invalid += 1
                result = err
                rec["error"] = "invalid_call"
            else:
                self.counts["valid_calls"] += 1
                self.consecutive_invalid = 0
                result = self.env.apply(name, args)
            self.history += [{"role": "assistant", "content": shown}, {"role": "tool", "content": result}]
            if not err and T.is_terminal(name):
                self._end("terminal_tool")
        rec["result"] = result
        rec["events_to"] = len(self.env.events)
        self.turns.append(rec)
        if not self.done and self.consecutive_invalid >= self.config.max_invalid:
            self._end("invalid_limit")
        if not self.done and len(self.turns) >= self.scenario.max_turns:
            self._end("max_turns")
        return result

    # ------------------------------------------------------------------ views

    def actions(self):
        """The model's actions, in order: each valid tool call and the final answer."""
        out = []
        for t in self.turns:
            if t["call"] and t["error"] is None:
                out.append({"turn": t["turn"], "kind": t["call"]["name"], "call": t["call"], "text": t["visible"]})
            elif t["final_answer"] is not None:
                out.append({"turn": t["turn"], "kind": "final_answer", "call": None, "text": t["final_answer"]})
        return out


def run_episode(episode, generate):
    """generate(messages, start) -> continuation. Runs to the end; returns the episode."""
    while not episode.done:
        messages, start = episode.prompt()
        episode.feed(generate(messages, start))
    return episode


def run_batch(episodes, generate_batch, max_batch=None):
    """generate_batch([(messages, start), ...]) -> [continuation, ...]. Steps every open episode in lockstep."""
    active = [e for e in episodes if not e.done]
    while active:
        chunk = active if not max_batch else active[:max_batch]
        outs = generate_batch([e.prompt() for e in chunk])
        if len(outs) != len(chunk):
            raise ValueError("generate_batch returned a different number of continuations")
        for e, o in zip(chunk, outs):
            e.feed(o)
        active = [e for e in episodes if not e.done]
    return episodes
