---
created: 2026-02-18
aliases: [np.arange]
tags:
  - python/numpy
---

> `np.arange(n)` generates an array of integers from <mark style="background: yellow">0 to n-1</mark>, just like Python's `range()` but returns a NumPy array.

---

### Usage

```python
import numpy as np

np.arange(5)          # [0, 1, 2, 3, 4]
np.arange(2, 10)      # [2, 3, 4, 5, 6, 7, 8, 9]
np.arange(0, 1, 0.2)  # [0.0, 0.2, 0.4, 0.6, 0.8]
```

Supports start, stop, and step — same logic as `range()`.

---

Read more:
- [[np.array creates a NumPy array from a Python list]]
- [[np.linspace generates evenly spaced numbers between two values]]
