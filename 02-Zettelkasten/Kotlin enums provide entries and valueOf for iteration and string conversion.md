---
aliases: [enum entries, enum valueOf]
created: 2026-03-27
tags: [kotlin, enums]
---

### `entries` — iterate over all enum values

Kotlin's replacement for Java's `values()`:

```kotlin
enum class Color { RED, GREEN, BLUE }

Color.entries.forEach { println(it) }
// RED
// GREEN
// BLUE
```

---

### `valueOf()` — string to enum

Converts a string to its matching enum constant:

```kotlin
val color = Color.valueOf("RED")  // Color.RED
val bad = Color.valueOf("PURPLE") // 💥 IllegalArgumentException
```

<mark style="background: #FF5582A6;">Case-sensitive and crashes if no match.</mark> Validate input before calling.

---

Read more:

- [[Kotlin enums can have methods that enforce business rules]]
- [[Kotlin MOC]]
