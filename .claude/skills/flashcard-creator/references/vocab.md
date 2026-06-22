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

All vocab cards go under the `Tech-KB::English Vocab` deck root, split into category files:

```
05-Flashcards/vocab/
├── idioms.md          → TARGET DECK: Tech-KB::English Vocab::Idioms
├── phrasal-verbs.md   → TARGET DECK: Tech-KB::English Vocab::Phrasal Verbs
├── advanced.md        → TARGET DECK: Tech-KB::English Vocab::Advanced
├── it-terms.md        → TARGET DECK: Tech-KB::English Vocab::IT Terms
└── collocations.md    → TARGET DECK: Tech-KB::English Vocab::Collocations
```

Files and folders are created on-demand. Pick the best-fitting category for the word.

Each file needs a header:

```markdown
TARGET DECK: Tech-KB::English Vocab::{Category}
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
- **Optional — omit if nothing useful to add.** Most cards won't need this.
- Good uses:
  - Literal vs figurative: "Literally: a road with one-direction traffic. Here used figuratively: a situation with no going back."
  - Context shift: "In general English means 'to provide.' In cloud/IT: to allocate and configure resources automatically."
  - Register/formality: "Formal written English. Casual alternative: 'set up.'"
- Skip if it would just restate the definition.
- **Never reference the user's own mistake.** If they sent the phrase with an error, silently
  fix it in Example/English and write the Note as the positive rule only — don't quote the
  wrong version or say "not X".
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

```markdown
TARGET DECK: Tech-KB::English Vocab::Idioms

START
A_English_Translate
A situation where only one outcome or direction is possible
English: one-way street (figurative)
Russian: Односторонняя улица; безальтернативная ситуация
Example: For years after the pandemic, remote work felt like a **one-way street**.
Note: Literally a street allowing travel in one direction only. Figuratively: something with no alternative or return.
Tags: idiom figurative
<!--ID: 1770704985806-->
END

START
A_English_Translate
To be reducible to the essential point
English: to boil down to
Russian: Сводиться к (чему-то)
Example: The whole debate **boils down to** whether we prioritize latency or throughput.
Tags: phrasal-verb
<!--ID: 1770704985808-->
END
```

```markdown
TARGET DECK: Tech-KB::English Vocab::IT Terms

START
A_English_Translate
To allocate and configure resources so they are ready for use
English: to provision
Russian: Выделять и настраивать ресурсы
Example: The platform automatically **provisions** a new VM when traffic spikes.
Note: General English means "to supply." In IT: automated resource allocation and setup.
Tags: cloud infrastructure
<!--ID: 1770704985809-->
END

START
A_English_Translate
An operation that produces the same result no matter how many times it runs
English: idempotent
Russian: Идемпотентный
Example: PUT requests should be **idempotent** — sending the same update twice won't create duplicates.
Tags: api rest
<!--ID: 1770704985811-->
END
```

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
