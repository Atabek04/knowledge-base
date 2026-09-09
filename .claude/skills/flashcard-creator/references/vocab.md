# Vocabulary Flashcard Rules

For when the user sends a sentence and asks what a word or phrase means. These cards use the
`English Card` note type — the word on the front, its meaning and usage on the back.

## Prerequisites

### Anki Setup (One-time)

1. Install [AnkiConnect](https://ankiweb.net/shared/info/2055492159) addon in Anki
2. Configure AnkiConnect: Tools → Add-ons → AnkiConnect → Config:
```json
{
  "webCorsOriginList": ["app://obsidian.md"]
}
```

3. Create note type `English Card` in Anki — fields and templates are specified in
   `syntax.md`.

### Obsidian Setup (One-time)

1. Install `Obsidian_to_Anki` plugin
2. Set scan folder to include `05-Flashcards/`

---

## When to Use

User sends a sentence and asks what a word/phrase means.

**Action:** Add a new `START...END` block to the appropriate flashcard file in
`05-Flashcards/vocab/`.

---

## Card Format

```markdown
START
English Card
{the target word or phrase}
Back: {the meaning, bolding the core of it}
- {a distinction or restriction worth carrying}
Russian: {Russian translation matching this sense}
Example: {original sentence from user, target word bolded}
Forms: {word family, · separated}
Pattern: {grammatical frame the word demands}
Collocations: {· separated, partner word bolded}
Synonyms: {each one stating how it differs}
Tags: vocab {part of speech or domain}
<!--ID: 1770704985804-->
END
```

Only `Front` (the bare word line) and `Back` are required. Every other field disappears from
the rendered card when empty — fill only what earns its place.

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

### Front — the bare word line
- The exact word or phrase the user asked about, on its own line right after the note type
- If figurative usage, mark it: `one-way street (figurative)`
- Phrasal verbs in infinitive form: `to boil down to`

### Back
- The meaning as a sentence, with the **core of the definition bolded**
- Below it, bullets only for a distinction or restriction that changes how the word is used:
  a boundary against a near-synonym, a transitivity constraint, a literal-vs-figurative split
- One sense per card — if a word has multiple distinct meanings, make separate cards

### Russian
- The translation matching **this card's sense only** — not the word's whole range
- If no clean 1:1 exists, give the closest plus a short parenthetical
- **Translate as a native speaker, not a dictionary.** Write what a Russian person actually
  says out loud — not the calque or the first machine-translation hit. If a textbook-correct
  word exists but nobody uses it, drop it or demote it to second place.
  - ✓ `газированная вода, газировка` for *seltzer water*
  - ✗ `сельтерская вода` — technically a translation, but almost no one says it
- Renders directly under the meaning, above the example

### Example
- Prefer the original sentence the user sent
- Refine only if the original is too long or unclear
- Bold the target word: `Remote work felt like a **one-way street**.`

### Forms / Pattern / Collocations / Synonyms
See `syntax.md` for the mechanics. The one rule worth repeating: **`Synonyms` is never a
bare list.** Each entry states how it differs, because a thesaurus swap preserves the meaning
and destroys the collocation. `wane` alone teaches nothing; `wane — influence and interest,
not physical stock` teaches the boundary.

### What not to put on the card

**The default is less.** Everything on a card is something the learner carries on every
single review — a line that isn't pulling weight is pure cost.

Do not write:

- **A restatement of the definition** in different words.
- **A contrast or opposite word** just because one exists. `de jure` is genuinely interesting
  next to `de facto` and still doesn't belong — it's a second word smuggled onto a card that
  tests one. If it's worth learning, it gets its own card.
- **Spelling or form mechanics the Example already displays** — "written as two words, no
  hyphen" is dead weight when the Example shows the word written correctly.
- **Etymology that only decorates.** "Latin for 'of fact'" explains nothing the definition
  didn't. Keep an origin only when it works as a *mnemonic hook* — something that makes the
  word re-derivable rather than merely memorized (`crux` = Latin for *cross*, so the crux is
  the crossing point where everything resolves).
- **Extra senses of the word.** Those are separate cards, not a footnote.

One hard rule: **never reference the user's own mistake.** If they sent the phrase with an
error, silently fix it in Example/Front and write the rule positively — don't quote the wrong
version or say "not X".
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
- Each card's **Back and Example must match its own context** — don't cross-contaminate.
- The `Back` may briefly point to the *other* sense ("Everyday English: …" / "In IT: …") so
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

#### `general.md` — everyday English, tagged by word class

```markdown
TARGET DECK: English::General

START
English Card
trail
Back: A **series of marks or things left behind** along a path, showing where something passed.
- The whole sequence, not one mark — a single footprint is not a trail
- Figuratively: any ordered residue a process leaves behind
Russian: след, цепочка следов; тропа
Example: Solving a linear system produces a **trail** of systems, each replacing the last, and the answer is read off the final one.
Forms: trail · trailed · trailing
Pattern: a trail **of** sth
leave **a trail**
Collocations: **paper** trail · **hiking** trail · trail of **destruction** · **blaze a** trail
Synonyms: **track** — the physical marks themselves, often one set of prints
**wake** — what follows behind a moving thing, water or metaphor; never a route you walk
Tags: vocab noun
END

START
English Card
to boil down to
Back: To be **reducible to the essential point** once everything inessential is stripped away.
Russian: сводиться к (чему-то)
Example: The whole debate **boils down to** whether we prioritize latency or throughput.
Tags: vocab phrasal-verb
END
```

What these two show:

- **The second card is four lines, and that is a normal card.** Fill the optional fields only
  when the word actually has a family, a frame, or a confusable neighbour worth the space.
- **Word class lives in `Tags:`, not in a separate file.** `phrasal-verb` is a tag, not a deck.
- **The user's own sentence is the Example**, kept verbatim with the target bolded — the
  word is recalled in the context they actually met it in.

#### `tech-terms.md` — a distinct meaning inside a domain

```markdown
TARGET DECK: English::Tech Terms

START
English Card
to provision
Back: To **allocate and configure infrastructure automatically** so it is ready to serve traffic.
- Everyday English means "to supply with what's needed" — provisioning a ship for a voyage; in IT the sense narrows to automated resource allocation
Russian: разворачивать, поднимать (сервер, окружение)
Example: The platform automatically **provisions** a new VM when traffic spikes.
Collocations: **provision a** server · **auto-**provisioning
Tags: vocab cloud infrastructure
END
```

What this one shows:

- **The domain sense gets its own card** — the definition and example are framed entirely
  inside cloud infrastructure, never split across two contexts.
- **A bullet points at the everyday sense** so the learner sees the link, but the card is
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
- Only `Front` and `Back` are required — omit any optional field with nothing to say
- Tags: lowercase, space-separated
- Check the file before adding to avoid duplicates
