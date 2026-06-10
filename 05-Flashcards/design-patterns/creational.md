TARGET DECK: Tech-KB::Design Patterns::Creational
Tags: design-patterns creational
**Related:** [[Design Patterns - MOC]]

---

<!-- Factory Method, Abstract Factory, Builder, Singleton, Prototype.
     Card per pattern: intent, when to apply, a Spring/Java example, the trade-off. -->

## Factory Method

Q: What is the Factory Method pattern in one sentence?
A: Define an abstract method for creating an object in a base class, and let each subclass override it to return a different concrete type.

---

Q: What are the four roles in Factory Method?
A:
- **Product** — interface all created objects implement
- **ConcreteProduct** — the actual objects (`Truck`, `Ship`)
- **Creator** — abstract class with the factory method + business logic that uses the product
- **ConcreteCreator** — subclass that overrides the factory method to return a specific type

---

Q: What is the structural difference between Simple Factory and Factory Method?
A:
- **Simple Factory** — one static method with `if/else`, decides the type via a parameter
- **Factory Method** — abstract method in a base class, subclass override decides the type via polymorphism

Simple Factory couples the caller to a decision. Factory Method moves that decision into which subclass you instantiate.

---

Q: In Factory Method, where does the decision of which concrete type to create actually live?
A: At the composition root (e.g. `main()`), where you instantiate the ConcreteCreator:
```java
Logistics logistics = new RoadLogistics(); // decision is here
logistics.planDelivery();                  // Creator never sees "Truck"
```

---

Q: Why must the Creator be an abstract class and not an interface?
A: Creator holds shared business logic (e.g. `planDelivery()`). An interface can't contain implementation. Making it an interface forces you to duplicate that logic in every ConcreteCreator.
