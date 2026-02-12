---
created: 2026-02-12
aliases: [Encoding Categorical Data, Categorical Encoding]
tags:
  - ml/preprocessing
---

> ML algorithms are math — they multiply, sum, and compare **numbers**. They can't do math on "France" or "Germany".

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
- [[Machine Learning MOC]]
