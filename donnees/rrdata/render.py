"""How a situation is shown: to the generator and the judges (plain text), and to the trained model (chat messages)."""

TOOLS_INTRO = ("You can use the following tools. To call a tool, write exactly one block of the form\n"
               '<tool_call>{"name": "<tool name>", "arguments": {<arguments as JSON>}}</tool_call>\n'
               "and wait for its result before going on.\n\nTools:")

LABELS = {"user": "[USER]", "assistant": "[ASSISTANT]", "tool": "[TOOL RESULT]"}


def tools_block(spec, fam):
    tools = fam.data.get("tools") or []
    if not tools:
        return ""
    lines = [f"- {spec.tools[t]['signature']}: {spec.tools[t]['description_en']}" for t in tools]
    return TOOLS_INTRO + "\n" + "\n".join(lines)


def system_text(sit, tools=""):
    return "\n\n".join(x for x in [(sit.get("system_prompt") or "").strip(), tools] if x)


def render_situation(sit, tools=""):
    parts = []
    sp = system_text(sit, tools)
    if sp:
        parts.append("[SYSTEM PROMPT]\n" + sp)
    for t in sit.get("turns", []):
        parts.append(LABELS[t["role"]] + "\n" + t["content"].strip())
    return "\n\n".join(parts)


def chat_messages(sit, tools, target):
    """The training example: system prompt, turns, then the assistant turn that the loss is computed on."""
    msgs = []
    sp = system_text(sit, tools)
    if sp:
        msgs.append({"role": "system", "content": sp})
    for t in sit["turns"]:
        msgs.append({"role": t["role"], "content": t["content"].strip()})
    msgs.append({"role": "assistant", "content": target})
    return msgs


def with_preface(open_tag, close_tag, preface, action):
    return f"{open_tag}{preface}{close_tag}\n{action}"
