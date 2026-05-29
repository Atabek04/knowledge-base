---
created: 2026-05-29
aliases: [softmax, softmax function]
tags:
  - ml/training
  - ml/probability
---

During the forward pass, the input tokens travel through all [[Neural network layers build increasingly abstract representations of input data|layers]] of the network. The final layer outputs one raw number per token in the vocabulary — these are called **logits**.

Logits are not probabilities: they can be negative, greater than 1, and they do not sum to anything meaningful.

**Softmax** converts those raw scores into a proper [[Classification outputs probability scores to express confidence in predictions|probability distribution]]: every value becomes positive and they all sum to exactly 100%.

> **Why "Softmax"?** "Max" because it pushes the highest value even higher. "Soft" because it doesn't pick one hard winner — all tokens keep a probability, the highest just dominates.

---

### How it works (intuition)

Given raw scores for a 5-word vocabulary:

```
"blue"   → 8
"green"  → 3
"cat"    → 1
"run"    → 0
"purple" → 2
```

Softmax raises `e` to the power of each score, then divides each result by the total:

```
e^8 = 2981   → 2981 / 3421 = 87%
e^3 = 20     → 20   / 3421 = 6%
e^1 = 2.7    → ...
e^0 = 1      → ...
e^2 = 7.4    → ...
              total ≈ 3421 = 100%
```

The highest raw score gets a disproportionately large probability — softmax amplifies differences.

---

### Why it matters for training

After softmax, the probability of the correct token goes directly into [[Cross-entropy loss measures probability assigned to the correct token|cross-entropy loss]].

Example: sentence is `"The sky is ___"`, correct answer is `"blue"`.

If softmax gave `"blue"` only 2% → loss is high → [[Gradient adjusts params to reduce loss|gradient]] nudges the weights that produced `"blue"`'s logit so it scores higher next time.

---

Read more:
- [[Cross-entropy loss measures probability assigned to the correct token]]
- [[Classification outputs probability scores to express confidence in predictions]]
- [[LLM training uses next-token prediction on existing text to learn statistical patterns]]
- [[Gradient adjusts params to reduce loss]]
