---
aliases: [nullable types]
created: 2026-03-26
tags: [kotlin, null-safety]
---

### `Type?` means "this can be null"

By default, Kotlin variables **cannot** be null:

```kotlin
var name: String = "Ayub"
name = null  // ❌ Compile error — String can't hold null
```

Adding `?` makes it nullable:

```kotlin
var name: String? = "Ayub"
name = null  // ✅ String? accepts null
```

---

### The compiler enforces safe access

Once a variable is nullable, Kotlin won't let you use it unsafely:

```kotlin
val name: String? = null
println(name.length)   // ❌ Compile error — name could be null
println(name?.length)  // ✅ Safe call — returns null instead of crashing
```

<mark style="background: #FFF3A3A6;">The `?` in the type is a contract: you're telling Kotlin "null is possible here," and Kotlin holds you to it.</mark>

---

Read more:

- [[Safe call operator avoids null crashes by returning null instead]]
- [[Elvis operator provides a default when left side is null]]
- [[Kotlin tells you to declare variables with initialization]]
- [[Kotlin MOC]]
