### Template expression `$`

When the template expression is processed, Kotlin automatically calls the `.toString()` function.

#### use for Variable name

```kotlin
val i = 10
println("i = $i") 
// i = 10

val letters = listOf("a","b","c","d","e")
println("Letters: $letters") 
// Letters: [a, b, c, d, e]
```

#### use for Expressions in curly braces

```kotlin
val s = "abc"
println("$s.length is ${s.length}") 
// abc.length is 3
```

---

### Read more

- [[Kotlin MOC]]

