---
aliases: [let, scope function let]
created: 2026-03-27
tags: [kotlin, scope-functions]
---

### What `let` does

Calls a block of code on an object and returns the block's result. Inside the block, the object is accessed as `it`.

```kotlin
val length = "Hello".let {
    println(it)    // prints: Hello
    it.length      // last expression = return value
}
println(length)    // 5
```

---

### Most common use — safe call + `let`

Execute code **only if not null**:

```kotlin
val name: String? = "Ayub"

name?.let {
    println("Name is $it, length is ${it.length}")
}
// prints: Name is Ayub, length is 4

val nullName: String? = null
nullName?.let {
    println("This never runs")
}
```

`?.let` means: "if not null, do this with it." If null, the whole block is skipped.

---

### Scoping — limit variable lifetime

Use `let` to keep a temporary value confined to a block:

```kotlin
val result = fetchData().let { raw ->
    // `raw` only exists inside this block
    raw.trim().uppercase()
}
// raw is not accessible here
```

Without `let`, you'd need a separate variable polluting the outer scope.

---

### Chaining transformations

```kotlin
val formatted = "  hello world  "
    .let { it.trim() }
    .let { it.capitalize() }
// "Hello world"
```

---

Read more:

- [[Safe call operator avoids null crashes by returning null instead]]
- [[Elvis operator provides a default when left side is null]]
- [[Kotlin MOC]]
