---
aliases: [Sentence Mining, MIA method, Refold method, i+1 cards, contextual vocabulary cards]
created: 2026-05-28
tags: [language-learning, vocabulary, anki, sentence-mining, refold, mia]
---

### What it is

Sentence mining is a vocabulary acquisition strategy where learners extract full sentences containing unknown words from authentic input (books, shows, articles, podcasts) and build Anki cards from those sentences — rather than from word lists or dictionary entries.

---

### Why sentences, not isolated words

A word's meaning is partially a function of its context — collocations, register, pragmatic use patterns.

"Run a company" / "run a marathon" / "run a program" are the same word with semantically distinct uses. An isolated word card collapses this richness into a single decontextual gloss. A sentence card preserves the *instance* of use that makes meaning concrete.

This is the incidental acquisition advantage applied deliberately: you're using the authentic context as the card, not a dictionary's summary of it.

---

### The Refold / MIA (Massive Input Approach) workflow

1. Consume authentic input at i+1 (shows, podcasts, books you can mostly understand)
2. When an unknown word appears in a sentence you otherwise understand, mine it
3. **Card front:** the sentence with the unknown element highlighted or blanked (cloze)
4. **Card back:** the target word's meaning + a translation of the unknown word only (not the whole sentence)
5. Review in Anki with SRS scheduling

---

### The i+1 card requirement

A mined sentence must have <mark style="background: yellow">**exactly one unknown word or grammar point**</mark>.

If two or more things are unknown in the sentence, the card will be failed for the wrong reason and the SRS interval won't track the right item. Mixing unknowns creates ambiguous feedback — the algorithm can't distinguish "forgot the target word" from "didn't understand the context."

---

### How it inverts traditional vocabulary study

**Traditional order:**
word list → study word in isolation → encounter it later in context (hoping context reinforces)

**Sentence mining order:**
encounter word *in* context → build card *from* that context → review *in* context

You start from meaning-in-use rather than arriving at it later. The card preserves the acquisition moment.

---

### Tools for implementation

- **Language Reactor** (Netflix/YouTube) — mines sentences from subtitles with one click → Anki
- **Yomichan/Yomitan** (browser extension) — hover-to-dictionary + instant Anki card creation (Japanese/Chinese)
- **Readlang** — sentence mining from web articles for European languages
- **Obsidian + ObsidianToAnki** — mine sentences from text notes captured in the vault

---

Read more:
- [[Spaced repetition schedules vocabulary review at expanding intervals matched to the forgetting curve]]
- [[Deliberate vocabulary study and incidental acquisition target different frequency bands in the lexicon]]
- [[Comprehensible input at i+1 requires graded exposure sequenced by difficulty to drive acquisition]]
- [[Nation's vocabulary load research identifies word-frequency thresholds for unaided text comprehension]]
