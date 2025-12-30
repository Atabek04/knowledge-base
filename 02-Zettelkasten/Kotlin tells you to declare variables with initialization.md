Parent: [[Kotlin MOC]]

---

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

Exception: lateinit
learn about that and link that note to this one

```kotlin
lateinit var name: String  // Allowed
// use later: name = "Ayub"
```