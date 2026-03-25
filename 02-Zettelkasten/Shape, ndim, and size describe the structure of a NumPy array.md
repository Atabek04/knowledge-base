---
created: 2026-02-18
aliases: [Array Shape, ndim, shape]
tags:
  - python/numpy
---

> Every NumPy array has three structural properties: <mark style="background: yellow">shape</mark> (dimensions), <mark style="background: yellow">ndim</mark> (number of dimensions), and <mark style="background: yellow">size</mark> (total elements).

---

### Example

```python
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

arr.shape   # (2, 3) → 2 rows, 3 columns
arr.ndim    # 2      → 2 dimensions (2D array)
arr.size    # 6      → total elements (2 × 3)
```

---

### Quick reference

| Property | Returns | Example |
|---|---|---|
| `.shape` | rows × columns (as tuple) | `(2, 3)` |
| `.ndim` | number of dimensions | `2` |
| `.size` | total element count | `6` |

Knowing the shape is essential for [[Reshape changes array dimensions without changing the data|reshaping]] — the total elements must match.

---

Read more:
- [[NumPy provides efficient array operations for numerical computing in Python]]
- [[Reshape changes array dimensions without changing the data]]
