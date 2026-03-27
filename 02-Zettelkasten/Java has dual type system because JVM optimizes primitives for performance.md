---
aliases: [Java dual type system, autoboxing]
created: 2026-03-26
tags: [java, types]
---

### Two separate type systems

Java has **primitives** and **wrapper objects** for the same data:

| Primitive | Wrapper   |
| --------- | --------- |
| `int`     | `Integer` |
| `boolean` | `Boolean` |
| `double`  | `Double`  |

---

### Why the duality?

<mark style="background: #FFF3A3A6;">Performance.</mark> Primitives live on the stack — fast, no garbage collection overhead.
Objects live on the heap — slower (allocation, GC, pointer dereferencing).

But primitives **can't be used in generics or collections** (`List<int>` is illegal).
So Java needs wrappers for those cases.

---

### Autoboxing bridges the gap (Java 5+)

Java automatically converts between primitives and wrappers:

```java
List<Integer> list = new ArrayList<>();
list.add(5);           // autoboxing: int → Integer
int value = list.get(0); // unboxing: Integer → int
```

Convenient, but has a hidden cost — each autobox creates a heap object.

---

Read more:

- [[Primitive types store actual value, references store only address in memory]]
- [[Kotlin is single type system, no wrappers]]
- [[Java MOC]]
