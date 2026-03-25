---
created: 2026-02-18
aliases: [Vectorized Operations, Vectorization]
tags:
  - python/numpy
---

> **Vectorized operations** apply math to <mark style="background: yellow">every element in an array at once</mark> — no Python loop needed.

---

### Examples

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

a + b        # [5, 7, 9]
a * b        # [4, 10, 18]
a + 10       # [11, 12, 13]
np.sqrt(a)   # [1.0, 1.41, 1.73]
```

One line = operation on every element. Internally NumPy runs optimized **C loops**, not Python loops.

---

### Why this matters for ML

Vectorization is used daily for:
- [[Feature scaling transforms features to similar ranges for efficient training|Feature scaling]] — normalizing entire columns at once
- Matrix multiplication — core of neural network computations
- Computing [[Loss function - formula that measures how wrong the model is|loss functions]] across all data points

<mark style="background: #ADCCFFA6;">This is the reason [[NumPy exists because Python lists are too slow for numerical computing|NumPy exists]] — without vectorization, ML on large datasets would be impractical.</mark>

---

Read more:
- [[NumPy exists because Python lists are too slow for numerical computing]]
- [[Broadcasting expands smaller arrays to match shapes automatically]]
- [[Feature scaling transforms features to similar ranges for efficient training]]
