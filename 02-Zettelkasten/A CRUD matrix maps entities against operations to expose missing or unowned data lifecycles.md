---
aliases: [CRUD Matrix, CRUD Analysis]
tags: [data-modeling, requirements, system-analysis, documentation]
created: 2026-05-31
---

### What it is

A **CRUD matrix** is a grid that maps **entities** (or data elements) against the **operations** performed on them — **C**reate, **R**ead, **U**pdate, **D**elete — usually broken down by which process, function, or actor performs each.

Rows = entities. Columns = processes (or actors). Cells = the CRUD letters that process applies.

---

### What it looks like

| Entity \ Process | Register | Place Order | Ship Order | Monthly Report |
|--|--|--|--|--|
| **Customer** | C | R | R | R |
| **Order** | — | C | RU | R |
| **Invoice** | — | C | — | R |
| **Product** | — | R | R | R |

---

### What it reveals

The matrix is a **completeness check** — gaps in the grid are design smells:

- <mark style="background: #f9a8d4">An entity with no **C**</mark> → who creates this data? It's read but never written (missing process or external source unaccounted for).
- <mark style="background: #f9a8d4">An entity with no **D** or no **U**</mark> → can stale data ever be corrected or removed? (often a retention/governance gap)
- <mark style="background: #f9a8d4">An entity created by no one but read everywhere</mark> → an **unowned entity**; nobody is responsible for it.
- A process touching almost every entity → a possible **god process** doing too much.

---

### Why it's useful to an engineer / analyst

It cross-checks the process model against the [[A data dictionary is the authoritative catalog defining every data element and its rules|data model]]: every entity should have a clear lifecycle (created, updated, eventually archived/deleted) owned by some process.

<mark style="background: #93d4d4">It connects requirements to ownership</mark> — surfacing entities that need a [[A data owner is accountable for a data domain while a data steward maintains its quality|data owner]] before they fall through the cracks.

---

Read more:
- [[A data dictionary is the authoritative catalog defining every data element and its rules]]
- [[A data owner is accountable for a data domain while a data steward maintains its quality]]
- [[AS-IS process modeling with BPMN reveals current workflow bottlenecks]]
- [[Databases - MOC]]
