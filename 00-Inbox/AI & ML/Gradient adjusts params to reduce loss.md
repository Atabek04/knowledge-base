
> **Gradient tells the model which direction to adjust each parameter** to reduce loss.

---

Math calculates this automatically using **calculus** (specifically: **derivatives**)

A **derivative** measures how much the output changes when you change the input by a tiny amount.

> If I nudge `x` by a tiny step, how much does `f(x)` change?

The derivative of `f(x)` is written as `f'(x)` or `df/dx`.

---

**Example** with `f(x) = x²`

$f(x) = x^2$
$f'(x) = \frac{d}{dx} x^2 = 2x$
$f'(3) = 2 \cdot 3 = 6$

At `x = 3` the derivative is `6`

This means: 
if you increase `x` from `3` to `3.001`, 
`f(x)` increases by approximately `0.006`

$\Delta f \approx f'(x) \cdot \Delta x$
$\Delta f \approx 6 \cdot 0.001 = 0.006$

---

#### Why Derivatives Show Direction

If the <mark style="background: #BBFABBA6;">derivative is positive</mark> → function is going uphill. :luc_arrow_up_right:

If the <mark style="background: #BBFABBA6;">derivative is negative</mark> → function is going downhill :luc_arrow_down_right: 

If the <mark style="background: #BBFABBA6;">derivative is zero</mark> → you're at a flat point (potentially minimum or maximum).

> We want to go downhill (reduce loss). 
 
So we move in the **<mark style="background: #FFB86CA6;">opposite direction</mark>** of the derivative:
- When derivative is **positive** → move left (decrease w)
- When derivative is **negative** → move right (increase w)

- Loss function: 
	- L(w) = **(prediction − actual)²** is a common one for regression
	- `L(w) = (w - 5)²`
	
```functionplot
---
title: Loss Function L(w) = (w - 5)²
xLabel: Weight (w)
yLabel: Loss
bounds: [0, 10, 0, 25]
grid: true
---
L(x)=(x-5)^2
```

**Derivative is POSITIVE (uphill) when `w` > 5:**
- w = 6: loss = 1, and if w increases, loss increases
- w = 7: loss = 4, still going up
- Derivative = 2(w - 5), which is positive when w > 5

---
