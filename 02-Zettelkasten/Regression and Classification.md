---
created: 2026-01-23
tags:
  - ml/classification
  - ml/regression
---

# What problem types does ML solve?

> Machine learning models solve **different types of problems** based on what the output should be.

The two most common problem types are:

1. **Regression** — predict a **continuous number**
2. **Classification** — predict a **category or class**

---
## Regression

> A **regression** problem asks the model to predict a **single number** that can have any value.

Not a category. 
Not "yes/no". 
Not one of five options.

A **number on the number line**.

---
### What is a **continuous number**?

> A number that can be **any value** — including decimals, fractions, and values between whole numbers.

Think of a number line: $...,-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2...$

> **Continuous** means infinite possible values exist between any two points.

This is different from **discrete** (only specific values, like integers or categories).

---
### Examples of regression problems:

- Predicting house price: $250,000 or $250,000.50 or $250,324.73
- Predicting temperature: 72°F or 72.5°F or 72.347°F
- Predicting person's height: 180 cm or 180.5 cm or 180.237 cm

Each prediction is **one single number**. 
That number can be any value on the number line.

---
### Classification: Predicting Categories

Classification is the other most common problem type.

Examples of classification problems:

- "Is this email spam?" → only two options: Yes or No
- "Which animal is this?" → options: Cat, Dog, Bird, Fish
- "Grade A, B, C, D, or F?" → only five options

These are **<mark style="background: #BBFABBA6;">discrete categories</mark>**, not continuous numbers.

---
### Regression vs Classification

The core difference:

**Regression:** infinitely many possible answers (any real number)

**Classification:** limited set of predefined answers (categories or classes)

---

Read more:
- [[Classification outputs probability scores to express confidence in predictions]]
- [[Types of ML]]
