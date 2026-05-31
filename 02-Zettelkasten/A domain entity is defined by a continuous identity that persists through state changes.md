---
aliases: [Entity, Domain Entity]
tags: [ddd, domain-model, architecture, design]
created: 2026-05-31
---

### What is a domain entity?

A **domain entity** is an object defined by a <mark style="background: yellow">continuous identity</mark> — not by the values it holds.

You already know this shape: a JPA `@Entity` with an `@Id`.
The row's identity is its `id`, and you can change every other column while it stays "the same" thing.

---

### Identity, not equality

Two entities are equal *if and only if* their identities match — never compare them field by field.

A `User` whose `email` and `displayName` both change is still the **same user**, because the `id` never changed.

This is why `equals()` / `hashCode()` on an entity should be based on the identifier, not on mutable attributes.

---

### Mutable over a lifecycle

An entity is *expected* to change state over time.
An `Order` moves through `PLACED → PAID → SHIPPED → DELIVERED` — same order, different state at each step.

The identity is the <mark style="background: #93d4d4">thread of continuity</mark> that ties those states together into one object.

---

### Why this matters

Modeling something as an entity is a deliberate choice: you are saying *"I need to track this individual thing across time."*

If you don't need to track it individually — if any instance with the same values is interchangeable — it should be a [[A value object has no identity and is compared by the equality of its attributes|value object]] instead.

---

Read more:
- [[A value object has no identity and is compared by the equality of its attributes]]
- [[An aggregate is a cluster of objects treated as one consistency boundary]]
- [[A domain model captures behavior and rules while a data model captures storage structure]]
- [[Primary key uniquely identifies each row and anchors referential integrity across tables]]
- [[Software Engineering Principles - MOC]]
