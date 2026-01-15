---
created: 2026-01-06
tags: [virtualization/vms]
sr-due: 2026-01-09
sr-interval: 1
sr-ease: 2.3
---

A **Virtual Machine (VM)** is software that completely emulates a physical computer. From the perspective of an operating system running inside it, the VM appears to be a real machine with actual hardware components.

Each VM has its own virtual hardware:

- **Virtual CPU** — software that emulates a processor core
- **Virtual RAM** — a region of the host's RAM allocated to the VM
- **Virtual Disk** — a file on the host's filesystem that appears as a hard drive to the VM
- **Virtual Network Card** — software that emulates a network interface

The **Guest OS** (operating system inside the VM) cannot tell the difference between real hardware and emulated hardware. When the Guest OS tries to read from the "disk," it doesn't know it's actually reading from a file on the host. When it writes to "network," it doesn't know it's writing through software emulation.

**Emulation** in this context means software perfectly imitates hardware behavior. The software:

1. Accepts the same inputs real hardware would accept
2. Produces the same outputs real hardware would produce
3. Creates an illusion so complete that Guest OS cannot distinguish real from fake

**Concrete Example:**

When the Guest OS wants to write data to disk:

```
Guest OS: "Write this data to disk"
         ↓
Hypervisor intercepts the request
         ↓
Hypervisor: "I'll pretend to be your disk"
         ↓
Hypervisor writes data to a file on the real host disk
         ↓
Hypervisor returns "Success" to Guest OS
         ↓
Guest OS: "My write succeeded" (unaware it wrote to a file)
```

The Guest OS is fooled. It performed what it believes was a disk operation, but the hypervisor intercepted it and performed the real work differently.

This level of abstraction is powerful. You can run Windows Guest OS on Linux host OS, or Ubuntu on Windows, or any combination. The Guest OS doesn't care about the real hardware—it only needs the hypervisor to emulate correctly.

## Links
- [[Virtual Machine emulates complete physical computer in software]]
- [[Guest OS runs inside VM while Host OS runs on physical hardware]]
- [[Hypervisor creates and manages virtual machines by dividing physical resources]]
- [[Guest OS communicates with emulated hardware through hypervisor intercepts]]
- [[VMs & Containers MOC]]
