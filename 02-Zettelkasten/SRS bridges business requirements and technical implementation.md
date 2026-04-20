---
created: 2026-04-10
aliases: [SRS, Software Requirements Specification]
tags:
  - software-engineering/requirements
---

> <mark style="background: yellow">The SRS (Software Requirements Specification) bridges business and development — it translates what the business wants (BRD) into how the system will achieve it.</mark>

---

### What the SRS contains

- **Functional requirements** — what the system must do
- **Non-functional requirements** — performance, security, scalability constraints
- **Use case descriptions** — detailed narratives for each use case
- **System constraints** — technical limitations and dependencies
- **High-level architecture** — overall system structure

---

### How the SRS is created

The SRS is derived from the [[BRD captures why the system is being built before any technical work begins|BRD]] after business analysts interact with the client regarding project requirements.

<mark style="background: cyan">The SRS answers "HOW" — it describes the basic structure and stages of project implementation.</mark>

---

### SRS vs BRD vs FRS

| Document | Question | Level | Audience |
|----------|----------|-------|----------|
| **BRD** | WHY? | Business goals | Client, sponsors |
| **SRS** | HOW? | System capabilities | Dev team, architects |
| **FRS** | WHAT exactly? | Field-level behavior | Developers |

<mark style="background: green">The SRS sits in the middle — technical enough for developers to plan, business-readable enough for stakeholders to validate.</mark>

---

### When it's created

**Phase 5** — after user stories and use case diagrams have captured stakeholder needs. The SRS elaborates the BRD into technical modules.

---

Read more:
- [[BRD captures why the system is being built before any technical work begins]]
- [[FRS describes system behavior at field-level granularity]]
- [[User stories express requirements as role-action-benefit statements]]
- [[Progressive elaboration zooms requirements from business goals to implementation details]]
