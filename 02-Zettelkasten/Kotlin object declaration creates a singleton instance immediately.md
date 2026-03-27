---
aliases: [object declaration, singleton]
created: 2026-03-27
tags: [kotlin, oop]
---

### `class` vs `object` — the core difference

`class` is a **blueprint** — you create instances from it:

```kotlin
class User(val name: String)

val user1 = User("Ayub")   // instance 1
val user2 = User("Ali")    // instance 2 — different object
```

`object` is a **single instance that already exists** — no constructor, no `new`, only one ever:

```kotlin
object Logger {
    fun log(msg: String) = println(msg)
}

Logger.log("Hello")  // use directly — there's only one Logger
```

---

### Why use it?

When you need **exactly one instance** — utilities, config, registries:

```kotlin
object DatabaseConfig {
    val url = "jdbc:postgresql://localhost:5432/mydb"
    val maxConnections = 10
}
```

In Java you'd write a class with a private constructor and a `static getInstance()` method. Kotlin does it in one keyword.

---

### `object` vs `data object`

```kotlin
object Foo        // toString() → Foo@3a71f4dd (memory address)
data object Foo   // toString() → Foo (clean name)
```

`data object` is just an `object` with a readable `toString()`. Useful inside [[Kotlin sealed types restrict subclasses to compile-time known set|sealed types]] for variants that carry no data.

---

Read more:

- [[Kotlin data object is a singleton with toString for free]]
- [[Kotlin data class auto-generates common methods for data holders]]
- [[Kotlin MOC]]
