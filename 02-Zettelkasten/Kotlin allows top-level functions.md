Parent: [[Kotlin MOC]]

---

### Previously in Java

Every method must be declared inside a class
Even a simple `main` requires a class wrapper

> This is a fundamental **JVM requirement**.

```java
// Java equivalent
public final class MyFunctionsKt {
    public static void greet(String name) { }
    public static int calculate(int x) { }
}
```

---
### Kotlin's approach

Kotlin allows top-level functions
These are functions that declared directly in a file
No class declaration needed

> You can write function outside of class, at file level.


```kotlin
// MyFunctions.kt file
fun greet(name: String) { }
fun calculate(x: Int) { }
```

---
### Under the Hood

Kotlin still compiles to JVM bytecode
Kotlin compiler **automatically generates a class** for top-level functions.
The generated class name is bases on the file name

---
### When to use Top-Level Functions

- Utility (*static*) functions that don't belong to any specific object
- Pure functions without state (*instance variables*)
- Extension functions
- Helper functions that operate on data