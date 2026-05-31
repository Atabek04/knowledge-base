---
aliases: [1NF, First Normal Form]
tags: [database, data-modeling, relational-model, normalization]
created: 2026-05-31
---

### The rule

A table is in **first normal form (1NF)** when every column holds a single <mark style="background: yellow">atomic value</mark> and there are no repeating groups.

One cell = one value. No lists, no `"phone1, phone2, phone3"`, no `tags` column stuffed with comma-separated items.

---

### What violates 1NF

| order_id | products |
|--|--|
| 1 | `"apple, bread, milk"` |

The `products` cell holds a list — a **repeating group**. You can't query "how many orders contain milk?" without parsing strings.

Also a violation: columns like `product_1`, `product_2`, `product_3` — the same repeating group spread across columns instead of inside one.

---

### The 1NF version

Split the repeating group into its own rows:

| order_id | product |
|--|--|
| 1 | apple |
| 1 | bread |
| 1 | milk |

Now each fact (one product on one order) is a single atomic row the database can index, filter, and join on.

---

### Why it's the foundation

1NF is the precondition for everything else.

<mark style="background: #f9a8d4">You cannot reason about functional dependencies — the basis of 2NF and 3NF — until values are atomic.</mark> The higher normal forms assume you are already in 1NF.

---

Read more:
- [[Normalization eliminates redundancy to prevent insert update and delete anomalies]]
- [[Second normal form removes partial dependencies on part of a composite key]]
- [[Databases - MOC]]
