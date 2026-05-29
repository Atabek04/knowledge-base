---
created: 2026-05-29
aliases: [BPE, Byte Pair Encoding, BPE tokenizer]
tags:
  - ml/nlp
  - ai-engineering
---

**Byte Pair Encoding (BPE)** is the algorithm most LLMs use to build their tokenizer vocabulary. It learns which character sequences are common enough to deserve their own token.

---

### How BPE works

1. Start with individual characters: `["u", "n", "b", "e", "l", "i", "e", "v", "a", "b", "l", "e"]`
2. Count all adjacent pairs across the entire training corpus
3. Merge the most frequent pair into a new token
4. Repeat until the vocabulary reaches the target size (~100k tokens)

After many merges, common words become single tokens (`"the"`, `"return"`, `"import"`). Rare words stay split into smaller pieces.

---

### What determines which merges happen

The training corpus. If the model trains on mostly English text, English words get merged first. If it trains on code, `"def"`, `"class"`, `"return"` become single tokens.

This is why [[Each model trains its own tokenizer on its training corpus producing different token splits|each model tokenizes differently]] — BPE reflects the statistical patterns of that model's specific training data.

---

### The result

A fixed vocabulary of subword units. Every possible input text can be represented as a sequence of tokens from this vocabulary — including words that never appeared in training.

---

Read more:
- [[Tokenization splits text into subword units to balance vocabulary size and meaning]]
- [[Each model trains its own tokenizer on its training corpus producing different token splits]]
- [[LLM training uses next-token prediction on existing text to learn statistical patterns]]
