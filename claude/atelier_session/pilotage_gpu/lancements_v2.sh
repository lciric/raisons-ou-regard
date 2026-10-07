# Balayage (note du 4 octobre), sur l'extraction v2
python3 -m rrexp launch organism_inhibition --max-hours 0 \
 --arg sdf_adapter=runs/organism-20261003-164800-9e3e/out/sdf_adapter \
 --arg ei_adapter=runs/organism-20261004-003822-bc0f/out/ei_round6/adapter \
 --arg subspace_run=extract_eval-20261005-114155-50b2 \
 --arg cues=indices-v2-2026-10-05 \
 --arg half=choix --arg gaps=false --arg rival=false --arg 'controls=[]' \
 --arg 'settings=[{"layers": "all", "rank": 1}, {"layers": "all", "rank": 4}, {"layers": "all", "rank": 16}, {"layers": [4, 5, 6, 7, 8], "rank": 16}, {"layers": "all", "erase": {"fit_sets": ["extraction"]}}, {"layers": [4, 5, 6, 7, 8], "erase": {"fit_sets": ["extraction"]}}]' \
 --arg 'comparator={"top": 6, "n_draws": 1}' \
 --arg 'manipulation={"cue_set": "validation", "draws": 1, "failure_layer": 6}' \
 --arg seed=1

# Effacement sur la conduite (7c3d refait), indices v2
python3 -m rrexp launch organism_inhibition --max-hours 0 \
 --arg sdf_adapter=runs/organism-20261003-164800-9e3e/out/sdf_adapter \
 --arg ei_adapter=runs/organism-20261004-003822-bc0f/out/ei_round6/adapter \
 --arg subspace_run=extract_eval-20261005-114155-50b2 \
 --arg cues=indices-v2-2026-10-05 \
 --arg half=choix \
 --arg 'framings=["eval_extraction", "deploy_extraction", "eval_framing", "deploy_framing"]' \
 --arg 'settings=[{"layers": "all", "erase": {"fit_sets": ["extraction"]}}]' \
 --arg 'comparator={"top": 1, "n_draws": 1}' \
 --arg seed=1
