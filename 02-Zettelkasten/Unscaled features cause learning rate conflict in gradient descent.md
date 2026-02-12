---
created: 2026-02-12
tags:
  - ml/preprocessing
  - ml/training
---

> The problem isn't that the model **can't** learn with unscaled features.
> The problem is that it learns **inefficiently** and **unstably**.

**Core issue:** Gradient descent uses **ONE learning rate** for **ALL features**.

When features have different scales:
- The same learning rate is **too fast** for large features
- The same learning rate is **too slow** for small features

This causes:
1. **Slow convergence** — takes many more iterations to reach optimal weights
2. **Unstable training** — weights overshoot and [[Oscillation happens when gradient overcorrects and bounces around the optimal value|oscillate]]
3. **Numerical issues** — very large gradients can cause precision errors

---

### Complete Example

Predict house price using:
- Bedrooms ($x_1$): values 2, 3, 4
- Square footage ($x_2$): values 1000, 2000, 3000

**Training data:**

| Bedrooms ($x_1$) | Sqft ($x_2$) | Price ($y$) |
|------------------|--------------|-------------|
| 2                | 1000         | $200k       |
| 3                | 2000         | $300k       |
| 4                | 3000         | $400k       |

**Model:** $\hat{y} = w_1 \cdot x_1 + w_2 \cdot x_2 + b$

Starting: $w_1 = 0$, $w_2 = 0$, $b = 0$, $\alpha = 0.0001$

---

#### Gradient calculation

Using chain rule on MSE:
$$\frac{\partial MSE}{\partial w_j} = 2(\hat{y} - y) \cdot x_j$$

**For $w_1$ (bedrooms):**
$$\frac{\partial MSE}{\partial w_1} = 2(0 - 200000) \cdot 2 = -800{,}000$$

**For $w_2$ (sqft):**
$$\frac{\partial MSE}{\partial w_2} = 2(0 - 200000) \cdot 1000 = -400{,}000{,}000$$

<mark style="background: #FF5582A6">Gradient for sqft is **500x larger** than gradient for bedrooms!</mark>

---

#### After one update

$$w_1 = 0 - 0.0001 \cdot (-800{,}000) = 80$$
$$w_2 = 0 - 0.0001 \cdot (-400{,}000{,}000) = 40{,}000$$

**Predict for the SAME house (2 bedrooms, 1000 sqft):**

$$\hat{y} = 80 \cdot 2 + 40{,}000 \cdot 1000 = 40{,}000{,}160$$

**We predicted $40 million for a $200k house!**

---

### The Impossible Choice

| Learning Rate | Effect on Sqft Weight     | Effect on Bedroom Weight |
|---------------|---------------------------|--------------------------|
| Large (0.01)  | Overshoots wildly         | Learns reasonably        |
| Medium (0.0001) | Still overshoots        | Learns very slowly       |
| Small (0.000001) | Learns slowly           | Barely moves             |

<mark style="background: yellow">This is the **fundamental problem** that [[Feature scaling transforms features to similar ranges for efficient training|feature scaling]] solves.</mark>

---

Read more:
- [[Feature scaling transforms features to similar ranges for efficient training]]
- [[Oscillation happens when gradient overcorrects and bounces around the optimal value]]
- [[Gradient adjusts params to reduce loss]]
- [[Weights define how much each feature matters]]
