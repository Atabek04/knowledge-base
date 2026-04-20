---
aliases: [constructor parameter vs property, val var in constructor]
---

A constructor parameter declared with `val` or `var` becomes a **class property** — accessible anywhere in the class with a generated getter (and setter for `var`).

```kotlin
class Contact(val id: Int, var email: String)
// contact.id and contact.email are accessible
```

Without `val` or `var`, the parameter only exists **during initialization**:

```kotlin
class Contact(id: Int, email: String) {
    // id and email only available here, not as contact.id
}
```

Use plain parameters when you only need the value to set up other properties and don't want to expose it as a field.

---

### Read more
- [[Kotlin primary constructor is declared in the class header with parentheses]]
- [[Kotlin data class auto-generates common methods for data holders]]
- [[Kotlin MOC]]
