---
aliases: [Composition over inheritance, Composition vs inheritance, HAS-A vs IS-A]
---

There are two ways for one class to reuse another's behavior, and their names tell you exactly how they work.

**Inheritance** — a subclass *inherits* a parent's behavior. The relationship is <mark style="background: yellow">**IS-A**</mark>: a `CreditCardPayment` *is a* `Payment`. The behavior is fixed at compile time and baked into the class.

**Composition** — an object is *composed* of other objects it holds and delegates to. The relationship is <mark style="background: yellow">**HAS-A**</mark>: a `CheckoutService` *has a* payment behavior and *has a* receipt behavior. The parts can be swapped at runtime.

The Gang of Four's first principle: <mark style="background: yellow">**favor composition over inheritance.**</mark>

### Runtime vs compile time

This is the deepest reason to prefer composition:

- <mark style="background: yellow">**Inheritance** is resolved at **compile time**.</mark> The behavior a subclass has is baked in — `CreditCardPayment extends Payment` is fixed forever. You cannot swap it while the program runs.
- <mark style="background: yellow">**Composition** is resolved at **runtime**.</mark> The composed object is an interface reference — the actual implementation is unknown until someone injects it. You can pass a different one on every call.

The composed field (`private val pay: PaymentStrategy`) is just a slot. Whatever object fills that slot at runtime *is* the behavior. That is why Strategy, Decorator, and State all rely on composition: they all need to change behavior *without* recompiling.

---

### The problem with inheritance: combinatorial explosion

Inheritance handles **one** axis of variation cleanly. The moment **two** behaviors vary *independently*, it explodes — because a class is one fixed thing, so every *combination* needs its own subclass.

Say payment type (card, PayPal, crypto) and receipt delivery (email, SMS, none) vary independently. Baking both into the hierarchy:

| | Email | SMS | None |
|---|---|---|---|
| **Card** | CardEmail | CardSms | CardNone |
| **PayPal** | PayPalEmail | PayPalSms | PayPalNone |
| **Crypto** | CryptoEmail | CryptoSms | CryptoNone |

That's <mark style="background: pink">3 × 3 = 9 classes</mark>. Add a 4th payment → it must pair with all 3 receipts → **+3**. Then a 4th receipt → pairs with all 4 payments → **+4**. Total **16**. Growth is **multiplicative**.

### The composition fix

Give each varying behavior its own family, and let one object *hold* both. They mix at runtime:

```kotlin
class CheckoutService(
    private val pay: (Order) -> Unit,      // HAS-A payment behavior
    private val sendReceipt: (Order) -> Unit  // HAS-A receipt behavior
) {
    fun checkout(order: Order) {
        pay(order)
        sendReceipt(order)
    }
}
```

Now it's <mark style="background: green">3 + 3 = 6</mark> pieces. Add a payment → **+1**. Add a receipt → **+1**. Growth is **additive**. The 4th-of-each case: composition needs **2** new pieces (total 8); inheritance needs **16**.

### When to use each

- **Use composition** when behavior *varies*, is *reused* across unrelated types, or must change at runtime. This is the default.
- **Use inheritance** only for a *true* IS-A relationship — a genuine, stable subtype — not merely to share code. Subclassing for code reuse causes the <mark style="background: pink">fragile base class problem</mark>: a change in the parent silently breaks every child.

Rule of thumb: <mark style="background: cyan">if you can't honestly say "child *is a* parent" in plain English, you want composition.</mark>

### Read more
- [[The Strategy pattern makes algorithms interchangeable by hiding each behind a common interface]]
- [[The Gang of Four book cataloged 23 reusable object-oriented design patterns]]
- [[Software Engineering Principles - MOC]]
- [[Design Patterns - MOC]]
