---
aliases: [data class]
created: 2026-03-26
tags: [kotlin, oop]
---

### Regular `class` vs `data class`

A regular `class` is just a container — you define everything yourself.

A `data class` auto-generates `equals()`, `hashCode()`, `toString()`, and `copy()` based on the constructor parameters. It's for classes that just **hold data**.

```kotlin
class User(val name: String, val age: Int)
println(User("Ayub", 25))  // User@3a71f4dd (useless)

data class User(val name: String, val age: Int)
println(User("Ayub", 25))  // User(name=Ayub, age=25) (useful)
```

---

### What gets auto-generated?

| Method | What it does |
|---|---|
| `toString()` | Readable output: `User(name=Ayub, age=25)` |
| `equals()` | Compares by property values, not reference |
| `hashCode()` | Consistent with `equals()` for use in maps/sets |
| `copy()` | Creates a new instance with optionally changed fields |

```kotlin
val user = User("Ayub", 25)
val older = user.copy(age = 26)  // User(name=Ayub, age=26)
```

---

### Python equivalent — `@dataclass`

Same concept, different syntax:

```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
```

Auto-generates `__init__`, `__repr__`, `__eq__` — same idea.

---

Read more:

- [[Kotlin primary constructor is declared in the class header with parentheses]]
- [[Kotlin MOC]]
