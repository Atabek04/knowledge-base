---
created: 2026-01-12
tags: [linux/process]
---

**Context switching** enables one CPU core to execute multiple processes by rapidly switching between them.

The OS scheduler decides when to pause the current process and resume another process.

## How context switching works

**OS scheduler decides** time is up for the current process based on scheduling policy.

**Save state** — CPU registers, memory pointers, and program counter are saved to memory.

**Load new state** — the next process's saved state is loaded into the CPU.

**Resume execution** — the new process continues from where it left off.

## Timeline example

```
Time 0ms:   Process A running (0-10ms)
Time 10ms:  Context switch → Process B running (10-20ms)
Time 20ms:  Context switch → Process C running (20-30ms)
Time 30ms:  Context switch → Process A resumes (30-40ms)
```

Three processes share one CPU core, each getting approximately 10ms per turn.

## Performance cost

Context switching is **expensive** in terms of CPU cycles.

The OS must save and load CPU state including registers, cache, and memory pages.

CPU caches get flushed during context switches, leading to slower execution when processes resume.

Too many context switches causes **thrashing** — the CPU spends more time switching than actually executing processes.

## Multi-core advantage

On a 4-core CPU, 4 processes can run in **true parallel** simultaneously.

Remaining processes still use context switching on those cores, but with less contention.

## Links

- [[Process is an instance of a program in execution with isolated memory space and resources]]
- [[Kernel is the core OS program with complete control over system]]
- [[Linux MOC]]
