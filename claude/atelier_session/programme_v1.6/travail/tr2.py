import json,sys
d=json.load(open(sys.argv[1]))
print({s:round(v.get('degradation',{}).get('kl') or -1,5) for s,v in d['settings'].items()})
for s,man in d['manipulation'].items():
    print('=== setting',s)
    for c,cv in man['conditions'].items():
        L=cv.get('layers',[])
        if not L: print(' ',c,'no layers', list(cv.keys())); continue
        def m(k):
            v=[l.get(k) for l in L if l.get(k) is not None]
            return (round(sum(v)/len(v),4), round(max(v),3)) if v else None
        print(f"  {c:40s} lin_last={m('linear_last')} mlp_last={m('mlp_last')} lin_mean={m('linear_mean')} mlp_mean={m('mlp_mean')} resproj={m('residual_projection')} T_lin_last={m('transfer_linear_last')} T_mlp_last={m('transfer_mlp_last')} T_lin_mean={m('transfer_linear_mean')}")
