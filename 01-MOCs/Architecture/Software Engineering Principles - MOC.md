---
tags: [moc, software-engineering, principles]
---

## Encapsulation & API Boundaries

*What should a module hide, and how?*

- [[Getters and setters add boilerplate without real encapsulation|Getters/setters add boilerplate, not encapsulation]]
- [[C achieves data hiding by omitting struct definitions from headers|C hides data via opaque pointers in headers]]
- [[Private keyword in C++ created header dependencies and long compile times|C++ private created header deps and slow compiles]]
- [[Private fields are a type-level fix for a module-level problem|Private fields: type-level fix for a module problem]]

## API Contract Theory

*What does an API actually promise?*

- [[Hyrum's Law states any observable behavior in a library will be depended on|Hyrum's Law: any observable behavior gets depended on]]

---

## Coupling & Cohesion

*The central tension of software structure: things that change together should live together; things that don't should stay apart.*

- [ ] High cohesion — a module does one thing and owns everything needed to do it
- [ ] Low coupling — modules depend on as little of each other as possible
- [ ] Afferent vs efferent coupling — who depends on you vs who you depend on
- [ ] Connascence — a more precise vocabulary for coupling (name, type, value, timing, execution order)

---

## Separation of Concerns

*Don't solve two problems in the same place.*

- [ ] Horizontal layers vs vertical slices — layered architecture vs feature modules
- [ ] Cross-cutting concerns — logging, auth, tracing don't belong inside business logic
- [ ] Aspect-oriented thinking — when to pull a concern out vs keep it inline
- [ ] The cost of premature separation — over-abstraction is also a violation of SoC

---

## Dependency Management

*Explicit is better than implicit. Point inward, not outward.*

- [ ] Dependency Inversion Principle — high-level modules must not depend on low-level modules
- [ ] Explicit vs implicit dependencies — constructors over service locators
- [ ] Dependency injection vs service locator — why DI wins
- [ ] Acyclic dependencies principle — no cycles between packages/modules
- [ ] Stable dependencies principle — depend in the direction of stability

---

## Abstraction & Levels of Detail

*A function should operate at one level of abstraction. Mixing levels is a readability tax.*

- [ ] Stepdown rule — each function reads at one level, calls down to the next
- [ ] Leaky abstractions — when the abstraction forces you to know what it hides
- [ ] Law of Demeter — don't talk to strangers; a method should only call its direct collaborators
- [ ] Tell, don't ask — give objects commands, not questions about their state

---

## Invariants & Design by Contract

*What is always true, and who is responsible for keeping it true?*

- [ ] Preconditions — what must hold before a function is called
- [ ] Postconditions — what the function guarantees on return
- [ ] Invariants — what is always true about an object's state
- [ ] Fail fast — crash early on violated invariants rather than propagating bad state
- [ ] Defensive programming vs trusting callers — where to draw the line

---

## Immutability & State Management

*Mutable shared state is the root of most concurrency bugs and many logic bugs.*

- [ ] Value objects vs entities — objects defined by value vs by identity
- [ ] Immutability as default — why immutable-first reduces bugs
- [ ] Where state is acceptable — the boundaries where mutation is contained
- [ ] Command-Query Separation (CQS) — a method either changes state or returns data, never both

---

## Error Handling Philosophy

*Errors are part of the contract. Treat them as first-class design decisions.*

- [ ] Exceptions vs return values — when each approach wins (Go/Rust vs Java)
- [ ] Error propagation — let errors bubble vs handle locally
- [ ] Checked vs unchecked exceptions — the Java debate
- [ ] Error as data — Result/Either types and their tradeoffs
- [ ] Panic vs recoverable error — when crashing is the right answer

---

## Naming as Design

*A name is a compression of intent. Bad names are a design smell, not a style issue.*

- [ ] Names reveal intent — if the name is hard to write, the abstraction is probably wrong
- [ ] Ubiquitous language — names should match the domain, not the implementation
- [ ] Symmetry in naming — if you have `open`, you need `close`; if `add`, then `remove`
- [ ] Primitive obsession — when a bare `String` or `int` should be a named type

---

## Composition vs Inheritance

*Inheritance is the strongest coupling in OOP. Reach for it last.*

- [[Favor composition over inheritance when behaviors vary independently|Favor composition over inheritance (HAS-A vs IS-A)]]
- [ ] The fragile base class problem — subclassing breaks when the parent changes
- [ ] Mixin vs inheritance vs delegation
- [ ] When inheritance is correct — true is-a relationships, not code reuse

---

## Domain-Driven Design

*Model the business in objects defined by identity, value, and consistency boundaries — not by table layout.*

- [[A domain entity is defined by a continuous identity that persists through state changes|Entity: continuous identity through state changes]]
- [[A value object has no identity and is compared by the equality of its attributes|Value object: no identity, equality by value]]
- [[An aggregate is a cluster of objects treated as one consistency boundary|Aggregate: one consistency boundary per transaction]]
- [[The aggregate root is the only object outside code may hold a reference to|Aggregate root: the only externally held reference]]
- [[A domain model captures behavior and rules while a data model captures storage structure|Domain model (behavior) vs data model (storage)]]

---

## Related MOCs

- [[Architecture - MOC]]
- [[Design Patterns - MOC]]
- [[API Design - MOC]]

- [[Architecture - MOC]]
- [[Design Patterns - MOC]]
- [[API Design - MOC]]
