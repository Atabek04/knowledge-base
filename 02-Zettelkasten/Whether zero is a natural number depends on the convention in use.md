---
created: 2026-09-05
tags: [math, foundations, number-systems, convention]
aliases: [is zero natural, zero in N]
---

"Is zero a natural number?" looks like a question with a right answer. It is not. Two established conventions disagree, both are correct inside their own tradition, and a learner who met only one of them will think the other is a mistake.

Knowing that the split exists is the actual knowledge here.

---

### The two conventions

<b>Integer: yes, always.</b> <mark style="background: #FFF3A3A6;">Zero is an integer under every convention — the argument is only ever about whether it belongs to ℕ.</mark>

<mark style="background: #FF9E9EA6;">Whether ℕ starts at 0 or at 1 is a convention, not a fact — two established traditions disagree and both are correct inside their own.</mark>

- <b>ℕ starts at 0</b> — the ISO 80000-2 standard, set theory, logic, and computer science. Counting a collection that might be empty makes 0 the natural base case, and array indices start there for the same reason.
- <b>ℕ starts at 1</b> — most school curricula, which call 0 a "whole number" instead. Here "natural" means the numbers you count objects with, and you do not start counting at zero.

Neither camp is wrong. They are answering slightly different questions about what "natural" was ever supposed to mean.

---

### How to write it unambiguously

When it matters, do not rely on the reader sharing your convention — say it in the symbol:

```
ℕ₀     naturals including 0     {0, 1, 2, 3, …}
ℕ⁺     naturals excluding 0     {1, 2, 3, …}
```

<mark style="background: #ADCCFFA6;">Write ℕ₀ or ℕ⁺ whenever the reader might not share your convention — ISO 80000-2 defines exactly this pair so technical writing never has to guess.</mark>

In practice: check what your own textbook declares in its opening pages, and use that consistently for the rest of the book. The convention is a local setting, not a global truth.

---

### Read more

- [[Each number system patches a hole the previous one could not express]]
- [[Math Foundations MOC]]
