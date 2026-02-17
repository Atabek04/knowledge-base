---
created: 2026-02-12
aliases: [Encoding Categorical Data, Categorical Encoding]
tags:
  - ml/preprocessing
---

> **Categorical data** is data that represents a fixed set of groups or categories — like "male"/"female" or "France"/"Germany". Values are labels, not numbers you can do math on.

> Not every string column is categorical. If values are unique per row (like names or IDs), they don't represent repeating groups — they're just identifiers and are typically [[Irrelevant or unique columns should be dropped before training|dropped]] before encoding.

ML algorithms are math — they multiply, sum, and compare **numbers**. They can't do math on "France" or "Germany".

A model sees `y = w1 * age + w2 * salary + w3 * country`. What's `w3 * "France"`? Nothing — it breaks.

Encoding converts categories into numbers so the model can actually compute with them.

---

### Two main methods

- [[Label encoding assigns an integer to each category]]
- [[One-hot encoding creates a binary column for each category]]

---

Read more:
- [[Missing data must be handled because most ML algorithms cannot compute with NaN]]
- [[Feature is an input variable the model uses to make predictions]]
- [[Irrelevant or unique columns should be dropped before training]]
- [[Machine Learning MOC]]
