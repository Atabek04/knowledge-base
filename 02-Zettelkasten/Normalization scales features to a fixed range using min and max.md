---
created: 2026-02-12
aliases: [Normalization, MinMaxScaler, Min-Max Scaling]
tags:
  - ml/preprocessing
---

> **Normalization** (Min-Max Scaling) transforms features to range [0, 1].

$$x_{scaled} = \frac{x - x_{min}}{x_{max} - x_{min}}$$

---

### Examples

**Bedrooms (range 2-4):**
- Bedroom = 2: $(2-2)/(4-2) = 0$
- Bedroom = 3: $(3-2)/(4-2) = 0.5$
- Bedroom = 4: $(4-2)/(4-2) = 1$

**Sqft (range 1000-3000):**
- Sqft = 1000: $(1000-1000)/(3000-1000) = 0$
- Sqft = 2000: $(2000-1000)/(3000-1000) = 0.5$
- Sqft = 3000: $(3000-1000)/(3000-1000) = 1$

<mark style="background: green">Now both features range from 0 to 1!</mark>

---

Read more:
- [[Feature scaling transforms features to similar ranges for efficient training]]
- [[Standardization centers features around zero using mean and standard deviation]]
