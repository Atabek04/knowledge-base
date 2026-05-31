---
aliases: [4NF, 5NF, multivalued dependency, join dependency]
tags: [database, data-modeling, relational-model, normalization]
created: 2026-05-31
---

### Beyond BCNF

After [[Boyce-Codd normal form requires every determinant to be a candidate key|BCNF]], two higher normal forms exist. You rarely apply them by name, but knowing the failure they catch is useful.

---

### Fourth normal form (4NF) — multivalued dependencies

A **multivalued dependency** is when one key independently determines **two separate sets** of values.

A person has many `skills` and many `languages`, unrelated to each other. Storing both in one table forces a row for every *combination*:

| person | skill | language |
|--|--|--|
| Ali | Java | English |
| Ali | Java | Arabic |
| Ali | SQL | English |
| Ali | SQL | Arabic |

That Cartesian product is pure redundancy. <mark style="background: yellow">4NF splits the two independent multivalued facts into separate tables</mark> — `person_skills` and `person_languages`.

---

### Fifth normal form (5NF) — join dependencies

**5NF** (project-join normal form) handles cases where a table can be losslessly split into **three or more** smaller tables, but not into any two of them.

It removes redundancy that only shows up when a relationship among three entities can be reconstructed by joining pairwise tables. In practice this is rare and mostly of theoretical interest.

---

### Why awareness is enough

<mark style="background: #f9a8d4">Almost every real schema stops at 3NF or BCNF.</mark>

4NF/5NF violations are uncommon, and when they appear the fix is the same instinct as always: *one independent fact per table.* You don't need to memorize them — you need to recognize a Cartesian-product table when you see one.

---

Read more:
- [[Boyce-Codd normal form requires every determinant to be a candidate key]]
- [[Normalization eliminates redundancy to prevent insert update and delete anomalies]]
- [[Databases - MOC]]
