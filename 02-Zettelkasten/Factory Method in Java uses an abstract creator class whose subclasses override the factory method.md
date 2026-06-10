---
aliases: [Factory Method in Java, Java Factory Method]
---

Java implementation of the [[The Factory Method pattern lets subclasses decide which object to instantiate by overriding a factory method|Factory Method pattern]]. The Creator is an **abstract class** with the factory method declared `abstract` — each ConcreteCreator subclass overrides it to return a specific type.

### Product interface

```java
interface Transport {
    void deliver();
}
```

### ConcreteProducts

```java
class Truck implements Transport {
    public void deliver() { /* by road */ }
}

class Ship implements Transport {
    public void deliver() { /* by sea */ }
}
```

---

### Creator

```java
abstract class Logistics {
    abstract Transport createTransport();   // factory method

    void planDelivery() {
        Transport t = createTransport();    // no new Truck() here
        t.deliver();
    }
}
```

`planDelivery()` is the business logic. It uses `Transport` — the interface — never a concrete class. `createTransport()` is the one seam where the subclass plugs in.

---

### ConcreteCreators

```java
class RoadLogistics extends Logistics {
    public Transport createTransport() { return new Truck(); }
}

class SeaLogistics extends Logistics {
    public Transport createTransport() { return new Ship(); }
}
```

### Composition root

```java
// The ONE place the concrete type is chosen
Logistics logistics = new RoadLogistics();
logistics.planDelivery();
```

Switch road → sea: change `new RoadLogistics()` to `new SeaLogistics()`. Nothing else changes.

---

### Adding a new transport type

1. Implement `Transport`: `class Plane implements Transport { ... }`
2. Subclass `Logistics`: `class AirLogistics extends Logistics { public Transport createTransport() { return new Plane(); } }`
3. Use it at startup: `new AirLogistics()`

`Logistics`, `Truck`, `Ship` — untouched. This is Open/Closed in practice.

---

### Why abstract class, not interface, for Creator

`Logistics` is abstract — not an interface — because it holds real business logic (`planDelivery()`). The factory method is `abstract`; the surrounding logic is concrete.

<mark style="background: #FF000040;">Don't make Creator an interface</mark> — you'd lose the shared business logic and be forced to duplicate `planDelivery()` in every ConcreteCreator.

---

### Read more
- [[The Factory Method pattern lets subclasses decide which object to instantiate by overriding a factory method]]
- [[Design Patterns - MOC]]
