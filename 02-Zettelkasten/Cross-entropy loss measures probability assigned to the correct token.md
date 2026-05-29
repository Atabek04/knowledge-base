---
created: 2026-05-29
aliases: [cross-entropy loss, cross-entropy, language model loss]
tags:
  - ml/training
  - ml/nlp
---

Cross-entropy loss answers one question: **how much probability did the model give to the correct answer?**

It is the standard [[Loss function - formula that measures how wrong the model is|loss function]] for language models, replacing the Mean Squared Error used in regression.

---

### Formula

```
Loss = -log( probability of correct token )
```

These two things are the same relationship stated differently — "high probability = good" is the goal, and `Loss = -log(p)` is the formula that implements it. When probability is high, `-log(p)` produces a small number (low loss). When probability is low, `-log(p)` produces a large number (high loss). The formula is just a way to turn "how good is the probability?" into a number gradient descent can minimize:

| Probability for correct token | Loss |
|---|---|
| 0.87 (87%) | 0.14 — very low, good |
| 0.45 (45%) | 0.80 — moderate |
| 0.03 (3%)  | 3.50 — high, bad |

Loss of 0 = model was 100% sure of the correct token.
Loss of ∞ = model assigned 0% to the correct token.

---

### How it connects to training

1. [[Softmax converts raw model scores into a probability distribution summing to 100%|Softmax]] turns raw scores → probability distribution
2. Cross-entropy picks out the probability of the correct token
3. [[Gradient adjusts params to reduce loss|Gradient descent]] nudges weights to increase that probability

This is identical in structure to regression: compute loss → compute gradient → update weights.

---

### Interpreting raw loss values

Raw cross-entropy values are hard to interpret alone. The more readable metric is [[Perplexity measures LLM quality as how many words the model effectively considers at each step|perplexity]]:

```
Perplexity = e^(loss)
```

A loss of 1.6 → perplexity ≈ 5 (GPT-4 territory). A loss of 10.8 → perplexity ≈ 50,000 (random model).

---

Read more:
- [[Loss function - formula that measures how wrong the model is]]
- [[Softmax converts raw model scores into a probability distribution summing to 100%]]
- [[Perplexity measures LLM quality as how many words the model effectively considers at each step]]
- [[Gradient adjusts params to reduce loss]]
- [[LLM training uses next-token prediction on existing text to learn statistical patterns]]
