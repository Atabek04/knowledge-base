---
aliases: [closure, effectively final, capturing lambda, lambda capture]
created: 2026-08-19
tags: [java]
---

A lambda's body often refers to variables it never received as parameters — a service object, a loop value, a string built earlier in the method. Where do those come from once the lambda runs later, possibly on a different thread, after the method that created it has already returned?

<mark style="background: #FFF3A3A6;"><b>A closure is a function (or lambda) that captures references to the variables and objects from the scope it was written in, and keeps them alive for whenever it actually runs.</b></mark> It's not copying values at creation time in some vague sense — it's holding onto the actual references, the same way a class holds a field.

---

### It behaves like an invisible field

```java
EmailService emailService = new EmailService();
String a = "a@example.com";

Thread t1 = new Thread(() -> emailService.sendEmail(a));
```

The lambda never took `emailService` or `a` as parameters. It just reaches into the enclosing method's scope and grabs them — the same job `EmailTask`'s `recipient` field did explicitly, except the compiler does it for you.

### Captured locals must be final or effectively final

A local variable lives on the stack frame of the method that declared it — and [[Each Java thread has its own call stack, so a local variable is never directly visible to another thread|every thread has its own, private stack]]. A lambda might not run on the same thread that created it, and by the time it does run, the method that declared the variable may have already returned — its stack frame gone.

So the lambda can't "look up the current value" later; there's no shared place left to look. The only option is for the JVM to **copy the variable's value into the lambda itself**, at the moment the lambda is created — a hidden field on a heap object, which every thread *can* see.

That copy creates the question the restriction answers: what happens if the original variable changes *after* the copy was taken?

- **Silent staleness** — you'd reassign the variable expecting the lambda to now use the new value (that's how a field or object reference behaves), but the lambda's copy is frozen from capture time. Nothing errors; the lambda just quietly keeps using the old value. A real, easy-to-miss bug.
- **Or, if Java tried to track the live value instead of freezing a copy** — it would need real [[A plain shared variable's write is not guaranteed to be visible to another thread without synchronization|cross-thread synchronization]] just for a local variable, and locals have no synchronization tools available at all (no `volatile` local, no way to `synchronize` a stack slot) — those only exist for heap-based fields.

<mark style="background: #FF5582A6;"><b>Java sidesteps the whole problem by requiring captured locals to be `final` or effectively final — never reassigned after their initial value. That guarantees the frozen copy inside the lambda can never go stale, because there's nothing left for it to diverge from.</b></mark>

```java
String name = "Atabek";
Runnable r = () -> System.out.println(name);  // OK — name is never reassigned

String status = "pending";
status = "done";                               // reassigned
Runnable r2 = () -> System.out.println(status); // compile error
```

This is **not** about calling one lambda's `run()` multiple times — that's always fine, same frozen value every time. It's about the *source variable* being reassigned after capture. Two separate lambdas, each closing over its own distinct variable that's never reassigned, have no conflict at all:

```java
String r1 = "a@example.com";
Runnable t1 = () -> sendEmail(r1);   // freezes r1's value into t1

String r2 = "b@example.com";
Runnable t2 = () -> sendEmail(r2);   // a different variable — freezes r2's value into t2
```

Instance fields and `this` don't have this restriction — a lambda inside an instance method can freely read and write `this.someField`, because that field lives on the heap with the object, not on a stack frame that might disappear. That's exactly where a [[Thread.start() launches a new OS thread asynchronously, while calling run() directly executes synchronously on the caller's thread|named class]] earns its keep over a lambda — its fields are mutable and reusable across many `run()` calls, with none of the effectively-final ceiling a closure is stuck under.

### Read more

- [[Each Java thread has its own call stack, so a local variable is never directly visible to another thread]]
- [[A plain shared variable's write is not guaranteed to be visible to another thread without synchronization]]
- [[Thread.start() launches a new OS thread asynchronously, while calling run() directly executes synchronously on the caller's thread]]
- [[A Java lambda is an anonymous object implementing a functional interface's single abstract method, not a value of a function type]]
- [[Java MOC]]
