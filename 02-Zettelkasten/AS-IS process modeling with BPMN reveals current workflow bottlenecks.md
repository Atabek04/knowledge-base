---
created: 2026-04-10
aliases: [AS-IS modeling, current state BPMN]
tags:
  - software-engineering/requirements
---

> <mark style="background: yellow">AS-IS process modeling maps the current-state workflows using BPMN to identify bottlenecks and inefficiencies before designing any solution.</mark>

---

### Why model the current state first

Although there's always a temptation to jump straight into the software solution or functional requirements, it almost always makes sense to **first analyze the existing business process**.

Without understanding how things work today, you risk:
- Automating a broken process (making it faster but still wrong)
- Missing critical edge cases that users handle manually
- Building features nobody needs while ignoring real pain points

---

### What you produce

A set of **BPMN diagrams** showing:
- Current workflows end-to-end
- Handoff points between roles/departments
- Decision points and branches
- <mark style="background: green">Bottlenecks, manual steps, and inefficiencies (the problems worth solving)</mark>

---

### When this happens

This is **Phase 2** — immediately after the BRD is signed off. The BRD tells you WHY you're building something. AS-IS modeling shows you WHAT currently exists.

<mark style="background: cyan">This is the first time modeling enters the requirements process — and it's BPMN, not UML.</mark>

---

Read more:
- [[BRD captures why the system is being built before any technical work begins]]
- [[BPMN comes before UML because process understanding precedes system design]]
- [[TO-BE process modeling redesigns workflows alongside UML use case diagrams]]
