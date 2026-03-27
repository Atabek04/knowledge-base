# Design Patterns — MOC

> **Phase 1** of [[00 - IT Career - MOC]]
> Learn patterns to write maintainable, flexible code

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
- [ ] **Factory Method** — Delegate object creation to subclasses
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
- [ ] **Strategy** — Interchangeable algorithms
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

## Related
- [[Java Core - MOC]]
- [[Architecture - MOC]]
- [[00 - IT Career - MOC]]
