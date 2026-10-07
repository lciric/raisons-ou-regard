#!/bin/bash
# Decision 34: launches each pending candidate when an H100 SXM offer passes the config's filters, and follows the open
# runs with the watcher, until nothing is pending or open. Events go to stdout, one line each.
SP=/tmp/claude-0/-home-user-sycophancy-construct-validity/332d478c-da90-5795-bb10-27657d88c4d0/scratchpad
cd /home/user/raisons-ou-regard/experiences || exit 1
export PYTHONPATH=/home/user/raisons-ou-regard/experiences
source "$SP/common_args.sh"
PENDING="${PENDING-A B C}"
launch_deadline=$(( $(date +%s) + ${LAUNCH_HOURS:-10}*3600 ))
last_tick=0
log() { echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) $*"; }
log "START (resume) pending=[$PENDING] launch deadline in ${LAUNCH_HOURS:-10} h"
while :; do
  if [ -n "$PENDING" ]; then
    if [ "$(date +%s)" -ge "$launch_deadline" ]; then
      log "GAVE_UP pending=[$PENDING]: no H100 SXM offer before the deadline"
      PENDING=""
    else
      n=$(timeout 120 python3 "$SP/count_offers.py" 2>/dev/null || echo 0)
      [[ "$n" =~ ^[0-9]+$ ]] || n=0
      # the credit must cover the runs: 20 $ before the first launch, 10 $ before a later one
      need=${MIN_CREDIT_NEXT:-10}; [ "$(echo $PENDING | wc -w)" -ge 3 ] && need=${MIN_CREDIT_FIRST:-20}
      credit=$(timeout 120 python3 "$SP/credit_now.py" 2>/dev/null || echo 0)
      if ! python3 -c "import sys; sys.exit(0 if float('${credit:-0}') >= $need else 1)" 2>/dev/null; then
        if [ $(( $(date +%s) - ${last_wait:-0} )) -ge 1800 ]; then
          log "WAIT_CREDIT credit ${credit} \$ < ${need} \$; pending=[$PENDING]"
          last_wait=$(date +%s)
        fi
        n=0
      fi
      for c in $PENDING; do
        [ "$n" -gt 0 ] || break
        out=$(timeout 900 python3 -m rrexp launch organism_inhibition "${COMMON[@]}" --arg "${!c}" --arg "$(v=${c}_COMP; echo "${!v}")" --gpu "H100 SXM" --max-hours 4 2>>"$SP/launch_stderr.log")
        line=$(printf '%s' "$out" | python3 "$SP/parse_launch.py")
        if [[ "$line" == *" launched "* ]]; then
          log "LAUNCHED candidate $c: $line"
          PENDING=$(echo $PENDING | tr ' ' '\n' | grep -vx "$c" | tr '\n' ' ' | sed 's/ *$//')
        else
          log "LAUNCH_FAILED candidate $c: $line (see launch_stderr.log)"
        fi
        n=$((n - 1))
      done
    fi
  fi
  timeout 900 python3 -m rrexp watch --once 2>>"$SP/watch_stderr.log" | while read -r l; do log "WATCH $l"; done
  open=$(timeout 120 python3 "$SP/open_runs.py" 2>/dev/null || echo "?")
  if [ -z "$PENDING" ] && [ "$open" = "0" ]; then
    log "END nothing pending, no open run"
    exit 0
  fi
  if [ $(( $(date +%s) - last_tick )) -ge 3600 ]; then
    log "TICK pending=[$PENDING] open=$open"
    last_tick=$(date +%s)
  fi
  sleep 120
done
