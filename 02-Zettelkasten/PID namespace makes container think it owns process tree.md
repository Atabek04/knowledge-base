---
created: 2026-01-06
tags: [virtualization/containers]
sr-due: 2026-01-09
sr-interval: 1
sr-ease: 2.3
---

The **PID (Process ID) namespace** isolates the process tree so each container believes it owns all processes in the system, starting from PID 1.

**How It Works:**

The kernel maintains two different PID numbers for the same process:

- **Host PID** — the PID visible to the host system
- **Container PID** — the PID visible inside the container's PID namespace

```yaml
Kernel's Internal Tracking:
┌─────────────────────────────────┐
│ Process: nginx                  │
│ Host PID: 567                   │ ← visible on host
│ Container PID: 1                │ ← visible in container
│ Belongs to: PID namespace #42   │
└─────────────────────────────────┘
```

When the container asks the kernel "what's my PID," the kernel returns 1. When the host asks "what processes are running," the kernel returns the host PIDs.

**Container Isolation:**

The container cannot see or interact with processes outside its namespace. If a container tries to:
- Kill PID 568 (a host process outside the namespace)
- Send signal to PID 234 (another container process)
- List processes with `ps` command

The kernel refuses because those PIDs don't exist in the container's namespace. The container only sees PID 1 (itself).

**Process Tree Isolation:**

Inside container A, `ps` command shows:

```
PID    COMMAND
1      nginx
2      bash
```

On the host, `ps` shows:

```
PID    COMMAND
567    nginx (container A)
568    bash (container A)
1      init
234    nginx (container B)
...
```

Same processes, but completely different PIDs. The containers don't know about each other's existence because they have separate PID namespaces.

**Why PID 1 Matters:**

In Unix systems, PID 1 is special—it's the init process that starts all others and handles zombie processes. When a container is created, the first process runs as PID 1 inside the container. This allows the container to behave like a minimal operating system.

When the container's PID 1 (the main application) exits, the entire container stops. The host OS doesn't care—it just sees PID 567 exiting. But inside the container, the entire "system" terminated.

**Parent-Child Relationships:**

PID namespace doesn't work through parent-child filtering. Instead, the kernel translates between address spaces. When a process calls `fork()` or `exec()`, the kernel:

1. Creates/loads process as normal
2. Assigns host PID (visible on host)
3. Assigns container PID (visible in namespace)
4. Returns container PID to the process

The process never knows its host PID—the kernel hides this detail.

## Links
- [[Namespaces isolate what container processes can see]]
- [[Cgroups limit how many resources container processes can consume]]
- [[Kernel is the core OS program with complete control over system]]
- [[VMs & Containers MOC]]
