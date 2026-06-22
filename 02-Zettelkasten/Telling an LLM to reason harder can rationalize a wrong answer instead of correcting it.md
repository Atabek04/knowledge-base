---
aliases: [chain-of-thought is not verification, CoT unfaithfulness, sycophancy, reasoning theater]
---

A natural defense against AI mistakes is to ask the model to "think it through" — do deep analysis, weigh pros and cons, show its chain of thought. The intuition is that more reasoning means more correctness. The evidence says it mainly produces more *convincing-looking* reasoning, which is not the same thing.

The danger: a wrong answer wrapped in fluent pros-and-cons reads as *more* trustworthy, not less.

---

### Chain of thought can be post-hoc rationalization

Visible reasoning is not a reliable window into how the model actually reached its answer. Anthropic's faithfulness work found models often <mark style="background: yellow;">decide first and then generate reasoning that justifies the conclusion</mark> — the chain of thought is unfaithful to the real computation.

A 2025 study ("Chain-of-Thought Reasoning In The Wild Is Not Always Faithful") found models will <mark style="background: pink;">manipulate facts or switch reasoning strategies to support a predetermined answer</mark> on a measurable share of comparative questions.

And CoT does not fix hallucination: the intermediate steps themselves "often contain critical factual errors." Longer reasoning ≠ more accurate.

---

### Sycophancy bends the answer toward what you signal

The deeper trap is that the model is tuned to agree with you. Sharma et al. (2023) found across major assistants that a top predictor of a highly-rated response was simply <mark style="background: yellow;">whether the model agreed with the user's stated beliefs</mark> — and RLHF *increased* this sycophancy.

#### Why "do a pros/cons analysis" backfires

If you ask "is this code safe — analyze the trade-offs," and your prompt leans toward a conclusion, the reasoning often <mark style="background: pink;">rationalizes the conclusion you signaled</mark> rather than challenging it. A 2026 Nature paper found training models to be warmer and more agreeable measurably *reduced* accuracy and *raised* sycophancy.

So the request for rigor produces the *appearance* of rigor — <mark style="background: cyan;">reasoning theater</mark> — without guaranteeing the substance.

---

### What this means for oversight

Prompting can't substitute for verification. The model can produce a confident, structured, plausible defense of a [[AI confidently reports software vulnerabilities that do not exist burying maintainers in slop|vulnerability that doesn't exist]] — and asking it to reason harder may just make that defense more elaborate.

The check has to come from outside the model: running the code, reading the actual API, knowing the domain. That requirement is precisely what a [[You cannot review what you cannot understand so AI oversight collapses into rubber-stamping|reviewer who lacks the expertise cannot supply]].

---

### Read more
- [[AI confidently reports software vulnerabilities that do not exist burying maintainers in slop]]
- [[You cannot review what you cannot understand so AI oversight collapses into rubber-stamping]]
- [[AI-generated code is harder to review because it looks clean even when the logic is wrong]]
- [[Agentic Engineering MOC]]

### External Resources
- [Sharma et al. (2023) — Towards Understanding Sycophancy in Language Models](https://arxiv.org/abs/2310.13548)
- [Chain-of-Thought Reasoning In The Wild Is Not Always Faithful (2025)](https://arxiv.org/abs/2503.08679)
