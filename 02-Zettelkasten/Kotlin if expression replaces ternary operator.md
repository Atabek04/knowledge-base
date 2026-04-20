---
aliases: [Kotlin ternary, if expression, if as expression]
---

Kotlin has no ternary operator (`? :`). Instead, `if` is an **expression** — it returns a value.

```kotlin
val max = if (a > b) a else b
```

Java equivalent:
```java
int max = a > b ? a : b;
```

Because `if` returns a value, `else` is required when used as an expression.
Both branches must produce a value of compatible type.

---

### Read more
- [[Kotlin when expression replaces switch with more power and flexibility]]
- [[Kotlin MOC]]
