---
aliases: [thread stack, per-thread stack, local variables and threads]
created: 2026-08-19
tags: [java, concurrency]
---

Every running thread — the main thread, and every `Thread` you spawn — gets its **own call stack**, allocated separately by the JVM. A method's local variables live as slots on that thread's stack frame for that method call.

<mark style="background: #FFF3A3A6;"><b>Because each thread's stack is private to it, one thread cannot directly read or write a local variable that lives on a different thread's stack.</b></mark> There's no shared address for it to reach into — it simply isn't there.

---

### Why this matters for a spawned Thread

```java
void sendAll() {
    String recipient = "a@example.com";   // lives on sendAll()'s stack frame

    new Thread(() -> sendEmail(recipient)).start();
    // sendAll() may return — its stack frame is popped — before the new thread even runs
}
```

By the time the new thread actually executes, `sendAll()`'s stack frame may already be gone. The new thread was never going to be able to reach into it anyway — stacks aren't shared. So whatever the lambda needs from that scope has to be handed to it some other way: copied into the lambda object itself, on the heap, which *is* visible to every thread.

This is exactly the mechanism behind [[A Java lambda closure captures references to variables from its enclosing scope, which must be final or effectively final|closure capture]] — the JVM copies the captured value into the lambda at creation time, because there's no way to let the lambda read the original stack slot later, from another thread.

Instance fields and heap objects don't have this problem — the heap is shared across all threads, so any thread can read `this.someField` regardless of which thread created the object.

### Read more

- [[A Java lambda closure captures references to variables from its enclosing scope, which must be final or effectively final]]
- [[Thread.start() launches a new OS thread asynchronously, while calling run() directly executes synchronously on the caller's thread]]
- [[Java MOC]]
