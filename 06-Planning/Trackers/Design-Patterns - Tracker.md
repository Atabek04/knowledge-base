# Design Patterns

**MOC:** [[Design Patterns - MOC]]
**Books:** Head First Design Patterns (Freeman) · Enterprise Application Patterns (Fowler)
**Progress:** 0 / 33 patterns

> End-state: 8 core patterns **implemented in Java** + can explain *when/why* (not just name); remaining GoF understood; 5 enterprise patterns implemented; can answer scenario prompts out loud in 45 min.
>
> Senior interviews test **trade-off fluency and "when to apply"**, rarely "define Singleton". Depth on 8 beats shallow on 23. For each pattern: implement it, then code the painful "without it" version to feel why it exists, then connect it to a Spring/framework example you already use.

> ⚠️ **Mid-level reframe (2026-05-27):** for the current first-offer goal, patterns are **low-yield vs DSA/SD/behavioral**. Active scope = only **6 high-yield** (Strategy, Factory Method, Builder, Singleton, Observer, Decorator), learned *light* — recognize + one real-code use each, folded into Java study Jun–Aug (~30–45 min/wk), **not** a weekend track. The full 33 below stay here as the **post-offer / senior-upgrade** path. Schedule: [[Interview-Prep-Execution]] (Ribaat).

---

## Tier 1 — Core 8 (implement in Java + explain) 🔴 do first

- [ ] **Strategy** — interchangeable algorithms · Spring: `Comparator`, payment-method selection
- [ ] **Factory Method** — defer creation to subclasses · Spring: `BeanFactory`
- [ ] **Builder** — step-by-step complex object · Java: `StringBuilder`, Lombok `@Builder`
- [ ] **Observer** — notify dependents on change · Spring: `ApplicationEvent` / listeners
- [ ] **Decorator** — add behavior dynamically · Java IO streams, servlet filters
- [ ] **Adapter** — bridge incompatible interfaces · wrapping a 3rd-party SDK
- [ ] **Facade** — simple interface over a subsystem · a service-layer wrapper
- [ ] **Command** — encapsulate a request as an object · job queue / undo

## Tier 2 — Remaining GoF (understand + sketch, implement if time)

### Creational
- [ ] Singleton — single instance · Spring beans are singletons by default
- [ ] Abstract Factory — families of related objects
- [ ] Prototype — clone existing objects

### Structural
- [ ] Bridge — separate abstraction from implementation
- [ ] Composite — uniform treatment of object trees
- [ ] Flyweight — share common state
- [ ] Proxy — placeholder / lazy / access control · Spring AOP, `@Transactional`

### Behavioral
- [ ] Chain of Responsibility — pass request along a chain · servlet filter chain
- [ ] Iterator — sequential access without exposing internals
- [ ] Mediator — centralize complex communication
- [ ] Memento — capture/restore state (undo)
- [ ] State — behavior changes with state
- [ ] Template Method — algorithm skeleton, deferred steps · `AbstractList`
- [ ] Visitor — add operations without modifying classes

## Tier 3 — Enterprise patterns (backend-critical) 🔴 high interview value

- [ ] **Repository** — abstract data access · Spring Data
- [ ] **Service Layer** — application boundary
- [ ] **Unit of Work** — track changes, coordinate writes · JPA persistence context
- [ ] **Data Mapper** — map objects ↔ DB · JPA/Hibernate
- [ ] **Domain Model** — object model with behavior
- [ ] **Value Object** — immutable, defined by value
- [ ] **Entity** — identity-based object
- [ ] **Aggregate** — cluster of entities with a root (DDD)
- [ ] **Transaction Script** — procedural business logic

## Tier 4 — Interview readiness

- [ ] Scenario practice: "support 5 payment providers without if-else" (→ Strategy/Factory)
- [ ] Scenario practice: "add cross-cutting logging/retry without touching classes" (→ Decorator/Proxy)
- [ ] Explain Singleton thread-safety + why it's often an anti-pattern
- [ ] Explain "pattern-itis" — knowing when NOT to use a pattern (senior signal)
- [ ] Map each Tier-1 pattern to a real example from your own codebase

## Flashcards

- [ ] `05-Flashcards/design-patterns/creational.md`
- [ ] `05-Flashcards/design-patterns/structural.md`
- [ ] `05-Flashcards/design-patterns/behavioral.md`
- [ ] `05-Flashcards/design-patterns/enterprise.md`
