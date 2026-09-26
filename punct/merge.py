"""Align punctuated out/<id>.txt with the full word list from the VTT.
Produces a (time, word) list where words carry the agent's punctuation/capitals,
and any word the agent never saw is inserted unpunctuated."""
import re,difflib,glob,sys
sys.path.insert(0,'/Users/anita/Sandbox-Vibe/vibecoding/writing-brain')
norm=lambda w: re.sub(r"[^a-z0-9]","",w.lower())
def merged(vid, parse):
    vtt=[p for p in glob.glob('transcripts/*.en-orig.vtt') if f'_{vid}_' in p][0]
    full=parse(vtt)                                   # [(t, word)]
    out=[w for w in open(f'punct/out/{vid}.txt',encoding='utf-8').read().split() if norm(w)]
    a=[norm(w) for _,w in full]; b=[norm(w) for w in out]
    sm=difflib.SequenceMatcher(None,a,b,autojunk=False)
    res=[]; stats={'equal':0,'insert':0,'replace':0,'delete':0}
    for tag,i1,i2,j1,j2 in sm.get_opcodes():
        if tag=='equal':
            res+= [(full[i][0], out[j1+(i-i1)]) for i in range(i1,i2)]; stats['equal']+=i2-i1
        elif tag=='delete':                          # agent lacked these words: keep raw
            res+= full[i1:i2]; stats['delete']+=i2-i1
        elif tag=='replace':                         # keep raw words (timing is ground truth)
            res+= full[i1:i2]; stats['replace']+=i2-i1
        else: stats['insert']+=j2-j1                 # agent added words: drop
    return res, stats
