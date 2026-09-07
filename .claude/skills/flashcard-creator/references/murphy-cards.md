# Writing Murphy flashcards

The working brief for turning a unit of Raymond Murphy's *English Grammar in Use* (5th
edition) into Anki cards. The learner is a software engineer, first language Uzbek/Russian,
preparing for IELTS Academic band 8.0.

## Reading the book

PDF: `~/Documents/Books/English/Grammar/English Grammar in Use.pdf`

Unit *n*'s explanation page is **`2n + 12`**; the exercises sit on `2n + 13` and are not
carded. Read a unit with:

```
pdftotext -f <page> -l <page> -layout "$HOME/Documents/Books/English/Grammar/English Grammar in Use.pdf" -
```

<mark style="background: #FF5582A6;">Read every unit before writing its cards.</mark> Never write from a memory of what the grammar
point probably says — the book's own examples, and especially its *(not …)* warnings, are the
raw material.

## The two note types

**English Card** — plain question and answer. The line after the note type is the question;
`Back:` holds the answer.

**English Grammar** — a cloze. The line after the note type is the sentence; `Explanation:`
holds the reasoning. Write the gap as `{1:answer}`. Two gaps make two separate cards, so use
one per card unless you mean otherwise.

### Block format — the parser is strict

```
START
English Card
The question, on one line
Back: **The lead claim.**
- a supporting bullet
- another
Tags: grammar <topic-tag>
END

START
English Grammar
The sentence with a {1:gap} (hint) in it.
Explanation: Why that form, in one line.
- the rival form and what it would have meant
- the trap, or a second example
Tags: grammar <topic-tag>
END
```

Blank line between blocks. Never write an `<!--ID:-->` — the sync stamps those. Markdown
works inside fields. Never use the literal double-equals character pair; it breaks Dataview.

## How to write the cards

Grammar is not knowledge, it is a **choice made under time pressure**. Two or three forms are
always available and one is right, so the card must rehearse the choice.

1. **Name the competing form on every card.** <mark style="background: #ABF7F7A6;">A card that shows only the correct answer leaves
   the wrong one untouched, and the wrong one is what turns up in the essay.</mark> The explanation
   says what the rival would have meant.
2. **One card per decision, not per example.** A unit prints five sentences for one rule
   because books teach by repetition; cards do not. Card the decision once, in the sentence
   that shows it most sharply, and list the rest inside the explanation.
3. **Cover every lettered block.** A–E each add a distinct use or restriction. The **form**
   block is the one that gets skipped, and it is what breaks under pressure.
4. **Prefer the sentences flagged *(not …)*.** Those parentheses are Murphy naming the error
   real learners make — pre-identified decision points, and the best gaps in the unit.
5. **A cloze gap must have exactly one correct answer.** If two forms fit, the card grades the
   learner on guessing your intent, and marking a correct answer wrong is worse than having no
   card. Pick a sentence whose grammar forces one form, or put the lemma in brackets after the
   gap — `I {1:have known} (know) her since 2019` — adding a constraint where needed:
   `(rain, negative)`, `(go, with *always*)`.
6. **State the count when a card holds a list** — "When do you use X? *(three uses)*". The
   number tells the learner when to stop retrieving. Past three or four items, split the card
   or group the list into named families.
7. **Give the first-language contrast in Russian, never Uzbek**, and only where it genuinely
   explains a likely error: *"Russian has one present tense, so the simple form feels correct
   here."* Do not force it onto every card.
8. **Exceptions earn their own card** — performatives, stative verbs, irregular behaviour.
   They read as footnotes in the book and are pure trap in the exam.
9. Answers stay scannable: a bold lead claim, then two to four short bullets.

Roughly **5–8 cards per unit**, set by how many real decisions it holds. A dense unit earns
more, a thin one fewer. Never pad to reach a number.

## Two worked examples

```
START
English Grammar
Please don't make so much noise. I {1:'m trying} (try) to work.
Explanation: Happening now, unfinished → present continuous.
- *I try to work* is the present simple, which states a habit, not this moment
- Russian has one present tense — *я стараюсь* covers both, which is why the simple form feels correct here
Tags: grammar present-continuous
END

START
English Card
*think* takes both tenses. What decides which?
Back: **Believe → simple. Consider → continuous.**
- *I **think** Mary is Canadian* — my opinion, a state
- *Nicky **is thinking** of giving up her job* — she is considering it, an activity under way
- The split is the same one as everywhere: **state or action**
Tags: grammar present-simple present-continuous stative-verbs
END
```

## The deck map

One file per deck, at `05-Flashcards/english/grammar/{nn}-{topic}.md`. Sections and unit
ranges follow the book's own contents, which are already in prerequisite order.

| Deck | Units |
|---|---|
| `01 - Present and Past` | 1–6 |
| `02 - Present Perfect and Past` | 7–18 |
| `03 - Future` | 19–25 |
| `04 - Modals` | 26–37 |
| `05 - If and Wish` | 38–41 |
| `06 - Passive` | 42–46 |
| `07 - Reported Speech` | 47–48 |
| `08 - Questions and Auxiliaries` | 49–52 |
| `09 - Verb Patterns` | 53–68 |
| `10 - Articles and Nouns` | 69–81 |
| `11 - Pronouns and Determiners` | 82–91 |
| `12 - Relative Clauses` | 92–97 |
| `13 - Adjectives and Adverbs` | 98–112 |
| `14 - Conjunctions and Prepositions` | 113–120 |
| `15 - Prepositions` | 121–136 |
| `16 - Phrasal Verbs` | 137–145 |

Each file opens with four lines, then a blank line, `---`, a blank line, and the blocks:

```
TARGET DECK: English::Grammar::<deck>
Tags: grammar
**Chapter:** <chapter> — Murphy, English Grammar in Use, Units <range>
**Related:** [[IELTS - MOC]]
```
