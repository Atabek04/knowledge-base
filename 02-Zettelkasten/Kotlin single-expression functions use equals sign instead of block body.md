---
aliases: [expression body, single-expression function]
created: 2026-03-26
tags: [kotlin, functions]
---

### Block body — verbose for one-liners

```kotlin
fun double(x: Int): Int {
    return x * 2
}
```

---

### Expression body — drop `{}` and `return`

When a function has only one expression, use '=' instead:

```kotlin
fun double(x: Int): Int = x * 2
```

The return type can even be inferred:

```kotlin
fun double(x: Int) = x * 2
```

---

### Works great with `when`

```kotlin
fun describe(x: Int) = when {
    x > 0 -> "positive"
    x < 0 -> "negative"
    else -> "zero"
}
```

---

Read more:

- [[Kotlin allows top-level functions]]
- [[Kotlin when expression replaces switch with more power and flexibility]]
- [[Kotlin MOC]]
