---
aliases: [Thread vs Runnable, start vs run, Thread.start, Runnable]
created: 2026-08-19
tags: [java, concurrency]
---

<mark style="background: #FFF3A3A6;"><b>A `Thread` is Java's object for one OS-backed line of execution. A `Runnable` is just a task — one method, `run()`, with no return value and no special powers of its own.</b></mark>

They're separate on purpose. If `Runnable` didn't exist and the only way to define a task was `extends Thread`, every task class would be permanently welded to "is a thread" — it could never also extend some other useful base class (Java has no multiple inheritance), it couldn't be reused by handing the *same* task to a thread pool later, and testing it would mean testing a `Thread`, not just your logic.

Keeping them separate gives each object one job:

- **`Runnable`** — describes *what work to do*. Just a `run()` method. No OS resources, no thread machinery — it's inert until something executes it.
- **`Thread`** — describes *who runs it*. Owns the actual OS-backed execution: allocates a stack, gets scheduled by the OS, and calls `run()` on whatever `Runnable` it was given.

This split is also what makes `Executor` (the next chunk) possible at all: once "the task" and "the thing that runs it" are separate objects, you can swap out *how* a `Runnable` gets executed — new thread each time, a reused pool, a scheduled delay — without changing the task's code at all.

---

### Two ways to attach work to a Thread

**Preferred — implement `Runnable`, hand it to a `Thread`:**

```java
public class EmailTask implements Runnable {
    private final String recipient;

    public EmailTask(String recipient) {
        this.recipient = recipient;
    }

    @Override
    public void run() {
        sendEmail(recipient);
    }
}

Thread t = new Thread(new EmailTask("a@example.com"));
```

A class earns the extra ceremony when the task has its own state (fields) or logic worth naming and testing in isolation — like `recipient` here.

**Less common — `extends Thread`, override `run()`.** Ties your task class to *being* a thread, which is rarely what you want.

#### Lambda shorthand

`Runnable` is a [[A Java functional interface has exactly one abstract method — default and static methods don't count toward that limit|functional interface]] — it has exactly one abstract method, `run()` — so [[A Java lambda is an anonymous object implementing a functional interface's single abstract method, not a value of a function type|a lambda]] can stand in for it directly:

```java
Thread t1 = new Thread(() -> sendEmail(a));
```

The lambda body *is* `run()`'s body. It's a [[A Java lambda closure captures references to variables from its enclosing scope, which must be final or effectively final|closure]] — it can call methods on any object reachable from its surrounding scope (e.g. `emailService.sendEmail(a)`), not just methods in the same class. Good for a one-off inline task; a named class is better once there's state worth carrying.

---

### `start()` vs `run()` — the trap

<mark style="background: #FF5582A6;"><b>Calling `.start()` asks the OS to spin up a brand-new thread and returns almost immediately — it does not wait for the task to finish. Calling `.run()` directly is just a normal method call: it executes on the current thread and blocks like any other method.</b></mark>

```java
Thread t1 = new Thread(() -> sendEmail(a));
Thread t2 = new Thread(() -> sendEmail(b));

t1.start();  // returns immediately; t1's thread runs sendEmail(a) in the background
t2.start();  // runs concurrently with t1 — total time ≈ max(a, b), not a + b

t1.run();    // WRONG: no new thread. Executes on the caller's thread, blocks until done.
t2.run();    // then this blocks too — back to fully sequential, same as no threads at all
```

Mixing up `run()` for `start()` throws no error and gives no warning — it silently turns concurrent code back into sequential code. This is a real, easy-to-ship bug.

**Why does `Thread` even expose `run()` publicly?** Because when you `extends Thread` and override it, the new OS-backed thread needs *some* public method to call into — `run()` is that entry point either way.

### Read more

- [[A Java functional interface has exactly one abstract method — default and static methods don't count toward that limit]]
- [[A Java lambda is an anonymous object implementing a functional interface's single abstract method, not a value of a function type]]
- [[A Java lambda closure captures references to variables from its enclosing scope, which must be final or effectively final]]
- [[Java MOC]]
