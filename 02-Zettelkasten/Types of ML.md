---
created: 2026-01-22
tags:
  - ml/fundamentals
  - ml/types
---

> All ML works by **learning from data**.
> But they differ in **what kind of guidance** (instructions) they get while learning.

---
### Labeled & Unlabeled data

**Labeled** - each data point **comes with a *correct answer*** or label
- Email text ⇾ `spam`/`not_spam`
- Image ⇾ `cat`/dog 

**Unlabeled** - data points don't have any correct answers attached.

---
### Supervised Learning

You give the system **labeled examples** (input + correct answer)
It learns to map inputs to outputs, by finding patterns.

You train with `X -> Y`

---
### Unsupervised Learning

You give the system unlabeled data
It finds hidden patterns or groups on its own.

You train with `X` only (no `Y`)

---

### Reinforcement Learning

The system learns by `trial-and-error`
Getting reward for good actions
Penalties for bad ones

---

Read more:
- [[Differences of - AI, ML, DL, GenAI]]
- [[Regression and Classification]]