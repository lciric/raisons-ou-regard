import json,re,glob,collections
import importlib.util
W='/tmp/claude-0/-home-user-sycophancy-construct-validity/332d478c-da90-5795-bb10-27657d88c4d0/scratchpad/cours_v36'
spec = importlib.util.spec_from_file_location('ap', f'{W}/outils/appliquer.py'); ap = importlib.util.module_from_spec(spec); spec.loader.exec_module(ap)
L = {k: open(v, encoding='utf8').read().split('\n') for k, v in ap.SRC.items()}
def ident(h):
    for p in (r'^#+\s+(Q\d+)\.', r'^#+\s+(F·\d+)', r'^#+\s+(M\d+)\s*·', r'^#+\s+(C bis)', r'^#+\s+([A-I])(?:\.|\s·|\s\()', r'^#+\s+(\d+)\s*[·.]'):
        m=re.match(p,h)
        if m: return m.group(1)
    return None
def nearest(fi,i):
    for j in range(i,-1,-1):
        if re.match(r'^#{1,6} ',L[fi][j]): return j,L[fi][j]
    return -1,''
STOP=set('The A An In It This That Le La Les Un Une Des Il Elle On Ce Cette Et But Mais Two Deux What Ce Qui Pour For To De Du'.split())
def toks(s):
    s=s.replace(' ',' ').replace(' ',' ')
    t=set(re.findall(r'\d+(?:[.,]\d+)?|[A-Z][\w·\-]*[A-Z0-9][\w·\-]*|[A-Z][a-z]{2,}|\w+·\w+',s))
    return {x.replace(',','.') for x in t if x not in STOP}
res=collections.Counter(); out=[]
for f in sorted(glob.glob(f'{W}/travail/insertions_*.json')):
    d=json.load(open(f,encoding='utf8')); tr=d['tranche']
    F=[x for x in d['insertions'] if x['fichier']=='FR'];E=[x for x in d['insertions'] if x['fichier']=='EN']
    for k,(x,y) in enumerate(zip(F,E),1):
        info=[]
        for z in (x,y):
            fi=z['fichier'];a,b=ap.TRANCHES[tr][fi]
            i=[i for i in range(a-1,min(b,len(L[fi]))) if L[fi][i].strip()==z['ancre'].strip()][0]
            j,h=nearest(fi,i)
            info.append((i,j,h,ident(h),toks(L[fi][i])))
        (iF,jF,hF,idF,tF),(iE,jE,hE,idE,tE)=info
        inter=tF&tE
        if idF and idE:
            verdict='ident_ok' if idF==idE else 'IDENT_DIFF'
        else:
            verdict='tokens_ok' if inter else 'A_VERIFIER'
        res[verdict]+=1
        if verdict in ('IDENT_DIFF','A_VERIFIER') or (verdict=='ident_ok' and not inter and (tF or tE)):
            out.append(f'{tr} paire {k} [{verdict}] FR l.{iF+1} (titre l.{jF+1} {idF}) / EN l.{iE+1} (titre l.{jE+1} {idE}); communs={sorted(inter)[:8]}\n   FR: {L["FR"][iF].strip()[:150]}\n   EN: {L["EN"][iE].strip()[:150]}\n   titreFR: {hF[:90]}\n   titreEN: {hE[:90]}')
print(res)
open(f'{W}/travail/_application/endroit.txt','w',encoding='utf8').write('\n'.join(out)+'\n')
print(len(out),'cas listés')
