import os, sys, time, datetime, anthropic
c = anthropic.Anthropic(api_key=os.environ["RR_ANTHROPIC_API_KEY"])
for i in range(10):
    now = datetime.datetime.utcnow().strftime("%H:%M:%S")
    try:
        r = c.messages.create(model="claude-opus-5-5", max_tokens=16, messages=[{"role": "user", "content": "Reply with the single word: ok"}])
        print(now, "CREDIT OK", r.stop_reason, flush=True)
        sys.exit(0)
    except anthropic.APIStatusError as e:
        print(now, "status", e.status_code, str(e.message)[60:120], flush=True)
    time.sleep(60)
print("toujours pas de crédit après 10 essais", flush=True)
sys.exit(1)
