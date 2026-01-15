---
created: 2026-01-06
tags: [virtualization/vms]
sr-due: 2026-01-09
sr-interval: 1
sr-ease: 2.3
---

**Host OS** and **Guest OS** are two distinct operating systems in a virtualization setup, each with different responsibilities and hardware interactions.

| Aspect | Host OS | Guest OS |
|--------|---------|----------|
| **Installation Location** | Installed directly on physical machine | Installed inside a VM |
| **Hardware Access** | Talks to real hardware directly | Talks to emulated (fake) hardware |
| **Resource Ownership** | Owns all physical resources | Owns only allocated resources |
| **Role** | Manages physical machine | Manages its own VM environment |
| **Kernel** | Real OS kernel controlling physical hardware | Real OS kernel but controlling virtual hardware |

The **Host OS** manages the physical machine and all its hardware. When you boot a laptop, the Host OS (Windows, macOS, Linux) loads first. It controls the real CPU, RAM, disk, network card, and all peripherals.

The **Guest OS** is a complete operating system that runs inside a VM as an application under the Host OS. It has its own kernel, own filesystems, own network configuration. But these are all virtual—managed by the Host OS and hypervisor.

**Concrete Example:**

Your laptop is a MacBook with macOS (Host OS). You install VirtualBox (a hypervisor) on your MacBook. Inside VirtualBox, you create a VM and install Ubuntu Linux (Guest OS).

From the MacBook's perspective:
- macOS runs the real hardware
- VirtualBox is just an application running under macOS
- The Ubuntu inside VirtualBox is completely isolated, doesn't know about macOS

From the Ubuntu's perspective:
- Ubuntu owns and controls a machine (the VM)
- It has virtual CPU, virtual RAM, virtual disk, virtual network
- It's completely unaware that another OS (macOS) actually owns the hardware

The two operating systems are completely separate entities. You can have multiple Guest OSs running simultaneously, each running its own operating system kernel independently. The Host OS mediates all hardware access and isolates each VM from the others.

## Links
- [[Kernel is the core OS program with complete control over system]]
- [[Virtual Machine emulates complete physical computer in software]]
- [[Hypervisor creates and manages virtual machines by dividing physical resources]]
- [[VMs & Containers MOC]]
