---
aliases: [Spaced Repetition, SRS, Anki SRS, SuperMemo, SM-2 algorithm]
created: 2026-05-28
tags: [language-learning, vocabulary, spaced-repetition, anki, memory, retention]
---

### What it is

Spaced repetition is a scheduling algorithm that times each vocabulary review to occur just before memory of that item decays below a threshold (typically ~90% recall probability).

**The mechanism:**
Ebbinghaus (1885) showed memory decays exponentially after initial encoding. Re-encoding at the moment of near-forgetting produces a steeper, longer-lasting retention curve than re-encoding while memory is still fresh.

The algorithm exploits this: easy items expand their review intervals; hard items contract them. You spend your time where forgetting is actually happening.

---

### How Anki implements it (SM-2)

Anki uses a variant of the SM-2 algorithm. Each review produces a quality rating (Again / Hard / Good / Easy). The system calculates:

- **Interval** — days until next review
- **Ease factor** — a multiplier (default 2.5) that expands or contracts intervals based on accumulated rating history

A card consistently rated "Hard" might appear every 3 days; a card rated "Easy" might appear once a month. Over time, the algorithm learns the retention curve for each card individually.

---

### What makes SRS different from generic flashcards

Generic flashcard review (random order, fixed repetition) ignores the forgetting curve. You review words you already know as often as words you're struggling with.

SRS allocates review time *inversely to recall strength* — maximum efficiency per minute of study.

Nation's research on vocabulary acquisition suggests a word needs 10–20+ varied-context exposures before full acquisition. <mark style="background: cyan">SRS maintains words in active memory between natural input encounters</mark> — it is a retention tool, not a primary acquisition tool.

---

### Critical limitation

<mark style="background: pink">SRS does not teach vocabulary — it only maintains what's already partially learned.</mark>

A card you don't understand on day one will keep failing regardless of scheduling. The fix: create the card *after* you understand the word in context, not before.

This is why [[Sentence mining builds Anki cards from real input to preserve the contextual meaning that isolated words lose|sentence mining]] is a superior card-creation method over importing raw word lists.

---

### Relationship to deliberate vs. incidental acquisition

SRS is the primary tool for the [[Deliberate vocabulary study and incidental acquisition target different frequency bands in the lexicon|deliberate study]] phase (core frequency bands: first 3,000 word families). Beyond that frequency range, incidental acquisition through extensive reading is more scalable.

---

Read more:
- [[Sentence mining builds Anki cards from real input to preserve the contextual meaning that isolated words lose]]
- [[Deliberate vocabulary study and incidental acquisition target different frequency bands in the lexicon]]
- [[Desirable difficulties make learning harder in ways that improve long-term retention over short-term fluency]]
- [[Nation's vocabulary load research identifies word-frequency thresholds for unaided text comprehension]]
