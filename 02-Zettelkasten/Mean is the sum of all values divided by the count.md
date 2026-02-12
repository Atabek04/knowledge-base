---
created: 2026-02-12
aliases: [Mean, Average]
tags:
  - ml/math
  - math/statistics
---

> **Mean** (average) = sum of all values divided by how many values there are.

### Formula

$$\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i$$

Where:
- $\bar{x}$ — the mean (read "x bar")
- $n$ — number of values
- $x_i$ — each individual value

### Example

Values: 10, 20, 30, 40, 100

$$\bar{x} = \frac{10 + 20 + 30 + 40 + 100}{5} = \frac{200}{5} = 40$$

---

### In Python

```python
df["income"].mean()    # → 40.0
```

---

### When mean is misleading

<mark style="background: #FF5582A6">Mean is sensitive to outliers</mark> (values abnormally far from the rest).

Salaries at a small company: `30k, 35k, 32k, 28k, 33k, 500k`

- Mean: **109k** — misleading, nobody except the CEO earns near that
- Median: **32.5k** — still represents the typical employee

That's when [[Median is the middle value when data is sorted|median]] is a better choice.

---

Read more:
- [[Median is the middle value when data is sorted]]
- [[Missing data must be handled because most ML algorithms cannot compute with NaN]]
- [[Math for ML MOC]]
