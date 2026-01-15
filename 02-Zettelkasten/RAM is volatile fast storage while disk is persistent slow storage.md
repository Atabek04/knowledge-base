---
created: 2026-01-06
tags: [os/kernel]
sr-due: 2026-01-09
sr-interval: 1
sr-ease: 2.3
---

Computer systems have two types of storage with fundamentally different characteristics—**RAM (primary memory)** and **Disk/SSD (secondary storage)**. Understanding this difference is crucial for understanding buffers, caching, and why the kernel exists.

**RAM (Random Access Memory)** is volatile—all data is lost when power turns off. However, RAM is extremely fast. The CPU can access RAM in nanoseconds and directly perform operations on data in RAM.

**Disk or SSD (secondary storage)** is persistent—data survives power shutdown indefinitely. But disk is vastly slower than RAM. Reading from disk takes milliseconds (millions of times slower than RAM).

| Characteristic | RAM | Disk/SSD |
|---|---|---|
| **Volatility** | Volatile (lost on power off) | Persistent (survives forever) |
| **Speed** | Nanoseconds | Milliseconds (10^6 times slower) |
| **Cost** | Expensive per GB | Cheap per GB |
| **Capacity** | Small (8-64 GB typical) | Large (256 GB - TBs typical) |
| **CPU Access** | CPU can directly access | CPU cannot directly access |
| **Use Case** | Running programs and data | Permanent storage |

The CPU cannot directly access disk at all. To read a file from disk, the CPU must ask the kernel, which uses **device drivers** to communicate with the disk hardware. The kernel then copies data from disk into RAM, and finally the CPU accesses it from RAM.

This two-level storage hierarchy is why **buffers** exist. If the CPU read one byte at a time from disk, it would spend 99.9% of time waiting for disk. Instead, buffers hold chunks of data in fast RAM, allowing the CPU to work with fast storage while eventual persistence on slow disk is handled in the background.

## Links
- [[Buffers store data during transfers between components with speed mismatches]]
- [[Kernel is the core OS program with complete control over system]]
- [[System calls provide the bridge from user programs to kernel services]]
- [[VMs & Containers MOC]]
