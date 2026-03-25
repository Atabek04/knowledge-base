---
created: 2026-02-19
aliases: [plt.scatter, scatter plot]
tags:
  - python/matplotlib
---

> **`plt.scatter(x, y)` draws each data point as a separate dot on the chart.**

---

### Why "scatter"?

In English, "scatter" means to throw things in different directions — like scattering seeds on the ground. The dots land wherever the data puts them, with no lines connecting them.

That's exactly what this method does — it **scatters** dots across the chart, one per data point.

---

### How it works

You pass two arrays of equal length:

```python
plt.scatter(x, y, color='red')
```

- `x` — array of values for the horizontal axis
- `y` — array of values for the vertical axis
- `color` — optional, defaults to blue

For each index `i`, it places a dot at position `(x[i], y[i])`.

**Example:**

```python
x = [1, 2, 3]
y = [10, 20, 30]
plt.scatter(x, y, color='red')
```

This draws 3 dots: at (1, 10), (2, 20), and (3, 30).

---

### When to use

<mark style="background: yellow">Use `scatter` when you want to show **raw data points** — no connections, no lines.</mark>

In ML, you'll typically scatter the actual test data (`X_test`, `y_test`) to see where real observations fall.

---

Read more:
- [[Pyplot is the convenience module for quick plotting in Matplotlib]]
- [[plt.plot draws a line by connecting points in order]]
- [[Matplotlib is a Python library for creating static and interactive visualizations]]
