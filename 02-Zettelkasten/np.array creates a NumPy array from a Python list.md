---
created: 2026-02-18
aliases: [np.array]
tags:
  - python/numpy
---

> `np.array()` converts a Python list into a <mark style="background: yellow">NumPy array</mark> — the fundamental data structure for numerical computing.

---

### Usage

```python
import numpy as np

a = np.array([1, 2, 3])       # 1D array
b = np.array([[1,2], [3,4]])   # 2D array
```

This is the most direct way to create an array — you manually provide the data.

---

### Two other common ways to create arrays

- [[np.arange generates sequential integers like Python range|np.arange(n)]] → generates 0 to n-1 automatically
- [[np.linspace generates evenly spaced numbers between two values|np.linspace(start, end, count)]] → generates evenly spaced numbers

---

Read more:
- [[NumPy provides efficient array operations for numerical computing in Python]]
- [[np.arange generates sequential integers like Python range]]
- [[np.linspace generates evenly spaced numbers between two values]]
