---
created: 2026-06-08
tags: [java, jvm, compilation]
aliases: [bytecode vs machine code, java bytecode]
---

When you compile a `.java` file with `javac`, the output is **bytecode** — a set of instructions stored in `.class` files. Bytecode is not machine code: it cannot run directly on a CPU.

<mark style="background: #FFF3A3A6;">Bytecode targets the JVM (a virtual machine), not any physical processor. It is platform-independent by design.</mark>

---

### Bytecode vs machine code

| | Java bytecode | Machine code |
|---|---|---|
| **Target** | JVM (virtual machine) | Physical CPU (x86, ARM, etc.) |
| **Platform** | Platform-independent | Platform-specific |
| **Execution** | Interpreted or JIT-compiled by JVM | Directly executed by CPU |
| **Instruction set** | ~200 JVM opcodes | Thousands of CPU instructions |
| **Example instructions** | `iload_0`, `iadd` | `mov eax, [ebp-4]`, `add eax, ebx` |

---

### Why this enables portability

The same `.class` file runs on any machine with a JVM — Windows, Linux, macOS, ARM — because the JVM is the target, not the OS or CPU. This is the foundation of the [[Write Once, Run Anywhere principle works because of JVM|Write Once, Run Anywhere]] guarantee.

---

### What actually runs bytecode

Since bytecode cannot execute on hardware directly, the JVM must translate it at runtime. The [[JVM interpreter executes bytecode by mapping instructions to pre-compiled C functions|JVM interpreter]] does this by mapping each opcode to a pre-compiled C function that performs the equivalent operation in native machine code.

---

### Read more

- [[JVM interpreter executes bytecode by mapping instructions to pre-compiled C functions]]
- [[Write Once, Run Anywhere principle works because of JVM]]
- [[JVM has 5 key responsibilities]]
