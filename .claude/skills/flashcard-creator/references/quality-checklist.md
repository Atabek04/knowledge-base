# Flashcard Quality Gate

Run this as a fast pass over a batch **before syncing to Anki**. It's a gate, not a
tutorial — for the *why* behind each rule, see `question-rules.md`. The point is to catch
the failures that quietly waste review time for months.

## Top 5 killers — check these first

Most bad cards die on one of these. Scan for them before anything else.

1. **Enumeration trap** — 4+ items crammed into one answer. Split (see below).
2. **Hidden hint** — the stem leaks the answer. The 70% test: cover the answer, read the
   stem; if someone who never studied could guess it ≥70% of the time → rewrite.
3. **Interference** — another card in the batch has a stem that cues the *same* answer in
   its first few words. Add a distinctive landmark so each stem uniquely points to one answer.
4. **Fused concepts** — definition + reason (or two facts) in one card. One fact = one card.
5. **Orphan** — no trace back to a real atomic note, or no link to a MOC/related concept.

## Enumeration Split Protocol

A list of 4+ items is unretrievable as a single answer, and cloze does **not** fix it (the
hidden chunk has no surrounding scaffold to cue it). Split mechanically:

- **One count card** — "How many X are there?" → the number.
- **One card per item** — either ordinal ("What is the 3rd X?") or, better, keyed on each
  item's distinguishing property so the card isn't just rote position.

≤3 items may stay in one answer as a short bullet list.

## Per-card checks

**Atomicity & load**
- [ ] Tests one idea
- [ ] Answer ≤ ~1 sentence or ≤ 3 bullets — longer → split
- [ ] No 4+ item list (use the split protocol)

**Question quality**
- [ ] Phrased as a question, ends in `?`
- [ ] Not a yes/no stem — rephrase with what / how / why / when / which
- [ ] Stem uniquely specifies one answer
- [ ] No answer tokens leaked into the stem (70% test)

**Recall, not recognition**
- [ ] No multiple-choice / "which of these" — the deck trains production; the exam supplies distractors
- [ ] Real cognitive effort required (not trivial, not impossible)

**Connection & source**
- [ ] Traces back to an existing atomic note (no general-knowledge invention)
- [ ] Linked to a MOC or related concept (not orphaned trivia)

**Technical**
- [ ] Wrapped in START/END, blank line between cards, correct note type
- [ ] `TARGET DECK:` header present and correct
- [ ] No hand-written `<!--ID:-->` (the plugin stamps these)

**Visual cards only** (if the card uses an image — see `visual-cards.md`)
- [ ] Image is the *cue*, not the answer (no "what does X look like?" → image-in-answer)
- [ ] Stem still makes sense if the image failed to load

## Pass condition

All applicable boxes checked → sync. Anything unchecked → fix or delete the card. A deleted
weak card costs nothing; a kept weak card costs review minutes every interval for months.
