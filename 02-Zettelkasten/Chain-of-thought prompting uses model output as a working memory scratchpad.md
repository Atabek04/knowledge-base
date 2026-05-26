---
aliases: [chain-of-thought, CoT, CoT prompting]
---

Chain-of-thought (CoT) prompting, introduced by Wei et al. (2022), discovered that appending "let's think step by step" to a prompt dramatically improves LLM performance on reasoning tasks.

The mechanism: generating intermediate steps forces the model to allocate more tokens before committing to an answer. Each intermediate token becomes part of the context, giving the model a longer "runway" of working state before the final answer.

This is not a new architecture — it is the same autoregressive prediction running longer. The model uses its own generated text as an external working memory, similar to writing notes on paper before concluding.

Performance on math, logic, and multi-step questions improves substantially. The question debated in research is *why*:

- **Elicited reasoning view:** the model performs genuine intermediate reasoning, and CoT unlocks it
- **Constrained imitation view:** the model imitates the *form* of step-by-step reasoning it saw in training data (textbooks, worked solutions) without performing the underlying logic

The distinction matters because imitation generalizes only within the training distribution — it breaks on genuinely novel problem structures, even when the individual steps are familiar.

---

### Read more

- [[Autoregressive token prediction generates responses in a single forward pass without deliberation]]
- [[Reasoning models use reinforcement learning on outcome rewards to discover thinking strategies]]
- [[Chain-of-thought in LLMs may be constrained imitation of human reasoning patterns rather than genuine inference]]
- [[Chollet's ARC benchmark exposes the gap between pattern memorization and genuine reasoning]]
