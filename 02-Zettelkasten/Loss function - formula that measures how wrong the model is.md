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
	
2. **Problem if we don’t square:**
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

Read more:
- [[Gradient adjusts params to reduce loss]]
- [[Parameter is a value that defines how a system behaves]]