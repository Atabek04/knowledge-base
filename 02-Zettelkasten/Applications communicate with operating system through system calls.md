---
created: 2026-01-12
tags: [linux/fundamentals]
---

Applications communicate with the OS kernel via **system calls**.

A system call is a request from an application to the OS kernel to perform a privileged operation.

This includes file I/O, memory allocation, network access, and hardware control.

## How it works

```
Application → System Call → OS Kernel → Hardware
```

The application cannot execute privileged operations directly because it runs in **user mode** with restricted permissions.

Only the kernel runs in **kernel mode** with unrestricted hardware access.

## Examples of system calls

**`read()`** — request to read data from a file.

**`write()`** — request to write data to disk.

**`open()`** — request to open a file.

**`socket()`** — request to create a network connection.

**`fork()`** — request to create a new process.

## Why system calls exist

The OS enforces **privilege separation** between user mode and kernel mode.

Applications run in user mode and cannot execute privileged instructions or access hardware directly.

System calls are the **only legal bridge** between user mode and kernel mode.

This prevents malicious or buggy applications from corrupting the system or accessing hardware without validation.

## Links

- [[Kernel is the core OS program with complete control over system]]
- [[User Space and Kernel Space represent two CPU privilege modes]]
- [[System calls provide the bridge from user programs to kernel services]]
- [[CPU mode switch transitions from User Mode to Kernel Mode during syscalls]]
- [[Linux MOC]]
