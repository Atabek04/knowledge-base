---
created: 2026-05-29
aliases: [backpropagation, backprop, backward pass]
tags:
  - ml/training
  - ml/deep-learning
---

Backpropagation is the algorithm that computes [[Gradient adjusts params to reduce loss|gradients]] for every weight in a neural network, so each weight can be nudged to reduce the loss.

The name comes from the direction: gradients are computed starting from the **output** (where the loss is) and flowing **backwards** toward the input, layer by layer.

---

### Why "backward"?

A neural network has many stacked layers. During the **forward pass**, input flows left → right: layer 1 → layer 2 → ... → output → loss.

To update weights in layer 1, you need to know: *how much did layer 1's mistake contribute to the final loss?* You can only answer that after computing how much layers 2, 3, ..., N contributed.

So gradients must be computed in reverse order: loss → layer N → layer N-1 → ... → layer 1.

---

### The math underneath

Backprop applies the **chain rule** from calculus: if `A → B → C`, then the derivative of C with respect to A equals:

```
dC/dA = (dC/dB) × (dB/dA)
```

Each layer multiplies the incoming gradient by its own local derivative and passes it further back. No new math — just [[Gradient adjusts params to reduce loss|gradient descent]] applied through many layers in sequence.

---

### Scale in LLMs

GPT-3 has 96 layers and 175 billion weights.

Every training step runs backprop through all 96 layers, computing a gradient for each of the 175B weights. This is why training a large LLM costs millions of dollars.

---

### Backprop vs forward pass

| Forward pass | Backprop |
|---|---|
| Input → output | Loss → input |
| Computes predictions | Computes gradients |
| Runs at inference too | Training only |

---

Read more:
- [[Gradient adjusts params to reduce loss]]
- [[Neural network weights are compressed statistical patterns not human-readable instructions]]
- [[LLM training uses next-token prediction on existing text to learn statistical patterns]]
- [[Cross-entropy loss measures probability assigned to the correct token]]
