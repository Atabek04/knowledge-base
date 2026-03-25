---
created: 2026-02-18
aliases: [OLS, Ordinary Least Squares]
tags:
  - ml/regression
  - ml/optimization
---

> **Ordinary Least Squares (OLS)** finds the best-fit line by <mark style="background: yellow">minimizing the sum of squared errors</mark> between predictions and actual values.

---

### Why it's called that

The name tells you exactly what it does:

- **Squares** — we square each error (distance from dot to line) so negatives don't cancel out positives
- **Least** — we find the line that makes the total of those squared errors **as small (least) as possible**
- **Ordinary** — this is the basic, standard version. 
	- There are fancier variants (Weighted Least Squares, Generalized Least Squares) — "ordinary" means no special tricks, just the straightforward approach

---

### How it works

![[OLS_simple_linear_regression.png]]

The grey lines show many possible lines you could draw. Each one has different errors (dashed blue lines = residuals). OLS finds the **one dark line** where the sum of all squared residuals is smallest.

The residual for each point: $\varepsilon_i = y_i - \hat{y}_i$ (actual value minus predicted value on the line).

We start with the MSE formula. Remember that $\hat{y}_i = b_0 + b_1 x_i$ (the prediction from our line):

$$MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 = \frac{1}{n} \sum_{i=1}^{n} (y_i - b_0 - b_1 x_i)^2$$

Now the only unknowns are **b₀ and b₁**. Everything else ($x_i$, $y_i$, $n$) is data we already have.

To find the minimum, we take the **derivative** with respect to b₀ and b₁, **set each to zero**, and solve:

$$\frac{\partial MSE}{\partial b_0} = 0 \quad \text{and} \quad \frac{\partial MSE}{\partial b_1} = 0$$

Solving these two equations gives us:

$$b_1 = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sum(x_i - \bar{x})^2}$$

$$b_0 = \bar{y} - b_1\bar{x}$$

Where $\bar{x}$ and $\bar{y}$ are the means of X and y.

Plug in your data → get b₁ and b₀ → you have your line.

---

### b₀ and b₁ — are they weights?

Yes — b₀ and b₁ are the **parameters** (weights) of the model:
- **b₁** = the [[Weights define how much each feature matters|weight]] — how much the feature influences the prediction
- **b₀** = the [[Bias adds a baseline shift to all predictions|bias]] (intercept) — the baseline when the feature is 0

In ML literature you'll see both notations:
- Statistics style: $b_0, b_1$ or $\beta_0, \beta_1$
- ML style: $w$ (weight) and $b$ (bias)

Same thing, different communities.

---

### Why not always use OLS?

OLS finds the answer **directly** — no learning rate, no steps, no iterations. Unlike [[Gradient adjusts params to reduce loss|gradient descent]] which adjusts weights step by step.

<mark style="background: #ADCCFFA6;">But OLS only works when the math is manageable</mark> — Simple and Multiple Linear Regression. For complex models (many features, non-linear, neural networks), the equations become impossible to solve directly, and gradient descent is the only option.

---

Read more:
- [[Simple linear regression predicts a target using one feature and a straight line]]
- [[Loss function - formula that measures how wrong the model is]]
- [[Gradient adjusts params to reduce loss]]
