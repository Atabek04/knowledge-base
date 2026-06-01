TARGET DECK: Tech-KB::Java::Runtime Optimizations
Tags: java jvm optimization
**Chapter:** Runtime Optimizations
**Related:** [[Java MOC]]

---

START
Coding Questions
What is method inlining in the JVM?
Back: **Method inlining** — JVM replaces a method call with the method's actual code directly at the call site.

```java
// Before inlining
int result = add(5, 3); // → calls add(), creates stack frame

// After inlining
int result = 5 + 3; // → method disappears, code inserted inline
```
Tags: java jvm optimization
<!--ID: 1780311507041-->
END

START
Coding Questions
Why does the JVM use method inlining?
Back: Eliminates **method call overhead**:
- No stack frame creation
- No argument passing
- No return jump

Result: fewer CPU instructions, faster execution — especially for small, frequently called methods.
Tags: java jvm optimization
<!--ID: 1780311507062-->
END

START
Coding Questions
What is dead code elimination in the JVM?
Back: **Dead code elimination** — JVM removes code that can never execute from the compiled native output.

```java
if (false) {
    System.out.println("never runs"); // removed entirely
}
```

Also removes unreachable code after a `return` statement.
Tags: java jvm optimization
<!--ID: 1780311507082-->
END

START
Coding Questions
Why does the JVM eliminate dead code?
Back: Produces **smaller, faster compiled code**:
- Less memory used for useless instructions
- Fewer CPU instructions to execute
- Cleaner native output after JIT compilation
Tags: java jvm optimization
<!--ID: 1780311507102-->
END
