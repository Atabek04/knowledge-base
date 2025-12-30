Java bytecode designed for the JVM only, not for physical hardware.

We still need JVM to:
1. Interpret bytecode
2. translate bytecode into a machine code.

---

**Bytecode vs Machine Code:**

| Aspect           | Java Bytecode                      | Machine Code                       |
| ---------------- | ---------------------------------- | ---------------------------------- |
| **Target**       | JVM (virtual machine)              | Physical CPU (x86, ARM, etc.)      |
| **Platform**     | Platform-independent               | Platform-specific                  |
| **Execution**    | Interpreted or JIT-compiled by JVM | Directly executed by CPU           |
| **Instructions** | JVM instruction set (~200 opcodes) | CPU instruction set (thousands)    |
| **Example**      | `iload_0`, `iadd`                  | `mov eax, [ebp-4]`, `add eax, ebx` |
