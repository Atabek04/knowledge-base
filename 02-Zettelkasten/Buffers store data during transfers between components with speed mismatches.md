---
created: 2026-01-06
tags: [os/kernel]
sr-due: 2026-01-09
sr-interval: 1
sr-ease: 2.3
---

A **buffer** is temporary storage in RAM that holds data while being transferred between two components with different speeds. Buffers decouple producers (fast sources) from consumers (slow destinations) by holding data in fast storage until the slower component is ready.

The fundamental problem buffers solve: disk is ~100,000x slower than RAM. Without buffers, the CPU would spend almost all time waiting for disk.

**Without buffer:**
```
CPU reads 1 byte → CPU waits 0.1ms for disk
→ CPU processes 0.00001ms → CPU waits 0.1ms again
→ CPU is idle 99.99% of the time
```

**With buffer:**
```
Disk reads 4KB chunk into RAM buffer (0.4ms)
→ CPU reads from fast RAM (0.00001ms per byte)
→ While CPU processes, disk reads next chunk
→ CPU is busy 99.9% of the time
```

Buffers exist at many boundaries where speed mismatches occur. The concept applies wherever a **producer** (creates data at one rate) and **consumer** (processes data at different rate) interact:

| From → To | Buffer Purpose |
|-----------|---|
| Disk → RAM | Collect file chunks so CPU doesn't wait for slow disk reads |
| RAM → Disk | Batch file writes together (more efficient than individual bytes) |
| Network → RAM | Hold incoming packets until application is ready to process |
| RAM → Network | Hold outgoing data until network is ready to transmit |
| Keyboard → RAM | Hold keystrokes until application reads them |

**Concrete example in C:**

```c
char buffer[1024];                    // you allocate storage in RAM
int bytes = read(fd, buffer, 1024);   // kernel fills this with file data
// Process the 1024 bytes quickly from fast RAM
```

When you call `read()`, the kernel reads 1024 bytes from disk into your buffer in RAM. You then process those bytes at CPU speed. While you process, the kernel can read the next 1024 bytes. This parallelism keeps both disk and CPU busy.

The buffer is the temporary storage area. It sits between the slow disk and the fast CPU, absorbing the speed difference. This principle applies to any producer-consumer pattern—printing queues, network packets, video frames, audio samples.

## Links
- [[RAM is volatile fast storage while disk is persistent slow storage]]
- [[System calls provide the bridge from user programs to kernel services]]
- [[CPU mode switch transitions from User Mode to Kernel Mode during syscalls]]
- [[VMs & Containers MOC]]
