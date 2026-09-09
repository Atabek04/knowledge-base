# Flashcard Syntax Reference

Note types, deck hierarchy, file header, and the START/END block format.

## Contents

- Note type: Coding Questions
- Note type: English Card
- Note type: English Grammar
- Deck hierarchy (by subject)
- File header
- START/END block format (one-liner + multi-line)

---

## Note Type: Coding Questions

Fields: `Front`, `Back`

**Anki setup:** Tools → Manage Note Types → Add → Blank → Name: `Coding Questions` →
Fields: Front, Back → Cards: Front `{{Front}}`, Back `{{Back}}`

Used by every `Tech-KB::`, `Math::` and `Self-Mastery::` card. **Not** for `English::` —
those have their own two note types below.

---

## Note Type: English Card

Fields: `Front`, `Back`, `Russian`, `Example`, `Collocations`, `Synonyms`, `Forms`, `Pattern`

Everything after `Back` is optional and disappears from the rendered card when left empty,
so the same note type carries a full vocabulary entry and a bare question-and-answer card.

`Russian` renders directly under the meaning, above the example — it is part of the answer,
not a detail row. Fill it on vocabulary cards; leave it empty on question-and-answer cards.

Vocabulary entry:

```
START
English Card
dwindle
Back: To **shrink steadily over time** until little is left.
- Always gradual — a sudden drop is *plummet*
- Intransitive: a thing dwindles, you cannot dwindle it
Russian: сокращаться, убывать (постепенно)
Example: Attendance **dwindled** from 400 to barely 30 over the decade.
Forms: dwindle · dwindled · dwindling
Pattern: dwindle **to** sth
dwindle **away**
Collocations: dwindling **resources** · dwindling **supply** · dwindle **to** nothing
Synonyms: **diminish** — neutral, size or importance
**wane** — influence, interest, power; not physical stock
Tags: vocab
END
```

Bare question and answer — identical to a Coding Questions card, just a different type:

```
START
English Card
How do you decide singular vs plural on a Listening gap-fill before the audio plays?
Back: **From the printed stem's own grammar.**
- "the ___ **are** stored in" forces plural
- `car(s)` scores **zero**
Tags: ielts listening
END
```

### Filling the optional fields

- **`Synonyms`** — never a bare list. Each entry states *how it differs*, because a
  thesaurus swap preserves the meaning and destroys the collocation. `wane` alone teaches
  nothing; `wane — influence and interest, not physical stock` teaches the boundary.
- **`Pattern`** — the grammatical frame the word demands: `depend **on** sth`,
  `it is worth **doing**`. One per line; the template renders newlines, so no `<br>`.
- **`Forms`** — the word family, `·`-separated. This is where Listening gap-fill marks live.
- **`Example`** — the sentence the word was actually met in, not an invented one.
- **`Collocations`** — `·`-separated, with the partner word bolded.

---

## Note Type: English Grammar

Cloze. Fields: `Text`, `Explanation`

```
START
English Grammar
I {1:have known} (know) her since 2019.
Explanation: Unfinished time period → present perfect.
- *know* is stative, so there is no continuous: "have been knowing" is wrong
- "I **knew** her in 2019" — finished time, past simple
- Russian uses the present *знаю*, which is why "I know her since 2019" feels right
Tags: grammar
END
```

### The gap must have exactly one right answer

<mark style="background: #FF5582A6;">If two correct answers fit the gap, the card is broken — it grades the learner on guessing
which one you had in mind.</mark> Marking a correct sentence wrong is worse than no card at
all, because it teaches distrust of the deck.

`I {1:have lived} here since 2019` is exactly this failure: *have been living* is equally
correct. Three ways to close it, in order of preference:

1. **Choose a sentence where only one form works.** *know* is stative, so the continuous is
   simply ungrammatical and the gap is forced. Best option — the constraint is the grammar
   itself, and learning it is the point.
2. **Put the lemma in brackets after the gap** — `{1:have known} (know)`. Murphy's own
   exercise convention, and it fixes the word while leaving the form to be produced.
3. **Name the constraint in brackets** when several forms remain — `(know — not continuous)`.
   Use last; a bracket that gives away the answer defeats the card.

When a second form genuinely is correct in that sentence, say so in `Explanation` and state
what changes the choice. That is a teaching point, not a defect — but it belongs in the
explanation, never in the gap.

<mark style="background: #ADCCFFA6;">The cloze is the test. `Explanation` is a reminder, and the learner is never graded on
recalling it.</mark> It renders smaller and dimmer for exactly that reason, so keep it to
the contrast and the trap — if it grows into a second thing to memorise, the card is doing
two jobs and the recall target blurs.

Use `{1:...}` / `{c1:...}` for the gap; the sync script converts it and detects the cloze
type by inspecting the template, not by the note type's name.

**Never card a rule you have not yet learned.** Read the unit, write the note, then card
it — a card tests knowledge, it does not deliver it. For a rule statement itself, use
`English Card`; `English Grammar` is for producing a form in a real sentence.

---

## Deck Hierarchy

The deck roots are independent, and they never mix:

- **`Tech-KB::`** — technical knowledge. Cards test what a thing *does*, how it works, why
  it behaves that way.
- **`English::`** — the English language. Vocabulary, grammar, and exam preparation under
  `English::IELTS::`.
- **`Math::`** — mathematics, studied as a subject in its own right.
- **`Self-Mastery::`** — habits, discipline, study technique.

The split is by *what the card asks*, not by subject matter. A card about a technical word
is still a vocabulary card if it asks for the word's meaning — see "English Vocab" below.

### Machine Learning

```
Tech-KB::Machine Learning::Fundamentals
Tech-KB::Machine Learning::Data Preprocessing
Tech-KB::Machine Learning::Model Training
Tech-KB::Machine Learning::Regression
Tech-KB::Machine Learning::Classification
Tech-KB::Machine Learning::Unsupervised
Tech-KB::Machine Learning::Model Evaluation
Tech-KB::Machine Learning::Dimensionality Reduction
Tech-KB::Machine Learning::Model Selection
```

### Math

Math is its own root, not under `Tech-KB::` — it is a subject studied for itself, not a
technology.

```
Math::Linear Algebra
Math::Calculus
Math::Probability
```

### English

```
English::General
English::Tech Terms
English::Collocations::01 - Grammatical Aspects
English::Collocations::02 - Special Aspects
English::Collocations::03 - Travel and Environment
English::Collocations::04 - People and Relationships
English::Collocations::05 - Leisure and Lifestyle
English::Collocations::06 - Work and Study
English::Collocations::07 - Society and Institutions
English::Collocations::08 - Basic Concepts
English::Collocations::09 - Functions
English::Grammar::01 - Present
English::Grammar::02 - Past
English::Grammar::03 - Present Perfect
English::Grammar::04 - Future
English::Grammar::05 - Modals
English::Grammar::06 - Conditionals and Wish
English::Grammar::07 - Passive
English::Grammar::08 - Reported Speech
English::Grammar::09 - Questions and Auxiliaries
English::Grammar::10 - Verb Patterns
English::Grammar::11 - Articles and Nouns
English::Grammar::12 - Pronouns and Determiners
English::Grammar::13 - Relative Clauses
English::Grammar::14 - Adjectives and Adverbs
English::Grammar::15 - Conjunctions
English::Grammar::16 - Prepositions
English::Grammar::17 - Phrasal Verbs
English::IELTS::Band Descriptors
English::IELTS::Listening and Reading
English::IELTS::Speaking Technique
English::IELTS::Strategy and Evidence
English::IELTS::Writing Technique
```

Grammar sub-decks are numbered because they run in prerequisite order — tenses before
modals before conditionals — and they follow Murphy's own sequence. Files live at
`05-Flashcards/english/grammar/{nn}-{topic}.md`, one per deck. The topics are grammar
topics, not book chapters, so they survive finishing the book.

Collocation sub-decks follow the sections of *English Collocations in Use Intermediate*,
files at `05-Flashcards/english/collocations/{nn}-{topic}.md`. Units 1–5 are method and are
never carded. Card-writing rules for both books live in `murphy-cards.md` and
`collocation-cards.md`.

`English::IELTS::` holds **exam technique only** — band descriptors, section strategy, the
mechanics that score or lose marks.

A **word** met during IELTS practice does not go there. A word is a word regardless of where
you met it, so it goes to `English::General` (or `English::Tech Terms`) and outlives the exam.
The one thing that stays in the IELTS tree is spelling drilled for the Listening answer sheet,
because that exists only for the test.

### Software Engineering

```
Tech-KB::Software Engineering::Requirements Engineering
```

### Economics

```
Tech-KB::Economics::AI and Labor
```

### Python

```
Tech-KB::Python::NumPy
Tech-KB::Python::Pandas
Tech-KB::Python::Matplotlib
Tech-KB::Python::Scikit-learn
```

### Linux

```
Tech-KB::Linux::Command-Line Tools
Tech-KB::Linux::Shell Scripting
Tech-KB::Linux::Permissions
```

### DSA (one deck per pattern)

```
Tech-KB::DSA::Sliding Window
Tech-KB::DSA::Two Pointers
Tech-KB::DSA::Fast & Slow Pointers
Tech-KB::DSA::Merge Intervals
Tech-KB::DSA::Trees
Tech-KB::DSA::Graphs
Tech-KB::DSA::Dynamic Programming
(… one per NeetCode/Grokking pattern)
```

### Architecture

```
Tech-KB::Architecture::Reliability
Tech-KB::Architecture::Scalability & Performance
Tech-KB::Architecture::Maintainability
Tech-KB::Architecture::Data Pipelines
Tech-KB::Architecture::Domain-Driven Design
```

### System Design

```
Tech-KB::System Design::Non-Functional Requirements
Tech-KB::System Design::Building Blocks
Tech-KB::System Design::Designs
```

### Design Patterns

```
Tech-KB::Design Patterns::Creational
Tech-KB::Design Patterns::Structural
Tech-KB::Design Patterns::Behavioral
Tech-KB::Design Patterns::Enterprise
```

### Behavioral

```
Tech-KB::Behavioral::STAR Method
Tech-KB::Behavioral::Story Bank
Tech-KB::Behavioral::Negotiation
```

### English Vocab

All English cards sit under the `English::` root — exactly two decks, split by the
**context the word is used in**:

```
English::General      → 05-Flashcards/vocab/general.md
English::Tech Terms   → 05-Flashcards/vocab/tech-terms.md
```

**`English::Tech Terms` is a vocabulary deck, not a knowledge deck.** It holds words the
learner met in a technical context, and it asks one thing: *what does this word mean here?*
It never asks what a tool does, how a protocol works, or why a pattern exists — those are
`Tech-KB::` cards, driven by atomic notes.

- ✓ `to provision` — "to allocate and configure infrastructure so it's ready to serve traffic"
- ✗ `idempotent` framed as "why should PUT be idempotent?" — that's a REST concept card, `Tech-KB::Backend::REST`

Idioms, phrasal verbs and collocations are **not** separate decks — they all live in
`English::General` and are distinguished by their `Tags:` line. See `vocab.md` for the
field format and the dual-context rule.

### Self-Mastery

```
Self-Mastery::Mindset::Recognition & Self-Worth
Self-Mastery::Discipline::Accountability
Self-Mastery::Study Techniques::Caffeine & Cognition
```

The deck list grows on demand — these are the established roots, not a closed set. When a
note belongs to a new subject, extend the hierarchy following the same `Tech-KB::{Category}::{Topic}`
shape.

---

## File Header

Each flashcard file starts with a header that sets the target deck:

```markdown
TARGET DECK: Tech-KB::Machine Learning::Regression
Tags: ml regression
**Related:** [[Link to MOC or concept]]
```

One deck per file. The `TARGET DECK:` value maps the file to its Anki deck.

### Ordering sub-decks that have a natural sequence

Anki sorts sibling decks **alphabetically**, and there's no manual reorder. For most
topic decks that's fine (`Classes`, `Collections`, `Null Safety` — order doesn't matter).
But when siblings carry a real sequence — a DSA pattern progression, a course's chapter
order, a build-up of prerequisites — alphabetical sort scrambles it.

Fix: zero-pad a numeric prefix so the sort respects the sequence.

```
Tech-KB::DSA::01 - Two Pointers
Tech-KB::DSA::02 - Sliding Window
Tech-KB::DSA::03 - Fast & Slow Pointers
```

Use two digits (`01`, not `1`) so the tenth deck doesn't sort before the second. Only do
this where order is meaningful — don't prefix decks that are just an unordered set.

---

## START/END Block Format

### One-liner

```markdown
START
Coding Questions
What does OLS stand for?
Back: Ordinary Least Squares — finds best-fit line by minimizing sum of squared errors
Tags: ml regression
<!--ID: 1771415062868-->
END
```

### Multi-line

```markdown
START
Coding Questions
What are the three properties that describe the structure of a NumPy array?
Back:
- `.shape` → rows × columns as tuple, e.g. `(2, 3)`
- `.ndim` → number of dimensions, e.g. `2`
- `.size` → total element count, e.g. `6`
Tags: python numpy
<!--ID: 1771415062870-->
END
```

The `<!--ID:-->` line is stamped automatically by the plugin on first sync. Never write or
edit it by hand. Leave a blank line between one `END` and the next `START`.
