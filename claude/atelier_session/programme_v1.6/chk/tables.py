import sys,re
lines=open(sys.argv[1],encoding='utf8').read().split('\n')
i=0
while i<len(lines):
    if lines[i].startswith('|'):
        start=i
        if i>0 and lines[i-1].strip()!='':
            print('NO BLANK BEFORE TABLE at',i+1, repr(lines[i-1][:60]))
        hdr=lines[i].count('|')
        j=i
        while j<len(lines) and lines[j].startswith('|'):
            c=len(re.findall(r'(?<!\\)\|',lines[j]))
            if c!=hdr: print('CELL COUNT',j+1,c,'vs',hdr, lines[j][:80])
            j+=1
        if j<len(lines) and lines[j].strip()!='':
            print('NO BLANK AFTER TABLE at',j+1, repr(lines[j][:60]))
        i=j
    else: i+=1
