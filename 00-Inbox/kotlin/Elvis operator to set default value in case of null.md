
If value is `null`, you can return default value

That's done by using **Elvis operator** - `?:`

```kotlin
fun main() {
    val nullString: String? = null
    println(nullString?.length ?: 0)
    // 0
}
```
