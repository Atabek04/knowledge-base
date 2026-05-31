---
aliases: [Domain Model vs Data Model, Domain Model]
tags: [ddd, domain-model, architecture, data-modeling, design]
created: 2026-05-31
---

### Two models, two questions

A **domain model** and a **data model** describe the same business, but answer different questions.

- **Domain model** → *"how does this thing behave, and what rules must hold?"*
- **Data model** → *"how is this thing stored and related to other stored things?"*

A relational/ERD schema is a data model. A DDD object graph with [[A domain entity is defined by a continuous identity that persists through state changes|entities]], [[A value object has no identity and is compared by the equality of its attributes|value objects]], and [[An aggregate is a cluster of objects treated as one consistency boundary|aggregates]] is a domain model.

---

### What each one optimizes for

| | Domain model | Data model |
|--|--|--|
| **Goal** | Express business behavior and invariants | Store and retrieve data efficiently |
| **Unit** | Aggregate (consistency boundary) | Table / row |
| **Holds** | Methods, rules, state transitions | Columns, keys, foreign keys |
| **Equality** | Identity (entity) or value (VO) | Primary key |
| **Driven by** | The domain experts' language | Normalization + query patterns |

---

### They are not the same shape

A single aggregate often maps to **several tables** (an `Order` and its lines).
A value object often has **no table of its own** — it's embedded as columns in the owner's row.

<mark style="background: #f9a8d4">The mismatch between these two models is the object–relational impedance mismatch</mark> — the gap that ORMs like Hibernate exist to bridge.

---

### Why keep them separate

If you let the table layout dictate your objects, business rules leak into anemic data-bags and the model stops protecting its invariants.

The domain model expresses *intent*; the data model serves *persistence*. Mapping between them is a deliberate layer, not an accident.

---

Read more:
- [[A domain entity is defined by a continuous identity that persists through state changes]]
- [[An aggregate is a cluster of objects treated as one consistency boundary]]
- [[Normalization eliminates redundancy to prevent insert update and delete anomalies]]
- [[Software Engineering Principles - MOC]]
- [[Databases - MOC]]
