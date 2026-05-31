TARGET DECK: Tech-KB::Databases::Normalization
Tags: database normalization data-modeling
**Chapter:** Database Normalization
**Related:** [[Databases - MOC]]

---

START
Coding Questions
What is database normalization and what does it organize data to achieve?
Back:
**Normalizing** = organizing columns into tables so each fact is stored in **exactly one place**.

- Removes redundancy step by step via normal forms (1NF → 2NF → 3NF → BCNF)
- Each form removes a specific harmful **dependency**
- Goal: no duplicated facts → no contradictions
Tags: database normalization
END

START
Coding Questions
What are the three anomalies that normalization prevents? Give a one-line example of each.
Back:
- **Insert anomaly** — can't record one fact without another (can't add a course until a student enrols)
- **Update anomaly** — a duplicated fact must change in all rows or data contradicts itself (professor's office updated in 40 of 50 rows)
- **Delete anomaly** — deleting a row destroys an unrelated fact (last student drops → course vanishes)
Tags: database normalization anomalies
END

START
Coding Questions
What does first normal form (1NF) require?
Back:
Every column holds a single **atomic value**, with **no repeating groups**.

- One cell = one value (no `"apple, bread, milk"`)
- No `product_1`, `product_2`, `product_3` columns
- It's the precondition for reasoning about functional dependencies (2NF/3NF)
Tags: database normalization 1nf
END

START
Coding Questions
What dependency does second normal form (2NF) remove, and when can it be violated?
Back:
2NF removes **partial dependencies** — a non-key column depending on only **part** of a composite key.

- Only relevant when the key is **composite**
- e.g. key `(student_id, course_id)`: `course_title` depends only on `course_id` → violation
- Fix: move it to a table keyed by the part it depends on
Tags: database normalization 2nf
END

START
Coding Questions
What dependency does third normal form (3NF) remove?
Back:
3NF removes **transitive dependencies** — a non-key column depending on **another non-key column** (`key → A → B`).

- e.g. `employee_id → dept_id → dept_name`; `dept_name` depends on the key only *through* `dept_id`
- Fix: pull `dept_name` into a `departments(dept_id, dept_name)` table
- Mnemonic: depend on *the key, the whole key, and nothing but the key*
Tags: database normalization 3nf
END

START
Coding Questions
How does BCNF differ from 3NF, and when does the difference matter?
Back:
**BCNF**: for *every* dependency `X → Y`, `X` must be a **candidate key** (every determinant is a key).

- 3NF's loophole: allows a non-key column to determine a candidate-key attribute
- Only bites with **multiple overlapping candidate keys** (e.g. `teacher → subject` while key is `(student, subject)`)
- BCNF is informally "3.5NF"
Tags: database normalization bcnf
END

START
Coding Questions
What is denormalization and what trade-off does it make?
Back:
**Denormalizing** = deliberately reintroducing redundancy into a normalized schema to make **reads faster**.

- Techniques: duplicate a column, precompute aggregates, materialized views
- Buys **read speed** with **write complexity** — copies can drift, must be kept in sync
- Default in OLAP/analytics (star schemas, wide tables)
Tags: database normalization denormalization performance
END

START
Coding Questions
What redundancy do 4NF and 5NF address?
Back:
- **4NF** removes **multivalued dependencies** — one key independently determines two separate value sets (skills × languages → Cartesian-product rows). Fix: split into two tables.
- **5NF** removes **join dependencies** — a table losslessly splits into 3+ tables but no two.

Most real schemas stop at 3NF/BCNF; awareness is enough.
Tags: database normalization 4nf 5nf
END
