TARGET DECK: Tech-KB::Java::JVM & Compilation
Tags: java jvm
**Chapter:** JVM & Compilation Fundamentals
**Related:** [[Java MOC]]

---

START
Coding Questions
What is the JVM and what does it do?
Back: **JVM (Java Virtual Machine)** — runtime engine that executes Java bytecode.
- Platform-specific implementation (different JVM for each OS/CPU)
- Core component that actually runs Java programs
Tags: java jvm
<!--ID: 1780311507123-->
END

START
Coding Questions
What does the JRE include and who uses it?
Back: **JRE (Java Runtime Environment)** = JVM + standard libraries (`java.lang`, `java.util`, etc.)
- Everything needed to **run** Java applications
- Does NOT include development tools
- Installed by end users who only run apps, not develop them
Tags: java jvm
<!--ID: 1780311507144-->
END

START
Coding Questions
What does the JDK include and who needs it?
Back: **JDK (Java Development Kit)** = JRE + development tools (`javac`, debugger, `javadoc`, etc.)
- Everything needed to **develop and run** Java applications
- Required by developers — not end users
Tags: java jvm
<!--ID: 1780311507164-->
END

START
Coding Questions
What are the 5 key responsibilities of the JVM?
Back:
1. **Bytecode loading & verification**
2. **Bytecode execution** — interpretation + JIT compilation
3. **Memory management** — heap (objects), stack (method calls), garbage collection
4. **Platform abstraction** — consistent API regardless of OS; translates Java threads to OS threads
5. **Runtime optimization** — profiling hot code paths, method inlining, dead code elimination
Tags: java jvm
<!--ID: 1780311507185-->
END

START
Coding Questions
How does the JVM execute bytecode at runtime?
Back: Two mechanisms:
- **Interpretation** — JVM reads each bytecode instruction and maps it to a pre-compiled C function
- **JIT compilation** — hot code paths are compiled to native machine code at runtime for faster re-execution
Tags: java jvm
<!--ID: 1780311507206-->
END

START
Coding Questions
Why can't Java bytecode run directly on the CPU?
Back: Bytecode targets the **JVM (virtual machine)**, not physical CPU hardware.
- Uses JVM instruction set (~200 opcodes like `iload_0`, `iadd`)
- CPU only understands its own instruction set (`mov eax`, `add eax, ebx`)
- JVM interpreter bridges the gap by mapping bytecode → native machine code
Tags: java jvm
<!--ID: 1780311507227-->
END

START
Coding Questions
What is the full execution chain from .java source to CPU?
Back:
`.java` → `javac` → `.class` (bytecode) → JVM interpreter → pre-compiled C function → native machine code → CPU
Tags: java jvm
<!--ID: 1780311507247-->
END

START
Coding Questions
Why does Java have different JDKs for each OS and CPU architecture?
Back: The **JVM itself is a compiled C program** — it must be compiled separately for each OS and processor architecture.
- The bytecode is platform-independent
- But the JVM that runs it is platform-specific
- That's what enables "Write Once, Run Anywhere" — same bytecode, different JVMs
Tags: java jvm
<!--ID: 1780311507268-->
END

START
Coding Questions
What is the trade-off between traditionally compiled languages (C, Go) and interpreted languages (Java, Python)?
Back:
| | Compiled (C, Go) | Interpreted (Java, Python) |
|--|--|--|
| **Speed** | Fastest — runs directly on CPU | Slower — runtime layer overhead |
| **Portability** | Must recompile per platform | Platform-independent code |
| **Safety** | No runtime checks | Runtime verification possible |
Tags: java jvm
<!--ID: 1780311507289-->
END

START
Coding Questions
What is JVM runtime profiling?
Back: **Profiling** — JVM monitors and measures code while it's running to identify "hot" code paths (frequently executed).
- Hot paths get JIT-compiled to native machine code
- Rarely executed code stays interpreted
- This is why Java gets faster the longer it runs
Tags: java jvm
<!--ID: 1780311507309-->
END

START
Coding Questions
What is `javap`?
Back: JDK **class file disassembler**. Reads a `.class` file and prints its structure: fields, methods, signatures, and bytecode instructions.
Tags: java jvm tooling javap
<!--ID: 1780311507329-->
END

START
Coding Questions
What does `javap -p` do?
Back: Includes **private** and **package-private** members in the output (default shows only public).
Tags: java jvm tooling javap
<!--ID: 1780311507349-->
END

START
Coding Questions
What does `javap -c` do?
Back: Disassembles method bodies into **JVM bytecode** (`iload`, `invokevirtual`, etc.) — the main reason to use javap.
Tags: java jvm tooling javap
<!--ID: 1780311507370-->
END

START
Coding Questions
What does the common combo `javap -p -c ClassName` show?
Back: Every member (public + private) **plus** its bytecode. Standard "what did the compiler produce?" command.
Tags: java jvm tooling javap
<!--ID: 1780311507391-->
END

START
Coding Questions
What does `javap -v` add?
Back: **Verbose** dump — constant pool, stack map frames, line number table, access flags, and full method bytecode.
Tags: java jvm tooling javap
<!--ID: 1780311507412-->
END
