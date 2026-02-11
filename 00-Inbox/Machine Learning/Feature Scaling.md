### Definition

> **Feature scaling** is transforming features to similar numerical ranges
> ⚠️ That's why **Feature scaling** only applies to **numerical features**.

Our features have different scales:
- Age: 18-65
- Income: $20,000-$200,000
- Years of experience: 0-40

---

### The Real Problem: Learning Rate Conflict

🤔 The issue isn't that the model **can't** learn with unscaled features.

🔴 The problem is that it learns **inefficiently** and **unstably**.

**Core issue:** Gradient descent uses **ONE learning rate** for **ALL features**.

When features have different scales:
- The same learning rate is **too fast** for large features
- The same learning rate is **too slow** for small features

This causes:
1. **Slow convergence** - Takes many more iterations to reach optimal weights
2. **Unstable training** - Weights overshoot and oscillate
3. **Numerical issues** - Very large gradients can cause precision errors

---

### Complete Mathematical Example

Let's predict house price using:
- Bedrooms ($x_1$): values 2, 3, 4
- Square footage ($x_2$): values 1000, 2000, 3000

**Training data:**

| Bedrooms ($x_1$) | Sqft ($x_2$) | Price ($y$) |
|------------------|--------------|-------------|
| 2                | 1000         | $200k       |
| 3                | 2000         | $300k       |
| 4                | 3000         | $400k       |

**Model formula:**

$\hat{y} = w_1 \cdot x_1 + w_2 \cdot x_2 + b$

**Starting point:**
- Initial weights: $w_1 = 0$, $w_2 = 0$, $b = 0$
- Learning rate: $\alpha = 0.0001$

---

### Iteration 1: First Training Example

Training on: 2 bedrooms, 1000 sqft, actual price = $200,000

#### Step 1: Make Prediction

$$\hat{y} = w_1 \cdot x_1 + w_2 \cdot x_2 + b = 0 \cdot 2 + 0 \cdot 1000 + 0 = 0$$

#### Step 2: Calculate Loss (MSE)

$$MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$

For single example ($n=1$):

$$MSE = (200000 - 0)^2 = 40{,}000{,}000{,}000$$

#### Step 3: Calculate Gradients

**How to derive the gradient formula:**

We have:
- $MSE = (y - \hat{y})^2$
- $\hat{y} = w_1 x_1 + w_2 x_2 + b$

Use **chain rule** (MSE depends on $\hat{y}$, and $\hat{y}$ depends on $w_j$):
$$\frac{\partial MSE}{\partial w_j} = \frac{\partial MSE}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial w_j}$$

**Part 1:** Derivative of MSE with respect to prediction:
$$\frac{\partial MSE}{\partial \hat{y}} = \frac{\partial}{\partial \hat{y}}(y - \hat{y})^2 = 2(y - \hat{y}) \cdot (-1) = 2(\hat{y} - y)$$


**Part 2:** Derivative of prediction with respect to weight:
$$\frac{\partial \hat{y}}{\partial w_j} = \frac{\partial}{\partial w_j}(w_1 x_1 + w_2 x_2 + b) = x_j$$

**Combine using chain rule:**
$$\frac{\partial MSE}{\partial w_j} = 2(\hat{y} - y) \cdot x_j$$

**For $w_1$ (bedrooms):**
$$\frac{\partial MSE}{\partial w_1} = 2(0 - 200000) \cdot 2 = -800{,}000$$

**For $w_2$ (sqft):**
$$\frac{\partial MSE}{\partial w_2} = 2(0 - 200000) \cdot 1000 = -400{,}000{,}000$$

**Critical observation:** Gradient for sqft is **500x larger** than gradient for bedrooms!

This happens because sqft values are 500x larger than bedroom values.

#### Step 4: Update Weights

$$w_{new} = w_{old} - \alpha \cdot \frac{\partial MSE}{\partial w}$$
$$w_1 = 0 - 0.0001 \cdot (-800{,}000) = 80$$
$$w_2 = 0 - 0.0001 \cdot (-400{,}000{,}000) = 40{,}000$$

---

### The Problem Emerges

After one update:
- $w_1 = 80$ (weight for bedrooms)
- $w_2 = 40000$ (weight for sqft)

**Now predict for the SAME house (2 bedrooms, 1000 sqft):**

$$\hat{y} = 80 \cdot 2 + 40{,}000 \cdot 1000 + 0 = 160 + 40{,}000{,}000 = 40{,}000{,}160$$

**We predicted $40 million for a $200k house!**

The weight $w_2$ changed **too much** because:
1. The feature value (1000) is large
2. So the gradient ($-400,000,000$) is huge
3. Even with tiny learning rate (0.0001), the weight jumped massively

The model **overshot** the optimal value.

---

### What If We Decrease Learning Rate?

Try $\alpha = 0.000001$ (100x smaller):

**For $w_1$:** $w_1 = 0 - 0.000001 \cdot (-800{,}000) = 0.8$

**For $w_2$:** $w_2 = 0 - 0.000001 \cdot (-400{,}000{,}000) = 400$

**Prediction:** $\hat{y} = 0.8 \cdot 2 + 400 \cdot 1000 = 1.6 + 400{,}000 = 400{,}001.6$

Still predicting \$400k instead of \$200k!

Let's try even smaller: $\alpha = 0.0000001$

**For $w_1$:** $w_1 = 0 - 0.0000001 \cdot (-800{,}000) = 0.08$

**For $w_2$:** $w_2 = 0 - 0.0000001 \cdot (-400{,}000{,}000) = 40$

**Prediction:** $\hat{y} = 0.08 \cdot 2 + 40 \cdot 1000 = 0.16 + 40{,}000 = 40{,}000.16$

Now closer, but still 5x off!

**And look at $w_1$:** It only changed by 0.08

The bedroom weight will take **thousands of iterations** to reach its optimal value.

---

### The Impossible Choice

**You cannot pick a learning rate that works well for BOTH features:**

| Learning Rate | Effect on Sqft Weight     | Effect on Bedroom Weight |
|---------------|---------------------------|--------------------------|
| Large (0.01)  | Overshoots wildly         | Learns reasonably        |
| Medium (0.0001) | Still overshoots        | Learns very slowly       |
| Small (0.000001) | Learns slowly           | Barely moves             |

This is the **fundamental problem** that feature scaling solves.

---

### What is Oscillation?

> **Oscillation** is when the model keeps **bouncing above and below** the correct answer, overshooting in one direction, then overcorrecting in the other.

Think of it like pushing a swing too hard — it doesn't stop in the middle, it flies past to the other side, then back again.

This happens because the gradient **overcorrects**: the error is large → the gradient is large → the weight changes too much → now the error is large in the **opposite direction**.

---

#### Oscillation in action (simplified to sqft only)

To see the bouncing clearly, let's use one feature:

$\hat{y} = w \times x$, where $x = 1000$ (sqft), actual price = \$200k, $\alpha = 0.0000008$

Gradient formula: $\frac{\partial L}{\partial w} = 2(\hat{y} - y) \cdot x$

| Step | Weight | Prediction | Error | Gradient | What happened |
|------|--------|------------|-------|----------|---------------|
| 0 | 0 | \$0k | -\$200k | -400M | Way too low |
| 1 | 320 | \$320k | +\$120k | +240M | Overshot! Too high |
| 2 | 128 | \$128k | -\$72k | -144M | Corrected too far back |
| 3 | 243 | \$243k | +\$43k | +86M | Overshot again |
| 4 | 174 | \$174k | -\$26k | -52M | Back too far |
| 5 | 216 | \$216k | +\$16k | +31M | Still bouncing |
| 6 | 191 | \$191k | -\$9k | -19M | Getting closer... |
| 7 | 206 | \$206k | +\$6k | +11M | Still bouncing |
| 8 | 197 | \$197k | -\$3k | -7M | Almost there |
| 9 | 202 | \$202k | +\$2k | +4M | Close |

**Pattern:** Each overshoot is ~60% of the previous one. The model **does** converge, but wastes many iterations bouncing.

Now imagine a second feature (bedrooms, values 2-4) with this same learning rate — its weight **barely moves** while sqft bounces wildly. One feature oscillates, the other crawls.

> ⚠️ With an even larger learning rate, oscillations can get **bigger** each step instead of smaller. The model **diverges** — loss goes to infinity, and it never learns.

---

### Solution: Feature Scaling

When we scale both features to similar ranges (like 0-1):
- All gradients become comparable in size
- One learning rate works efficiently for all features
- Model converges quickly and stably

#### 1. Normalization (Min-Max Scaling)

Transforms features to range [0, 1]:

$$x_{scaled} = \frac{x - x_{min}}{x_{max} - x_{min}}$$

**Example for bedrooms (range 2-4):**
- Bedroom = 2: $(2-2)/(4-2) = 0$
- Bedroom = 3: $(3-2)/(4-2) = 0.5$
- Bedroom = 4: $(4-2)/(4-2) = 1$

**Example for sqft (range 1000-3000):**
- Sqft = 1000: $(1000-1000)/(3000-1000) = 0$
- Sqft = 2000: $(2000-1000)/(3000-1000) = 0.5$
- Sqft = 3000: $(3000-1000)/(3000-1000) = 1$

Now both features range from 0 to 1!

#### 2. Standardization (Z-score)

Centers data around 0 with standard deviation of 1:

$$x_{scaled} = \frac{x - \mu}{\sigma}$$

Where:
- $\mu$ = mean of the feature
- $\sigma$ = standard deviation of the feature

This is preferred when your data has outliers.

---

### Scaled Features in Action

Let's redo the training with scaled features and compare to the oscillation table.

Using the second data point: sqft = 2000, price = \$300k

After min-max scaling: $x_{scaled} = 0.5$

$\hat{y} = w \times x$, where $x = 0.5$, actual price = \$300k, $\alpha = 1.5$

**Notice:** we can use $\alpha = 1.5$ instead of $0.0000008$ — almost **2 million times larger!**

| Step | Weight | Prediction | Error | What happened |
|------|--------|------------|-------|---------------|
| 0 | 0 | \$0k | -\$300k | Starting |
| 1 | 450k | \$225k | -\$75k | Big jump, right direction |
| 2 | 563k | \$281k | -\$19k | Getting close |
| 3 | 591k | \$295k | -\$5k | Almost there |
| 4 | 598k | \$299k | -\$1k | Very close |
| 5 | 600k | \$300k | -\$0.3k | Converged |

#### Compare: unscaled vs scaled

| | Unscaled | Scaled |
|---|---|---|
| Learning rate | 0.0000008 | 1.5 |
| Iterations to converge | 9+ (still bouncing) | 5 (done) |
| Oscillation? | Yes — bounces above and below | No — smooth approach from one side |
| Error pattern | -200k → +120k → -72k → +43k... | -300k → -75k → -19k → -5k → -1k |

**Key insight:** With scaled features, the error **shrinks steadily** in one direction. No bouncing. The gradient is small enough that the learning rate doesn't cause overshooting, yet large enough to converge quickly.

This is why feature scaling matters — it's not about whether the model **can** learn, it's about learning **efficiently and stably**.

---

### Key Concepts to Understand

Before diving deeper:
- [[Parameter is a value that defines how a system behaves]]
- [[Weights define how much each feature matters]]
- [[Gradient adjusts params to reduce loss]]

---

### Related Notes

- [[Machine Learning Process Stages]]
- [[Feature is input param to make prediction]]
- [[Data Splitting to Train and Test Set]]