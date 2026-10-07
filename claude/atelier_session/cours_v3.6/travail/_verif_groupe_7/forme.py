import json,re
W='/tmp/claude-0/-home-user-sycophancy-construct-validity/332d478c-da90-5795-bb10-27657d88c4d0/scratchpad/cours_v36'
for tr in ['volet11_1_a_20','volet11_21_a_52','volet11_53_et_fin']:
    d=json.load(open(f'{W}/travail/insertions_{tr}.json',encoding='utf8'))
    for n,ins in enumerate(d['insertions'],1):
        t=ins['texte']
        quotes=re.findall(r'«\s*([^»]*?)\s*»',t)+re.findall(r'"([^"]*)"',t)+re.findall(r'“([^”]*)”',t)
        for q in quotes:
            w=len(q.split())
            if w>=12: print(tr,n,ins['fichier'],'citation',w,'mots:',q[:100])
        if re.search(r'\bfirst\b|\bpremier\b|\bpremière\b',t,re.I):
            print(tr,n,ins['fichier'],'FIRST?',re.findall(r'.{30}(?:first|premier|première).{30}',t,re.I))
        # format checks
        l0=t.split('\n')[0]
        ok = l0.startswith('> ⚠ *(v3.6)*') or l0.startswith('> ⚠ **Limites et parades** :') or l0.startswith('> ⚠ **Limits and workarounds**:') or l0.startswith('> **⚠ Limites et parades —') or l0.startswith('> **⚠ Limits and workarounds —')
        if not ok: print(tr,n,'FORMAT?',l0[:80])
        if (l0.startswith('> ⚠ **Limites') or l0.startswith('> ⚠ **Limits')) and not l0.rstrip().endswith('*(v3.6)*'): print(tr,n,'renvoi sans (v3.6) final')
        # acronyms: uppercase tokens of 2+ letters
        for a in sorted(set(re.findall(r'\b[A-Z][A-Z0-9]{1,}[a-z]?\b',t))):
            if a not in {'SFT','RL','DPO','LoRA','GPU','AUROC','SAE','SAEs','CoT','NLA','NLAs','LLM','README','RLHF','MMLU','GPT','WMDP','CHIVE','TRACE','SHADE','AISI','ACP','MSM','RMU','K47','K63','K70','K71','K72','K52','K67','JB8','JB10','G1','A4','A10','B14','M4','M5','M7','M9','M10','II','AUC','ARC','AF','NEM','RLVR','J','EN','FR'}:
                print(tr,n,ins['fichier'],'SIGLE?',a)
