---
created: 2026-05-29
aliases: [tokenization, tokens, subword tokenization]
tags:
  - ml/nlp
  - ai-engineering
---

A **token** is the smallest unit of text an LLM processes. Tokens are not words — they are pieces of words, whole common words, or individual characters depending on frequency.

`"unbelievable"` → `["un", "believ", "able"]` — 3 tokens.

---

### Why not whole words?

Using whole words as tokens creates two problems:

**1. Vocabulary explodes into millions.**

`"run"`, `"runs"`, `"running"`, `"ran"`, `"runner"` are five separate unrelated tokens. The model learns each from scratch with no shared understanding.

**2. Unknown words break the model.**

A word never seen during training has no token. The model is stuck.

---

### Why subwords solve both problems

Subword tokens capture shared meaning through shared pieces:

- `"un-"` always signals negation → model learns it once, applies everywhere
- `"-ing"` always signals ongoing action
- `"-able"` always signals capability

This mirrors the root-word logic in Arabic: ك-ت-ب carries "writing" meaning across كِتَاب, كَاتِب, كَتَبَ. English prefixes/suffixes work the same way.

Unknown words become combinations of known pieces — `"ChatGPT"` → `["Chat", "G", "PT"]`.

---

### Vocabulary size vs compute

[[Softmax converts raw model scores into a probability distribution summing to 100%|Softmax]] must output a probability for every token in the vocabulary. Larger vocabulary = more compute per token prediction.

GPT-4 uses ~100,000 tokens — enough to cover English, code, multiple languages, and emoji efficiently.

---

Read more:
- [[BPE builds a tokenizer vocabulary by iteratively merging the most frequent character pairs]]
- [[Each model trains its own tokenizer on its training corpus producing different token splits]]
- [[Softmax converts raw model scores into a probability distribution summing to 100%]]
- [[LLM training uses next-token prediction on existing text to learn statistical patterns]]
