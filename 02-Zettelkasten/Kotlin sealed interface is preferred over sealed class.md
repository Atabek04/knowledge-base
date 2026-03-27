---
aliases: [sealed interface vs sealed class]
created: 2026-03-27
tags: [kotlin, oop]
---

### `sealed interface` vs `sealed class`

Both restrict subclasses to a compile-time known set. The difference:

- `sealed interface` — subtypes can extend **other classes** too
- `sealed class` — subtypes can only extend this one parent

```kotlin
// Preferred — flexible
sealed interface PaymentError

// Only when you need shared state in the parent
sealed class PaymentError(val timestamp: Instant)
```

<mark style="background: #FFF3A3A6;">Default to `sealed interface`. Use `sealed class` only when you need shared state or behavior in the parent.</mark>

---

Read more:

- [[Kotlin sealed types restrict subclasses to compile-time known set]]
- [[Kotlin MOC]]
