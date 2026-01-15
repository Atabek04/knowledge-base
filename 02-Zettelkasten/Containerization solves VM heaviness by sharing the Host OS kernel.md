---
created: 2026-01-06
tags: [virtualization/containers]
sr-due: 2026-01-09
sr-interval: 1
sr-ease: 2.3
---

Virtualization solved the hardware underutilization problem, but created new problems. Containerization emerged as a solution to these VM-specific limitations.

**VM Problems that Containerization Solves:**

**Heaviness** — Each VM runs a complete OS kernel (500MB-1GB+ RAM per VM). Running 10 VMs means 10 complete OS instances, consuming enormous memory and disk resources.

**Slow Startup** — Starting a VM means booting an entire operating system from scratch. OS initialization, services starting, configuration loading takes minutes. Scaling from 1 to 100 VMs means waiting 100+ minutes total.

**Wasteful Duplication** — 10 VMs = 10 OS kernels all performing the same functions (process scheduling, memory management, device handling, filesystem) with 90% redundancy. This is fundamentally wasteful.

**The Key Question Containers Ask:** Do we really need a separate OS kernel per application? The answer is no.

Containerization takes a different approach: **share the Host OS kernel, but isolate everything above it**.

How do two applications running on the same OS kernel achieve isolation without duplicate kernels?

Using two Linux kernel features:

1. **Namespaces** — create isolated views so processes cannot see each other
2. **Cgroups** — enforce resource limits so processes cannot starve each other

With this approach, 10 containers running 10 applications can share a single OS kernel. The memory saved is dramatic:

- 10 VMs: 10GB+ consumed by OS instances alone
- 10 containers: <100MB consumed by OS (shared kernel), remainder available for applications

Containers start in milliseconds instead of minutes because they don't boot an OS—they just start the application within the already-running kernel.

The isolation is weaker than VMs (both containers share the same kernel), but isolation is still strong enough for most use cases. The efficiency gains make containers the default for modern cloud infrastructure.

## Links
- [[Containers share kernel but isolate everything above it]]
- [[Virtualization solves hardware underutilization and application isolation problems]]
- [[Each VM carries full Guest OS making it resource-heavy]]
- [[VMs & Containers MOC]]
