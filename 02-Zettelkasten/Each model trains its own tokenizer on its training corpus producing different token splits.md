---
created: 2026-05-29
aliases: [model tokenizers differ, tokenizer differences]
tags:
  - ml/nlp
  - ai-engineering
---

Different LLMs tokenize the same text differently because each model trains its own tokenizer on its own training data using [[BPE builds a tokenizer vocabulary by iteratively merging the most frequent character pairs|BPE]].

The tokenizer is not shared between models — it is a trained artifact specific to each model.

---

### Why this matters

The same sentence fed to GPT-4 and Llama 3 produces different token sequences with different token counts.

Token count directly affects:
- **Cost** — APIs charge per token
- **Context window usage** — a 128k context window means 128k tokens, not words
- **Speed** — more tokens = more forward passes = slower generation

---

### What drives the differences

| Factor | Effect |
|---|---|
| Training corpus language mix | Languages seen more → their words get single tokens |
| Code vs prose ratio | Code keywords (`def`, `return`) may become single tokens |
| Target vocabulary size | GPT-4: ~100k · Llama 3: ~32k · different granularity |

A model trained on mostly English will split Arabic or Chinese text into many small tokens, using context window space inefficiently for those languages.

---

Read more:
- [[BPE builds a tokenizer vocabulary by iteratively merging the most frequent character pairs]]
- [[Tokenization splits text into subword units to balance vocabulary size and meaning]]
