---
aliases: [BCNF, Boyce-Codd Normal Form, determinant]
tags: [database, data-modeling, relational-model, normalization]
created: 2026-05-31
---

### The rule

**Boyce-Codd normal form (BCNF)** is a stricter 3NF: for *every* functional dependency `X → Y`, `X` must be a <mark style="background: yellow">candidate key</mark>.

A **determinant** is any column (or set) that determines another. BCNF says: every determinant must be able to serve as a key. No exceptions.

---

### Why 3NF isn't always enough

3NF has a loophole: it permits a non-key column to determine *part of a key* — a candidate-key attribute. BCNF closes it.

This only bites when a table has **multiple overlapping candidate keys**. Example — a student takes subjects, each subject taught by one teacher, each teacher teaches one subject:

| student | subject | teacher |
|--|--|--|

- Candidate key: `(student, subject)`
- But `teacher → subject` — a non-key determinant. <mark style="background: #f9a8d4">3NF allows this; BCNF forbids it.</mark>

---

### The BCNF fix

Decompose so every determinant is a key:

- `teaches(teacher, subject)` — `teacher` is the key
- `enrols(student, teacher)`

Now no determinant is a non-candidate-key column.

---

### Practical note

BCNF is "3.5NF" — most schemas in clean 3NF are already in BCNF.

You only reach for it when overlapping candidate keys create a hidden anomaly that 3NF missed. Pushing further (4NF/5NF) is rarer still — see the awareness note.

---

Read more:
- [[Third normal form removes transitive dependencies between non-key columns]]
- [[Fourth and fifth normal forms remove multivalued and join dependencies]]
- [[Databases - MOC]]
