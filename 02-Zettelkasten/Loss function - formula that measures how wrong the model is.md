---
created: 2026-01-22
tags:
  - ml/training
  - ml/loss
---

> Loss function - **mathematical formula** that measures "**how wrong**" the model is.

#### Lower loss = better predictions

> ⚠️ Different problems need **different loss functions** 
> because they measure "wrongness" differently

---
##### Example

For house price prediction, loss might be:
Predicted $250k, actual $300k
loss = 50² = 2,500

> ⚠️ Not all Lost Functions use Square Error

---

**Why we square the error**

1. **Error = difference between predicted and actual**
	- Example: $250k − $300k = −50k

2. **Problem if we don't square:**
    - Positive and negative errors **<mark style="background: #FFB8EBA6;">can cancel each other</mark>** if we just sum them.
    - Example:
	    - one prediction $+50k$, another $−50k$,
	    - sum = 0
	    - looks perfect, which is wrong 🚩

3. **Squaring fixes this:**
    - Square makes all errors **<mark style="background: #FFB8EBA6;">positive</mark>** → both +50k and −50k become 2,500.
    - **Larger mistakes are penalized more** (50² = 2,500 vs 10² = 100)
	    - *meaning, punishes big mistakes more heavily.*

---

### Common Loss Functions

#### Mean Squared Error (MSE)

Most common loss function for regression problems.

**Formula:**

$$MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$

Where:
- $n$ = number of training examples
- $y_i$ = actual value for example $i$
- $\hat{y}_i$ = predicted value for example $i$

**Steps:**
1. Calculate error for each prediction: $(y_i - \hat{y}_i)$
2. Square each error: $(y_i - \hat{y}_i)^2$
3. Take the average: sum all squared errors and divide by $n$

**Example with 3 predictions:**

| Actual ($y$) | Predicted ($\hat{y}$) | Error | Squared Error |
|--------------|----------------------|-------|---------------|
| $300k        | $250k                | 50k   | 2,500,000,000 |
| $400k        | $420k                | -20k  | 400,000,000   |
| $200k        | $180k                | 20k   | 400,000,000   |

$$MSE = \frac{2,500,000,000 + 400,000,000 + 400,000,000}{3} = 1,100,000,000$$

The gradient (used in training) is:

$$\frac{\partial MSE}{\partial w_j} = \frac{2}{n} \sum_{i=1}^{n} (\hat{y}_i - y_i) \cdot x_{ij}$$

For a single example:

$$\frac{\partial MSE}{\partial w_j} = 2(\hat{y} - y) \cdot x_j$$

> ⚠️ The factor of 2 often gets absorbed into the learning rate in practice.

---

Read more:
- [[Gradient adjusts params to reduce loss]]
- [[Parameter is a value that defines how a system behaves]]