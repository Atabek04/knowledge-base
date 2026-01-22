
Function = takes input, produces output.

Input = image of cat
Output = `cat` *(or probability: 95% cat, 3% dog, 2% other)*

---

> A **parameter** is a **value that defines how a system behaves**.

In a recipe, the amount of salt or sugar is a parameter
changing it changes the taste.	

> In ML, **parameters are the numbers the model learns from data** to make predictions.

> The model **adjusts these numbers** during training to minimize error.

---
##### Where do parameters come from?

Initially: **random numbers** (or **smart guesses**). 
The model starts blind.

During training, the model adjusts them by calculating loss and moving downhill.

After training, the final numbers are saved and used forever.

---

##### Parameters are divided into two

1. **Weights** - multiply features to show how much they matter.
2. **Biases** - add a baseline shift to all predictions.

Read more:
- [[Weights define how much each feature matters]]
- [[Bias adds a baseline shift to all predictions]]

---
In machine learning, our function is the **loss function**. 
It takes model parameters as input and outputs how wrong the model is.

Read more: [[Loss function - formula that measures how wrong the model is]]

---
### Training Process - Supervised Learning

**Step 1:** 
	Feed the model an example
	(e.g., "house with 100m², 2 bedrooms → actual price $300k").
**Step 2:** 
	Model makes a prediction with current parameters 
	(maybe it guesses $250k).
**Step 3:** 
	Calculate **how wrong** it was 
	(error = $50k off).
**Step 4:** 
	Adjust the parameters slightly to reduce that error.
**Step 5:** 
	Repeat with thousands/millions of examples until predictions get accurate.