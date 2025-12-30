Parent: [[Kotlin MOC]]

---

## Java has 2 Type System

1. **Primitive**: int, boolean, double, char, etc.
2. **Wrappers**: Integer, Boolean, Double, Character, etc.

---
#### Why this duality?

<mark style="background: #FFB86CA6;">Performance reason.</mark>
Primitives are stored directly in stack.
Objects are stored on heap with reference overhead.

---
#### JVM connection

This duality actually coupled with JVM architecture
JVM optimized for primitive operations

---
#### Why not just Objects?

Performance penalty:
- heap allocation
- GC overhead
- pointer dereferencing, etc.

---
### Trade-off

Primitives :luc_arrow_right_circle: fast, but **can't use in generics or collections**
Wrappers :luc_arrow_right_circle: work everywhere, but **slower**

**Autoboxing** (Java 5+) bridges the gap automatically

---

## Kotlin's Approach

### Single Type System

You always write: `val age: Int = 21`
No Integer wrapper class exposed
Everything looks like an object

#### Under the hood

Kotlin compiler decides.

Uses primitives when possible:
- non-nullable types

Users wrappers when necessary:
- nullable types
- generic types

```kotlin
val a: Int = 5        // → int a = 5
val b: Int? = null    // → Integer b = null
val list = listOf(1)  // → List<Integer>
```

---