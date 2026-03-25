---
created: 2026-02-18
aliases: [Why NumPy]
tags:
  - python/numpy
---

> **NumPy exists because Python lists are too slow and memory-heavy** for large-scale numerical operations.

---

### The problem with Python lists

Imagine storing 1 million numbers in a Python list:

- Numbers are scattered **all over memory** (not contiguous)
- Each number is wrapped in a **Python object** with metadata → overhead
- Operations happen **one element at a time** in a Python loop → slow

```python
# Adding 10 to each number — Python loops 1 million times
for i in range(len(arr)):
    arr[i] += 10
```

<mark style="background: #FFB8EBA6;">This is painfully slow for large datasets.</mark>

---

### How NumPy fixes it

1. **Contiguous memory** — numbers are stored side by side in one block of memory
2. **Same data type** — no per-element overhead (no Python object wrappers)
3. **C code under the hood** — operations run in compiled C, not interpreted Python
4. **Vectorized operations** — one line replaces the entire loop

```python
import numpy as np

arr = np.array([1, 2, 3, ...])  # 1 million numbers
arr += 10  # one line = 1 million operations, runs in C
```

<mark style="background: #BBFABBA6;">NumPy arrays are 50-100x faster than Python lists for numerical work.</mark>

---

### Why this matters for ML

NumPy is the **foundation** that ML libraries build on:
- [[Scikit-learn provides ready-to-use ML algorithms and preprocessing tools|Scikit-learn]] — preprocessing and models
- TensorFlow — deep learning
- PyTorch — deep learning
- [[Pandas provides data manipulation and analysis for tabular data in Python|Pandas]] — DataFrames are built on NumPy arrays

Without NumPy's speed, training models on large datasets would be impractical.

---

Read more:
- [[NumPy provides efficient array operations for numerical computing in Python]]
- [[Pandas provides data manipulation and analysis for tabular data in Python]]
- [[Scikit-learn provides ready-to-use ML algorithms and preprocessing tools]]
