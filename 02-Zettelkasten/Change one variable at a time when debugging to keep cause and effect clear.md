---
created: 2026-06-24
tags: [debugging/mindset]
aliases: [change one variable at a time, isolate variables]
---

When a bug is stubborn, the temptation is to change several things at once and re-run — bump a timeout, add a null check, tweak a config — hoping the bug disappears. It often does. But now you have a worse problem: you don't know *which* change fixed it, or whether one change introduced a new bug that simply masks the old one.

The rule borrowed from controlled experiments: <mark style="background: #FFF3A3A6; font-weight: bold;">change exactly one variable per test and hold everything else constant.</mark>

---

### Why multiple changes lie to you

Say you change A and B together and the bug is gone. What do you actually know?

- maybe A fixed it and B did nothing
- maybe B fixed it and A did nothing
- maybe neither fixed it and B introduced a *different* bug that hides the symptom

<mark style="background: #FF5582A6; font-weight: bold;">All three look identical from the outside.</mark> The changes are *confounded* — their effects can't be told apart. One change at a time keeps a clean line from cause to effect.

---

#### This is the discipline that makes the scientific method work

[[Debug by the scientific method observe hypothesize test repeat|The scientific loop]] only gives clean signal if each experiment tests one thing. The moment a test varies two factors, its result stops ruling anything in or out — you've spent a run and learned nothing decisive.

---

### Cost vs benefit

| | One change at a time | Many changes at once |
|---|---|---|
| Speed per step | slower | faster |
| Signal per step | <mark style="background: #ADCCFFA6;">clean — you know what did it</mark> | ambiguous |
| Risk | low | masks bugs, adds new ones |

The per-step slowness is real, but it's almost always cheaper than re-debugging a bug you thought you fixed.

---

### Read more
- [[Debug by the scientific method observe hypothesize test repeat]]
- [[Bisection isolates a fault by repeatedly halving the search space]]
- [[Debugging & Troubleshooting - MOC]]
