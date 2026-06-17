---
aliases: [Factory Method, Factory Method pattern]
---

**Factory** = a thing that makes other things. **Method** = the making happens inside one overridable method. The subclass IS the factory — it decides what comes out.

### Intent

Define an abstract method for creating an object in a base class, and let each subclass override it to return a different concrete type.

---

### Problem

A logistics app starts with only trucks. The `Logistics` class is full of business logic: load cargo, plot the route, generate invoices. All of it hardcodes `new Truck()`.

Now the business wants ships. You can't add `new Ship()` into the same class without forking every road-specific branch. The creation of the transport is tangled into business logic that should know nothing about it.

---

### Solution

Extract the `new Truck()` call into an abstract method — `createTransport()`. `Logistics` calls only that method and gets back a `Transport`. It never knows if it's a Truck or a Ship.

Two subclasses fill in the detail:
- `RoadLogistics.createTransport()` → `new Truck()`
- `SeaLogistics.createTransport()` → `new Ship()`

At startup, `main()` instantiates `RoadLogistics` or `SeaLogistics` once. From that point, `planDelivery()` runs identically for both.

---

### Real-world analogy

A logistics company's HQ knows how to plan a delivery: load cargo, plot the route, generate the invoice. Whether cargo travels by truck or ship depends on which regional branch handles the order — HQ never specifies the vehicle. Each branch overrides the "which vehicle" step while the planning process stays the same.

---

### Structure — the four roles

- <mark style="background: #FFF3A3A6;">**Product**</mark> — interface every created object implements (`Transport` → `deliver()`)
- <mark style="background: #FFF3A3A6;">**ConcreteProduct**</mark> — the actual objects being created (`Truck`, `Ship`)
- <mark style="background: #FFF3A3A6;">**Creator**</mark> — abstract class declaring the factory method; contains business logic that *uses* the product but never names a concrete type
- <mark style="background: #FFF3A3A6;">**ConcreteCreator**</mark> — subclass that overrides the factory method to return a specific ConcreteProduct

### Diagram

![[factory_method_structure.png]]

---

### Pseudocode

```
interface Transport:
    deliver()

class Truck implements Transport:
    deliver(): // by road

class Ship implements Transport:
    deliver(): // by sea

abstract class Logistics:
    abstract createTransport(): Transport    // factory method

    planDelivery():
        t = createTransport()               // no "new Truck()" here
        t.deliver()

class RoadLogistics extends Logistics:
    createTransport(): return new Truck()

class SeaLogistics extends Logistics:
    createTransport(): return new Ship()

// At startup — the ONE place the concrete type is chosen
logistics = new RoadLogistics()
logistics.planDelivery()
```

---

### When to use

- The exact type to create isn't known until runtime or startup configuration.
- You're building a framework or library and want callers to extend it by subclassing, not by editing your code.
- You need to add new product types without touching existing creator or product classes.
- Creation logic would be duplicated across multiple places if not centralized in a subclass.

---

### Pros and cons

**Pros**
- Loose coupling — Creator never names a ConcreteProduct.
- Open/Closed — add `AirLogistics` by adding one subclass; existing code untouched.
- Single Responsibility — creation logic lives in ConcreteCreator, business logic lives in Creator.

**Cons**
- Class count grows — every new product type needs a matching ConcreteCreator subclass.
- <mark style="background: #FF000040;">Common mistake:</mark> confusing this with Simple Factory. Simple Factory = one static method with `if/else`, coupled to a parameter. Factory Method = subclass override with polymorphism, the decision lives in which type you instantiate.

---

### Read more
- Implementations:
    - [[Factory Method in Java uses an abstract creator class whose subclasses override the factory method]]
    - [[Spring applies Factory Method through BeanFactory and FactoryBean to decouple object creation from business logic]]
- Related patterns:
    - [[The Strategy pattern makes algorithms interchangeable by hiding each behind a common interface]]
- [[Design Patterns - MOC]]
