---
created: 2026-02-19
aliases: [plt.plot, line plot]
tags:
  - python/matplotlib
---

> **`plt.plot(x, y)` connects data points with straight line segments in the order they appear.**

---

### Why "plot"?

In English, "to plot" means to mark positions on a map or graph. Think of a detective "plotting" locations on a map and drawing lines between them.

That's what this method does — marks points, then draws lines between them.

---

### How it works

Same parameters as `scatter` — two arrays:

```python
plt.plot(x, y, color='blue')
```

- `x` — array of values for the horizontal axis
- `y` — array of values for the vertical axis
- `color` — optional, defaults to blue

<mark style="background: yellow">It doesn't need a mathematical function. It simply connects point 1 to point 2, point 2 to point 3, and so on.</mark>

**Example:**

```python
x = [1, 2, 3]
y = [10, 20, 30]
plt.plot(x, y, color='blue')
```

This draws lines: (1,10) → (2,20) → (3,30).

---

### Why does this work for regression lines?

A linear regression produces predictions that already lie on a straight line. So when `plot` connects them in order, the result looks like a perfect line — because it **is** one.

<mark style="background: pink">If your `x` values are not sorted, the line will zigzag between points instead of looking smooth.</mark> In practice, `X_test` is usually sorted or you sort it before plotting.

---

### scatter vs plot

| | `scatter` | `plot` |
|---|---|---|
| Draws | Individual dots | Connected line |
| Use for | Raw data points | Trends, predictions |

---

Read more:
- [[Pyplot is the convenience module for quick plotting in Matplotlib]]
- [[plt.scatter draws individual data points as dots on a chart]]
- [[Matplotlib is a Python library for creating static and interactive visualizations]]
