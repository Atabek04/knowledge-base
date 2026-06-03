---
created: 2026-06-03
tags: [kotlin, immutability, collections]
aliases: [read-only List, List vs MutableList]
---

Kotlin splits its collections into two type hierarchies: **read-only** (`List`, `Set`, `Map`) and **mutable** (`MutableList`, `MutableSet`, `MutableMap`).

The read-only interface deliberately declares no `add`, `remove`, or `set`. A variable typed as `List` simply has no way to mutate the collection — the compiler rejects it.

```kotlin
val items: List<String> = listOf("a", "b")
items.add("c") // ❌ compile error — List has no add()
```

---

### Read-only is a type, not a copy

`List` declares only read operations: `get`, `size`, `contains`, iteration.
`MutableList` **extends** `List`, adding the mutators `add`, `remove`, `set`.

So read-only costs nothing — no defensive copy, no wrapper. It is just the narrower type that hides the write methods.

<mark style="background: #FFF3A3A6;">Choosing `List` over `MutableList` is choosing a type that has no mutators, not making a frozen copy.</mark>

---

### Benefit — the accessor cannot be abused

When a class exposes a collection as `List`, callers receive a reference they **cannot** mutate. The protection lives in the type, caught at compile time.

```kotlin
data class Account(val transactions: List<String>)

val acc = Account(mutableListOf("t1"))
acc.transactions.add("FAKE") // ❌ won't compile — List has no add()
```

Passing `mutableListOf(...)` to a `List` parameter is fine: `MutableList` **is-a** `List` (subtype), so a subtype satisfies a supertype slot. The object stays mutable — but `transactions` is *typed* `List`, a narrower lens that hides the mutators.

Compare Java: a record accessor returns `java.util.List`, whose [[Java List is an interface and its mutability depends on the implementation, not the type|interface declares `add()` no matter the implementation]]. The mutation compiles and runs — it only fails at runtime if the list happens to be immutable. Kotlin removes `add` from the type entirely, so <mark style="background: #ADCCFFA6;">the same leak is caught by the compiler instead of slipping through to runtime.</mark>

---

### Caveat — read-only is not immutable

`List` is a read-only **view**, not a deep-immutability guarantee. The underlying object can still be a `MutableList` held elsewhere, and changes there show through the view.

```kotlin
val mutable = mutableListOf("a")
val readOnly: List<String> = mutable

mutable.add("b")  // ✅ same object — mutated through the original reference
println(readOnly) // [a, b]
```

Why it leaks: `val readOnly: List<String> = mutable` copies **nothing** — both names point to the *same* object. The `List` type only hides `add()` from the `readOnly` name; the `mutable` name still reaches the shared object.

<mark style="background: #FF5582A6;">A `List` reference promises only that *you* can't mutate through it — not that no one can.</mark>

#### Prevent it — copy, don't alias

`toList()` snapshots into a fresh list, breaking the shared reference, so later mutations to the original don't show:

```kotlin
val mutable = mutableListOf("a")
val readOnly = mutable.toList()  // independent copy
mutable.add("b")
println(readOnly)  // [a] — unaffected
```

For a list nobody can ever mutate, use `kotlinx.collections.immutable` (`toImmutableList()`).

Java's [[Java List is an interface and its mutability depends on the implementation, not the type#A read-only view is not immutable — copy to detach|`Collections.unmodifiableList()` carries the identical trap]] — a read-only view over a still-mutable backing list.

---

### Read more

- [[Kotlin has 3 main collections for grouping items]]
- [[Java List is an interface and its mutability depends on the implementation, not the type]]
- [[val in Kotlin guards only its own level of reference not nested objects]]
- [[Java records auto-generate accessor, equals, hashCode, and toString from their components]]
- [[Defensive copying prevents external mutation of internal state]]
