---
created: 2026-02-12
aliases: [Slope of line and curve]
tags:
  - math/calculus
---

> **Slope** tells you **how steep something is** — how much `y` changes when `x` changes.

Think of walking up a hill:
- Steep hill → big slope
- Flat ground → slope = 0
- Going downhill → negative slope

**Formula:** $m = \frac{\Delta y}{\Delta x}$

---

### Lines: Constant Slope

**Example:** $y = 2x + 1$

**Finding slope:**
- $x_1 = 0$; $y_1 = 1$
- $x_2 = 1$; $y_2 = 3$
- $\Delta y = 3 - 1 = 2$
- $\Delta x = 1 - 0 = 1$
- $m = \frac{2}{1} = 2$

**What slope = 2 means:**
- For every 1 unit right (run), go 2 units up (rise)

**Using slope to predict:**

$$\Delta y = slope \times \Delta x$$

Start at (3, 7). If x increases by 0.5, what's new y?

```
Δy = 2 × 0.5 = 1
New y = 7 + 1 = 8
```

**Verify:** $y = 2(3.5) + 1 = 8$ ✓

<mark style="background: yellow">For lines, predictions are **always exact** (slope never changes).</mark>

---

### Curves: Changing Slope

**Example:** $y = x^2$

Unlike lines, slope **changes at every point**.

**Slope at different points:**
- At x = 0: slope = 0 (flat)
- At x = 1: slope = 2
- At x = 2: slope = 4 (steeper!)

To find slope at any point, we use [[Derivative measures how fast something is changing at a specific point|derivatives]].

**Using slope to predict:**

At point (2, 4) where slope = 4:

If x increases by 0.1, what's new y?

```
Δy ≈ slope × Δx
Δy ≈ 4 × 0.1 = 0.4
Predicted y = 4.4
```

**Actual:** $y = (2.1)^2 = 4.41$

**Error:** 0.01 (small!)

<mark style="background: yellow">For curves, predictions are **approximate** — slope changes as you move.</mark>

```functionplot
---
title: Curve y = x² and Its Derivative y = 2x
xLabel: x
yLabel: y
bounds: [-3, 3, -2, 9]
grid: true
---
y = x^2
y = 2*x
```

**Visual:**
- Blue: Original curve $y = x^2$
- Red: Derivative $y = 2x$ (shows slope at each point)

---

### Connection to Machine Learning

In math: slope = how much y changes per unit of x.

In ML: slope = how much the **prediction changes** per unit of the **feature**.

<mark style="background: cyan">In ML, slope is also called **weight** (`w` or `b₁`).</mark> Same idea — how much one feature influences the output. "Slope" is the math term, "weight" is the ML term.

A [[Linear regression finds the best-fit line through data|linear regression]] model learns the best slope and intercept from data automatically — instead of you calculating it by hand.

The prediction formula is the same: $y = mx + b$

---

Read more:
- [[Derivative measures how fast something is changing at a specific point]]
- [[Tangent line touches curve at exactly one point and shows instantaneous slope]]
- [[Two methods to find slope of a curve - calculation or visual estimation]]
- [[Linear regression finds the best-fit line through data]]

Good YouTube videos:
- [Understanding Differentiation Part 1: The Slope of a Tangent Line](https://youtu.be/ktOYbZ8CpLA)
