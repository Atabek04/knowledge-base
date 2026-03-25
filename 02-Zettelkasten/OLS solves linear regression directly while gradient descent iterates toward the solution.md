---
created: 2026-02-18
aliases: [OLS vs Gradient Descent, Normal Equation vs Gradient Descent]
tags:
  - ml/optimization
  - ml/regression
---

> **OLS** finds the optimal weights in <mark style="background: yellow">one calculation</mark>. 
> **Gradient descent** finds them through <mark style="background: yellow">many small steps</mark>. Which one to use depends on the model and data size.

---

### When to use OLS (Normal Equation)

OLS works by solving the **Normal Equation** directly:

$$\hat{\theta} = (X^TX)^{-1}X^Ty$$

This gives you the exact optimal weights — no iterations, no learning rate, no tuning.

<mark style="background: #BBFABBA6;">Use OLS when:</mark>
- The model is **linear** (Simple or Multiple Linear Regression)
- Number of features is **under ~10,000**

---

### When to use Gradient Descent

<mark style="background: #FFB8EBA6;">Use gradient descent when:</mark>
- The model is **non-linear** (neural networks, deep learning) — no closed-form solution exists
- Number of features **exceeds ~10,000** — matrix inversion becomes O(n³) and too slow
- The matrix $X^TX$ is **non-invertible** (features are copies of each other, or more features than samples)

---

### Comparison

| | OLS | Gradient Descent |
|---|---|---|
| Speed | One-shot calculation | Many iterations |
| Complexity | O(n³) for matrix inversion | O(kmn) per iteration |
| Feature scaling needed? | **No** | **Yes** |
| Learning rate to tune? | **No** | **Yes** |
| Works for non-linear? | **No** | **Yes** |
| Large features (>10k) | Too slow | Efficient |
| Numerical stability | Worse (amplifies errors) | Better |

---

### Why the ~10,000 threshold?

OLS requires inverting an n×n matrix — that's **O(n³)** complexity. With 100 features, that's 1 million operations. With 10,000 features, that's **1 trillion** operations. Gradient descent scales linearly with features per iteration, making it far more practical at scale.

---

Read more:
- [[Ordinary Least Squares minimizes the sum of squared errors to find the best-fit line]]
- [[Gradient adjusts params to reduce loss]]
- [[Feature scaling transforms features to similar ranges for efficient training]]
