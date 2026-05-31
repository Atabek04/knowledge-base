---
aliases: [Master Data Management, MDM, Golden Record]
tags: [data-governance, data-modeling, system-analysis, integration]
created: 2026-05-31
---

### What is master data?

**Master data** is the core, shared business entities that many systems reference: customers, products, suppliers, employees, accounts.

It is contrasted with *transactional* data (orders, payments) — master data is the **nouns** the transactions act on.

---

### Why duplicates and inconsistencies arise

Each system tends to keep its own copy of the same entity:

- CRM has "Acme Corp", billing has "ACME Corporation", support has "Acme Inc."
- A customer updates their address in one app; the other three never hear about it.

Without coordination, <mark style="background: #f9a8d4">the same real-world entity fragments into conflicting records</mark> across systems, and no one can answer "how many customers do we actually have?"

---

### What MDM enforces

**Master Data Management (MDM)** is the discipline and tooling that establishes <mark style="background: yellow">one trusted, authoritative record per entity — the "golden record"</mark> — and keeps every system aligned to it.

It works by:
- **Matching & merging** duplicate records into one
- Defining a **system of record** (the authoritative source for each entity)
- **Propagating** changes so updates reach every consumer
- Applying [[A data owner is accountable for a data domain while a data steward maintains its quality|ownership and stewardship]] so someone governs the golden record

---

### Relation to MDM vs normalization

[[Normalization eliminates redundancy to prevent insert update and delete anomalies|Normalization]] removes duplication *within one database*. MDM removes duplication *across many independent systems* — the same goal of "one fact, one place" raised to the enterprise level.

---

Read more:
- [[A data owner is accountable for a data domain while a data steward maintains its quality]]
- [[Data quality is measured along completeness accuracy consistency and timeliness]]
- [[Normalization eliminates redundancy to prevent insert update and delete anomalies]]
- [[Databases - MOC]]
