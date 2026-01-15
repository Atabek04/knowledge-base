---
created: 2026-01-06
tags: [virtualization/vms]
sr-due: 2026-01-09
sr-interval: 1
sr-ease: 2.3
---

A **hypervisor** is the software layer that creates, manages, and runs virtual machines. It is the essential technology that makes virtualization possible. The hypervisor sits between physical hardware and one or more Guest Operating Systems.

The hypervisor performs three critical responsibilities:

**1. Divides Physical Resources** — allocates portions of host CPU, RAM, disk, and network to each VM. VM1 might get 2 CPU cores and 4GB RAM, VM2 might get 4 CPU cores and 8GB RAM. The hypervisor enforces these limits.

**2. Isolates VMs from Each Other** — ensures one VM cannot access another VM's memory or interfere with its execution. A crash in VM1 doesn't affect VM2. One VM's runaway process doesn't steal another VM's CPU time.

**3. Emulates Hardware** — tricks each Guest OS into believing it owns actual hardware. When Guest OS tries to read from "disk," the hypervisor intercepts this and reads from a file instead. When Guest OS configures "network," the hypervisor creates virtual network interfaces.

![[hypervisor-diagram.png]]

The hypervisor runs with special privileges that allow it to intercept all privileged operations from Guest OSs. When a Guest OS tries to execute hardware operations (disk read, network send), the hypervisor catches these operations and handles them safely.

Hypervisors differ in implementation—some are thin and fast, others are feature-rich. But all hypervisors share this core model: mediate hardware access, enforce isolation, and emulate hardware.

The hypervisor itself runs at a privilege level above normal Guest OS kernels. On Type 1 hypervisors (running bare metal), the hypervisor acts like the OS. On Type 2 hypervisors (running on Host OS), the hypervisor is an application with special privileges.

Without the hypervisor's isolation and emulation, virtualization wouldn't be possible. The hypervisor is what allows dozens of Guest OSs to safely run on a single physical machine without interfering with each other.

## Links
- [[Virtual Machine emulates complete physical computer in software]]
- [[Guest OS communicates with emulated hardware through hypervisor intercepts]]
- [[Hypervisor Type 1 runs on bare metal while Type 2 runs on Host OS]]
- [[VMs & Containers MOC]]
