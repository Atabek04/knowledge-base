---
created: 2026-02-19
aliases: [plt.title, plt.xlabel, plt.ylabel, chart labels]
tags:
  - python/matplotlib
---

> **Three methods add text labels to your chart: `title` at the top, `xlabel` on the x-axis, `ylabel` on the y-axis.**

---

### Usage

```python
plt.title('Salary vs Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Salary ($)')
```

Each takes a string. All three are optional — the chart renders without them, but labels make it readable.

---

### When to use

<mark style="background: yellow">Always label your axes when presenting results.</mark> Without labels, a chart is just dots and lines with no meaning.

For quick personal debugging, you can skip them.

---

Read more:
- [[Pyplot is the convenience module for quick plotting in Matplotlib]]
- [[plt.scatter draws individual data points as dots on a chart]]
- [[plt.plot draws a line by connecting points in order]]
