---
created: 2026-01-06
tags: [moc]
---

Understanding how modern systems run multiple applications through virtualization (VMs) and containerization (containers). Both achieve isolation and resource management but use fundamentally different approaches—VMs emulate complete hardware, containers share the kernel.

## Part 1 — OS Fundamentals

Foundation concepts about how operating systems manage resources, enforce isolation, and provide services to applications.

### Kernel & System Architecture

- [[Kernel is the core OS program with complete control over system|Kernel: core OS program with total control]]
- [[User Space and Kernel Space represent two CPU privilege modes|User space vs kernel space: two privilege modes]]
- [[System calls provide the bridge from user programs to kernel services|System calls: the only path to kernel services]]
- [[CPU mode switch transitions from User Mode to Kernel Mode during syscalls|Mode switch: user → kernel on a syscall (trap)]]

### Memory & Data Transfer

- [[RAM is volatile fast storage while disk is persistent slow storage|RAM: volatile/fast; disk: persistent/slow]]
- [[Buffers store data during transfers between components with speed mismatches|Buffers absorb speed mismatches in transfers]]

## Part 2 — Virtualization & VMs

Technology enabling multiple isolated operating systems on single physical hardware. Each VM has complete Guest OS, making them resource-heavy but strongly isolated.

### Core Virtualization Concepts

- [[Virtualization solves hardware underutilization and application isolation problems|Virtualization: utilization + isolation]]
- [[Virtual Machine emulates complete physical computer in software|VM emulates a whole computer in software]]
- [[Guest OS runs inside VM while Host OS runs on physical hardware|Guest OS in the VM, Host OS on hardware]]
- [[Hypervisor creates and manages virtual machines by dividing physical resources|Hypervisor divides hardware among VMs]]

### Hypervisor Architecture

- [[Hypervisor Type 1 runs on bare metal while Type 2 runs on Host OS|Type 1 on bare metal, Type 2 on a host OS]]
- [[Type 1 hypervisor is faster due to direct hardware access|Type 1 is faster: direct hardware access]]
- [[Guest OS communicates with emulated hardware through hypervisor intercepts|Guest OS hits emulated hardware via the hypervisor]]

### VM Architecture Layers

- [[VM architecture layers from hardware through Guest OS to applications|VM stack: hardware → host → hypervisor → guest → app]]
- [[Each VM carries full Guest OS making it resource-heavy|Each VM ships a full OS → heavy]]

## Part 3 — Containerization

Lightweight isolation technology using shared kernel instead of full operating systems. Containers use two Linux features—namespaces and cgroups—for security and resource management.

### Core Container Concepts

- [[Containerization solves VM heaviness by sharing the Host OS kernel|Containers share the host kernel (lighter than VMs)]]
- [[Containers share kernel but isolate everything above it|Containers share the kernel, isolate above it]]

### Linux Isolation Primitives

- [[Namespaces isolate what container processes can see|Namespaces isolate what a container sees (PID, NET, …)]]
- [[PID namespace makes container think it owns process tree|PID namespace: container owns its process tree]]
- [[NET namespace gives each container isolated network stack|NET namespace: isolated network stack]]
- [[Virtual network interfaces are software-emulated NICs|Virtual NICs are software-emulated]]
- [[Docker bridge connects container networks to host NIC|Docker bridge links container nets to the host NIC]]
- [[Cgroups limit how many resources container processes can consume|Cgroups cap container resource use]]
- [[Namespaces provide isolation while cgroups provide resource fairness|Namespaces isolate; cgroups ration]]

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
