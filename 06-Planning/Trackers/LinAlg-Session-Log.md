---
created: 2026-09-04
tags: [tracker, linear-algebra]
---

One line per math session, appended by the `math-professor` skill. This file is the **single
source of truth**. The Wall Tracker checkbox and the weekly-plan checkbox in the Ribaat vault
are views of it, and when they disagree the log wins.

Roadmap → [[Linear Algebra MOC]]

---

## Field format

```
DATE | SECTION | MINUTES | attempted N / correct N | slips N | misc: TAG | gap: NODE | cards N | done: § or - | next: THE FIRST MOVE
```

- **misc** carries a misconception tag from the skill's fifteen-item table, or `none`.
- **gap** names the prerequisite node backed up to, or `none`.
- **done** carries a section number only when all four exit conditions are met, otherwise `-`.
- **next** is an implementation intention, concrete enough to start without thinking. "§1.5 ex 11, closed-book" is valid. "Continue" is not.

Two boxes, two meanings. The Wall Tracker box is ticked only on `done:`. The weekly-plan box
is ticked for any dose at or above the twenty-minute floor.

---

## Weekly roll-up, Fridays

Count sections done, cards made, misconception tags that recurred twice or more, and days at
minimum dose. A tag recurring twice earns a contrastive card and a fresh relearn slot. Two
consecutive minimum-dose days trigger the Deal.

---

## Sessions

| Date | Section | Min | Attempted / correct | Slips | Misconception | Gap | Cards | Done | Next |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |

---

## Relearn slots

Each closed section gets a fresh exercise at +3, +10 and +30 days, closed-book. Correct
advances the slot. Wrong triggers triage and resets it to +3.

| Section | +3 due | +10 due | +30 due | Status |
|---|---|---|---|---|
| | | | | |

---

## Deferrals

Topics parked mid-session, each with the section that triggers picking it back up.

| Deferred | Trigger section | Raised |
|---|---|---|
| | | |
