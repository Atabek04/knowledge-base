---
created: 2026-05-29
aliases: [LLM training, next-token prediction training, language model training]
tags:
  - ml/nlp
  - ml/training
  - ai-engineering
---

An LLM learns by reading existing text — books, articles, code, internet — and repeatedly answering one question: *given all the words so far, what word comes next?*

Nobody labels the data manually. The correct answer is already there: it is the word that actually appeared next in the original text.

---

### How it mirrors linear regression

In [[Simple linear regression predicts a target using one feature and a straight line|linear regression]], the model predicts a number (house price) from features (size, rooms).

In LLM training the same structure applies:

| Regression | LLM training |
|---|---|
| Features | All tokens before the blank |
| Target | The next token in the original text |
| Loss | [[Cross-entropy loss measures probability assigned to the correct token\|Cross-entropy]] |
| Weight update | [[Gradient adjusts params to reduce loss\|Gradient descent]] |

The difference: instead of outputting one number, the model outputs a [[Softmax converts raw model scores into a probability distribution summing to 100%\|probability distribution]] over every word in the vocabulary (~50,000 words).

---

### Training loop

1. Feed the model a sequence of tokens: `"The sky is"`
2. Model outputs a probability for every word in the vocabulary
3. Compute [[Cross-entropy loss measures probability assigned to the correct token|cross-entropy loss]] — how much probability did the correct word `"blue"` get?
4. [[Backpropagation propagates gradients backward through layers using the chain rule|Backpropagation]] nudges all weights to increase that probability next time
5. Repeat for hundreds of billions of tokens

After training, the weights are frozen. No training happens when you ask a question.

---

### What the model actually "learns"

The model does not store facts. It stores [[Neural network weights are compressed statistical patterns not human-readable instructions|compressed statistical patterns]] in billions of weights. The appearance of knowledge is a side effect of those patterns.

---

Read more:
- [[Autoregressive token prediction generates responses in a single forward pass without deliberation]]
- [[Softmax converts raw model scores into a probability distribution summing to 100%]]
- [[Cross-entropy loss measures probability assigned to the correct token]]
- [[Backpropagation propagates gradients backward through layers using the chain rule]]
- [[Simple linear regression predicts a target using one feature and a straight line]]
- [[Neural network weights are compressed statistical patterns not human-readable instructions]]
- [[Gradient adjusts params to reduce loss]]
