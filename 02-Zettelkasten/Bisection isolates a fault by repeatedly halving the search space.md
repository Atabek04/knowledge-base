---
created: 2026-06-24
tags: [debugging/method]
aliases: [bisection, binary search debugging, halving the search space]
---

When a fault is hiding *somewhere* in a large space — 1000 lines, 200 commits, a ten-stage data pipeline — checking each point one at a time is O(n) and brutal. Bisection cuts that to O(log n) by halving the space on every test instead of stepping through it.

The name says the method: <mark style="background: #FFF3A3A6; font-weight: bold;">**bi-section** — cut the suspect range in two, decide which half holds the fault, discard the other half, repeat.</mark>

---

### How it works

1. Find a **known-good** point and a **known-bad** point — the fault lies between them.
2. Test the **midpoint**.
3. The result tells you which half the fault is in → throw the other half away.
4. Repeat on the surviving half until the range is one point.

Each test deletes half the remaining suspects, so a space of 1000 collapses in ~10 tests, and <mark style="background: #BBFABBA6;">20 commits resolve in about 5 tests</mark> (log₂ 20 ≈ 4.3).

---

#### Where it applies

- **Commits** — find a good and bad commit, test the middle one. `git bisect` automates exactly this.
- **A data pipeline** — at which stage does the value first go wrong? Inspect the midpoint stage.
- **Code** — comment out half the function; does the bug survive? That half is innocent.
- **Config / dependencies** — bisect which changed setting or version bump broke the build.

---

### Why it's an instance of the scientific method

Each midpoint test is one cycle of [[Debug by the scientific method observe hypothesize test repeat|observe → hypothesize → test]]: the hypothesis is "the fault is in this half," and the midpoint result confirms or refutes it. <mark style="background: #ADCCFFA6;">Bisection is just that loop applied to a linearly-ordered search space.</mark>

---

### Read more
- [[Debug by the scientific method observe hypothesize test repeat]]
- [[Differential debugging asks what changed since the system last worked]]
- [[Debugging & Troubleshooting - MOC]]
