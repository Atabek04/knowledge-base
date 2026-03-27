---
aliases: [val guards one level]
created: 2026-03-26
tags: [kotlin, immutability]
---
### `val` on class fields prevents reassignment

A `val` field in a class follows the same rule — you can't reassign it, but if it holds a reference type, the object behind it can still be mutated.

```kotlin
class User(val name: String, var age: Int)

val user = User("Ayub", 25)
user.name = "Ali"  // ❌ name is val — can't reassign
user.age = 26      // ✅ age is var — can reassign
```

---

### Composition — `val` holding another object

When a class holds another object via `val`, you can't swap the object, but you can reach *into* it and change its `var` fields.

```kotlin
class Engine(var horsepower: Int)
class Car(val engine: Engine)

val car = Car(Engine(150))

car.engine.horsepower = 200  // ✅ Changing Engine's internal state
car.engine = Engine(300)     // ❌ Reassigning engine — blocked by val
```

The `val` on `engine` says: "this Car always points to **that specific** Engine instance." What happens *inside* that Engine is not `val`'s business.

---

### Making nested objects truly immutable

The only way to prevent internal mutation is to make the nested object's fields `val` too:

```kotlin
class Engine(val horsepower: Int, val fuelType: String)
class Car(val engine: Engine)

val car = Car(Engine(150, "Petrol"))
car.engine.horsepower = 200  // ❌ Now also blocked
```

---

### Key insight

> <mark style="background: #FFF3A3A6;">Each `val` only controls its own level. It doesn't cascade down.</mark>

- `val car` — can't swap the Car
- `val engine` inside Car — can't swap the Engine
- `var horsepower` inside Engine — *can* change the value

<mark style="background: #ADCCFFA6;">To make something fully immutable, every level in the chain must be `val`.</mark>

---

Read more:

- [[Variable declaration in Kotlin is done by var and val]]
- [[Kotlin is single type system, no wrappers]]
- [[Kotlin MOC]]
