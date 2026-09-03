---
aliases: [first-class functions, functions as values, higher-order functions]
---

In most languages, a function is just a procedure you call. In languages with **first-class functions**, a function is a *value* — just like an integer or a string. You can store it in a variable, pass it as an argument, and return it from another function.

This is what makes patterns like [[Strategy pattern in Kotlin uses a function type instead of an interface|Strategy in Kotlin]] possible without any boilerplate interface.

### What "first-class" means concretely

Three capabilities define a first-class function:

1. **Store** — assign a function to a variable
2. **Pass** — hand a function to another function as an argument
3. **Return** — produce a function as a return value

A function that accepts or returns another function is called a **higher-order function**.

### Kotlin

Kotlin has native first-class functions. The type of a function is written as `(ParamType) -> ReturnType`.

```kotlin
val greet: (String) -> String = { name -> "Hi, $name" }

fun run(fn: (String) -> String): String = fn("Atabek")

run(greet)  // "Hi, Atabek"
```

A `typealias` can name the function type to make it readable:

```kotlin
typealias Greeter = (String) -> String
val greet: Greeter = { name -> "Hi, $name" }
```

### Python

Functions in Python are objects. Pass them directly — no wrapping needed.

```python
def greet(name: str) -> str:
    return f"Hi, {name}"

def run(fn):
    return fn("Atabek")

run(greet)  # "Hi, Atabek"
```

`lambda` creates an anonymous function inline: `lambda name: f"Hi, {name}"`.

### Java

Java has no true first-class functions. The workaround is [[A Java functional interface has exactly one abstract method — default and static methods don't count toward that limit|functional interfaces]] — interfaces with exactly one abstract method — filled in by [[A Java lambda is an anonymous object implementing a functional interface's single abstract method, not a value of a function type|a lambda]], an anonymous object implementing that one method.

```java
Function<String, String> greet = name -> "Hi, " + name;

static String run(Function<String, String> fn) {
    return fn.apply("Atabek");
}

run(greet);  // "Hi, Atabek"
```

---

### Read more
- [[Strategy pattern in Kotlin uses a function type instead of an interface]]
- [[Strategy pattern in Python uses a first-class function as the strategy]]
- [[Strategy pattern in Java is an interface implemented by interchangeable algorithm classes]]
- [[Kotlin typealias creates a readable alias for an existing type without creating a new class]]
- [[A Java functional interface has exactly one abstract method — default and static methods don't count toward that limit]]
- [[A Java lambda is an anonymous object implementing a functional interface's single abstract method, not a value of a function type]]
