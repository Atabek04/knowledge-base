---
aliases: [inference scaling, test-time compute, inference-time compute]
---

Traditional scaling in deep learning means more parameters and more training compute → better models.

Reasoning models introduced a second axis: **inference-time compute scaling**. The model spends more tokens during generation — thinking longer — and accuracy on hard tasks improves as a result.

This is analogous to a human being given more time to work through a difficult problem before answering.

The practical trade-off: reasoning traces are 3–5× longer than a standard GPT-4o response on the same prompt. For hard math or code, they can be orders of magnitude longer. Token cost scales with problem difficulty.

OpenAI reports that o3 used 10× more training compute than o1, but also that o3 can allocate substantially more inference compute per query. These are additive gains.

This represents a shift in how AI capability is understood: model quality is no longer determined by size alone, but by the combination of parameter count, training compute, and inference budget.

---

### Read more

- [[Reasoning models use reinforcement learning on outcome rewards to discover thinking strategies]]
- [[Thinking tokens create a bounded scratchpad that separates deliberation from final output]]
- [[Autoregressive token prediction generates responses in a single forward pass without deliberation]]
