#!/bin/bash
# The vast.ai credit every 5 minutes while the decision 34 runs are open; CREDIT_LOW under 1.5 $.
cd /home/user/raisons-ou-regard/experiences || exit 1
export PYTHONPATH=/home/user/raisons-ou-regard/experiences
SP=/tmp/claude-0/-home-user-sycophancy-construct-validity/332d478c-da90-5795-bb10-27657d88c4d0/scratchpad
while ps -p "$(cat "$SP/poll_launch.pid")" > /dev/null 2>&1; do
  c=$(timeout 120 python3 -m rrexp check 2>/dev/null | python3 -c "import json,sys; print(round(json.load(sys.stdin)['vast']['credit_usd'],2))" 2>/dev/null)
  if [ -n "$c" ]; then
    tag=CREDIT; python3 -c "import sys; sys.exit(0 if $c < 1.5 else 1)" && tag=CREDIT_LOW
    echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) $tag $c"
  fi
  sleep 300
done
echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) CREDIT_WATCH_END"
