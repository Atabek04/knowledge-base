> It's not related to GC or class unloading.

Eliminating dead code is one of techniques of runtime optimizations in JVM.

Assume that we have this code:

```java
if (false) {
    System.out.println("This never runs");
}

int x = 5;
return x;
```

The JVM recognizes that `if (false)` block can never execute

So it removes it entirely from the compiled native code
Same with unreachable code after a `return` statement

Why?
Smaller, faster compiled code.
Less memory wasted on useless instructions.
