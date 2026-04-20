---
created: 2026-04-10
aliases: [interleaved requirements, documents and models]
tags:
  - software-engineering/requirements
---

> <mark style="background: yellow">Documents and models in requirements engineering are interleaved, not sequential — you don't "first write everything, then model everything."</mark>

---

### How interleaving works

Each phase produces both a document and a model that feed each other:

- **Phase 1**: BRD (document) — no model yet
- **Phase 2**: AS-IS BPMN (model) — validates BRD scope
- **Phase 3**: TO-BE BPMN + Use Case Diagram (models) — shapes user stories
- **Phase 4**: User stories (document) — derived from models
- **Phase 5**: SRS (document) — informed by use cases and stories
- **Phase 6**: Detailed UML (models) — elaborates SRS requirements
- **Phase 7**: FRS (document) — references UML models directly

<mark style="background: cyan">Every model is grounded in a written requirement. Every document is validated by a model. They co-evolve.</mark>

---

### The practitioner reality

<mark style="background: pink">The BABOK itself treats requirements knowledge areas as concurrent, not strictly sequential.</mark> A certain amount of requirements analysis takes place during elicitation activities.

One practitioner's blunt take: the document will be wrong and out of date the moment you finish it, and if it's longer than two pages, nobody will read it entirely.

This is why the community consensus leans toward: **keep documents lean, use models for clarity, iterate frequently** rather than perfecting upfront.

---

Read more:
- [[Progressive elaboration zooms requirements from business goals to implementation details]]
- [[BPMN comes before UML because process understanding precedes system design]]
- [[Detailed UML diagrams are specification tools created after requirements are documented]]
