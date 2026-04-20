---
created: 2026-04-10
aliases: [TO-BE modeling, future state process]
tags:
  - software-engineering/requirements
---

> <mark style="background: yellow">TO-BE process modeling designs the desired future state with BPMN, and simultaneously introduces the first UML artifact — the Use Case Diagram.</mark>

---

### Two deliverables in one phase

**1. TO-BE BPMN diagrams** — how the process *should* work after the system is built. These remove the bottlenecks and manual steps identified in [[AS-IS process modeling with BPMN reveals current workflow bottlenecks|AS-IS modeling]].

**2. UML Use Case Diagram** — the first UML artifact. It's high-level: showing actors, system boundaries, and major interactions.

---

### Use Case Diagrams

Use case diagrams comprise:
- **Actors** — external entities (users or organizations) that interact with the system
- **Use cases** — functions users can access within the system
- **System boundary** — what's inside vs outside the system

<mark style="background: green">The Use Case Diagram shows *which functions users can access* — it's a map of system capabilities from the user's perspective.</mark>

---

### Why these two together

The TO-BE BPMN shows the redesigned business process. The Use Case Diagram shows which parts of that process the *system* will handle.

<mark style="background: cyan">Together, they answer: "How should work flow?" (BPMN) and "What does the system do within that flow?" (Use Cases).</mark>

---

Read more:
- [[AS-IS process modeling with BPMN reveals current workflow bottlenecks]]
- [[BPMN comes before UML because process understanding precedes system design]]
- [[User stories express requirements as role-action-benefit statements]]
