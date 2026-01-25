---
created: 2026-01-21
tags: [linux, shell, kernel, os-fundamentals]
---

A shell is the command-line interface that interprets user input and translates it into system calls that the kernel executes. The shell acts as an intermediary between the user and the operating system kernel.

When a user types a command, the shell parses it, expands variables and wildcards, and then requests the kernel to perform the requested operation through system calls like `open()`, `read()`, `fork()`, and `execve()`.

## How do shells interpret user commands?

All shells follow a similar parsing sequence: read input from user/script, tokenize (split into words), parse (check syntax), expand (variables, globs: *, ?), then execute (run command).

---

What are the main differences between sh, bash, and zsh?

**sh** (Bourne shell, 1979) is the POSIX standard with minimal features and maximum compatibility for system scripts. **bash** (1989) extends sh with additional features like history, aliases, and arrays while maintaining backward compatibility. **zsh** (1990) is a modern shell with advanced features and context-aware tab completion, commonly used by enthusiasts but not POSIX-compliant.

---

Which shell types require knowledge of system calls to work?

All shells must understand **system calls** like `open()` to open files, `read()` to read data, `fork()` to create processes, and `execve()` to execute programs. These are the fundamental operations shells translate user commands into.

---

Why do different shells exist if they all communicate with the same kernel?

Different shells prioritize different goals: **sh** prioritizes compatibility and portability, **bash** balances features with compatibility, and **zsh** prioritizes user experience and modern features. The choice depends on whether you need maximum portability, balance, or modern interactive features.

---

## Related Notes

- [[Kernel is the core OS program with complete control over system]]
- [[Applications communicate with operating system through system calls]]
- [[Linux terminal prompt shows username, hostname, current directory, and user privilege level]]
- [[Shebang tells the operating system which interpreter should execute a script]]

## Flashcards

?
What is the primary role of a shell?

A **shell** interprets user commands and translates them into **system calls** that the **kernel** executes.

---

?
What are the three main shells used in Linux?

**sh** (POSIX standard), **bash** (most common), and **zsh** (modern, user-friendly).

---

?
What are the five steps shells use to process commands?

1. **Read** input from user/script
2. **Tokenize** (split into words)
3. **Parse** (check syntax)
4. **Expand** (variables, globs: *, ?)
5. **Execute** (run command)

---

?
Name four common system calls that shells use to interact with the kernel.

**open()** — open file, **read()** — read data, **fork()** — create process, **execve()** — execute program.

---

?
What is the key difference between sh and bash?

**bash** extends **sh** with additional features (history, aliases, arrays) while maintaining backward compatibility; **sh** is the minimal POSIX standard.
