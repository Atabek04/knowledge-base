---
aliases: [Aggregate Root, Root Entity]
tags: [ddd, domain-model, architecture, design, invariants]
created: 2026-05-31
---

### What is the aggregate root?

The **aggregate root** is the single entity inside an [[An aggregate is a cluster of objects treated as one consistency boundary|aggregate]] that serves as its <mark style="background: yellow">only entry point</mark>.

In an `Order` aggregate, `Order` is the root; `OrderLine` items are internal members.

---

### The single-reference rule

Code outside the aggregate may hold a reference **only** to the root — never to an internal member directly.

You don't do `orderLine.setQuantity(3)`.
You do `order.changeLineQuantity(lineId, 3)`.

The root mediates every change, so it can <mark style="background: #93d4d4">enforce the aggregate's invariants</mark> before allowing it.

---

### Why route everything through the root?

If outside code could grab an `OrderLine` and mutate it directly, the rule *"total = sum of lines"* could be violated without the `Order` ever knowing.

Forcing all changes through the root means there is exactly **one gatekeeper** responsible for keeping the aggregate valid. This is the same idea as encapsulation — the root hides its internals and exposes intent-revealing methods.

---

### The root owns identity

The aggregate root is also the thing with a global identity (its [[Primary key uniquely identifies each row and anchors referential integrity across tables|primary key]]).

Internal members may have local identifiers, but they are only meaningful *within* the root. You reference an order by its id; you reference a line *through* its order.

---

Read more:
- [[An aggregate is a cluster of objects treated as one consistency boundary]]
- [[A domain entity is defined by a continuous identity that persists through state changes]]
- [[Primary key uniquely identifies each row and anchors referential integrity across tables]]
- [[Software Engineering Principles - MOC]]
