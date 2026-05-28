---
aliases: [Interleaving, interleaved practice, contextual interference]
created: 2026-05-28
tags: [learning, study-method, practice, retention]
---

### What it is

Interleaving is the practice of mixing different problem types or topics within a single study session — in contrast to blocked practice (exhausting one type before moving to the next).

<mark style="background: yellow">Interleaved practice hurts short-term performance and dramatically improves long-term transfer.</mark>

---

### The mechanism: contextual interference effect

During **blocked practice**: the correct strategy stays loaded in working memory for the entire block. You execute, not decide.

During **interleaved practice**: you must first *identify* what type of problem you're facing, *retrieve* the right strategy from long-term memory, then *execute*. Three cognitive operations instead of one.

This forced strategy selection is harder but builds durable discrimination ability — knowing *which* tool to reach for, not just how to use a tool you've already identified.

Three contributing mechanisms:
1. **Elaboration through comparison** — contrasting similar problems highlights distinctions
2. **Reconstruction** — forgetting and re-retrieving the solution plan each time strengthens it
3. **Attention shift** — noticing what differs between problem types builds pattern recognition

---

### Research evidence

- Kornell & Bjork (2008): interleaved art-style study → 65% accuracy on transfer vs 50% blocked
- 2020 classroom study: interleaved math students scored **61% on a 1-month delayed test** vs **37% for blocked**
- Contextual interference effect replicated across motor skills, mathematics, language

---

### The fluency illusion

During blocked practice, learners feel more competent — the answer is still in working memory.

<mark style="background: pink">This feeling is not accuracy.</mark> Researchers found "the feeling of fluency during blocked practice was so strong it overrode direct evidence of failure."

This is why interleaving feels wrong at first. It is supposed to feel harder — that is the mechanism.

---

### Critical caveat

Interleaving works best once you have basic familiarity with each problem type.

Complete beginners should use a short blocked phase (3–5 problems per category) before switching to interleaved sessions. Pure beginners need some schema before they can benefit from discrimination pressure.

---

### Application to LeetCode and programming

**Don't do:** 50 array problems → 50 two-pointer problems → 50 graph problems.

This builds execution fluency *within* category, not recognition *across* problems.

**Do this instead:**
- Use NeetCode 150's topic groupings for short blocked acquisition (3–5 problems per pattern)
- Then switch to cross-topic mixed sessions
- A single session: one sliding window + one BFS + one binary search variant

For system design: mix one rate-limiter, one database sharding, one API design in a single session — not three consecutive database problems.

---

Read more:
- [[Desirable difficulties make learning harder in ways that improve long-term retention over short-term fluency]]
- [[Retrieval practice strengthens memory by recalling information rather than re-reading it]]
- [[Deliberate practice builds expert mental representations through focused effort at the edge of current ability]]
