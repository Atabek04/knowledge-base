---
aliases: [2NF, Second Normal Form, partial dependency]
tags: [database, data-modeling, relational-model, normalization]
created: 2026-05-31
---

### The rule

A table is in **second normal form (2NF)** when it is in 1NF **and** every non-key column depends on the <mark style="background: yellow">whole primary key</mark>, not just part of it.

2NF only has teeth when the key is **composite** (made of more than one column). With a single-column key, partial dependency is impossible, so 1NF tables with simple keys are already in 2NF.

---

### What a partial dependency is

A **partial dependency** is when a non-key column depends on only *part* of a composite key.

Table `(student_id, course_id)` as the key:

| student_id | course_id | student_name | course_title | grade |
|--|--|--|--|--|

- `grade` depends on **both** `student_id` *and* `course_id` — correct
- `student_name` depends on **only** `student_id` — <mark style="background: #f9a8d4">partial dependency</mark>
- `course_title` depends on **only** `course_id` — partial dependency

---

### Why it's a problem

`course_title` is duplicated for every student in that course → update anomaly.
You can't add a course with no students enrolled → insert anomaly.

These are the same [[Normalization eliminates redundancy to prevent insert update and delete anomalies|anomalies]] normalization exists to kill.

---

### The 2NF fix

Move each partially-dependent column to a table keyed by the part it actually depends on:

- `students(student_id, student_name)`
- `courses(course_id, course_title)`
- `enrolments(student_id, course_id, grade)`

Now every non-key column depends on its table's full key.

---

Read more:
- [[First normal form requires atomic column values with no repeating groups]]
- [[Third normal form removes transitive dependencies between non-key columns]]
- [[Databases - MOC]]
