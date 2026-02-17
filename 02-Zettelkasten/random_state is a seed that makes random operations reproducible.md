---
created: 2026-02-16
aliases: [random_state, Random Seed]
tags:
  - ml/fundamentals
---

> `random_state` is a **seed** for the random number generator — same seed always produces the same result.

Many ML operations involve randomness: shuffling data before splitting, initializing weights, sampling rows. Without a fixed seed, Python picks a new random seed each run (based on system time) — so every run shuffles differently, producing different accuracy scores. You can't tell if a change in results came from your code or just a different split.

```python
# Different shuffle each run
train_test_split(X, y, test_size=0.2)

# Same shuffle every run
train_test_split(X, y, test_size=0.2, random_state=42)
```

The number itself (1, 42, 123) doesn't matter — it just picks a specific shuffle order. What matters is: **same seed = same output.**

<mark style="background: green">Use a fixed `random_state` during development so your results are reproducible and comparable across experiments.</mark>

---

Read more:
- [[Train-test split evaluates model performance on unseen data]]
- [[Machine Learning MOC]]
