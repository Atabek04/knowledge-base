---
created: 2026-01-12
tags: [linux/fundamentals]
---

The operating system acts as a mediator between applications and hardware, preventing direct communication.

Applications cannot talk directly to hardware because it would create security vulnerabilities, implementation complexity, and resource conflicts.

## Problems with direct hardware access

**Security risk** — malicious applications could corrupt data, steal information, or damage hardware.

**Implementation complexity** — every application would need to implement hardware-specific code for different device models.

**Resource conflicts** — multiple applications accessing the same hardware simultaneously would cause data corruption and crashes.

**No isolation** — one buggy application could crash the entire system.

## OS as mediator

The operating system sits between applications and hardware:

```
Application → OS Kernel → Hardware
```

**Validation** — the OS validates all requests before granting hardware access.

**Coordination** — the OS schedules and serializes hardware access to prevent conflicts.

**Abstraction** — the OS provides standard interfaces so applications don't need device-specific code.

**Protection** — the OS isolates applications from each other and from critical system resources.

## Privilege enforcement

Applications run in **user mode** with restricted permissions.

Only the kernel runs in **kernel mode** with unrestricted hardware access.

Applications must request privileged operations through **system calls**.

The kernel validates each request and executes it on behalf of the application.

## Links

- [[Operating system prevents direct hardware access for security, abstraction, and resource coordination]]
- [[Kernel is the core OS program with complete control over system]]
- [[Applications communicate with operating system through system calls]]
- [[User Space and Kernel Space represent two CPU privilege modes]]
- [[Linux MOC]]
