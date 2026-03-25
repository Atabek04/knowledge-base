---
created: 2026-02-18
aliases: [Simple Linear Regression, SLR]
tags:
  - ml/regression
---

> **Simple Linear Regression** finds the <mark style="background: yellow">best straight line</mark> through data to predict a continuous target from **one feature**.

---

### Why "simple" and why "linear"

- **Simple** — uses only **one** input feature (X)
- **Linear** — the relationship between feature and target forms a **straight line**

---

### The equation

$$y = b_0 + b_1 x$$

- `y` — the predicted target (e.g. salary)
- `x` — the input feature (e.g. years of experience)
- `b₁` — the **slope** (how much y changes when x increases by 1)
- `b₀` — the **intercept** (the value of y when x = 0)

This is the same as `y = mx + b` from school math, just different letters.

---

### Example

![[potato_simple_linear_regression.png]]

**Feature (X):** Nitrogen Fertilizer (kg)
**Target (ŷ):** Potato yield (tonnes)

The model learns: $Potatoes[t] = b_0 + b_1 \times Fertilizer[kg]$

- **b₀ = 8t** — with zero fertilizer, the farm still produces 8 tonnes (the intercept)
- **b₁ = 3 t/kg** — each extra kg of fertilizer adds 3 tonnes of potatoes (the slope)

On the plot, the orange arrows show b₁ in action: 
- move `+1kg` right on X → the line goes +3t up on Y. 
- Each blue dot is a separate harvest — scattered around the line, not perfectly on it.

---

### How the line fits data

Each data point is plotted as a dot on a graph (X axis = feature, Y axis = target).

![[best_fit_line.png]]

Left plot — raw scattered data points. 
Right plot — the best-fit line drawn through them. Some dots are above the line, some below.

<mark style="background: #FFB8EBA6;">No single line can pass through all dots perfectly.</mark>

![[error_best_fit_line.jpg]]

The vertical distance from each dot to the regression line = the **error** for that point.

In the image above, notice the two arrows:
- one points **down** to a dot below the line (the model predicted too high)
- the other points **up** to a dot above the line (the model predicted too low). Both have roughly the same distance from the line.

But if we just sum the raw errors, the positive (+5) and negative (-5) would cancel out — giving us 0, as if the model were perfect. It's not.

That's why we **square** each error first. Squaring does two things:
- Makes all errors **positive** — above or below, both count
- **Punishes large errors more** — an error of 10 becomes 100, while an error of 5 becomes 25

Then we take the **average** of all squared errors — that's **Mean Squared Error (MSE)**
$$MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$

The best line is the one where MSE across all points is smallest. We don't aim for zero error — we aim for the **minimum** error.

How do we find that minimum? [[Ordinary Least Squares minimizes the sum of squared errors to find the best-fit line|OLS]] takes the MSE formula, uses calculus to find the exact b₀ and b₁ that produce the smallest total error — no iterations needed.

---

Read more:
- [[Regression predicts a continuous number]]
- [[Ordinary Least Squares minimizes the sum of squared errors to find the best-fit line]]
- [[Loss function - formula that measures how wrong the model is]]
- [[Supervised learning means the model learns from labeled data with known answers]]
