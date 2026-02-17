---
created: 2026-02-17
aliases: [Classification]
tags:
  - ml/classification
---

> **Classification** predicts a <mark style="background: yellow">discrete category</mark> — which group does this belong to.

---

### What "classification" means in English

To **classify** means to **sort things into groups**. A librarian classifies books by genre. A doctor classifies a tumor as malignant or benign.

In ML, the model looks at input features and decides **which category** the data belongs to.

---

### What makes it classification

The output is a **label from a fixed set of choices**:
- Spam / Not spam (2 classes → binary classification)
- Cat / Dog / Bird (3+ classes → multiclass classification)
- Positive / Negative / Neutral (sentiment)

<mark style="background: #FFB8EBA6;">If the answer is "which one" or "what type" → it's classification.</mark>

The model doesn't just pick a category — it outputs [[Classification outputs probability scores to express confidence in predictions|probability scores]] expressing how confident it is in each choice.

---

### Regression vs Classification

| | Regression | Classification |
|---|---|---|
| Output | Continuous number | Discrete category |
| Question | How much? | Which one? |
| Example | House price = $250,000 | Email = spam |

---

Read more:
- [[Supervised learning means the model learns from labeled data with known answers]]
- [[Regression predicts a continuous number]]
- [[Classification outputs probability scores to express confidence in predictions]]
