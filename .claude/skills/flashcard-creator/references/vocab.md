# Vocabulary Flashcard Rules

For when the user sends a sentence and asks what a word or phrase means. These cards test
**production recall** — the user reads an English definition and must produce the word. A
different note type and deck from technical cards; don't reuse the tech-card format here.

## Prerequisites

### Anki Setup (One-time)

1. Install [AnkiConnect](https://ankiweb.net/shared/info/2055492159) addon in Anki
2. Configure AnkiConnect: Tools → Add-ons → AnkiConnect → Config:
```json
{
  "webCorsOriginList": ["app://obsidian.md"]
}
```

3. Create note type `A_English_Translate` in Anki:
   - Tools → Manage Note Types → Add → Blank
   - Name: `A_English_Translate` (case-sensitive)
   - **Fields button** — add in this order:
     1. `Definition` — English definition sentence (card front)
     2. `English` — the target English word or phrase
     3. `Russian` — Russian translation
     4. `Example` — sentence showing usage in context
     5. `Note` — optional context-specific clarification
   - **Cards button:**
     - Front template: `{{Definition}}`
     - Back template: `{{English}}<br>{{Russian}}<br><br>{{Example}}<br><br><i>{{Note}}</i>`

### Obsidian Setup (One-time)

1. Install `Obsidian_to_Anki` plugin
2. Set scan folder to include `05-Flashcards/`

---

## When to Use

User sends a sentence and asks what a word/phrase means.

**Action:** Add a new `START...END` block to the appropriate flashcard file in
`05-Flashcards/vocab/`.

---

## How It Works

The card tests **production recall**: user reads a definition and must recall the English
word.

```
Front (Definition):  "A situation where only one outcome or direction is possible"
Back (English):      "one-way street (figurative)"
Back (Russian):      "Одностороннее движение; безальтернативная ситуация"
Back (Example):      "For years after the pandemic, remote work felt like a one-way street."
Back (Note):         "Literally: a street allowing travel in one direction only. Figuratively: something with no alternative or no turning back."
```

---

## Card Format

```markdown
START
A_English_Translate
{concise English definition as a sentence}
English: {the target word or phrase}
Russian: {Russian translation}
Example: {original sentence from user, or a refined version}
Note: {context-specific meaning, literal vs figurative, register — only if useful}
Tags: {tags}
<!--ID: 1770704985804-->
END
```

---

## File Location & Deck

All vocab cards go under the `English` deck root, split by **context**, not by
part-of-speech or word class. There are exactly two files:

```
05-Flashcards/vocab/
├── general.md      → TARGET DECK: English::General
└── tech-terms.md   → TARGET DECK: English::Tech Terms
```

**Pick the file by context, not by word type.** Idioms, phrasal verbs, collocations and
advanced vocabulary all live in `general.md` — they are everyday English and are
distinguished by their `Tags:` line (`idiom`, `phrasal-verb`, `collocation`), not by a
separate file or deck. A word only goes to `tech-terms.md` when it carries a **distinct
meaning inside a technical/domain context** (see "Dual-context words" below).

Do **not** create new vocab files or deck paths. Two files, two decks — that's the whole
structure. Adding `idioms.md` or an `English Vocab::` deck root fragments the review queue
and orphans cards in Anki.

Each file's header is already in place:

```markdown
TARGET DECK: English::General
```

---

## Field Rules

### Definition (front of card)
- A concise English sentence explaining the meaning
- The user reads this and tries to recall the word — so **never include the target word**
- Write it like a dictionary entry but natural, not robotic
- One definition per card — if a word has multiple distinct meanings, make separate cards

### English
- The exact word or phrase the user asked about
- If figurative usage, mark it: `one-way street (figurative)`
- Phrasal verbs in infinitive form: `to boil down to`

### Russian
- Translation matching the specific definition given
- If no clean 1:1 translation exists, give closest + brief note
- **Translate as a native speaker, not a dictionary.** Write the word a Russian person
  actually says in daily life — not the literal/calque form or the first hit a machine
  translator returns. Pick the most commonly practiced term; if a textbook-correct word
  exists but nobody uses it, drop it or demote it to second place.
  - ✓ `газированная вода, газировка` for *seltzer water*
  - ✗ `сельтерская вода` — technically a translation, but almost no one says it
  - Litmus test: would a native speaker use this word out loud, or only see it in a manual?

### Example
- Prefer the original sentence the user sent
- Refine only if the original is too long or unclear
- Bold the target word: `Remote work felt like a **one-way street**.`

### Note

**The default is no Note at all.** Most cards should ship without this field. Everything on
a card is something the learner has to carry in their head on every single review — a Note
that isn't pulling weight is pure cost.

A Note is admissible for exactly two reasons:

1. **A mnemonic hook** — something that makes the word *re-derivable* rather than merely
   memorized. `crux` = Latin for *cross*, so the crux is the crossing point where everything
   resolves. The learner who forgets the meaning can rebuild it from the hook.
2. **A clarification or distinction that changes how the word is used** — the thing that
   would otherwise cause a mistake in real usage:
   - Literal vs figurative: "Literally a road with one-direction traffic; here figurative — a situation with no going back."
   - Context shift: "General English: 'to supply.' In cloud/IT: automated resource allocation."
   - Register: "Formal written English. Casual alternative: 'set up.'"

If what you're about to write isn't one of those two, **delete the field**. Encyclopedic
background, contrast words, etymology-as-decoration and usage trivia all read as useful and
are not — they inflate a one-word card into a paragraph the learner must re-read forever.

Concretely, do not write:

- **A restatement of the definition** in different words.
- **A contrast or opposite word** just because one exists. `de jure` is genuinely interesting
  next to `de facto` and still doesn't belong — it's a second word smuggled onto a card that
  tests one. If it's worth learning, it gets its own card.
- **Spelling or form mechanics the Example already displays** — "written as two words, no
  hyphen" is dead weight when the Example shows the word written correctly.
- **Etymology that only decorates.** "Latin for 'of fact'" explains nothing the definition
  didn't. Keep an origin only when it functions as the hook in case 1.
- **Extra senses of the word.** Those are separate cards, not a footnote.

One hard rule when a Note *is* justified: **never reference the user's own mistake.** If they
sent the phrase with an error, silently fix it in Example/English and write the Note as the
positive rule only — don't quote the wrong version or say "not X".
  - ✓ `You advocate FOR something. Always takes the article: "a big advocate for".`
  - ✗ `Needs the article — "a big advocate for", not "big advocate for".`

---

## Dual-context words (general + technical)

Some words carry a **distinct meaning in a technical/domain context** AND a **different
everyday-English meaning** (e.g. `oscillate`, `converge`, `pile up`, `ransom`). Never stuff
both senses into one card — a card mixing two contexts tests neither cleanly and the
example can only show one.

**Make two separate cards:**

| Card | File | Deck | Frame definition + example in... |
|------|------|------|----------------------------------|
| Technical | `vocab/tech-terms.md` | `English::Tech Terms` | the technical/domain context (ML, networking, security…) |
| General | `vocab/general.md` | `English::General` | everyday English |

Rules:
- Each card's **Definition and Example must match its own context** — don't cross-contaminate.
- The `Note` may briefly point to the *other* sense ("Everyday English: …" / "In IT: …") so
  the learner sees the link, but the card is tested on its own context only.
- Tag the technical card with its domain (`ml`, `networking`, `security`); the general card
  gets only its part of speech (`verb`, `noun`, `phrasal-verb`).
- **Why:** clean per-context retrieval, and the tech deck stays a focused study unit instead
  of being diluted with everyday senses.

A word belongs in `General` only (single card) when its example/usage is everyday and it has
no distinct technical sense — domain flavor in the *example* alone (e.g. economics, finance)
doesn't make it a tech term.

---

## Example Cards

Everything below is a real card from the vault, annotated with the rule it demonstrates.

#### `general.md` — everyday English, tagged by word class

```markdown
TARGET DECK: English::General

START
A_English_Translate
Existing or accepted as the real thing in practice, even though it was never officially declared or made official
English: de facto
Russian: фактический, по факту, на деле (хотя официально не закреплённый)
Example: If the course slips badly, $20 becomes the **de facto** price and $29 loses credibility when it finally arrives.
Tags: adjective adverb latin
END

START
A_English_Translate
To be reducible to the essential point once everything inessential is stripped away
English: to boil down to
Russian: сводиться к (чему-то)
Example: The whole debate **boils down to** whether we prioritize latency or throughput.
Tags: phrasal-verb
END
```

What these two show:

- **The Definition never contains the target word** — "de facto" appears nowhere in its
  own front field, so recall is real production, not pattern-matching.
- **Neither card has a `Note`, and that is the normal case.** `de facto` invites one —
  etymology, the `de jure` contrast, the no-hyphen spelling — and every candidate failed the
  test: the definition already carries the meaning, the Example already shows the spelling,
  and `de jure` is a second word that belongs on its own card. Four lines is the whole card.
- **Word class lives in `Tags:`, not in a separate file.** `phrasal-verb` is a tag, not a
  deck.
- **The user's own sentence is the Example**, kept verbatim with the target bolded — the
  word is recalled in the context they actually met it in.

#### `tech-terms.md` — a distinct meaning inside a domain

```markdown
TARGET DECK: English::Tech Terms

START
A_English_Translate
To allocate and configure infrastructure automatically so it is ready to serve traffic
English: to provision
Russian: разворачивать, поднимать (сервер, окружение)
Example: The platform automatically **provisions** a new VM when traffic spikes.
Note: Everyday English means "to supply with what's needed" — provisioning a ship for a voyage. In IT the sense narrows to automated resource allocation and setup.
Tags: cloud infrastructure
END
```

What this one shows:

- **The domain sense gets its own card** — the definition and example are framed entirely
  inside cloud infrastructure, never split across two contexts.
- **The `Note` points at the everyday sense** so the learner sees the link, but the card is
  still tested on one meaning only.
- **The Russian is what an engineer actually says** (`разворачивать`), not the dictionary
  calque (`обеспечивать`).
- **Tags name the domain** (`cloud`, `infrastructure`) rather than the part of speech.

---

## Sync

1. Anki must be running
2. Click Anki ribbon icon in Obsidian
3. New cards get `<!--ID: -->` stamped automatically — don't touch these
4. Editing and re-syncing updates the card (progress preserved)

---

## Key Rules

- One word/phrase per card
- Blank line between `END` and next `START`
- Never include the target word in the Definition field
- Note field is optional — omit entirely if nothing useful to add
- Tags: lowercase, space-separated
- Check the file before adding to avoid duplicates
