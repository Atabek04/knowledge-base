---
created: 2026-01-12
tags: [linux/memory]
---

**RAM** and **hard disk** serve complementary roles in computer architecture with opposite trade-offs.

RAM offers speed but volatility, while disk offers persistence but slowness.

## The desk and library analogy

**RAM** = your desk (fast access, limited space, loses papers when you leave).

**Hard disk** = library (huge storage, slow retrieval, data persists after closure).

## Why both are needed

**RAM** — the CPU works at the desk instantly to execute code and read data.

**Hard disk** — stores programs and files permanently, surviving power loss.

## How they work together

When you open a program:

**OS fetches from library** — loads program from hard disk.

**Loads to desk** — copies program into RAM.

**CPU executes from desk** — runs the program from RAM.

If the CPU waited for disk on every instruction, the computer would be unusably slow.

## Speed comparison

| Storage | Access speed |
|---------|-------------|
| RAM | ~1 nanosecond (instant) |
| Hard disk | ~10 milliseconds |
| **Difference** | **10 million times slower** |

## Size comparison

| Storage | Typical capacity |
|---------|------------------|
| RAM | 8-16 GB |
| Hard disk | 256 GB - 2 TB (1000x larger) |

The desk is small with limited RAM.

The library is huge with large disk capacity.

## Links

- [[CPU cannot directly access hard disk because of speed and interface differences, requiring RAM as intermediary]]
- [[Memory swapping extends RAM by moving unused data to hard disk when RAM is full]]
- [[Buffers store data during transfers between components with speed mismatches]]
- [[Linux MOC]]
