---
created: 2026-04-10
aliases: [user stories, user story format]
tags:
  - software-engineering/requirements
---

> <mark style="background: yellow">User stories capture requirements in a simple format: **As a [role], I want [action], so that [benefit]** — each with acceptance criteria defining "done."</mark>

---

### Structure

Each story follows:

```
As a [role], I want [action], so that [benefit].
```

Plus **acceptance criteria** — the DONE WHEN conditions that make the story testable.

The highest-level **Epic User Story** represents the overall project objective. Epics break down into smaller stories.

---

### What user stories clarify

The format forces you to identify:
- **Who** needs this (stakeholder/role)
- **What** they need (the action)
- **Why** they need it (the benefit/motivation)

<mark style="background: green">This stakeholder-centric framing prevents building features that solve no real user problem.</mark>

---

### User stories vs other documents

<mark style="background: pink">User stories are NOT a replacement for the BRD</mark> — they live at a different level.

- **User stories** — high-level, user-facing, behavior-oriented
- **System requirements (SRS)** — more detailed and lower-level, technically oriented

Depending on the project, you might need both together. Stories capture intent; SRS captures technical detail.

---

### When they're created

**Phase 4** — after the TO-BE process and Use Case Diagrams exist. Stories are derived from the use cases and redesigned workflows.

---

Read more:
- [[TO-BE process modeling redesigns workflows alongside UML use case diagrams]]
- [[SRS bridges business requirements and technical implementation]]
- [[BRD captures why the system is being built before any technical work begins]]
