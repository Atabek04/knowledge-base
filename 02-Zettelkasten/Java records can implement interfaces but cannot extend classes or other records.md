---
created: 2026-06-08
tags: [java, records]
aliases: [record interface, record inheritance]
---

A Java record implicitly extends `java.lang.Record` and is implicitly `final`. Java allows only single-class inheritance — that slot is already taken, so <mark style="background: #FFF3A3A6;">records cannot extend any other class.</mark> They can implement any number of interfaces.

---

### Why records are final

Records are value types — their identity comes entirely from their components. Subclassing would let a child class add new fields, which would break the auto-generated `equals()` and `hashCode()` (both derived only from declared components).

Making records `final` closes that loophole: the component list is fixed and complete.

---

### Implementing interfaces

An interface defines a behavior contract without adding state, so it doesn't conflict with a record's sealed component list. Records implement interface methods in their body:

```java
interface Describable {
    String describe();
}

record Point(int x, int y) implements Describable {
    @Override
    public String describe() {
        return "Point at (" + x + ", " + y + ")";
    }
}
```

This is the primary way to use records in polymorphic APIs — declare the variable as the interface type:

```java
List<Describable> shapes = List.of(new Point(1, 2), new Point(3, 4));
```

---

### Practical constraint: no shared base DTO

Because records cannot extend a class, you cannot inherit shared fields from a base class (e.g. `BaseDto` with audit fields `createdAt`, `updatedBy`). If that pattern is required, [[Java record is a dependency-free alternative to Lombok @Value for immutable value types|Lombok `@Value`]] is a better fit — it can extend a class.

---

### Read more

- [[Java records auto-generate accessor, equals, hashCode, and toString from their components]]
- [[Java record is a dependency-free alternative to Lombok @Value for immutable value types]]
