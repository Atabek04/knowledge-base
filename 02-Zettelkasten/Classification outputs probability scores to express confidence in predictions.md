---
created: 2026-01-23
tags:
  - ml/classification
  - ml/probability
---

## What is Probability in ML?

> A **probability** is a **number between 0 and 1** (or 0% to 100%) that represents **how likely** something is.

In ML, it answers: "How confident is the model in this prediction?"

> $P(\text{prediction}) = \text{confidence level}$

Example probabilities:
- 0.95 (95%) = very confident
- 0.70 (70%) = fairly confident
- 0.52 (52%) = barely confident
- 0.10 (10%) = very unconfident

---
## How Classification Uses Probability

A **classification** model doesn't just pick a category.

It assigns a **probability** — a percentage — to each possible category.

This probability tells you **how confident** the model is.

---

### Email Spam Example

**<mark style="background: #BBFABBA6;">Without probability:</mark>**

- Input: "You won $1 million!!!"
- Output: `SPAM`

Model commits. 
Spam or not spam. 
Binary. 
No confidence information.

**<mark style="background: #BBFABBA6;">With probability:</mark>**

Compare these two predictions:

- Input: 
	- "You won $1 million!!!"
	- `95% spam, 5% not spam` 
	- (very confident)
- Input: 
	- "Meeting at 3pm tomorrow"
	- `52% spam, 48% not spam` 
	- (barely confident, almost coin flip)

Both are "spam" predictions. 
But the confidence is **completely different**.

---

Why does confidence matter?

> Because **different situations have different risk levels**.

---

### Risk-based decisions with custom thresholds

**Scenario 1: Email spam filter (low risk)**
- Set threshold: only auto-delete if **≥ 90% spam**

If you auto-delete at 52%, you might delete legitimate emails (risky).
If you require 90%, you're safe: only delete when very confident.

---

**Scenario 2: Cancer detection (high risk)**
- Set threshold: alert doctor if **≥ 99% cancer**

If you alert at 70%, you cause unnecessary panic.
If you require 99%, you miss real cancers (even riskier).

---

**The power of probability:**

You control **when to act** based on **how confident** the model is.

Different applications need different thresholds
**Without probability**, you have no control. The model decides, period.

**With probability**, you set the confidence bar based on **your risk tolerance**.

---

Read more:
- [[Regression and Classification]]
- [[Types of ML]]
