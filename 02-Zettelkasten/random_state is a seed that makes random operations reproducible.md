---
created: 2026-02-16
aliases: [random_state, Random Seed]
tags:
  - ml/fundamentals
---

> `random_state` is a **seed** for the random number generator — same seed always produces the same result.

Many ML operations involve randomness: shuffling data before splitting, initializing weights, sampling rows. [[Computers generate pseudorandom numbers using a formula not true randomness|Computers don't generate true randomness]] — they use a formula that needs a starting number. Without a fixed seed, Python picks one from the system clock — so every run shuffles differently, producing different accuracy scores. You can't tell if a change in results came from your code or just a different split.

```python
# Different shuffle each run
train_test_split(X, y, test_size=0.2)

# Same shuffle every run
train_test_split(X, y, test_size=0.2, random_state=42)
```

The number itself (1, [[42 is not a special seed it is just a convention from pop culture|42]], 123) doesn't matter — it just picks a specific shuffle order. What matters is: **same seed = same output.**

### Why does this matter?

The model works fine either way — randomness doesn't hurt accuracy. The problem is for **you as the developer**.

Without a fixed seed, you can't tell if a change in results came from your code or just a different shuffle. A fixed seed gives you three things:

- **Debugging** — if there's a problem, you can reproduce it exactly
- **Fair comparison** — you compare model versions on identical data splits
- **Sharing code** — others can run your code and get your exact results

<mark style="background: pink/red">Without reproducibility, debugging and comparing experiments becomes guesswork.</mark>

<mark style="background: green">Use a fixed `random_state` during development so your results are reproducible and comparable across experiments.</mark>

---

Read more:
- [[Computers generate pseudorandom numbers using a formula not true randomness]]
- [[42 is not a special seed it is just a convention from pop culture]]
- [[Train-test split evaluates model performance on unseen data]]
- [[Machine Learning MOC]]
