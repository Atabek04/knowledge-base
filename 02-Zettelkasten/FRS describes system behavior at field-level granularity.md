---
created: 2026-04-10
aliases: [FRS, Functional Requirements Specification]
tags:
  - software-engineering/requirements
---

> <mark style="background: yellow">The FRS (Functional Requirements Specification) is the most detailed and granular document — it describes precisely how the system functions to satisfy all BRD and SRS requirements.</mark>

---

### What the FRS contains

- **Field-level specifications** — every input field, its type, length, default value
- **Exact validation rules** — "email must match regex X, max 255 chars"
- **Button behaviors** — what each UI action triggers
- **Error messages** — exact wording for every error state
- **References to UML models** — directly links to sequence and activity diagrams from Phase 6

---

### FRS vs SRS

| Aspect | SRS | FRS |
|--------|-----|-----|
| Level | System capabilities | Field-level behavior |
| Audience | Architects, leads | Developers |
| Example | "System shall validate user input" | "Email field: required, max 255 chars, regex `^[a-z]+@...`, error: 'Invalid email format'" |

<mark style="background: green">The FRS is the developer's working document — precise enough that a developer can implement without asking clarifying questions.</mark>

---

### When it's created

**Phase 7** — after detailed UML diagrams exist. The FRS references those models directly and adds the granular specifications around them.

<mark style="background: cyan">The FRS sits at the bottom of the progressive elaboration chain: BRD (why) → SRS (how) → FRS (what exactly).</mark>

---

Read more:
- [[SRS bridges business requirements and technical implementation]]
- [[BRD captures why the system is being built before any technical work begins]]
- [[Detailed UML diagrams are specification tools created after requirements are documented]]
- [[Progressive elaboration zooms requirements from business goals to implementation details]]
