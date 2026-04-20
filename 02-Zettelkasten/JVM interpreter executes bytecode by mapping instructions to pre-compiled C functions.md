---
aliases: [JVM bytecode execution, bytecode interpreter]
---

<mark style="background: yellow">Java bytecode is not machine code</mark> — it targets the JVM (a virtual machine), not physical CPU hardware.

Because of this, bytecode can't run on its own.

---

### Why Bytecode Needs the JVM

The <mark style="background: yellow">JVM interpreter is written in C</mark>.

When it sees a bytecode instruction, it doesn't convert it on the fly into raw assembly. Instead, it maps each bytecode opcode to a **pre-compiled C function** that already knows how to perform that operation in native machine code.

So the execution chain looks like:

```
.java → javac → bytecode (.class) → JVM interpreter → pre-compiled C function → native machine code → CPU
```

---

### Bytecode vs Machine Code

| Aspect           | Java Bytecode                      | Machine Code                       |
| ---------------- | ---------------------------------- | ---------------------------------- |
| **Target**       | JVM (virtual machine)              | Physical CPU (x86, ARM, etc.)      |
| **Platform**     | Platform-independent               | Platform-specific                  |
| **Execution**    | Interpreted or JIT-compiled by JVM | Directly executed by CPU           |
| **Instructions** | JVM instruction set (~200 opcodes) | CPU instruction set (thousands)    |
| **Example**      | `iload_0`, `iadd`                  | `mov eax, [ebp-4]`, `add eax, ebx` |

---

Read more:
- [[JVM has 5 key responsibilities]]
- [[Write Once, Run Anywhere principle works because of JVM]]
