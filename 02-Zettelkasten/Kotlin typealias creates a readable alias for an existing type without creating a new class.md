---
aliases: [typealias, Kotlin typealias]
---

`typealias` gives an existing type a new name. No new class is created — the alias and the original type are interchangeable at runtime. The only benefit is **readability at the call site**.

### Syntax

```kotlin
typealias PaymentStrategy = (Order) -> Unit
typealias UserId = Long
typealias UserMap = Map<UserId, List<String>>
```

After the alias, `PaymentStrategy` and `(Order) -> Unit` are identical to the compiler.

### Most common use: naming function types

<mark style="background: yellow">Function types like `(Order) -> Unit` are hard to read at a glance.</mark> A `typealias` makes the intent visible:

```kotlin
// Before
class CheckoutService(private val pay: (Order) -> Unit)

// After
typealias PaymentStrategy = (Order) -> Unit
class CheckoutService(private val pay: PaymentStrategy)
```

This is the idiomatic way to implement the [[Strategy pattern in Kotlin uses a function type instead of an interface|Strategy pattern in Kotlin]] — the `typealias` acts as the strategy "interface".

### What it is NOT

- <mark style="background: pink">**Not a new type**</mark> — the compiler treats `typealias Foo = Bar` as exactly `Bar`. You cannot overload on `Foo` vs `Bar`, and they satisfy each other's type constraints.
- **Not a value class** — use `@JvmInline value class` if you want actual type safety with zero runtime overhead.

### Read more
- [[Strategy pattern in Kotlin uses a function type instead of an interface]]
- [[First-class functions treat functions as values that can be passed, stored, and returned]]
