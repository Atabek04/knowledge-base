---
created: 2026-01-12
tags: [linux/fundamentals]
---

Operating systems prevent applications from accessing hardware directly for several critical reasons.

## Security isolation

Malicious applications cannot corrupt disk data, steal information, or damage hardware.

The OS validates all hardware requests before execution.

## Hardware abstraction

The OS provides a unified interface so applications don't need device-specific code.

Applications call standard system calls like `read()` instead of implementing driver code for each disk model.

## Privilege control

Only the OS can execute privileged operations like I/O, memory management, and interrupt handling.

Applications run in restricted user mode without hardware access permissions.

## Resource coordination

The OS prevents conflicts when multiple applications compete for the same resources.

Two applications cannot write to the same disk sector simultaneously or bind to the same network port.

## Reliability

An application crash doesn't crash the entire system.

The OS manages fault isolation between processes.

## Driver updates

Hardware vendors can update drivers without requiring applications to recompile.

The standard OS interface remains stable while underlying hardware implementations change.

## Links

- [[Kernel is the core OS program with complete control over system]]
- [[Applications communicate with operating system through system calls]]
- [[User Space and Kernel Space represent two CPU privilege modes]]
- [[Operating system mediates between applications and hardware for security and abstraction]]
- [[Linux MOC]]
