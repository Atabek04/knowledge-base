---
aliases: [primary constructor]
created: 2026-03-26
tags: [kotlin, oop]
---

### Why `()` not `{}`?

The `()` in a class declaration is the <mark style="background: #FFF3A3A6;">primary constructor</mark> — it declares constructor parameters right in the class header.

```kotlin
// This:
class User(val name: String, val age: Int)

// Is shorthand for:
class User {
    val name: String
    val age: Int
    
    constructor(name: String, age: Int) {
        this.name = name
        this.age = age
    }
}
```

---

### `{}` is for the class body

If you need methods or extra properties, add `{}`. If not, skip it entirely.

```kotlin
data class User(val name: String, val age: Int)  // no {} needed

class Car(val brand: String) {
    fun drive() = println("Driving $brand")  // needs {}
}
```

---

Read more:

- [[Kotlin data class auto-generates common methods for data holders]]
- [[Kotlin MOC]]
