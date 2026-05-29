TARGET DECK: Tech-KB::Java::Variables & Types
Tags: java variables types
**Chapter:** Variables & Types
**Related:** [[Java MOC]]

---

START
Coding Questions
What are the 4 types of Java variables?
Back:
- **Instance fields** — belong to an object, each object has its own copy
- **Static fields** — belong to the class, shared across all instances
- **Local variables** — declared inside a method, destroyed when method returns
- **Parameters** — passed into a method at call time, scoped to method body
Tags: java variables
END

START
Coding Questions
Where does the JVM store each of the 4 variable types?
Back:
| Variable Type | JVM Storage |
|---|---|
| Instance field | **Heap** — inside the object allocation |
| Static field | **Heap** — inside the Class object |
| Local variable | **Stack** — inside the method's stack frame |
| Parameter | **Stack** — same stack frame as local variables |
Tags: java variables jvm
END

START
Coding Questions
What is the default initialization difference between instance fields and local variables?
Back:
- **Instance & static fields** — auto-initialized (`0`, `null`, `false`)
- **Local variables & parameters** — NOT initialized by default; compiler forces explicit assignment before use
Tags: java variables
END

START
Coding Questions
How does a primitive variable differ from a reference variable in memory?
Back:
- **Primitive** — stores the actual value directly (`int age = 25` → variable contains `25`)
- **Reference** — stores a memory address pointing to the object on the heap (`String name = new String("John")` → variable contains `0x7a8f9b2`)
Tags: java variables types
END

START
Coding Questions
What happens when you assign one reference variable to another?
Back: Both variables point to the **same object** in memory — no copy is made.

```java
String s1 = new String("Hello");
String s2 = s1; // s2 points to same object
```

Modifying the object through `s1` is visible through `s2`.
Tags: java variables references
END

START
Coding Questions
Why does Java have both primitives and wrapper types (dual type system)?
Back: **Performance.**
- Primitives live on the **stack** — fast, no GC overhead
- Objects live on the **heap** — slower (allocation, GC, pointer dereferencing)

But primitives **can't be used in generics or collections** (`List<int>` is illegal) — so wrappers exist for those cases.
Tags: java types
END

START
Coding Questions
What is autoboxing in Java?
Back: **Autoboxing** — Java automatically converting between primitives and their wrapper types (Java 5+).

```java
List<Integer> list = new ArrayList<>();
list.add(5);           // autoboxing: int → Integer
int value = list.get(0); // unboxing: Integer → int
```
Tags: java types autoboxing
END

START
Coding Questions
What is the hidden cost of autoboxing?
Back: Each autobox creates a **new heap object** — adds allocation overhead and GC pressure.

In tight loops or high-frequency code, repeated autoboxing can degrade performance significantly.
Tags: java types autoboxing
END

START
Coding Questions
What is upcasting in Java and is it safe?
Back: **Upcasting** — casting a child type to a parent type (e.g., `Dog` → `Animal`).
- Always **implicit and safe** — a Dog *is* an Animal
- No `(Type)` syntax needed

```java
Dog dog = new Dog();
Animal animal = dog; // implicit upcast
```
Tags: java casting types
END

START
Coding Questions
What is downcasting in Java and when does it fail?
Back: **Downcasting** — casting a parent-typed variable back to a child type. Requires explicit `(Type)` syntax.

Fails with `ClassCastException` if the actual object in memory is not the target type:

```java
Animal animal = new Cat();
Dog dog = (Dog) animal; // 💥 ClassCastException — it's a Cat
```

Rule: the variable type doesn't matter — what matters is the **actual object in memory**.
Tags: java casting types
END

START
Coding Questions
What should you always do before downcasting?
Back: Check with `instanceof` to avoid `ClassCastException`:

```java
if (animal instanceof Dog) {
    Dog dog = (Dog) animal; // safe
    dog.fetch();
}
```
Tags: java casting types
END

START
Coding Questions
What are the 4 scope levels in Java?
Back:
- **Class scope** — `private` field outside any method; accessible anywhere in the class
- **Method scope** — variable inside a method; only accessible within that method
- **Loop scope** — variable declared in a loop; only accessible inside the loop
- **Bracket scope** — variable inside `{}` block; only accessible within those braces
Tags: java variables scope
END

START
Coding Questions
How do you distinguish primitive type names from object/wrapper type names in Java?
Back: **Naming convention:**
- **Primitives** start with lowercase: `int`, `double`, `boolean`, `char`, `long`, `float`, `byte`, `short`
- **Object/wrapper types** start with uppercase: `Integer`, `Double`, `Boolean`, `Character`, `String`
Tags: java types naming
END

START
Coding Questions
Where does a Java object live vs where does its reference live?
Back:
- **Object** → always on the **heap**, regardless of where it's declared
- **Reference** (the variable holding the address) → depends on declaration site:
  - Local variable → **stack**
  - Instance variable → **heap** (part of the enclosing object)
  - Static variable → **metaspace**
Tags: java memory heap stack
END

START
Coding Questions
For `List<Integer> list = new ArrayList<>()` declared inside a method — what lives on the stack vs heap?
Back:
- `list` reference → **stack**
- `ArrayList` object → **heap**
- Each `Integer` wrapper object → **heap**

Only the variable `list` is on the stack. All objects are always on the heap.
Tags: java memory heap stack
END

START
Coding Questions
Why is passing an object to a Java method cheap?
Back: You copy the **reference** (4 or 8 bytes), not the object itself.

The reference has a fixed size regardless of how large the object is — so the cost is always the same.
Tags: java memory references
END
