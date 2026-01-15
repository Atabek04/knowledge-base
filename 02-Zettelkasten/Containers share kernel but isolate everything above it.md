---
created: 2026-01-06
tags: [virtualization/containers]
sr-due: 2026-01-09
sr-interval: 1
sr-ease: 2.3
---

The core idea of containerization is fundamentally different from virtualization. Instead of emulating hardware and running multiple Guest OSs, containers share a single Host OS kernel while isolating application environments.

**No Guest OS Layer**

Unlike VMs (which require a complete Guest OS), containers eliminate the Guest OS entirely. Containers run directly on the Host OS kernel—the same kernel that runs the host system itself.

**Shared Kernel Benefits:**

- No OS startup overhead (kernel already running)
- No redundant OS instances (one kernel manages all containers)
- Minimal resource consumption (containers add only application + libraries, not a full OS)
- Fast startup (milliseconds instead of minutes)

**Isolation Mechanism**

Isolation in containers comes from two Linux kernel features, not from emulated hardware:

1. **Namespaces** — provide visibility isolation (what can the process *see*)
2. **Cgroups** — provide resource isolation (what can the process *use*)

From a container's perspective, it appears to own:
- Its own process tree (PID namespace)
- Its own network stack (NET namespace)
- Its own filesystem (MNT namespace)
- Its own hostname (UTS namespace)
- Its own user IDs (USER namespace)
- Its own IPC primitives (IPC namespace)

But in reality, all containers share the same kernel that manages these isolated views.

![[container-architecture.png]]

**Comparison to VMs:**

```
VM Architecture:
App → Bins/Libs → Guest OS kernel → Hypervisor → Host OS kernel → Hardware

Container Architecture:
App → Bins/Libs → (Host OS kernel directly, isolated via namespaces)
```

Containers have one fewer layer of abstraction. They access the kernel directly through namespaces instead of going through the Guest OS abstraction layer.

**Trade-off: Weaker Isolation for Efficiency**

Containers cannot run a different OS kernel. You cannot run Windows kernel in a Linux container. All containers must share the same host kernel.

This is acceptable for most cloud workloads (containers run Linux on Linux, not different OSs). The efficiency gain is worth the isolation trade-off.

## Links
- [[Containerization solves VM heaviness by sharing the Host OS kernel]]
- [[Namespaces isolate what container processes can see]]
- [[Cgroups limit how many resources container processes can consume]]
- [[VM architecture layers from hardware through Guest OS to applications]]
- [[VMs & Containers MOC]]
