---
created: 2026-01-06
tags: [virtualization/containers]
sr-due: 2026-01-09
sr-interval: 1
sr-ease: 2.3
---

Containers achieve complete isolation through two complementary Linux kernel features: **namespaces** provide isolation boundaries, and **cgroups** provide resource limits. Together, they create secure, fair container environments.

**Namespaces: Isolation Boundaries**

Namespaces control **visibility**—what a process can see. They create virtual boundaries:

- PID namespace: process cannot see other processes
- NET namespace: process cannot see other networks
- MNT namespace: process cannot see other filesystems
- UTS namespace: process has isolated hostname
- USER namespace: process root ≠ system root
- IPC namespace: process cannot see other IPC resources

If Container A tries to access something outside its namespace, the kernel refuses. From Container A's perspective, those resources don't exist.

**Cgroups: Resource Limits**

Cgroups control **consumption**—how much resources a process can use. They enforce limits:

- CPU limit: process cannot use more than allocated CPU time
- Memory limit: process cannot allocate more RAM than allowed
- Disk I/O limit: process cannot read/write faster than allowed
- Network limit: process cannot exceed bandwidth allocation

If Container B tries to allocate memory beyond its limit, the kernel denies the allocation (and may kill the process).

**Why Both Are Necessary:**

| Scenario | Namespace Only | Cgroup Only | Both |
|----------|---|---|---|
| Container A runs `ps` | Won't see other processes ✓ | Sees all processes, can query them ✗ | Can't see, can't query ✓ |
| Container A leaks memory | Still isolated ✓ | Memory leak crashes host ✗ | Capped, doesn't crash host ✓ |
| Container B launches network sniff | Can't see other nets (NET ns) ✓ | Sees all traffic, can sniff ✗ | Isolated network view ✓ |

**Real-World Breakdown:**

Without namespaces (only cgroups):
```
Container A: gets 2GB memory, 50% CPU
Container B: gets 2GB memory, 50% CPU

But: Container A can see Container B's processes
     Container B can see Container A's network traffic
     Container A can interfere with Container B
Result: Weak isolation, security risk
```

Without cgroups (only namespaces):
```
Container A: isolated network, processes, filesystem
Container B: isolated network, processes, filesystem

But: Container A allocates 5GB memory (host only has 4GB)
     Host crashes trying to fulfill allocation
     Container B becomes completely unusable
Result: Good security, bad stability
```

With both (proper containers):
```
Container A: 2GB mem, 50% CPU, isolated everything
Container B: 2GB mem, 50% CPU, isolated everything

Container A cannot see, kill, or interfere with B
Container B cannot consume more than 2GB (gets killed if tried)
Result: Secure isolation + fair resource sharing
```

**Container Runtime Implementation:**

When you run `docker run` or similar, the container engine:

1. **Creates namespaces** — PID, NET, MNT, UTS, USER, IPC
2. **Configures cgroups** — sets memory, CPU, I/O limits
3. **Launches process** — in the new namespace with cgroup limits applied
4. **Process cannot escape** — kernel enforces both boundaries

This combination makes containers simultaneously isolated (can't interfere) and fair (can't starve others).

## Links
- [[Namespaces isolate what container processes can see]]
- [[Cgroups limit how many resources container processes can consume]]
- [[PID namespace makes container think it owns process tree]]
- [[NET namespace gives each container isolated network stack]]
- [[Containerization solves VM heaviness by sharing the Host OS kernel]]
- [[VMs & Containers MOC]]
