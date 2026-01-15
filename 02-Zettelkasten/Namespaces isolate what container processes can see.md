---
created: 2026-01-06
tags: [virtualization/containers]
sr-due: 2026-01-09
sr-interval: 1
sr-ease: 2.3
---

**Namespaces** are a Linux kernel feature that isolates system resources so that processes have different views of the same system. Each namespace creates an illusion that a process has its own private instance of a resource.

When you create a container, the kernel creates multiple namespaces simultaneously. Each namespace type isolates a different aspect of the system. The container process lives inside all these namespaces together.

**Six Namespace Types:**

| Namespace | Type | Isolates |
|-----------|------|----------|
| **PID** | Process | Container sees only its own processes (starting from PID 1) |
| **NET** | Network | Container has own network stack, IP, ports, routing |
| **MNT** | Mount | Container has own filesystem view and mount points |
| **UTS** | Unix Timesharing | Container has own hostname and domain name |
| **USER** | User ID | Container root user ≠ host root user |
| **IPC** | Interprocess Communication | Container has own message queues and shared memory |

**Concrete Example: PID Namespace**

On the host system, many processes run:

```
PID 1 (init)
PID 234 (nginx)
PID 567 (container's main process)
PID 568 (another host process)
```

From the perspective of the container (inside PID namespace), it sees:

```
PID 1 (its own main process, kernel reassigns it)
```

The container cannot see the other processes. It cannot send signals to them, cannot access their memory, cannot even know they exist. From inside the container, the process is PID 1 (alone in the system).

The kernel maintains this illusion by:

1. Assigning the container process a **host PID** (567 in this example)
2. Assigning it a **container PID** (1 in its own namespace)
3. When container asks "what's my PID," returning the container PID
4. When container lists processes, returning only processes in its namespace

The **same process** appears as PID 567 on the host and PID 1 inside the container.

**Namespace Independence**

Each namespace type is independent. You could have:
- Container A: isolated PID and NET, but shared filesystem (MNT)
- Container B: isolated PID, NET, MNT but different user context (USER)

However, containers typically use all six namespaces together for complete isolation. The six types work as layers of isolation:

```
Container A = PID namespace #42 + NET namespace #43 + MNT namespace #44 + UTS namespace #45 + USER namespace #46 + IPC namespace #47
```

Toggling a namespace on/off controls that particular isolation layer.

## Links
- [[PID namespace makes container think it owns process tree]]
- [[NET namespace gives each container isolated network stack]]
- [[Virtual network interfaces are software-emulated NICs]]
- [[Namespaces provide isolation while cgroups provide resource fairness]]
- [[Containers share kernel but isolate everything above it]]
- [[VMs & Containers MOC]]
