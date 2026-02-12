---
created: 2026-02-12
aliases: [Median]
tags:
  - ml/math
  - math/statistics
---

> **Median** = the middle value when all values are sorted in order.

### Formula

Sort values first, then:

- **Odd count** → pick the middle value: $\text{median} = x_{\frac{n+1}{2}}$
- **Even count** → average of two middle values: $\text{median} = \frac{x_{\frac{n}{2}} + x_{\frac{n}{2}+1}}{2}$

### Example (odd)

Values: 10, 20, **30**, 40, 100

Median = **30** (the middle one)

### Example (even)

Values: 10, 20, **30, 40**, 50, 100

Median = $\frac{30 + 40}{2}$ = **35**

---

### In Python

```python
df["income"].median()    # → 30.0
```

---

### Why median over mean?

<mark style="background: yellow">Median ignores outliers.</mark> In the odd example, whether the last value is 100 or 1,000,000, the median stays 30.

That's why `median` is the preferred imputation strategy when data has outliers.

---

Read more:
- [[Mean is the sum of all values divided by the count]]
- [[Missing data must be handled because most ML algorithms cannot compute with NaN]]
- [[Math for ML MOC]]
