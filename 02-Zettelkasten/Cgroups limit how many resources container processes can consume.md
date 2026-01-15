---
created: 2026-01-06
tags: [virtualization/containers]
sr-due: 2026-01-09
sr-interval: 1
sr-ease: 2.3
---

**Cgroups** (Control Groups) are a Linux kernel feature that enforces resource limits on processes. While namespaces control what processes can *see*, cgroups control what resources processes can *use*.

Cgroups prevent one container from monopolizing host resources and crashing everything. Without cgroups, a single runaway container could consume all RAM and CPU, making the host unusable.

**What Resources Can Cgroups Limit?**

| Resource | Example Limit | Effect |
|----------|---|---|
| **CPU** | 50% of one core | Process gets maximum CPU time, cannot use more |
| **Memory** | 512 MB | Process cannot allocate more RAM, gets killed if exceeded |
| **Disk I/O** | 10 MB/s read | Disk reads throttled to maximum speed |
| **Network** | 1 Mbps bandwidth | Network speed capped, excess packets dropped |

**CPU Limiting Example:**

Container A with CPU limit of 50%:

```
Container A process runs → CPU scheduler limits it
If container tries to use >50% CPU, scheduler throttles it
Container gets time slices: Run 50ms, pause 50ms, run 50ms...
Result: Container uses exactly 50% CPU, never more
```

The process doesn't know it's being throttled—it just observes it's getting less CPU time. The kernel enforces the limit transparently.

**Memory Limiting Example:**

Container B with memory limit of 512MB:

```
Container allocates memory → Kernel tracks usage
Allocation 1: 100MB (OK, total 100MB)
Allocation 2: 200MB (OK, total 300MB)
Allocation 3: 300MB (Limit exceeded! 300+300=600MB > 512MB limit)
Kernel kills the process or denies the allocation
```

Memory limits are hard boundaries. Process cannot exceed the limit (Linux kills it if attempted).

**Cgroups vs Namespaces:**

| Feature | Namespaces | Cgroups |
|---------|-----------|---------|
| **What they control** | Visibility (can't *see*) | Resource usage (can't *use*) |
| **Purpose** | Security isolation | Resource fairness |
| **Enforcement** | Hide resources | Limit resources |
| **If violated** | Process unaware | Kernel kills process |

Namespaces prevent information leakage. Cgroups prevent resource starvation.

**Real-World Scenario:**

Imagine two containers on host with 4GB RAM:

Without cgroups:
```
Container A starts and allocates 3.5GB
Container B starts and tries to allocate 1GB
Kernel: Only 0.5GB available, cannot allocate
Container B crashes or hangs
Host becomes unstable
```

With cgroups:
```
Container A: limit 2GB
Container B: limit 2GB

Container A allocates 1.9GB (OK, under limit)
Container B allocates 1.9GB (OK, under limit)
Total: 3.8GB used (within available 4GB)
Both containers run stably
```

**Cgroup Hierarchy:**

Cgroups are organized hierarchically. You can create nested cgroups:

```
/ (root)
├── docker
│   ├── container1 (limit: 2GB, 50% CPU)
│   └── container2 (limit: 1GB, 25% CPU)
└── kubernetes
    ├── pod1
    └── pod2
```

Different applications (Docker, Kubernetes) manage their own cgroup hierarchies while the kernel enforces all limits.

## Links
- [[Namespaces provide isolation while cgroups provide resource fairness]]
- [[Containerization solves VM heaviness by sharing the Host OS kernel]]
- [[Namespaces isolate what container processes can see]]
- [[VMs & Containers MOC]]
