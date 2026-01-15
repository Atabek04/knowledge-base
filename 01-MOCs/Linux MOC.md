---
created: 2026-01-12
tags: [moc]
---

Operating system fundamentals, Linux kernel architecture, Unix/Linux history, and system management concepts.

## Part 1 — OS Fundamentals

### Core Concepts

- [[Kernel is the core OS program with complete control over system]] — first program after bootloader, manages all resources
- [[Operating system mediates between applications and hardware for security and abstraction]] — prevents direct hardware access
- [[Operating system prevents direct hardware access for security, abstraction, and resource coordination]] — reasons for OS mediation
- [[Applications communicate with operating system through system calls]] — the bridge between user programs and kernel

### User Interface

- [[GUI and CLI are applications that mediate between users and kernel through system calls]] — graphical vs command-line interfaces
- [[Linux terminal prompt shows username, hostname, current directory, and user privilege level]] — understanding the prompt format

## Part 2 — Linux History & Philosophy

### Unix Origins

- [[Unix is a foundational operating system created in 1969 that influenced modern operating system design]] — Bell Labs creation and Unix philosophy
- [[Berkeley Software Distribution became open source when Unix source code was leaked]] — BSD variants and history
- [[POSIX is a standard specification that ensures operating system compatibility and portability]] — standardizing Unix interfaces

### Linux Creation

- [[Linus Torvalds created Linux in 1991 as an open-source alternative to proprietary Minix]] — birth of Linux kernel
- [[Linux is the kernel while Linux distributions package the kernel with tools and utilities]] — kernel vs complete OS

## Part 3 — System Architecture

### Process Management

- [[Process is an instance of a program in execution with isolated memory space and resources]] — what processes are
- [[Context switch allows one CPU core to execute multiple processes by rapidly switching between them]] — how multitasking works

### Memory Management

- [[RAM provides fast temporary storage while hard disk provides large persistent storage]] — complementary roles
- [[CPU cannot directly access hard disk because of speed and interface differences, requiring RAM as intermediary]] — why RAM is necessary
- [[Memory swapping extends RAM by moving unused data to hard disk when RAM is full]] — extending RAM capacity

### Filesystem

- [[Linux root filesystem uses a hierarchical tree structure with standardized directories for different purposes]] — FHS directory layout

## Related MOCs

- [[VMs & Containers MOC]] — virtualization, containers, kernel namespaces, cgroups
- [[Networking MOC]] — network protocols and communication

## Practice

(Flashcards to be added)

## External Resources

- [Linux man pages](https://man7.org/)
- [Linux Kernel Documentation](https://www.kernel.org/doc/)
- [The Linux Command Line](https://linuxcommand.org/)
