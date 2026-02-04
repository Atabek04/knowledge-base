### Definition

> **Feature scaling** is transforming features to similar numerical ranges

> ⚠️ That's why **Feature scaling** only applies to **numerical features**.

Our features have different scales:
- Age: 18-65
- Income: $20,000-$200,000
- Years of experience: 0-40

---
### Problem:

Algorithms treat larger numbers as more important.

First we should understand, how models calculate predictions:
- [[Parameter is a value that defines how a system behaves]]
- [[Weights define how much each feature matters]]
- [[Gradient adjusts params to reduce loss]]

**Example problem:**

Predicting house price using:
- Bedrooms: 2, 3, 4
- Square footage: 1000, 2000, 3000

**Without scaling:**
- Change in bedrooms: +1 (goes from 2→3)
- Change in sqft: +1000 (goes from 1000→2000)

Algorithm sees sqft changes as **1000x bigger** than bedroom changes.

Model thinks: "*Sqft matters way more!*" (even if bedrooms are equally important)

---
### Solution

#### 1. Normalization (Min-Max Scaling)

- Squeeze values between 0 and 1
- Formula: `(x - min) / (max - min)`

Example:

#### 2. Standardization (Z-score)

- Center around 0, standard deviation of 1
- Formula: `(x - mean) / standard_deviation`

---

Questions:
what's the point of transforming features to similar numberica ranges?

<mark style="background: #FF5582A6;">Why algorithms treat large numbers as more important</mark>

when you said: Scale everything to comparable range (like 0-1).
what does `comparable range` means? is it some sort of groupping vluaes
or is it just mapping some unique values to samller numbers?

I want you to show example of problem and solution of it