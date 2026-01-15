
Safe calls prevent `NullPointerException`

If the object is null, the entire expression returns null.
If object exists, proceeds with the call.

```kotlin
val length = name?.length
```

Chain doesn't execute if any part is null.

```
user?.address?.city?.name
```

---
### Accept the risk `!!`

```kotlin
val length = name!!.length  // throws NPE if null
```

Explicitly accept the risk. 
Use only when absolutely certain value exists.