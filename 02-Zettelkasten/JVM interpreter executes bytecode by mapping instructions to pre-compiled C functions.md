---
created: 2026-06-08
tags: [java, jvm, compilation]
aliases: [JVM bytecode execution, bytecode interpreter]
---

[[Java bytecode is not machine code — it targets the JVM instruction set, not a physical CPU|Bytecode]] cannot run on hardware directly — the JVM must translate it at runtime. The JVM interpreter is the component that does this.

<mark style="background: #FFF3A3A6;">The JVM interpreter is written in C. When it encounters a bytecode opcode, it maps it to a pre-compiled C function that already knows how to perform that operation in native machine code.</mark>

No on-the-fly assembly generation happens — the C functions are compiled ahead of time and the interpreter simply dispatches to the right one.

---

### Execution chain

```
.java → javac → bytecode (.class) → JVM interpreter → pre-compiled C function → native machine code → CPU
```

Each step in the chain adds one layer of indirection:
- `javac` compiles source to bytecode (platform-independent)
- The JVM interpreter maps bytecode opcodes to C functions (platform-specific, per JVM install)
- The C functions execute as native machine code on the CPU

---

### Why pre-compiled C functions

Writing the interpreter in C means the JVM itself is compiled once per platform (x86 JVM, ARM JVM, etc.). The bytecode stays the same everywhere — only the C function implementations differ per CPU architecture.

This is also why JIT compilation is a significant optimization: instead of dispatching through C for every opcode, the JIT compiles hot bytecode directly to native machine code, cutting out the interpreter dispatch entirely.

---

### Read more

- [[Java bytecode is not machine code — it targets the JVM instruction set, not a physical CPU]]
- [[JVM has 5 key responsibilities]]
- [[Write Once, Run Anywhere principle works because of JVM]]
