> Method inlining - one of techniques of runtime optimizations of JVM.

Assume that we have this code:

```java
public int add(int a, int b) {
    return a + b;
}

int result = add(5, 3);
```

Without inlining, the JVM has to:
1. Create a stack frame
2. Pass arguments
3. Execute the method
4. Return the result

---

With inlining:
- JVM replaces `add(5, 3)` directly with `5 + 3` in the code.
- No method call overhead.
- The method disappears :luc_arrow_right: its code is inserted where it was called.
