---
aliases: [Data Dictionary]
tags: [data-modeling, requirements, system-analysis, documentation, database]
created: 2026-05-31
---

### What it is

A **data dictionary** is a formal catalog that defines <mark style="background: yellow">every data element in a system</mark> — its name, meaning, type, constraints, and allowed values — in one authoritative place.

It answers, for any field: *what is this, exactly, and what rules govern it?*

---

### What it documents per element

| Attribute | Example |
|--|--|
| **Name** | `order_status` |
| **Definition** | The current lifecycle state of an order |
| **Data type / format** | `ENUM`, max 20 chars |
| **Allowed values** | `PLACED, PAID, SHIPPED, DELIVERED, CANCELLED` |
| **Constraints** | NOT NULL; default `PLACED` |
| **Source / owner** | Order Service; owned by Fulfilment team |
| **Relationships** | references `orders.id` |

---

### Why a backend engineer / analyst needs it

The dictionary kills the most expensive bug class: <mark style="background: #f9a8d4">two teams meaning different things by the same word.</mark>

- Does `customer` include guests who never registered? Is `revenue` gross or net? Is a date stored UTC or local?
- A shared definition makes those answers unambiguous before code is written.

It is also the bridge between the **business glossary** (terms domain experts use) and the **physical schema** (columns the database stores) — and the seed for [[Data quality is measured along completeness accuracy consistency and timeliness|data quality]] rules and [[Data governance documents the retention archival and deletion rules for each class of data|governance]] policies.

---

### Where it lives

It ranges from a literal spreadsheet maintained by analysts, to schema comments, to a generated artifact in a data catalog tool. The form varies; the purpose — **one agreed definition per element** — does not.

---

Read more:
- [[A CRUD matrix maps entities against operations to expose missing or unowned data lifecycles]]
- [[Data quality is measured along completeness accuracy consistency and timeliness]]
- [[A data owner is accountable for a data domain while a data steward maintains its quality]]
- [[Databases - MOC]]
