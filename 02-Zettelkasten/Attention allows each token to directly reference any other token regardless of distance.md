---
created: 2026-06-01
aliases: [attention mechanism, self-attention, attention]
tags:
  - ml/nlp
  - ai-engineering
---

**Attention** is the mechanism that lets each token in a sequence look at every other token simultaneously and decide which ones are relevant to understanding itself.

---

### The problem it solves

Before attention, models (RNNs) processed text one token at a time, left to right, carrying a compressed "hidden state" forward. By token 50, information from token 1 was largely gone — long-range dependencies were impossible to capture reliably.

Attention discards that constraint entirely: every token can directly reference any other token in a single step, regardless of how far apart they are.

---

### How it works (intuition)

Sentence: `"The animal didn't cross the street because it was too tired."`

When the model processes `"it"`, attention assigns a **relevance score** to every other token:

```
"animal"  → high score (tired fits an animal)
"street"  → low score  (streets don't get tired)
"tired"   → high score (directly related)
```

The model then updates `"it"`'s [[Word embeddings map tokens to high-dimensional vectors that encode meaning through context|embedding vector]] by pulling meaning from high-scoring tokens — effectively resolving the reference.

This happens for every token, simultaneously, in every layer.

---

### Self-attention vs cross-attention

**Self-attention**: tokens attend to other tokens in the same sequence (used in the main transformer body).

**Cross-attention**: tokens in one sequence attend to tokens in a different sequence (used in encoder-decoder models for translation).

---

### Why "Attention Is All You Need"

The 2017 paper by Vaswani et al. replaced RNNs entirely with pure attention — no recurrence, no convolution. The title claims attention alone is sufficient to capture all the structure needed for language tasks. Every major LLM (GPT, Claude, Gemini) is built on this architecture.

---

Read more:
- [[Transformers replaced RNNs by processing all tokens in parallel using attention]]
- [[Word embeddings map tokens to high-dimensional vectors that encode meaning through context]]
- [[Neural network layers build increasingly abstract representations of input data]]
