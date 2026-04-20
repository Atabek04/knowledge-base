TARGET DECK: Tech-KB::Kotlin::Null Safety
Tags: kotlin null-safety
**Chapter:** Control Flow & Null Safety
**Related:** [[Kotlin MOC]]

---

START
Coding Questions
How do you **declare a nullable type** in Kotlin?
Back:
- Append `?` to the type: `var name: String? = "Ayub"`
- Without `?`, the variable **cannot** hold null — `String` vs `String?`
- `name = null` compiles only if the type is `String?`
Tags: kotlin null-safety
<!--ID: 1774840548883-->
END

START
Coding Questions
What happens if you try to assign `null` to a non-nullable type in Kotlin?
Back: The compiler throws a **compile error** — non-nullable types like `String` reject null by design
Tags: kotlin null-safety
<!--ID: 1774840548894-->
END

START
Coding Questions
Why does Kotlin prevent you from calling methods directly on a nullable variable?
Back: The variable might be `null` at runtime, so the compiler **enforces safe access** — you must use `?.`, `?:`, or a null check before calling methods on a `Type?`
Tags: kotlin null-safety
<!--ID: 1774840548905-->
END

START
Coding Questions
What does the **safe call operator** `?.` do in Kotlin?
Back:
- **Short-circuits** if the receiver is null — returns `null` immediately without calling the method
- `name?.length` is equivalent to: `if (name != null) name.length else null`
- The method on the right side **never executes** when the left side is null
Tags: kotlin null-safety
<!--ID: 1774840548917-->
END

START
Coding Questions
How does **chaining safe calls** work in Kotlin? Give an example.
Back:
- Chain multiple `?.` calls — if **any** link is null, the entire chain returns `null`
- `val city = user?.address?.city`
- Replaces nested null checks in Java:
```kotlin
// Java equivalent:
if (user != null && user.getAddress() != null) {
    city = user.getAddress().getCity();
}
```
Tags: kotlin null-safety
<!--ID: 1774840548929-->
END

START
Coding Questions
What does the **Elvis operator** `?:` do in Kotlin?
Back:
- **Provides a default** when the left side is null
- `val length = name?.length ?: 0` → if `name` is null, `length` becomes `0`
- Pairs naturally with the safe call `?.`
Tags: kotlin null-safety
<!--ID: 1774840548941-->
END

START
Coding Questions
What can the Elvis operator `?:` do besides providing a default value?
Back:
- **Throw an exception:** `val name = user?.name ?: throw IllegalArgumentException("Name required")`
- **Early return:** `val name = user?.name ?: return`
Tags: kotlin null-safety
<!--ID: 1774840548953-->
END

START
Coding Questions
What does `?.let {}` do with a nullable value in Kotlin?
Back:
- **Executes the block only if the value is not null** — skips entirely if null
- `name?.let { println("Name is $it") }`
- Use when you want to run logic only on non-null values
Tags: kotlin null-safety
<!--ID: 1774840548965-->
END

START
Coding Questions
When should you use `requireNotNull()` in Kotlin?
Back:
- When null means a **bug** — the value should never be null at this point
- Throws `IllegalArgumentException` if the value is null
- `val name = requireNotNull(nullableName) { "Name must not be null" }`
Tags: kotlin null-safety
<!--ID: 1774840548977-->
END

START
Coding Questions
When should you use `require()` in Kotlin?
Back:
- When **validating input** at function boundaries
- Throws `IllegalArgumentException` if the condition is false
- `require(age > 0) { "Age must be positive, got $age" }`
Tags: kotlin null-safety
<!--ID: 1774840548989-->
END

START
Coding Questions
What is the difference between **lenient** (`?.`, `?:`) and **strict** (`requireNotNull()`, `require()`) null strategies in Kotlin?
Back:
- **Lenient** — handle null gracefully: return `null` or a fallback value
- **Strict** — crash fast when assumptions are violated: throw `IllegalArgumentException`
- Use lenient when null is an acceptable state, strict when null indicates a bug
Tags: kotlin null-safety
<!--ID: 1774840549001-->
END

START
Coding Questions
How does Kotlin's `when` expression differ from Java's `switch`?
Back:
- **Returns a value** — can assign result directly
- **No `break` needed** — each branch is isolated
- Supports **range checks**: `in 90..100`
- Supports **type checks** with smart cast: `is String`
- Supports **boolean conditions** (without argument): `when { x.isOdd() -> ... }`
- **Exhaustive enum checking** — compiler-enforced, no silent fall-through
Tags: kotlin null-safety
<!--ID: 1774840549013-->
END

START
Coding Questions
How do you match **multiple values** in a single `when` branch?
Back: Separate values with a comma: `0, 1 -> "binary"`
Tags: kotlin null-safety
<!--ID: 1774840549025-->
END

START
Coding Questions
How does `when` handle **range checking** in Kotlin?
Back:
- Use the `in` keyword with a range: `in 90..100 -> "A"`
- Java `switch` cannot do range checks at all
```kotlin
when (score) {
    in 90..100 -> "A"
    in 80..89 -> "B"
    else -> "F"
}
```
Tags: kotlin null-safety
<!--ID: 1774840549037-->
END

START
Coding Questions
What is **smart casting** inside a `when` type check?
Back:
- After `is Type`, Kotlin automatically casts the variable — no manual cast needed
- `is String -> println(obj.length)` — `obj` is already `String` inside the branch
Tags: kotlin null-safety
<!--ID: 1774840549048-->
END

START
Coding Questions
How does `when` work **without an argument** in Kotlin?
Back:
- Each branch is a **boolean expression** — replaces `if-else` chains
```kotlin
when {
    x.isOdd() -> "x is odd"
    y.isEven() -> "y is even"
    else -> "x+y is odd"
}
```
Tags: kotlin null-safety
<!--ID: 1774840549060-->
END

START
Coding Questions
Why is `when` with enums considered safer than Java `switch`?
Back:
- The compiler enforces **exhaustive checking** — no `else` needed when all cases are covered
- If you add a new enum value later, the compiler **forces** you to handle it
- Java `switch` silently falls through to `default`
Tags: kotlin null-safety
<!--ID: 1774840549072-->
END

START
Coding Questions
What does the **not-null assertion operator** `!!` do in Kotlin, and when should you use it?
Back: `!!` **asserts** that a value is non-null and bypasses Kotlin's null safety system:
```kotlin
val length = name!!.length  // throws NullPointerException if name is null
```
- If value is `null` at runtime → throws `NullPointerException`
- Use only when you are **absolutely certain** the value cannot be null (e.g. external API guarantees non-null despite nullable return type)
- Prefer `?.`, `?:`, or `requireNotNull()` in almost all cases
Tags: kotlin null-safety
END
