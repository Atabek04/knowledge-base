---
aliases: [Data Owner, Data Steward, Data Ownership]
tags: [data-governance, data-modeling, system-analysis, roles]
created: 2026-05-31
---

### Two roles, two responsibilities

Data governance splits responsibility for a body of data into two distinct roles:

- **Data Owner** — <mark style="background: yellow">accountable</mark> for a data domain: sets the rules, approves access, answers for its correctness and compliance. Usually a senior business person.
- **Data Steward** — <mark style="background: yellow">responsible</mark> for the day-to-day: enforces the owner's rules, fixes quality issues, maintains definitions. A hands-on operational role.

The classic split: the owner **decides**, the steward **does**.

---

### Why separate them

The person with the *authority* to set policy (owner) is rarely the person with the *time and proximity* to maintain data daily (steward).

Naming both makes accountability unambiguous: <mark style="background: #f9a8d4">when data is wrong, there is a named owner answerable for it and a named steward who fixes it</mark> — not a diffuse "the system" that no one is responsible for.

This is exactly the **unowned entity** gap a [[A CRUD matrix maps entities against operations to expose missing or unowned data lifecycles|CRUD matrix]] surfaces: every entity needs an owner.

---

### Owner vs Steward at a glance

| | Data Owner | Data Steward |
|--|--|--|
| **Accountable for** | Outcomes, policy, compliance | Execution, daily quality |
| **Typical person** | Business/department head | Analyst, ops, DBA |
| **Decides or does** | Decides | Does |
| **Example call** | "Marketing may not see raw PII" | Deduplicates customer records weekly |

---

Read more:
- [[Master data management enforces one trusted record for entities shared across systems]]
- [[Data quality is measured along completeness accuracy consistency and timeliness]]
- [[A CRUD matrix maps entities against operations to expose missing or unowned data lifecycles]]
- [[Databases - MOC]]
