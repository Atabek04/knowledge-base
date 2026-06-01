---
created: 2026-06-01
aliases: [Transformer architecture, Transformer, RNN vs Transformer]
tags:
  - ml/nlp
  - ai-engineering
---

The **Transformer** is the neural network architecture introduced in the 2017 paper *"Attention Is All You Need"* (Vaswani et al.). It powers every major LLM — GPT, Claude, Gemini, Llama.

---

### What came before: RNNs

**RNNs (Recurrent Neural Networks)** processed text one token at a time, left to right. Each step produced a hidden state passed to the next step — like a running summary.

Problems:
- Information from early tokens faded by later tokens (vanishing gradient)
- Sequential processing — token N couldn't start until token N-1 finished → slow
- Long-range dependencies were unreliable

---

### What Transformers changed

Transformers process all tokens **in parallel**. Instead of a left-to-right pipeline, every token attends to every other token simultaneously via [[Attention allows each token to directly reference any other token regardless of distance|self-attention]].

| | RNN | Transformer |
|---|---|---|
| Processing | Sequential (one by one) | Parallel (all at once) |
| Long-range memory | Fades over distance | Direct access to all tokens |
| Training speed | Slow (sequential) | Fast (parallelizable on GPU) |
| Architecture | Hidden state | Attention + feed-forward layers |

---

### Transformer structure (simplified)

Each layer in a Transformer has two sub-components:

1. **Self-attention** — tokens look at each other, update their [[Word embeddings map tokens to high-dimensional vectors that encode meaning through context|embeddings]] based on context
2. **Feed-forward network** — each token's updated embedding passes through a small neural network independently

This repeats across all layers (GPT-3: 96 layers). Each pass builds more abstract understanding.

---

Read more:
- [[Attention allows each token to directly reference any other token regardless of distance]]
- [[Neural network layers build increasingly abstract representations of input data]]
- [[Word embeddings map tokens to high-dimensional vectors that encode meaning through context]]
- [[LLM training uses next-token prediction on existing text to learn statistical patterns]]
