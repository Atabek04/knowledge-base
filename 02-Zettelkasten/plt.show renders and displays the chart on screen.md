---
created: 2026-02-19
aliases: [plt.show]
tags:
  - python/matplotlib
---

> **`plt.show()` takes everything you've built (scatter, plot, labels) and renders it on screen.**

---

### Why is it needed?

[[Pyplot is the convenience module for quick plotting in Matplotlib|pyplot]] builds the chart in memory as you call `scatter`, `plot`, `title`, etc. Nothing appears until you call `show()`.

```python
plt.scatter(X_test, y_test, color='red')
plt.plot(X_test, y_pred, color='blue')
plt.title('Salary vs Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()    # now it actually appears
```

<mark style="background: pink">`plt.show()` must be the **last** call. Anything added after it goes to a new, empty chart.</mark>

No parameters needed — it just renders whatever has been built so far.

---

Read more:
- [[Pyplot is the convenience module for quick plotting in Matplotlib]]
- [[plt.scatter draws individual data points as dots on a chart]]
- [[plt.plot draws a line by connecting points in order]]
- [[plt.title, xlabel, and ylabel add text labels to a chart]]
