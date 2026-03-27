---
aliases: [when expression]
created: 2026-03-26
tags: [kotlin, control-flow]
---

### Java `switch` vs Kotlin `when`

Java's `switch` is limited — only works with primitives, strings, enums. Needs `break` everywhere. Can't return values (until Java 14+).

Kotlin's `when` fixes all of that.

---

### Basic usage — matching values

```kotlin
val result = when (obj) {
    "1" -> "One"
    "Hello" -> "Greeting"
    else -> "Unknown"
}
```

No `break` needed. Each branch is isolated. And it <mark style="background: #FFF3A3A6;">returns a value</mark> — you can assign it directly.

---

### Multiple values in one branch

```kotlin
when (x) {
    0, 1 -> "binary"
    else -> "other"
}
```

---

### Range checking

```kotlin
when (score) {
    in 90..100 -> "A"
    in 80..89 -> "B"
    in 70..79 -> "C"
    else -> "F"
}
```

Java `switch` can't do this at all.

---

### Type checking with smart cast

```kotlin
when (obj) {
    is String -> println(obj.length)   // smart cast — obj is already String here
    is Int -> println(obj + 1)
    else -> println("unknown")
}
```

No need to manually cast after checking — Kotlin does it for you.

---

### Without argument — replaces `if-else` chains

```kotlin
when {
    x.isOdd() -> "x is odd"
    y.isEven() -> "y is even"
    else -> "x+y is odd"
}
```

Each branch is just a boolean expression. Cleaner than nested `if-else`.

---

### With enums — exhaustive checking

```kotlin
enum class State { IDLE, RUNNING, FINISHED }

val message = when (state) {
    State.IDLE -> "It's idle"
    State.RUNNING -> "It's running"
    State.FINISHED -> "It's finished"
}
// no `else` needed — compiler knows all cases are covered
```

<mark style="background: #BBFABBA6;">If you add a new enum value later, the compiler forces you to handle it.</mark> Java `switch` silently falls through to `default`.

---

### Why it's better than Java `switch`

| Feature | Java `switch` | Kotlin `when` |
|---|---|---|
| Returns a value | Java 14+ only | Always |
| Needs `break` | Yes | No |
| Range checks | No | `in 1..10` |
| Type checks | No | `is Type` + smart cast |
| Boolean conditions | No | Yes (without argument) |
| Exhaustive enums | No | Compiler-enforced |

---

Read more:

- [[Casting converts between types in an inheritance hierarchy]]
- [[Kotlin MOC]]
