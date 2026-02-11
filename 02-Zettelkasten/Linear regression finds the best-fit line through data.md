---
created: 2026-02-11
tags:
  - ml/regression
  - math/slope
---

### What is linear regression?

> **Linear regression** finds the line that best fits your data, so you can predict new values.

**Linear** — you're fitting a **line** (equation: $y = mx + b$).

**Regression** — you're "going back" to the data to find the relationship that explains it.

---

### How it works

You have data points but **no equation**. For example:

| Size (sq ft) | Price ($k) |
|---|---|
| 800 | 150 |
| 1000 | 200 |
| 1200 | 250 |
| 1500 | 325 |

The model tries many possible lines (different $m$ and $b$ values).

For each line, it measures how far off the predictions are from actual values.

It picks the line with the **least total error** — the "best fit."

---

### What the model learns

The model finds two values:

- **Slope ($m$)** — how much the prediction changes per unit of the feature
- **Intercept ($b$)** — the baseline value when the feature is 0

Once found, prediction works just like any line equation:

$$\hat{y} = m \cdot x + b$$

Plug in any $x$ → get predicted $y$.

---

### Why "best fit" and not "perfect fit"?

Real data is messy. Points don't fall exactly on a line.

Different pairs of points give different slopes.

So the model picks the line that **minimizes total error** across all points — not one that passes through any specific pair.

---

### Connection to slope

This is the same slope from basic math: $m = \frac{\Delta y}{\Delta x}$

The difference: in ML, the slope is **learned from data** automatically, not calculated by hand from two known points.

---

### Key assumptions

Linear regression assumes:

- The relationship between feature and prediction is **linear** (constant slope)
- One slope fits all data points
- If data follows a **curve**, linear regression won't fit well

For curved relationships, other methods exist (e.g., polynomial regression).

---

Read more:
- [[Slope of line and curve]]
- [[Regression and Classification]]
