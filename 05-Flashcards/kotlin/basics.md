TARGET DECK: Tech-KB::Kotlin::Basics
Tags: kotlin basics
**Chapter:** Basic Types
**Related:** [[Kotlin MOC]]

---

START
Coding Questions
What are the two keywords for **declaring variables** in Kotlin, and what does each one control?
Back:
- `var` — **mutable** variable (can reassign)
- `val` — **immutable** reference (cannot reassign)
- `val` is equivalent to `final` in Java
Tags: kotlin basics
<!--ID: 1774840548063-->
END

START
Coding Questions
What is the difference between **reassigning** a variable and **changing its state** in Kotlin?
Back:
- **Reassigning** — changing what the variable points to (a different object or value)
- **Changing state** — modifying internal data of the object the variable already points to
- `val` only prevents **reassigning**, not changing state
Tags: kotlin basics
<!--ID: 1774840548075-->
END

START
Coding Questions
Why does `val` on a **primitive-like type** (`Int`, `Boolean`) make it fully immutable, but `val` on a **reference type** does not?
Back:
- Primitive-like types: the value **is** the data — no separate heap object to mutate
- Reference types: the variable holds a **memory address** — `val` locks the address but the object at that address can still change
- `val` locks the pointer, not the object
Tags: kotlin basics
<!--ID: 1774840548086-->
END

START
Coding Questions
Why is `val list = mutableListOf(1, 2)` **not** the same as having an immutable list?
Back:
- `val` locks the **reference** — you can't reassign `list` to a different object
- But the list contents can still be modified: `list.add(3)` works fine
- The reference is fixed, but the object behind it is still mutable
Tags: kotlin basics
<!--ID: 1774840548098-->
END

START
Coding Questions
Given this Kotlin code, which lines compile and which don't? Why?
```kotlin
class User(val name: String, var age: Int)
val user = User("Ayub", 25)
user.name = "Ali"
user.age = 26
```
Back:
- `user.name = "Ali"` — **does not compile** — `name` is `val`, can't reassign
- `user.age = 26` — **compiles** — `age` is `var`, reassignment allowed
Tags: kotlin basics
<!--ID: 1774840548110-->
END

START
Coding Questions
In Kotlin, if a class holds another object via `val`, can you modify the nested object's `var` fields? Why?
Back: Yes — `val` only guards **its own level** of reference, not nested objects
- You can't swap the nested object (`val` blocks reassignment)
- But you can reach into it and change its `var` fields
- Each `val` only controls its own level — it doesn't cascade down
Tags: kotlin basics
<!--ID: 1774840548121-->
END

START
Coding Questions
How do you make a nested object **truly immutable** in Kotlin?
Back: Make **every level** in the chain `val`:
```kotlin
class Engine(val horsepower: Int, val fuelType: String)
class Car(val engine: Engine)
```
- `val car` — can't swap the Car
- `val engine` — can't swap the Engine
- `val horsepower` — can't change the value
Tags: kotlin basics
<!--ID: 1774840548133-->
END

START
Coding Questions
What happens if you try to read a variable before initializing it in Kotlin?
Back: Kotlin throws a **compile-time error**: `Variable must be initialized`
- Unlike Java, which gives fields default values (`0`, `null`, `false`) and fails at **runtime**
- Kotlin catches uninitialized access **early** at compile time
Tags: kotlin basics
<!--ID: 1774840548145-->
END

START
Coding Questions
What is `lateinit` in Kotlin and when does it fail?
Back: An escape hatch — you tell Kotlin: "I promise I'll **initialize** this later"
```kotlin
lateinit var name: String
```
- If you use it before initializing → `UninitializedPropertyAccessException` at runtime
- Only works with `var`, not `val`
Tags: kotlin basics
<!--ID: 1774840548156-->
END

START
Coding Questions
How does Kotlin's **single type system** differ from Java's dual type system?
Back:
- Kotlin has **one unified type system** — you always write `Int`, never `Integer`
- No primitives vs wrappers distinction at the language level
- The **compiler decides** under the hood:
  - Non-nullable → compiles to JVM primitive (`int`, `boolean`)
  - Nullable or generic → compiles to wrapper (`Integer`, `Boolean`)
- You get Java's performance without managing two type systems
Tags: kotlin basics
<!--ID: 1774840548168-->
END

START
Coding Questions
What are **top-level functions** in Kotlin, and how do they differ from Java methods?
Back:
- **Top-level functions** are declared directly in a file, no class needed
- In Java, every method must live inside a class
- Kotlin compiler automatically generates a wrapper class from the file name under the hood
```kotlin
// MyFunctions.kt
fun greet(name: String) { }
```
Tags: kotlin basics
<!--ID: 1774840548180-->
END

START
Coding Questions
When should you use **top-level functions** in Kotlin?
Back:
- Utility (static) functions that don't belong to any specific object
- Pure functions without state
- Extension functions
- Helper functions that operate on data
Tags: kotlin basics
<!--ID: 1774840548191-->
END

START
Coding Questions
What is a **single-expression function** in Kotlin and how do you write one?
Back: A function with only one expression — use `=` instead of block body `{}`:
```kotlin
// Block body
fun double(x: Int): Int {
    return x * 2
}

// Expression body
fun double(x: Int): Int = x * 2

// Return type can be inferred
fun double(x: Int) = x * 2
```
Tags: kotlin basics
<!--ID: 1774840548203-->
END

START
Coding Questions
How do you use a **single-expression function** with `when` in Kotlin?
Back:
```kotlin
fun describe(x: Int) = when {
    x > 0 -> "positive"
    x < 0 -> "negative"
    else -> "zero"
}
```
- The `when` expression is the single expression, so `=` works directly
Tags: kotlin basics
<!--ID: 1774840548214-->
END

START
Coding Questions
How do **string templates** work in Kotlin?
Back: Use `$` prefix for template expressions — Kotlin auto-calls `.toString()`:
- **Variable**: `"i = $i"`
- **Expression**: `"length is ${s.length}"`
```kotlin
val s = "abc"
println("$s.length is ${s.length}")
// abc.length is 3
```
Tags: kotlin basics
<!--ID: 1774840548226-->
END

START
Coding Questions
What is the **format specifier** for integers in Kotlin, and how do you add a thousands separator?
Back:
- `%d` — integer format specifier
- `%,d` — integer with thousands separator
```kotlin
"%d".format(1234)    // 1234
"%,d".format(1234)   // 1,234
```
- `%d` is for integers only — **not** for doubles
Tags: kotlin basics
<!--ID: 1774840548238-->
END

START
Coding Questions
What is the **format specifier** for doubles in Kotlin, and how do you control decimal places?
Back:
- `%f` — floating point, default 6 decimals
- `%.2f` — floating point, 2 decimal places
- `%,.2f` — thousands separator + 2 decimals
```kotlin
"%f".format(3.14)       // 3.140000
"%.2f".format(3.14)     // 3.14
"%,.2f".format(1234.5)  // 1,234.50
```
Tags: kotlin basics
<!--ID: 1774840548249-->
END

START
Coding Questions
What is an **extension function** in Kotlin and how does it differ from a Java utility method?
Back: An **extension function** adds a method to an existing type without modifying or inheriting from it:
```kotlin
fun String.toReportType(): ReportType =
    ReportType.valueOf(this.uppercase())

"overdue_report".toReportType()
```
- `String.` is the **receiver type**, `this` refers to the instance
- Under the hood compiles to a static method (same as Java util) — but the call site reads naturally
- Replaces `*Utils` classes with discoverable, autocomplete-friendly calls
Tags: kotlin basics
<!--ID: 1780311506400-->
END

START
Coding Questions
What are the key constraints of Kotlin extension functions?
Back:
- Can only access **public** members of the receiver — no private field access
- Resolved **statically** — compile-time type determines which extension is called, no polymorphism
- Should be scoped `private` or `internal` when only relevant in one file/module
Tags: kotlin basics
<!--ID: 1780311506421-->
END

START
Coding Questions
When should you use extension functions in Kotlin, and when should you avoid them?
Back:
**Use for:**
- Type conversions: `entity.toDomain()`, `"value".toReportType()`
- Domain-specific operations on standard types: `LocalDateTime.toDisplayFormat()`
- Replacing `*Utils` static methods

**Avoid when:**
- Logic is complex (20+ lines) — use a service method instead
- It substitutes proper class design
Tags: kotlin basics
<!--ID: 1780311506441-->
END

START
Coding Questions
Why does `@NotBlank` on a Kotlin data class property fail to validate by default?
Back: A Kotlin data class property is simultaneously a **constructor parameter**, a **backing field**, and a **getter**. The default annotation target is **parameter**.
- Jakarta Validation inspects **fields** (or getters), not constructor parameters
- So `@NotBlank val name: String` places the annotation on the parameter — validation is silently skipped
Tags: kotlin basics
<!--ID: 1780311506462-->
END

START
Coding Questions
How do you fix Jakarta Validation annotations on Kotlin data class properties?
Back: Use the `@field:` **use-site target** to place the annotation on the backing field:
```kotlin
data class GenerateReportRequest(
    @field:NotBlank(message = "reportName is required")
    val reportName: String,
)
```
- Without `@field:`, the annotation targets the constructor parameter and validation does nothing
Tags: kotlin basics
<!--ID: 1780311506482-->
END

START
Coding Questions
What are the available annotation use-site targets in Kotlin?
Back:
| Target | Where it goes |
|---|---|
| `@param:` | Constructor parameter **(default)** |
| `@field:` | Backing field |
| `@get:` | Getter method |
| `@set:` | Setter method |
| `@property:` | Kotlin property (not visible to Java) |
Tags: kotlin basics
<!--ID: 1780311506503-->
END

START
Coding Questions
Why does Kotlin default annotation target to `@param:` instead of `@field:`?
Back: The primary constructor is the **source** declaration — field and getter are derived from it. So the compiler targets the most direct element.
- Frameworks like **Jackson** deserialize by **calling the constructor** — they need `@param:`
- If Kotlin defaulted to `@field:`, `@JsonProperty("user_name")` would be invisible to Jackson
- Field-based frameworks (Jakarta Validation, JPA) need explicit `@field:` instead
Tags: kotlin basics
<!--ID: 1780311506523-->
END

START
Coding Questions
What are the three parts needed to create a custom validation annotation in Kotlin?
Back:
1. **Annotation class** — declares the contract with `@Constraint(validatedBy = [...])`
2. **Validator class** — implements `ConstraintValidator<AnnotationType, ValidatedType>` with `isValid()` logic
3. **Application** — place the annotation on the target class or field
- The annotation must declare `message`, `groups`, and `payload` — required by Jakarta spec
Tags: kotlin basics
<!--ID: 1780311506543-->
END

START
Coding Questions
Why should a custom `ConstraintValidator` return `true` when the value is `null`?
Back: To **separate concerns** — let `@NotNull` handle nullability independently.
- If the validator rejects `null`, you can't have an optional field that's valid when absent but validated when present
- Convention: custom validators assume non-null, null-checking is a separate annotation's job
Tags: kotlin basics
<!--ID: 1780311506564-->
END

START
Coding Questions
Why is `@field:Valid` required on a parent field to trigger validation of a nested object?
Back: Jakarta Validation only validates the **top-level object** by default. `@Valid` tells it to **cascade** into nested objects.
- In Kotlin, must use `@field:Valid` because the default target is parameter, not field
- Without it, custom annotations on the nested class (like `@ValidDateRange`) never fire
Tags: kotlin basics
<!--ID: 1780311506585-->
END

START
Coding Questions
When should you use `@Target(AnnotationTarget.CLASS)` vs `@Target(FIELD)` for a custom validation annotation?
Back:
- **`CLASS`** — when the rule spans **multiple fields** (e.g. "from-date before to-date")
- **`FIELD`** — when the rule validates a **single value** (e.g. custom format check)
- Class-level targets validate the whole object, so the validator receives all fields at once
Tags: kotlin basics
<!--ID: 1780311506606-->
END

START
Coding Questions
What are **default parameters** in Kotlin and what problem do they solve?
Back: **Default parameters** let you assign a fallback value to a function parameter — callers can omit it entirely.
```kotlin
fun printMessage(message: String, prefix: String = "Info") {
    println("[$prefix] $message")
}
printMessage("Hello")          // [Info] Hello
printMessage("Hello", "Log")  // [Log] Hello
```
- Eliminates the need for multiple overloads
- In Java you'd write two separate methods; Kotlin covers both with one function
Tags: kotlin basics
<!--ID: 1780311506626-->
END

START
Coding Questions
How do you write a function call using **named arguments** in Kotlin, and why would you use them?
Back: **Named arguments** let you pass parameters by name instead of position:
```kotlin
printMessage(prefix = "Log", message = "Hello")
```
- Order doesn't matter when names are used
- Improves readability — no need to check the function signature to know what each value means
- Especially helpful for `Boolean` and `String` params where position is ambiguous
- Combine with default params: skip optional args, name only the ones you pass
Tags: kotlin basics
<!--ID: 1780311506647-->
END

START
Coding Questions
How do you iterate over a **number range** in Kotlin?
Back: Use the `..` operator to create a closed range and `in` to iterate:
```kotlin
for (number in 1..5) {
    print(number)
}
// 12345
```
- `1..5` is a **closed range** — both endpoints inclusive
- Works with any `Comparable` type
Tags: kotlin basics
<!--ID: 1780311506668-->
END

START
Coding Questions
How do you iterate over a **collection** with a `for` loop in Kotlin?
Back:
```kotlin
val cakes = listOf("carrot", "cheese", "chocolate")

for (cake in cakes) {
    println("Yummy, it's a $cake cake!")
}
```
- `in` works with any `Iterable`
- No index by default — use `withIndex()` if you need both index and value
Tags: kotlin basics
<!--ID: 1780311506689-->
END

START
Coding Questions
Why doesn't Kotlin have a ternary operator, and what do you use instead?
Back: Kotlin has no `? :` ternary. Instead, `if` is an **expression** — it returns a value directly:
```kotlin
val max = if (a > b) a else b
```
- `else` is **required** when `if` is used as an expression
- Both branches must return a compatible type
- Java equivalent: `int max = a > b ? a : b;`
Tags: kotlin basics
<!--ID: 1780311506709-->
END

START
Coding Questions
What is `typealias` in Kotlin, and what does it NOT do?
Back:
- `typealias` gives an **existing type a new name** — no new class is created
- The alias and the original type are **fully interchangeable** at compile time
- Most common use: naming function types for readability:
```kotlin
typealias PaymentStrategy = (Order) -> Unit
```
- **NOT** a new type — you cannot overload on `Foo` vs its alias `Bar`
- **NOT** a value class — use `@JvmInline value class` for actual type safety
Tags: kotlin basics
<!--ID: 1782128730080-->
END

START
Coding Questions
What does it mean for functions to be "first-class" in Kotlin? Show an example.
Back:
- Functions are **values** — store, pass, and return them like any other type
- Function type syntax: `(ParamType) -> ReturnType`
```kotlin
val greet: (String) -> String = { name -> "Hi, $name" }

fun run(fn: (String) -> String) = fn("Atabek")

run(greet)  // "Hi, Atabek"
```
- A function that accepts/returns another function = **higher-order function**
Tags: kotlin basics
<!--ID: 1782128730082-->
END

START
Coding Questions
How do Java, Python, and Kotlin differ in support for first-class functions?
Back:
- **Kotlin** — native first-class functions; function type `(A) -> B`; `typealias` names them
- **Python** — functions are objects; pass directly; `lambda` for inline anonymous fns
- **Java** — no true first-class fns; uses `@FunctionalInterface` + lambdas as syntactic sugar for anonymous class instances; common types: `Function<A,B>`, `Runnable`, `Consumer<T>`
Tags: kotlin basics
<!--ID: 1782128730085-->
END
