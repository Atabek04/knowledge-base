---
created: 2026-06-01
aliases: [embeddings, word embeddings, embedding vectors]
tags:
  - ml/nlp
  - ai-engineering
---

An LLM is a math machine — it only computes numbers. But words are text.

**Embeddings** solve this by mapping each token to a list of hundreds or thousands of numbers called an **embedding vector**. This isn't arbitrary encoding like ASCII — it encodes *meaning*.

---

### How meaning ends up in numbers

Nobody defines what each number in the vector means. The model starts with random vectors and adjusts them during training via [[Backpropagation propagates gradients backward through layers using the chain rule|backpropagation]].

Words that appear in similar contexts get nudged toward similar vectors. After training on billions of sentences, the vectors capture real relationships:

```
king - man + woman ≈ queen
Paris - France + Italy ≈ Rome
```

`"king"` and `"queen"` end up with nearly identical vectors except along dimensions the model learned to associate with gender.

---

### Context reshapes embeddings

A static embedding table gives each token one fixed vector. But meaning changes with context:

- `"bank"` near `"river"` → different vector than `"bank"` near `"money"`

This context-sensitive adjustment happens inside the [[Neural network layers build increasingly abstract representations of input data|layers]] through the [[Attention allows each token to directly reference any other token regardless of distance|attention mechanism]] — each layer refines the token's representation based on surrounding tokens.

---

### Why this matters for inference

When you send a prompt, every token is converted to its embedding vector first. Those vectors carry meaning into the network — the layers compute on them, not on raw text.

The prompt itself is the "customization" — different prompts produce different vectors → different layer activations → different generated output.

---

Read more:
- [[Attention allows each token to directly reference any other token regardless of distance]]
- [[Tokenization splits text into subword units to balance vocabulary size and meaning]]
- [[Neural network layers build increasingly abstract representations of input data]]
- [[Backpropagation propagates gradients backward through layers using the chain rule]]
- [[LLM training uses next-token prediction on existing text to learn statistical patterns]]
