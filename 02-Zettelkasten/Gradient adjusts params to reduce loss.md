---
created: 2026-01-23
tags:
  - ml/training
  - ml/optimization
---

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

> $\Delta f \approx f'(x) \cdot \Delta x$

$\Delta f \approx 6 \cdot 0.001 = 0.006$

---

#### Why Derivatives Show Direction

For Loss Function we gonna use **<mark style="background: #ADCCFFA6;">Mean Squared Error (MSE)</mark>**:

```
L(w) = (prediction − actual)²
```

Our example: $L(w) = (w - 5)^2$
**Derivative:** $L'(w) = 2(w - 5)$

---

**When derivative is <mark style="background: #BBFABBA6;">POSITIVE</mark>** (w > 5) → going uphill :luc_arrow_up_right:

Example: w = 7
- $L'(7) = 2(7 - 5) = 4$ (positive)
- Loss = $(7 - 5)^2 = 4$
- If we **increase** w further, loss goes **up**
- **Move left** (decrease w) to reduce loss

Update with learning_rate = 0.01:
- $w_{new} = 7 - (0.01 \times 4) = 7 - 0.04 = 6.96$
- **w decreased** ✓ (moved left)

---

**When derivative is <mark style="background: #BBFABBA6;">NEGATIVE</mark>** (w < 5) → going downhill :luc_arrow_down_right:

Example: w = 2
- $L'(2) = 2(2 - 5) = -6$ (negative)
- Loss = $(2 - 5)^2 = 9$
- If we **increase** w, loss goes **down**
- **Move right** (increase w) to reduce loss

Update with learning_rate = 0.01:
- $w_{new} = 2 - (0.01 \times -6) = 2 - (-0.06) = 2.06$
- **w increased** ✓ (moved right)

---

**When derivative is <mark style="background: #BBFABBA6;">ZERO</mark>** (w = 5) → flat point (minimum!)

Example: w = 5
- $L'(5) = 2(5 - 5) = 0$
- Loss = $(5 - 5)^2 = 0$ (minimum loss ✓)
- This is where we stop adjusting

---

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

---

#### The Update Rule: How We Actually Move

The formula that updates the weight each step:

$w_{new} = w_{old} - (learning\_rate \times derivative)$

The **minus sign** is the key: it makes us move **opposite** the derivative.

---

#### What is Learning Rate?

> ⚠️**Learning rate is NOT random.** 

You **choose** it before training.

It's a **hyperparameter** that controls **<mark style="background: #BBFABBA6;">how big each step is</mark>**

Common values: `0.001`, `0.01`, `0.1`

Think of it as "caution level":
- **Small learning rate** (0.001) = take tiny steps, slower but safer
- **Large learning rate** (0.1) = take big steps, faster but might overshoot

We **always** subtract — the derivative itself carries the direction.

---
#### Parabola - convex function

A **convex** function has:
- One clear **bottom point** (global minimum)
- Smooth sides sloping down to it
- A nice property: gradient descent will **always find the minimum**

Not all loss functions are convex, but many simple ones are.
This is why the U-shape matters — it guarantees we can find the best weights.

---

Read more:
- [[Loss function - formula that measures how wrong the model is]]
- [[Parameter is a value that defines how a system behaves]]
- [[Weights define how much each feature matters]]
- [[Bias adds a baseline shift to all predictions]]
