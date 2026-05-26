---
aliases: [neural network weights, why AI is unreadable]
---

Traditional software has source code — instructions written by humans that can be read, stepped through, and audited.

Neural networks have weights: billions of floating-point numbers produced by gradient descent over training data. No human wrote them. No human can read them in any meaningful sense.

Each weight encodes a tiny fragment of a statistical pattern extracted from training examples. Together they produce behavior, but the relationship between any individual weight and any specific output is not traceable by inspection.

When a model produces an answer, approximately billions of numbers were multiplied together in a specific order. That computation has no equivalent of "the model thought X because of rule Y." There is no rule. There is only the aggregate result of the optimization process.

This is the root cause of the black-box problem — not complexity, not proprietary secrecy, but the fundamental nature of how neural networks encode knowledge.

---

### Read more

- [[Superposition allows neural networks to encode more features than neurons using overlapping activation patterns]]
- [[Black-box AI models prevent auditing of decision-making processes]]
- [[Mechanistic interpretability reverse-engineers neural network computations into readable circuits]]
