---
created: 2026-01-06
tags: [virtualization/vms]
sr-due: 2026-01-09
sr-interval: 1
sr-ease: 2.3
---

VM architecture consists of six distinct layers, each with a specific responsibility. Understanding these layers clarifies how virtualization enables multiple isolated operating systems.

**1. Server Layer — Physical Hardware**

The actual physical machine you can touch. Contains real CPU cores, RAM modules, disk drives, network interfaces.

This is the foundation. All virtual machines ultimately rely on this hardware, even though they don't directly access it.

**2. Host OS Layer**

The operating system installed on the physical machine. In Type 1 hypervisors, this might be ESXi (which acts as the OS). In Type 2 hypervisors, this is your regular OS (Windows, Linux, macOS).

The Host OS (or Type 1 hypervisor acting as OS) manages real hardware and ensures fair resource allocation among VMs.

**3. Hypervisor Layer**

The virtualization software that creates and manages virtual machines. In Type 1 setup, hypervisor is the Host OS. In Type 2 setup, hypervisor sits above Host OS as an application.

The hypervisor divides physical resources, isolates VMs, and emulates hardware.

**4. Guest OS Layer**

A complete, fully-functional operating system running inside each VM. Each VM has its own kernel, system processes, and drivers. This Guest OS is completely separate from the Host OS.

**Important:** Each VM has its own independent kernel. VM1 might run Linux kernel 5.10, while VM2 runs Windows kernel 22H2. These kernels run independently without interfering.

**5. Bins/Libs Layer (Binaries and Libraries)**

Executable programs and shared libraries that applications depend on. This includes programming language runtimes (Java, Python, Node), system utilities, and shared libraries.

Each VM has its own isolated copy of binaries and libraries. VM1's Java 8 doesn't conflict with VM2's Java 11 because they're completely separate.

**6. App Layer**

Your actual application code. Each application runs inside a specific VM, using that VM's Guest OS, binaries, and libraries.

**Illustration:**

```
┌─────────────────────────────────────────────────────┐
│ Application 1  │  Application 2  │  Application 3 │
├─────────────────────────────────────────────────────┤
│ Bins/Libs 1    │  Bins/Libs 2    │  Bins/Libs 3   │
├─────────────────────────────────────────────────────┤
│ Guest OS (Linux) │ Guest OS (Win) │ Guest OS (Linux)│
├─────────────────────────────────────────────────────┤
│           Hypervisor Layer                          │
├─────────────────────────────────────────────────────┤
│           Host OS (if Type 2)                       │
├─────────────────────────────────────────────────────┤
│           Physical Hardware                         │
└─────────────────────────────────────────────────────┘
```

The key insight: **each VM carries a complete Guest OS**. This isolation is strong (VMs cannot affect each other) but expensive in resources. Three VMs = three complete operating systems consuming CPU, RAM, and disk space.

This is why [[Containerization solves VM heaviness by sharing the Host OS kernel]]—containers skip the Guest OS layer entirely and share the Host's kernel.

## Links
- [[Kernel is the core OS program with complete control over system]]
- [[Hypervisor creates and manages virtual machines by dividing physical resources]]
- [[Guest OS runs inside VM while Host OS runs on physical hardware]]
- [[Each VM carries full Guest OS making it resource-heavy]]
- [[VMs & Containers MOC]]
