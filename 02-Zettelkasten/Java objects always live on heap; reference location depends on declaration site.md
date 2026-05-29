---
created: 2026-05-29
tags: [java, jvm, memory]
aliases: [stack vs heap java, reference vs object memory]
---

Every Java **object** is allocated on the heap — always, regardless of where it's declared.

The **reference** (the variable holding the address) lives somewhere else:
- Local variable → **stack** (lives for the duration of the method call)
- Instance variable → **heap** (part of the enclosing object)
- Static variable → **metaspace** (class-level, lives for the class lifetime)

### Example

```java
void process() {
    List<Integer> list = new ArrayList<>();
    // 'list' reference → stack
    // ArrayList object + Integer objects → heap
}

class Foo {
    List<Integer> list = new ArrayList<>();
    // 'list' reference → heap (part of Foo instance)
    // ArrayList object + Integer objects → heap
}
```

So for `List<Integer>`: the List object and all Integer wrapper objects always live on the heap.
Only the variable `list` (the reference) changes location.

A reference has a fixed size (4 or 8 bytes) regardless of what it points to — the object size varies.
This is why passing objects to methods is cheap: you copy the reference, not the object.

---

Java has no stack-allocated objects like C++. The JVM always heap-allocates objects — with one exception: JIT escape analysis can eliminate heap allocation when it proves an object doesn't escape the method.

---

### Comparison: Java vs C++ vs Python

| Language | Default when passing to method | Opt into no-copy |
|---|---|---|
| **Java** | Reference copy (cheap) | N/A — always reference |
| **C++** | Full object copy (expensive) | `&` reference or `*` pointer |
| **Python** | Reference copy (like Java) | N/A — always reference |

**C++** defaults to copying the whole object — you must explicitly use `&` or `*` to avoid it.

**Python** behaves like Java but splits by mutability:
- Mutable (`list`, `dict`) → function can mutate caller's object
- Immutable (`int`, `str`) → "modification" silently creates a new object; original untouched

Python uses reference counting + cyclic GC instead of JVM generational heap GC. Objects still live on heap, references on stack — same mental model, different internals.

---

### Read more

- [[Primitive types store actual value, references store only address in memory]]
- [[Java has 4 types of variables each with distinct scope and memory location]]
