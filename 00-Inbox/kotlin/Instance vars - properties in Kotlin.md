
### Constructor Parameters

```kotlin
class Contact(val id: Int, var email: String)
```

- Becomes a property accessible throughout the class.
- Automatically creates getter (and setter for var). 
- Part of primary constructor AND class property.
#### Without val/var

```kotlin
class Contact(id: Int, email: String)
```

- Just constructor parameters. 
- **Only accessible during initialization**. 
- Not stored as class properties.

---
### Body Properties

```kotlin
class Contact(val id: Int) {
    val category: String = ""
}
```

- Declared after construction. 
- Must be initialized (or lateinit). 
- Not part of constructor signature.