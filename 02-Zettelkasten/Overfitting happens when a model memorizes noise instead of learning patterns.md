---
created: 2026-03-27
aliases: [Overfitting]
tags:
  - ml/fundamentals
---

> **Overfitting** happens when a model learns not only the true patterns but also the **noise** in the training data.

The classic sign: high accuracy on training data, poor accuracy on test data. The model memorized the training examples instead of learning generalizable patterns — like a student who memorizes exam answers but can't solve new problems.

### Why it happens

The model is too complex for the amount of data it has. It starts fitting to random fluctuations (noise) that don't exist in new data.

<mark style="background: pink/red">A model that scores 99% on training but 60% on test is not a good model — it's an overfitted one.</mark>

### How the test set helps

The [[Train-test split evaluates model performance on unseen data|test set]] acts as a reality check. Since the model never saw this data during training, poor test performance exposes overfitting early — before the model reaches production.

<mark style="background: green">Always compare training accuracy vs test accuracy. A large gap between them is a red flag for overfitting.</mark>

---

Read more:
- [[Train-test split evaluates model performance on unseen data]]
- [[Machine Learning MOC]]
