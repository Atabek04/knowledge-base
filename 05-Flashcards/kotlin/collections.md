TARGET DECK: Tech-KB::Kotlin::Collections
Tags: kotlin collections
**Chapter:** Scope Functions & Collections
**Related:** [[Kotlin MOC]]

---

START
Coding Questions
What are Kotlin's five **scope functions**, and how do they differ?
Back: All five **scope functions** execute a block of code on an object. They differ by **object reference** and **return value**:
- `let` — ref: `it`, returns: **lambda result**
- `apply` — ref: `this`, returns: **the object**
- `also` — ref: `it`, returns: **the object**
- `run` — ref: `this`, returns: **lambda result**
- `with(obj)` — ref: `this`, returns: **lambda result**
Tags: kotlin collections
<!--ID: 1774840548261-->
END

START
Coding Questions
When should you use `let` vs `apply` vs `also`?
Back:
- **`let`** — null checks and transformations (`name?.let { it.trim() }`)
- **`apply`** — object configuration (`Server().apply { port = 8080 }`)
- **`also`** — side effects like logging (`result.also { log.info(it) }`)
Tags: kotlin collections
<!--ID: 1774840548273-->
END

START
Coding Questions
When should you use `run` vs `with(obj)`?
Back: Both are used for **scoped computation** using `this` and returning the **lambda result**. The only difference is syntax:
- `obj.run { ... }` — called on the object
- `with(obj) { ... }` — object passed as argument
Tags: kotlin collections
<!--ID: 1774840548284-->
END

START
Coding Questions
What is the key rule about nesting scope functions in Kotlin?
Back: <mark style="background: #FF5582A6;">Don't nest scope functions.</mark>
- Nesting makes code unreadable
- Keep to **one level deep**, max
Tags: kotlin collections
<!--ID: 1774840548296-->
END

START
Coding Questions
What does Kotlin `let` do, and what does it return?
Back: **`let`** calls a block of code on an object, referencing it as `it`, and returns the **last expression** (lambda result):
```kotlin
val length = "Hello".let {
    println(it)    // prints: Hello
    it.length      // return value
}
// length = 5
```
Tags: kotlin collections
<!--ID: 1774840548307-->
END

START
Coding Questions
How do you use `?.let` for null-safe execution in Kotlin?
Back: Combine the **safe call operator** `?.` with `let` to execute code **only if not null**:
```kotlin
name?.let {
    println("Name is $it, length is ${it.length}")
}
```
- If `name` is null, the entire block is **skipped**
Tags: kotlin collections
<!--ID: 1774840548319-->
END

START
Coding Questions
How can `let` be used for **scoping** (limiting variable lifetime)?
Back: Use `let` to confine a temporary value to a block:
```kotlin
val result = fetchData().let { raw ->
    raw.trim().uppercase()
}
// `raw` is not accessible here
```
Without `let`, you'd need a separate variable **polluting the outer scope**.
Tags: kotlin collections
<!--ID: 1774840548331-->
END

START
Coding Questions
How do you chain `let` calls for transformations in Kotlin?
Back: **Chaining** `let` applies sequential transformations:
```kotlin
val formatted = "  hello world  "
    .let { it.trim() }
    .let { it.capitalize() }
// "Hello world"
```
Tags: kotlin collections
<!--ID: 1774840548343-->
END

START
Coding Questions
What are Kotlin's 3 main **collection** types?
Back:
1. **List** — ordered, allows duplicates
2. **Set** — unordered, unique items only
3. **Map** — key-value pairs, allows duplicate values
Tags: kotlin collections
<!--ID: 1774840548355-->
END

START
Coding Questions
How do you create a read-only list vs a mutable list in Kotlin?
Back:
- **Read-only**: `listOf("a", "b", "c")` — returns `List`
- **Mutable**: `mutableListOf("a", "b", "c")` — returns `MutableList`
Tags: kotlin collections
<!--ID: 1774840548366-->
END

START
Coding Questions
How do you create a read-only set vs a mutable set in Kotlin?
Back:
- **Read-only**: `setOf("apple", "banana")` — returns `Set`
- **Mutable**: `mutableSetOf("apple", "banana")` — returns `MutableSet`
- Duplicate items are **ignored** in sets
Tags: kotlin collections
<!--ID: 1774840548378-->
END

START
Coding Questions
How do you create a read-only map vs a mutable map in Kotlin?
Back:
- **Read-only**: `mapOf("apple" to 100, "kiwi" to 190)` — returns `Map`
- **Mutable**: `mutableMapOf("apple" to 100, "kiwi" to 190)` — returns `MutableMap`
- Use the `to` keyword to create key-value pairs
Tags: kotlin collections
<!--ID: 1774840548389-->
END

START
Coding Questions
How do you cast a mutable list to read-only to prevent unwanted modifications?
Back: Assign the `MutableList` to a `List` variable:
```kotlin
val shapes: MutableList<String> = mutableListOf("triangle", "square")
val shapesLocked: List<String> = shapes
```
`shapesLocked` has no mutating methods exposed.
Tags: kotlin collections
<!--ID: 1774840548401-->
END

START
Coding Questions
How do you check if an item exists in a Kotlin list?
Back: Use the **`in` operator**:
```kotlin
val shapes = listOf("triangle", "square", "circle")
println("circle" in shapes)  // true
```
Tags: kotlin collections
<!--ID: 1774840548412-->
END

START
Coding Questions
How do you obtain a map's keys and values in Kotlin?
Back: Use the `.keys` and `.values` properties:
```kotlin
val menu = mapOf("apple" to 100, "kiwi" to 190)
println(menu.keys)    // [apple, kiwi]
println(menu.values)  // [100, 190]
```
Tags: kotlin collections
<!--ID: 1774840548423-->
END

START
Coding Questions
How does `filter {}` work on Kotlin collections?
Back: **`filter`** keeps items that match the given condition:
```kotlin
val nums = listOf(1, 2, 3, 4, 5)
nums.filter { it > 3 }  // [4, 5]
```
Tags: kotlin collections
<!--ID: 1774840548435-->
END

START
Coding Questions
How does `map {}` work on Kotlin collections?
Back: **`map`** transforms each item in the collection:
```kotlin
val names = listOf("ayub", "ali")
names.map { it.uppercase() }  // [AYUB, ALI]
```
Tags: kotlin collections
<!--ID: 1774840548448-->
END

START
Coding Questions
What does `flatMap {}` do, and how does it differ from `map {}`?
Back: **`flatMap`** transforms each item into a list, then **flattens** them into a single list:
```kotlin
val users = listOf(User("Ayub", listOf("A", "B")), User("Ali", listOf("C")))
users.flatMap { it.tags }  // [A, B, C]
```
- `map` would give `[[A, B], [C]]` — a list of lists
- `flatMap` **unwraps** them into one flat list
Tags: kotlin collections
<!--ID: 1774840548461-->
END

START
Coding Questions
How does `associate {}` work on Kotlin collections?
Back: **`associate`** converts a list into a map:
```kotlin
val users = listOf(User(1, "Ayub"), User(2, "Ali"))
users.associate { it.id to it.name }  // {1=Ayub, 2=Ali}
```
Tags: kotlin collections
<!--ID: 1774840548473-->
END

START
Coding Questions
How does `groupBy {}` work on Kotlin collections?
Back: **`groupBy`** converts a list into a **map of lists**, grouped by a key:
```kotlin
val words = listOf("apple", "ant", "banana", "bat")
words.groupBy { it.first() }
// {a=[apple, ant], b=[banana, bat]}
```
Tags: kotlin collections
<!--ID: 1774840548485-->
END

START
Coding Questions
What do `any {}`, `none {}`, and `all {}` do on Kotlin collections?
Back: Boolean checks across a collection:
- **`any`** — `true` if **at least one** item matches
- **`none`** — `true` if **no item** matches
- **`all`** — `true` if **every item** matches
```kotlin
val nums = listOf(1, 2, 3, 4)
nums.any { it > 3 }   // true
nums.none { it > 5 }  // true
nums.all { it > 0 }   // true
```
Tags: kotlin collections
<!--ID: 1774840548498-->
END

START
Coding Questions
What is the difference between `first {}` and `firstOrNull {}` in Kotlin?
Back:
- **`first { }`** — returns the first matching item, throws **`NoSuchElementException`** if none found
- **`firstOrNull { }`** — returns the first matching item, returns **`null`** if none found (safe)
```kotlin
nums.first { it > 10 }       // 💥 NoSuchElementException
nums.firstOrNull { it > 10 } // null
```
Use **`firstOrNull`** when you're not sure a match exists.
Tags: kotlin collections
<!--ID: 1774840548511-->
END

START
Coding Questions
How do you chain collection transformations in Kotlin?
Back: **Chaining** works because each transformation returns a new collection:
```kotlin
val ayubTotal = orders
    .filter { it.customer == "Ayub" }
    .filter { it.paid }
    .map { it.amount }
    .sum()  // 300.0
```
Tags: kotlin collections
<!--ID: 1774840548524-->
END

START
Coding Questions
What is the difference between `List` and `MutableList` in Kotlin?
Back: Kotlin splits collections into **read-only** and **mutable** type hierarchies:
- **`List`** — declares only read ops (`get`, `size`, `contains`); **no** `add`/`remove`/`set`
- **`MutableList`** — extends `List`, adding the mutators `add`, `remove`, `set`
```kotlin
val items: List<String> = listOf("a")
items.add("b") // ❌ compile error — List has no add()
```
Read-only is a **narrower type**, not a defensive copy — it costs nothing.
Tags: kotlin collections
<!--ID: 1782128730087-->
END

START
Coding Questions
Why does Kotlin's read-only `List` catch a mutation bug that Java's record accessor lets through?
Back: It's a **type-level** guard caught at compile time:
- **Java** — `java.util.List` interface declares `add()`, so a record accessor's return type still carries mutators. `acc.transactions().add("X")` compiles, fails only at runtime (if immutable)
- **Kotlin** — `List` omits `add()` entirely, so `acc.transactions.add("X")` **won't compile**
Tags: kotlin collections
<!--ID: 1782128730090-->
END

START
Coding Questions
Is a Kotlin `List` immutable?
Back: **No — read-only is not immutable.** `List` is a read-only **view**; the underlying object can still be a `MutableList` held elsewhere:
```kotlin
val mutable = mutableListOf("a")
val readOnly: List<String> = mutable
mutable.add("b")  // ✅ changes show through
println(readOnly) // [a, b]
```
A `List` reference promises only that **you** can't mutate through it. For true immutability, copy or use `kotlinx.collections.immutable`.
Tags: kotlin collections
<!--ID: 1782128730092-->
END

START
Coding Questions
A Kotlin `List` reference still changed when the original `MutableList` was appended. Why, and how do you prevent it?
Back: **Why** — `val readOnly: List<String> = mutable` copies nothing; both names point to the **same object**. The `List` type only hides `add()` from that name.
**Prevent** — copy, don't alias:
```kotlin
val readOnly = mutable.toList()  // independent snapshot
mutable.add("b")
println(readOnly)  // [a] — unaffected
```
For a never-mutable type use `kotlinx.collections.immutable` (`toImmutableList()`).
Tags: kotlin collections
<!--ID: 1782128730095-->
END
