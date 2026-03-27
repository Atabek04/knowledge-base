---
aliases: [collection transformations, filter map flatMap]
created: 2026-03-27
tags: [kotlin, collections]
---

### `filter {}` — keep items matching a condition

```kotlin
val nums = listOf(1, 2, 3, 4, 5)
nums.filter { it > 3 }  // [4, 5]
```

---

### `map {}` — transform each item

```kotlin
val names = listOf("ayub", "ali")
names.map { it.uppercase() }  // [AYUB, ALI]
```

---

### `flatMap {}` — transform each item to a list, then flatten

```kotlin
val groups = listOf(listOf(1, 2), listOf(3, 4))
groups.flatMap { it }  // [1, 2, 3, 4]

// more practical:
val users = listOf(User("Ayub", listOf("A", "B")), User("Ali", listOf("C")))
users.flatMap { it.tags }  // [A, B, C]
```

`map` would give you `[[A, B], [C]]` — a list of lists. `flatMap` unwraps them into one flat list.

---

### `associate {}` — list → map

```kotlin
val users = listOf(User(1, "Ayub"), User(2, "Ali"))
users.associate { it.id to it.name }  // {1=Ayub, 2=Ali}
```

---

### `groupBy {}` — list → map of lists

```kotlin
val words = listOf("apple", "ant", "banana", "bat")
words.groupBy { it.first() }
// {a=[apple, ant], b=[banana, bat]}
```

---

### `any {}` / `none {}` / `all {}` — boolean checks

```kotlin
val nums = listOf(1, 2, 3, 4)

nums.any { it > 3 }   // true — at least one matches
nums.none { it > 5 }  // true — no item matches
nums.all { it > 0 }   // true — every item matches
```

---

### `first {}` / `firstOrNull {}` — find one item

```kotlin
val nums = listOf(1, 2, 3, 4)

nums.first { it > 2 }        // 3
nums.first { it > 10 }       // 💥 NoSuchElementException

nums.firstOrNull { it > 2 }  // 3
nums.firstOrNull { it > 10 } // null (safe)
```

<mark style="background: #FF5582A6;">Use `firstOrNull` when you're not sure a match exists.</mark>

---

### Chaining — the real power

Transformations return new collections, so you chain them:

```kotlin
data class Order(val customer: String, val amount: Double, val paid: Boolean)

val orders = listOf(
    Order("Ayub", 100.0, true),
    Order("Ali", 50.0, false),
    Order("Ayub", 200.0, true)
)

val ayubTotal = orders
    .filter { it.customer == "Ayub" }  // keep Ayub's orders
    .filter { it.paid }                // keep paid only
    .map { it.amount }                 // extract amounts
    .sum()                             // 300.0
```

---

Read more:

- [[Kotlin has 3 main collections for grouping items]]
- [[To check that an item is in a list, use in operator]]
- [[Kotlin MOC]]
