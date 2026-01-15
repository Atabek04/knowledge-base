---
created: 2026-01-12
tags: [linux/process]
---

A **process** is a running instance of a program with its own isolated memory space and allocated resources.

One program can have multiple processes running simultaneously.

## Key characteristics

**Running instance** — a program file on disk becomes a process when loaded into memory and executed.

**Isolated memory** — each process has its own address space and cannot access another process's memory.

**Unique ID (PID)** — the OS assigns a process identifier for tracking and management.

**Resources** — the OS allocates CPU time, file descriptors, memory, and network sockets to each process.

**OS managed** — only the OS can start, stop, pause, or kill processes.

**User mode execution** — processes run in restricted mode and cannot execute privileged instructions.

## Program vs process

**Program** = static file on disk containing executable code.

**Process** = dynamic program running in memory.

One program can spawn multiple processes.

**Example:** Opening three browser windows creates three separate browser processes from one program file.

## Links

- [[Context switch allows one CPU core to execute multiple processes by rapidly switching between them]]
- [[Kernel is the core OS program with complete control over system]]
- [[Applications communicate with operating system through system calls]]
- [[Linux MOC]]
