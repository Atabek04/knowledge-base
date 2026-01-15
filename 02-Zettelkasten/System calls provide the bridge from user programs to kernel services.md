---
created: 2026-01-06
tags: [os/kernel]
sr-due: 2026-01-09
sr-interval: 1
sr-ease: 2.3
---

A **system call** is the only legal way for user space programs to request services from the kernel. When an application needs to read a file, allocate memory, or use the network, it must make a system call—there is no alternative.

The kernel exposes a fixed set of system calls that applications can invoke. Each system call has a unique number. When a program calls `read()`, `write()`, `open()`, or `malloc()`, these are typically wrappers around kernel system calls.

The flow is: Application (user space) → **system call** → Kernel (kernel space) → Hardware → Result returned to application.

System calls are the contract between applications and the operating system. On Linux, a program can read the `/proc/sys/kernel/syscall_table` to see all available system calls (typically 300+). Common examples:

| System Call | Number | Purpose |
|-------------|--------|---------|
| `read` | 0 | Read from file descriptor |
| `write` | 1 | Write to file descriptor |
| `open` | 2 | Open or create file |
| `close` | 3 | Close file descriptor |
| `fork` | 57 | Create new process |
| `exec` | 59 | Execute program |

The kernel maintains a **syscall table** (array of function pointers) that maps syscall numbers to kernel handler functions. When a system call is invoked with a specific number, the kernel looks up the handler and executes it.

Without system calls, applications would need to know how every hardware device works and communicate directly with them—which would be unsafe, complex, and non-portable. System calls abstract hardware details and provide a unified interface.

## Links
- [[Kernel is the core OS program with complete control over system]]
- [[User Space and Kernel Space represent two CPU privilege modes]]
- [[CPU mode switch transitions from User Mode to Kernel Mode during syscalls]]
- [[VMs & Containers MOC]]
