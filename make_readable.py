"""Build readable, paragraphed transcripts in readable/ from the raw captions.
Reads transcripts/*.vtt (never modified). Words are kept verbatim; only layout changes."""
import re, glob, os, html, sys

OUT = 'readable'
os.makedirs(OUT, exist_ok=True)
TS = re.compile(r'(\d+):(\d\d):(\d\d)\.(\d{3})')
def secs(m): h, mi, s, ms = map(int, m.groups()); return h*3600 + mi*60 + s + ms/1000
def clean(t): return re.sub(r'\s+', ' ', html.unescape(t).replace('\xa0', ' ')).strip()

def parse(path):
    """Return [(start_seconds, word), ...]"""
    raw = open(path, encoding='utf-8').read()
    auto = '<c>' in raw
    words = []
    for block in re.split(r'\n\n+', raw.replace('\r','')):
        lines = block.split('\n')
        ti = next((k for k, l in enumerate(lines) if '-->' in l), None)
        if ti is None: continue
        a, b = [secs(m) for m in TS.finditer(lines[ti])][:2]
        body = lines[ti+1:]
        if auto:
            if b - a < 0.05: continue                      # 10ms duplicate cue
            body = [l for l in body if l.strip() and l.strip() != '\xa0']
            if not body: continue
            new = body[-1]                                   # rolling captions: last line is the new text
            t = a
            for piece in re.split(r'(<\d+:\d\d:\d\d\.\d{3}>)', new):
                m = TS.search(piece) if piece.startswith('<') else None
                if m: t = secs(m); continue
                for w in clean(re.sub(r'<[^>]+>', '', piece)).split():
                    words.append((t, w))
        else:
            ws = clean(re.sub(r'<[^>]+>', '', ' '.join(body))).split()
            for k, w in enumerate(ws):
                words.append((a + (b - a) * k / max(len(ws), 1), w))
    return words

def paragraphs(words):
    # sentences
    sents, cur = [], []
    for k, (t, w) in enumerate(words):
        cur.append((t, w))
        if re.search(r'[.?!]["\')\]]*$', w) and not re.fullmatch(r'(Mr|Mrs|Dr|vs|e\.g|i\.e|St)\.', w):
            sents.append(cur); cur = []
    if cur: sents.append(cur)
    punct = len(sents) / max(len(words), 1)
    if punct < 1/60:                                         # unpunctuated captions: chunk by pauses
        sents, cur = [], []
        for k, (t, w) in enumerate(words):
            cur.append((t, w))
            nxt = words[k+1][0] if k+1 < len(words) else t
            if len(cur) >= 12 and nxt - t > 0.9 or len(cur) >= 40: sents.append(cur); cur = []
        if cur: sents.append(cur)
    paras, cur, n = [], [], 0
    for k, s in enumerate(sents):
        cur.append(s); n += len(s)
        gap = (sents[k+1][0][0] - s[-1][0]) if k+1 < len(sents) else 0
        if (n >= 45 and gap >= 0.85) or n >= 150:
            paras.append(cur); cur, n = [], 0
    if cur: paras.append(cur)
    return paras, punct

def fname(d, t):
    c = re.sub(r'[\\/:*?"<>|？：＂｜]+', ' ', t); c = re.sub(r'\s+', ' ', c).strip(' .')
    return f'{d[:4]}-{d[4:6]}-{d[6:]} {c}'

report = []
for line in open('index.tsv'):
    d, vid, title, src = line.rstrip('\n').split('\t')[:4]
    vtt = [p for p in glob.glob(f'transcripts/{d}_*.{src}.vtt') if f'_{vid}_' in p][0]
    words = parse(vtt)
    punct_note = ''
    if os.path.exists(f'punct/out/{vid}.txt'):
        sys.path.insert(0, 'punct'); from merge import merged
        words, st = merged(vid, parse)
        punct_note = '; punctuation and capitalization added by Claude (auto-captions had none)'
    paras, punct = paragraphs(words)
    name = fname(d, title)
    if name.endswith('WITHOUT A.I'): name = name[:-3] + 'AI'
    kind = 'manual captions' if src in ('en-CA', 'en-en-CA') else 'auto-captions'
    out = [f'# {title}', '', f'- Date: {d[:4]}-{d[4:6]}-{d[6:]}', f'- Video: https://youtu.be/{vid}',
           f'- Source: YouTube {kind} ({src}), words unchanged; paragraph breaks and timestamps added{punct_note}', '', '---', '']
    for p in paras:
        t = int(p[0][0][0]); stamp = f'{t//3600}:{t%3600//60:02d}:{t%60:02d}' if t >= 3600 else f'{t//60}:{t%60:02d}'
        text = ' '.join(w for s in p for _, w in s)
        out += [f'**[{stamp}](https://youtu.be/{vid}?t={t})** {text}', '']
    open(f'{OUT}/{name}.md', 'w', encoding='utf-8').write('\n'.join(out))
    report.append((name[:60], len(words), len(paras), round(len(words)/max(len(paras),1)), 'NO-PUNCT' if punct < 1/60 else ''))
for r in report: print(*r, sep='\t')
print(len(report), 'files;', sum(r[1] for r in report), 'words')
