---
aliases: [Aggregate, Consistency Boundary]
tags: [ddd, domain-model, architecture, design, invariants]
created: 2026-05-31
---

### What is an aggregate?

An **aggregate** is a cluster of related entities and value objects that the system treats as a <mark style="background: yellow">single unit for data changes</mark>.

Example: an `Order` together with its `OrderLine` items. You don't load or save a stray order line on its own — you work with the whole order.

---

### The consistency boundary

The reason aggregates exist is the <mark style="background: #93d4d4">consistency boundary</mark>: a rule that must always hold true is enforced *inside* one aggregate.

Invariant: *"an order's total must equal the sum of its line items."*

If line items lived outside the order, two transactions could change them independently and break that rule. Keeping them inside one aggregate means the rule is checked in one place, atomically.

---

### One transaction = one aggregate

The practical rule: <mark style="background: #f9a8d4">a single transaction should modify only one aggregate.</mark>

Inside the aggregate: changes are **immediately consistent** (enforced now, atomically).
Across aggregates: changes are **eventually consistent** — you coordinate them with domain events, not one big transaction.

This is the same trade-off behind the [[Outbox pattern guarantees event delivery by writing to an outbox table in the same transaction|outbox pattern]]: update one aggregate, emit an event, let other aggregates react.

---

### How big should an aggregate be?

As small as the invariant allows.

Large aggregates load more data and create lock contention; tiny aggregates can't enforce real rules. The invariant defines the boundary — not the object graph.

---

Read more:
- [[The aggregate root is the only object outside code may hold a reference to]]
- [[A domain entity is defined by a continuous identity that persists through state changes]]
- [[Outbox pattern guarantees event delivery by writing to an outbox table in the same transaction]]
- [[Software Engineering Principles - MOC]]
