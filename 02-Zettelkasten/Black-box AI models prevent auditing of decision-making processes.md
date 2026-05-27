---
aliases: [black-box problem, black-box AI]
---

A black-box model is one where inputs and outputs are observable but the internal reasoning process is not.

Modern deep learning models — especially large transformer-based systems — are black boxes in this sense. We can observe that a model produces an output; we cannot trace *why* it produced that output at the level of human-understandable logic.

This matters in three distinct ways:

**Scientific:** We cannot verify whether the model is reasoning or pattern-matching. Correct outputs give no evidence of correct process.

**Practical:** When a model fails — a misdiagnosis, a biased loan decision, a dangerous autonomous action — there is no decision trail to audit, debug, or fix reliably.

**Safety:** An opaque system that performs well on known distributions may behave unpredictably on novel inputs, and we have no tools to detect this in advance.

Geoffrey Hinton's post-2023 concern is precisely this: LLMs may be doing more than we realize, and we have no way to verify what that is — in either direction.

---

### Read more

- [[Mechanistic interpretability reverse-engineers neural network computations into readable circuits]]
- [[LeCun argues LLMs lack world models needed for general intelligence]]
- [[Turing Test replaces the question of machine thinking with behavioral indistinguishability]]
