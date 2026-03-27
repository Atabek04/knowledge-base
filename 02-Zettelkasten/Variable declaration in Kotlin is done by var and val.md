Parent: [[Kotlin MOC]]

---

### Two keywords for controlling mutability

`var` — mutable variable (can reassign)
`val` — immutable reference (cannot reassign)

`val` ≈ `final` in Java — once assigned, you cannot reassign the reference.

---

### Reassigning vs Changing State

These are two different operations:

**Reassigning** — changing what the variable points to (a different object or value).
**Changing state** — modifying internal data of the object the variable already points to.

`val` only prevents **reassigning**. It says nothing about changing state.

---

### How this plays out depends on the data type

The impact of `val` vs `var` depends on whether the variable holds a <mark style="background: #FFF3A3A6;">primitive-like type</mark> or a <mark style="background: #FFF3A3A6;">reference type</mark>.

#### Primitive-like types (`Int`, `Boolean`, `Double`, etc.)

The value **is** the data — there's no separate address and object.
`val x = 5` means `x` *is* 5. There's no heap object to mutate internally.

So `val` on a primitive-like type = **fully immutable**. There's no state to change.

```kotlin
val x = 5
x = 10  // ❌ Can't reassign
// No .mutate() or internal state to change either — it's just 5
```

#### Reference types (`List`, `MutableList`, custom objects, etc.)

Variables hold a <mark style="background: #BBFABBA6;">memory address</mark> pointing to an object on the heap.

- **Reassigning** = change the address (point to a different object)
- **Changing state** = modify data at that address (same object, different contents)

```kotlin
val list = mutableListOf(1, 2)  // list points to address 0x001

list.add(3)  // ✅ State change — 0x001 now contains [1, 2, 3]
             // list still points to 0x001

list = mutableListOf(4, 5)  // ❌ Reassignment — would point to 0x002
                             // val prevents this
```

---

### Key insight

> <mark style="background: #FFF3A3A6;">`val` locks the pointer, not the object</mark>

For primitive-like types: `val` = fully immutable (value *is* the object, nothing to mutate).
For reference types: `val` = reference is locked, but the object behind it can still change.

This is why `val list = mutableListOf(...)` is **not** the same as having an immutable list — the reference is fixed, but the list contents can still be modified.

---

Read more:

- [[Kotlin is single type system, no wrappers]]
- [[Kotlin MOC]]