---
aliases: [3NF, Third Normal Form, transitive dependency]
tags: [database, data-modeling, relational-model, normalization]
created: 2026-05-31
---

### The rule

A table is in **third normal form (3NF)** when it is in 2NF **and** no non-key column depends on another <mark style="background: yellow">non-key column</mark>.

Every non-key column must depend on *the key, the whole key, and nothing but the key.*

---

### What a transitive dependency is

A **transitive dependency** is `key → A → B`: the key determines `A`, and `A` in turn determines `B`. So `B` depends on the key only *through* `A`.

| employee_id | dept_id | dept_name |
|--|--|--|

- `dept_id` depends on `employee_id` ✓
- `dept_name` depends on `dept_id`, **not directly** on `employee_id` — <mark style="background: #f9a8d4">transitive dependency</mark>

---

### Why it's a problem

`dept_name` repeats for every employee in the department.
Rename a department → update every employee row (update anomaly). Delete the last employee → lose the department's name (delete anomaly).

---

### The 3NF fix

Pull the transitively-dependent column into a table keyed by the column it really depends on:

- `employees(employee_id, dept_id)`
- `departments(dept_id, dept_name)`

`dept_name` now lives once, keyed by `dept_id` — the thing it actually depends on.

---

### 2NF vs 3NF in one line

- **2NF** removes dependency on *part of the key*.
- **3NF** removes dependency on *a non-key column*.

3NF is the practical target for most OLTP schemas — far enough to kill anomalies, not so far it hurts.

---

Read more:
- [[Second normal form removes partial dependencies on part of a composite key]]
- [[Boyce-Codd normal form requires every determinant to be a candidate key]]
- [[Databases - MOC]]
