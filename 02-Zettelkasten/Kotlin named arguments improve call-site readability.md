---
aliases: [named arguments, named args]
---

Named arguments let you pass function parameters by name instead of position.

```kotlin
fun printMessage(message: String, prefix: String) {
    println("[$prefix] $message")
}

printMessage(prefix = "Log", message = "Hello")
// [Log] Hello
```

Benefits:
- Order doesn't matter when names are used
- Improves readability — no need to check the function signature
- Especially helpful for booleans and strings where position is hard to remember

Combine with default parameters: skip optional args and name only the ones you pass.

---

### Read more
- [[Kotlin default parameters reduce function overloads]]
- [[Kotlin MOC]]
