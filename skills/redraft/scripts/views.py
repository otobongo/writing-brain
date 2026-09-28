#!/usr/bin/env python3
"""Views of a draft for the redraft skill.

Prints the patterns the Writer Science method checks, so the reviewer (and the
writer) can see them: the skim view (unit openings), the topic list (sentence
openings), the introduction beside the conclusion, key terms, the punctuation
X-ray, and flags for finish-level issues.

Every flag is a place to look, not a verdict: the script cannot know the reader.

Usage:
    python3 views.py draft.md            # readable report
    python3 views.py draft.md --json     # machine-readable
    cat draft.txt | python3 views.py -   # read from stdin

Standard library only.
"""

import json
import re
import sys
from collections import Counter, OrderedDict

# ----------------------------------------------------------------------------
# Word lists (mirror references/review-finish.md; extend there and here)
# ----------------------------------------------------------------------------

FILLERS = ["actually", "basically", "certain", "various", "particularly", "really",
           "virtually", "individual", "generally", "practically", "very", "quite",
           "extremely", "literally", "simply", "just", "totally", "essentially",
           "definitely", "truly", "honestly", "it is worth noting that",
           "it is important to note that", "in terms of", "needless to say"]

DOUBLETS = ["each and every", "first and foremost", "full and complete", "true and accurate",
            "any and all", "basic and fundamental", "one and only", "various and sundry",
            "aid and abet", "cease and desist", "hope and trust", "fit and proper",
            "over and above", "if and when", "unless and until", "clear and simple"]

REDUNDANT = ["future plans", "past history", "end result", "final outcome", "free gift",
             "basic fundamentals", "consensus of opinion", "totally transform", "completely eliminate",
             "anticipate upcoming", "previous experience", "ultimate result", "suddenly astonish",
             "added bonus", "close proximity", "advance planning", "unexpected surprise",
             "new innovation", "join together", "repeat again", "collaborate together",
             "each individual", "true fact", "general consensus", "exact same", "revert back",
             "still remains", "brief summary", "past experience", "personal opinion"]
REDUNDANT_PATTERNS = [r"\b\w+ in (?:nature|size|shape|number|color|colour|character|scope)\b",
                      r"\bin an? \w+ (?:manner|fashion|way)\b",
                      r"\bat an early (?:time|stage|point)\b"]

WORDY = OrderedDict([
    ("the reason for", "why"), ("the reason why", "why"), ("despite the fact that", "although"),
    ("in spite of the fact that", "although"), ("in the event that", "if"),
    ("in a situation where", "when"), ("concerning the matter of", "about"),
    ("due to the fact that", "because"), ("owing to the fact that", "because"),
    ("at this point in time", "now"), ("at the present time", "now"),
    ("in order to", "to"), ("for the purpose of", "to / for"), ("with regard to", "about"),
    ("with respect to", "about"), ("in relation to", "about"), ("a large number of", "many"),
    ("a majority of", "most"), ("has the ability to", "can"), ("is able to", "can"),
    ("in the near future", "soon"), ("on a daily basis", "daily"), ("prior to", "before"),
    ("subsequent to", "after"), ("in close proximity to", "near"), ("the fact that", "(often cuttable)"),
    ("make a decision", "decide"), ("give consideration to", "consider"),
    ("conduct an investigation", "investigate"), ("take into consideration", "consider"),
    ("is in need of", "needs"), ("there is a need for", "(name who needs what)"),
])

NEG_EXPLICIT = ["not", "no", "never", "nor", "none", "nothing", "nobody", "neither"]
NEG_IMPLICIT = ["prevent", "prevents", "prevented", "lack", "lacks", "lacking", "fail", "fails",
                "failed", "doubt", "reject", "rejected", "avoid", "avoids", "deny", "denied",
                "refuse", "refused", "exclude", "excluded", "prohibit", "prohibited", "without",
                "unless", "except", "against", "preclude", "precludes", "contradict"]
NOT_SWAPS = OrderedDict([
    ("not different", "similar"), ("not many", "few"), ("not allow", "prevent"),
    ("not notice", "overlook"), ("not often", "rarely"), ("not include", "omit"),
    ("not the same", "different"), ("not remember", "forget"), ("not able", "unable / cannot"),
    ("not important", "trivial / minor"), ("not certain", "uncertain"), ("did not accept", "rejected"),
    ("does not have", "lacks"), ("not possible", "impossible"),
])

HEDGES = ["might", "may", "could", "perhaps", "possibly", "arguably", "somewhat", "seems", "seem",
          "appears", "appear", "likely", "probably", "at least partly", "more or less", "to some extent",
          "in some cases", "relatively", "fairly", "sort of", "kind of", "tend to", "tends to"]
ABSOLUTES = ["every", "all", "always", "never", "only", "obviously", "of course", "clearly",
             "undoubtedly", "outright", "certainly", "definitely", "absolutely", "without doubt",
             "everyone", "nobody", "completely", "entirely"]
GAP_COVER = ["obviously", "of course", "clearly", "undoubtedly", "it goes without saying"]

EMPTY_VERBS = [r"\boccur(?:s|red|ring)?\b", r"\btak(?:e|es|ing) place\b", r"\btook place\b",
               r"\bundert(?:ake|akes|ook|aken)\b", r"\bconduct(?:s|ed|ing)?\b", r"\bperform(?:s|ed|ing)?\b",
               r"\bresult(?:s|ed)? in\b", r"\blead(?:s)? to\b", r"\bled to\b",
               r"\b(?:make|makes|made|give|gives|gave|have|has|had|provide|provides|provided) (?:a |an |the )?\w+(?:tion|sion|ment|ance|ence)\b",
               r"\bthere is a need\b", r"\bwas the result of\b", r"\bis the result of\b"]
NOMINAL = re.compile(r"\b[a-z]{4,}(?:tion|sion|ment|ance|ence|ity|ure)s?\b", re.I)
NOT_NOMINAL = {"nation", "nations", "moment", "moments", "comment", "comments", "government",
               "mention", "question", "questions", "station", "future", "nature", "culture",
               "picture", "structure", "century", "city", "community", "university", "quality",
               "opportunity", "reality", "audience", "evidence", "experience", "science",
               "sentence", "sentences", "difference", "section", "sections", "fiction", "position",
               "attention", "portion", "caption", "option", "options", "procedure", "department",
               "environment", "document", "ministry", "entity", "identity", "authority", "security",
               "priority", "activity", "industry", "feature", "features", "measure", "pressure",
               "treasure", "adventure", "signature", "literature", "temperature", "creature", "failure"}

METADISCOURSE = [r"\bin this (?:article|essay|post|paper|piece|section|chapter|report|video|episode|guide)\b",
                 r"\bthis (?:article|essay|post|paper|piece|section|chapter|report) (?:will|explores|examines|discusses|looks at|covers|aims)\b",
                 r"\bthe (?:following|preceding|previous|next) (?:section|chapter|paragraph)\b",
                 r"\bas (?:mentioned|noted|discussed|stated|seen) (?:above|earlier|before|previously)\b",
                 r"\bit is (?:important|worth|interesting) to (?:note|mention|remember)\b",
                 r"\bi (?:will|am going to|'m going to) (?:discuss|explore|show|explain|talk about|cover)\b",
                 r"\blet'?s (?:dive in|get started|take a look)\b",
                 r"\b(?:firstly|secondly|thirdly|lastly)\b"]

OPENING_PATTERNS = OrderedDict([
    ("background opening", [r"\bthroughout history\b", r"\bover the (?:past|last) (?:few )?(?:decades?|years?|centur(?:y|ies))\b",
                            r"\bin today'?s\b", r"\bsince the dawn\b", r"\bfor (?:decades|centuries|years)\b",
                            r"\bhas been (?:studied|discussed|debated)\b", r"\bin recent years\b", r"\bnowadays\b"]),
    ("definition opening", [r"\bis defined as\b", r"\brefers to\b", r"\bthe (?:dictionary|term) \w+ (?:means|is)\b"]),
    ("announcement", [r"\bin this (?:article|essay|post|paper|piece|video|episode)\b",
                      r"\bthis (?:article|essay|post|paper|piece) (?:will|explores|examines|discusses)\b",
                      r"\b(?:i|we)(?:'m| am| are| will) (?:going to )?(?:discuss|explore|show|talk about|share|cover)\b",
                      r"\btoday,? (?:i|we)(?:'m| am| are| will)\b"]),
    ("gap claim", [r"\bno (?:one|study|research|studies) (?:has|have)\b", r"\bunderstudied\b",
                   r"\bremains? (?:unexplored|unclear|poorly understood)\b", r"\bgap in the literature\b",
                   r"\blittle is known\b", r"\bthe first to\b"]),
    ("writer's effort or conviction", [r"\bafter (?:months|years|weeks) of\b", r"\bi(?:'ve| have) spent\b",
                                       r"\bi believe\b", r"\bpassionate about\b", r"\bi(?:'m| am) (?:so )?excited\b",
                                       r"\bthis will change\b", r"\bmost important (?:thing|lesson)\b"]),
])

TURN_WORDS = ["but", "however", "yet", "although", "though", "instead", "by contrast", "despite",
              "unfortunately", "the problem", "the trouble", "except"]
ADDITIVE_OPENERS = ["and", "also", "furthermore", "moreover", "in addition", "additionally", "plus"]

VALUE_WORDS = ["enable", "enables", "unlock", "unlocks", "prevent", "prevents", "erode", "erodes",
               "limit", "limits", "cost", "costs", "risk", "risks", "critical", "crucial", "essential",
               "before", "problem", "mistake", "fail", "fails", "lose", "loses", "waste", "wastes",
               "save", "saves", "gain", "but", "however", "although", "instead", "why", "matters"]

CLICHES = ["game changer", "game-changer", "move the needle", "at the end of the day", "low-hanging fruit",
           "think outside the box", "paradigm shift", "tapestry of", "navigate the landscape",
           "in today's fast-paced", "take it to the next level", "unlock the power", "a testament to",
           "best of both worlds", "tip of the iceberg", "win-win", "circle back", "deep dive",
           "leverage synergies", "hit the ground running", "cutting-edge", "world-class", "seamless"]

PEOPLE_LABELS = ["passionate", "brilliant", "dedicated", "visionary", "tireless", "driven",
                 "hardworking", "hard-working", "results-oriented", "detail-oriented", "innovative",
                 "dynamic", "rockstar", "ninja", "guru", "motivated", "enthusiastic"]

WEAK_ENDINGS = re.compile(
    r"(?:\b(?:it|them|this|that|these|those|him|her|us|me|there|here|as well|too|also|etc|"
    r"of|to|for|with|about|from|on|in|at|by|up|out|in this regard|and so on|in general|"
    r"(?:according to|said|says|notes|noted|writes) [\w .'-]{1,40}))\W*$", re.I)

STOPWORDS = set("""a an the and or but if then so of to in on at by for with from as is are was were be been being
it its it's this that these those there here their they them we our us you your i me my he she his her him
not no do does did done have has had having can could will would should may might must shall
what which who whom whose when where why how all any each every some such more most other than too very
just also only into over under about after before between through during out up down off again
further once both few own same s t don now one two three new like get got make made even much many well
really because while though although yet still ever never always often""".split())

PRONOUN_OPENERS = {"it", "its", "they", "their", "them", "this", "these", "that", "those", "he", "she",
                   "his", "her", "we", "our", "such", "both", "each"}

ABBREV = ["e.g.", "i.e.", "etc.", "vs.", "Mr.", "Mrs.", "Ms.", "Dr.", "Prof.", "St.", "U.S.", "U.K.",
          "a.m.", "p.m.", "No.", "Fig.", "cf.", "approx.", "Inc.", "Ltd.", "Co."]


# ----------------------------------------------------------------------------
# Parsing
# ----------------------------------------------------------------------------

def strip_markdown(s):
    s = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"(\*\*|__|\*|_|`)", "", s)
    return s.strip()


def split_sentences(text):
    t = text
    for i, a in enumerate(ABBREV):
        t = t.replace(a, a.replace(".", "\u2024"))
    t = re.sub(r"(\d)\.(\d)", "\\1\u2024\\2", t)
    parts = re.split(r"(?<=[.!?])[\"'\u201d\u2019)\]]*\s+(?=[\"'\u201c\u2018(\[]?[A-Z0-9])", t)
    return [p.replace("\u2024", ".").strip() for p in parts if p.strip()]


def is_heading(line, next_is_para):
    s = line.strip()
    if s.startswith("#"):
        return True
    words = s.split()
    return (next_is_para and 0 < len(words) <= 10 and not re.search(r"[.!?:;,]$", s)
            and not s.startswith(("-", "*", "\u2022")) and s[0:1].isupper())


def parse(raw):
    raw = raw.replace("\r\n", "\n")
    blocks = [b for b in re.split(r"\n\s*\n", raw) if b.strip()]
    units = []  # list of dict: kind heading|para|list, text
    for bi, b in enumerate(blocks):
        lines = [l for l in b.split("\n") if l.strip()]
        # a heading line glued on top of a paragraph
        if len(lines) > 1 and lines[0].strip().startswith("#"):
            units.append({"kind": "heading", "text": strip_markdown(lines[0].lstrip("# "))})
            lines = lines[1:]
        if all(re.match(r"\s*(?:[-*\u2022]|\d+[.)])\s+", l) for l in lines):
            units.append({"kind": "list", "text": " ".join(strip_markdown(re.sub(r"^\s*(?:[-*\u2022]|\d+[.)])\s+", "", l)) for l in lines),
                          "items": [strip_markdown(re.sub(r"^\s*(?:[-*\u2022]|\d+[.)])\s+", "", l)) for l in lines]})
            continue
        text = strip_markdown(" ".join(l.strip() for l in lines))
        nxt = bi + 1 < len(blocks)
        if len(lines) == 1 and is_heading(lines[0], nxt):
            units.append({"kind": "heading", "text": strip_markdown(lines[0].lstrip("# "))})
        else:
            units.append({"kind": "para", "text": text})
    # title: first heading if it comes first
    title = units[0]["text"] if units and units[0]["kind"] == "heading" else None
    # sections
    sections, cur = [], {"heading": None, "paras": []}
    pn = 0
    for u in units:
        if u["kind"] == "heading":
            if cur["heading"] is not None or cur["paras"]:
                sections.append(cur)
            cur = {"heading": u["text"], "paras": []}
        else:
            pn += 1
            sents = split_sentences(u["text"]) if u["kind"] == "para" else u["items"]
            cur["paras"].append({"n": pn, "kind": u["kind"], "text": u["text"], "sents": sents})
    sections.append(cur)
    if title and sections and sections[0]["heading"] == title and not sections[0]["paras"]:
        sections = sections[1:]
    elif title and sections and sections[0]["heading"] == title:
        sections[0]["heading"] = None if len(sections) > 1 else sections[0]["heading"]
    paras = [p for s in sections for p in s["paras"]]
    return title, sections, paras


# ----------------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------------

def words(s):
    return re.findall(r"[A-Za-z][A-Za-z'\-]*|\d[\d,.%]*", s)


def stem(w):
    w = w.lower().strip("'")
    for suf in ("ations", "ation", "ings", "ing", "ies", "ied", "es", "ed", "ly", "s"):
        if len(w) > len(suf) + 3 and w.endswith(suf):
            return w[: -len(suf)]
    return w


def content(ws):
    return [stem(w) for w in ws if w.lower() not in STOPWORDS and len(w) > 2 and not w[0].isdigit()]


def unquote(s):
    return re.sub(r"[\"\u201c][^\"\u201d]{0,400}[\"\u201d]", " ", s)


def phrase_hits(text, phrases):
    low = " " + text.lower() + " "
    out = []
    for p in phrases:
        if re.search(r"(?<![\w-])" + re.escape(p) + r"(?![\w-])", low):
            out.append(p)
    return out


def regex_hits(text, patterns):
    out = []
    for p in patterns:
        m = re.search(p, text, re.I)
        if m:
            out.append(m.group(0))
    return out


def opener(s, n=8):
    ws = s.split()
    return " ".join(ws[:n]) + (" \u2026" if len(ws) > n else "")


def index_of(p):
    s = p["sents"]
    if not s:
        return ""
    first = s[0]
    if len(s) > 1 and (len(first.split()) < 8 or first.rstrip().endswith((":", "?"))):
        return first + " " + s[1]
    return first


def fmt_ref(p, si=None):
    return "P%d" % p["n"] + ("" if si is None else ".S%d" % (si + 1))


# ----------------------------------------------------------------------------
# Views
# ----------------------------------------------------------------------------

def skim_view(title, sections):
    rows = []
    for s in sections:
        entry = {"heading": s["heading"], "paras": []}
        for p in s["paras"]:
            idx = index_of(p)
            flags = []
            if p["kind"] == "para":
                o = idx.strip()
                if re.match(r"^(?:in )?(?:\d{4}|(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\w*\b)", o, re.I):
                    flags.append("opens on a date")
                if re.match(r"^[\d$\u00a3\u20ac]", o) or re.match(r"^\S+%", o):
                    flags.append("opens on a number")
                if o[:1] in "\"\u201c":
                    flags.append("opens on a quotation")
                if re.match(r"^(?:for example|for instance|one day|once upon)\b", o, re.I):
                    flags.append("opens on an example or story")
                if re.search(r"\([A-Z][A-Za-z]+(?: et al\.?)?,? \d{4}\)", o.split(",")[0]):
                    flags.append("opens on a citation")
                if re.match(r"^(?:however|additionally|moreover|furthermore|also|and|but|so|then|next|finally)[,]?\s*$", o.split(" ")[0].lower()):
                    pass
            entry["paras"].append({"ref": fmt_ref(p), "kind": p["kind"], "index": idx, "flags": flags,
                                   "sentences": len(p["sents"])})
        rows.append(entry)
    return {"title": title, "sections": rows}


def topic_view(paras):
    out = []
    for p in paras:
        if p["kind"] != "para" or len(p["sents"]) < 2:
            continue
        first_c = set(content(words(p["sents"][0])))
        rows = []
        for i, s in enumerate(p["sents"]):
            op = opener(s)
            link = ""
            if i > 0:
                prev_end = set(content(words(" ".join(p["sents"][i - 1].split()[-8:]))))
                op_c = set(content(words(" ".join(s.split()[:8]))))
                first_word = (s.split() or [""])[0].lower().strip(",")
                if op_c & prev_end:
                    link = "picks up the end of the previous sentence"
                elif op_c & first_c or first_word in PRONOUN_OPENERS:
                    link = "links to the paragraph's topic"
                else:
                    link = "starts somewhere new"
            rows.append({"ref": fmt_ref(p, i), "opening": op, "link": link})
        new_count = sum(1 for r in rows if r["link"] == "starts somewhere new")
        out.append({"ref": fmt_ref(p), "openings": rows, "new_starts": new_count})
    return out


def intro_conclusion(paras):
    body = [p for p in paras if p["kind"] == "para"]
    if not body:
        return {}
    intro = body[:2] if len(body) > 4 else body[:1]
    concl = body[-2:] if len(body) > 4 else body[-1:]
    it = " ".join(p["text"] for p in intro)
    ct = " ".join(p["text"] for p in concl)
    iw, cw = set(content(words(it))), set(content(words(ct)))
    overlap = round(100 * len(iw & cw) / max(1, len(iw | cw)))
    turns = phrase_hits(it, TURN_WORDS)
    intro_sents = [s for p in intro for s in p["sents"]]
    first_turn = next((i for i, s in enumerate(intro_sents) if phrase_hits(s, TURN_WORDS)), None)
    concl_open = concl[0]["sents"][0] if concl[0]["sents"] else ""
    flags = []
    if not turns:
        flags.append("no turn word (but / however / yet ...) in the introduction: is there a problem?")
    if re.match(r"^(?:in (?:summary|conclusion|closing)|to (?:sum up|summari[sz]e|conclude)|overall|all in all)\b", concl_open, re.I):
        flags.append("conclusion opens as a summary")
    if overlap >= 45:
        flags.append("introduction and conclusion share many words: restatement rather than push-off?")
    return {
        "introduction": [fmt_ref(p) for p in intro], "conclusion": [fmt_ref(p) for p in concl],
        "intro_last_sentence": intro_sents[-1] if intro_sents else "",
        "intro_first_turn": (intro_sents[first_turn] if first_turn is not None else None),
        "conclusion_last_sentence": concl[-1]["sents"][-1] if concl[-1]["sents"] else "",
        "word_overlap_percent": overlap, "turn_words_in_intro": turns, "flags": flags,
        "intro_text": it, "conclusion_text": ct,
    }


def opening_patterns(paras):
    body = [p for p in paras if p["kind"] == "para"]
    first = " ".join(s for p in body[:2] for s in p["sents"][:3])[:900]
    hits = OrderedDict()
    for label, pats in OPENING_PATTERNS.items():
        h = regex_hits(first, pats)
        if h:
            hits[label] = h
    return hits


def connectors(paras):
    body = [p for p in paras if p["kind"] == "para"]
    additive_runs, however_openers, prev_however = [], [], False
    run = []
    for p in body:
        for i, s in enumerate(p["sents"]):
            fw = s.lower()
            if any(re.match(r"^" + re.escape(a) + r"\b", fw) for a in ADDITIVE_OPENERS):
                run.append(fmt_ref(p, i))
            else:
                if len(run) >= 3:
                    additive_runs.append(run)
                run = []
        is_h = bool(p["sents"]) and p["sents"][0].lower().startswith("however")
        if is_h and prev_however:
            however_openers.append(fmt_ref(p))
        prev_however = is_h
    if len(run) >= 3:
        additive_runs.append(run)
    text = " ".join(p["text"] for p in body)
    nwords = max(1, len(words(text)))
    return {"however_count": len(re.findall(r"\bhowever\b", text, re.I)),
            "however_per_1000_words": round(1000 * len(re.findall(r"\bhowever\b", text, re.I)) / nwords, 1),
            "consecutive_paragraphs_opening_however": however_openers,
            "runs_of_additive_openers": additive_runs}


def finish_scan(paras):
    flags = []

    def add(kind, ref, detail, sent):
        flags.append({"kind": kind, "ref": ref, "detail": detail, "sentence": sent})

    you_run = []
    for p in paras:
        for i, s in enumerate(p["sents"]):
            ref = fmt_ref(p, i)
            sq = unquote(s)
            low = sq.lower()
            f = phrase_hits(sq, FILLERS)
            if len(f) >= 2:
                add("fillers", ref, ", ".join(f), s)
            for d in phrase_hits(sq, DOUBLETS):
                add("doublet", ref, d, s)
            for r in phrase_hits(sq, REDUNDANT) + regex_hits(sq, REDUNDANT_PATTERNS):
                add("redundancy", ref, r, s)
            for w in phrase_hits(sq, list(WORDY.keys())):
                add("wordy phrase", ref, "%s \u2192 %s" % (w, WORDY[w]), s)
            neg = len(re.findall(r"\b(?:%s)\b|n't\b" % "|".join(NEG_EXPLICIT), low)) + len(phrase_hits(sq, NEG_IMPLICIT))
            if neg >= 2:
                add("stacked negatives", ref, "%d negatives in one sentence" % neg, s)
            for w in phrase_hits(sq, list(NOT_SWAPS.keys())):
                add("negative with a positive form", ref, "%s \u2192 %s" % (w, NOT_SWAPS[w]), s)
            h = phrase_hits(sq, HEDGES)
            if len(h) >= 2:
                add("stacked hedges", ref, ", ".join(h), s)
            a = phrase_hits(sq, ABSOLUTES)
            if len(a) >= 2:
                add("stacked absolutes", ref, ", ".join(a), s)
            for g in phrase_hits(sq, GAP_COVER):
                add("certainty word that may cover a gap", ref, g, s)
            ev = regex_hits(sq, EMPTY_VERBS)
            noms = [m for m in NOMINAL.findall(sq) if m.lower() not in NOT_NOMINAL]
            if ev and noms:
                add("empty verb + nominalisation", ref, "%s / %s" % (", ".join(ev), ", ".join(noms[:3])), s)
            elif len(noms) >= 3:
                add("nominalisation cluster", ref, ", ".join(noms[:4]), s)
            if re.match(r"^(?:there (?:is|are|was|were)|it (?:is|was) (?:\w+ )?(?:that|to)|this is (?:why|how|the reason|what))\b", low.strip()):
                add("dummy subject", ref, " ".join(s.split()[:5]), s)
            for m in regex_hits(sq, METADISCOURSE):
                add("metadiscourse", ref, m, s)
            for c in phrase_hits(sq, CLICHES):
                add("stock phrase (ask: what does this show?)", ref, c, s)
            for lab in phrase_hits(sq, PEOPLE_LABELS):
                add("label on a person (show, don't label?)", ref, lab, s)
            if p["kind"] == "para" and WEAK_ENDINGS.search(sq.rstrip(" .!?\"'\u201d")+" .") and len(s.split()) > 6:
                m = WEAK_ENDINGS.search(sq.rstrip(" .!?\"'\u201d") + " .")
                add("weak word in the stress position", ref, m.group(0).strip(" ."), s)
            if re.match(r"^you\b", low.strip()):
                you_run.append(ref)
            else:
                if len(you_run) >= 3:
                    add("run of sentences with 'you' as subject", you_run[0], "%d in a row" % len(you_run), "")
                you_run = []
            internal = re.findall(r"[,;:()\u2014\u2013]|--", s[:-1])
            if len(internal) >= 5:
                add("heavily punctuated sentence (see X-ray)", ref, "%d internal marks" % len(internal), s)
    # em dashes and one-sentence paragraph runs
    body = [p for p in paras if p["kind"] == "para"]
    text = " ".join(p["text"] for p in body)
    dashes = len(re.findall(r"\u2014|\s--\s|\s\u2013\s", text))
    one_runs, run = [], []
    for p in body:
        if len(p["sents"]) == 1:
            run.append(fmt_ref(p))
        else:
            if len(run) >= 3:
                one_runs.append(run)
            run = []
    if len(run) >= 3:
        one_runs.append(run)
    return {"flags": flags,
            "em_dashes": dashes, "em_dashes_per_1000_words": round(1000 * dashes / max(1, len(words(text))), 1),
            "runs_of_one_sentence_paragraphs": one_runs}


def xray(paras):
    out = []
    for p in paras:
        if p["kind"] != "para":
            continue
        marks = []
        for s in p["sents"]:
            marks.append(re.sub(r"[^,;:()\u2014\u2013?!.\"\u201c\u201d-]", "", s) or ".")
        out.append({"ref": fmt_ref(p), "xray": "  ".join(marks)})
    return out


def key_terms(title, sections, paras):
    body = [p for p in paras if p["kind"] == "para"]
    ws = [w.lower() for p in body for w in words(p["text"])]
    uni = Counter(w for w in ws if w not in STOPWORDS and len(w) > 3 and not w[0].isdigit())
    bi = Counter()
    for p in body:
        pw = [w.lower() for w in words(p["text"])]
        for a, b in zip(pw, pw[1:]):
            if a not in STOPWORDS and b not in STOPWORDS and len(a) > 2 and len(b) > 2:
                bi[a + " " + b] += 1
    terms = {"top_words": uni.most_common(15), "top_phrases": [x for x in bi.most_common(12) if x[1] > 1]}
    if title:
        tnouns = [w for w in words(title) if w.lower() not in STOPWORDS and len(w) > 3]
        intro_text = " ".join(p["text"] for p in body[:2]).lower()
        report = []
        for t in tnouns:
            st = stem(t)
            where = [fmt_ref(p) for p in body if st in [stem(w) for w in words(p["text"])]]
            report.append({"title_word": t, "in_introduction": st in [stem(w) for w in words(intro_text)],
                           "appears_in": where[:12], "count": len(where)})
        terms["title_words"] = report
    heads = []
    for s in sections:
        if not s["heading"] or not s["paras"]:
            continue
        hc = set(content(words(s["heading"])))
        sc = Counter(content(words(" ".join(p["text"] for p in s["paras"]))))
        top = set(w for w, _ in sc.most_common(25))
        heads.append({"heading": s["heading"], "shares_words_with_section": sorted(hc & top)})
    terms["headings"] = heads
    return terms


def value_words(paras):
    rows = []
    for p in paras:
        if p["kind"] != "para" or not p["sents"]:
            continue
        rows.append({"ref": fmt_ref(p), "in_opening": phrase_hits(p["sents"][0], VALUE_WORDS)})
    with_none = [r["ref"] for r in rows if not r["in_opening"]]
    return {"paragraph_openings_without_value_words": with_none, "total_paragraphs": len(rows)}


def build(raw):
    title, sections, paras = parse(raw)
    body = [p for p in paras if p["kind"] == "para"]
    stats = {"words": len(words(" ".join(p["text"] for p in paras))), "paragraphs": len(body),
             "lists": len([p for p in paras if p["kind"] == "list"]),
             "sections": len([s for s in sections if s["heading"]]),
             "sentences": sum(len(p["sents"]) for p in body)}
    return OrderedDict([
        ("stats", stats), ("skim", skim_view(title, sections)), ("intro_conclusion", intro_conclusion(paras)),
        ("opening_patterns", opening_patterns(paras)), ("topics", topic_view(paras)),
        ("key_terms", key_terms(title, sections, paras)), ("value_words", value_words(paras)),
        ("connectors", connectors(paras)), ("finish", finish_scan(paras)), ("xray", xray(paras)),
    ])


# ----------------------------------------------------------------------------
# Readable report
# ----------------------------------------------------------------------------

def render(v):
    L = []
    st = v["stats"]
    L.append("VIEWS (flags are places to look, not verdicts; judge each against the reader)")
    L.append("%d words, %d paragraphs, %d sections, %d lists. Refs: P = paragraph, S = sentence." %
             (st["words"], st["paragraphs"], st["sections"], st["lists"]))

    L.append("\n== 1. SKIM VIEW: only the openings. Do they tell the whole story? ==")
    if v["skim"]["title"]:
        L.append("TITLE: " + v["skim"]["title"])
    for s in v["skim"]["sections"]:
        if s["heading"]:
            L.append("\n## " + s["heading"])
        for p in s["paras"]:
            tag = " [list]" if p["kind"] == "list" else ""
            fl = ("   <- " + "; ".join(p["flags"])) if p["flags"] else ""
            L.append("  %s%s: %s%s" % (p["ref"], tag, p["index"][:260], fl))

    ic = v["intro_conclusion"]
    if ic:
        L.append("\n== 2. INTRODUCTION beside CONCLUSION: underline the point in each; are they the same point? ==")
        L.append("Introduction (%s) ends: %s" % (", ".join(ic["introduction"]), ic["intro_last_sentence"]))
        L.append("First turn in the introduction: %s" % (ic["intro_first_turn"] or "(none)"))
        L.append("Conclusion (%s) ends: %s" % (", ".join(ic["conclusion"]), ic["conclusion_last_sentence"]))
        L.append("Word overlap: %d%%" % ic["word_overlap_percent"])
        for f in ic["flags"]:
            L.append("  ! " + f)
    if v["opening_patterns"]:
        L.append("\n== 3. OPENING PATTERNS in the first sentences ==")
        for k, h in v["opening_patterns"].items():
            L.append("  ! %s: %s" % (k, "; ".join(h)))

    L.append("\n== 4. TOPIC LIST: the first words of each sentence. Who is each paragraph about? ==")
    for t in v["topics"]:
        L.append("%s  (%d of %d sentences start somewhere new)" % (t["ref"], t["new_starts"], len(t["openings"])))
        for r in t["openings"]:
            L.append("    %-7s %-62s %s" % (r["ref"].split(".")[1], r["opening"][:62], ("\u21b3 " + r["link"]) if r["link"] else ""))

    kt = v["key_terms"]
    L.append("\n== 5. KEY TERMS ==")
    L.append("Most used words: " + ", ".join("%s (%d)" % x for x in kt["top_words"]))
    if kt["top_phrases"]:
        L.append("Repeated phrases: " + ", ".join("%s (%d)" % x for x in kt["top_phrases"]))
    for t in kt.get("title_words", []):
        L.append("  title word '%s': %s in the introduction; in %d paragraphs %s" %
                 (t["title_word"], "appears" if t["in_introduction"] else "NOT", t["count"], ", ".join(t["appears_in"])))
    for h in kt["headings"]:
        L.append("  heading '%s' shares with its section: %s" % (h["heading"], ", ".join(h["shares_words_with_section"]) or "NOTHING (cryptic heading?)"))

    vw = v["value_words"]
    L.append("\n== 6. VALUE WORDS at paragraph openings ==")
    L.append("%d of %d paragraph openings have no problem/benefit/turn word: %s" %
             (len(vw["paragraph_openings_without_value_words"]), vw["total_paragraphs"],
              ", ".join(vw["paragraph_openings_without_value_words"][:30])))

    c = v["connectors"]
    L.append("\n== 7. CONNECTORS ==")
    L.append("'however': %d (%.1f per 1,000 words)" % (c["however_count"], c["however_per_1000_words"]))
    for r in c["runs_of_additive_openers"]:
        L.append("  ! run of additive openers (and / also / furthermore): " + ", ".join(r))
    if c["consecutive_paragraphs_opening_however"]:
        L.append("  ! consecutive paragraphs opening 'However': " + ", ".join(c["consecutive_paragraphs_opening_however"]))

    f = v["finish"]
    L.append("\n== 8. FINISH FLAGS (drop false alarms: quotes, warnings, field terms, deliberate choices) ==")
    L.append("em dashes: %d (%.1f per 1,000 words)" % (f["em_dashes"], f["em_dashes_per_1000_words"]))
    for r in f["runs_of_one_sentence_paragraphs"]:
        L.append("  run of one-sentence paragraphs: " + ", ".join(r))
    by = OrderedDict()
    for x in f["flags"]:
        by.setdefault(x["kind"], []).append(x)
    for k, xs in by.items():
        L.append("- %s (%d)" % (k, len(xs)))
        for x in xs[:12]:
            L.append("    %-8s %s%s" % (x["ref"], x["detail"], ("   | " + x["sentence"][:110]) if x["sentence"] else ""))
        if len(xs) > 12:
            L.append("    ... %d more" % (len(xs) - 12))

    L.append("\n== 9. PUNCTUATION X-RAY (little between full stops = simply built sentences) ==")
    for x in v["xray"]:
        L.append("  %-5s %s" % (x["ref"], x["xray"][:160]))
    return "\n".join(L)


def main(argv):
    if len(argv) < 2 or argv[1] in ("-h", "--help"):
        print(__doc__)
        return 0
    src = argv[1]
    raw = sys.stdin.read() if src == "-" else open(src, encoding="utf-8", errors="replace").read()
    v = build(raw)
    if "--json" in argv:
        print(json.dumps(v, indent=1, ensure_ascii=False))
    else:
        print(render(v))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
