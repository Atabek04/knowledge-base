---
aliases: [Normalization, Database Normalization]
tags: [database, data-modeling, relational-model, normalization]
created: 2026-05-31
---

### What is normalization?

**Normalization** is the process of organizing columns into tables so that <mark style="background: yellow">each fact is stored in exactly one place</mark>.

It works by removing redundancy step by step through a series of **normal forms** (1NF, 2NF, 3NF, BCNF…), each removing a specific kind of harmful dependency.

---

### The problem: anomalies

Redundancy isn't just wasted space — it lets the database hold **contradictory data**. Three classic anomalies appear when the same fact is duplicated across rows:

**Insert anomaly**
You can't record one fact without also having another.
*Can't add a new course until at least one student enrols in it* — because course data lives in the student-enrolment row.

**Update anomaly**
A fact stored in many rows must be changed in **all** of them, or the data contradicts itself.
*A professor's office moves; you update 40 of 50 rows → 10 rows now show the wrong office.*

**Delete anomaly**
Deleting a row destroys an **unrelated** fact stored only in that row.
*The last student drops a course → the course itself vanishes from the database.*

---

### How normalization fixes them

Each anomaly comes from storing two independent facts in one row.

Normalization <mark style="background: #93d4d4">splits those facts into separate tables linked by keys</mark>, so each fact lives once. Update it in one place; it's consistent everywhere by reference.

---

### The trade-off

More tables means more JOINs to reassemble data, which costs read performance.

That's why analytics systems deliberately go the other way — see [[Denormalization trades write integrity for read performance by reintroducing redundancy|denormalization]].

---

Read more:
- [[First normal form requires atomic column values with no repeating groups]]
- [[Second normal form removes partial dependencies on part of a composite key]]
- [[Third normal form removes transitive dependencies between non-key columns]]
- [[Denormalization trades write integrity for read performance by reintroducing redundancy]]
- [[Databases - MOC]]
