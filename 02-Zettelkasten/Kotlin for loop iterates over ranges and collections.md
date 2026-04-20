---
aliases: [for loop, Kotlin range, range iteration]
---

Kotlin `for` loop uses the `in` keyword to iterate over a range or collection.

### Iterating a range

```kotlin
for (number in 1..5) {
    print(number)
}
// 12345
```

`1..5` creates a closed range — both endpoints inclusive.

---

### Iterating a collection

```kotlin
val cakes = listOf("carrot", "cheese", "chocolate")

for (cake in cakes) {
    println("Yummy, it's a $cake cake!")
}
```

Same syntax for both — `in` works with any `Iterable`.
No index by default. Use `withIndex()` if you need both index and value.

---

### Read more
- [[To check that an item is in a list, use in operator]]
- [[Kotlin when expression replaces switch with more power and flexibility]]
- [[Kotlin MOC]]
