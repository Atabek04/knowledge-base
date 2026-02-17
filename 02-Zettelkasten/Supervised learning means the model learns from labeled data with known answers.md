---
created: 2026-02-17
aliases: [Supervised Learning]
tags:
  - ml/fundamentals
---

> **Supervised learning** is when a model learns from examples where the <mark style="background: yellow">correct answer is already known</mark>.

---

### Where the name comes from

"Supervised" in English means someone is **watching over and guiding** you — like a supervisor at work who corrects your mistakes.

Same idea here. During training, you show the model examples with the right answer attached. The model predicts, gets corrected, and improves.

The "supervisor" is the **labeled data** — the [[Target is the output variable the model learns to predict|target column (y)]] that tells the model what the correct output should be for each input.

---

### What "labeled data" means

Each row in your dataset has:
- **Input features (X)** — what the model sees
- **A label (y)** — the correct answer

Without labels, the model has no one to learn from — that's [[Unsupervised learning finds patterns in data without predefined labels|unsupervised learning]].

---

### Two types of supervised learning

- [[Regression predicts a continuous number|Regression]] — predict a continuous number (price, temperature)
- [[Classification predicts a discrete category|Classification]] — predict a category (spam/not spam, cat/dog)

---

Read more:
- [[Target is the output variable the model learns to predict]]
- [[X represents features and y represents target in ML notation]]
- [[Regression predicts a continuous number]]
- [[Classification predicts a discrete category]]
