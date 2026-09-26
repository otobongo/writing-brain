"""Assemble concept_review/out_*.json -> site/concepts.js and concept-index.md"""
import json,glob,re
vids={}
for f in glob.glob('readable/*.md'):
    s=open(f,encoding='utf-8').read(); vid=re.search(r'youtu\.be/(\S+)',s).group(1)
    vids[vid]=(re.search(r'- Date: (\S+)',s).group(1), s.split('\n')[0][2:], f)
cands={c['name']:c for c in json.load(open('concept_candidates.json'))}
order=[c['name'] for c in json.load(open('concept_candidates.json'))]
out=[]
for f in glob.glob('concept_review/out_*.json'):
    for c in json.load(open(f)):
        valid=[(h['vid'],h['t']) for h in cands.get(c['name'],{'hits':[]})['hits']]
        hits=[h for h in c['hits'] if (h['vid'],h['t']) in valid]
        hits.sort(key=lambda h:(vids[h['vid']][0],h['t']))
        out.append({'group':c['group'],'name':c['name'],'hits':hits,'dropped':len(c['hits'])-len(hits)})
out.sort(key=lambda c: order.index(c['name']) if c['name'] in order else 999)
open('site/concepts.js','w',encoding='utf-8').write('window.CONCEPTS='+json.dumps(out,ensure_ascii=False)+';')
fmt=lambda t:(f'{t//3600}:{t%3600//60:02d}:{t%60:02d}' if t>=3600 else f'{t//60}:{t%60:02d}')
md=['# Writer Science — concept index','',
 'Every place a concept is taught on the channel, with a link to that moment in the video. **Bold** = best explanation to watch first. Built from the transcripts in `readable/`; passing mentions were dropped.','']
g=None
for c in out:
    if c['group']!=g: g=c['group']; md+=[f'## {g}','']
    md.append(f'### {c["name"]}'); md.append('')
    if not c['hits']: md.append('_No teaching passage found by search._'); md.append(''); continue
    md.append('| When | Video | What he says |'); md.append('|---|---|---|')
    for h in c['hits']:
        d,title,_=vids[h['vid']]; link=f'[{fmt(h["t"])}](https://youtu.be/{h["vid"]}?t={h["t"]})'
        if h.get('primary'): link=f'**{link}**'
        md.append(f'| {link} | {title} ({d[:4]}) | {h.get("note","")} |')
    md.append('')
open('concept-index.md','w',encoding='utf-8').write('\n'.join(md))
print(len(out),'concepts', sum(len(c['hits']) for c in out),'hits', sum(c['dropped'] for c in out),'invalid dropped', sum(1 for c in out if not c['hits']),'empty')
