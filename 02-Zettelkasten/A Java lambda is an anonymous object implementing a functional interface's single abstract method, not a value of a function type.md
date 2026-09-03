---
aliases: [Java lambda, lambda expression, lambda vs functional interface]
created: 2026-08-19
tags: [java]
---

A [[A Java functional interface has exactly one abstract method — default and static methods don't count toward that limit|functional interface]] describes a shape — one method, one signature. A lambda is what fills that shape.

<mark style="background: #FFF3A3A6;"><b>Functional interface = the type / contract. Lambda = the value</b> — a concrete, anonymous object built on the spot whose body becomes the implementation of that one abstract method.</mark> They're not synonyms; one names a shape, the other is a thing shaped that way.

Analogy: the functional interface is the socket shape — one slot, this size. The lambda is the plug you make to fit it. The socket shape doesn't run anything by itself; you need an actual plug.

---

### Matching a lambda to its interface

```java
Thread t1 = new Thread(() -> sendEmail(a));
```

- `Runnable` is the **functional interface** — the parameter type `Thread`'s constructor declares it needs.
- `() -> sendEmail(a)` is the **lambda** — the actual object passed in.

The compiler checks: does this lambda's parameter list and return type match the interface's one abstract method? `Runnable.run()` takes nothing and returns nothing; `() -> sendEmail(a)` takes nothing and returns nothing → match. The compiler then wraps the lambda body into an anonymous `Runnable` instance behind the scenes.

Swap the interface and the same lambda syntax means something else entirely:

```java
Function<String, String> greet = name -> "Hi, " + name;
```

Here the lambda implements `Function<T, R>`'s `apply()` method instead — same lambda *syntax*, different target type, different generated object.

---

### Lambdas are objects, not functions

<mark style="background: #FF5582A6;"><b>Java has no true first-class functions. A lambda does not exist independently of some functional-interface type — it is always compiled into an instance of whichever interface the context expects.</b></mark> This matters for two concrete things:

- **Reference identity** — two lambdas with identical code are not guaranteed to be the same object by reference; each is its own instance.
- **Serialization** — a lambda can only be serialized if its target functional interface (and the lambda itself) is explicitly marked `Serializable`; plain lambdas aren't serializable by default.

### Read more

- [[A Java functional interface has exactly one abstract method — default and static methods don't count toward that limit]]
- [[First-class functions treat functions as values that can be passed, stored, and returned]]
- [[Java MOC]]
