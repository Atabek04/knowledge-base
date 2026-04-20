TARGET DECK: Tech-KB::Kotlin::Classes
Tags: kotlin classes
**Chapter:** Classes
**Related:** [[Kotlin MOC]]

---

START
Coding Questions
What is the **primary constructor** in Kotlin and where is it declared?
Back: The **primary constructor** is declared in the class header with `()` — it defines constructor parameters right in the class signature:
- `class User(val name: String, val age: Int)`
- If properties are declared with `val`/`var` in the constructor, Kotlin auto-generates fields and assignments
- Equivalent to writing a full `constructor()` block with manual field assignments inside `{}`
Tags: kotlin classes
<!--ID: 1774840548540-->
END

START
Coding Questions
When do you need `{}` (class body) on a Kotlin class, and when can you skip it?
Back: **Skip `{}`** when the class only holds data and has no methods:
- `data class User(val name: String, val age: Int)`

**Add `{}`** when you need methods or extra properties:
```kotlin
class Car(val brand: String) {
    fun drive() = println("Driving $brand")
}
```
Tags: kotlin classes
<!--ID: 1774840548554-->
END

START
Coding Questions
What does a `data class` auto-generate compared to a regular `class` in Kotlin?
Back: A **data class** auto-generates these methods based on constructor parameters:
- `toString()` → readable output: `User(name=Ayub, age=25)` instead of `User@3a71f4dd`
- `equals()` → compares by **property values**, not reference
- `hashCode()` → consistent with `equals()` for use in maps/sets
- `copy()` → creates a new instance with optionally changed fields
Tags: kotlin classes
<!--ID: 1774840548568-->
END

START
Coding Questions
How does `copy()` work on a Kotlin data class?
Back: **Copying** creates a new instance with optionally overridden fields — unchanged fields keep their original values:
```kotlin
val user = User("Ayub", 25)
val older = user.copy(age = 26)  // User(name=Ayub, age=26)
```
Tags: kotlin classes
<!--ID: 1774840548581-->
END

START
Coding Questions
What is the Python equivalent of Kotlin's `data class`?
Back: Python's `@dataclass` decorator — same concept, different syntax:
```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
```
Auto-generates `__init__`, `__repr__`, `__eq__` — same idea as Kotlin's `toString()`, `equals()`, etc.
Tags: kotlin classes
<!--ID: 1774840548594-->
END

START
Coding Questions
What is the difference between `class` and `object` in Kotlin?
Back:
- `class` is a **blueprint** — you create multiple instances from it: `val u1 = User("A")`, `val u2 = User("B")`
- `object` is a **single instance that already exists** — no constructor, no `new`, only one ever created:
```kotlin
object Logger {
    fun log(msg: String) = println(msg)
}
Logger.log("Hello")  // use directly
```
Tags: kotlin classes
<!--ID: 1774840548607-->
END

START
Coding Questions
When should you use an `object` declaration in Kotlin?
Back: Use **object** when you need **exactly one instance** — utilities, config, registries:
```kotlin
object DatabaseConfig {
    val url = "jdbc:postgresql://localhost:5432/mydb"
    val maxConnections = 10
}
```
In Java you'd write a class with a private constructor and `static getInstance()`. Kotlin does it in one keyword.
Tags: kotlin classes
<!--ID: 1774840548619-->
END

START
Coding Questions
What is the difference between `object` and `data object` in Kotlin?
Back:
- `object Foo` → `toString()` returns `Foo@3a71f4dd` (memory address)
- `data object Foo` → `toString()` returns `Foo` (clean name)

A **data object** is just an `object` with a readable `toString()`. Useful inside sealed types for variants that carry no data.
Tags: kotlin classes
<!--ID: 1774840548632-->
END

START
Coding Questions
Why does Kotlin have `companion object` instead of the `static` keyword?
Back: Kotlin has **no `static` keyword**. Instead, a `companion object` is a singleton tied to the class — its members are accessed through the class name directly:
```kotlin
class User(val name: String) {
    companion object {
        const val MAX_AGE = 150
        fun fromEmail(email: String) = User(email.substringBefore("@"))
    }
}
User.MAX_AGE            // 150
User.fromEmail("a@b.com")
```
Tags: kotlin classes
<!--ID: 1774840548644-->
END

START
Coding Questions
What is a common use case for `companion object` in Kotlin?
Back: **Factory methods** — instead of multiple constructors, use companion object for readable creation:
```kotlin
class Color(val r: Int, val g: Int, val b: Int) {
    companion object {
        fun red() = Color(255, 0, 0)
        fun fromHex(hex: String): Color { /* parse */ }
    }
}
val red = Color.red()
val custom = Color.fromHex("#FF5582")
```
Tags: kotlin classes
<!--ID: 1774840548656-->
END

START
Coding Questions
How is a `companion object` related to `object` declarations in Kotlin?
Back: A **companion object** is just an **object declaration nested inside a class**. The difference: you access its members through the **class name** directly, without naming the object.
Tags: kotlin classes
<!--ID: 1774840548669-->
END

START
Coding Questions
How do Kotlin nested classes differ from Java inner classes by default?
Back:
| | Java | Kotlin |
|---|---|---|
| No outer reference | `static class` | `class` (default) |
| Has outer reference | `class` (default) | `inner class` |

Kotlin **flips Java's default** — nested classes are **static by default** (no hidden reference to the outer instance). You must explicitly add `inner` to get the outer reference.
Tags: kotlin classes
<!--ID: 1774840548680-->
END

START
Coding Questions
Why is Java's default for inner classes considered dangerous?
Back: In Java, inner classes **hold a hidden `this$0` reference** to the outer instance by default — causing **memory leak risk** if you forget to add `static`. The dangerous option (holding outer reference) is Java's default, so you must remember `static` every time.

Kotlin fixes this by making the safe choice (no outer reference) the default.
Tags: kotlin classes
<!--ID: 1774840548692-->
END

START
Coding Questions
How do you create a nested class vs an inner class in Kotlin, and how do you instantiate each?
Back:
- **Nested** (default) — no outer reference, created independently:
```kotlin
class Report(val id: String) {
    class Metadata(val author: String, val version: Int)
}
val meta = Report.Metadata("Ayub", 1)
```
- **Inner** — holds reference to outer, needs an outer instance:
```kotlin
class Report(val id: String) {
    inner class Page(val number: Int) {
        fun header() = "Report $id — Page $number"
    }
}
val page = Report("R-001").Page(1)
```
Tags: kotlin classes
<!--ID: 1774840548704-->
END

START
Coding Questions
When should you use `inner class` vs a nested class (default) in Kotlin?
Back: Use **nested** (default) for logical grouping — the nested class doesn't need the outer instance's state.

Use **`inner`** only when the nested class genuinely needs access to the outer instance's properties/methods. In practice, `inner` is rare.
Tags: kotlin classes
<!--ID: 1774840548715-->
END

START
Coding Questions
What is the difference between a constructor parameter **with** `val`/`var` and **without** in Kotlin?
Back:
- **With `val`/`var`** → becomes a **class property** — stored, accessible from outside, getter generated:
```kotlin
class Contact(val id: Int, var email: String)
// contact.id and contact.email work anywhere
```
- **Without `val`/`var`** → **init-only parameter** — only available during initialization, not stored as a field:
```kotlin
class Contact(id: Int, email: String)
// id and email not accessible after construction
```
Use plain params when the value is only needed to initialize other properties and should not be exposed.
Tags: kotlin classes
END
