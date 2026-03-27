---
aliases: [elvis operator]
created: 2026-03-26
tags: [kotlin, null-safety]
---

### `?:` — "if null, use this instead"

```kotlin
val name: String? = null
val length = name?.length ?: 0  // name is null → length = 0

val name2: String? = "Ayub"
val length2 = name2?.length ?: 0  // not null → length2 = 4
```

---

### Pairs naturally with safe call `?.`

Safe call gets the value *or null*, Elvis provides the fallback:

```kotlin
val city = user?.address?.city ?: "Unknown"
```

If `user`, `address`, or `city` is null → you get `"Unknown"`. No crash, no nested if-checks.

---

### Can also throw or return

Elvis isn't limited to default values:

```kotlin
val name = user?.name ?: throw IllegalArgumentException("Name required")

// Or early return in a function
fun greet(user: User?) {
    val name = user?.name ?: return
    println("Hello, $name")
}
```

---

Read more:

- [[Safe call operator avoids null crashes by returning null instead]]
- [[Kotlin MOC]]
