---
created: 2026-04-10
aliases: [RTM, requirements traceability matrix, traceability matrix]
tags:
  - software-engineering/requirements
---

> <mark style="background: yellow">A Requirements Traceability Matrix (RTM) links every requirement backward to its business goal (BRD) and forward to its test cases — ensuring nothing is built without justification and nothing goes untested.</mark>

---

### What it traces

| Column | Purpose |
|--------|---------|
| **Business goal** (BRD) | Why does this requirement exist? |
| **Requirement ID** (SRS/FRS) | What exactly is being built? |
| **Design artifact** (UML) | How is it modeled? |
| **Test case** | How do we verify it works? |

---

### Why it matters

<mark style="background: pink">Without traceability, two things go wrong:</mark>

1. **Gold plating** — features get built that trace to no business goal (wasted effort)
2. **Coverage gaps** — requirements exist that have no corresponding test case (untested behavior)

---

### When it's created

**Phase 8** — alongside prototyping. Wireframes or interactive prototypes visually validate the FRS, while the RTM validates logical completeness.

<mark style="background: green">The RTM is the quality assurance backbone of requirements engineering — it proves completeness in both directions.</mark>

---

Read more:
- [[Progressive elaboration zooms requirements from business goals to implementation details]]
- [[BRD captures why the system is being built before any technical work begins]]
- [[FRS describes system behavior at field-level granularity]]
