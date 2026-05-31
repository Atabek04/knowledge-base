TARGET DECK: Tech-KB::Architecture::Domain-Driven Design
Tags: ddd domain-model architecture
**Chapter:** Domain Model (DDD building blocks)
**Related:** [[Software Engineering Principles - MOC]]

---

START
Coding Questions
What defines a domain entity, and how is one entity compared to another for equality?
Back:
A **domain entity** is defined by a **continuous identity**, not by its attribute values.

- Two entities are equal **iff their identities match** — never field by field
- `equals()`/`hashCode()` are based on the identifier, not mutable fields
- A `User` whose email and name change is still the **same** user
Tags: ddd domain-model entity
END

START
Coding Questions
Why is a domain entity expected to be mutable over its lifecycle?
Back:
An entity models a thing you need to **track across time**, so its state changes by design.

- `Order`: `PLACED → PAID → SHIPPED → DELIVERED` — same order, different state
- The **identity** is the thread of continuity tying those states into one object
Tags: ddd domain-model entity
END

START
Coding Questions
What is a value object, and how is equality decided for it?
Back:
A **value object** has **no identity** — it is defined entirely by its attributes.

- Equality is **by value**: `Money(100,"USD") == Money(100,"USD")` is `true`
- Examples: `Money`, `DateRange`, `Address`
- Contrast with an entity, where equality is by identity
Tags: ddd domain-model value-object
END

START
Coding Questions
Why must a value object be immutable?
Back:
If value objects were mutable and shared, changing one place would **silently change another**.

- Immutability makes them **safe to share freely**
- To "change" a value you create a **new** object (Java `record` / `final` fields)
- No lifecycle, no row to own → interchangeable
Tags: ddd domain-model value-object immutability
END

START
Coding Questions
What is an aggregate, and what does its consistency boundary guarantee?
Back:
An **aggregate** is a cluster of entities + value objects treated as **one unit for changes** (e.g. `Order` + its `OrderLine`s).

- The **consistency boundary** = the invariant enforced inside it (e.g. "total = sum of lines")
- Inside the boundary: changes are checked **atomically, in one place**
Tags: ddd domain-model aggregate invariants
END

START
Coding Questions
Why should a single transaction modify only one aggregate?
Back:
Inside one aggregate, changes are **immediately consistent** (enforced atomically).

Across aggregates, you accept **eventual consistency** — coordinate with domain events, not one big transaction.

This keeps locks small and avoids cross-boundary contention (the trade-off behind the outbox pattern).
Tags: ddd domain-model aggregate consistency
END

START
Coding Questions
What is the aggregate root, and what is the single-reference rule?
Back:
The **aggregate root** is the one entity that is the aggregate's **only entry point**.

- Outside code may reference **only the root**, never an internal member
- `order.changeLineQuantity(lineId, 3)` — not `orderLine.setQuantity(3)`
- The root mediates every change so it can **enforce invariants**
Tags: ddd domain-model aggregate-root
END

START
Coding Questions
Why must all changes to an aggregate go through its root?
Back:
If outside code could mutate an internal member directly, the aggregate's invariant could be broken **without the root knowing**.

- Routing through the root gives exactly **one gatekeeper** for validity
- Same principle as encapsulation: hide internals, expose intent-revealing methods
Tags: ddd domain-model aggregate-root invariants
END

START
Coding Questions
How does a domain model differ from a data model?
Back:
They describe the same business but answer different questions:

- **Domain model** → *how does it behave, what rules must hold?* (aggregates, entities, VOs, methods)
- **Data model** → *how is it stored and related?* (tables, rows, keys, FKs)

A domain model expresses **intent**; a data model serves **persistence**.
Tags: ddd domain-model data-model
END

START
Coding Questions
What is the object–relational impedance mismatch, and where does it come from?
Back:
The **mismatch** between the domain model's shape and the data model's shape.

- One aggregate often maps to **several tables** (`Order` + lines)
- A value object often has **no table** — embedded as columns
- This gap is what ORMs (Hibernate) exist to **bridge**
Tags: ddd domain-model data-model orm
END
