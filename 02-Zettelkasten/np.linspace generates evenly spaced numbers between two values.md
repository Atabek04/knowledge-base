---
created: 2026-02-18
aliases: [np.linspace]
tags:
  - python/numpy
---

> `np.linspace(start, end, count)` generates <mark style="background: yellow">count evenly spaced numbers</mark> between start and end (inclusive).

---

### Usage

```python
import numpy as np

np.linspace(0, 1, 5)    # [0.0, 0.25, 0.5, 0.75, 1.0]
np.linspace(0, 10, 3)   # [0.0, 5.0, 10.0]
```

Unlike [[np.arange generates sequential integers like Python range|np.arange]] where you specify the **step**, here you specify **how many numbers** you want and NumPy calculates the spacing.

---

Read more:
- [[np.array creates a NumPy array from a Python list]]
- [[np.arange generates sequential integers like Python range]]
