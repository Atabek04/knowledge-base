---
created: 2026-01-06
tags: [os/kernel]
sr-due: 2026-01-09
sr-interval: 1
sr-ease: 2.3
---

The CPU operates in two distinct **privilege modes** that determine what instructions can execute and what hardware can be accessed. Modern processors have hardware-enforced privilege levels for security.

**Kernel Space** is where the kernel code runs with unrestricted hardware access. Instructions in kernel mode can read/write any memory location, access all devices, enable/disable interrupts, and execute privileged instructions. The CPU physically allows these operations only in kernel mode.

**User Space** is where all application programs run with restricted, isolated access. Applications cannot directly access hardware. They cannot read/write arbitrary memory, cannot access other programs' memory, cannot access hardware devices. Attempting privileged instructions in user mode causes the CPU to reject them.

| Aspect | Kernel Space | User Space |
|--------|--------------|------------|
| **Privilege Level** | Unrestricted | Restricted, isolated |
| **Hardware Access** | Full access to all devices | No direct hardware access |
| **Memory Access** | Can access any memory | Can only access own memory |
| **Code Running Here** | OS kernel, device drivers | User applications |
| **Crash Impact** | System crash, everything fails | Only that application dies |
| **Who Controls Switches** | Kernel decides when to context switch | Cannot control own context switches |

The hardware enforces this boundary strictly. If a user program tries to execute a privileged instruction (like reading from disk), the CPU generates an **exception** and the kernel handles it. This prevents buggy or malicious applications from crashing the entire system.

The privilege mode switch happens frequently during normal operation. When an application needs to read a file, it cannot do it directly—it must request the kernel in kernel mode, then switch back to user mode to continue running.

## Links
- [[Kernel is the core OS program with complete control over system]]
- [[System calls provide the bridge from user programs to kernel services]]
- [[CPU mode switch transitions from User Mode to Kernel Mode during syscalls]]
- [[VMs & Containers MOC]]
