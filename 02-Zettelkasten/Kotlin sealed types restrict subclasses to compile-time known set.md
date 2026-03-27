---
aliases: [sealed class, sealed interface]
created: 2026-03-27
tags: [kotlin, oop]
---

### The problem enums can't solve

Enums are great when every variant is a singleton with the same shape. But what if each variant carries **different data**?

```kotlin
// Enum — every entry has the same properties
enum class Color(val hex: String) {
    RED("#FF0000"),
    GREEN("#00FF00")
    // every entry MUST have hex — same shape
}

// But what about errors?
// InsufficientFunds needs: balance, required
// CardExpired needs: expiry date
// GatewayTimeout needs: retry duration
// Each error carries DIFFERENT data — enums can't do this
```

In Java you'd use an abstract class with subclasses — then pray nobody forgets a case in `instanceof` chains.

Kotlin's sealed types solve this:

```kotlin
sealed interface PaymentError {
    data class InsufficientFunds(val balance: BigDecimal, val required: BigDecimal) : PaymentError
    data class CardExpired(val expiry: YearMonth) : PaymentError
    data class GatewayTimeout(val retryAfter: Duration) : PaymentError
    data object UnsupportedCurrency : PaymentError  // no data needed
}
```

Each subtype is its own class with its own properties. But the compiler **knows all of them** — just like enums.

---

### Exhaustive `when` — forget a case and it won't compile

```kotlin
fun describe(error: PaymentError): String = when (error) {
    is PaymentError.InsufficientFunds -> "Need ${error.required}, have ${error.balance}"
    is PaymentError.CardExpired -> "Card expired: ${error.expiry}"
    is PaymentError.GatewayTimeout -> "Retry in ${error.retryAfter}"
    PaymentError.UnsupportedCurrency -> "Currency not supported"
}
```

<mark style="background: #FFF3A3A6;">Same exhaustiveness guarantee as enums — add a new subtype later and the compiler forces you to handle it.</mark>

Note: `data class` subtypes use `is` for type checking (they have instances). `data object` is a singleton — compared directly without `is`.

---

### Sealed vs Enum — when to use which?

| | Enum | Sealed |
|---|---|---|
| Each entry | Singleton, same properties | Own class, own data |
| Good for | Statuses, types, fixed sets | Errors, results, events |
| Data per variant | Same shape for all | Different payload each |

---

Read more:

- [[Kotlin enums can have methods that enforce business rules]]
- [[Kotlin sealed interface is preferred over sealed class]]
- [[Kotlin data object is a singleton with toString for free]]
- [[Kotlin data class auto-generates common methods for data holders]]
- [[Kotlin MOC]]
