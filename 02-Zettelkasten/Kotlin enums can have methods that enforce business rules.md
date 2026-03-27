---
aliases: [enum methods, enum business logic]
created: 2026-03-27
tags: [kotlin, oop, enums]
---

### Enums aren't just constants — they can have behavior

#### What is a "transition"?

Think of an online order going through stages:

`CREATED → PAID → SHIPPED → DELIVERED`

Not every jump is allowed. You can't go from `CREATED` to `DELIVERED` — you haven't paid yet. Once `CANCELLED`, you can't go anywhere.

A "transition" is <mark style="background: #FFF3A3A6;">moving from one status to another</mark>. The method checks: "from where I am now, is it legal to go to this next status?"

In Java, this logic lives in a service class. In Kotlin, the enum itself can know which transitions are legal:

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

#### What are `this` and `next`?

```kotlin
OrderStatus.CREATED.canTransitionTo(OrderStatus.PAID)
//          ^^^^^^^ this              ^^^^ next
```

- `this` — the instance you called the method on (same `this` as OOP). Here it's `CREATED`.
- `next` — the function parameter: the status you're **trying to go to**. Here it's `PAID`.

#### `next in setOf(...)` — what does this mean?

`in` checks if an item exists in a set. So:

```kotlin
CREATED -> next in setOf(PAID, CANCELLED)
// reads: "if current is CREATED, is `next` inside {PAID, CANCELLED}?"

// same as writing:
CREATED -> next == PAID || next == CANCELLED
```

Just cleaner.

```kotlin
OrderStatus.CREATED.canTransitionTo(OrderStatus.PAID)       // true
OrderStatus.DELIVERED.canTransitionTo(OrderStatus.SHIPPED)   // false
```

---

### Why `when` on `this` needs no `else`

Normally `when` needs `else` as a catch-all:

```kotlin
when (x) {
    1 -> "one"
    2 -> "two"
    else -> "other"  // needed — x could be anything
}
```

But with enums, the compiler **knows every possible value**. `OrderStatus` can only be CREATED, PAID, SHIPPED, DELIVERED, or CANCELLED — nothing else exists. If you handle all five, there's nothing left for `else` to catch.

<mark style="background: #FFF3A3A6;">That's what "exhaustive" means — every case is covered, the compiler verified it.</mark>

If someone adds a new status later, <mark style="background: #FF5582A6;">it won't compile until they update this function.</mark>

---

Read more:

- [[Kotlin when expression replaces switch with more power and flexibility]]
- [[Kotlin single-expression functions use equals sign instead of block body]]
- [[Kotlin enums provide entries and valueOf for iteration and string conversion]]
- [[Kotlin MOC]]
