---
created: 2026-06-01
aliases: [call stack, stack frame, call stack Java]
tags:
  - java/jvm
  - python/core
---

Every time a method is called, the JVM pushes a **stack frame** onto the call stack. When the method returns, that frame is popped and destroyed — locals are gone.

The call stack is **LIFO**: last method called is first to return.

![[call_stack_diagram.png]]

Each frame holds:
- local variables
- parameters
- the return address (where to go after this method finishes)

```java
void main() {
    foo();         // frame pushed
}                  // foo's frame popped on return

void foo() {
    int x = 5;    // x lives in foo's frame only
    bar();         // another frame pushed on top
}                  // foo's frame popped, x gone forever

void bar() { ... }
```

---

### Watch

[Call stack animation — how frames change as code runs](https://www.youtube.com/watch?v=pTZppmeZSBQ)

---

Read more:
- [[A generator object is a suspended stack frame that resumes at yield]]
- [[Java has 4 types of variables each with distinct scope and memory location]]
