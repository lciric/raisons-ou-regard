import os, anthropic
key = os.environ.get("RR_ANTHROPIC_API_KEY")
print("key present:", bool(key))
c = anthropic.Anthropic(api_key=key)
try:
    r = c.messages.create(model="claude-opus-5-5", max_tokens=16, messages=[{"role": "user", "content": "Reply with the single word: ok"}])
    print("status: ok", "| stop:", r.stop_reason, "| usage in/out:", r.usage.input_tokens, r.usage.output_tokens)
except anthropic.APIStatusError as e:
    msg = str(getattr(e, "message", e))
    print("status:", e.status_code, "|", msg[:200])
except Exception as e:
    print("error:", type(e).__name__, str(e)[:200])
