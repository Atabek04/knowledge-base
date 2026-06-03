### Well, you can declare var without initialization

```kotlin
// Variable declared without initialization
val d: Int
// Variable initialized
d = 3

// Variable explicitly typed and initialized
val e: String = "hello"

// Variables can be read because they have been initialized
println(d) // 3
println(e) // hello
```

But if you don't initialize a var before it's read, you see an error:

```kotlin
// Variable declared without initialization
val d: Int

// Triggers an error
println(d)
// Variable 'd' must be initialized
```

---

### How is this different from Java?

Java fields get <mark style="background: #FF5582A6;">default values</mark> (`0`, `null`, `false`), so uninitialized access compiles fine but crashes at **runtime**:

```java
class User {
    int age;       // defaults to 0
    String name;   // defaults to null
}

User user = new User();
user.name.length(); // 💥 NullPointerException at runtime
```

Kotlin catches this at **compile time** — your code never runs if a variable might be uninitialized.

Same goal, different timing: Java catches it late, Kotlin catches it early.

---

### Exception: `lateinit`

An escape hatch — you're telling Kotlin: "I promise I'll initialize this later."

```kotlin
lateinit var name: String

// Later...
name = "Ayub"
println(name)  // ✅ Promise kept
```

If you break that promise:

```kotlin
lateinit var name: String
println(name)  // 💥 UninitializedPropertyAccessException
```

---

Read more:

- [[Variable declaration in Kotlin is done by var and val]]
- [[Kotlin MOC]]