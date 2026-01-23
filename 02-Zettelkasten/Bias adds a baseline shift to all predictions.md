---
created: 2026-01-22
tags:
  - ml/fundamentals
  - ml/parameters
---

> **Bias (`b`) is a number the model learns
> :luc_arrow_right_circle: that gets added to every prediction,
> ⚠️ *regardless of features.***

Bias tells you: **"What's the baseline prediction before we consider any features?"**

---

`predicted_price = w₁ × (square_feet) + w₂ × (bedrooms) + b`

If b = 10,000:
- Empty land (0 sq ft, 0 bedrooms) → predicted = 0 + 0 + 10,000 = **$10,000**
- The baseline is $10k just for the location/foundation

Without bias, empty land would cost $0 (wrong).

---
##### Is bias also adjusted during training?

**Yes.** 
Just like weights, bias starts random and gets adjusted to minimize loss.

The model learns: 
1. "What features matter?" (weights)
2. "What's the starting point?" (bias)

---
##### Real-world intuition:

In a recipe:
- weights are like "how much salt ***per*** cup of flour"
- bias is like "always add 1 teaspoon of salt ***no matter what***."

---

Read more: 
- [[Weights define how much each feature matters]] 
- [[Parameter is a value that defines how a system behaves]]