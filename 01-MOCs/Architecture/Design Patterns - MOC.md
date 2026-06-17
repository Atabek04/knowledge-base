> Learn patterns to write maintainable, flexible code
>
> **Hands-on practice:** `~/design-pattern-katas` (WSL git repo) — tests-first refactor katas, Java/Kotlin/Python. Tracker: [[Design-Patterns - Tracker]].

---

## Progress

- [ ] Creational patterns
- [ ] Structural patterns
- [ ] Behavioral patterns
- [ ] Enterprise patterns

---

## Topics

### Creational Patterns
- [ ] **Singleton** — Single instance, global access
- [[The Factory Method pattern lets subclasses decide which object to instantiate by overriding a factory method|Factory Method — subclass overrides the creation step, Creator never names a concrete type]]
    - [[Factory Method in Java uses an abstract creator class whose subclasses override the factory method|Java implementation — abstract Creator, ConcreteCreator subclasses]]
    - [[Spring applies Factory Method through BeanFactory and FactoryBean to decouple object creation from business logic|Spring — BeanFactory, FactoryBean, and @Bean methods as factory methods]]
- [ ] **Abstract Factory** — Create families of related objects
- [ ] **Builder** — Construct complex objects step by step
- [ ] **Prototype** — Clone existing objects

### Structural Patterns
- [ ] **Adapter** — Make incompatible interfaces work together
- [ ] **Bridge** — Separate abstraction from implementation
- [ ] **Composite** — Treat individual objects and compositions uniformly
- [ ] **Decorator** — Add responsibilities dynamically
- [ ] **Facade** — Simplified interface to complex subsystem
- [ ] **Flyweight** — Share common state between objects
- [ ] **Proxy** — Placeholder for another object

### Behavioral Patterns
- [ ] **Chain of Responsibility** — Pass request along chain
- [ ] **Command** — Encapsulate request as object
- [ ] **Iterator** — Sequential access without exposing internals
- [ ] **Mediator** — Centralize complex communications
- [ ] **Memento** — Capture and restore object state
- [ ] **Observer** — Notify dependents of state changes
- [ ] **State** — Alter behavior when state changes
- [[The Strategy pattern makes algorithms interchangeable by hiding each behind a common interface|Strategy]] — interchangeable algorithms (Kotlin · Python · Java impls linked in note)
- [ ] **Template Method** — Define algorithm skeleton, defer steps
- [ ] **Visitor** — Add operations without modifying classes

### Enterprise Patterns
- [ ] **Repository** — Abstract data access
- [ ] **Unit of Work** — Track changes and coordinate writes
- [ ] **Data Mapper** — Transfer data between objects and database
- [ ] **Service Layer** — Define application's boundary
- [ ] **Domain Model** — Object model with behavior
- [ ] **Transaction Script** — Procedural business logic
- [ ] **Value Object** — Immutable objects defined by values
- [ ] **Entity** — Objects with identity
- [ ] **Aggregate** — Cluster of entities with root

---

## Pattern Selection Guide

| Problem | Consider |
|---------|----------|
| Object creation is complex | Builder, Factory |
| Need single instance | Singleton |
| Incompatible interfaces | Adapter |
| Add features without subclassing | Decorator |
| Complex subsystem | Facade |
| Algorithm varies | Strategy |
| Object changes behavior with state | State |
| Notify multiple objects | Observer |
| Undo/redo operations | Command, Memento |

---

## Books

- [[The Gang of Four book cataloged 23 reusable object-oriented design patterns|Gang of Four cataloged 23 OO design patterns]]

| Book | Priority | Status |
|------|----------|--------|
| **Head First Design Patterns** — Freeman | 🔴 Critical | ⏳ |
| **Enterprise Application Patterns** — Fowler | 🟡 Important | ⏳ |

---

## Project Tasks

**E-Commerce:** Apply patterns
- [ ] Use Builder for complex Order objects
- [ ] Implement Repository pattern for data access
- [ ] Use Strategy for different payment methods
- [ ] Apply Observer for order status notifications
- [ ] Use Factory for creating different product types

---

## Learning Path

No course for this track — it's learned by **implementing in Java**, not reading. Sequence: master the **core 8** deeply first (Strategy, Factory Method, Builder, Observer, Decorator, Adapter, Facade, Command), then breadth on the rest, then enterprise patterns. For each: implement it → code the painful "without it" version → tie it to a Spring/Java example you already use.

Module-by-module progress:

- [[Design-Patterns - Tracker]] — `06-Planning/Trackers/` · sequenced implementation path (33 patterns)

Sequencing + time budget: [[Interview-Prep-Master-Plan]]

---

## Related
- [[Interview-Prep-Master-Plan]]
- [[Java MOC]]
- [[Architecture - MOC]]
