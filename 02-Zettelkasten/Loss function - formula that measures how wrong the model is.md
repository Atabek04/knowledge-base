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

### How loss is calculated

#### Example

For house price prediction, loss might be:
Predicted $250k, actual $300k
loss = 50² = 2,500

> ⚠️ Not all Loss Functions use Square Error

---

#### Why we sum the errors

The model makes a prediction for **every** data point — not just one.

Each prediction has its own error (how far off it was).

But we need **one single number** to judge the model overall — not a separate error for each point.

So we **sum all individual errors** into one total score.

That total score tells us: "overall, how wrong is this model?"

---

#### Why we square the error

> We square errors to make them all positive — so negative errors don't cancel out positive ones when summed.

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

#### MSE Gradient — where the formula comes from

The gradient is just the [[Derivative]] of the loss function — it tells us the **slope** of the loss curve.

Remember from [[Slope of line and curve]]: the [[Derivative]] tells you how fast something changes at a specific point. Here, we're asking:

> **If I nudge this [[Weights define how much each feature matters|weight]] slightly, how much does the loss change?**

Think about it in three steps:

1. If I change a weight → my **prediction** changes (because prediction = weight × feature)
2. If my prediction changes → my **loss** changes (because loss = how far off the prediction is)
3. My ideal model has **minimal loss** → so I use the gradient to know **which direction** to adjust my weights to **decrease** the loss

That's exactly what a derivative does — measures rate of change. The gradient tells you the slope of the loss curve, so you can move **downhill** toward lower loss.

---

##### Deriving it step by step

Start with MSE for a single prediction:
$$L = (y - \hat{y})^2$$

Our prediction is a line: $\hat{y} = w \cdot x + b$

So:
$$L = (y - (w \cdot x + b))^2$$

Now take the derivative with respect to $w$ (how does loss change when we adjust the weight?):

**Step 1:** Apply the chain rule — derivative of something² = 2 × something × derivative of the inside:
$$\frac{\partial L}{\partial w} = 2(y - \hat{y}) \cdot \frac{\partial}{\partial w}(y - wx - b)$$

**Step 2:** The derivative of $(y - wx - b)$ with respect to $w$ is just $-x$:
$$\frac{\partial L}{\partial w} = 2(y - \hat{y}) \cdot (-x) = -2(y - \hat{y}) \cdot x$$

**Step 3:** Rearrange the sign:
$$\frac{\partial L}{\partial w} = 2(\hat{y} - y) \cdot x$$

For all $n$ data points, average them:

$$\frac{\partial MSE}{\partial w} = \frac{2}{n} \sum_{i=1}^{n} (\hat{y}_i - y_i) \cdot x_i$$

---

##### What the result tells us

The gradient formula has two parts multiplied together: $(\hat{y} - y) \cdot x$

**The error part** $(\hat{y} - y)$ tells us the direction:
- **Positive** (predicted too high) → gradient is positive → **decrease** the weight
- **Negative** (predicted too low) → gradient is negative → **increase** the weight

**Why "$x$ is positive" matters:** 
- The sign of the gradient depends on both the error AND the feature value $x$. 
- For features like sqft or bedrooms, $x$ is always positive, so the error alone determines the direction. 
- But some features can be negative (e.g., temperature, normalized values), which would flip the gradient's sign.

**How weights actually change:**

The update rule multiplies learning rate by the gradient (not adds/subtracts):

$$w_{new} = w_{old} - (learning\_rate \times gradient)$$

- Gradient is **positive** → subtract → weight **decreases**
- Gradient is **negative** → minus × negative = plus → weight **increases**

The gradient points in the direction of **increasing** loss — so we move **opposite** to it.

> ⚠️ The factor of 2 often gets absorbed into the learning rate in practice.

---

Read more:
- [[Gradient adjusts params to reduce loss]]
- [[Parameter is a value that defines how a system behaves]]
- [[Weights define how much each feature matters]]
- [[Derivative]]
- [[Slope of line and curve]]
