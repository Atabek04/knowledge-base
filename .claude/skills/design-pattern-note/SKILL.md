---
name: design-pattern-note
description: >-
  Write and structure design pattern notes in the Zettelkasten. Use this whenever the user
  is creating, drafting, or documenting a GoF / design pattern (Strategy, Observer, Factory,
  Decorator, etc.), adding a pattern to the Design Patterns MOC, writing per-language
  implementation notes for a pattern, or asks to "make a note for X pattern". Also trigger
  when teaching a pattern reaches the note-creation step, or when the user wants the
  refactoring.guru-style structure applied to a pattern. Covers the 3-tier note structure
  (concept hub + per-language implementations + principle notes), which language to write
  in, diagrams, and the pedagogy that makes pattern notes memorable.
argument-hint: "[pattern name]"
---

# Design Pattern Note Writer

How to capture a design pattern in this vault so it stays atomic, language-agnostic at the
core, and memorable. The template lives at `Templates/Design Pattern.md` — use it for the
concept hub.

## Three-tier structure

A single pattern is **never** one monolithic note. It splits into three kinds:

1. **Concept note (the hub)** — language-neutral. Follows the template sections: Intent,
   Problem, Solution, Real-world analogy, Structure, When to use, Pros/cons. Pseudocode
   only — no real language. Title is a complete statement
   (e.g. "The Strategy pattern makes algorithms interchangeable by hiding each behind a
   common interface"). This note is "atomic" at the granularity of *one pattern* — every
   section is a facet of that single concept.

2. **Implementation notes** — one per language, written in **Kotlin, Python, and Java**.
   Each is idiomatic, because the pattern often looks *different* per language:
   - Java → interface + one class per algorithm
   - Kotlin → a function type / `typealias`, often no interface
   - Python → a bare first-class function, no interface or ABC
   Default teaching examples to **Kotlin** (least boilerplate). Java is the anchor language
   for first understanding. Each impl note links back to the hub and to its sibling impls.

3. **Principle notes** — general OOP principles a pattern relies on (composition over
   inheritance, open/closed, etc.) are their own atomic notes under the
   `Software Engineering Principles - MOC`, referenced by many patterns. **Never inline a
   principle into one pattern note** — it belongs to all of them.

"Relations with other patterns" (refactoring.guru's last section) is **not** prose here —
it becomes Zettelkasten links in the Read more section. Linking is what the vault does best.

## While writing

- **Fetch refactoring.guru** (`https://refactoring.guru/design-patterns/<pattern>`) for a
  proven analogy and the section ordering. It's the reference for tone and structure — adapt
  the analogy in your own words, don't copy.
- **Add a diagram** — download a UML/structure image to `Assets/` and embed it in the
  Structure section. Visual recall beats prose for patterns. (Use `curl` + the Wikipedia
  imageinfo API or refactoring.guru's diagram.)
- **Keep framework tricks out of the hub** — Spring `Map<String, Strategy>` injection, DI
  wiring, etc. go in the language impl note, never the concept hub. The hub owns only the
  language-neutral mechanic.
- After the concept note and each impl note: add to the `Design Patterns - MOC` (replace the
  `- [ ] Pattern` checkbox with a link) and create flashcards via `flashcard-creator`.

## Pedagogy that makes pattern notes stick

Apply these *inside* the note, not just when teaching live:

- **Name as mnemonic** — open by explaining *why* the pattern has that name, so the name lets
  the reader re-derive the idea. "Strategy = a chosen, swappable *way* to do a task."
- **Problem before solution** — the Problem section shows the painful *without-it* version
  first (the growing `if/else`, the class explosion). The reader must *feel* the need before
  seeing the fix.
- **Quantify the trade-off** — when the value is structural, make it numeric:
  "inheritance = 3×3 = 9 classes (multiplicative); composition = 3+3 = 6 (additive)."
  Numbers beat adjectives.
- **Name the relationship intuition** — spell out IS-A vs HAS-A, "holds vs extends," so the
  reader knows *which kind* of relationship the pattern uses.
- **Surface the common misconception** — every pattern has one (e.g. "Strategy removes all
  `if/else`" — it only *isolates* the choice). Put it in Pros/cons with a pink highlight.

## Worked reference

The Strategy pattern is the canonical example of all of the above:
- Hub: `The Strategy pattern makes algorithms interchangeable by hiding each behind a common interface`
- Impls: `Strategy pattern in Kotlin ...`, `... in Python ...`, `... in Java ...`
- Principle: `Favor composition over inheritance when behaviors vary independently`
