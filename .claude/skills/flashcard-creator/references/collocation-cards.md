# Writing collocation flashcards

The working brief for turning a unit of McCarthy & O'Dell's *English Collocations in Use
Intermediate* (2nd edition) into Anki cards. The learner is a software engineer, first
language Uzbek/Russian, preparing for IELTS Academic band 8.0.

## Reading the book

PDF: `~/Documents/Books/English/Collocations/Collocations In Use Intermediate.pdf`

Unit *n*'s explanation page is **`2n + 8`**; the exercises sit on `2n + 9` and are **not**
carded yet. Read a unit with:

```
pdftotext -f <page> -l <page> -layout "$HOME/Documents/Books/English/Collocations/Collocations In Use Intermediate.pdf" -
```

<mark style="background: #FF5582A6;">Read every unit before writing its cards.</mark> The book's own example sentences and its
**Common mistakes** boxes are the raw material; never write a collocation card from a general
sense of what collocates with what.

## The note type

**English Card** only. The line after the note type is the question; `Back:` holds the answer.
Do not use `English Grammar` — cloze cards come later, from the exercises.

```
START
English Card
The cue, on one line
Back: **The collocation.**
- a supporting bullet
- another
Tags: collocations <topic-tag>
END
```

Blank line between blocks. Never write an `<!--ID:-->` — the sync stamps those. Markdown
works inside fields. Never use the literal double-equals character pair; it breaks Dataview.

## The card format, and the reasoning behind it

Cards run **meaning → collocation**, never the reverse. You already recognise *heavy rain*
when reading; what fails is writing *strong rain*. <mark style="background: #ABF7F7A6;">A recognition card builds a passive
vocabulary that never reaches the page.</mark>

But a bare gloss is ambiguous — "rain falling very hard" admits *heavy*, *torrential* and
*pouring*. So the cue carries two constraints: **the gloss, and the node word**.

```
START
English Card
Proof so complete that it cannot be argued against → ______ proof
Back: **irrefutable proof** — literally proof that cannot be refuted.
- Weaker sibling: *he does not **offer** irrefutable proof* — proof is **offered**, not *given*
- Related: **supporting evidence**, which you *offer*
Tags: collocations academic-writing
END
```

### The rules

1. **Give the node word, produce the collocate.** `______ research`, `______ proof`,
   `make a ______ contribution`. The blank marks what the learner supplies.
2. **When several collocates are correct, list them all and state the count.**
   *"**powerful arguments** — also **compelling** · **persuasive** — three that work."*
   <mark style="background: #FF5582A6;">Marking a correct answer wrong is worse than having no card</mark>, and it teaches distrust of
   the whole deck. Naming the alternatives is the honest fix, not pretending one exists.
3. **Name the error the card prevents.** Every unit's *Common mistakes* box is a card:
   *do research* not *make research*, *put forward a theory* not *give a theory*. These are the
   highest-value cards in the book because they are pre-identified failure points.
4. **Give the Russian source of the error where it explains one** — *делать* behind *make
   research*, *сильный дождь* behind *strong rain*. Only where it genuinely predicts the
   mistake; do not force it onto every card, and never use Uzbek.
5. **Function cards beat word cards for the rhetorical units.** Where a unit groups
   collocations by the job they do, card the job: *"How do you hedge an opinion in academic
   writing? (two collocations)"* → **a tentative explanation** · **broadly support the view
   that…**. These transfer to Task 2 in a way single-word cards do not.
6. **Card the collocation, never the topic word.** The unit on Weather is not a vocabulary
   list about weather — it is about which adjective goes with which noun. If a card would be
   answered by knowing a word rather than knowing a pairing, it does not belong.
7. **Select, do not sweep.** A unit lists twenty or more collocations; card the ones that
   earn a place. A collocation earns one if it is unguessable from its parts, if the book
   flags it as a mistake, or if it is usable in an IELTS essay or a Part 3 answer. Skip the
   ones that are transparent to a competent reader.
8. Answers stay scannable: a bold lead, then two to four short bullets.

Aim for **6–10 cards per unit** in the topic sections, and more where the unit is dense with
mistakes or academic language. Never pad to a number.

### Register matters, and it varies by unit

This book is largely conversational. Units on Music, Sport, Ways of walking and Taste and
smell serve Speaking, not Writing. Units on Academic writing, Cause and effect, Number and
frequency, Change, and Claiming and denying serve Task 1 and Task 2 directly.

Where a collocation is informal or spoken, **say so on the card** and give the neutral
equivalent if one exists. A learner who drops *hit the headlines* into Task 2 loses marks for
register, and the card is where that gets prevented.

## The deck map

One file per deck, at `05-Flashcards/english/collocations/{nn}-{topic}.md`. Sections follow
the book's own contents.

| Deck | Units |
|---|---|
| `01 - Grammatical Aspects` | 6–9 |
| `02 - Special Aspects` | 10–12 |
| `03 - Travel and Environment` | 13–16 |
| `04 - People and Relationships` | 17–20 |
| `05 - Leisure and Lifestyle` | 21–26 |
| `06 - Work and Study` | 27–33 |
| `07 - Society and Institutions` | 34–39 |
| `08 - Basic Concepts` | 40–50 |
| `09 - Functions` | 51–60 |

**Units 1–5 are never carded** — *What is a collocation*, dictionary use, types, register.
They are method, read once.

Each file opens with four lines, then a blank line, `---`, a blank line, and the blocks:

```
TARGET DECK: English::Collocations::<deck>
Tags: collocations
**Chapter:** <chapter> — McCarthy & O'Dell, English Collocations in Use Intermediate, Units <range>
**Related:** [[IELTS - MOC]]
```
