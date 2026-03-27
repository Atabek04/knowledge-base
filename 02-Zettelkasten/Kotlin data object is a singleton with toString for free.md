---
aliases: [data object]
created: 2026-03-27
tags: [kotlin, oop]
---

### `data object` — singleton that prints nicely

Use when a variant has **no data** to carry:

```kotlin
sealed interface PaymentError {
    data object UnsupportedCurrency : PaymentError
}

println(PaymentError.UnsupportedCurrency)
// UnsupportedCurrency (not PaymentError$UnsupportedCurrency@3a71f4dd)
```

Regular `object` prints a memory address. `data object` auto-generates `toString()`.

---

### `data object` vs `data class` vs `object`

| | `object` | `data object` | `data class` |
|---|---|---|---|
| Singleton | Yes | Yes | No |
| `toString()` | Memory address | Class name | Property values |
| Holds data | No | No | Yes |

---

Read more:

- [[Kotlin sealed types restrict subclasses to compile-time known set]]
- [[Kotlin data class auto-generates common methods for data holders]]
- [[Kotlin MOC]]
