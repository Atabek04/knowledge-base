---
created: 2026-06-24
tags: [debugging/method]
aliases: [scientific method debugging, hypothesis-driven debugging]
---

The slowest way to debug is to change things at random — "try this, try that" — because you alter the system without knowing whether the change matters. Treating a bug as a science experiment makes every step measurable: each test rules a cause in or out, so the search space only ever shrinks.

The method is the same one from school science class: <mark style="background: #FFF3A3A6; font-weight: bold;">observe → hypothesize → predict → test → repeat.</mark>

---

### The loop

1. **Observe** — gather the facts: the error, the inputs, what changed, the logs.
2. **Hypothesize** — state one falsifiable claim about the cause.
3. **Predict** — "if that's true, then I should see X."
4. **Test** — run the smallest experiment that checks the prediction.
5. **Update** — confirmed or refuted, you now know more. Loop.

---

#### A hypothesis must be falsifiable

A useful hypothesis is one a single test can *disprove*:

> "The `NullPointerException` happens because `user` is null when the cache misses."

That predicts something concrete — a null `user` on a cache miss — which a log line or breakpoint can confirm or kill in one run. <mark style="background: #FF5582A6; font-weight: bold;">"Something's wrong with the cache" is not a hypothesis</mark> — nothing can refute it, so it can't guide a test.

---

### Why it beats guessing

Every experiment partitions the possibilities: the bug is either in *this* half or the other. Random edits don't partition anything — a fix that "works" leaves you unsure *what* worked or whether you just hid the bug.

This is the engine underneath the more specific methods: [[Change one variable at a time when debugging to keep cause and effect clear|changing one variable at a time]] keeps each experiment clean, and [[Bisection isolates a fault by repeatedly halving the search space|bisection]] is just this loop applied to a search space.

---

### Read more
- [[Change one variable at a time when debugging to keep cause and effect clear]]
- [[Bisection isolates a fault by repeatedly halving the search space]]
- [[Read the error message literally before forming any theory]]
- [[Debugging & Troubleshooting - MOC]]
