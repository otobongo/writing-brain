# Skill mapping: turning the Writer Science method into Claude skill behaviour

Built from the ten deep-read reports (read_01 to read_10, all 50 videos). I checked the AI passages directly against the transcripts: V1, V14, V15, V19, V20, V23, V27, V33, V34, V35, V36, V40, V44, V45, V49 and V50. Everything is paraphrased. Quotes are under 15 words. All examples are mine, written in the spirit of his. Citations use the form V45 13:48.

What this file does:
- §1 sets out the design rules the whole method imposes on a skill.
- §2 defines the stages used throughout.
- §3 maps every technique in the reports to skill behaviour: what it is used for, when, with what inputs, and where he says not to use it.
- §4 is the catalogue of mechanical checks, with what each misses and what it wrongly flags. It also lists the checks the skill must *not* run.
- §5 sets out what his position on AI implies for what the skill may and may not do.
- §6 proposes the skill's modes.
- §7 turns his unresolved tensions into operating rules.
- §8 lists gaps and cautions for whoever builds the skill.

**Headlines**
- **Judgment and interview carry most of the method; scripts carry little.** §3 maps 291 techniques:
  - 178 need a judgment question from the model;
  - 115 need a step from the writer (an interview answer or an exercise);
  - 82 have any mechanical component;
  - 35 are coaching or design only.

  The mechanical layer clusters at the sentence and finishing stages. The parts that create value (reader, problem, point, evidence, judgment) can only be asked about, not computed.
- **Scripts do more good producing views than verdicts.** The skim of indexes, the topic list, the punctuation X-ray, and the introduction and conclusion side by side let the *writer* see the pattern. That is how he diagnoses too.
- **Four gates come before any feedback.** Which draft is this (thinking or reader)? Who is the reader? Work top-down. Show at most three issues at a time.
- **On AI, the skill is a coach and diagnostic editor, never a ghostwriter.** It asks, locates, explains, demonstrates on parallel examples and navigates the writer's own notes. It does not draft, polish, restyle, supply ideas, or scrub "AI tells" (§5). The model is useful as a *cold reader* for finding gaps, but it is not the reader.
- **Eleven modes, plus genre overlays.** Brief, Think, Unstick, Bridge, Architect, Flow, Finish, Readers, Gym, Plan and Notes (§6).
- **Thirteen anti-checks** that popular tools run and his method rejects (§4.3).

---

## 0. Codes used in the tables

**About the quotation marks.** A question in quotation marks after "J:" or "W:" is my proposed wording for the skill to use. It is not his. His own words appear only as short phrases with a timestamp.

**Use type** (what the skill does with a technique; many techniques have more than one)

| Code | Meaning |
|---|---|
| **M** | Mechanical check. A script can run it on a draft. The ID (M1 to M51) points to the catalogue in §4, which gives the heuristic, what it misses and what it wrongly flags. A mechanical hit is only ever a *location to look at*, never a verdict. |
| **J** | Judgment question. The model asks it of the draft, using the reader brief. |
| **W** | Writer step. An interview question or an exercise. The writer answers or writes; the skill does not. |
| **C** | Coaching or explanation only. Nothing is checked. The skill explains the idea when it is relevant, or uses it to frame other feedback. |
| **design** | Not a check. A rule that shapes how the skill behaves everywhere. |

**Stage** (see §2)

S0 intake · S1 think · S2 bridge · S3 bones · S4 flow · S5 finish · S6 readers · B block and process (any time) · P practice (away from a draft) · Plan (book or project planning) · Notes (the writer's capture system)

**Inputs** (what the skill needs before the technique means anything)

| Code | Input |
|---|---|
| R | Reader brief: who they are, what they believe now, where their knowledge stops, their problem or decision, and their type (uninformed, indifferent or resistant) |
| G | The writer's goal: what the text must do in the world |
| Gen | Genre, venue and its conventions |
| Q | The driving question |
| P | The point sentence, written by the writer |
| KT | Key terms list |
| CW | The reader community's code and value words |
| D | Which draft this is: thinking draft or reader draft |
| N | Neighbouring sentences (the one before and the one after) |
| E | Evidence and sources |
| WN | The writer's own notes and earlier drafts |

"Don't apply" gives his stated limit where he gives one. Where he gives none and the report inferred one, it is marked *(inferred)*.

---

## 1. Ten design rules the method imposes on the skill

1. **Establish the reader before judging reader-facing text.** He won't look at a client's text until the reader questions are answered (V24 3:22). Coherence is not in the text; it arises between writer, reader and text (V49 8:21 to 10:14). Meaning is what readers do with a text (V33 8:53). So no check that depends on the reader runs without a brief. The one exception is the thinking draft, where readers are kept out deliberately (V38 18:28, V42 17:29).

2. **Ask which draft this is before doing anything.** A thinking draft can't be line-edited into a reader draft (V31 8:47, V35 12:09, V47 17:30). Pulling readers into phase one causes block and corrupts the thinking (V38 18:28). The skill's first routing question is: are you still working out what you think, or shaping it for readers?

3. **Go top-down.** The order is reader, point, problem, key terms, subjects, connections, then mechanics (V24 22:56). The "bones" come before sentence flow (V50 35:11). If the introduction is the only thing you fix, fix that (V46 19:48). The skill does not polish sentences in a draft whose point it can't find.

4. **Diagnose; don't enforce rules.** Every flag names the effect on *this* reader and leaves the choice with the writer. There are no universal rules because there are no universal readers (V12 7:30). He calls writing "not paint-by-numbers" (V27 4:54). Rules and AI tools that apply them lead writers to assume all readers are the same (V33 13:04).

5. **Check the locations readers use, not feel.** Writers can't reread their own drafts by feel (V49 3:40, V50 3:43 to 4:24). The skill should not substitute its own feel either. It checks the places readers look: title, end of the introduction, the index of each unit, topic and stress positions, key terms, and the conclusion.

6. **Treat reader complaints as symptoms.** "Unclear", "dense" and "disorganized" describe friction, not its cause (V32 3:24 to 3:50, V47 6:18 to 7:16). The skill never acts on them literally. For example, "dense" does not automatically mean "shorten".

7. **Work on one tool at a time.** He warns against applying many tools at once (V12 51:02, V19 1:14:43) and suggests adding one practice a week (V23 40:48). Each pass surfaces a few ranked issues, not an audit of fifty.

8. **The writer keeps the pen.** The skill asks, locates, explains, and demonstrates on parallel examples. The writer writes. See §5.

9. **Teach his way.** Give one vivid image per idea. Commit the fault, then fix it. Ask "which version is easier?" before explaining. Give fixes as short numbered steps. (These are observations of his teaching across V6 to V10 in read_02.)

10. **Keep the anti-checks off.** The skill does not suggest varying sentence length, banning the passive, avoiding repetition, grading readability, hunting em dashes, or enforcing school rules. The full list is in §4.3.

---

## 2. The stages

| Stage | What exists | Reader in the room? | What the skill may do |
|---|---|---|---|
| **S0 Intake** | A goal, maybe notes | Being defined | Interview for goal, reader and genre. Assign the code-word hunt. |
| **S1 Think** | Freewrites; a thinking draft | No (V38 18:28; V42 17:29) | Keep the question in front of the writer, run timers, offer prompts, retrieve the writer's own notes on request. No quality judgments, no compression, no structure advice. |
| S1a Vent | Goal-less daily freewrite ("magma") | No, not even the writer (V41 22:53, 25:56) | Nothing beyond the timer. The skill does not read it unless asked, and then only after it has cooled (V41 27:01). |
| S1b Tethered draft | Question-driven exploration (V42 17:29) | No | As S1. |
| **S2 Bridge** | A finished thinking draft and the "click" (V47 12:03) | Arrives here | Reverse outline (labels written by the writer), comparing the point sentences in the introduction and conclusion, stating the point, listing the reader's questions. |
| **S3 Bones** | A reader draft in a new document | Yes | Value, point, introduction, structure, argument, conclusion, title. |
| **S4 Flow** | Bones that hold | Yes | Paragraph topic strings and sentence construction. |
| **S5 Finish** | Near-final text | Yes | Compression, calibration, emphasis economy, mechanics last (V24 21:04 to 22:56). |
| **S6 Readers** | Something to show | Real ones | Set up and run early-reader protocols. Translate feedback into diagnoses. |
| **B** Block and process | Any | Any | Coaching, diagnostic questions, one practice. |
| **P** Practice | No draft | None | Drills. |
| **Plan** | A book or project idea | Being defined | Positioning and the purpose chain. |
| **Notes** | The writer's vault | None | Read-only navigation (V40). |

Three modes of writing must be kept apart: the goal-less vent (V41), the question-tethered artist draft (V42), and the architect's reader-facing work (V42) (read_09, "Across" point 3). Judgment words, backspacing and self-commentary during S1 are signs that the architect has leaked in (V41 24:03, V42 17:29).

---

## 3. Technique map

Where a technique appears in several videos, it gets one row that cites all of them. Row IDs (A1, B3 and so on) are referred to in §6.

### 3A. Foundations: the lenses every other check runs through

| ID | Technique (sources) | Use | Stage | Inputs | How the skill uses it | Don't apply |
|---|---|---|---|---|---|---|
| A1 | Judge by effect on the reader, not by rulebook (V2 0:21 to 1:11; V8 11:53; V10 4:40 to 6:04; V22 3:19; V33 8:53) | design, C | all | R | Every flag is worded as reader effect plus a choice. When a writer cites a rule, the skill asks what the rule protects the reader from, which is his method in V2. | It doesn't license errors. Mechanics still get checked, last (V24 21:36). |
| A2 | Tools, not rules; no universal readers (V9 6:01; V12 0:41, 7:30; V14 7:04; V31 14:02; V42 8:28) | design, C | all | R | The skill never states a style rule. It names a tool and its conditions. It explains this when a writer arrives with rule-based feedback from a teacher, an editor or Grammarly. | He still insists you learn the rules first (V36 12:09). |
| A3 | Learn the rules, then break them on purpose (V2 19:54; V12 2:45 to 3:46; V36 9:58 to 13:48) | J, C | S4 to S5 | R, Gen | J: "Is this break deliberate, and what effect does it buy?" Deliberate breaks are shielded from mechanical flags. He warns that an AI assistant would smooth them away (V36 11:15). | A break made out of ignorance reads as an error; breaks must be rare enough to register (V36 12:09). |
| A4 | Test a rule against its advocates' own practice (V14 10:59 to 12:35) | C | B | none | A coaching reply when a writer defends a rule by authority. | Some style tips are harmless (V14 0:57). |
| A5 | Reader feedback reports feelings, not causes (V19 26:31; V24 15:50; V32 3:24 to 3:50; V35 12:09; V47 4:44 to 8:19) | W, J | S6, S3 to S4 | Feedback text and where it points | W: collect the feedback words and their locations. J: map each to candidate causes (point buried, topics scattered, writer's order, unpacked shorthand) and test them. | Readers are still good at sensing *where* the friction is (V47 4:44). |
| A6 | The coffee stain, or briefed-reader, problem: you can't reread your own draft (V24 0:52 to 1:40; V49 1:49 to 3:40; V50 2:00 to 4:24) | C, design | S2 to S5 | none | Explains why the skill uses location checks and why "it reads fine to me" isn't evidence. It also limits the skill (see §5.6). | Don't prescribe "rest it and reread as a stranger" as the fix. He calls it impossible (V50 2:00). |
| A7 | Coherence is relational, not in the text (V49 7:34 to 10:14) | design | S3 to S4 | R | Justifies the reader-brief gate. The skill won't certify a passage "clear" in the abstract. | none |
| A8 | Clear but useless is useless: value before clarity (V12 35:29; V19 8:34 to 10:39; V27 25:12 to 27:52; V30 15:41; V42 21:23) | J (gate) | S3 before S4 | R, P | Before any sentence work, J asks: "What will this reader be able to do or understand afterwards?" If there's no answer, the skill routes to value and point work, not polishing. | Not in phase one, where value is still being made. |
| A9 | Writing is social; words signal membership (V12 3:46 to 7:54, 14:37 to 18:09; V24 1:40 to 3:01; V31 10:11 to 14:02; V42 9:28 to 14:20) | C, J | S0, S4 | R, CW | Frames the register and code-word checks (B14, L8). | none |
| A10 | Writing is thinking (V3 11:39; V11 6:14; V17 2:43 to 4:07; V20 4:04; V35 0:50; V38 10:24). Later qualified: writing is where thinking becomes visible (V40 5:53 to 12:17; V42 16:02) | C, design | S1 | none | Coaches writers who wait until they "know what to say". It is also why the skill does not generate ideas: the thinking is where the writer's value lies (V35 8:11). | Incubation, sleep and dreams also count (V41 16:41). |
| A11 | Clear writing comes from clear thinking (V7 28:11) | J | S3 to S4 | none | J: if repeated line edits haven't cleared a passage, the idea is unclear, not the sentence. Route that passage back to S1 or S2. | Only when edits have stalled *(inferred)*. |
| A12 | GPS directions, not a garden hose; directions to the restaurant (V19 6:26 to 8:34; V24 4:18 to 7:28; V35 9:41 to 13:27; V47 10:18 to 11:07) | W, C | S2 to S3 | R | W: "Where is your reader standing now? Where must they end up?" This is the organising image for every reader draft. | The thinking draft (V19 8:34). |
| A13 | Writing as a two-player game (V20 0:00 to 0:47, 22:49 to 23:28) | W, J | S3 | R | W: after each paragraph the writer puts the reader's likely reply in brackets. J: does the next paragraph answer it? | The thinking phase (V20 8:25). |
| A14 | Genre as a sequence of functions (the Starbucks test); the template trap; function, not form (V20 16:36 to 21:38; V31 2:16 to 3:35, 22:48) | W, J | S3 | Gen, G, R | W: list the functions this genre needs to reach the goal writer and reader share. J: tag each paragraph with its function, and flag "favourite colour" paragraphs that serve none. | His own sequences are functions, not templates (V19 51:23). Don't turn them into forms (V31 9:42). |
| A15 | The reading model: linear, three or four items held, the "mental briefcase" (V26 1:32 to 4:55) | C, J | S4 | N | J: by the time the reader reaches the verb, how many open items are they holding? Pairs with M8. | A lens, not a style to impose (V26 2:51). |
| A16 | The sentence as a camera shot: order controls what is seen first and last (V26 1:50 to 3:37) | J | S4 | N | J: "Is this sentence meant to orient (context first) or to reveal (the striking particular first)? Is the order the one you chose?" | Neither order is better (V26 2:51). A reveal costs working memory in dense exposition *(inferred)*. |
| A17 | Good writing is care for the reader (V6 5:27) | C | all | none | Sets the tone of coaching. | none |

### 3B. Reader, purpose and value (intake)

| ID | Technique (sources) | Use | Stage | Inputs | How the skill uses it | Don't apply |
|---|---|---|---|---|---|---|
| B1 | The four reader questions: what motivated them to pick this up, what problem they face, what answer they want, what decision they're making (V24 3:01 to 3:22) | W | S0, S2 | none | Interview. The answers are stored in the writer's own words as the core of the brief. | none |
| B2 | The purpose chain: your goal, then who must read for it to come true, then their pain (V18 10:47 to 13:56; V19 10:39 to 14:33) | W | S0, Plan | G | Interview. For books it extends to the table of contents as a bridge and a filter (O-books). | He suggests fiction may run on personal taste (V18 14:32). |
| B3 | The architect's four questions: what they believe now, where their knowledge stops, what problems they're solving, what must change in their thinking (V42 23:44; V25 7:59 to 8:27) | W | S2 | none | Interview. Stored as brief fields: *believes now*, *knows up to*, *trying to solve*, *must think afterwards*. | Not during the artist phase (V42 20:28 to 20:50). |
| B4 | Reader types: uninformed, indifferent, resistant (V24 10:50 to 12:20); and levels of awareness (V27 27:00) | W, J | S0, S3 | R | W: the writer classifies the reader. J: does the introduction do the matching job? That means background for the uninformed, consequences for the indifferent, and dismantling the blocking belief for the resistant. The "however" must hit that belief (V24 8:15 to 10:27). | none |
| B5 | The rhetorical planning wheel: purpose and actions, writer's role, audience, context (V30 4:46 to 11:13) | W | S0 | G, Gen | Interview for high-stakes genres such as grants, personal statements and memos. | Low-stakes texts close to "the classic scene" need little mapping *(inferred)*. |
| B6 | "What must they also believe?" (V30 7:08) | W, J | S0, S3 | P, R | W: break the target belief into qualities. J: is there real evidence in the draft for each quality? | none |
| B7 | Problem statement at the top of the page: topic, question, what it helps the reader gain or avoid (V12 35:03 to 37:20) | W | S0, end of S1 | Q, R | The writer fills it in. The skill uses it later as the filter for "does this belong?" questions. | A planning tool; not for publication (V12 37:20). |
| B8 | Value is a solution the reader can perceive; readers don't owe you attention (V18 7:47 to 9:52; V19 8:34 to 10:39; V31 3:35; V46 8:20) | J | S3 | R | J: "Could a busy stranger see what's in this page for them?" | Pure entertainment sits outside this exchange (V31 3:35). |
| B9 | Practical versus conceptual problems (V18 4:21 to 5:10; V19 7:44; V22 10:19 to 11:17; V28 14:11 to 14:52) | W, J | S2 to S3 | P | W: classify the problem. J: does the promise name an action (practical), or an old idea replaced by a new one (conceptual)? | none |
| B10 | Knowledge versus value; the benefit-or-cost question (V20 9:33 to 16:36) | W | S2 to S3 | R | W: under each idea the writer writes "Benefit:" or "Cost avoided:" for this reader. | He declines to give positioning templates (V20 15:41). |
| B11 | The reader's definition of an essay; arguments of fact versus judgment; "valuable to whom?"; understanding before persuasion (V25 0:45 to 3:18) | W, J | S0 | R, Gen | W: a question of fact means a report; a question of judgment means an essay for a named community. J: are calls to action crowding out understanding? | Shifting what readers care about is rare and risky, but not ruled out (V25 4:50, 7:01). |
| B12 | Original isn't valuable; replace the gap model with the model-error frame (V25 3:18 to 7:01; V31 14:34 to 18:37) | M25, J | S3 | R | M25 flags "no one has studied", "understudied", "gap in the literature", "first to". J: name the model readers use now and where it fails. | A tiny enthusiast audience may read anything (V31 15:00). Some academic genres expect a gap statement *(inferred)*. |
| B13 | Assume the reader doesn't care; build a bridge from what they do care about (V39 16:37 to 19:04) | W, J, M37 | S3 | R | W: list what you want them to care about, and what they already care about. J: does the opening start from the second list? M37 flags value words used as if self-evidently good. | none |
| B14 | Community code words; the anthropologist exercise (V12 3:46 to 5:57; V19 16:59 to 18:46; V22 30:25 to 32:22; V31 14:02; V35 13:27 to 18:54) | W, M34, J | S0 collect, S4 apply | CW | W: the writer collects 4 or 5 texts the readers share and mines them. The skill may count word frequencies in texts the writer supplies; that is navigation, not generation. J: are the key claims phrased in the reader's value words? | Don't import words you don't understand *(inferred, V22)*. No showy vocabulary for its own sake (V12 5:57). |
| B15 | Unpack expert compression (in place of "curse of knowledge") (V47 12:59 to 16:21) | J, M29 | S4 | R, Gen | M29 lists undefined acronyms, named methods and coined terms at first use. J: which of these does *this* reader lack? See §5.6: the model is itself "briefed" on many subjects. | Writing only for peers (V47 14:32). The lesson is not "write at a fifth-grade level" (V47 13:39). |
| B16 | Several audiences are like several chess games at once (V25 2:24) | W | S0 | R | W: choose the primary reader, or plan for each. | none |
| B17 | Curiosity conversations: learn readers' language (V17 34:36 to 35:19; V19 1:11:07) | W | S0, S6 | none | Recommend them. The skill can help plan questions and tally themes from notes the writer supplies. | none |
| B18 | What the text should do in the world; articulate equals authoritative (V38 13:22 to 14:48) | W | S0 | G | W: "What should this text make happen, and for whom?" | none |

### 3C. Thinking on the page (phase one)

| ID | Technique (sources) | Use | Stage | Inputs | How the skill uses it | Don't apply |
|---|---|---|---|---|---|---|
| C1 | Door closed, door open: producing and perfecting are separate sessions (V11 2:03 to 5:13) | W, C | S1 | D | W: "Is this session for producing or for perfecting?" In a producing session the skill says nothing about quality. | Editing still matters, just at another time (V11 0:00, 5:13). V23 36:18 rejects separating revision from writing; see §7. |
| C2 | Timed non-editing; bracketed placeholders; the timed "solo" (V11 3:01 to 4:27; V12 44:07 to 45:38; V20 6:12) | W | S1 | none | Exercise: set a timer, no backspace, "[better word]" placeholders. The skill can run the timer. | The output is not shareable (V11 12:01). |
| C3 | The question tether: write the question at the top of the page (V20 6:12 to 7:40; V35 6:40; V42 17:29; V43 5:43, where the title does the same job) | W | S1b | Q | The skill keeps the question visible and, only if asked, brings the writer back to it. | The goal-less vent has no question (V41 22:53). |
| C4 | The goal-less daily vent, "magma" (V41 22:17 to 31:10) | W | S1a | none | The exercise itself. Later, once it has cooled, the writer rereads for lines with "shine". The skill may ask which lines have energy, but it doesn't choose them. | Not a first draft. "Good" and "bad" don't apply (V41 22:53, 24:03). |
| C5 | Working with words, then with ideas: "fermentation" (V11 11:16 to 15:32) | W | S1 | none | The skill prompts the alternation: freewrite, then the writer writes a one-sentence summary of each idea, picks one, and freewrites on it. | The material still needs shaping for readers (V11 15:32). |
| C6 | Let X become Y: follow doubt to a new claim (V11 5:30 to 8:33) | C | S1 | none | Coaching. | The reader version presents Y, not the journey *(inferred; cf. V19 4:55)*. |
| C7 | Private prompts: write to yourself as "you"; "this feels wrong because…"; "what I'm trying to say is…" (V11 8:33 to 9:14) | W | S1 | none | Offered when the writer is stuck. | Private devices, removed from the reader draft *(inferred)*. |
| C8 | Imagine an audience and a 30-minute limit; talk it out or dictate (V11 9:14 to 10:41; V20 7:40) | W | S1 | none | Exercise. A transcript is raw material, never the draft (see §5.4). | none |
| C9 | A question, not a topic; "writing in reverse" (V38 2:14 to 3:23; V39 0:32 to 3:20) | W, J | S1, S3 | Q | W: turn a topic or thesis back into a question. J (at S3): was this evidence found by the question, or recruited to prop up a belief? | none |
| C10 | The "I don't know" ritual: say it, then ask what evidence you would need (V19 3:19 to 4:05; V38 3:23 to 5:42) | W | S1 | Q | A prompt. | none |
| C11 | The question as a filter for evidence (V38 5:06 to 5:42) | J | S1 to S3 | Q, E | J: "Does this help answer the question?" | none |
| C12 | The inquiry method: neutral evidence plus reasoning makes the claim (V38 6:40 to 10:43) | W, J | S1 to S2 | Q, E | W: two columns, evidence described neutrally and reasoning. J: which one would a critic reject? | For value questions. Empirical questions use empirical methods *(inferred)*. |
| C13 | Ask "why?" five times to reach a systemic question (V17 5:34 to 6:04) | W | S1, Plan | none | Exercise. | none |
| C14 | Story first, lesson second (V17 6:42 to 7:38) | W, J | S1, S3 | E | W: keep a teachable-moment log. J: does each anecdote support *this* claim, or one next to it? | none |
| C15 | Reading is food, not fuel (V35 0:50 to 3:38) | C, J | S1 | Q | Name the gap, read to fill it, return to writing. J: "Is this reading filling a specific gap?" | none |
| C16 | Drafts as excavation sites and labs; bring ideas into contact (V20 5:06 to 5:22; V35 6:40 to 8:11) | W | S1 | WN | Exercise. The skill may retrieve two of the writer's own notes to set side by side; that is navigation. | none |
| C17 | Whimsy: writing as a play space (V36 19:29 to 25:12) | C, W | S1 | none | Framed as "let's see where this goes". Any surprise prompts are questions, never text (§5.5). | He admits he rarely manages it (V36 22:59). |
| C18 | Fear as a metal detector: "What am I most afraid of here?" (V23 30:00 to 32:41) | W | S1, B | none | A prompt. | none |
| C19 | Don't fix your ending in advance; don't hoard your best idea (V23 32:41 to 34:19) | C | S1 | none | Coaching. | He suggests it may be just his personal preference (V23 32:41). For drafting only. |
| C20 | Concision comes later; early pruning is "writing anorexia" (V23 34:19 to 35:22) | design | S1 | D | The skill never runs compression checks (M1 to M5) on a thinking draft. | none |
| C21 | Artist and architect (V23 35:22 to 36:18; V42 14:20 to 20:01) | C | S1 to S2 | D | The vocabulary for switching modes. | none |
| C22 | Revision as recursive writing: pause, reread, map the shape, find the strongest thoughts (V23 36:18 to 38:09) | W | S1 | none | The *writer* rereads during drafting. The skill doesn't judge. | See the §7 tension with V19's strict separation. |
| C23 | Research counts as writing if it serves the piece (V23 38:09 to 39:56) | J | S1, B | Q | J: "Are you reading for a specific gap, or avoiding the page?" | none |
| C24 | Scholar before researcher: draft the review before designing the study (V1 3:13 to 5:23) | W | Plan, S1 (academic) | none | An interview question for academics. | none |
| C25 | Unpack the library: juxtapose notes at random (V7 0:00, 39:21; V41 27:53) | W | S1 | WN | The skill can surface random notes from the writer's vault. | none |
| C26 | The expert's curse: block means reader awareness arrived too early (V20 1:05 to 4:04) | C | B, S1 | none | A reframe. | none |
| C27 | Two conversations: rehearsing or discovering (V41 28:56 to 31:10) | J | S1, S4 | none | J: "Does this passage sound like your stock presentation?" | none |

### 3D. Block, habits and process

| ID | Technique (sources) | Use | Stage | Inputs | How the skill uses it | Don't apply |
|---|---|---|---|---|---|---|
| D1 | Name the block as fear; fear only shows up for writing that matters (V23 0:00 to 2:36) | C, W | B | none | W: "Is this a piece that matters to you?" | none |
| D2 | Habit design (2025): invent the person who writes; about two months of discipline; mornings; a consistent pattern; announce the habit, not the project; two pages or the Seinfeld rule; the arithmetic; a stopping point; one writing place (V23 3:26 to 13:37) | W, C | B | none | Help the writer build a plan in their own terms, aiming low (V23 13:37 to 16:20). | For creative projects that are uniquely the writer's, his 2026 view is that discipline is the wrong frame (V41 0:00 to 3:07, 21:17). Habits still suit routine writing (V41 13:46). The skill asks which kind of project it is. |
| D3 | The missed-goal protocol: forgive, look forward, never carry the debt (V23 16:20 to 19:52) | W | B | none | Coaching. | none |
| D4 | Stuck mid-session: open a new document and type "I'm stuck because…" for 5 to 10 minutes (V23 19:52 to 22:22) | W | B | none | Exercise. | none |
| D5 | Lost faith: reread slowly as a reader, then outline what you actually have (V23 22:22 to 24:09) | W, J | B, S2 | Draft | W: the writer rereads and outlines. J: the skill then checks the outline's logic (see F1). | none |
| D6 | Talk it through with one trusted person; share work while it's struggling (V23 24:09 to 25:45) | C | B | none | Recommend it. Groups larger than 3 or 4 tend to be too polite. | none |
| D7 | Virtuous procrastination; the perfectionism loop; say your excuses out loud (V11 5:13 to 5:30; V23 25:45 to 30:00) | J, W | B | none | J: "Does this task move the piece forward?" W: set a release date. | The business side still needs doing (V23 27:37). |
| D8 | Block as a signal; a project chosen by a past self; put it away (V41 0:00 to 3:07, 9:08 to 10:46, 14:41 to 16:41) | W | B | none | W: "Who chose this project, and when? What keeps interrupting you?" | Letting go is painful (V41 11:28). Not for routine writing (V41 13:46). |
| D9 | Explanatory models: Lacan's three registers (V41 5:36 to 10:46); elephant and rider (V41 14:41) | C | B | none | Optional lenses only. The skill does not psychoanalyse the writer. | He says the layers can't be dispensed with (V41 9:34). |
| D10 | The night shift: stop, hand the problem over, catch the images (V41 16:41 to 20:09) | C, W | B | none | Coaching. | none |
| D11 | Finisher or voice-seeker (V44 4:35 to 10:18) | W | B | none | Two diagnostic questions route the writer: a deadline and a partner for finishers; readers and craft for voice-seekers. | none |
| D12 | Accountability partner; early readers; a community of practice (V44 7:46, 28:00 to 34:31) | C | B, S6 | none | Recommend them. The skill cannot stand in for them (§5.6). | A community tacked on at the end is not enough (V44 33:37). |
| D13 | Write with stakes: publish under your name to readers you respect (V36 13:48 to 19:29) | C | B | none | Coaching. | Exploratory writing needs safety *(inferred, V36 22:59)*. |
| D14 | One tool at a time (V12 51:02; V19 1:14:43; V23 40:48) | design | all | none | Caps how much each pass returns. | none |
| D15 | The paradox of the fear of publishing; signs of success (V19 1:05:09, 1:13:02 to 1:14:43) | C | B, S6 | none | Coaching. | none |
| D16 | Share ideas and let opportunities find you (V44 0:51 to 4:35, 13:07 to 14:02) | C | B | none | Coaching. | none |
| D17 | Don't force it: listen to resistance that survives every method (V11 10:41 to 11:16) | C | B | none | Tell this apart from momentary distraction during a timed session, which should be refused (V11 3:32). | none |

### 3E. Notes and capture

| ID | Technique (sources) | Use | Stage | Inputs | How the skill uses it | Don't apply |
|---|---|---|---|---|---|---|
| E1 | A windmill, not a filing cabinet: judge the system by its output (V40 0:00 to 1:39) | J | Notes | WN | J: "Which part of your system only stores?" | none |
| E2 | Two input streams, culture and life, plus a dream log (V40 1:39 to 4:00) | W | Notes | none | Recommend them. | The sources folder is for collecting only (V40 2:06). |
| E3 | Daily note and weekly note (V40 4:00 to 5:53) | W | Notes | none | The skill may create the empty template. | none |
| E4 | Fleeting note with a timestamp ID (V40 5:53 to 7:26) | W | Notes | none | The skill may create the ID; the writer types the note. | none |
| E5 | Literature note as a dialogue with the text; the same/different question (V40 7:26 to 10:37; V44 21:35) | W | Notes | E | The skill asks "Where is this the same as what you think, and where is it different?" It never writes the response or summarises the source. | Most literature notes will never be used, and that's fine (V40 10:37). |
| E6 | Permanent note: one idea, in your words, with two links (V40 10:37 to 13:50) | W, M50 | Notes | WN | M50 flags orphan notes and notes holding several ideas. The writer writes the notes. | none |
| E7 | Let patterns surface; note where ideas agree and differ (V40 13:50 to 15:54) | W | Notes | WN | The skill may retrieve candidate related notes. The writer writes the comparison. | none |
| E8 | AI as a read-only navigation layer: index, hub and structure notes, weekly review, Q&A, outputs kept apart (V40 15:54 to 23:23) | allowed AI use | Notes | WN | See §5 and the Notes mode (§6). | It must not summarise sources or tell him the main ideas (V40 15:54). See §5.4 for the tension with the index agent. |
| E9 | Collect scraps and interesting names (V12 29:53 to 31:16, 40:37 to 41:39) | W | Notes, P | none | Recommend. | Names are mainly for narrative *(inferred)*. |

### 3F. The bridge: from the writer's draft to the reader's

| ID | Technique (sources) | Use | Stage | Inputs | How the skill uses it | Don't apply |
|---|---|---|---|---|---|---|
| F1 | Reverse outline: label what each part *does*; anything you can't label is fluff or still tangled; read the labels alone; line them up with the reader's questions (V23 22:22 to 24:09; V35 8:11 to 9:41; V47 18:15 to 22:07) | W first, then J | S2 | Draft, R | The *writer* writes the labels, because they are the writer's thinking. The skill then asks: which labels repeat? Which follow the order of discovery? Where does the claim first appear? If the writer asks the skill for labels, it offers them as a cold reader's hypotheses for the writer to correct. A mislabel is itself a finding: if the skill misreads a section, so may a reader (the logic of V44 17:02). | Not an outline before drafting (V47 20:14). |
| F2 | Label test at paragraph and section level; one message per paragraph (V21 15:32, 29:54 to 30:30; V22 19:00 to 20:27) | J, W | S2 to S3 | none | Same approach as F1. | A one-sentence paragraph is fine when its job fits in one sentence (V22 20:27). |
| F3 | Diagnose interference. Writer patterns: the answer at the end, order of discovery, background first, narrated thinking, side trails, unpacked shorthand (V19 25:11 to 27:22; V31 18:37 to 21:37; V35 11:09; V47 0:00 to 3:55, 9:18, 12:59) | J, M26 | S2 | D, R | J lists which writer patterns appear, and where. M26 pulls out the introduction and conclusion, and finds narrated-process markers ("at first I thought", "then I realized", "eventually it became clear"). | Don't apply while the writer is still generating (V47 21:09). |
| F4 | A new document for readers, rebuilt from where the reader starts (V19 27:22 to 29:54; V20 7:40 to 9:33; V31 8:47; V47 9:18 to 12:03); in practice, pull the points out of the old draft and relocate them (V50 0:00, 15:06) | W, C | S2 | none | Coaches the writer to open a new document and rebuild from the reader's starting point, pulling points from the thinking draft. The skill never merges or paraphrases the thinking draft into the reader draft. | A routine summary may not need two documents *(inferred, V47 16:21)*. |
| F5 | Compare the point sentences in the introduction and the conclusion; synthesise the sharper one (V50 4:24 to 8:23) | M26, W, J | S2 | Draft | M26 pulls out both sections. W: the writer underlines one point sentence in each. J: "Is it the same point? Which is sharper?" The writer does the synthesis. | Writing that makes no point (V50 0:48). |
| F6 | Mine the sympathetic middle-rated reviews or beta comments (V18 1:47 to 2:38) | W, J | S6 | Feedback | J: group recurring complaints and trace each to promise, purpose, structure or voice. | none |

### 3G. The point and the argument

| ID | Technique (sources) | Use | Stage | Inputs | How the skill uses it | Don't apply |
|---|---|---|---|---|---|---|
| G1 | Claim test: significant, non-obvious, debatable. Someone else must be wrong ("water is wet" fails) (V3 8:00 to 8:57; V17 13:18 to 13:36; V25 8:27 to 9:25; V50 17:54, 22:13 to 23:11) | W, J | S2 to S3 | P, R | W: the writer writes the claim as one sentence. J: "Who would disagree? Would this reader need evidence? Does it change their understanding?" If not, the writer sharpens it. | A level-5 platitude is not a point, while level 4 is (V50 22:13). |
| G2 | Claim, evidence, warrant; "point *because* reason"; the bridge sentence (V17 6:42 to 7:38; V19 1:04:23; V25 8:27 to 11:00; V50 17:24 to 21:04) | W, J | S3 | P, E, R | W: the writer states each main point as "[point] because [reason]". J: find links that are only plausible (the skill, as a cold reader, is suited to this; see §5.6), then ask the writer for the bridge. | The three parts needn't be three sentences, but all three must be there (V50 18:24). |
| G3 | Use evidence *this* reader accepts (V19 1:04:23; V25 9:25 to 10:02; V50 18:24) | J | S3 | R, Gen | J: "Is this the kind of evidence your reader trusts, such as data, a case, a primary source or experience?" | none |
| G4 | Answer objections where they arise; the three standard buckets are other causes, counterexamples and definitions (V3 8:57 to 9:31; V19 15:13 to 16:59, 57:59 to 1:00:28; V20 22:49 to 24:25) | W, J | S3 | P, R | W: the writer lists the objections their reader would raise. J: for each main claim, which bucket is unanswered, and does the answer come where the doubt arises? | none |
| G5 | Make the judgment call (V39 3:20 to 4:58) | J | S3 | none | J: flags "some say X, others Y" with no verdict, and asks the writer what the evidence supports. | If credentials are thin, borrow credibility by quoting an expert, but still make the judgment (V39 4:15). |
| G6 | Analysis, not description: how it works, why, what follows (the watch test) (V3 2:32 to 3:43; V12 46:41 to 47:33) | J, M (weak) | S3 | none | Weak mechanical signal: paragraphs with no relational words (because, so, which means, therefore). J: "How does this work? Why? What follows for the reader?" | Assignments that actually ask for a summary (V3 2:32). |
| G7 | Calibrate certainty to the evidence and the community (V3 9:31 to 11:39; V18 32:35 to 33:25; V19 1:02:00 to 1:05:09; V50 30:18 to 35:11) | M18, J | S5 | Gen, E | See M18. J: "Does the strength of this claim match your evidence and your readers' norms?" | Peer-reviewed communities expect more hedging (V19 1:02:55). Idea books and gift books expect less (V17 12:13, 35:19). |
| G8 | Disagree without making enemies: concede first; enter the conversation politely (V12 14:37 to 18:09; V19 35:19 to 40:04; V22 8:14; V28 4:20) | J | S3 | R | J: "Is the view you're overturning stated fairly and credited before the turn?" | "You don't always have to do this" (V19 38:53). |
| G9 | Research builds the problem, not a display of reading (V19 40:04 to 42:56) | M43, J | S3 | E | M43 flags runs of "X argues… Y shows…" with no follow-up. J: "What should the reader do with this citation? Does it create tension?" | none |
| G10 | Head off "this isn't new" (V22 26:27 to 27:16) | J | S3 | R | J: "What nearby idea will readers think of first? Where did it fall short?" | none |
| G11 | The reader-belief frame: the idea you hold, what's wrong with it, what it costs you (V31 5:35 to 7:55) | W | S2 | R | W: three lines written by the writer. | Phase one, where writing about what interests you is fine (V31 7:55). |
| G12 | Boldness for idea books (V17 9:13 to 14:44; V16 12:21 to 15:14) | J | S3 | Gen, G | See §7 (hedging versus boldness). | Academic writing needs restraint (V17 12:13). |

### 3H. Introduction, title and conclusion

| ID | Technique (sources) | Use | Stage | Inputs | How the skill uses it | Don't apply |
|---|---|---|---|---|---|---|
| H1 | The problem-first introduction: status quo or common ground, concession, the destabilising *but*, the cost or benefit to this reader, then the solution (V19 30:43 to 33:26; V22 5:23 to 11:17; V24 8:15 to 12:20; V27 25:12 to 31:36; V28 4:20 to 14:52; V31 0:52 to 7:55; V46 3:52 to 8:20) | J, W, M25 | S3 | R, P, CW | J: find each move in the opening and name the one that's missing. W: the writer drafts a five-line skeleton: invert the point to get the status quo, and choose history, a recent event or a common belief as the common ground (V28 6:16 to 7:43). M25 flags openings built on background, definitions, "in this essay I will", the gap model, or the author's effort. | Narrative creative nonfiction can open on an image (V21 4:20). The status quo can be an accepted state whose cost nobody has counted, not only the literal opposite (V28 5:18). Don't copy his skeleton wording (V27 29:04; V28 13:36). |
| H2 | The two-vendor test (V28 1:15 to 4:20) | M47, J | S3 | none | M47 highlights writer-centred phrases (effort, conviction, excitement, reading-time warnings). J: "Which vendor does your opening sound like?" | He notes the Mack essay he critiques succeeded anyway (V28 2:27). |
| H3 | The "so what?" test gives you the consequence; keep condition and consequence close together (V19 1:07:30 to 1:08:47; V28 10:19 to 11:53) | J, W | S3 | R | Asked in the reader's voice. J also checks the distance between the *but* and the stated cost. | It needs a specific reader, not a general audience (V28 11:00). |
| H4 | Keep *but* and *however* for the problem turn (V28 11:00; V31 4:34 to 5:35; V34 8:51 to 9:42) | M19 | S3, S5 | none | See M19. | none |
| H5 | Solution preview: give a promise and a direction, not details; practical or conceptual (V28 12:20 to 14:52) | J | S3 | P | J: flags a vague solution ("we need to think differently") or a background lecture in its place. | Previews only, no details (V28 13:06). |
| H6 | The optional prelude (V28 15:14 to 15:55) | J | S3 | none | J: "Does the prelude replace the problem?" | If the problem is interesting, no prelude is needed (V28 15:14). |
| H7 | Loaded value words in the status quo (V22 6:18 to 8:14) | J | S3 | CW | J: do the words describing the old view frame it as dated, accurately and with restraint? | Not contempt (V22 8:14). |
| H8 | The introduction previews the structure (V22 32:40 to 34:30) | M49, J | S3 | KT | M49 checks whether the key nouns in the section headings appear near the end of the introduction. | none |
| H9 | The point at the end of the introduction by default; point last as an advanced option with its key terms previewed (V24 4:18 to 7:28; V47 3:55; V50 8:23 to 11:36) | J, M26 | S3 | P | J finds the writer's point sentence and where it sits. If it comes last, J checks that its key terms were previewed early and come together at the end (V50 10:42). | Point last is acceptable in creative nonfiction and at section level (V50 9:37). The V21 model essay withholds its thesis. |
| H10 | The title: it is the first line; a curiosity trigger; three key-term nouns; no inside jokes or keyword parking lots (V6 2:43 to 5:27; V46 1:04 to 2:55) | W, J, M24 | S3, S5 | KT, R | W: the writer drafts one title for each of the four triggers. J: "Which trigger does it use? Does the piece pay off the loop?" M24 checks that the title's nouns recur and flags coined terms. The skill does not write titles, because they are reader-facing text (§5). | Search and reference pieces may need a descriptive title *(inferred, V6)*. So may a committed audience *(inferred, V46)*. |
| H11 | The conclusion returns to the problem, shows it solved and pushes off higher; not a summary (V46 16:18 to 19:48) | M26, J | S3 | P | M26 flags "In summary", "In conclusion" and "To sum up", and high word overlap with the introduction. J: "Does it end at a higher level than it began?" | none |
| H12 | If you fix one thing, fix the introduction (V46 19:48) | design | S3 | none | Sets the priority order in Architect mode. | none |
| H13 | The engine of the story and the Bilbo moment: open on something that raises the question, and build trust with a simple concrete story before abstraction (V12 33:24 to 35:03, 41:39 to 44:07) | J | S3 | R | J: "Is there a moment that raises the question the piece answers? Does a concrete case come before the theory?" | The engine is framed for stories; the nonfiction equivalent is an anomaly *(inferred)*. |
| H14 | Curiosity loops, the four triggers (V6 3:54 to 5:27; V46 2:16) | C, J | S3 | R | J: "Is a loop opened, and is it closed?" | A trigger the piece doesn't pay off is bait *(inferred)*. See also J12. |

### 3I. Structure and coherence

| ID | Technique (sources) | Use | Stage | Inputs | How the skill uses it | Don't apply |
|---|---|---|---|---|---|---|
| I1 | Index and discussion at every scale, which he calls fractal (V18 21:12 to 25:41; V27 37:51 to 43:21; V46 8:20 to 12:43) | M22, J | S3 | P, KT | M22 pulls out the indexes. J: does each index state a *problem or point*, not a topic, and name its key terms? One to three sentences for a paragraph. | Point-last sections (V50 9:37). Narrative creative nonfiction. |
| I2 | The skim test, which doubles as a reverse outline (V46 12:12; V47 19:13 to 21:09) | M22, J | S3 | none | A script produces the skim view. The model and the writer read it as a storyboard. | none |
| I3 | Underline the paragraph's point and promote it (V18 22:07 to 22:33; V50 14:49 to 15:06) | W, J | S3 | none | W: the writer underlines it. J: if nothing can be underlined, the paragraph needs reworking. | none |
| I4 | Order sections by the questions the point raises, in the order they arise (V19 47:22 to 49:20; V50 12:16 to 13:57) | W, J, M46 | S3 | P, R | W: the writer lists the reader's questions in order. J: compare that list with the section order. M46 flags "First, / Second," used as though it were an organising principle. | Don't impose a rigid order such as chronology (V50 13:22). |
| I5 | Problems and subproblems as the architecture (V19 33:26 to 35:19) | W, J | S3 | P | W: map the subproblems to sections. | He calls it "a bit of a conceit" imposed on discovery (V19 34:34). |
| I6 | Transitions that round off and push on; a question as a palate cleanser (V50 15:50 to 16:32) | J, M42 | S3 | none | M42 measures rhetorical-question density. J: "Is this the question the reader is actually asking?" | Rhetorical questions are overused (V50 15:50). |
| I7 | Key terms: announced in the index and repeated; a "constellation" of terms (V24 12:20 to 15:13; V46 13:26 to 15:51) | M23, J | S3 to S4 | KT | M23 counts terms and detects drift. J: "Is anything in this discussion not anchored to the index?" | Synonyms are fine in topic chains. Previewed terms must stay exact (V48 20:31). |
| I8 | Train readers in your naming system early (V19 45:45 to 47:22) | M41, J | S4 | KT | none | none |
| I9 | The four signals of coherence; the map before the terrain; headings built from key concepts (V27 31:36 to 37:51) | M49, J | S3 | KT | M49 flags headings that share no term with their section (cryptic headings). J: "Is there an introductory segment, and does it end on the point?" | Motivated readers tolerate more, but no one survives incoherence (V27 32:42). |
| I10 | One theme and two or three points as the thread (V22 17:32 to 19:00) | W, J | S2 to S3 | P | W: one line for the theme, then the points. J: which paragraphs serve none of them? | none |
| I11 | "Do you need that?" from large units down to small (V22 2:24 to 3:19) | J | S3 for sections, S5 for words | P | Questions about what to cut, working top-down. | Not during drafting (V23 34:19). |
| I12 | The 3D cube puzzle and orphaned ideas; Grice's point that readers assume every sequence is meant (V18 15:26 to 20:19; V24 18:11 to 20:59) | J | S3 to S4 | none | J: for each adjacent pair of paragraphs or sentences, say why B follows A. If you can't, add a bridge or move B. | Pantsing is fine while exploring (V18 16:48). |
| I13 | Context first: meaning shifts with what comes before (the red-yellow-blue test) (V18 20:19 to 21:12) | J | S3 to S4 | R | J: "What must the reader already have in mind for this to mean what you intend?" | none |
| I14 | A table of ideas for each chapter (V18 23:07) | W | Plan, S3 | none | The writer lists the point sentences in order. | Not while drafting to explore (V18 17:41). |
| I15 | The uneven U: start at level 4, go down to evidence at level 1, interpret it, return to level 4, then push off to level 5 (V18 23:07 to 25:41; V50 21:38 to 30:18) | J, M27 | S3 | P | J: tag each sentence with its level (5 to 1) and check the shape. M27 flags paragraphs that open on a statistic or quote, and paragraphs that end on one. | Adapt it: he says it reflects his literary-criticism training (V50 28:54). |
| I16 | No hit-and-run quotations (V50 24:47 to 25:19, 29:31) | M27, J | S3 | none | none | Epigraphs; deliberate endings in creative nonfiction *(inferred)*. |
| I17 | Private, contextual and textual structure; heavy metadiscourse as a symptom of private structure (V49 6:42 to 14:02) | J, M15 | S3 to S4 | Gen | J: "What is the principle behind this order, and could the reader know it?" M15 measures metadiscourse density. | Metadiscourse isn't banned (V49 11:14). |
| I18 | Label the relationships: logical bridges and transitions (V18 22:33 to 23:07; V24 18:11 to 21:04) | J | S4 | N | J at each unlinked pair of sentences. | When the relationship is painfully obvious (V18 23:07). |
| I19 | Plan the reader's journey as a decision tree (V20 21:38 to 24:58) | W | S2 to S3 | R | W: the writer answers his planning questions: reservations, prior agreement, resistance, whether they want a critique, which counterarguments. | The thinking phase. |
| I20 | Every sentence is a tile on the path: name its job (V19 18:46 to 21:25; V20 17:08 to 21:38) | J | S3 | R | J: "What is this sentence doing here: problem, evidence, background, turn?" If it has no job, cut it. | none |
| I21 | Coherence at every level: sentences, paragraphs, sections, chapters (V18 15:57 to 16:48) | J | S3 to S4 | none | J: at each level, does the unit link back and set up what comes next? | none |

### 3J. Examples, concreteness and story inside exposition

| ID | Technique (sources) | Use | Stage | Inputs | How the skill uses it | Don't apply |
|---|---|---|---|---|---|---|
| J1 | Concrete, sensory language a reader "could stub their toe on" (V9 9:17 to 13:32; V12 10:56; V22 13:48 to 15:28; V26 9:19 to 11:54) | J, M12 (concreteness) | S4 | R | M12 scores the concreteness of subjects and nouns, and flags "X of Y occurred" patterns. J: "Can you picture it?" | Not a licence to pad *(inferred, V9)*. Concreteness is not the same as the active voice (V26 10:24). |
| J2 | An abstraction made into a character with verbs (V9 12:44 to 13:32) | J | S4 | none | J: "Is this abstraction the object of 'is', or the subject of an action?" | none |
| J3 | The ladder of abstraction: move between levels (V12 10:56 to 12:09) | J, M12 | S3 to S4 | none | A paragraph abstractness profile. J: "Is this all high, or all low?" | He asks for balance, not a ratio. |
| J4 | The intuition pump, rather than a plain example (V22 28:15 to 30:25) | J, W | S3 | R | J: "Where must the reader take your word for it?" W: find a familiar situation with the same structure. The writer chooses it; the skill does not. | none |
| J5 | Story, then one-sentence lessons, then named concepts, then redeploy them like chess pieces (V22 23:32 to 28:15) | J, M23 | S3 | KT | M23 flags concept names that drift. J: "Is this example told but never summed up?" | none |
| J6 | Examples in the order AA-B, not A-B-A (V12 45:38 to 46:41) | J | S3 | none | J: flags a pattern of example, qualification, back to the example. | none |
| J7 | Abstraction delivered through a concrete moment (V21 27:01 to 28:33) | J | S3 (creative nonfiction) | none | J: "Is there a scene in front of each stated lesson?" | none |
| J8 | Foreground what you saw; put the research in the background (V39 5:39 to 11:29) | W, J | S3 (narrative) | E | W: sort material into research, interviews and reporting. If the reporting column is empty, go and get some. | Visual detail must serve the question (V39 9:54). |
| J9 | Teach inside the scene, without breaking for exposition (V39 5:39 to 8:57) | J | S3 (narrative) | none | J: flags "X is a Y that does Z" definitions that stop the story. | none |
| J10 | Characters, not labels (V39 20:04 to 22:57) | M36, J | S4 | none | M36 flags evaluative adjectives about people. J: "Which action shows this?" | none |
| J11 | Interview the person, not the source (V39 21:58 to 22:57) | W | S1 | none | Suggested interview questions. | none |
| J12 | Expectations, setups and payoffs; a motif as a recurring chord (V21 8:40 to 9:25; V26 11:54 to 13:21; V39 13:36 to 16:37; V42 2:12 to 3:31) | J | S3 | none | J: map what is planted and where it pays off, and flag promises never paid. | Hype words are not the device (V26 12:53). Value-free hooks are out (V28 0:00). |
| J13 | Dramatize ideas (V7 36:47 to 38:32) | C | none | none | Coaching only. | none |

### 3K. Paragraph and sentence flow

| ID | Technique (sources) | Use | Stage | Inputs | How the skill uses it | Don't apply |
|---|---|---|---|---|---|---|
| K1 | Characters as subjects, actions as verbs (V6 6:03 to 12:04; V12 32:10 to 33:24; V24 15:13 to 18:11; V27 0:41 to 5:34; V37 3:13 to 4:21) | M6, M7, J | S4 | R, N | M6 and M7 flag nominalizations and empty verbs. J: "Who does what here? Is that character in the subject, and the action in the verb?" | Old-before-new can win over a human subject (V37 13:39 to 14:29). Familiar concepts can serve as characters (V27 9:21). |
| K2 | The three-step fix for zombie nouns: put the action in a verb, make the doer the subject, then link the clauses with logic words (V8 2:52 to 8:06; V12 47:33 to 48:28) | C, J | S4 | N | The skill explains the three steps on a *parallel* example (§5.7). The writer rewrites their own sentence. | Use the passive when the agent is unknown (V8 6:33). The suffix tip both misses and overflags (V8 4:39). |
| K3 | Triage nominalizations; they have four legitimate uses (V27 5:34 to 11:43) | J | S4 | R, N | J sorts each M6 hit: a hidden action, a subject linking back, a replacement for "the fact that", an object, or a term so familiar to these readers it acts as a character. Only hidden actions and false-agent subjects are raised. | Leave the four legitimate uses alone (V27 11:03). |
| K4 | Empty verbs: *occurred*, *resulted in*, *took place* (V27 4:16; V32 10:31 to 11:43, 18:32) | M7, J | S4 | none | J: "What is the real action, and who does it?" | none |
| K5 | Short subject, early verb: the tunnel, the locomotive, the runway (V8 0:42 to 2:27; V12 0:41 to 2:26; V27 21:11 to 25:12; V37 16:40 to 19:35) | M8, J | S4 | N | J: "Is the reader holding their breath?" | A long subject made of old information may be linking back to the previous sentence *(inferred, V8)*. Length *after* the verb is fine (V27 24:45). |
| K6 | Move long introductory clauses (V12 48:28 to 49:26) | M9, J | S4 | N | none | A *since* clause that marks known information belongs up front (V32 20:19; V37 14:29). |
| K7 | Don't split a verb from its object; place the interrupting phrase according to what the next sentence picks up (V12 49:26 to 51:02) | M10, J | S4 | N | J reads sentence N+1 to decide where the interrupter goes. | none |
| K8 | Old before new: topic first, comment after (V8 8:46 to 11:53; V15 7:58 to 12:29; V37 4:21 to 4:53; V48 3:00 to 4:02) | M13, J | S4 | N | none | A deliberate reveal (V26 2:51). |
| K9 | The two-charge sentence: every sentence needs something old and something new (V15 2:58 to 7:58) | J | S4 | R | J: flags sentences with nothing new (cut or merge them) and sentences with no old anchor (add context). | What counts as "old" depends on the reader (V15 5:16). |
| K10 | Handoffs between sentences: the relay race, the handshake, the Busan taxi driver (V9 9:17; V15 17:20; V26 4:55 to 5:48; V27 11:43 to 15:07) | M13, J | S4 | N | none | Handoffs alone can produce a smooth chain that goes nowhere (V27 15:42 to 17:46). |
| K11 | Cohesion versus coherence; underline the first seven or eight words of each sentence; keep a clear focus (V15 12:29; V27 15:07 to 21:11; V32 3:50 to 5:46) | M12, J | S4 | R | The script prints the underlined openings. J asks three things. Could you predict the passage's subject from them? Could you draw them? Would *this reader* see them as one related set? | "In most of your sentences", not all (V27 20:05). |
| K12 | The movie-poster test: whose story is this? (V32 0:23 to 2:14, 5:16) | J, W | S4 | R | W: the writer names the star. J: is the star in the opening positions? | none |
| K13 | Two skis: keep the sentence topic in line with the passage topic; don't vary topics for variety's sake (V9 1:55 to 6:01; V19 43:50 to 45:45; V22 11:17 to 13:04; V26 5:48 to 9:19; V32 5:46, 13:05) | M12, J | S4 | none | none | A deliberate topic change with a reason (V26 9:19). The whole-to-parts pattern (V48 13:14). |
| K14 | The reader-question test: choose the subject by what the reader cares about (V33 2:39 to 12:31) | W, J | S4 | R | J: for key sentences, phrase the question the reader would ask. W: for ambiguous cases, the writer decides which reader group the piece is for. | In some niches readers do care about the named expert (V33 11:10). He won't meddle with rules that already work for a writer (V33 8:08). |
| K15 | Identify the passive correctly: *be* plus a past participle, with the receiver of the action as subject (V14 7:44 to 10:59) | M11 | S4 | none | Identification only. It includes reporting false alarms from grammar checkers. | none |
| K16 | Choosing the passive: five uses (focus on the thing acted on, actor irrelevant, actor unknown, stress position, sound); keeping flow; controlling agency; the three-step conversion (V9 6:01 to 9:17; V14 3:03 to 7:04; V15 13:05 to 17:20; V24 16:49; V32 5:46 to 7:46; V42 4:27 to 9:28) | J | S4 | R, N | For each passive M11 identifies, J asks which use it serves, whether it links, and whether it hides an agent the reader needs to see (V14 5:51; V42 7:12). | About 5% of sentences (V6 11:47; V15 13:34) is a sanity signal, not a quota. |
| K17 | The stress position: keep weak words out of the end of the sentence (V2 9:38 to 10:48; V14 13:50 to 16:03; V26 13:21; V37 16:03) | M14, J | S4 | none | none | Speech. Split infinitives are often fine (V14 15:45). |
| K18 | Four topic-progression patterns, chosen by purpose, each with a failure mode: constant topic, linking, whole-to-parts, theme preview (V48 4:02 to 21:39) | J, M12, M23 | S4 | Purpose of each paragraph | J reads the topic list to identify the pattern, then checks its failure mode. Constant topic can stagnate; linking can run off the rails; whole-to-parts needs its umbrella named; theme preview breaks if the previewed terms are swapped for synonyms. | Patterns can be scaled up and nested (V48 21:39). |
| K19 | Sentence anatomy (topic and comment) and the colour-and-line diagnostic (V37 2:14 to 5:39) | M12, M13, J | S4 | none | Coreference chains plotted by slot. Lines that zigzag between sentence starts and ends are the sign of trouble. | none |
| K20 | The index position at the end of the first sentence; enumerators that point back to it (V37 7:25, 11:33 to 12:26) | J | S4 | none | none | Signposts only for heavy, complex lists (V37 11:59). |
| K21 | Subordinate the interpretation: ", which…" and then an *-ing* phrase (V37 9:04 to 10:48) | M31, J | S4 | none | none | When the two clauses really are equal (V37 9:27). |
| K22 | Use a transitive verb for changes that were caused (V37 10:48 to 11:33) | M30, J | S4 | none | none | Genuinely agentless natural processes (V37 11:12). |
| K23 | Split an overloaded sentence; demote the minor part with *since* (V32 19:16 to 20:19; V37 14:29 to 16:03) | J | S4 | P (the focus) | none | *Because* is not wrong (V32 20:19). |
| K24 | Demote attributions: move "according to X" out of an emphatic slot (V37 19:35 to 20:28) | M44, J | S4 | none | none | none |
| K25 | Close the loop: the last sentence echoes the index (V37 21:04) | J | S4 | none | none | none |
| K26 | When the two principles conflict (character subject versus old before new), weigh both (V37 12:26 to 14:29) | J | S4 | N | The skill sets out both options with the effect of each. The writer decides. | He treats it as a judgment call and invites alternatives (V37 13:11). |
| K27 | Order clauses cause then effect; reduce a secondary effect to an *-ing* phrase (V32 9:08 to 10:31) | J | S4 | none | none | none |
| K28 | Pack sprawling phrases into noun-phrase "suitcases"; keep "including" next to its category (V32 12:05 to 13:05) | M48, J | S4 | none | none | The awkward version isn't wrong (V32 12:05). |
| K29 | Familiar before new inside a phrase (V32 15:35 to 16:34) | J | S4 | N | none | none |
| K30 | Hyponyms and related forms count as repetition (V32 10:11, 21:13 to 21:41) | design | S4 | none | Makes M12 and M13 match lemmas, category members and near-synonyms. | Only if the umbrella term was actually introduced. |
| K31 | Signpost the zoom-in with "for example"; keep transitions rare (V32 17:01 to 18:32) | J | S4 | none | J: where the topic string breaks, "Is this an illustration? Mark it." | Overused transitions (V32 17:37). |
| K32 | Replace metadiscourse with conversational moves (a question, visual language, moving together), then reorganise (V9 13:32 to 16:45) | M15, J | S4 | Gen | none | Spoken scripts. Sparing use is fine (V9 14:50). |
| K33 | Abstract pronoun plus *be* ("That is why…", "It is the case that…") (V6 10:41) | M17 | S4 | none | none | none |
| K34 | Keep parallel names in a consistent order (V37 7:53) | M (low priority) | S5 | none | none | He calls it a small point. |
| K35 | The sentence-purpose question; judge a sentence by its effect in context (V10 4:40 to 6:56) | J | S4 | R | J: "What should the reader see here?" | Mechanics still matter at proofreading *(inferred)*. |
| K36 | Sentence length follows the load it carries (V42 0:00 to 4:27) | anti-check, J | S4 | none | Never suggest varying length. For a long sentence, J asks: "Is it coordinated and balanced, or carrying too much?" | none |
| K37 | Fewer function words; syntax as the DNA of an idea (V5 4:43 to 5:53) | M38 | S4 (introductions) | none | none | He ties the finding to introductions. Collapsing too far produces noun stacks *(report caution)*. |
| K38 | Write so the reader feels smart, not so you look smart (V5 2:05 to 4:43) | J | S4 | R | none | Don't simplify the ideas themselves (V5 3:55). |
| K39 | Grammar at the mechanics stage: pronoun case, agreement, comma splices, dangling participles, the Oxford comma (V2 4:56 to 19:54) | M51 | S5 | Gen | Flags only. | Speech or transcribed speech, for run-ons (V2 12:33). House style decides the Oxford comma (V2 15:33). |
| K40 | Litotes as a deliberate half-positive (V2 2:12 to 4:24) | J | S5 | none | Protects "not un-" from M5 when the partial positive is the intent. | none |
| K41 | Sentence-final prepositions: a style choice for formal writing, because the end carries stress (V2 6:59 to 10:48) | M14 | S5 | Gen | none | Speech. The fronted version can sound stuffy (V2 8:47). |

### 3L. Voice, persona, stance and register

| ID | Technique (sources) | Use | Stage | Inputs | How the skill uses it | Don't apply |
|---|---|---|---|---|---|---|
| L1 | Voice emerges from lived experience; style as integrity between thought and words (V36 1:10 to 5:55; V38 10:50 to 16:38) | J, W | S3 to S4 | none | J: "What in this section could only have come from you?" W: the writer adds their own material where it serves the point. The skill never supplies experience, anecdotes or perspective. | none |
| L2 | The persona on the page is not the author: be a partner, not a preacher (V18 25:41 to 27:28, 34:19 to 35:20) | J | S4 | none | J: "What kind of person do these sentences create? Does any sentence talk down?" | none |
| L3 | Take "you" out of the subject position when the sentence is really about an idea (V18 27:28 to 32:35) | M16, J | S4 | Gen | none | Advice columns, where you really are addressing the reader's situation (V18 29:43). |
| L4 | Personal language builds investment. Separate the author-function "I" from the flesh-and-blood "I" (V4 8:45 to 13:24; V5 5:53 to 9:53; V19 1:00:28 to 1:02:00; V22 20:49 to 23:32) | J | S4 | Gen | J: "Is there a person on the page where the reader's goodwill matters? Is 'I' owning a claim backed by evidence, or standing in for reasons?" (See V3 0:51.) | Methods and results sections (V5 8:01). Controversies where naming people inflames things (V4 13:03 to 13:24). Overuse (V19 1:01:27). |
| L5 | Inviting persuasion: questions, "let's look", "notice", "we" (V22 20:49 to 23:32, 26:27) | J | S4 | R | none | Rhetorical questions can be misused (V22 21:41). |
| L6 | Joint attention, the classic scene, blending (V30 2:44 to 15:41; V9 15:37; V43 4:05 to 4:56) | J, W | S4, P | R | J: "Where does the text leave the shared scene: a sudden lecture, an abstraction nobody can see, talking *at* the reader?" W: the blend exercise (T8). | Genres with strict conventions may limit tense and address; keep the showing anyway *(inferred)*. |
| L7 | Deliberate register: code words, $10 words and cheap words (V12 3:46 to 7:54; V42 9:28 to 14:20) | J | S4 | R, CW | J: "Is each specialist term a deliberate choice for this reader?" Feynman's check applies: can you say it plainly? (V42 13:46) | Empty obscurity (V42 13:46). Showy words (V12 5:57). |
| L8 | Understate the serious, overstate the light (V12 38:43 to 40:20) | J, M (weak) | S4 | none | Weak signal: stacked emotive intensifiers attached to grave nouns. J presents it as a choice. | He grants the explicit approach also works (V12 40:20). |
| L9 | Avoid clichés, which are dying metaphors (V12 37:40 to 38:43) | M35, J | S5 | none | none | none |
| L10 | Embodied metaphor and the portal test (V36 5:55 to 9:58) | J | S4 | none | J: "Does the familiar thing change how we understand the unfamiliar one? Would someone who had handled both things say this?" The skill never proposes metaphors; he says AI metaphors come out "a few degrees off" (V36 6:22). | The test doesn't require adding metaphors *(inferred)*. |
| L11 | Confident without arrogance (V19 1:02:00 to 1:05:09); qualifiers in balance (V18 32:35 to 33:25) | See G7, M18 | S5 | none | none | none |
| L12 | Stakes and early readers make voice (V36 17:19; V44 30:39 to 31:59) | C | B, S6 | none | Coaching: a flat voice often means there's no real reader (§6 Unstick). | none |

### 3X. Compression, calibration, punctuation and mechanics

| ID | Technique (sources) | Use | Stage | Inputs | How the skill uses it | Don't apply |
|---|---|---|---|---|---|---|
| X1 | Compression reduces cognitive load; it is not the same as shortness (V29 2:15 to 2:36, 15:56) | C, design | S5 | D | Frames every compression flag: "This costs the reader effort with no return in meaning." | Not in the thinking draft (V23 34:19). It is the start of polishing, not the end (V29 20:02). |
| X2 | Cut filler words (V29 2:36 to 5:39); prune intensifiers such as "very" (V6 1:08 to 2:43) | M1 | S5 | none | none | Keep a word that carries meaning. Keep qualifiers that change the claim *(inferred, V6)*. |
| X3 | Cut doublets (V29 5:39 to 7:18) | M2 | S5 | Gen | none | Fixed legal terms *(inferred)*. |
| X4 | Cut redundancy: modifiers, categories and general implications (V29 6:19 to 11:34) | M3, J | S5 | none | M3 catches the first two kinds. General implications need J: "What does this sentence say in the fewest words?" | He admits there's no firm rule for categories (V29 10:06). |
| X5 | Find the exact word to replace a phrase, *le mot juste* (V29 11:34 to 16:20) | M4, J | S5 | none | M4 uses a phrase list. J: "How many ideas does this sentence hold, and how many words?" | Don't reach for rare words to impress (V29 13:07). |
| X6 | Write in the affirmative, and watch for hidden negatives (V29 16:20 to 20:02) | M5, J | S5 | none | none | Keep the negative when the warning is the point (V29 20:02). Keep deliberate litotes (K40). |
| X7 | McCarthy's question, "Do you need that?", and the punctuation X-ray (V22 1:34 to 3:19) | M21, J | S5 | none | none | The X-ray diagnoses; it doesn't rule. |
| X8 | Calibrate certainty. The scale runs hedged, calibrated, strident. Fix two slots: the verb and the subject noun (V3 9:31 to 11:39; V50 30:18 to 35:11) | M18, J | S5 | Gen, E | J: "Is this claim hedged in the verb, or in the scope of the subject? Is the absolute covering a gap in the argument?" | Different fields have different norms (V19 1:02:55; V50 32:08). |
| X9 | Em dashes: exemplification, asides, mitigation; definitions belong in a ", which" clause; the loudness scale; read punctuation silently (V34 2:31 to 11:48) | M20, J | S5 | none | none | Never flag a dash as an AI tell (V34 1:42 to 2:31). |
| X10 | Emphasis economy: *however*, dashes and signposts all lose force when overused (V32 17:37; V34 4:36 to 5:35, 8:51 to 9:42) | M19, M20 | S5 | none | none | none |
| X11 | The headlights check: the visible risk of looking like AI versus the invisible cost of being unclear (V34 0:00 to 2:31) | C | S5 | none | Coaching when a writer self-censors a tool for fear of looking AI-written. | none |
| X12 | Mechanics last: proofreading, house style, platform conventions, presentation (V24 21:04 to 22:56) | M51 | S5 | Gen | Flags only. Online tools are acceptable here (V24 21:58). | Don't start here (V24 21:36 to 21:58). |

### 3Z. Figures and memorable lines (V12's rhetorical tools)

A skill uses these mainly as C and P: it explains the figure and drills it on the writer's own content (T-drills). At S5 it can ask a J question: "This is the line you want remembered. Is it built to stick?" No reliable mechanical check is worth running. Detecting alliteration or anaphora is easy, but flagging it helps no one.

| ID | Figure (sources) | Use | Note for the skill | Don't apply |
|---|---|---|---|---|
| Z1 | Deliberate grammatical "mistake", which the captions render as "analogy", almost certainly enallage (V12 2:45 to 3:46) | C, J, P | Protect it as a deliberate break (A3). | Needs readers who trust that you know the rule. If frequent, or in a routine report, it reads as an error *(inferred)*. |
| Z2 | Ironic juxtaposition (V12 7:54 to 9:14) | C, P | none | none |
| Z3 | Alliteration (V12 9:14 to 10:56) | C, P | none | It makes claims sound truer than they are, so keep it for claims you can support *(inferred)*. |
| Z4 | Polyptoton (V12 12:09 to 12:59) | C, P | none | none |
| Z5 | Antithesis, joined with a semicolon (V12 12:59 to 14:37) | C, P | none | Semicolons are otherwise often better avoided (V12 13:51). |
| Z6 | Diacope, epistrophe (V12 21:21 to 24:22) | C, P | none | none |
| Z7 | The forward-pointing opening pronoun, which the captions render as "prolapsus", almost certainly prolepsis (V12 24:22 to 25:40) | C, P | none | It can frustrate readers who scan reports for facts *(inferred)*. |
| Z8 | Piling up, which the captions render as "conju", almost certainly congeries (V12 25:40 to 27:40) | C, P | none | none |
| Z9 | Synesthesia (V12 18:45 to 21:21) | C, P | none | Everyday forms have become clichés *(inferred)*. |
| Z10 | A motif as a recurring chord (V42 2:12 to 3:31) | J | See J12. | none |

### 3O. Genre modules

Each module switches some default checks off and adds its own. The skill turns a module on when the writer names the genre, or when the brief makes it clear.

**O-cnf: creative nonfiction from ordinary experience (V21).** The default "point first" check is switched off (V21 34:19; V50 9:37). Opening with an image replaces the problem-first introduction.

| ID | Technique | Use | How the skill uses it | Don't apply |
|---|---|---|---|---|
| O1 | The creative/nonfiction grid: aim beyond the facts (V21 1:08 to 3:09) | W, J | W: "In one sentence, what deeper truth do these events point to?" J: "Would a stranger say 'OK, and?' at the end?" | Memos, manuals and reports are for plain information transfer (V21 1:30). |
| O2 | The opening image as a seed: every character and theme appears in it (V21 4:20, 7:53 to 8:40) | W, J | W: list the characters and themes. J: does anything first appear halfway through? | This is what he admires in this essay, not a universal rule. Professional writing leads with the point (V24). |
| O3 | Pointing the camera: what you select is what it means (V21 5:47 to 7:07) | J | J: "Could a reader guess the theme from what you chose to notice?" | none |
| O4 | Crossover linking: describe each thing in the other's vocabulary (V21 10:34 to 11:26) | C, J | none | Keep it subtle. |
| O5 | Research inside the story; no orphaned facts (V21 9:57 to 11:26, 18:02 to 19:47) | M (weak), J | Weak signal: an expository paragraph with no narrator present. J: "What job does this fact do, and which narrative moment brings it in?" | Non-creative nonfiction *(inferred)*. |
| O6 | The web of signification: word families and a contrast family; metaphors from the story's own world (V21 11:55 to 15:32) | W, M (possible) | W: circle the theme words in one colour and the opposing words in another. A lexical-field tagger could help. | none |
| O7 | Artistic licence, only in service of a purpose (V21 12:38 to 13:58) | J | J: "Does this reshaping sharpen a theme already in play?" | Journalism, or wherever readers expect verbatim accuracy *(inferred)*. |
| O8 | Label each section by its function to see the arc (V21 15:32, 29:54 to 30:30) | W | The same exercise as F2, applied to a model essay or to your own draft. | none |
| O9 | Plant and call back (V21 8:40 to 9:25, 22:33, 27:01, 33:46 to 34:19) | J | J: list what was planted and check that each returns, changed. | none |
| O10 | Abstraction through a concrete moment (J7); the subject as a mirror; a change of setting at the culmination; two time scales (V21 24:26 to 25:11, 32:03, 22:33, 35:10) | C, J | none | none |

**O-sci: narrative idea and science writing (V39).** The rows are J1, J8, J9, J10, J11, J12, B13, C9 and G5, plus these:

| ID | Technique | Use | How the skill uses it | Don't apply |
|---|---|---|---|---|
| O11 | Drive the piece with one question, so that digressions become relevant; keep the topic word out of the title if it repels (V39 0:32 to 3:20) | W, J | W: turn the topic into a puzzling case. J: "Does each episode help answer the question?" | none |
| O12 | Orient the reader in time with plain markers (V39 11:29 to 13:36) | M33, J | none | none |
| O13 | The one-word hyperlink: a word from the emotional thread, used accurately in a technical section (V39 18:44 to 19:04) | J | J: "Is the technical section cut off from the human story?" | Only where the word is accurate for the technical subject *(inferred)*. |

**O-imp: the impersonal essay (V43).**

| ID | Technique | Use | How the skill uses it | Don't apply |
|---|---|---|---|---|
| O14 | The dream test for private symbols (V43 0:21 to 1:11) | J, W | J: "Does this image's meaning depend on memories only you have?" | Readers who come to a memoir for the person *(inferred)*. |
| O15 | The impersonal turn: ask what it reveals about the world, not what it means to me; turn feelings into claims (V43 2:43 to 4:05, 9:46 to 10:09) | J, W, M (weak) | Weak signal: the density of "I" as subject. J: "Is each feeling reported, or argued as a claim about an object the reader can see?" | Not bland objectivity. The passion is redirected, not removed (V43 9:46). |
| O16 | Be in relation with the reader, rather than asking them to relate (V43 4:05 to 4:56, 8:50 to 9:46) | J | J: "Does the opening establish the writer's identity before showing the reader anything to look at?" | none |
| O17 | The value question: will the reader understand the writer, or the world? (V43 10:09) | W | W: "After reading, they'll see that…", finished without using "me". | none |
| O18 | Zadie Smith's six arrows: title in the centre; first and last lines written first; then promise, development, devil's advocate, wind down, reprise, conclusion (V43 4:56 to 8:50) | W, J | Use it once the writer knows their position (S3), or as a revision check. J: "Is there a devil's advocate move? Does anything new appear after the wind-down? Does the end arrive where the promise pointed?" | He doesn't limit it to a phase. Using it only after the thinking phase is a reconciliation with V42's anti-outline stance (read_09, "Across" point 7). Don't use it as a starting outline for thinking. |

**O-acad: academic writing (V1, V3, V4, V5).**

| ID | Technique | Use | How the skill uses it | Don't apply |
|---|---|---|---|---|
| O19 | Choose the review's method first; choose from the menu of review types (V1 5:23 to 8:56) | W | W: decide coverage, controversies, depth of critique and layout before drafting. Match the review type to its purpose. | none |
| O20 | The peer-review complaint checklist (V1 9:44 to 10:40) | J, M (partial) | M: paragraphs that each open with a different author and year; sections organised by year. J: the six complaints (listing without ranking, chronology, selection not driven by the hypothesis, theory and data never meeting, strings of summaries, a single discipline). | Chronology suits a textbook (V1 9:44). |
| O21 | Synthesize, set priorities, push past your discipline (V1 10:05 to 11:33) | J | J: "Does any paragraph's subject name a pattern or tension, rather than a single author?" | none |
| O22 | Plot versus story; casting studies as major and minor characters, allies and adversaries, or cut; the forest and the missing puzzle piece (V4 1:26 to 5:47) | W, J, M (partial) | W: the writer casts the sources. M: integral versus parenthetical citation ratio, and paragraph length per source. J: "Does the review read as a story in which your study is the missing piece?" | none |
| O23 | Mind map before matrix (V4 6:36 to 8:16) | W | Exercise. | Keep the matrix for filing (V4 7:58). |
| O24 | Two kinds of "I"; personal front matter, impersonal middle; present tense for your own findings (V4 8:45 to 13:24; V5 5:53 to 10:43) | M40, M39, J | none | Methods and results (V5 8:01). Procedures stay in the past tense *(inferred)*. |
| O25 | Simplicity over complexity; fewer function words in the introduction (V5 2:05 to 5:53) | M38, J | none | Don't simplify the ideas (V5 3:55). |
| O26 | Hedges and boosters as calibration (V3 9:31 to 11:39) | M18, J | See X8. | none |

**O-dia: dialogue and scene (V13, with V7).**

| ID | Technique | Use | How the skill uses it | Don't apply |
|---|---|---|---|---|
| O27 | No author-splaining: cut adverbs on speech verbs and labels for emotions (V13 1:21 to 7:18) | M32, J | none | Expository claims of your own should still be explicit *(inferred)*. |
| O28 | Ask why the text switches to dialogue here (V13 7:18 to 7:51) | J | none | none |
| O29 | Lines with more than one meaning (V13 7:51 to 10:52) | J | none | Not "totally vague and vapid" (V13 10:21). |
| O30 | Silent dialogue, or ellipsis, at moments of shame (V13 10:52 to 19:06) | C, J | none | "Only one writing tool" (V13 19:06). Save it for the key moment. |
| O31 | Free indirect discourse; mechanics that carry meaning (V7 8:18 to 9:51, 15:56 to 19:31) | C | none | Avoid free indirect discourse in argument, where the reader must know whose claim is whose *(inferred)*. |

**O-book: expert nonfiction books (V16, V17, V18). Mostly the Plan stage.**

| ID | Technique | Use | How the skill uses it | Don't apply |
|---|---|---|---|---|
| O32 | The book as an identity signal; rebalancing ethos, pathos and logos (V16 1:35 to 3:21, 14:23) | W, J | J: "What would a reader be saying about themselves by recommending this?" | It is not a licence to be inaccurate (V19 1:04:23). |
| O33 | The Vow: a promise, stated as a changed behaviour; say it out loud, watch the listener's face, lock it in (V16 3:21 to 7:47) | W | The pitch-to-a-stranger loop is an exercise with a real person. The skill can't replace the listener's face. | "Name the change" is for prescriptive books. For idea books, the change is swapping an old idea for a new one (V18 5:10). |
| O34 | The Victim: one reader in pain, described in their own words (V16 7:47 to 12:21) | W, J | J: "Is the pain described in category terms or in lived detail? Are there chapters written for other readers?" | Broad positioning is right for mass-market and booking-agent books (V16 8:36; V17 25:25). |
| O35 | The Villain: name a shared enemy, which should be a system, a trend or a shortcut (V16 12:21 to 15:14) | W | none | Temper it if you need peers' acceptance (V19 35:19 to 40:04). His villains are never individual people. |
| O36 | Six book types chosen by goal (V17 all) | W | W: state the definition of success, match it to a type, and adopt that type's reader, shape and stance. J: warn about mismatches, such as an ideas book sold as a practical guide (V18 35:20). | none |
| O37 | Test the method before writing the book (V17 20:01) | W | W: "Have you taught this method to people and fixed what they misunderstood?" | none |
| O38 | Chapter titles as promises (V18 2:38 to 7:12) | J, M (partial) | M: chapter titles that are bare noun phrases. J: "Does the title say what the reader will be able to do, or which idea replaces which?" The writer writes the titles. | Framed for prescriptive books (V18 5:10). |
| O39 | Purpose chain and table of contents as a bridge; filter every element (V18 9:52 to 15:26) | W, J | See B2. J: "Does this story, idea or example help *this* reader solve *this* problem?" | Fiction (V18 14:32). |
| O40 | The section test: what should the reader understand, feel or do differently afterwards? (V17 38:16) | J | none | none |
| O41 | Sharpen the axe: plan the book before drafting the book (V17 38:16) | C | Place it after the thinking phase (read_04, "Across", Developments point 8). | Not before thinking (V17 8:34). |

### 3T. Practice drills (P stage, away from a live draft)

His underlying rule: practice is not performance. Once the skills are in place, you move on to meaningful content (V10 10:46). Models should be writing that has lasted: "seeds, not twigs" (V7 13:45 to 15:56). So the model texts should come from the writer's own reading, not from the skill (§5.5).

| ID | Drill (sources) | Use | What the skill does | Limits |
|---|---|---|---|---|
| T1 | Sentence bird-watching: collect sentences, not words (V10 1:57 to 2:27) | W | Keeps the writer's list and asks what pattern each sentence uses and where its weight falls. | none |
| T2 | Great Sentences Mad Libs: keep the structure, swap words slot by slot (V10 6:56 to 10:08) | W, J | The writer picks a model from T1 and writes the variants. The skill checks that each variant keeps the slots. | Form practice, not content (V10 10:46). |
| T3 | Copy work from memory; steal style (V12 27:40 to 29:53; V14 12:35 to 13:50); type out a whole work (V7 7:00 to 7:46) | W, M45 | M45 diffs the writer's from-memory version against the original the writer supplies, and asks what they keep dropping. | Style, not ideas (V12 29:15). The writer supplies the source text, which avoids reproducing it. |
| T4 | Translation as apprenticeship, including translating between registers (V7 13:45) | W, J | J: "Did every claim survive the change of register?" | none |
| T5 | One paragraph per page (V10 0:00 to 0:44, 10:08 to 10:46) | W | The skill can split a draft onto separate pages or screens for the writer. | A method for drafting and revising, not a layout *(inferred)*. |
| T6 | The précis: summarise the argument in your own words, then argue against it (V36 13:48 to 16:10) | W, J | J: "Does your summary match the source you have in front of you?" The writer writes both parts. | none |
| T7 | The joint-attention drill: ten minutes with a partner, trading observable details (V30 2:44 to 5:36) | W | Explains the drill. Solo version: describe a picture as if to someone beside you. | "A bit of a conceit" (V30 4:46). |
| T8 | Blend: one paragraph of your real material, written inside the classic scene, read aloud (V30 13:05 to 15:41) | W, J | J: "Where does the paragraph leave the scene?" | none |
| T9 | Annotate a model text: label its sections by function (V21 15:32, 29:54; V22 19:00) | W, J | none | none |
| T10 | The anthropologist exercise, which builds the CW list (V19 16:59 to 18:46; V22 31:32; V35 17:57) | W, M (counting) | The skill counts frequencies in texts the writer supplies. | none |
| T11 | The punctuation X-ray on an admired text (V22 1:34 to 3:19) | M21 | none | none |
| T12 | A letter of response to a *published* essay (V44 18:55 to 19:31) | W, J | Rehearses the U3 format before the writer workshops their own work. | none |
| T13 | Rip a solo: 20 minutes of improvised writing (V12 44:07 to 45:38) | W | Runs the timer. | A drafting mode, not a finished product. |

### 3U. Testing with real readers and handling feedback (S6)

| ID | Technique (sources) | Use | How the skill uses it | Don't apply |
|---|---|---|---|---|
| U1 | Test with real people; watch where they struggle (V19 1:11:07 to 1:13:02) | C, W | Helps the writer plan who to ask and what to watch for. | none |
| U2 | Early readers: people you respect and want respect from, in a community of practice (V44 28:00 to 34:31) | C, W | Recommend. The skill doesn't pose as one (§5.6). | none |
| U3 | The letter of response: first say what the piece is trying to do, then what you would steal, and only then what's missing (V44 15:30 to 18:55, 21:10) | W, J | Coaches the writer to write letters to others. On request the skill writes a *cold-reading* letter on the writer's draft, clearly labelled, and stage one becomes a check: if the skill misreads the aim, the draft has a problem (V44 17:02). | The middle stages weren't recalled on camera (V44 18:13). |
| U4 | Two readings: gut reaction first, then a "body scan" a few days later that locates each effect (V44 22:00 to 24:38) | W, J | J: turns a vague verdict into a location, such as "where does the boredom start and stop?" | none |
| U5 | Same and different; the silent-author rule; the seminar format (V44 21:35 to 27:14, 3:51 to 4:35, 15:00 to 16:07) | C | Explains how to run a group. | none |
| U6 | Feedback words are symptoms (A5); readers are the "worst people" to diagnose (V47 4:44) | J | See A5. | Readers still sense *where* the problem is. |
| U7 | The pitch-to-a-stranger loop (V16 6:17) | W | An exercise with a real person. | none |
| U8 | Mine the sympathetic reviews (F6) | W, J | See F6. | none |

---

## 4. Catalogue of mechanical checks

These are the checks a script can run. What each one produces is a *location plus an observation*. The model then sorts the hits using the reader brief (the J layer) and drops the false alarms before the writer sees anything. No check edits text. All of them run only on reader drafts (stages S3 to S5). None runs on a thinking draft or a vent (C20, D14).

The thresholds are starting points to tune. He gives rough numbers himself: three to four items in working memory (V26 3:37), underline the first seven or eight words (V27 18:19), readers build momentum over nine or ten words (V27 21:35), his model sentence reaches subject and verb within five words (V27 23:26), a paragraph index is one to three sentences (V46 12:43), and the passive fits perhaps 5% of sentences (V6 11:47, V15 13:34). Treat these as signals, not quotas.

### 4.1 The checks

| ID | Flags | Heuristic | Wrongly flags (false positives) | Misses (false negatives) | Stage and gate | Source |
|---|---|---|---|---|---|---|
| M1 | Filler words | Word list: *actually, basically, certain, various, particularly, really, virtually, individual, generally, given, practically*, plus *very, quite, extremely*. Flag two or more in a sentence, or a high density per paragraph. | *certain* meaning sure; *individual* in contrast with a group; *given* as a preposition ("given the data"); *generally* as a real statement of scope; quotations and dialogue. | Throat-clearing phrases ("it is worth noting that", "in terms of"); fillers not on the list. | S5 | V29 2:36 to 5:39; V6 1:48 |
| M2 | Doublets | A fixed list (*each and every, first and foremost, full and complete, true and accurate, any and all, basic and fundamental*), plus "X and Y" pairs whose two words are near-synonyms by WordNet or embedding similarity. | Legal terms of art (*null and void* in contracts); pairs that make two distinct claims (*safe and effective*); a deliberate rhetorical doubling. | Doublets spread across phrases ("clear and easy to understand"). | S5 | V29 5:39 to 7:18 |
| M3 | Redundant modifiers and categories | A pair list (*future plans, past history, end result, free gift, basic fundamentals, consensus of opinion, totally transform*). Patterns: "X in (nature, size, shape, number)", "in a X manner", "X phase of development", "at an early time". | *past medical history* as a chart heading; *in nature* meaning the natural world. | General implications spread across several words (*trying to learn*, *the art of poetry*); these need J (X4). | S5 | V29 6:19 to 11:34 |
| M4 | A wordy phrase where one word would do | A phrase list: *the reason for* becomes why; *despite the fact that*, although; *in the event that*, if; *in a situation where*, when; *concerning the matter of*, about; *due to the fact that*, because; *at this point in time*, now. | Legal drafting conventions; an *in order to* that clarifies purpose in a long sentence. | New circumlocutions not on the list. | S5 | V29 15:21 |
| M5 | Stacked negatives | Per clause, count explicit negatives (*not, no, never, n't, nor*) and implicit ones (*prevent, lack, fail, doubt, reject, avoid, deny, refuse, exclude, prohibit, without, unless, except, against*). Flag two or more, especially alongside a passive or a nominalization. Also flag replaceable "not X" pairs (*not many* becomes few, *not allow* becomes prevent, *not include* becomes omit). | Warnings where the negative is the point ("Do not mix…") (V29 20:02); deliberate litotes (K40); "not X but Y" contrasts; quoted rules. | Negative meaning carried by verbs not on the list (*declined to*, *stopped*). | S5 | V29 16:20 to 20:02 |
| M6 | Nominalizations, weighted towards subject position | Suffixes *-tion, -sion, -ment, -ence, -ance, -ity, -al, -ure*, and gerund heads followed by "of". Nouns that are also verbs (*review, use, change, decline, increase*) when followed by "of". Weight rises when the noun is the grammatical subject, heads an "of" chain, or pairs with an empty verb (M7). | Words that aren't derived from verbs (*nation, moment, comment, government*). His four legitimate uses: a subject that links back ("That sale paid…"), a replacement for "the fact that", an object ("approved her recommendation"), and a term familiar to this reader ("deployment" for engineers) (V27 6:33 to 9:21). | Nominalizations with no suffix and not on the list; ones hidden in possessives ("Truman's conclusion", V37 17:02). | S4. Sorted by K3 | V8 4:39; V12 47:33; V27 5:34 to 11:43 |
| M7 | Empty or light verbs | Verbs *occur, take place, undertake, conduct, perform, result in, lead to*; "make, give, have or provide" plus a nominalization ("give consideration to"); "there is a need for"; "was the result of". | *conduct* in a methods section where that is the norm; *occur* for natural events; *lead to* where the causal chain is the point. | Other light-verb pairings not on the list. | S4 | V8 4:39 to 5:50; V27 4:16; V32 10:53 |
| M8 | Words before the main verb; subject length | Parse each sentence. Count tokens from the start to the root verb, and the span of the subject. Flag a subject over about 8 tokens, or more than about 12 tokens before the verb. | A long subject made of old information that links back (K5); a deliberate periodic or reveal sentence (A16); list items and headings; parser errors on questions and imperatives. | Short but abstract subjects ("Implementation occurred"); M6 and M7 catch those. | S4 | V8 0:42 to 2:27; V12 0:41; V27 21:11 to 25:12; V37 16:40 |
| M9 | A long introductory subordinate clause | The sentence begins with *because, since, although, while, when, if, after, given that* or *despite*, and the main clause starts 15 or more tokens in. | A *since* clause that marks a known cause (V32 20:19); time orientation in narrative (V39 12:45); conditions that set the scope of an instruction. | Long participial or prepositional openers ("Following a detailed review of…"). | S4 | V12 48:28 to 49:26 |
| M10 | Material wedged between a verb and its object | By parse: five or more tokens between a verb and its direct object, especially when set off by commas. | Heavy-noun-phrase shift, where a long object is legitimately moved to the right. | Interruptions between subject and verb (M8 covers these). | S4 | V12 49:26 to 51:02 |
| M11 | Identifying the passive (no fault implied) | By parse: *be* or *get* plus a past participle, with a patient as the subject. Labelled agentless or with a "by" phrase. It also reports common checker false alarms: "there were…", the past perfect, linking verb plus adjective ("became quiet"). A second label marks agentless passives on nouns of responsibility (*mistake, error, decision, breach, cut*) as candidates for the agency question (K16). | Adjectival or stative participles ("the door was closed"), which are ambiguous. | Reduced relative clauses ("the report written in May"); some *get*-passives. | S4 | V14 7:44 to 10:59; V14 5:51; V42 7:12 |
| M12 | The topic list: scatter and concreteness | Per paragraph, take each main clause's opening up to the main verb and print them as a vertical list (the writer's "underline"). Compute: overlap of head nouns between consecutive topics and with the paragraph's index; continuity once pronouns are resolved; the number of distinct topic heads; and a concreteness score for the head nouns from published concreteness norms. | The whole-to-parts pattern (distinct heads under a named umbrella, V48 13:14 to 18:16); the linking pattern, where each topic comes from the previous comment (check M13 too); unrecognised synonyms and hyponyms (K30); topic shifts marked by "for example" (V32 17:01). | Topics that are consistent but not what *this reader* cares about (V33); that needs K14. | S4 | V9 1:55; V26 5:48; V27 15:07 to 21:11; V32 3:50 to 5:46; V37 21:54; V48 3:00 |
| M13 | Handoffs between sentences | For each pair of sentences, does the opening of N+1 share a lemma, a coreferent or a near-synonym with the last 5 to 8 tokens of N, or with the paragraph's running topic? Flag an N+1 that links to neither, the case where information "comes out of nowhere" (V27 13:02). | Links through synonyms or category members that the system misses; a new topic that was explicitly previewed (the theme-preview pattern, V48 18:16); the first sentence of a paragraph. | The same word in a different sense; the smooth chain that goes nowhere (V27 15:42), which M13 passes. M12 and J have to catch that. | S4 | V8 10:03; V15 12:00; V26 4:55; V27 11:43 to 15:07; V32 8:32 |
| M14 | Weak word in the stress position | The last content word before the full stop is a pronoun, a preposition, an attribution ("according to X", "X said"), a trailing hedge, a filler ("as well", "in this regard"), or a timestamp. | Questions, dialogue, headings, short emphatic sentences where the pronoun *is* the point. | An ending made of content words that is nonetheless old information; that needs J with N. | S4 to S5 | V2 9:38 to 10:48; V14 15:24; V37 16:03 |
| M15 | Metadiscourse density | Patterns: "this (section, chapter, paper) will / examines", "in this essay I will", "the following / preceding section", "as mentioned above", "it is important to note", "the final point to be discussed", chains of *firstly, secondly*. Measured per 1,000 words and by position. | Genres that require it (theses, grant templates, long reports, navigation text); spoken scripts (V9 14:50); signals that carry content (headings with key terms, enumerators for heavy lists, V37 11:59). | Narration of the writer's own process (M26 covers it). | S4 | V9 13:32 to 16:45; V49 10:14 to 11:14 |
| M16 | "You" as subject | Sentences whose subject is *you*; runs of "you need to / you must / you should". | Instructions, manuals, how-to steps, advice columns (V18 29:43); letters; the personal language he recommends (V19 1:00:28). | Finger-wagging through "we must" or "one must". | S4 | V18 27:28 to 32:35 |
| M17 | Dummy and abstract-pronoun subjects | Sentences opening "There is / are / was / were…", "It is (adjective or noun) that / to…", "This / That is why / how / the reason / the way…". | Genuine statements of existence ("There are three exceptions"). He says dummy subjects are "not always wrong" (V18 34:19). | Other empty subjects ("The fact is…"). | S4 | V6 10:41; V18 33:25 to 34:19 |
| M18 | Stacks of hedges or absolutes | Hedges: *might, may, could, perhaps, possibly, arguably, somewhat, seems, appears, likely, at least partly, more or less, many, for some time now*. Absolutes: *every, all, always, never, only, obviously, of course, clearly, undoubtedly, outright*. Flag two or more hedges, or two or more absolutes, in a clause. Flag *obviously*, *of course* and *clearly* as possible cover for a gap in the argument (V50 31:47). Flag "every / all / many N" in subject position as a question of scope (V50 34:15). | Precisely quantified claims ("in 3 of 4 trials"); the reporting norms of a discipline (V19 1:02:55); a definitional *only*; quotations. | Overclaiming with no marker words (a bare universal); hedging done through vague scope instead of listed words. | S5 | V3 9:31 to 11:39; V18 32:35; V19 1:02:00 to 1:05:09; V50 30:18 to 35:11 |
| M19 | Balance of connectors | In the introduction, count additive connectors (sentence-initial *and, also, furthermore, moreover, in addition*) against instability words (*but, however, yet, although, by contrast, instead*). Flag an introduction with no instability word before the writer's point sentence, or a run of three or more additive connectors (V31 4:34). In the body, flag a high density of *however* and paragraphs opening "However," one after another (V34 8:51). | A problem stated with no connector ("Most managers assume X. In practice, Y."); narrative openings (V21); *but* in a non-contrastive sense. | A *however* that doesn't target the reader's actual belief (V24 8:15 to 10:27); that needs J. | S3, S5 | V28 11:00; V31 4:34 to 5:35; V34 8:51 to 9:42 |
| M20 | Em dash economy and dashes used for definitions | Count dash pairs per page. Classify what's inside each pair. A definition (it re-describes the preceding noun, or contains "i.e." or "meaning") suggests a ", which" clause instead (V34 10:44). Flag pages where most paragraphs have a dash pair. **Never report a dash as an AI tell.** | A personal essay where dashes are deliberately dense; ranges and number spans misread as dashes. | Emphasis overdone through parentheses or bold (V34 11:48); an optional count. | S5 | V34 4:36 to 11:48 |
| M21 | The punctuation X-ray | Strip letters and digits, keep punctuation and sentence breaks, and print the X-ray. Flag sentences with four or more internal marks, or that combine a semicolon, parentheses and dashes. | Lists; citations like "(Lee, 2020; Ortiz, 2021)"; decimals; legal enumerations. | Long run-ons strung with *and* and no punctuation; pair with M8. | S5, P | V22 1:34 to 3:19 |
| M22 | The index or skim view, and flags on openings | Detect headings and paragraphs. Print the first sentence of each paragraph (extending to two or three when the first is very short or ends in a colon or question) and the first paragraph of each section. Flag an index that opens with a year or date, a statistic, a quotation mark, "For example", "One day", an author-year citation, or only a transition; and an index that shares no content word with its heading or the key terms. | Sections deliberately written point-last (V50 9:37); creative nonfiction and narrative; example-first paragraphs in a narrative. | An index that names a topic but not a problem (V46 11:27); an index that reads fine but doesn't move the story on. Both need J. | S3 | V18 21:12; V27 37:51 to 43:21; V46 8:20 to 12:43; V47 19:13; V50 14:49 |
| M23 | Key-term tracking and synonym drift | Input: KT from the writer. The skill may suggest candidates from the title and introduction for the writer to confirm. Count each term, with its inflections, per section. Find near-synonyms in the same section that may be standing in for a term (*users, customers, clients, members*). In the theme-preview pattern, check that each previewed term opens its unit in exact form. Check that the title's nouns recur (V46 2:55). | Legitimate synonyms and category members in topic chains (V46 13:26; V48 13:14); variants of the same word ("autonomy", "autonomous"), which are allowed (V48 20:31). | Drift into a different concept with no word in common; terms the writer forgot to list. | S3 to S4 | V19 45:45; V22 28:01; V24 12:20 to 15:13; V46 13:26 to 15:51; V48 20:31 |
| M24 | Title checks | Flag "How to…", "N tips / ways…", and bare topic labels. Count the nouns after a colon. Check whether the title's nouns appear in the introduction. Flag a title phrase whose first appearance in the body comes after the third paragraph, a likely coined inside joke (V46 1:24). | Reference and search-optimised pieces; a venue's house title format; academic titles that require descriptors. | A clever title that opens no loop; a trigger the piece never pays off. Both need J. | S3, S5 | V6 2:43 to 5:27; V46 1:04 to 2:55 |
| M25 | Opening patterns | Check the first two or three sentences for: history or background ("Throughout history", "Over the past decades", "X has been studied since", "In today's world"); definitions ("X is defined as"); announcements ("In this essay I will", "This paper explores"); the gap model ("no study has", "understudied", "remains unexplored", "gap in the literature", "first to"); the writer's effort or conviction (see M47). | Academic genres that require a gap statement or an aims sentence; reports with a required background section; history essays where the history is the problem. | Openings that are fluent but still name a topic rather than a problem. | S3 | V19 4:05 to 4:55, 30:43; V28 1:59; V31 0:52 to 5:35, 14:34; V46 4:50 to 7:47 |
| M26 | Introduction and conclusion; the point; narrated process | Extract the introduction and conclusion and print them side by side for the writer to underline (F5). Flag conclusions that open "In summary / In conclusion / To sum up". Measure word overlap between introduction and conclusion; high overlap means restatement (V46 18:38; V50 6:33). In the body, flag narrated-process markers ("at first I thought", "I began by", "then I realized", "eventually it became clear", "after reviewing", "having considered"). | Genres that require a summary (executive summaries, abstracts); method narration in a methods section; reflective creative nonfiction, where the journey *is* the point. | A point stated in the middle of the body. The point sentence itself can't be found mechanically; the writer marks P. | S2 to S3 | V19 4:55; V24 4:18 to 7:28; V46 16:18 to 18:38; V47 2:51; V50 4:24 to 8:23 |
| M27 | Where evidence sits | The first sentence of a paragraph contains a statistic, a direct quotation, or an author-year citation as subject: "opens on evidence" (V50 24:25). The last sentence is a quotation or a number with nothing after it: "possible hit-and-run" (V50 25:19). | Epigraphs; results sections that report a finding per paragraph; endings in creative nonfiction. | Paraphrased evidence that is never interpreted. | S3 | V50 24:25 to 25:19, 29:31 |
| M28 | Runs of one-sentence paragraphs | Three or more one-sentence paragraphs in a row. | Transitions (V22 20:27); the conventions of social platforms; dialogue. | none worth noting | S3 | V22 20:27 to 21:00 |
| M29 | Undefined shorthand at first use | The first occurrence of an acronym with no expansion nearby. Capitalised named methods, effects, models or frameworks with no gloss within a sentence. A field-jargon list when the brief says the reader is a layperson. Checked against the brief's "knows up to" field, not against what the model understands (§5.6). | Acronyms this reader certainly knows; that depends on the reader. | Ordinary words used in a technical sense; whole arguments compressed into one noun phrase (V47 15:29). Both need J. | S4 | V47 12:59 to 16:21; V49 3:40 |
| M30 | Intransitive verbs of change used for caused social changes | *become, grow, emerge, arise, develop, increase, decline* with a social or organisational subject and no cause given. | Natural processes; trends whose cause really is unknown. | Other constructions that hide a cause. | S4 | V37 10:48 to 11:33 |
| M31 | An interpretation coordinated as if equal | ", so" or ", and" joining two independent clauses where the second is evaluative or causal. | High noise. Feed to J only. | none noted | S4 | V37 9:04 to 10:48 |
| M32 | Adverbs on speech verbs; labels for emotions (dialogue module only) | A speech verb with an *-ly* adverb within three words; "felt / seemed / was" plus an emotion word near a quotation. | Expository prose; necessary disambiguation in a fast exchange. | Emotion carried by nouns ("with bitterness"). | S4 (O-dia) | V13 5:54 to 7:18 |
| M33 | A shift in time with no marker (narrative module) | A paragraph whose tense or year differs from the previous one, with no time adverbial in its first sentence. Low precision. | Deliberate disorientation. | Shifts marked only by context. | S4 (O-sci, O-cnf) | V39 11:29 to 13:36 |
| M34 | Density and position of value words | The generic lexicon (opportunity: *enables, unlocks*; cost: *prevents, erodes, limits*; urgency: *critical, before*; instability: *but, however, although*) plus the writer's CW list. Highlight them, "circling" as he does. Report whether each paragraph's first sentence has one, flag long stretches with none, and check that the introduction front-loads them (V19 54:13). | Generic words that carry no value in this community; *critical* in a medical sense; narrative passages. | Community words not in CW; stakes conveyed concretely without marker words. | S3 | V19 49:20 to 54:13; V22 6:18 to 8:14, 30:25 |
| M35 | Clichés and stock images | A stock-phrase list (*game changer, move the needle, at the end of the day, low-hanging fruit*) and stock images such as *tapestry of* or *navigate the landscape of*. Each hit is presented as a question for the portal test (L10), **never** as "sounds like AI". | Quotations; irony; deliberate reuse. | Metaphors that sound fresh but show nothing (needs J). | S5 | V12 37:40; V36 6:22 to 9:58 |
| M36 | Labels applied to people | Evaluative adjectives (*passionate, brilliant, dedicated, visionary, tireless*) predicated of a person. | Quoted testimonials. | Labels applied through nouns ("a visionary"). | S4 | V39 20:04 to 21:35 |
| M37 | Value words treated as self-evidently good | *sustainable, resilient, innovative, progress, inclusive, best practice*, used as unargued praise in the opening or the thesis. | A community that genuinely shares the value. | none noted | S3 | V39 17:32 |
| M38 | Share of function words; "of" chains in the introduction | The ratio of function words to content words; noun phrases with three or more "of". | Proper names and titles. Over-collapsing into noun stacks is the opposite risk. | none noted | S4 (introductions) | V5 4:43 to 5:53 |
| M39 | Tense of your own findings (academic) | "(our / this) (study / analysis / results) (showed / demonstrated / revealed / found)" in the abstract, introduction or discussion. | Procedures; other researchers' results. | none noted | S4 (O-acad) | V5 9:53 to 10:43 |
| M40 | Personal pronouns by section (academic) | I and we per section; "it was found that" in the front matter; personal narration in the methods. | Disciplines where "we" is normal in methods. | none noted | S4 (O-acad) | V5 5:53 to 9:01 |
| M41 | Inconsistent names for one thing | Coreference clusters with different head nouns ("the vendor", "the supplier", "the partner") where the alternative label first appears after the opening third with no signal of equivalence. | Coreference errors; variation the reader has already been trained on. | none noted | S4 | V19 45:45 to 47:22; V24 14:39 |
| M42 | Density of rhetorical questions | Question marks outside dialogue and quotation, per 1,000 words, and questions sitting inside body paragraphs rather than at transitions. | FAQs; interview formats. | none noted | S3 | V22 21:41; V50 15:50 |
| M43 | Runs of citations as subjects | Two or more sentences in a row whose subject is an author with a reporting verb, and nothing afterwards that contrasts or combines them. | Integral citations for the "main characters" of a literature review (V4 3:40 to 5:47). | Piles of parenthetical citations. | S3 | V1 9:44; V19 41:02 to 42:56 |
| M44 | Attribution in the stress position | Sentences ending ", according to X", ", X said", "(as X notes)". | Journalistic quotation conventions. | none noted | S4 | V37 19:35 to 20:28 |
| M45 | Copy-work comparison (practice) | A word-level comparison of the writer's from-memory version with an original the writer supplies. Report omissions and substitutions by type: dropped connectors, dropped concrete detail, changed openings. | none | none | P | V12 29:15; V14 13:16 |
| M46 | Enumerators used as structure | Openers "First, / Second, / Third," when no preceding index names the set of items. | His own legitimate use, enumerators pointing back to an index of issues (V37 11:33), and theme-preview signposts (V48 21:39). So flag only when no index names the items. | none noted | S3 | V50 13:57 |
| M47 | Writer-centred phrases (the two-vendor test) | "after months / years of research", "I believe this may be the most important…", "this will change how you see…", "it felt like a secret", reading-time warnings, first-person effort verbs in the first paragraph. Reported alongside cues about the reader's problem. | A personal essay framed around the writer's journey. | none noted | S3 | V28 1:15 to 4:20 |
| M48 | Prepositional phrases stacked at the end of a sentence; a misplaced "including" | Three or more prepositional phrases in a row at the end of a sentence; "including" whose head is not the nearest compatible category. | Parser noise. | none noted | S4 | V32 12:05 to 13:05 |
| M49 | Headings versus their content | Content words in each heading against the section's most frequent content words. Flag headings with no overlap, which are likely cryptic (V27 34:45). Check whether the heading nouns appear in the last two sentences of the introduction (H8). | Creative headings in creative nonfiction. | none noted | S3 | V22 32:40; V27 33:44 to 35:23 |
| M50 | Note hygiene | Orphan notes with no links; notes holding several ideas (long, or with two or more claim-like sentences); literature notes that have quotations but no response. | Notes the writer is still developing. | none noted | Notes | V40 9:00 to 13:50 |
| M51 | Mechanics | Spelling, agreement, pronoun case, comma splices, dangling participles, house style (the serial comma), formatting and platform conventions. Flags only; the writer accepts or rejects each. | Deliberate rule-breaks (A3); dialogue or transcribed speech for run-ons (V2 12:33); house styles that forbid the serial comma (V2 15:33). | none noted | S5 only | V2; V24 21:04 to 22:56 |

### 4.2 How a hit reaches the writer

1. **The script runs** and produces hits.
2. **The J layer sorts them** using the brief, the genre module and the draft stage. It drops the known false positives listed above. For example, it keeps a passive that hands off to the next sentence, a nominalization that is a field term, and a negative that is a warning.
3. **Ranking is top-down** (V24 22:56): reader and value issues first, then structure, then flow, then finish. Only the top one to three issues go out (D14).
4. **Each issue is presented in five parts**:
   1. *where* it is;
   2. *what is there*, quoting a few of the writer's words;
   3. *the likely effect on this reader*, stated as a hypothesis;
   4. *a question* for the writer;
   5. optionally, *the move*, described using the writer's own words or shown on a parallel example (§5.7).

An illustration of the format (mine):

> **Paragraph 3, sentences 2 to 4.** The openings are "Budget constraints…", "Staff in two clinics…", "A new form…". Your reader, a ward manager, may not be able to tell what this paragraph is about, because each sentence starts somewhere new. Who is the paragraph really about: the clinics, the staff, or the form? If it's the staff, try opening most sentences with them. The next sentence already starts with "Nurses…", so ending this one on the nurses would hand it off.

### 4.3 Anti-checks: what the skill must not run

These are the "rules" he has spent the channel dismantling. A skill that ran them would contradict the method, and he notes they are already built into grammar checkers and AI tools (V14 7:44; V42 0:00).

| Do not | Why (sources) |
|---|---|
| Suggest varying sentence length, or set targets for average length | Length follows what the sentence carries; the "music" of prose is thematic echo (V42 0:00 to 4:27). He calls feedback built on that meme bogus (V44 30:08). |
| Flag the passive as a fault, or suggest "use active voice" | The passive is a tool for focus, flow, stress and agency (V14 3:03 to 7:04; V15 13:05 to 17:20; V24 16:49; V42 4:27 to 9:28). M11 identifies passives; it does not judge them. |
| Flag repetition, or suggest varying word choice or sentence openings | Strategic repetition creates coherence (V9 5:35; V19 43:50; V24 12:49; V26 5:48 to 6:30; V32 0:00 to 0:23). |
| Score readability grade levels, ban jargon, or aim for "fifth grade" | Language is social, and code words signal membership (V12 3:46 to 5:57; V42 9:28 to 14:20). He rejects "write at a fifth-grade level" (V47 13:39). |
| Treat "shorter is better" as a rule | V33 0:00 to 0:53. Compression means less load, not fewer words (V29 2:15). |
| Detect "AI tells" (em dashes, "delve", sentence templates) | The witch-hunt makes writers drop useful tools (V34 0:00 to 2:31). Hiding AI text is the wrong goal (V36 5:02). The debate over surface features happens at the wrong level (V45 2:13). |
| Enforce school rules: no "And" or "But" to open a sentence, no split infinitives, no final prepositions, no "hopefully" | They were grading conveniences (V31 13:10). The split-infinitive rule gets emphasis backwards (V14 13:50 to 16:03). The stress-position *reason* survives in M14 as a question, not a rule. |
| Enforce "never use I" or uniform impersonality | V4 12:15 to 14:02; V5 5:53 to 9:01. It is limited by section, not banned. |
| Check for a topic sentence or five-paragraph template | The template trap (V20 16:36 to 17:08; V31 0:52). He rejects the term "topic sentence" (V46 11:08). M22 checks the index because that is where readers look, not because a template says so. |
| Apply "omit needless words" as a standing instruction | If beginners knew which words were needless, they wouldn't need the advice (V14 0:57). Timing also matters (V23 34:19). |
| Treat word count as a measure of quality | Readers care about value, not word count (V42 3:31 to 4:27). |
| Reward "hooks" | He is against hooks that offer no value (V28 0:00). Setting up a question and paying it off is different (J12). |
| Run any of the checks on a thinking draft or a vent | V23 34:19; V41 24:03; V42 17:29. |

### 4.4 Implementation notes

- **Tooling.** A sentence splitter, a dependency parser (for subjects, root verbs, passives and objects), a coreference resolver (for M12, M13, M19 and M41), published concreteness norms (M12), embeddings or WordNet for synonyms (M2, M13, M23, M30), and word lists that each genre module can extend.
- **Exclusions.** Quotations, block quotes, code, dialogue (unless O-dia is on), headings (except for M24 and M49), references and captions.
- **Genre switches.** O-cnf turns off M22's opening flags, M25 and M26's conclusion flags. O-acad turns on M39, M40 and M43, and relaxes the hedging thresholds in M18. O-dia turns on M32. O-sci turns on M33.
- **Brief-dependent checks.** M12's concreteness and topic judgments, M23, M29 and M34 all need the brief (R, KT, CW). Without one, the skill either asks for it or labels those results provisional (§6, the Brief mode).
- **Scripts never edit text.** They produce views such as the skim view, the topic list, the X-ray and the introduction and conclusion side by side, plus flags. Views are often more useful than flags, because they let the *writer* see the pattern. That matches his own diagnostic style: underline the openings, circle the value words, read only the indexes (V27 18:19; V19 54:13; V46 12:12).

---

## 5. What his position on AI implies for the skill

### 5.1 What he actually says, in order

I checked these rows against the transcripts. The trend runs from "AI tools can't think" (2024 to 2025), through "AI can help me navigate my own notes" (April 2026), to "no AI at any stage of communicative writing" (July 2026). The permitted uses sit alongside the bans all along; he never counts them as writing.

| When | Position | Uses he permits or practises |
|---|---|---|
| V1 (Feb 2024) | Journal editors can tell glib AI text from scholarship (2:25). AI tools are "language producing machines", not thinking machines (10:40). They can't give you deep understanding of a field (8:56) or make judgments about importance. | none |
| V9 (Jan 2025) | Amateur programmers rely on AI no-code tools; writers should understand the reader's "machine" instead (1:08). | none |
| V14 (May 2025) | Bad style rules are baked into grammar checkers and AI (7:44). "AI cannot think", so it can't make these writing decisions (9:31). | none |
| V15 (May 2025) | AI writing tools create bad habits; handing writing off to AI overlooks reader psychology (0:00, 1:51). | none |
| V16 (Jul 2025) | His channel's "villain" is polished AI fluff that ignores readers (13:10 to 13:51). | none |
| V19 (Aug 2025) | Writers who use AI all start to sound the same; the human advantage is original thinking (0:23). AI advocates assume words have fixed meanings and produce patterns that perform no function for readers (18:46 to 20:33). AI research is confirmation bias (40:04). | none |
| V20 (Aug 2025) | "Pastiche AI writing" shuffles other people's ideas (4:04). AI writing ignores readers altogether (24:25). | "If you want to use AI to clean up" your own voice transcript as raw material, "you can do that" (7:40). |
| V23 (Sep 2025) | Outsourcing writing to AI pads the word count and dilutes the value (42:48). | none |
| V27 (Jan 2026) | Asking AI to clean up a draft returns text that doesn't sound like you; readers notice and lose trust (0:00). | none |
| V31 (Jan 2026) | Since AI, readers are drowning in information, so novelty alone is worth even less (18:10). | none |
| V33 (Feb 2026) | Rules give an illusion of certainty and can be automated with AI. AI agents lead writers to assume all readers are the same, and writers outsource their thinking about readers (8:08, 13:04). | none |
| V34 (Feb 2026) | The em-dash witch-hunt went too far. The dash is a symptom; the disease is a voice both confident and hollow (0:00, 12:17). | none |
| V35 (Feb 2026) | AI turns everything into "slop". Better prompts and templates make you blend in (0:00). If you know what you'll say before you write, AI can replace that writing (8:11). | none |
| V36 (Apr 2026) | AI is the sum of every voice, and blending them gives slop. Custom instructions that ban phrases treat tricking the reader as the goal (5:02). AI metaphors are formally correct but "a few degrees off" (6:22). AI would flag a deliberate rule-break as an error (11:15), because it is the "teacher's pet" (13:06). It has no stakes (18:08). Writing without AI is a different approach to writing, not a handicap (24:24). | Early GPT-2 as a "co-pilot" for surprise and divergent thinking; not something to outsource your writing to (20:15). He says newer models have lost this. |
| V38 (Apr 2026) | AI's "enthusiastic din"; style emerges from your own inquiry (10:50). | none |
| V39 (Apr 2026) | Research is now essentially free, so what you personally witnessed is the valuable part (11:11). | none |
| V40 (Apr 2026) | The key principle: AI should "work on my thinking instead of doing it" (15:54). He doesn't want it summarising articles, telling him the main ideas, or pointing out connections between notes (15:54). | Voice memo, AI clean-up, saved as a *fleeting note* (3:00). Read-only agents: a keyword index that "creates higher-order links" (18:05), hub and structure notes, a weekly review, and a Q&A that asks "have I thought about this before?" (17:36 to 21:47). AI outputs go in their own folder and are never fed back in (21:47 to 22:41). His phrase: "AI as a navigation layer over a knowledge graph that you've built yourself" (23:23). |
| V42 (May 2026) | Bad writing rules are now built into AI tools (0:00). | none |
| V44 (Jul 2026) | Setting AI writing aside, he says there are many excellent uses of AI (14:31). | Matching participants from interview transcripts. Drafting introduction emails through Gmail (12:30). Community software (14:31). A bullet list of a reader's gut-reaction voice note, for their private analysis (22:48). |
| V45 (Jul 2026) | There is something wrong with bringing AI in "at any stage" of the writing process (0:21). If you outsource any stage, you have corrupted the spirit (17:18). Workflow 1, restyling AI output, is hollow: there is no vision behind it (3:33 to 7:30). Workflow 2, handing your notes or voice memo to AI to clean up, is "just as pernicious", because style is not a coat of paint over substance (7:52 to 8:47). The result is "fluency without communication" (10:34). Style and substance are not separate levels; change one and you distort the other (11:41). AI has "only had the words that you used to index that idea", so its window onto your idea becomes a funhouse mirror (13:48 to 14:53). Better prompts won't fix it: you can never give enough context (the Laplace's demon argument), and the effort would be better spent on your reader (14:53 to 16:23). | "I use AI for all kinds of things. Just not communicative writing." Specifically, as a navigation layer in his second brain (17:18). |
| V49 (Aug 2026) | If coherence were in the text, you could automate it with AI or templates; it isn't, so you can't (7:34, 9:16). | none |
| V50 (Sep 2026) | His system keeps your meaning and voice instead of losing them to AI (0:00). | Using AI or a thesaurus to find the precise verb: "there's no excuse" not to (34:15). |

### 5.2 The argument underneath: five claims the skill has to respect

1. **Writing is a meeting of minds, and word choices follow from the relationship.** The words come from how you show up for a particular person (V45 2:37; V44 31:19 to 31:59). A tool that isn't in that relationship can't make those choices for the writer.
2. **The value is the writer's new thinking about a particular reader's problem.** If the content could have been known before writing began, AI can replace it (V35 8:11). AI output is at best the average of every voice (V36 5:02).
3. **Style and substance can't be separated.** Rewording distorts the idea, because AI sees only the words, never the thought behind them (V45 11:41, 13:48).
4. **Tools that enforce rules stop writers thinking about readers.** Writers end up assuming all readers are the same (V33 13:04; V14 9:31; V42 0:00).
5. **Judgment and stakes are human.** A text needs judgment calls (V39 3:20 to 4:58), decisions about what matters (V1 10:40), and someone whose reputation is on the line (V36 18:08).

### 5.3 The paradox, and how his own practice resolves it

The skill *is* AI. His own resolution (V40 15:54; V45 17:18) is to let AI work *on* the writer's thinking (navigating, indexing, retrieving, reminding, flagging gaps) but never *do* the thinking or the writing. There is also a second line of reasoning. The roles he plays for writers are ones a skill can play:

- the editor who won't look at a text until the reader questions are answered (V24 3:22);
- the editor whose job is to help writers name their goals and work backwards from the reader's needs, not to impose his own taste (V18 14:32 to 15:26);
- the diagnostician who uses reader locations instead of feel (V50);
- the seminar leader who is a "guide by the side", not a "sage on the stage" (V44 15:00 to 16:07).

The role he rejects is the ghostwriter or polisher (V45). So the skill is a **coach and diagnostic editor that never writes the writer's prose**.

### 5.4 What the skill must not do

| # | Must not | Source | Instead |
|---|---|---|---|
| N1 | Draft reader-facing prose from notes, bullets, outlines, transcripts or a prompt ("write me three points on X") | V45 3:33 to 8:47; V20 24:25; V23 42:48 | The Think or Brief interview; the writer drafts. |
| N2 | "Clean up", polish, restyle, or "make it sound better or more human" | V45 7:52 to 8:47, 11:41; V27 0:00; V36 5:02 | Locate, name the effect, ask (§5.7). |
| N3 | Rewrite the writer's sentences or paragraphs, even as "suggestions" | V45 13:26 to 14:53 (the funhouse mirror); V36 11:15 | Describe moves using the writer's own words; demonstrate on parallel examples. |
| N4 | Supply the writer's substance: claims, theses, points, examples, stories, anecdotes, metaphors, analogies, intuition pumps, evidence, answers to objections, titles, chapter titles, openings | V1 10:40; V35 8:11; V36 6:22; V38 6:40 to 9:31; V40 15:54 | Ask for them. Name what *kind* is missing: "a case this reader would recognise", "evidence of type X". |
| N5 | Do the research, or tell the writer what sources say or what their main ideas are | V19 40:04; V36 16:25; V40 15:54 | Help the writer read with a question. Check the writer's own summary against a source they supply (T6). |
| N6 | Scrub "AI tells" or help disguise text as human-written | V34; V36 5:02; V45 2:13 | Talk about the reader and the vision instead. |
| N7 | Enforce universal rules, or run the anti-checks in §4.3 | V33 13:04; V42 0:00 | Name the tool, its conditions, and its effect on this reader. |
| N8 | Critique, compress or restructure a thinking draft or a vent, unless the writer explicitly switches mode | V23 34:19; V38 18:28; V41 24:03; V42 17:29 | Think mode: the question, timers, prompts. |
| N9 | Pose as the target reader or as the writer's early readers, or pronounce a passage "clear" in absolute terms | V19 1:11:07; V44 28:53; V49 9:16 | Give provisional judgments tied to the brief, and send the writer to real readers (Readers mode). |
| N10 | Feed its own output back as the writer's thinking, for example by saving its summaries into their notes or treating its paraphrase of their point as *the* point | V40 21:47 to 22:41 | Keep skill output separate and labelled. The writer restates things in their own words. |
| N11 | Accept "just give you more context" as a way around N1 | V45 14:53 to 16:23 | Turn the writer's description of their reader into their own first paragraph addressed to that reader. |

### 5.5 What the skill may do

| # | May | Condition | Source |
|---|---|---|---|
| Y1 | Ask questions: the whole interview layer (B, C9 to C12, G1 to G4, H3, K14, I19) | none | V24 3:22; V20 22:49 to 24:25; V45 16:23 (turn to the reader) |
| Y2 | Locate and diagnose using reader locations and mechanical checks | Effects stated as hypotheses; top-down; capped | V49 3:40; V50 4:24; V24 22:56 |
| Y3 | Explain a concept and demonstrate it on an invented parallel example | The example is not built from the writer's own sentences | His own practice of demonstrating on model passages (V37 5:39 to 22:52; V50 17:24 to 28:54); committing the fault, then fixing it (V9 13:32) |
| Y4 | Navigate the writer's own material, read-only: index, "have I thought about this before?", resurfacing forgotten notes, flagging gaps and unfollowed links, a weekly review | Output kept apart and never fed back into the writer's notes | V40 15:54 to 23:23; V45 17:18 |
| Y5 | Pull out and lay out the writer's *own* sentences for inspection: skim view, topic list, introduction and conclusion side by side, X-ray, a reverse-outline scaffold | Extraction, not generation | V22 1:34; V27 18:19; V46 12:12 |
| Y6 | Logistics: timers, empty templates, reader scheduling, feedback-session agendas | none | V44 12:30 to 14:31 |
| Y7 | Private aids clearly marked as the skill's: a verbatim transcript of the writer's voice memo; a bullet list of their gut-reaction note | For the writer's own use only; never a draft; offered on request, not by default (gray zone GZ1) | V20 7:40; V40 3:00; V44 22:48 |
| Y8 | Offer a short list of candidate words for a slot the writer has identified, as a thesaurus would | At S5 only; the writer chooses; no sentence is rewritten | V50 34:15 |
| Y9 | Mechanics flags | At S5, last | V24 21:58 |
| Y10 | Divergent provocations in S1, on request | Given as questions, or as odd pairings of the writer's own notes; never copyable prose | V36 20:15; V7 0:00; V35 7:25 |
| Y11 | A "cold-reading" letter of response, on request | Labelled as not a real reader. Stage one ("what I think this is trying to do") works as a test. | V44 15:30 to 18:13; V50 2:54 |

### 5.6 Being honest about the skill's own reading

- **It is a cold reader of the writer's intentions.** It has only the words (V45 13:48). That is why it can't write for them, and also why it can spot gaps the writer skates over, just as the cold readers in the Carnegie Mellon study caught more structural errors than briefed ones (V50 2:54). The skill should use this deliberately. When it can't reconstruct why sentence B follows sentence A (I12), or what a section's point is (F1, I3), that failure is the finding.
- **But it is "briefed" on many subjects.** Like the briefed readers in the same study, it will fill technical gaps from its own knowledge that the real reader can't fill (V50 3:43 to 4:24; V47 12:59 to 16:21). So the compression checks (B15, M29) test against the brief's "knows up to" field, not against the model's own comprehension.
- **It is not the reader.** Coherence is relational (V49 9:16), and value is in the eye of the reader (V35 16:49). Every judgment that depends on the reader is provisional and ends with the advice to check it with a real reader (V19 1:11:07; V44 28:53).
- **It has nothing at stake** (V36 18:08). Its praise is worth little. It should not offer approval in place of readers the writer respects (V44 31:59).

### 5.7 Output rules that follow

**1. The ladder of help.** Stop at the lowest rung that works.
   1. *Locate.* Point to the paragraph or sentence and quote a few of the writer's words.
   2. *Name the effect* on this reader, as a hypothesis.
   3. *Ask* the question that brings out what the writer intended.
   4. *Describe the move* in the writer's own words. For example: "Your next sentence opens with 'the committee'; try ending this one on 'the committee'." Or: "The action is in 'implementation'; who implemented what?"
   5. *Demonstrate* on a parallel invented sentence on a different subject.
   - *Never* the sixth rung: writing the finished sentence for them.

**2. No rules, only effects and choices** (A1, A2).

**3. Top-down, and at most three issues per pass** (V24 22:56; V12 51:02).

**4. Mark provenance.** Anything the skill produces (retrieved lists, cold readings, transcripts) is labelled as the skill's and kept out of the writer's draft and notes (V40 21:47).

**5. Don't moralise.** He explicitly refuses to deliver a "cranky rant" about AI (V45 0:21). When the skill declines to ghostwrite, it says so once, briefly, in terms of the writer's goal, and offers a path forward.

An illustration (mine):

> **Writer:** Here are my notes. Turn them into a newsletter post.
>
> **Skill:** I won't draft it from the notes. Anything I produce would be fluent, but it wouldn't be your thinking, and your readers come for your thinking. Here's a faster route. Two questions first: who opens this newsletter, and what do they believe about this topic right now? Then, which line in these notes surprised you? Tell me that line as if you were saying it to one of those readers over coffee, and we'll build the post from your words.

### 5.8 Gray zones and how to decide them

| # | Case | Evidence on each side | Rule for the skill |
|---|---|---|---|
| GZ1 | Tidying or bulleting a voice memo | Permitted: V20 7:40 (as raw material), V40 3:00 (into a fleeting note), V44 22:48 (a private bullet list). Condemned: V45 7:52 to 8:47 (memo, then AI clean-up, then sent to readers), and V45 17:18 (any stage). | Only for private material that stays in the thinking layer. Verbatim transcription is preferred. Never used as a draft, and always labelled. The latest statement (V45) is the strictest, so the skill doesn't offer this by default. |
| GZ2 | Finding a word | V50 34:15 allows AI or a thesaurus to find a precise verb. | A short list of candidates for a slot the writer has named. No rewriting of the sentence around it. |
| GZ3 | Proposing reverse-outline labels, key terms, or "this paragraph's point" | V40 15:54 bars AI telling him the main ideas of *sources*. As an editor, he himself identifies the points in a client's draft (V50 4:24 to 15:06; V24 4:18 to 7:28). | The writer labels first. The skill proposes only on request, as a cold reader's hypothesis, and reports any mismatch as a finding (F1). |
| GZ4 | Showing a fix on the writer's own sentence | His live rewrites use model passages, not clients' text (V37; V50). V45 argues that rewording distorts. | Describe the move with the writer's words and demonstrate on a parallel sentence. A designer who allows more should know that this drifts towards the V45 "coat of paint" workflow. |
| GZ5 | Messages to real people: introductions, pitches, cover emails | He had AI draft introduction emails (V44 12:30), but V45, three days later, condemns AI in any communicative writing. | Follow V45. A message to a person is communicative writing. |
| GZ6 | Summarising sources | V40 15:54 (no AI summaries of articles in his notes); V36 16:25 (the worry that AI explanations remove the struggle). | The skill doesn't summarise sources for the writer. It can check the writer's own summary against a source they supply (T6). |
| GZ7 | Titles and headlines | They are reader-facing text (N4). | Explain the triggers, ask for four variants, and judge which trigger each uses and whether the piece pays it off (H10). |
| GZ8 | Divergent "surprise me" help | V36 20:15 values surprise for divergent thinking, and says current models have lost it. | Offer questions or odd pairings of the writer's own notes, never text (Y10). |

### 5.9 Consequences for how the skill describes itself

The skill's description should set expectations before the first request. A suggested line: *"A writing coach and diagnostic editor built on the Writer Science method. It helps you find your point, understand your reader, and see where your draft loses them. It doesn't write or rewrite your prose."*

The skill's own explanations to the writer are not the writer's communicative writing, so the skill may write them. But they should follow his principles: point first, concrete examples, one idea at a time, and a partner's voice rather than a preacher's (V18 35:20).

---

## 6. Proposed skill modes

### 6.1 Routing: the first 30 seconds

He asks about the reader and the purpose before anything else (V24 3:22), and he separates writing to think from writing to be read (V38 18:28; V47 0:00). So routing turns on two questions:

1. **Is there a draft, and whose is it for?** "Is this for you, to work out what you think, or for readers?"
2. **Who is the reader, and what should the text do?** Skip this question if a brief already exists.

| Situation | Mode |
|---|---|
| No draft, and the writer doesn't yet know what they think | **Think** |
| No draft, but a clear topic and reader | **Brief**, then Think, or straight to writing their reader draft |
| A book or large project idea | **Plan** |
| "I can't start", "I have 50 unfinished drafts", "my voice is flat" | **Unstick** |
| A thinking draft, and the writer has had the "click" (they can state what they now think) | **Bridge** |
| A thinking draft, no click yet | **Think**. No critique (N8). |
| A reader draft, no brief | **Brief** (short), then Architect |
| A reader draft with a brief | **Architect**, then **Flow**, then **Finish**. Stop at the highest unresolved level (V24 22:56; V50 35:11). |
| Feedback in hand ("my editor said it's dense") | **Readers**, then back into Architect or Flow |
| Wants to practise | **Gym** |
| Has a notes vault and asks "have I written about this?" | **Notes** |

**Design choice about the brief gate.** He won't read without a brief (V24 3:22). A skill that refuses outright may lose writers who just paste a draft. A compromise: ask the core brief questions in one short turn (B1 plus "what should change in their mind"). If the writer declines, infer a provisional reader from the draft, *state it*, and mark every reader-dependent judgment "provisional".

### 6.2 The modes

**1. Brief (the reader brief)**
- *Purpose:* fix who the text is for and what it must do, before any judgment.
- *Triggers:* the start of any review of a reader draft; "who should this be for?"; a genre the writer hasn't worked in before.
- *Does:*
  - asks the goal and what the text should make happen (B18, B2);
  - asks the four reader questions (B1), and what the reader believes now, where their knowledge stops, and what must change (B3);
  - asks the reader type (B4);
  - for high-stakes genres, runs the planning wheel (B5) and "what must they also believe?" (B6);
  - asks the problem statement (B7), practical or conceptual (B9), fact or judgment (B11), and whether there are several audiences (B16);
  - assigns the code-word hunt (B14, T10).
- *Mechanical:* none, apart from counting word frequencies in texts the writer supplies (B14).
- *Never:* invent the reader silently; fill in the brief's content for the writer.
- *Output:* a one-screen brief in the writer's own words. It is stored and fed to every later mode as R, G, Gen, KT and CW.
- *Exit:* to Think (if the writer doesn't yet know their point), Bridge (if there's a thinking draft) or Architect (if there's a reader draft).

**2. Think (a companion for the writer's own draft)**
- *Purpose:* help the writer find out what they think. The reader is kept out of the room.
- *Triggers:* "I don't know what I think yet"; a topic but no question; the writer says they're exploring.
- *Does:*
  - sets up the question tether (C3), the "I don't know" ritual (C10), and a timer with placeholders (C2, T13);
  - offers the private prompts (C7, C18), the words-and-ideas alternation (C5), and five whys (C13);
  - lays out evidence and reasoning in separate columns (C12);
  - checks that reading is filling a specific gap (C15), and flags research used as avoidance (C23);
  - offers the play framing (C17);
  - on request, retrieves the writer's own notes, including random or juxtaposed ones (C16, C25, Y4);
  - supports the goal-less vent (C4): timer only, no reading.
- *Mechanical:* none (C20).
- *Never:* judge quality, correct, compress or suggest structure (N8); bring in the reader (V42 17:29); supply ideas, claims or metaphors (N4); summarise sources (N5).
- *Exit signal:* the writer can state what they now think in one or two sentences (the "click", V31 20:02; V47 12:03), which leads to Bridge. If they stall, go to Unstick.

**3. Unstick (block and process coach)**
- *Purpose:* get the writer writing again without "discipline" theatre.
- *Triggers:* stuck, avoiding the work, perfectionism, a pile of unfinished drafts, a flat voice, fear of publishing.
- *Does:*
  - separates finishers from voice-seekers (D11);
  - names the block as fear, and uses fear as a metal detector (D1, C18);
  - checks for virtuous procrastination and the perfectionism loop (D7);
  - asks whether this project belongs to a past self (D8);
  - reframes the expert's curse (C26);
  - offers the mid-session freewrite (D4), and the reread-then-outline routine when faith is lost (D5);
  - asks whether this is a creative, uniquely-yours project (which calls for the V41 approach) or routine writing (where the V23 habits still help) (D2);
  - suggests early readers and stakes (D12, D13, L12);
  - gives one practice to try for a week (D14).
- *Mechanical:* none.
- *Never:* psychoanalyse (D9 is an optional lens only); prescribe a willpower regime for creative block (V41 21:17); moralise.
- *Exit:* to Think, or to Readers when the missing ingredient is a reader.

**4. Bridge (find the point; reverse outline)**
- *Purpose:* turn a thinking draft into the materials for a reader draft.
- *Triggers:* a finished thinking draft; "I know what I think now"; "my draft is a mess".
- *Does:*
  - the writer labels each section, and the skill checks the labels for repeats, orphans, order of discovery, and where the claim first appears (F1, F2);
  - puts the introduction and conclusion side by side for the writer to compare (F5);
  - tests the point: is it significant, non-obvious and debatable, and does "point *because* reason" hold (G1, G2)?
  - classifies the problem as practical or conceptual (B9);
  - asks for the theme and its two or three points (I10);
  - lists the writer patterns that will interfere with readers (F3);
  - has the writer list the reader's questions in the order they would arise (I4);
  - runs the reader-belief frame (G11).
- *Mechanical:* M26 (the introduction and conclusion view, and narrated-process markers). M22 as a skim view, run on the thinking draft only to *show* its shape, not to grade it.
- *Never:* write or synthesise the point sentence for the writer; merge the thinking draft into a reader draft (F4).
- *Output:* the writer's point sentence, their ordered list of reader questions, and a map of which pieces of the thinking draft answer which question.
- *Exit:* to Architect, with the writer drafting in a new document (F4).

**5. Architect (review of the bones)**
- *Purpose:* check that value, point, structure and argument hold for this reader.
- *Triggers:* a reader draft with a brief. The default for "review my draft".
- *Order* (priority from H12 and V24 22:56):
  1. The introduction: the problem-first moves, the two-vendor test, "so what?", the solution preview, the prelude (H1 to H7).
  2. Where the point sits: first or last (H9).
  3. Section order by reader question, the indexes, and the skim test (I1 to I4).
  4. Key terms and the signals of coherence (I7 to I9).
  5. Point anatomy and the uneven U (G2, I15, I16).
  6. Objections, the judgment call, and research used to build the problem (G4, G5, G9).
  7. The conclusion (H11).
  8. The title (H10).
  9. A value audit: the value of each paragraph, sentence functions, "so what?" (A8, B8, I20).
- *Mechanical:* M19, M22, M23, M24, M25, M26, M27, M28, M34, M37, M42, M43, M46, M47 and M49, all sorted through J.
- *Never:* rewrite the introduction, write titles, add evidence or examples (N3, N4).
- *Output:* the top one to three issues, in the §4.2 format, plus the skim view and the introduction/conclusion view as artefacts the writer can look at.
- *Exit:* to Flow once the bones hold.

**6. Flow (paragraphs and sentences)**
- *Purpose:* make each paragraph cohere and each sentence easy to process.
- *Triggers:* the bones hold; the writer asks about sentences; feedback says "choppy" or "hard to follow" at a local level.
- *Does:*
  - *Paragraph level:* the topic list and the movie poster (K11 to K13), the topic-progression pattern and its failure mode (K18), handoffs (K8 to K10), metadiscourse (K32), and signalling the zoom into an example (K31).
  - *Sentence level:* characters and actions (K1 to K4), the tunnel (K5 to K7), passive identification and choice (K15, K16), the stress position (K17), the reader-question test (K14), "you" and dummy subjects (L3, K33), caused change (K22), subordination (K21, K23), and conflicts between principles (K26).
- *Mechanical:* M6 to M17, M29 to M31, M36, M38, M41, M44 and M48, sorted through J (K3 triage for M6; K16 for M11).
- *Never:* rewrite sentences (N3); run the anti-checks (§4.3).
- *Output:* for each paragraph, the topic list as a visual, plus at most three sentence-level issues, each described as a move in the writer's words or shown on a parallel example.
- *Exit:* to Finish.

**7. Finish (compress, calibrate, emphasis, mechanics)**
- *Purpose:* take out wasted effort and set the strength of claims.
- *Triggers:* a near-final draft; "tighten this"; "does this sound too hedged or too arrogant?"
- *Does:*
  - compression (X1 to X6), McCarthy's question and the X-ray (X7);
  - calibration of certainty in the verb and the subject noun, against genre norms (X8, G7);
  - dashes and emphasis economy (X9, X10), clichés (L9), and the portal test for images (L10);
  - mechanics last (X12), including the V2 grammar points (K39 to K41).
- *Mechanical:* M1 to M5, M18, M20, M21, M35, M51, and M14 again.
- *Allowed extras:* word candidates for a slot the writer names (Y8), and mechanics flags (Y9).
- *Never:* flag a deliberate rule-break (A3); remove qualifiers that change the claim; flag dashes as AI.
- *Exit:* to Readers.

**8. Readers (testing and feedback)**
- *Purpose:* get the text in front of real readers and turn their reactions into diagnoses.
- *Triggers:* "is it ready?"; feedback in hand; "I don't have anyone to read it".
- *Does:*
  - helps the writer pick early readers and a community of practice (U2, D12), and plan curiosity conversations (B17);
  - explains how to run a letter of response, two readings, same-and-different, and the silent-author rule (U3 to U5);
  - runs the pitch-to-a-stranger loop (U7) and mines sympathetic reviews (F6);
  - translates feedback words into located, testable causes (A5, U6);
  - on request, writes a labelled cold-reading letter of response (Y11).
- *Never:* pretend to be the target reader or stand in for early readers (N9).
- *Exit:* back to Architect or Flow, with located friction.

**9. Gym (practice)**
- *Purpose:* build skill away from a live draft (V10 6:56 to 10:46).
- *Does:* the T1 to T13 drills. Model texts come from the writer's own reading: seeds, not twigs (V7 14:36). The skill checks form in Mad Libs variants (T2), compares copy work against the original (M45), checks a précis against its source (T6), and prints the X-ray of an admired text (T11).
- *Never:* supply its own model prose as the thing to imitate. That would train the writer on "the sum total of every voice" (V36 5:02).

**10. Plan (book and project positioning)**
- *Purpose:* set up a book or large project before drafting the book.
- *Does:*
  - the purpose chain and the table of contents as a bridge (B2, O39);
  - the six book types (O36);
  - the 3Vs: Vow, Victim, Villain (O33 to O35);
  - the identity-signal question (O32);
  - testing the method before writing about it (O37);
  - chapter titles as promises (O38), with the writer writing them and the skill checking that promise and content match;
  - a table of ideas for each chapter (I14);
  - the section test (O40);
  - thinking first, then sharpening the axe (O41).
- *Never:* write the pitch, the vow or the titles (N4).

**11. Notes (a navigator over the writer's own notes; optional, and only with access to the vault)**
- *Purpose:* help the writer's own thinking compound over time, as a windmill rather than a filing cabinet (E1).
- *Does:* read-only indexing, hub maps, flags on gaps and unfollowed links, a weekly review against the writer's goals, "have I thought about this before?", and resurfacing random notes (E8, C25). It also runs note-hygiene checks (M50) and asks the same/different question on literature notes (E5).
- *Never:* write, edit or delete the writer's notes; summarise sources; feed its own outputs back into the notes it indexes (V40 17:36, 21:47 to 22:41).

**Genre overlays.** These are switched on by the brief. They change the defaults in Architect and Flow.

| Overlay | Turns off | Turns on |
|---|---|---|
| O-cnf (V21) | Point first; the M25 and M26 flags | Opening image as seed; the web of signification; research inside the story; plant and call back |
| O-sci (V39) | none | A driving question; foreground and background; teaching inside the scene; time markers (M33); characters, not labels |
| O-imp (V43) | none | The dream test; the impersonal turn; the six arrows, once the writer knows their position |
| O-acad (V1, V3, V4, V5) | none | The peer-review checklist; casting; M39, M40, M43; hedging thresholds relaxed |
| O-dia (V13) | none | M32; ellipsis |
| O-book (V16 to V18) | none | Plan mode |

---

## 7. Tensions in his teaching, turned into operating rules

| # | Tension | Rule for the skill |
|---|---|---|
| 1 | Characters as subjects and actions as verbs (V6; V12; V27) versus the passive as a main tool (V9; V14; V15; V32; V42) | Never flag the passive as a fault. Identify it (M11), then ask about its link, focus and agency (K16). When a human subject would break old-before-new, set out both versions (K26; V37 13:39). |
| 2 | Be bold and take a stand (V16 2:43; V17 12:13, 35:19) versus concede and qualify (V18 32:35; V19 38:19 to 40:04) | Boldness belongs to the stance and positioning. Courtesy belongs to how you enter the conversation. The strength of each claim is calibrated to the community and backed by evidence (V19 1:02:55 to 1:05:09). Arrogance is a question of persona (V18 26:30). |
| 3 | Personal pronouns are good (V4; V5; V19 1:00:28) versus taking "you" out of the subject (V18 27:28) | A human presence is good. Habitually making the reader the grammatical actor in sentences about ideas reads as lecturing. Watch "I" standing in for reasons (V3 0:51). |
| 4 | "Templates are for dummies" (V20 24:25) versus his own fixed sequences (V27; V28; V43; V46; V50) | Present his sequences as reader *functions* and *locations* (V19 51:23). Check that each function is present, not that particular wording is used (V27 29:04; V28 13:36). |
| 5 | Rewrite in a completely new document (V19 28:15; V47 17:30) versus salvaging the points (V50 15:06) | V50's extract-and-relocate *is* how the new document gets written. Never line-edit the thinking draft into the final. |
| 6 | Separate writing from revision (V11; V19) versus "separating them is completely backwards" (V23 36:18) | Separate by *orientation*, not by time. Rereading and restructuring while drafting is fine. Serving the reader waits until the reader draft. |
| 7 | Point first (V24; V47; V50) versus a thesis at the end (V21) | The default is the end of the introduction. Point last is allowed with the key terms previewed (V50 10:01 to 11:36). Creative nonfiction may open on an image. |
| 8 | McCarthy's "do you need that?" (V22 2:24) versus "writing anorexia" (V23 34:19) | A matter of timing: cut when you have plenty of material, at S3 for sections and S5 for words. |
| 9 | Early readers matter (V44) versus readers being the "worst people" to diagnose a draft (V47 4:44) | Readers are sensors, not diagnosticians. Use the letter-of-response protocol to make their reactions usable. Locate what they report, then diagnose it. |
| 10 | Close synonyms are fine for key terms (V46 13:26) versus no synonyms for previewed terms (V48 20:31) | Synonyms can continue a topic chain. They must not rename a previewed or central key term. |
| 11 | Persuasion (V22 22:52; V20 21:38) versus understanding (V25 2:24 to 3:18) | For essays, default to understanding, with action second. White papers, grants and pitches are persuasive genres, so set this by genre in the brief. |
| 12 | AI tidying of transcripts allowed (V20 7:40; V40 3:00; V44 22:48) versus forbidden (V45 7:52, 17:18) | Gray zone GZ1: private only, labelled, never a draft, not offered by default. |
| 13 | Discipline and habits (V23) versus "give up discipline" (V41) | Ask whether this is a creative project that is uniquely the writer's (V41) or routine writing (V41 13:46, where habits still suit). Both reject willpower theatre. |
| 14 | Hooks and expectations (V26 11:54) versus "against hooks" (V28 0:00) | Keep setup and payoff. Cut openers that carry no value. |
| 15 | "Writing is thinking" (V38 21:34) versus doubts about thinking in language (V40 5:53 to 12:17; V42 16:02) | Writing is the best tool for making thinking visible. Incubation and sleep count too (V41 16:41). Practice is unchanged. |
| 16 | Signposts are boring (V9; V26 0:38) versus headings, point sentences and enumerators (V27 33:44; V37 11:59) | Signals that carry content are fine. Empty metadiscourse is a symptom (V49 11:14). |
| 17 | Emergent structure (V42 19:27) versus the six-arrow template (V43) | Use the six arrows once the writer knows their position, or as a revision check. Never as a starting outline for thinking. |
| 18 | Grammar doesn't matter (V10; V31 10:11) versus close grammatical diagnosis (V6; V8; V14; V37) versus em dashes changing clarity (V34) | Grammar is a diagnostic tool for reader effects, not a goal. Correctness is checked last. Suggest punctuation only when it changes emphasis or shows structure. |

---

## 8. Gaps and cautions for whoever builds the skill

**Material the captions don't contain.** Some things he showed on screen but never read aloud:
- the pen passage rewritten in V15;
- the middle stages of the letter of response (V44 18:13);
- the "visual guide to expert writing" (V46 2:55);
- the Mad Libs sheet of ten model sentences (V10);
- the Lacan diagram (V41);
- the German proverb (V15);
- the "four principles" promised in V14.

The skill should not invent these.

**Attributions to check before the skill repeats them.**
- "Curse of knowledge" credited to C.S. Lewis (V47 13:39). It is usually traced to Camerer, Loewenstein and Weber, and popularised by Pinker.
- Martha Nussbaum described as a psychoanalyst (V36 21:37).
- The Bezos memo as "five pages" (V36 17:19). It is usually six.
- Unnamed studies: the corpus of 30,000 articles (V5 0:55); spatial navigation while reading (V42 19:27); the Carnegie Mellon experiment (V50 2:00).

**Frameworks he uses without crediting.** The reports identify these:
- Joseph M. Williams's *Style*: characters and actions; nominalizations; topic strings; issue and discussion; the Romanov and Truman passages.
- Gopen and Swan: topic and stress positions.
- Daneš: thematic progression.
- Thomas and Turner: classic style and joint attention.
- Toulmin: claim, evidence, warrant.
- Swales: the gap move.
- Loewenstein: the curiosity triggers.
- Lakoff and Johnson.
- Haidt: elephant and rider.

The skill should use his terms. Where it credits a source, it should say that the idea "matches" that source, not that "he cites" it.

**His numbers are heuristics.** Treat them as tunable thresholds, not rules: 5% passive; seven or eight words; nine or ten words; three or four items; a one-to-three-sentence index; 90% dross (V41 31:10); two pages a day (V23 10:07).

**Corrections to writer-science-system.md that matter for the skill.**
- The six arrows being "for the Architect phase only" is an inference, not something V43 states.
- Part 10 of the summary allows "transcribing or bulleting a private voice note". That comes from V40 and V44. V45 then says no AI at any stage of communicative writing, which is why §5.8 GZ1 calls it a gray zone.
- Part 10 omits two permitted uses: word-finding (V50 34:15) and the divergent co-pilot (V36 20:15).
- "Heavy signposting as a symptom of private structure" comes from V49, not V9 (read_02).
- V23 rejects separating writing from revision *in time*, which qualifies axiom 4 (read_05).

**Things no mechanical check can reach.** The core of the method is judgment:
- whether the problem is one this reader cares about;
- whether the point is debatable;
- whether evidence is the kind this reader trusts;
- whether a metaphor passes the portal test;
- whether the writer has a vision at all (V45 5:09 to 6:14).

This is where the model's questions matter most. It is also where the skill must be most careful not to answer for the writer.

