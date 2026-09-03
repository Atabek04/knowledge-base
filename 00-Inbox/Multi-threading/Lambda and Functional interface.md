`Runnable` has exactly one abstract method (`run()`), which makes it a **functional interface** — Java lets a lambda stand in for it directly:

```java
Thread t1 = new Thread(() -> sendEmail(a));
```

---

- So any abstract method that has only method, becomes Functional Interface?
	- fresh up my knowledge on what's the Functional Interface in the first place
	- can Interface be also Functional Interface? abstract it's because it's already have implemented method? I forgot them, subhanaAllah. Can you leave them as blank in order to children implement them? or you always implement them? what about interface where you write default methods or not?
- So Lambda and Functional Interface, how they're related? they're not synonyms, are they? In that Thread constructor which one exactly is lambda and which one is functional interface

---

## Answers

### What is a Functional Interface, from scratch

An interface whose methods have **no body** describes a contract: "anything implementing me must provide these methods." That's the normal, default state of an interface method — it's implicitly `abstract`, even without writing the `abstract` keyword.

A **Functional Interface** is a narrower case: an interface with **exactly one** such no-body (abstract) method. Java also calls this the **SAM rule** — Single Abstract Method. `Runnable` qualifies: it has exactly one abstract method, `run()`.

`@FunctionalInterface` is an *optional* annotation you can put above the interface. It does nothing at runtime — it just makes the compiler double-check "does this really have exactly one abstract method?" and error out if you accidentally add a second one. A functional interface without the annotation still works; the annotation is just a safety net.

### Can an interface have `default`/`static` methods and still be functional?

Yes — and this is the piece you were missing. `default` and `static` methods **have a body**, so they don't count as "abstract." Only body-less methods count toward the SAM rule.

- **Abstract method** (no body) → whoever implements the interface (a class, or a lambda) **must** supply it. You cannot skip it.
- **`default` method** (has a body, written in the interface itself) → optional to override. Lets an interface add a new method later without breaking every existing implementer — they all inherit the default body for free.
- **`static` method** (has a body) → belongs to the interface itself, not to implementers. Called like `InterfaceName.method()`, e.g. `Comparator.naturalOrder()`.

So a functional interface can have as many `default`/`static` methods as it wants — `Comparator` has dozens — as long as exactly **one** method is still abstract. That one method is what a lambda ends up implementing.

### Lambda vs Functional Interface — not synonyms

They're two different *kinds of thing*, not two names for the same thing:

- **Functional Interface** = the **type** / the contract. It's the shape: "one method, this signature, this return type." `Runnable` is a type, same way `String` is a type.
- **Lambda** = a **value** — a concrete, anonymous object that satisfies that shape. It's the actual implementation, created on the spot.

Analogy: the functional interface is the *socket shape* (one slot, this size); the lambda is the *plug* you make that fits it. The socket shape doesn't do anything by itself — you need an actual plug (a lambda, or a class) to put into it.

**In `new Thread(() -> sendEmail(a))`:**
- `Runnable` is the **functional interface** — it's the parameter type `Thread`'s constructor declares it needs.
- `() -> sendEmail(a)` is the **lambda** — the actual object being passed in, whose body becomes the implementation of `Runnable`'s one abstract method, `run()`.

The compiler sees "constructor wants a `Runnable`" + "here's a lambda with no params and no return value" → matches `run()`'s signature (`void run()`) → accepts it, wraps it into an anonymous `Runnable` instance behind the scenes.