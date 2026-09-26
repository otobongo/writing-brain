import re,sys,difflib
base='/Users/anita/Sandbox-Vibe/vibecoding/writing-brain/punct'
norm=lambda w: re.sub(r"[^a-z0-9]","",w.lower())
def toks(p): return [t for t in open(p,encoding='utf-8').read().split()]
for vid in sys.argv[1:]:
    a=[norm(w) for w in toks(f'{base}/in/{vid}.txt')]; b=[norm(w) for w in toks(f'{base}/out/{vid}.txt')]
    a=[x for x in a if x]; b=[x for x in b if x]
    if a==b: print(vid,'OK',len(a),'words'); continue
    sm=difflib.SequenceMatcher(None,a,b,autojunk=False); bad=[o for o in sm.get_opcodes() if o[0]!='equal']
    print(vid,'MISMATCH',len(bad),'places; in=%d out=%d words'%(len(a),len(b)))
    for tag,i1,i2,j1,j2 in bad[:15]: print('  ',tag,'orig:',' '.join(a[max(0,i1-3):i2+3]),'| yours:',' '.join(b[max(0,j1-3):j2+3]))
