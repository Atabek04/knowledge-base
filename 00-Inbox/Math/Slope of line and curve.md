
### General definition

> **Slope** tells you **how steep something is**
> how much it goes **up or down** as you move forward.

Think of walking up a hill:
- Steep hill → big slope
- Flat ground → slope = 0
- Going downhill → negative slope

---

### Slope in math

> **How much `y` changes when `x` changes**

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

**Key:** For lines, predictions are **always exact** (slope never changes).

---

### Curves: Changing Slope

**Example:** $y = x^2$

Unlike lines, slope **changes at every point**.

**Slope at different points:**
- At x = 0: slope = 0 (flat)
- At x = 1: slope = 2
- At x = 2: slope = 4 (steeper!)

To find slope at any point, we use **derivatives**.

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

**Key:** For curves, predictions are **approximate** - slope changes as you move.

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

### What is a Derivative?

> **Derivative** = slope at a specific point on a curve

**How it works:**

Take two points very close together, calculate slope:
$$m = \frac{\Delta y}{\Delta x}$$

Make $\Delta x$ smaller and smaller → approach zero.

**Not $\Delta x = 0$** (that's undefined: 0/0)
**But $\Delta x \to 0$** (approaching zero)

**Analogy:**
- Average speed = total distance / total time (large $\Delta x$)
- Instantaneous speed = speedometer reading ($\Delta x \to 0$)

**Result:** Derivative measures **instantaneous rate of change**.

For $y = x^2$:
$$\frac{dy}{dx} = 2x$$

This tells you the slope at any point x.

---

### Tangent Line: Visualizing the Derivative

A **tangent line** touches the curve at exactly one point.

Its slope = the derivative at that point.

**Example:** At x = 1 on $y = x^2$:
- Point: (1, 1)
- Derivative: $f'(1) = 2(1) = 2$
- Tangent line: $y = 2x - 1$

```functionplot
---
title: Tangent Line at x = 1
xLabel: x
yLabel: y
bounds: [-1, 3, -1, 5]
grid: true
---
y = x^2
y = 2*x - 1
```

**What this shows:**
- Tangent line (red) touches curve at x = 1
- Its slope (2) = derivative at that point
- Line shows **instantaneous rate of change**

**Three ways to say the same thing:**
- Derivative at x = 1 is 2
- Slope of tangent line is 2
- Rate of change at x = 1 is 2

---

### Two Methods to Find Slope of a Curve

#### Method 1: Calculate Derivative

**Use when:** You have the equation

**Process:**
- Find derivative algebraically
- Plug in x value
- Get exact slope

**Example:** For $y = x^2$ at x = 3:
- $\frac{dy}{dx} = 2x$
- Slope = $2(3) = 6$

**Pros:** Exact, fast
**Cons:** Need equation

---

#### Method 2: Draw Tangent Line Visually

**Use when:** You only have a graph (no equation)

**Process:**
1. Pick point on curve
2. Mentally zoom in until curve looks straight
3. Draw line touching curve at that point (by eye)
4. Measure rise/run: $m = \frac{\Delta y}{\Delta x}$

**Pros:** Works without equation
**Cons:** Approximate, depends on drawing skill

**Real-world use:** Lab data, experimental graphs

---

**Key distinction:**
- Method 1: **Calculation** → precise
- Method 2: **Visual estimation** → approximate

---
### Summary

**Slope:**
- Line → constant everywhere
- Curve → changes at each point

**Derivative:**
- Mathematical way to find slope at exact point
- Uses limit as $\Delta x \to 0$
- Measures instantaneous rate of change

**Tangent line:**
- Visual representation of derivative
- Its slope = derivative at that point

> **Slope measures how fast something changes;
> derivatives tell you that change at an exact moment.**

---

### Connection to Machine Learning

In math: slope = how much y changes per unit of x.

In ML: slope = how much the **prediction changes** per unit of the **feature**.

A [[Linear regression finds the best-fit line through data|linear regression]] model learns the best slope and intercept from data automatically — instead of you calculating it by hand.

The prediction formula is the same: $y = mx + b$

---

Read more about [[Derivative]]

Good YouTube videos:
- [Understanding Differentiation Part 1: The Slope of a Tangent Line](https://youtu.be/ktOYbZ8CpLA)

