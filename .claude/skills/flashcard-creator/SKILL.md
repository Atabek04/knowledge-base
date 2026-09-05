---
name: flashcard-creator
description: >-
  Generate and maintain Anki flashcards from atomic notes in this Obsidian vault,
  and create English vocabulary cards when the user asks what a word or phrase means.
  Use this whenever the user creates or finishes an atomic note (cards must stay in
  sync with notes), says "make flashcards", "create cards", "add a card", "test me on
  this note", adds a new linked note to a MOC chapter that already has a flashcard file,
  or sends a sentence and asks what a word means. Also use when editing or fixing
  existing cards, choosing a deck path, or wiring up the Obsidian→Anki sync. Trigger
  even when the user doesn't say the word "flashcard" but is clearly building review
  material from notes.
---

# Flashcard Creator

This skill turns atomic notes into Anki cards via the `Obsidian_to_Anki` plugin. Cards
live as `START...END` blocks in `05-Flashcards/{topic}/{subtopic}.md`; the plugin syncs
them into Anki on a button press.

The whole point of a card is **effortful retrieval** — a card only helps if recalling
its answer forces real cognitive work. Most quality problems trace back to violating
that. Keep it front of mind.

## When this fires

1. **An atomic note was just created/finished** → making cards for it is mandatory, not
   optional. Don't wait to be asked. See "Note → card workflow" below.
2. **A new `[[]]` linked note is added to a MOC chapter that already has a flashcard
   file** → immediately add cards for it to that file. Notes and cards stay in lockstep.
3. **User says "make/create/add cards", "test me on this", "turn this into flashcards".**
4. **User sends a sentence and asks what a word/phrase means** → this is a vocab card.
   Read `references/vocab.md` and follow it.
5. **Editing, fixing, or re-decking existing cards.**

## Note → card workflow (the mandatory path)

After an atomic note exists and is mapped to a MOC, create its cards in the same pass:

1. Identify which MOC section the note belongs to.
2. Look in `05-Flashcards/` for a matching deck file (e.g. a Variables & Types note →
   `java/variables-types.md`).
3. **If a compatible file exists** → append cards to it.
4. **If no compatible file exists** → ask the user first:
   *"No flashcard file found for `{MOC section}`. Should I create
   `05-Flashcards/{topic}/{subtopic}.md` with deck `Tech-KB::{Category}::{Topic}`?"*
5. Never silently skip card creation.

## What becomes a card, and what never does

**Only existing atomic notes become cards.** Cards exist to review note content, so every
card must trace back to a real `[[]]` linked note. Never generate cards from general
knowledge, from your own training, or from bare MOC bullets that have no note behind them.
No note → no card.

**Within a note, don't skip the substance.** Every key concept, definition, formula,
command, or code snippet in the note should become a card. Atomic notes are small; cover
them fully.

## Writing the cards

Match the syntax exactly — the plugin is strict about block structure. The full spec
(note types, the deck hierarchy, file headers, one-liner vs multi-line blocks) lives in
`references/syntax.md`. **Read it before writing any card** so deck paths and field names
are right.

Two rules carry most of the answer quality:

**Use the term in its own answer.** When defining a concept, put the word itself (or its
verb/adjective form) in the answer — it builds the term↔meaning association instead of
forcing a guess.
- ✓ "**Classifying** input into a discrete category" — not "a technique that predicts categories"
- ✓ "**Normalizing** features to a fixed [0, 1] range"

**Structure the answer to be scannable.** Never a wall of text on one line. Use line
breaks between distinct ideas, bullet lists for steps/comparisons, bold for key terms.

**Write for a confused reader — clarity over brevity, but never bloat.** A card answer is a
micro-lesson, not a label. Apply the same teaching standard as an atomic note:
- **Hierarchy carries the meaning — use nesting, not run-on lines.** The reader scans the
  shape before the words, so let indentation do the teaching:
    - **Same-level bullet** = a *separate, parallel* point (another reason, another item).
    - **Sub-bullet** = it *explains or elaborates the bullet above it* (a cause's consequence,
      an example, a gloss). When one idea explains another, demote it a level.
    - **Max 3 levels deep.** Beyond that the card is trying to teach too much — split it.
- **But don't over-fragment.** Very short bullet + a single sub-bullet under it is often
  better as **one line**. Only break out a sub-level when the child is a genuinely distinct
  idea worth its own line; if it fits in a clause, keep it inline. Judge by reading length:
  a 3-line answer that *could* be 1 line wastes the reader's eye as much as a wall of text.
    - ✗ chain on one line: `Caused by large gradients → weight changes too big → overshoot`
    - ✓ split when each step is its own idea: `**large gradients**` / sub: `→ weight too big → overshoot`
    - ✓ keep inline when trivial: `seeded from the system clock → a different split each run`
- **Disambiguate look-alike terms explicitly.** When two concepts are easily confused
  (converge vs diverge, normalize vs standardize), contrast them as parallel bullets and add
  a one-line "Key:" that states the *distinguishing axis*, not just the two definitions.
- **Order logically:** definition → cause → mechanism → consequence/edge case. The reader
  should follow top-to-bottom without back-references.

**Expand every abbreviation on first use (strict).** The first time an acronym appears, write
it out and put the short form in brackets — `random number generator (RNG)`, not bare `RNG`.
Same rule as introducing a concept: check it's been spelled out before; if not, spell it out.
For a *simple* concept the expansion alone is enough (no further explanation needed).

**Never introduce a concept you don't explain (strict).** The moment a card's answer uses a
term, mechanism, or named thing the learner may not already hold (`global RNG`, `seed`,
`multicollinearity`), you MUST resolve it before the card ships — no bare jargon, ever.

Cards must be **self-contained**: Anki has no clickable card-to-card link during review, so a
learner cannot "jump to the other card." Never write a "See also: <other card>" pointer and
call the concept explained — it isn't, the reader can't follow it. Resolve every unexplained
term *inside the card itself*. Use the **2-3-word test** to decide how:
- **Can you explain it in a brief parenthetical (~2-5 words / one clause)?** → gloss it inline
  and move on. e.g. `random number generator (RNG)`, `multicollinearity (one column redundant)`.
- **Does it need more than that?** → DO NOT cram the explanation in — that bloats the card and
  smuggles in a second concept. Instead **make a separate granular card** that owns it (search
  the `05-Flashcards/` tree first with `grep` to avoid duplicates), and on *this* card keep
  only the shortest gloss that lets the sentence stand. One card teaches one thing.

This is the anti-bloat rule: when in doubt between "add three more sub-bullets explaining X"
and "spin X into its own card," spin it out. A long answer is a smell that two concepts shared
one card. The litmus test mirrors the atomic-note rule — a learner reading top-to-bottom must
never hit a term whose meaning lives nowhere in that same answer, *and* the answer must never
grow so long that it's really teaching two things.

Three failure modes are common enough to keep in mind on every batch (the protocols and
the full reasoning are in `references/question-rules.md`):

- **Split enumerations** — a list of 4+ items can't be recalled as one answer (and cloze
  won't save it). Break it into a count card + one card per item.
- **No hidden hints** — cover the answer and read the stem; if it's guessable, it leaks.
- **Watch interference** — if two cards' stems cue the same answer in their first few
  words, they collide on review. Add a distinctive landmark to each.

For the deeper craft of *what makes a question worth asking* — effortful retrieval, single
concept, right granularity (definition vs how vs why vs when), the extraction sweep — read
`references/question-rules.md`. Consult it whenever a card feels weak, trivial, or like trivia.

When a concept is inherently spatial — a topology, a tree operation, a sequence diagram, a
loss curve — a **visual card** beats words (dual coding). Read `references/visual-cards.md`
for the three valid patterns and the one rule (the image is the *cue*, never the answer).

Before syncing a batch, run the fast pre-sync gate in `references/quality-checklist.md` —
it catches the top failure modes (enumeration traps, leaked hints, interference, orphans)
that quietly waste review time for months.

## English cards

Three note types, picked by what the card asks. Full field lists and examples in
`references/syntax.md`.

| Card asks | Note type | Deck |
|---|---|---|
| A word's meaning, or any question and answer | `English Card` | `English::General` · `English::Tech Terms` |
| Produce a grammatical form in a real sentence | `English Grammar` (cloze) | `English::Grammar` |
| Produce the word from an English definition | `A_English_Translate` | see `references/vocab.md` |

`English Card` has five optional fields — `Example`, `Collocations`, `Synonyms`, `Forms`,
`Pattern` — that vanish when empty, so it also serves as a plain two-field card. Fill only
what earns its place; `Synonyms` must say how each one *differs*, never just list them.

**The recall target is one thing, and the rest is scenery.** On a grammar card the cloze is
the test and `Explanation` is a reminder the learner is never graded on — it renders dimmer
and smaller to make that obvious. Same logic on a vocab card: you recall the meaning, and
the collocations and forms are there to be re-read, not recited. <mark style="background: #FF5582A6;">A card that quietly asks the
learner to recall four fields is four cards wearing one coat, and none of them get learned.</mark>

**Never card a grammar rule before learning it.** Read the unit, write the note, then card
it. Cards test knowledge; they do not deliver it.

Exam technique belongs in `English::IELTS::`; a word or rule met during IELTS practice does
not — it goes to the general English decks, because it outlives the exam.

## Syncing to Anki

The card files are inert until synced. One-time setup (AnkiConnect, plugin scan folder)
and the daily sync flow are in `references/workflow.md`. The short version: Anki must be
running, click the Anki ribbon icon in Obsidian, new cards get an `<!--ID:-->` stamped
automatically — never hand-edit those IDs.

## Reference files

- `references/syntax.md` — note types, full deck hierarchy (+ ordering sequenced sub-decks), file header, START/END format
- `references/question-rules.md` — active-recall quality: effortful retrieval, phrasing rules, enumeration split, extraction sweep, pitfalls
- `references/quality-checklist.md` — fast pre-sync gate: top-5 killers + per-card checks
- `references/visual-cards.md` — when and how to make diagram/image cards (dual coding)
- `references/vocab.md` — vocabulary card format, fields, deck paths, examples
- `references/workflow.md` — Obsidian→Anki setup, sync, and the deck-rename migration gotcha
