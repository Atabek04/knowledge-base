---
aliases: [default method, interface default method, default keyword Java]
created: 2026-08-19
tags: [java, oop]
---

Before Java 8, adding a method to an interface was a breaking change — every class implementing that interface would suddenly fail to compile until it added the new method too.

<mark style="background: #FFF3A3A6;"><b>A default method is an interface method written with a body, using the `default` keyword. Implementers inherit that body for free and are never forced to override it — the interface can grow without breaking anyone already implementing it.</b></mark>

```java
interface Greeter {
    void greet(String name);              // abstract — every implementer must supply this

    default void greetLoudly(String name) {
        greet(name.toUpperCase());        // has a body — inherited automatically, optional to override
    }
}
```

Any existing class that already implements `Greeter` still compiles after `greetLoudly` is added — it just inherits the default body without writing a line of new code. An implementer that *does* want different behavior can still override it like any other method.

This is also why `default` methods don't count toward the [[A Java functional interface has exactly one abstract method — default and static methods don't count toward that limit|SAM rule]] for functional interfaces — they already have an implementation, so there's nothing left for a lambda to fill in.

### Read more

- [[A Java functional interface has exactly one abstract method — default and static methods don't count toward that limit]]
- [[Java interfaces define a contract with no state, while abstract classes can hold state and partial implementation]]
- [[Java MOC]]
