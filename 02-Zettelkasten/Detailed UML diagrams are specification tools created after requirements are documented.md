---
created: 2026-04-10
aliases: [detailed UML, UML specification phase]
tags:
  - software-engineering/requirements
---

> <mark style="background: yellow">Detailed UML diagrams (sequence, class, activity, state machine) are specification tools — they come after requirements are understood and documented in the SRS.</mark>

---

### Why not earlier

<mark style="background: pink">The most common mistake: drawing sequence diagrams before having an SRS.</mark>

For a sequence diagram to be useful, the use case diagram must be finalized. Otherwise, rework is inevitable when use cases are revised.

---

### What you produce at this phase

- **Activity Diagrams** — detailed workflow logic per use case
- **Sequence Diagrams** — object-to-object interactions, API calls, method names
- **Class Diagrams / ERDs** — data model, entity relationships
- **State Machine Diagrams** — lifecycle of key objects (e.g., Order: created → paid → shipped → delivered)

<mark style="background: green">A sequence diagram describes which systems are involved and provides the names of APIs and the method of calling them — this is developer-level specification.</mark>

---

### The process

Having a set business process from earlier phases, you meet with analysts or developers to specify the details. Each model elaborates a specific requirement from the SRS.

<mark style="background: cyan">Every model should be grounded in a written requirement it's elaborating — you don't model in a vacuum.</mark>

---

### When this happens

**Phase 6** — after the SRS is complete. These diagrams directly feed into the [[FRS describes system behavior at field-level granularity|FRS]].

---

Read more:
- [[BPMN comes before UML because process understanding precedes system design]]
- [[SRS bridges business requirements and technical implementation]]
- [[FRS describes system behavior at field-level granularity]]
- [[TO-BE process modeling redesigns workflows alongside UML use case diagrams]]
