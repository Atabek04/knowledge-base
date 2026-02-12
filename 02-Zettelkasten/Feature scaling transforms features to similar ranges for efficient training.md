---
created: 2026-02-12
aliases: [Feature Scaling]
tags:
  - ml/preprocessing
---

> **Feature scaling** is transforming features to similar numerical ranges.
> ⚠️ That's why **Feature scaling** only applies to **numerical features**.

Here "scaling" means **changing the measurement scale** — not making values bigger. You're re-expressing values on a new scale, like converting Celsius to Fahrenheit.

Our features have different scales:
- Age: 18-65
- Income: $20,000-$200,000
- Years of experience: 0-40

---

### Why it matters

When features have different scales, [[Unscaled features cause learning rate conflict in gradient descent|the learning rate can't work well for all features at once]].

Feature scaling solves this by making all gradients comparable in size, so one learning rate works efficiently for all features.

---

### Before and after

| | Unscaled | Scaled |
|---|---|---|
| Learning rate | 0.0000008 | 1.5 |
| Iterations to converge | 9+ (still bouncing) | 5 (done) |
| Oscillation? | Yes — bounces above and below | No — smooth approach |
| Error pattern | -200k → +120k → -72k → +43k... | -300k → -75k → -19k → -5k → -1k |

<mark style="background: yellow">Feature scaling isn't about whether the model **can** learn — it's about learning **efficiently and stably**.</mark>

---

### Two main methods

- [[Normalization scales features to a fixed range using min and max]]
- [[Standardization centers features around zero using mean and standard deviation]]

---

Read more:
- [[Unscaled features cause learning rate conflict in gradient descent]]
- [[Oscillation happens when gradient overcorrects and bounces around the optimal value]]
- [[Normalization scales features to a fixed range using min and max]]
- [[Standardization centers features around zero using mean and standard deviation]]
- [[Feature is an input variable the model uses to make predictions]]
