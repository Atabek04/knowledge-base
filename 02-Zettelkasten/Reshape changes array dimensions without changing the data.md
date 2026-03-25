---
created: 2026-02-18
aliases: [Reshape, np.reshape]
tags:
  - python/numpy
---

> `reshape()` changes the <mark style="background: yellow">dimensions of an array without modifying the data</mark> — only the view changes.

---

### Example

```python
arr = np.arange(12)        # [0, 1, 2, ..., 11]
arr.reshape(3, 4)
# [[ 0,  1,  2,  3],
#  [ 4,  5,  6,  7],
#  [ 8,  9, 10, 11]]
```

Same 12 elements, now viewed as a 3×4 matrix.

---

### Rules

- <mark style="background: #FFB8EBA6;">Total elements must match.</mark> You can't reshape 12 elements into (3, 5) — that's 15 slots
- Reshape doesn't copy data — it changes how the same memory is read

---

### Why this matters for ML

Every ML model expects input as a **2D array** — rows = samples, columns = features.

If your data is a flat 1D array, you need to reshape it before feeding it to a model:

```python
X = np.array([1, 2, 3, 4])
X = X.reshape(-1, 1)   # (4, 1) → 4 samples, 1 feature
```

`-1` means "figure out this dimension automatically."

---

Read more:
- [[Shape, ndim, and size describe the structure of a NumPy array]]
- [[NumPy provides efficient array operations for numerical computing in Python]]
