---
aliases: [companion object]
created: 2026-03-27
tags: [kotlin, oop]
---

### Kotlin has no `static` keyword

In Java, `static` members belong to the class, not instances:

```java
class User {
    static int MAX_AGE = 150;
    static User fromEmail(String email) { ... }
}
User.MAX_AGE;
User.fromEmail("a@b.com");
```

Kotlin replaces this with `companion object` — a singleton tied to the class:

```kotlin
class User(val name: String) {
    companion object {
        const val MAX_AGE = 150
        fun fromEmail(email: String) = User(email.substringBefore("@"))
    }
}

User.MAX_AGE                    // 150
User.fromEmail("ayub@mail.com") // User(name=Ayub)
```

---

### How it works

A `companion object` is just an [[Kotlin object declaration creates a singleton instance immediately|object declaration]] nested inside a class. The difference: you access its members through the **class name** directly, without naming the object.

---

### Common use case — factory methods

Instead of multiple constructors, use companion object for readable creation:

```kotlin
class Color(val r: Int, val g: Int, val b: Int) {
    companion object {
        fun red() = Color(255, 0, 0)
        fun fromHex(hex: String): Color { /* parse */ }
    }
}

val red = Color.red()
val custom = Color.fromHex("#FF5582")
```

---

Read more:

- [[Kotlin object declaration creates a singleton instance immediately]]
- [[Kotlin MOC]]
