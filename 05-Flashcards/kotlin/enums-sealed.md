TARGET DECK: Tech-KB::Kotlin::Enums & Sealed Types
Tags: kotlin enums sealed
**Chapter:** Enums & Sealed Types
**Related:** [[Kotlin MOC]]

---

START
Coding Questions
How can a Kotlin enum **enforce valid state transitions** (e.g. order statuses)?
Back: By **defining a method inside the enum** that uses `when(this)` to check allowed transitions:
- Each branch lists which statuses the current status (`this`) can move to
- `next in setOf(...)` checks if the target status is in the allowed set
```kotlin
enum class OrderStatus {
    CREATED, PAID, SHIPPED, DELIVERED, CANCELLED;

    fun canTransitionTo(next: OrderStatus): Boolean = when (this) {
        CREATED -> next in setOf(PAID, CANCELLED)
        PAID -> next in setOf(SHIPPED, CANCELLED)
        SHIPPED -> next == DELIVERED
        DELIVERED, CANCELLED -> false
    }
}
```
Tags: kotlin enums sealed
<!--ID: 1774840548727-->
END

START
Coding Questions
Why does a `when` expression on an enum not require an `else` branch?
Back: Because the compiler knows **every possible value** of the enum — if all cases are covered, there's nothing left for `else` to catch.
- This is called **exhaustive** matching — every case is covered, verified at compile time
- If a new enum constant is added later, the code **won't compile** until the new case is handled
Tags: kotlin enums sealed
<!--ID: 1774840548739-->
END

START
Coding Questions
What does `next in setOf(PAID, CANCELLED)` do inside an enum method?
Back: **Checks if `next` exists in the set** `{PAID, CANCELLED}`.
- `in` is the membership operator
- Equivalent to `next == PAID || next == CANCELLED`, just cleaner
Tags: kotlin enums sealed
<!--ID: 1774840548751-->
END

START
Coding Questions
How do you **iterate over all constants** of a Kotlin enum?
Back: Using the **`entries`** property (Kotlin's replacement for Java's `values()`):
```kotlin
enum class Color { RED, GREEN, BLUE }

Color.entries.forEach { println(it) }
// RED, GREEN, BLUE
```
Tags: kotlin enums sealed
<!--ID: 1774840548764-->
END

START
Coding Questions
How do you **convert a string to a Kotlin enum** constant?
Back: Using **`valueOf()`**:
```kotlin
val color = Color.valueOf("RED")  // Color.RED
```
- **Case-sensitive** — must match exactly
- **Throws `IllegalArgumentException`** if no match — validate input before calling
Tags: kotlin enums sealed
<!--ID: 1774840548776-->
END

START
Coding Questions
What problem do **sealed types** solve that enums cannot?
Back: Enums require every entry to have the **same shape** (same properties). **Sealed types** allow each variant to carry **different data**:
- `InsufficientFunds` needs `balance` and `required`
- `CardExpired` needs `expiry`
- `GatewayTimeout` needs `retryAfter`
- `UnsupportedCurrency` needs no data at all

Each subtype is its own class with its own properties, but the compiler still **knows all of them** at compile time.
Tags: kotlin enums sealed
<!--ID: 1774840548788-->
END

START
Coding Questions
Write a sealed interface where each subtype carries different data.
Back:
```kotlin
sealed interface PaymentError {
    data class InsufficientFunds(val balance: BigDecimal, val required: BigDecimal) : PaymentError
    data class CardExpired(val expiry: YearMonth) : PaymentError
    data class GatewayTimeout(val retryAfter: Duration) : PaymentError
    data object UnsupportedCurrency : PaymentError  // no data needed
}
```
- **`data class`** subtypes carry unique properties
- **`data object`** for variants with no data
- Compiler enforces **exhaustive** `when` — same guarantee as enums
Tags: kotlin enums sealed
<!--ID: 1774840548800-->
END

START
Coding Questions
In a `when` on a sealed type, when do you use `is` and when do you compare directly?
Back:
- **`is`** — for `data class` subtypes (they have instances, need type checking)
- **Direct comparison** (no `is`) — for `data object` subtypes (singletons, compared by reference)
```kotlin
when (error) {
    is PaymentError.InsufficientFunds -> ...  // data class — use is
    is PaymentError.CardExpired -> ...        // data class — use is
    PaymentError.UnsupportedCurrency -> ...   // data object — direct
}
```
Tags: kotlin enums sealed
<!--ID: 1774840548811-->
END

START
Coding Questions
When should you use **enum** vs **sealed type**?
Back:
| | **Enum** | **Sealed** |
|---|---|---|
| Each entry | Singleton, same properties | Own class, own data |
| Good for | Statuses, types, fixed sets | Errors, results, events |
| Data per variant | Same shape for all | Different payload each |
Tags: kotlin enums sealed
<!--ID: 1774840548823-->
END

START
Coding Questions
When should you use `sealed interface` vs `sealed class`?
Back:
- **`sealed interface`** (preferred default) — subtypes can extend **other classes** too, more flexible
- **`sealed class`** — only when you need **shared state or behavior** in the parent

```kotlin
sealed interface PaymentError           // preferred — flexible
sealed class PaymentError(val timestamp: Instant)  // only for shared state
```
Tags: kotlin enums sealed
<!--ID: 1774840548847-->
END

START
Coding Questions
What is a `data object` and when do you use it?
Back: A **`data object`** is a **singleton** that auto-generates a readable `toString()`:
- Use when a sealed type variant has **no data** to carry
- Regular `object` prints a memory address; `data object` prints the **class name**
```kotlin
println(PaymentError.UnsupportedCurrency)
// UnsupportedCurrency (not PaymentError$UnsupportedCurrency@3a71f4dd)
```
Tags: kotlin enums sealed
<!--ID: 1774840548859-->
END

START
Coding Questions
What are the differences between `object`, `data object`, and `data class`?
Back:
| | `object` | `data object` | `data class` |
|---|---|---|---|
| **Singleton** | Yes | Yes | No |
| **`toString()`** | Memory address | Class name | Property values |
| **Holds data** | No | No | Yes |
Tags: kotlin enums sealed
<!--ID: 1774840548870-->
END
