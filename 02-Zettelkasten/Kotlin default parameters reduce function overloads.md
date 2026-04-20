---
aliases: [default parameters, default params]
---

When a function parameter has a default value, callers can omit it entirely.

```kotlin
fun printMessage(message: String, prefix: String = "Info") {
    println("[$prefix] $message")
}

printMessage("Hello")          // [Info] Hello
printMessage("Hello", "Log")  // [Log] Hello
```

Default parameters eliminate the need for multiple overloads.
In Java you'd write two separate methods — in Kotlin, one function covers both.

Use defaults for optional configuration that has a sensible fallback.

---

### Read more
- [[Kotlin named arguments improve call-site readability]]
- [[Kotlin single-expression functions use equals sign instead of block body]]
- [[Kotlin MOC]]
