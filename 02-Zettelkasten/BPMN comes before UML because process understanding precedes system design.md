---
created: 2026-04-10
aliases: [BPMN before UML, BPMN vs UML]
tags:
  - software-engineering/requirements
---

> <mark style="background: yellow">BPMN comes before UML in requirements engineering. You must understand the business process before you can design the system that supports it.</mark>

---

### Why this ordering matters

- **BPMN** is business-facing and process-oriented — it shows how work flows through an organization
- **UML** is system-facing and object-oriented — it shows how software components interact

<mark style="background: pink">A critical mistake many beginners make: jumping to UML sequence diagrams or class diagrams before understanding the business process they're automating.</mark>

---

### BPMN as an elicitation tool

BPMN diagrams serve as **elicitation and analysis tools** — they help you discover and validate requirements with stakeholders.

Understanding a BPMN process flow doesn't require methodological knowledge. It's largely intuitive, which makes it ideal for business stakeholder workshops.

---

### UML as a specification tool

Detailed UML (sequence, class, activity diagrams) are **specification tools** — they formalize requirements that are already understood and documented.

<mark style="background: cyan">The rule: BPMN and high-level Use Case Diagrams help you *discover* requirements. Detailed UML helps you *specify* them.</mark>

---

### The exception — Use Case Diagrams

UML Use Case Diagrams are the one UML artifact that appears early (Phase 3, alongside TO-BE BPMN). They're high-level enough to serve as an elicitation tool rather than a specification tool.

---

Read more:
- [[AS-IS process modeling with BPMN reveals current workflow bottlenecks]]
- [[TO-BE process modeling redesigns workflows alongside UML use case diagrams]]
- [[Detailed UML diagrams are specification tools created after requirements are documented]]
