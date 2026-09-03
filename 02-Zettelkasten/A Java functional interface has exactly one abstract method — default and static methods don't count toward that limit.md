---
aliases: [functional interface, SAM interface, Single Abstract Method, FunctionalInterface]
created: 2026-08-19
tags: [java]
---

An [[Java interfaces define a contract with no state, while abstract classes can hold state and partial implementation|ordinary interface]] can declare as many abstract methods as it wants. A **functional interface** is the special case where exactly one stays abstract.

<mark style="background: #FFF3A3A6;">A <b>functional interface</b> is an interface with exactly one abstract (body-less) method — the <b>SAM rule</b>, Single Abstract Method.</mark>

`Runnable` qualifies to be a Functional Interface, because it has only one `run()` method.

---

### `default` and `static` methods don't count

The one-method limit only counts **abstract** methods. An interface can have any number of [[Java interface default methods carry a body so existing implementers don't break when the interface gains a new method|default methods]] and [[Java interface static methods belong to the interface's own namespace, not to any implementing class|static methods]] and still be functional — both have a body, so neither leaves anything for an implementer to fill in. But the moment a **second** abstract method shows up, the SAM rule breaks and the interface stops being functional — no lambda can implement two unrelated methods at once.

`Comparator` is a real example: it has one abstract method `compare()` plus dozens of `default`/`static` helpers: `reversed()`, `thenComparing()`, `naturalOrder()` — and it's still a functional interface, because only `compare()` is abstract.

---

### `@FunctionalInterface` is just a compiler check

The annotation does nothing at runtime and isn't required — the SAM rule works without it. Without it, a second abstract method added later goes unnoticed at the interface itself; the error only surfaces confusingly, at every lambda call site that now fails to compile. With it, <mark style="background: #ADCCFFA6;">the compiler rejects the interface declaration the moment a second abstract method shows up</mark> — the error appears where the mistake was made, not scattered across call sites.

### Read more

- [[Java interfaces define a contract with no state, while abstract classes can hold state and partial implementation]]
- [[Java interface default methods carry a body so existing implementers don't break when the interface gains a new method]]
- [[Java interface static methods belong to the interface's own namespace, not to any implementing class]]
- [[A Java lambda is an anonymous object implementing a functional interface's single abstract method, not a value of a function type|A Java lambda is an anonymous object implementing a functional interface's single abstract method]]
- [[First-class functions treat functions as values that can be passed, stored, and returned]]
- [[Java MOC]]
