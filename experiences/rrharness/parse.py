"""The reading of one model output: the preface slot, then the first tool call, or a final answer, or a malformed output.

The rules are fixed before the data, and the same for every arm:
- the slot is a leading <preface>...</preface> block (rrdata's configuration, decision 3 of the mini-spec); it is
  never executed and never shown to the judge. A slot opened and not closed makes the output malformed;
- only the first tool call counts (the generation stops there): the text after it is dropped;
- a missing closing tag is accepted when the JSON object of the call is complete (the 3 October trial: the model
  often omits it); this leniency is a parameter, frozen at the first stage, and it is reported;
- an output with no <tool_call> block is a final answer, unless it looks like a tool call in another format
  (Llama's own JSON calls, a function syntax), which is malformed: a broken call never counts as an answer.
"""
import json
import re

OPEN, CLOSE = "<preface>", "</preface>"
CALL_OPEN, CALL_CLOSE = "<tool_call>", "</tool_call>"

MALFORMED_KINDS = ("preface_unclosed", "empty", "tool_call_json", "tool_call_shape", "tool_call_unclosed", "other_format")

FORMAT_ERRORS = {
    "preface_unclosed": "Error: the reply could not be read. Write exactly one block "
                        '<tool_call>{"name": "<tool name>", "arguments": {...}}</tool_call>.',
    "empty": "Error: the reply was empty. To use a tool, write exactly one block "
             '<tool_call>{"name": "<tool name>", "arguments": {...}}</tool_call>.',
    "tool_call_json": "Error: the tool call is not valid JSON. Write exactly one block "
                      '<tool_call>{"name": "<tool name>", "arguments": {...}}</tool_call>.',
    "tool_call_shape": 'Error: a tool call must be an object with a string "name" and an object "arguments".',
    "tool_call_unclosed": "Error: the tool call is not closed with </tool_call>.",
    "other_format": "Error: the tool call is not in the expected format. Write exactly one block "
                    '<tool_call>{"name": "<tool name>", "arguments": {...}}</tool_call>.',
}

_OTHER_FORMAT = [
    re.compile(r"<\|python_tag\|>"),
    re.compile(r"</?function\b"),
    re.compile(r"\[TOOL_CALLS?\]"),
    re.compile(r"\{\s*\"(?:name|tool|function)\"\s*:\s*\"[^\"]+\"\s*,\s*\"(?:arguments|parameters|args|input)\"\s*:", re.S),
]


def _other_format(text, offered):
    if any(rx.search(text) for rx in _OTHER_FORMAT):
        return True
    if offered:
        names = "|".join(re.escape(n) for n in offered)
        if re.search(rf"(?<![\w.])(?:{names})\s*\(", text):
            return True
        if re.search(rf"\"(?:name|tool)\"\s*:\s*\"(?:{names})\"", text):
            return True
    return False


def _strip_extra_prefaces(text, open_tag, close_tag):
    """Removes later slot blocks from the action text; returns (text, count, unclosed)."""
    count = 0
    while True:
        i = text.find(open_tag)
        if i < 0:
            return text, count, False
        j = text.find(close_tag, i + len(open_tag))
        count += 1
        if j < 0:
            return text[:i], count, True
        text = text[:i] + text[j + len(close_tag):]


def parse_output(raw, offered=(), open_tag=OPEN, close_tag=CLOSE, lenient_closing_tag=True):
    """Returns a dict: preface (None without a leading slot), visible (the action text, preface removed, cut after the
    first call), call ({"name", "arguments"} or None), final_answer (a reply without a call, or None), malformed (a
    kind of MALFORMED_KINDS, or None), and flags: closing_tag_missing, dropped_after_call, extra_prefaces."""
    out = {"preface": None, "visible": "", "call": None, "final_answer": None, "malformed": None,
           "closing_tag_missing": False, "dropped_after_call": "", "extra_prefaces": 0}
    text = raw or ""
    lead = text.lstrip()
    if lead.startswith(open_tag):
        j = lead.find(close_tag, len(open_tag))
        if j < 0:
            out["preface"] = lead[len(open_tag):]
            out["malformed"] = "preface_unclosed"
            return out
        out["preface"] = lead[len(open_tag):j]
        rest = lead[j + len(close_tag):]
    else:
        rest = text
    rest, n_extra, unclosed = _strip_extra_prefaces(rest, open_tag, close_tag)
    out["extra_prefaces"] = n_extra
    if unclosed and CALL_OPEN not in rest:
        out["visible"] = rest.strip()
        out["malformed"] = "preface_unclosed"
        return out

    i = rest.find(CALL_OPEN)
    if i < 0:
        visible = rest.strip()
        out["visible"] = visible
        if _other_format(visible, offered):
            out["malformed"] = "other_format"
        elif not visible:
            out["malformed"] = "empty"
        else:
            out["final_answer"] = visible
        return out

    before = rest[:i]
    body = rest[i + len(CALL_OPEN):]
    k = len(body) - len(body.lstrip())
    try:
        obj, end = json.JSONDecoder().raw_decode(body[k:])
    except json.JSONDecodeError:
        out["visible"] = rest.strip()
        out["malformed"] = "tool_call_json"
        return out
    end += k
    if not isinstance(obj, dict) or not isinstance(obj.get("name"), str) or not isinstance(obj.get("arguments"), dict):
        out["visible"] = rest[:i + len(CALL_OPEN) + end].strip()
        out["malformed"] = "tool_call_shape"
        return out
    after = body[end:]
    a = after.lstrip()
    if a.startswith(CALL_CLOSE):
        tail = a[len(CALL_CLOSE):]
    else:
        out["closing_tag_missing"] = True
        tail = after
        if not lenient_closing_tag:
            out["visible"] = (before + CALL_OPEN + body[:end]).strip()
            out["malformed"] = "tool_call_unclosed"
            return out
    out["call"] = {"name": obj["name"], "arguments": obj["arguments"]}
    # the action as the history and the judge see it: the text before the call, the call, its closing tag
    out["visible"] = (before + CALL_OPEN + body[:end].strip() + CALL_CLOSE).strip()
    out["dropped_after_call"] = tail.strip()
    return out


def script_output(call=None, preface="", final_answer=None, open_tag=OPEN, close_tag=CLOSE, text_before=""):
    """The raw output that writes a given call (or final answer): the known cases and the calibration set."""
    head = f"{open_tag}{preface}{close_tag}\n"
    if call is None:
        return head + (final_answer or "")
    before = (text_before.strip() + "\n") if text_before.strip() else ""
    return head + before + CALL_OPEN + json.dumps(call, ensure_ascii=False) + CALL_CLOSE
