---
created: 2026-01-06
tags: [moc]
---

Understanding how modern systems run multiple applications through virtualization (VMs) and containerization (containers). Both achieve isolation and resource management but use fundamentally different approaches—VMs emulate complete hardware, containers share the kernel.

## Part 1 — OS Fundamentals

Foundation concepts about how operating systems manage resources, enforce isolation, and provide services to applications.

### Kernel & System Architecture

- [[Kernel is the core OS program with complete control over system]] — first program loaded after bootloader, stays in memory
- [[User Space and Kernel Space represent two CPU privilege modes]] — restricted vs unrestricted hardware access
- [[System calls provide the bridge from user programs to kernel services]] — only legal way to request kernel operations
- [[CPU mode switch transitions from User Mode to Kernel Mode during syscalls]] — trap mechanism triggered by privileged requests

### Memory & Data Transfer

- [[RAM is volatile fast storage while disk is persistent slow storage]] — speed and persistence tradeoff
- [[Buffers store data during transfers between components with speed mismatches]] — temporary storage decouples producer/consumer speeds

## Part 2 — Virtualization & VMs

Technology enabling multiple isolated operating systems on single physical hardware. Each VM has complete Guest OS, making them resource-heavy but strongly isolated.

### Core Virtualization Concepts

- [[Virtualization solves hardware underutilization and application isolation problems]] — consolidates multiple workloads on one server
- [[Virtual Machine emulates complete physical computer in software]] — virtual CPU, RAM, disk, network card
- [[Guest OS runs inside VM while Host OS runs on physical hardware]] — two-tier operating system architecture
- [[Hypervisor creates and manages virtual machines by dividing physical resources]] — software layer that tricks Guest OS into thinking it owns hardware

### Hypervisor Architecture

- [[Hypervisor Type 1 runs on bare metal while Type 2 runs on Host OS]] — direct vs hosted architecture
- [[Type 1 hypervisor is faster due to direct hardware access]] — fewer software layers means less overhead
- [[Guest OS communicates with emulated hardware through hypervisor intercepts]] — hypervisor software pretends to be physical hardware

### VM Architecture Layers

- [[VM architecture layers from hardware through Guest OS to applications]] — server → Host OS → hypervisor → Guest OS → bins/libs → app
- [[Each VM carries full Guest OS making it resource-heavy]] — each VM runs complete OS kernel consuming GBs of RAM

## Part 3 — Containerization

Lightweight isolation technology using shared kernel instead of full operating systems. Containers use two Linux features—namespaces and cgroups—for security and resource management.

### Core Container Concepts

- [[Containerization solves VM heaviness by sharing the Host OS kernel]] — isolation without duplicate kernels and OS overhead
- [[Containers share kernel but isolate everything above it]] — single shared kernel, multiple isolated application environments

### Linux Isolation Primitives

- [[Namespaces isolate what container processes can see]] — six types (PID, NET, MNT, UTS, USER, IPC) control visibility
- [[PID namespace makes container think it owns process tree]] — kernel maintains two PID numbers for each process
- [[NET namespace gives each container isolated network stack]] — own IP addresses, ports, routing table
- [[Virtual network interfaces are software-emulated NICs]] — kernel simulates hardware without physical device
- [[Docker bridge connects container networks to host NIC]] — virtual switch routes container traffic to outside world
- [[Cgroups limit how many resources container processes can consume]] — control CPU, memory, disk I/O, network bandwidth
- [[Namespaces provide isolation while cgroups provide resource fairness]] — visibility boundary vs usage limits

### Not Yet Covered

- Container Engine (Docker daemon) — how containers are created, started, and managed
- Container architecture layer-by-layer — detailed layer structure and comparison with VMs
- Container images and layering — how images are built and stored
- Container runtime — low-level execution (runc, containerd)

## Part 4 — Comparison & Decision Making

*Content not yet developed*

### Planning Topics

- Key differences between VMs and containers — isolation level, performance, startup time, resource overhead
- When to use VMs — strong isolation, different OS kernels, legacy applications, full OS control
- When to use Containers — microservices, rapid scaling, development parity, resource efficiency
- Hybrid approaches — containers inside VMs, serverless containers

## Related MOCs

- [[Linux MOC]] — OS fundamentals, kernel architecture, Unix/Linux history
- [[DevOps MOC]] — infrastructure, deployment, orchestration

## Practice

(Flashcards to be added after atomic notes complete)

## External Resources

- [Docker Documentation](https://docs.docker.com/)
- [Linux Namespaces man pages](https://man7.org/linux/man-pages/man7/namespaces.7.html)
- [Linux Cgroups Documentation](https://www.kernel.org/doc/Documentation/cgroup-v1/cgroups.txt)
- [KVM (Kernel-based Virtual Machine)](https://www.linux-kvm.org/)
