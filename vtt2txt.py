import re,glob,json,os
os.makedirs('text',exist_ok=True)
ids={}
for f in glob.glob('transcripts/*.vtt'):
    m=re.match(r'transcripts/(\d{8})_(.{11})_(.*?)\.(en[^.]*)\.vtt$',f)
    d,i,t,l=m.groups(); ids.setdefault(i,{})[l]=(f,d,t)
rows=[]
for i,v in ids.items():
    # prefer manual captions, then en-orig, then en
    for l in ('en-CA','en-en-CA','en-orig','en'):
        if l in v: f,d,t=v[l]; break
    out=[];last=''
    for line in open(f,encoding='utf-8'):
        line=line.strip()
        if not line or '-->' in line or line.startswith(('WEBVTT','Kind:','Language:')): continue
        line=re.sub(r'<[^>]+>','',line).strip()
        if line and line!=last: out.append(line); last=line
    txt=' '.join(out)
    dur=views=None
    try:
        j=json.load(open(f.rsplit('.',2)[0]+'.info.json')); dur=j.get('duration');views=j.get('view_count')
    except Exception: pass
    name=f'text/{d}_{i}.txt'
    open(name,'w').write(f'TITLE: {t}\nDATE: {d}\nURL: https://youtu.be/{i}\nSOURCE: {l}\n\n{txt}\n')
    rows.append((d,i,t,l,len(txt.split()),dur,views))
rows.sort()
with open('index.tsv','w') as o:
    for r in rows: o.write('\t'.join(map(str,r))+'\n')
print(len(rows),'videos',sum(r[4] for r in rows),'words')
