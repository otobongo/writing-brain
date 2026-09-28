---
name: redraft
description: Review and rewrite a piece of writing so it works for its reader, using William Fitzpatrick's Writer Science method (reader first, value before clarity, top-down revision, reader locations). Point it at any copy — a local file, a URL, a Google Doc, or pasted text — and it establishes who the reader is, reports every gap from the big picture down to the sentence with evidence, and saves a copy containing the issues, a full rewrite and the untouched original. It also creates podcast and speaking scripts from the writer's own notes or voice memos. Use this whenever someone wants to review, critique, improve, tighten, edit, "fix", redraft or rewrite an article, essay, newsletter, blog post, portfolio piece, case study, landing page, sales or marketing copy, product page, LinkedIn or social post, email, talk, speech, podcast script or video script — or asks why a piece doesn't land, isn't clear, reads flat or doesn't convert — even if they never mention a method or the word "review". Not for fiction, poetry, or pure proofreading of spelling and commas.
---

# Redraft

Redraft takes a piece of copy the writer points at, works out who it is for, finds where it fails that reader, and rewrites it. The original is never touched: the output is a new file with the issues, the rewrite, and a copy of the original, so the writer can compare and choose.

The judgments come from William Fitzpatrick's *Writer Science* method, distilled from 50 of his videos. Credit it that way when you describe what you're doing ("based on the Writer Science method"). Don't speak as him.

## The method in six sentences

Know these before you start; everything else in this skill follows from them.

1. **Writing is only good or bad for a particular reader.** There are no universal rules, only tools, so every judgment you make is about the effect on *this* reader, never "the rule says".
2. **Value comes before clarity.** Readers read to solve a problem they already have. Clear, organised and useless is still useless, so the reader's problem and the point come first, sentences last.
3. **Thinking on the page produces text in the wrong order for readers** (background first, discoveries in the order they happened, the answer at the end). He calls this *interference*. It can't be fixed by line editing; the structure has to be rebuilt in reader order.
4. **Readers read in a line and look in fixed places:** the title, the end of the introduction, the opening of every section and paragraph, the start (topic position) and end (stress position) of every sentence, the key terms, and the conclusion. Most clarity is placement.
5. **One shape repeats at every scale:** a short opening that states the point and names the key terms (the *index*), then a longer discussion that delivers it. The point sits at "the end of the beginning".
6. **The writer can't read their own draft cold, and neither can you by feel.** So check the locations deliberately instead of trusting how the text feels.

The full account, with sources, is in `references/method.md`. Read it the first time you use this skill in a session.

## Workflow for a review and rewrite

Work through these steps in order. The order matters: it is the method's top-down order, and doing sentence work before the point and structure are right wastes the writer's time.

### 1. Get the text, and keep the original safe

The writer will point you at something. Read it without changing it:
- **Local file:** read it directly. For `.docx`, extract the text (e.g. `textutil -convert txt` on macOS, or python-docx); for PDF, extract text; keep headings.
- **URL:** fetch the page and extract the main copy (headings, body, calls to action, captions). Note anything visual you can't see.
- **Google Doc or Drive file:** use the connected Drive tools if available; otherwise ask the writer to paste or export it.
- **Pasted text:** use it as given.

Save a verbatim copy of what you reviewed; it goes at the bottom of the output file. Never write to the source.

### 2. Identify the genre and what kind of draft this is

- **Genre** decides which genre file to load from `references/genres/` (see the map at the end) and what "good" looks like. A tweet doesn't get the treatment a 3,000-word essay does: scale the review to the stakes and length.
- **Draft type.** Is this a *reader draft* (it knows its point and is trying to deliver it) or a *thinking draft* (the writer was working out what they think — the point is buried at the end, missing, or there are several competing ones)? A thinking draft needs the bridge in `references/thinking-drafts.md` before anything else: find the point in the writer's own words, then rebuild. Don't polish sentences in a draft whose point you can't find.

### 3. Establish the reader

Every judgment depends on the reader, so settle this before reviewing. Ask **once**, briefly (skip what the text or conversation already answers):

- Who exactly is this for? (A specific person or group, not "everyone".)
- What do they believe or know about this now, and where does their knowledge stop?
- What problem are they trying to solve, or what decision are they making?
- What should they think or do differently after reading?
- What words does their community use for this? (Their code words.)

If the writer has saved briefs (look for a `reader-briefs.md` or a `briefs/` folder next to the source or in the working directory), offer to reuse one. If they don't answer or say "just do it", infer a **provisional reader** from the text and genre, state it at the top of the report, and mark reader-dependent findings as provisional. After a real brief is agreed, offer to save it for reuse. Details: `references/reader-brief.md`.

### 4. Build the views

Run the view script on the text. It prints the patterns the method checks — the skim view (paragraph openings only), the topic list (the first words of each sentence), the introduction beside the conclusion, and flags for fillers, doublets, wordy phrases, stacked negatives, hedges and absolutes, empty verbs, metadiscourse, turn words and more:

```bash
python3 scripts/views.py path/to/text.md            # readable report
python3 scripts/views.py path/to/text.md --json     # machine-readable
```

(Paths are relative to this skill's directory. Save pasted or fetched text to a temporary `.md` file first.)

Treat every flag as **a place to look, not a verdict**. The script can't know the reader; you can. Drop false alarms before they reach the writer (each reference file lists the usual ones).

### 5. Review from the top down

Go level by level, loading the reference file for each. Finding a serious problem at a higher level changes what matters below it, so don't skip ahead.

| Level | What you're checking | Reference |
|---|---|---|
| 1. Reader and value | Is there a problem this reader already has, visible early? What do they get? | `references/review-bones.md` |
| 2. The point and the argument | One arguable point, stated where readers look; reason and evidence this reader accepts; objections met | `references/review-bones.md` |
| 3. Title, opening, ending | Title that works on a cold reader; introduction built as a problem; conclusion that pushes off higher | `references/review-bones.md` |
| 4. Structure | Sections in the order the reader's questions arise; each unit opens with an index; stable key terms; the skim test | `references/review-bones.md` |
| 5. Paragraphs | One job each; a small, consistent cast at sentence openings; handoffs between sentences | `references/review-flow.md` |
| 6. Sentences | Characters as subjects, actions as verbs; short subject, early verb; old before new; strong words in the stress position | `references/review-flow.md` |
| 7. Finish | Compression (for load, not length); calibrated certainty; emphasis used sparingly; mechanics last | `references/review-finish.md` |

Before flagging anything, check `references/anti-checks.md`. There are "rules" this method deliberately rejects — varying sentence length, banning the passive, avoiding repetition, readability grades, hunting "AI tells", school rules — and flagging them would contradict everything else in the report. The same file has the procedure for when two pieces of advice seem to conflict (usually the answer depends on genre, reader, or scale).

Write each issue in this form, because it tells the writer what is wrong and why it matters, which is how the method teaches:

- **Where:** the location (e.g. "Introduction, sentence 3" or "Section 2 opening").
- **What's there:** a few of the writer's own words, quoted.
- **Effect on this reader:** what it does to them, as a reasoned judgment, not a rule.
- **Fix:** what the rewrite does about it (or the question the writer must answer).

Rank issues top-down and mark the **top three** as priorities: if the writer fixes nothing else, these matter most. Then list every other real issue, grouped by level. Leave out cosmetic nitpicks; a report of fifty minor flags hides the three that matter.

### 6. Rewrite

Now rewrite the whole piece to fix the issues, following `references/rewrite.md`. The essentials:

- **Use only what the writer gave you.** Rearrange, sharpen, compress, rebuild the structure, restore the point to where readers look. Never invent facts, numbers, results, quotes, testimonials, client names, stories or credentials. The value of the piece is the writer's own knowledge; invented substance destroys it and can embarrass them.
- **Where the rewrite needs something only the writer has** — the missing evidence, the real number, which of two points they mean, the reader's actual objection — leave a visible placeholder like `[[Q2: what did the pilot actually save — hours or cost?]]` and list the question in the report.
- **Keep their voice.** Their words, their examples, their register (unless the register is itself an issue for this reader). Change what the issues require, not everything you would have written differently.
- **Keep the genre's form** (a LinkedIn post stays a post; a landing page keeps its sections and call to action).

### 7. Save the output

Write one Markdown file using `assets/report-template.md`:
- **Local source:** save next to the original as `<original-name>.redraft.md` (e.g. `launch-post.md` → `launch-post.redraft.md`). If that exists, add a number.
- **URL, Google Doc or pasted text:** save to `redrafts/<short-slug>.redraft.md` in the current working directory.

The file holds: the reader and genre, a short summary, the issues (top three first), questions for the writer, the full rewrite, a table of what changed and why, and the original, unchanged. Offer a `.docx` or Google Doc version if the writer works in those.

### 8. Reply in chat

Keep it short, because the file has the detail: the provisional or agreed reader, the three priority issues in a line each, any questions blocking the rewrite, and a link to the file. Invite them to answer the questions so you can fill the placeholders.

## Creating a script (podcast, talk, video) from raw material

When the writer wants a new podcast episode, talk or speaking script, build it from **their** material: notes, bullet points, a voice-memo transcript, an old article, an outline. Follow `references/genres/scripts.md`:

1. Establish the listener (step 3 above) and the occasion (length, format, solo or interview).
2. Find the question the episode answers and the point, in their material. If the material has no point yet, help them find it before drafting (`references/thinking-drafts.md`).
3. Build the structure around the listener's questions, then write the script in spoken form — listeners can't re-read, so the rules shift (more previewing and repetition of key terms, shorter subjects, concrete scenes).
4. Mark every gap as a `[[Q: ...]]` placeholder rather than inventing a story, statistic or example.
5. Save as `<slug>.script.md` with the brief, the script, and the open questions, and review it at levels 1–4 before handing it over.

If the writer asks you to draft other kinds of copy from their material, use the same approach with the relevant genre file.

## Where to find things

| File | Read it when |
|---|---|
| `references/method.md` | First use in a session; any time you need the reasoning behind a judgment |
| `references/reader-brief.md` | Establishing the reader; reusing or saving briefs |
| `references/thinking-drafts.md` | The point is missing, buried, or split; creating from raw material |
| `references/review-bones.md` | Levels 1–4 |
| `references/review-flow.md` | Levels 5–6 |
| `references/review-finish.md` | Level 7 |
| `references/anti-checks.md` | Before flagging anything; when two principles conflict |
| `references/rewrite.md` | Step 6 |
| `references/genres/articles.md` | Articles, essays, newsletters, blog posts, op-eds |
| `references/genres/case-studies.md` | Portfolio pieces, case studies, project write-ups, bios and about pages |
| `references/genres/landing-pages.md` | Landing pages, product and service pages, sales copy, ads |
| `references/genres/social-and-email.md` | LinkedIn and other social posts, threads, emails, newsletters' subject lines |
| `references/genres/scripts.md` | Podcast, talk, speech and video scripts (reviewing or creating) |
| `assets/report-template.md` | Writing the output file |
| `scripts/views.py` | Step 4 |

Some genres (landing pages, social posts, scripts) are only partly covered by Fitzpatrick's teaching. Their genre files mark which advice is his and which is general craft knowledge added to fill the gap; keep that distinction in the report ("general copywriting practice, not from the method").

## Things that keep the report honest

- **Say why, in reader terms.** "Your reader, a hiring manager, reaches the outcome in paragraph 6" beats "move the outcome up".
- **His empirical claims are his reasoning, not settled science.** Several of his figures rest on studies he doesn't name. Explain the reader effect; don't cite the numbers as fact.
- **Never call anything an "AI tell"** or suggest changes to make text look less machine-written. That isn't a reader problem, and the method explicitly rejects it.
- **Respect deliberate choices.** A rule broken on purpose for an effect is a tool, not a fault. If a choice looks deliberate, ask rather than flag.
- **Out of scope:** fiction craft (plot, character), poetry, and pure proofreading. Say so if asked, and help with general knowledge labelled as such.
