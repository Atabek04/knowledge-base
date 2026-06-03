---
aliases: [Kotlin single type system]
created: 2025-12-30
tags: [kotlin, types]
---

### No dual system

Unlike [[Java has dual type system because JVM optimizes primitives for performance|Java's dual type system]], Kotlin has **one unified type system**.

You always write `Int`, never `Integer`. No primitives vs wrappers distinction at the language level.

```kotlin
val age: Int = 21     // looks like an object
val active: Boolean = true
```

---

### Under the hood — compiler decides

Kotlin compiler optimizes automatically:

- **Non-nullable** → compiles to JVM primitive (`int`, `boolean`)
- **Nullable or generic** → compiles to wrapper (`Integer`, `Boolean`)

```kotlin
val a: Int = 5        // → int a = 5
val b: Int? = null    // → Integer b = null
val list = listOf(1)  // → List<Integer>
```

<mark style="background: #FFF3A3A6;">You get Java's performance without managing two type systems.</mark>

---

Read more:

- [[Java has dual type system because JVM optimizes primitives for performance]]
- [[Variable declaration in Kotlin is done by var and val]]
- [[Kotlin MOC]]
