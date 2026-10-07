import json,sys
d=json.load(open(sys.argv[1]))
for s,man in d['manipulation'].items():
    print('=== setting',s, 'KL', d['settings'].get(s,{}).get('degradation',{}).get('kl'))
    for c,cv in man['conditions'].items():
        L=cv.get('layers',[])
        if not L: print(c,'no layers', cv.keys()); continue
        def col(k): return [l.get(k) for l in L if l.get(k) is not None]
        out=[c]
        for k in ['linear_last','mlp_last','linear_mean','residual_projection','transfer_linear_last','transfer_mlp_last','transfer_linear_mean','transfer_mlp_mean']:
            v=col(k)
            if v: out.append(f"{k}: mean={sum(v)/len(v):.4f} max={max(v):.3f}@L{L[[l.get(k) for l in L].index(max(v))]['layer']} min={min(v):.3f}")
        print('\n  '.join(out))
        v=col('transfer_linear_last')
        if v:
            below=[l['layer'] for l in L if l.get('transfer_linear_last') is not None and l['transfer_linear_last']<0.5]
            sym=[max(a,1-a) for a in v]
            print('  below0.5 layers:',below, 'n=',len(below))
            print('  sym mean %.4f  |a-.5| mean %.4f'%(sum(sym)/len(sym), sum(abs(a-.5) for a in v)/len(v)))
            print('  per-layer:', [(l['layer'],l['transfer_linear_last']) for l in L])
            vm=col('transfer_mlp_last')
            if vm:
                symm=[max(a,1-a) for a in vm]
                print('  mlp sym mean %.4f'%(sum(symm)/len(symm)))
                print('  mlp per-layer:', [(l['layer'],l.get('transfer_mlp_last')) for l in L])
        print('  summary', cv.get('summary'))
