---
created: 2026-01-12
tags: [linux/history]
---

**POSIX** (Portable Operating System Interface X) is a standard specification that defines which system calls must exist and how they should behave.

It ensures compatibility and portability across Unix-like operating systems.

## What POSIX defines

Which system calls must exist — `open()`, `read()`, `write()`, `fork()`, `exec()`.

How they should behave — standardized function signatures and return values.

Standard file operations — consistent file I/O across systems.

Process management — creation, termination, and inter-process communication.

Command line utilities — standard shell commands and behavior.

## The problem POSIX solved

**Before POSIX:** Programs written for Solaris didn't work on AIX.

Programs written for HP-UX required rewriting for BSD.

Each OS had different system calls and behaviors, creating a developer nightmare.

## How POSIX works

POSIX guarantees core system calls exist across all compliant systems:

| System call | Purpose |
|-------------|---------|
| `open()` | Open file |
| `read()` | Read from file |
| `write()` | Write to file |
| `fork()` | Create process |
| `exec()` | Execute program |
| `pipe()` | Inter-process communication |

## POSIX-compliant systems

| OS | Status |
|----|--------|
| Linux | POSIX-compliant (mostly) |
| macOS | POSIX-certified |
| BSD | POSIX-certified |
| Unix variants | POSIX-certified |
| Windows | Not POSIX-compliant (partial support via WSL) |

## Why POSIX matters

**Write once, run anywhere** on POSIX systems.

**Example code:**
```c
int fd = open("file.txt", O_RDONLY);
read(fd, buffer, 100);
close(fd);
```

This code works on Linux, macOS, and BSD without modification.

**Without POSIX:** You would need to rewrite file operations for each operating system.

## Key benefit

**Portability** — standardized interface means applications work across Unix-like systems without changes.

## Links

- [[Unix is a foundational operating system created in 1969 that influenced modern operating system design]]
- [[Berkeley Software Distribution became open source when Unix source code was leaked]]
- [[Applications communicate with operating system through system calls]]
- [[Linux MOC]]
