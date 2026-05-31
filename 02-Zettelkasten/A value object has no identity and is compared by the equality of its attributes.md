---
aliases: [Value Object, VO]
tags: [ddd, domain-model, architecture, design, immutability]
created: 2026-05-31
---

### What is a value object?

A **value object** is an object with <mark style="background: yellow">no identity</mark> — it is defined entirely by its attributes.

`Money(100, "USD")`, `DateRange(start, end)`, an `Address` — none of these has an "id". Two of them with the same values *are* the same thing.

---

### Equality by value

Two value objects are equal when all their attributes are equal.

`Money(100, "USD") == Money(100, "USD")` is `true`, even though they are two separate objects in memory.

Contrast this with a [[A domain entity is defined by a continuous identity that persists through state changes|domain entity]], where equality is decided by identity, not by attribute values.

---

### Immutable by design

A value object should be **immutable** — once created, it never changes.

To "change" an amount you create a *new* `Money`, you don't mutate the old one.
This is exactly what a Java `record` or `final`-field class gives you.

<mark style="background: #f9a8d4">Why immutability matters:</mark> if value objects were mutable and shared, changing one place would silently change another. Immutability makes them safe to share freely.

---

### Side effect: interchangeability

Because identity is irrelevant, any value object with the same values can replace another.

This is what makes them cheap — no lifecycle to track, no database row to own, no referential integrity to maintain.

---

Read more:
- [[A domain entity is defined by a continuous identity that persists through state changes]]
- [[An aggregate is a cluster of objects treated as one consistency boundary]]
- [[Software Engineering Principles - MOC]]
