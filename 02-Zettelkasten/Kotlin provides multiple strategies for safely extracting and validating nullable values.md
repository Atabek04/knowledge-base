---
aliases: [null validation strategies]
created: 2026-03-27
tags: [kotlin, null-safety]
---

### Strategy 1 — `?.` safe call: skip if null

```kotlin
val length = name?.length  // null if name is null, no crash
```

Use when: null result is acceptable.

---

### Strategy 2 — `?:` elvis: provide default

```kotlin
val length = name?.length ?: 0
```

Use when: you need a fallback value.

---

### Strategy 3 — `?.let {}`: execute block only if not null

```kotlin
name?.let { println("Name is $it") }
```

Use when: you want to run logic only on non-null values.

---

### Strategy 4 — `requireNotNull()`: crash with clear message if null

```kotlin
val name = requireNotNull(nullableName) { "Name must not be null" }
// throws IllegalArgumentException if null
```

Use when: null means a **bug** — the value should never be null at this point.

---

### Strategy 5 — `require()`: validate a condition

```kotlin
require(age > 0) { "Age must be positive, got $age" }
// throws IllegalArgumentException if condition is false
```

Use when: validating **input** at function boundaries.

---

### When to use which?

| Strategy | Intent | On null/fail |
|---|---|---|
| `?.` | Null is fine, skip it | Returns `null` |
| `?:` | Null is fine, use default | Returns fallback |
| `?.let {}` | Run code only if present | Skips block |
| `requireNotNull()` | Null is a bug | Throws exception |
| `require()` | Invalid input | Throws exception |

<mark style="background: #FFF3A3A6;">`?.` and `?:` are lenient — they handle null gracefully. `requireNotNull()` and `require()` are strict — they crash fast when assumptions are violated.</mark>

---

Read more:

- [[Safe call operator avoids null crashes by returning null instead]]
- [[Elvis operator provides a default when left side is null]]
- [[Kotlin let executes a block on a non-null object and returns the result]]
- [[Kotlin nullable types are declared with question mark suffix]]
- [[Kotlin MOC]]
