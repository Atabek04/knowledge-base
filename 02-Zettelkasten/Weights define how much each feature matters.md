---
created: 2026-01-22
tags:
  - ml/fundamentals
  - ml/parameters
---

> **A weight (`w`) is a number the model learns
> :luc_arrow_right_circle: that multiplies a feature to make predictions.**

The weight tells you: **"How much does this feature affect the prediction?"**

---

**Example:** In a simple model predicting house prices:
- Parameter 1: "how much does size matter?" (weight)
- Parameter 2: "how much does location matter?" (weight)

`predicted_price = w₁ × (square_feet) + w₂ × (bedrooms) + b`

- w₁ = 100 → each square foot adds **$100** to predicted price
- w₂ = 50,000 → each bedroom adds **$50,000** to predicted price

---

How do weights get learned?

1. Start with random weights
2. Make a prediction: multiply features by weights
3. Calculate loss: is prediction close to actual answer?
4. Adjust weights slightly to reduce loss
5. Repeat thousands of times until weights are accurate

See: [[Gradient adjusts params to reduce loss]]

---

What happens after training?

**Weights are frozen and saved.** 
You use them to predict on new data.

Example: After training, w₁ = 100, w₂ = 50,000.
New house: 3000 sq ft, 4 bedrooms.
Prediction: 100 × 3000 + 50,000 × 4 = **$500,000** (before adding bias)

---

Are weights the same as parameters?

**No.** Weights ARE a type of parameter, but parameters also include bias and other settings.

Read more:
- [[Parameter is a value that defines how a system behaves]]
- [[Bias adds a baseline shift to all predictions]]