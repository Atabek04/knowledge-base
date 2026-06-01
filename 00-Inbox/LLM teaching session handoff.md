---
created: 2026-06-01
tags: [inbox, handoff]
---

Resume the `/teach LLM` Socratic session. Context below.

---

### What was covered (all notes + flashcards created)

1. **Core trick** — LLMs predict next token using probability over full vocabulary
2. **Training** — cross-entropy loss, softmax, backprop, gradient descent, perplexity
3. **Layers** — hierarchical abstraction, brain analogy clarified
4. **Tokens** — subword tokenization, BPE, why models tokenize differently
5. **Embeddings** — tokens → high-dimensional vectors, meaning learned automatically, `king - man + woman ≈ queen`
6. **Attention + Transformers** — RNN problem, attention mechanism, "Attention Is All You Need" paper

### Stopped at

Mid-chunk: **Transformers & Attention** was explained verbally but the Socratic sequence wasn't fully completed. Chunk boundary was not reached — student left for urgent tasks before confirming understanding or getting the comprehension check.

### Resume plan

1. Quick check on attention: ask student to explain in their own words how `"it"` in "The animal was tired" gets resolved — confirm chunk is solid
2. Then continue to **Chunk 5 — Inference**: how a prompt becomes a response token by token, why the model can write essays/code it's never seen, how the prompt IS the customization
3. Then **Chunk 6 — Context window**
4. Then **Chunk 7 — Temperature**

### Student profile

- Complete beginner to LLMs and transformers
- Has prior knowledge: linear regression, gradient descent, loss functions, weights, backprop from ML course
- Learns well when new concepts are bridged to regression analogies
- Asks good "why" questions — engage them, don't skip
- Arabic speaker — root-word analogy worked well for tokenization

### Notes location

All atomic notes: `02-Zettelkasten/`
Flashcards appended to: `05-Flashcards/ml/model-training.md`
MOCs updated: `01-MOCs/AI-ML/Machine Learning MOC.md` and `01-MOCs/AI-ML/AI Engineering MOC.md`
