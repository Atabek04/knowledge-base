---
created: 2026-05-14
aliases: [javap]
tags: [java, jvm, tooling, bytecode]
---

`javap` is the JDK's **class file disassembler**. It reads a compiled `.class` file and prints its structure: package, fields, methods, signatures, constant pool, and JVM bytecode instructions. Ships with every JDK installation.

## Why use javap?

Verify what the compiler actually produced. Inspect bytecode to understand JIT optimizations, autoboxing, string concatenation, lambdas, `synchronized` lowering. Reverse-engineer public API of a class without source. Debug "why does this behave differently?" questions at the bytecode level.

---

What is the default output?

`javap ClassName` prints only **public** members — class declaration, public fields and methods, no bodies. Similar to a header file.

---

What does the `-p` flag do?

Shows **all members** including `private` and `package-private`. Useful when reading library internals.

---

What does the `-c` flag do?

Prints the actual **bytecode** of each method — the JVM instructions like `iload`, `invokevirtual`, `getfield`. This is the most useful flag.

---

How do you commonly combine flags?

`javap -p -c ClassName` — shows every member **and** its bytecode. The standard "what did the compiler do?" command.

## Useful flags

| Flag | Purpose |
|------|---------|
| `-p` | include private + package-private members |
| `-c` | disassemble method bodies into bytecode |
| `-v` | verbose: constant pool, stack map, line numbers, access flags |
| `-s` | print internal type signatures (descriptors) |
| `-l` | print line numbers and local variable tables |
| `-constants` | show final constants |

## Common examples

```bash
# Compile then inspect
javac Hello.java
javap Hello                    # public API only
javap -p Hello                 # all members
javap -c Hello                 # bytecode of public methods
javap -p -c Hello              # everything (most common)
javap -v Hello                 # full verbose dump

# Inspect a class inside a JAR
javap -c -p -classpath myapp.jar com.example.MyService

# JDK class
javap -c java.lang.String
```

## What you learn from `-c` output

- **String concatenation** in modern Java compiles to `invokedynamic` with `StringConcatFactory`, not `StringBuilder` chains
- **Autoboxing**: `Integer.valueOf(int)` calls appear where you wrote a plain `int`
- **Switch expressions** lower to `tableswitch` / `lookupswitch`
- **Lambdas** compile to a private synthetic method + `invokedynamic` bootstrapped by `LambdaMetafactory`
- **Enhanced `for`** over an array lowers to an index-based loop; over an `Iterable` uses `Iterator`

## Read more

- [[Java bytecode isn't Machine code]]
- [[JVM interpreter executes bytecode by mapping instructions to pre-compiled C functions]]
- [[Method inlining - replacing method call with method's actual code]]
- [[Java MOC]]
