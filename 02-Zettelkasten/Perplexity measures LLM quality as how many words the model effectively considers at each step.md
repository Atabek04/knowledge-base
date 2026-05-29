---
created: 2026-05-29
aliases: [perplexity, PPL, language model perplexity]
tags:
  - ml/nlp
  - ai-engineering
---

Perplexity (PPL) is the standard metric for evaluating language model quality. It answers: **how "confused" is the model when predicting the next token?**

Intuitively: if perplexity = 10, the model is effectively choosing between 10 equally likely words at each step.

---

### Formula

```
Perplexity = e^(average cross-entropy loss)
```

It is the exponentiated form of [[Cross-entropy loss measures probability assigned to the correct token|cross-entropy loss]], scaled into a more interpretable number.

---

### Reference values

| State | Loss | Perplexity |
|---|---|---|
| Untrained / random | ~10.8 | ~50,000 (full vocab size) |
| Poor model | ~3.5 | ~33 |
| GPT-4 level | ~1.6 | 5–15 |
| Perfect | 0 | 1 |

A random model has perplexity equal to the vocabulary size — it gives every word equal probability.
State-of-the-art LLMs achieve single-digit perplexity on standard benchmarks.

---

### Why perplexity instead of raw loss?

Raw cross-entropy values (0.14, 3.5) have no intuitive meaning.

Perplexity converts those numbers into "how many words was the model choosing between?" — a concrete, comparable scale.

Lower perplexity = model is more confident in the right answer = better.

---

Read more:
- [[Cross-entropy loss measures probability assigned to the correct token]]
- [[LLM training uses next-token prediction on existing text to learn statistical patterns]]
- [[Autoregressive token prediction generates responses in a single forward pass without deliberation]]
