"""Concept list with search patterns. Run: python3 concepts_seed.py -> concept_candidates.json"""
import re, json, glob

CONCEPTS = [
 # (group, name, [regex patterns, case-insensitive])
 ("Axioms","Tools, not rules", [r"writing tools?,? not (writing )?rules", r"no (universal )?(writing )?rules.{0,20}only (writing )?tools", r"rules? (versus|vs\.?|and) tools"]),
 ("Axioms","No universal readers", [r"no universal (rules|readers)", r"universal reader"]),
 ("Axioms","Reader decides what good writing is", [r"reader'?s? (decide|determine)", r"function of the reader'?s? experience", r"writing (isn'?t|is not) a thing.{0,15}function"]),
 ("Axioms","Value = solving a reader's problem", [r"clear.{0,40}useless", r"value,? value,? value", r"perceive (a )?problem.{0,30}perceive value"]),
 ("Axioms","Change the reader's ideas, not express yours", [r"change (the |your )?reader'?s? (ideas|mind|thinking)", r"not (about )?(self.?)?express"]),
 ("Axioms","Writing is thinking", [r"writing is thinking", r"extension of (your |my |our )?thinking", r"write (first|to) (and )?(understand|find out|think)"]),
 ("Two phases","Writer's draft vs reader draft", [r"writer'?s draft", r"reader'?s? draft", r"two (drafts|documents|phases|functions|processes)"]),
 ("Two phases","Interference (writing vs reading patterns)", [r"interference", r"writing patterns?.{0,40}reading patterns?", r"reading patterns"]),
 ("Two phases","Artist and architect", [r"artist.{0,30}architect", r"architect.{0,30}artist"]),
 ("Two phases","Door closed / door open", [r"door closed", r"door open"]),
 ("Two phases","Magma / volcano freewriting", [r"magma", r"volcano"]),
 ("Two phases","Coffee stain problem", [r"coffee stain"]),
 ("Two phases","Briefed reader (Carnegie Mellon study)", [r"briefed reader", r"carnegie mellon"]),
 ("Two phases","Directions to the restaurant", [r"directions to (the|a) restaurant", r"restaurant.{0,60}directions", r"how to get to (the|a) restaurant"]),
 ("Two phases","Christmas lights / tangled expertise", [r"christmas lights"]),
 ("Two phases","Reverse outline", [r"reverse outline", r"outline what you (actually )?have"]),
 ("Two phases","Skim test", [r"skim test", r"skim(ming)? (the |your )?(text|essay|index)"]),
 ("Process","Timed freewriting / non-editing", [r"set a timer", r"non.?editing", r"free.?writ", r"brain dump", r"morning pages"]),
 ("Process","Placeholders while drafting", [r"placeholder", r"\[find a better word\]", r"square brackets?"]),
 ("Process","Question at the top of the page / tether", [r"question at the top", r"tether", r"top of the page"]),
 ("Process","Question, not topic", [r"question,? not (a )?topic", r"topic.{0,40}question.{0,40}(reason|filter)", r"question is your filter", r"topic gives you"]),
 ("Process","Inquiry method (evidence + reasoning = claim)", [r"inquiry method", r"evidence (plus|\+|and) reasoning", r"reasoning equals? (a )?claim"]),
 ("Process","Reading is food, not fuel", [r"food,? not fuel", r"writing gets hungry"]),
 ("Process","Virtuous procrastination", [r"virtuous procrastination"]),
 ("Process","Writer's block as fear", [r"writer'?s block", r"fear.{0,40}metal detector", r"metal detector"]),
 ("Process","Writing anorexia / don't cut early", [r"anorexia", r"prun(e|ing) (too )?early", r"cut(ting)? too early"]),
 ("Process","Elephant and rider / night shift (unconscious)", [r"elephant", r"night shift", r"kekul"]),
 ("Process","Lacan: Imaginary, Symbolic, Real", [r"lacan", r"jouissance", r"the imaginary", r"the symbolic"]),
 ("Process","Aim low / small daily goals", [r"aim low", r"250 words", r"1,?000 words a day", r"two pages a day"]),
 ("Process","Wile E. Coyote rule", [r"coyote"]),
 ("Process","Zettelkasten / fleeting, literature, permanent notes", [r"zettelkasten", r"fleeting note", r"literature note", r"permanent note"]),
 ("Process","Copy work / steal style", [r"copy ?work", r"steal (their |your |the )?style", r"style is open source", r"typed? (out|up) (the )?(whole|entire)"]),
 ("Process","Great Sentences Mad Libs", [r"mad ?libs"]),
 ("Process","Sentence bird-watching / collect sentences", [r"bird.?watching", r"collect(ing)? (great |striking |interesting )?sentences"]),
 ("Reader","Know your reader / four reader questions", [r"know (exactly )?(who|your) (you'?re writing for|reader)", r"what motivated them", r"what decision"]),
 ("Reader","Uninformed, indifferent, resistant readers", [r"uninformed", r"indifferent reader", r"resistant reader"]),
 ("Reader","Rhetorical planning wheel / situational network", [r"planning wheel", r"situational network"]),
 ("Reader","Joint attention / classic scene / blending", [r"joint attention", r"classic scene", r"blending"]),
 ("Reader","Code words / secret language / value words", [r"code words?", r"secret (language|handshake)", r"value.?words?", r"value.?coded"]),
 ("Reader","Anthropologist exercise (mine community texts)", [r"anthropologist", r"four or five (pieces|texts|articles)", r"4 or 5"]),
 ("Reader","Problem statement template (topic/question/benefit)", [r"i am writing about", r"in order to help my reader", r"because i want to find out"]),
 ("Reader","Two-player game / genre as functions", [r"two.?player", r"starbucks", r"genre is", r"function(s)? (of|that) (the )?(text|sentence|genre)"]),
 ("Reader","Enter the conversation politely", [r"enter(ing)? (the|a) conversation", r"big kahuna", r"table of researchers", r"same side of the table"]),
 ("Reader","Audience capture", [r"audience capture"]),
 ("Reader","Expressionist vs rationalist / positivist", [r"expressionis", r"rationalis", r"positivis"]),
 ("Reader","Knowledge as puzzle vs model; the gap model", [r"puzzle piece", r"gap model", r"lacuna", r"nobody has (studied|explored|looked)"]),
 ("Value","Problem framework (status quo, concession, destabilizing condition, cost, solution)", [r"status quo", r"destabiliz", r"concession", r"common ground"]),
 ("Value","Condition + consequence; the 'so what?' test", [r"so what\??[\'\" ]", r"condition.{0,40}consequence", r"condition with no cost"]),
 ("Value","Practical vs conceptual problems", [r"conceptual problem", r"practical problem"]),
 ("Value","Language of instability (but, however)", [r"instability", r"language of continuity", r"catnip"]),
 ("Value","Martini glass / school essay", [r"martini", r"inverted triangle", r"paid reader", r"teachers? (are|is) (paid|hostage)"]),
 ("Value","Point sentence at the end of the introduction", [r"point sentence", r"end of the (introduction|beginning)", r"point first", r"point last"]),
 ("Value","Claim: significant, non-obvious, debatable / falsifiable", [r"non.?obvious", r"debatable", r"falsifiable", r"water is wet"]),
 ("Value","Claim, evidence, warrant / point, reason, evidence", [r"warrant", r"point.{0,10}reason.{0,10}evidence", r"logical (gap|bridge)"]),
 ("Value","Hedges and boosters / certainty calibration", [r"hedg", r"booster", r"strident", r"calibrat"]),
 ("Value","Three standard objections", [r"objection", r"beat (them|readers) to"]),
 ("Value","3V: Vow, Victim, Villain", [r"\bvow\b", r"\bvictim\b", r"\bvillain\b"]),
 ("Value","Six types of nonfiction books", [r"personal brand builder", r"new authority", r"lead getter", r"booking agent", r"legacy book", r"the gift"]),
 ("Value","Chapter titles as promises", [r"chapter.{0,30}promise", r"makes? a promise"]),
 ("Value","Purpose chain / table of contents as bridge", [r"purpose chain", r"table of contents", r"bridge"]),
 ("Value","Text as a stage / limit the cast", [r"(on|the|a) stage\b", r"cast of characters", r"spotlight"]),
 ("Structure","Index and discussion (fractal)", [r"index (and|/) discussion", r"index position", r"fractal", r"index section"]),
 ("Structure","Key terms / topic strings / constellation", [r"key terms?", r"topic string", r"constellation"]),
 ("Structure","Uneven U / five levels of specificity", [r"uneven u", r"levels? of (specificity|abstraction|generality)", r"level (four|five|4|5)"]),
 ("Structure","Hit-and-run quotation", [r"hit.?and.?run"]),
 ("Structure","Four signals of coherence; cohesion vs coherence", [r"cohesion", r"coherence", r"jigsaw"]),
 ("Structure","Private, contextual, textual structure (number series)", [r"private structure", r"contextual structure", r"textual structure", r"fibonacci", r"phone number"]),
 ("Structure","Metadiscourse / signposting", [r"metadiscourse", r"signpost"]),
 ("Structure","Grice's maxims", [r"grice", r"grace'?s maxims?"]),
 ("Structure","Conclusion: push off, end higher", [r"push off", r"conclusion.{0,60}(summary|summar)", r"see,? (i )?told you"]),
 ("Structure","Title: four intrigue / curiosity triggers", [r"curiosity (loop|trigger)", r"intrigue", r"violat(e|ing) expectation", r"headline"]),
 ("Structure","Opening image / opening number (CNF)", [r"opening (image|number|metaphor)", r"web of signification"]),
 ("Structure","Foreground vs background (narrative)", [r"foreground", r"background.{0,20}(research|papers)"]),
 ("Structure","Zadie Smith's six-arrow rectangle", [r"rectangle", r"six arrows?", r"devil'?s advocate", r"impersonal essay"]),
 ("Structure","Bilbo moment / AAB examples", [r"bilbo", r"gandalf", r"\ba a b\b", r"aab"]),
 ("Sentence","Characters as subjects, actions as verbs", [r"characters? (in|as) (the )?subject", r"actions? (in|as) (the )?verb", r"who does what"]),
 ("Sentence","Zombie nouns / nominalizations", [r"zombie", r"nominaliz"]),
 ("Sentence","Empty verbs", [r"empty verb", r"flabby", r"resulted in", r"took place"]),
 ("Sentence","Short subject, verb early (tunnel / locomotive)", [r"tunnel", r"locomotive", r"hold (their|your) breath", r"long (grammatical )?subject"]),
 ("Sentence","Topic position and stress position", [r"topic position", r"stress position", r"prime real estate", r"topic and comment", r"\bthe comment\b"]),
 ("Sentence","Old to new information flow", [r"old (to|and|before) new", r"old information", r"new information", r"familiar.{0,30}(first|start|beginning)"]),
 ("Sentence","Relay race / baton / shaking hands (sentence handoff)", [r"relay", r"baton", r"shak(e|ing) hands", r"swimmer", r"battery"]),
 ("Sentence","Passive voice as a tool", [r"passive (voice|construction|sentence)"]),
 ("Sentence","Movie-poster test", [r"movie poster"]),
 ("Sentence","First 7–8 words diagnostic", [r"first (seven|eight|7|8)", r"seven or eight words"]),
 ("Sentence","Reader-question test (bees make honey)", [r"bees make honey", r"honey is made", r"reader'?s? question"]),
 ("Sentence","Four topic-progression patterns", [r"constant topic", r"linking pattern", r"whole.?to.?parts", r"theme preview", r"umbrella"]),
 ("Sentence","Mental briefcase / working memory", [r"briefcase", r"working memory", r"three to four items", r"chunk"]),
 ("Sentence","Concrete language / stub your toe / ladder of abstraction", [r"stub (your|their) toe", r"ladder of abstraction", r"visual brain", r"smokestack"]),
 ("Sentence","Intuition pump", [r"intuition pump"]),
 ("Sentence","Since vs because; ', which' clauses; -ing reductions", [r"\bsince\b.{0,40}\bbecause\b", r"non.?restrictive", r"relative clause", r"non.?finite"]),
 ("Sentence","Strategic repetition; don't vary for variety", [r"strategic repetition", r"vary (your )?(sentence|word|opening)", r"avoid repetition", r"elegant variation"]),
 ("Sentence","Sentence length myth (Provost)", [r"provost", r"sentence length", r"vary (the )?length", r"music"]),
 ("Sentence","Jargon as membership card", [r"jargon", r"membership card", r"stochastic", r"non.?trivial"]),
 ("Sentence","Author-splaining / ellipsis in dialogue", [r"author.?splain", r"ellipsis", r"adverb"]),
 ("Compression","Filler, doublets, redundancy", [r"filler", r"doublet", r"redundan", r"throat.?clearing", r"each and every"]),
 ("Compression","Affirmative over negative", [r"affirmative", r"negative", r"implicit negative"]),
 ("Compression","Exact word (le mot juste)", [r"mot juste", r"exact word", r"despite the fact that"]),
 ("Compression","Punctuation X-ray / minimalism (McCarthy)", [r"x.?ray", r"thumbprint", r"minimalis", r"do you need that"]),
 ("Compression","Em dash: emphasis, three uses", [r"em ?dash", r"parenthes"]),
 ("Compression","Understate the serious, overstate the light", [r"understat", r"overstat", r"window ?pane"]),
 ("Feedback","Early readers / community of practice", [r"early readers?", r"beta readers?", r"community of practice", r"accountability partner"]),
 ("Feedback","Letter of response / two readings / silent author", [r"letter of response", r"silent author", r"junot", r"body.?scan", r"two readings"]),
 ("Feedback","Reader feedback describes symptoms (friction)", [r"friction", r"\bunclear\b.{0,40}\bdense\b", r"symptom"]),
 ("AI","AI cannot think / style is not a coat of paint", [r"coat of paint", r"language.?producing machine", r"polishing a turd", r"funhouse", r"slop"]),
 ("AI","Five skills AI will never replace", [r"moat", r"whimsy", r"embodied", r"transitional object", r"\bstakes\b"]),
 ("AI","AI as read-only navigation layer", [r"navigation layer", r"read.?only", r"wiki agent", r"hub notes?"]),
 ("Rhetoric","31 tools (alliteration, antithesis, polyptoton, diacope, epistrophe, prolepsis, congeries, synesthesia)", [r"alliteration", r"antithesis", r"polyptoton", r"diacope", r"epistrophe", r"prolepsis", r"congeries", r"synesthesia", r"enallage"]),
 ("Rhetoric","Ironic juxtaposition / kill your darlings", [r"juxtaposition", r"kill your darlings", r"darlings"]),
 ("Academic","Scholar vs researcher; organizing mind", [r"organizing mind", r"scholar", r"be a scholar"]),
 ("Academic","Literature review: plot vs story, casting studies", [r"plot.{0,20}story", r"story.{0,20}plot", r"main characters?.{0,40}(studies|research)", r"allies", r"adversaries", r"mind map"]),
 ("Academic","Citations: simple syntax, personal language, present tense", [r"present tense", r"function words", r"30,?000", r"citations"]),
 ("Academic","Author function vs flesh-and-blood author / persona", [r"author function", r"flesh.and.blood author", r"\bpersona\b"]),
]

def load():
    vids=[]
    for f in sorted(glob.glob('readable/*.md')):
        s=open(f,encoding='utf-8').read()
        title=s.split('\n')[0][2:]; vid=re.search(r'youtu\.be/(\S+)',s).group(1); date=re.search(r'- Date: (\S+)',s).group(1)
        paras=[(int(m.group(1)),m.group(2)) for m in re.finditer(r'\*\*\[[^\]]+\]\(https://youtu\.be/[^?]+\?t=(\d+)\)\*\* (.*)',s)]
        vids.append((vid,date,title,paras))
    return vids

if __name__=='__main__':
    vids=load(); out=[]
    for g,name,pats in CONCEPTS:
        rx=[re.compile(p,re.I) for p in pats]; hits=[]
        for vid,date,title,paras in vids:
            for i,(t,x) in enumerate(paras):
                n=sum(len(r.findall(x)) for r in rx)
                if n:
                    if hits and hits[-1]['vid']==vid and hits[-1]['i_end']>=i-1:
                        hits[-1]['i_end']=i; hits[-1]['n']+=n; hits[-1]['text']+=' '+x
                    else: hits.append({'vid':vid,'date':date,'title':title,'t':t,'i':i,'i_end':i,'n':n,'text':x})
        out.append({'group':g,'name':name,'hits':hits})
    json.dump(out,open('concept_candidates.json','w'),ensure_ascii=False,indent=0)
    for c in out: print(f"{len(c['hits']):4d}  {c['name']}")
    print(sum(len(c['hits']) for c in out),'candidate paragraphs')
