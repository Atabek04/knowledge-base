---
created: 2026-01-06
tags: [os/kernel]
sr-due: 2026-01-09
sr-interval: 1
sr-ease: 2.3
---

A **mode switch** (also called a **trap**) is the moment the CPU transitions from **User Mode** to **Kernel Mode**. This transition is triggered by privileged operations that only the kernel can handle.

Mode switches are triggered by three types of events:

1. **System call instruction** — application explicitly requests kernel service
2. **Hardware interrupt** — keyboard press, network packet arrival, timer tick
3. **Exception** — division by zero, page fault, invalid instruction

The CPU physically blocks privileged instructions in user mode. If a user program tries to write directly to disk, the CPU refuses and triggers an exception. The kernel then handles this exception—usually by terminating the program or logging an error.

The hardware enforces this boundary. There is no way for user code to bypass the mode switch mechanism or execute kernel code directly. This prevents compromised or buggy applications from taking over the system.

## Step-by-Step Example: Reading a File

Here's what happens when an application calls `read()` to read data from disk:

```
1. App calls read() function (user space)
         ↓
2. C library converts to syscall instruction (syscall number 0 on Linux)
         ↓
3. CPU switches from User Mode → Kernel Mode (TRAP)
         ↓
4. Kernel validates request & accesses disk via device driver
         ↓
5. Kernel copies data from disk into application's memory buffer
         ↓
6. CPU switches back to User Mode
         ↓
7. App receives the data and continues execution
```

This entire process happens in microseconds. The mode switch adds tiny overhead but provides essential security—the kernel can validate requests before granting hardware access.

The kernel uses the **syscall table** (see [[System calls provide the bridge from user programs to kernel services]]) to find the correct handler function. The CPU stores the syscall number in a register before triggering the trap, then the kernel reads that register to know which handler to call.

## Links
- [[Kernel is the core OS program with complete control over system]]
- [[User Space and Kernel Space represent two CPU privilege modes]]
- [[System calls provide the bridge from user programs to kernel services]]
- [[Buffers store data during transfers between components with speed mismatches]]
- [[VMs & Containers MOC]]
