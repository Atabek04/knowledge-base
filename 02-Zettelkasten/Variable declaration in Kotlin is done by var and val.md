Parent: [[Kotlin MOC]]

---

### Two keywords for controlling mutability

`var` - mutable variable (can reassign)
`val` - immutable reference (cannot reassign)

---

`val` ≈ `final` in Java

Once assigned, you cannot reassign the reference.

---
### Reassigning vs Changing State
##### Reassigning
changing what the variable points to.
making the variable reference a different object/value

##### Changing State
modifying internal data of the object
variable still points to the same object

---
### Case with Reference Types

Variables hold a memory address to heap.

Reassigning = change the address
Changing state = modify data at that address

```kotlin
val list = mutableListOf(1, 2)  // list points to address 0x001

list.add(3)  // State change - address 0x001 now contains [1,2,3]
             // list still points to 0x001

list = mutableListOf(4, 5)  // ❌ Reassignment - would point to 0x002
                            // val prevents this
```

---

### Key insight

> <mark style="background: #FFF3A3A6;">Var locks the pointer, not the object</mark>

For primitives: no difference (value = object)
For objects: huge difference (reference ≠ object)