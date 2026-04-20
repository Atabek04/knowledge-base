---
created: 2026-04-10
aliases: [progressive elaboration, requirements zoom-in]
tags:
  - software-engineering/requirements
---

> <mark style="background: yellow">Progressive elaboration is the core principle of requirements engineering — you start broad (WHY) and progressively zoom into detail (HOW, then WHAT exactly).</mark>

---

### The zoom-in spine

Requirements follow a natural narrowing path:

1. **BRD** — high-level business requirements (WHY are we building this?)
2. **SRS** — detailed functional and non-functional requirements (HOW will it work?)
3. **FRS** — granular functional requirements with data flows and UML (WHAT exactly does each piece do?)

Each level adds precision while staying traceable to the level above.

---

### Traceability backbone

A well-structured project traces a chain:

**Business goals → BRD scope → PRD features → FRD behaviors → system requirements → test cases**

<mark style="background: cyan">This chain is your traceability backbone — every low-level requirement should trace back to a business goal, and forward to a test case that validates it.</mark>

---

### Not a waterfall — a spiral

Progressive elaboration doesn't mean "write everything, then model everything."

<mark style="background: pink">Documents and models are interleaved at every level.</mark> Each phase produces a specific artifact that feeds the next. You elaborate as you learn — requirements analysis happens during elicitation, not after it.

---

Read more:
- [[BRD captures why the system is being built before any technical work begins]]
- [[SRS bridges business requirements and technical implementation]]
- [[FRS describes system behavior at field-level granularity]]
- [[Requirements traceability matrix links business goals to test cases]]
- [[Requirements documents and models are interleaved not sequential]]
