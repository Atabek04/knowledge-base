---
aliases: [Strategy in Kotlin, Kotlin Strategy pattern]
---

This is the idiomatic Kotlin implementation of the [[The Strategy pattern makes algorithms interchangeable by hiding each behind a common interface|Strategy pattern]]. Because Kotlin has first-class functions, the whole Strategy *interface* collapses into a **function type** — no interface, no concrete classes, far less boilerplate than Java.

### Strategy as a function type

A `typealias` names the contract. Each concrete strategy is just a lambda.

```kotlin
typealias PaymentStrategy = (Order) -> Unit

val creditCard: PaymentStrategy = { order -> /* charge card */ }
val payPal: PaymentStrategy     = { order -> /* redirect to PayPal */ }
```

### The Context holds the function

```kotlin
class CheckoutService(private val pay: PaymentStrategy) {
    fun checkout(order: Order) = pay(order)   // no if/else
}
```

### Selecting the strategy

```kotlin
val strategies = mapOf("card" to creditCard, "paypal" to payPal)

CheckoutService(strategies.getValue("paypal")).checkout(order)
```

### When you still want an interface

A bare function works when the strategy is *stateless* and has *one* operation. <mark style="background: pink">If a strategy needs shared state or several related methods, fall back to an `interface`</mark> — and a class can still implement the function type via `operator fun invoke`:

```kotlin
class CryptoPayment(private val wallet: Wallet) : PaymentStrategy {
    override fun invoke(order: Order) { /* use wallet */ }
}
```

### Read more
- [[The Strategy pattern makes algorithms interchangeable by hiding each behind a common interface]]
- [[Strategy pattern in Python uses a first-class function as the strategy]]
- [[Strategy pattern in Java is an interface implemented by interchangeable algorithm classes]]
