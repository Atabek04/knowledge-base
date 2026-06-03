1. Lists - ordered collections of item
2. Sets - unique unordered collections of items
3. Maps - sets of key-value pairs

---
## Lists

Lists store items in the order they are added.
Allow duplicate items.

1. Read-only list :luc_arrow_right_circle: `List`
	use the `listof()` function

2. Mutable list :luc_arrow_right_circle: `MutableList`
	use the `mutableListOf()` function

#### Type infer

Kotlin can infer the type of items stores.

```kotlin
// Read only list
val readOnlyShapes = listOf("triangle", "square", "circle")
println(readOnlyShapes)
// [triangle, square, circle]
```

You can also declare the types explicitly in the `<>`

```kotlin
// Mutable list with explicit type declaration
val shapes: MutableList<String> = mutableListOf("triangle", "square", "circle")
println(shapes)
// [triangle, square, circle]
```

#### Casting to prevent unwanted modifications

```kotlin
val shapes: MutableList<String> = mutableListOf("triangle", "square", "circle") 
val shapesLocked: List<String> = shapes
```

Read more about:
- [[To check that an item is in a list, use in operator]]

---
## Set

Sets store items in an unordered manner.
Doesn't allow duplicate items.

1. Read-only set :luc_arrow_right_circle: `Set`
	use the `setOf()` function

```kotlin
// Read-only set
val readOnlyFruit = setOf("apple", "banana", "cherry", "cherry")
```

2. Mutable set :luc_arrow_right_circle: `MutableSet`
	use the `mutableSetOf()` function

```kotlin
// Mutable set with explicit type declaration
val fruit: MutableSet<String> = mutableSetOf("apple", "banana", "cherry", "cherry")
```

---

## Map

Map stores items as key-value pairs.
You can have duplicate values in a map.

1. Read-only map :luc_arrow_right_circle: `Map`
	uses the `mapOf()` function

```kotlin
// Read-only map
val readOnlyJuiceMenu = mapOf("apple" to 100, "kiwi" to 190, "orange" to 100)

println(readOnlyJuiceMenu)
// {apple=100, kiwi=190, orange=100}
```

2. Mutable map :luc_arrow_right_circle: `MutableMap`
	uses the `mutableMapOf()` function

```kotlin
// Mutable map with explicit type declaration
val juiceMenu: MutableMap<String, Int> = mutableMapOf("apple" to 100, "kiwi" to 190, "orange" to 100)

println(juiceMenu)
// {apple=100, kiwi=190, orange=100}
```

Read more about:
- [[To obtain map's keys and values use these methods]]

---

### Read more

- [[Kotlin MOC]]
- [[To check that an item is in a list, use in operator]]
- [[To obtain map's keys and values use these methods]]
