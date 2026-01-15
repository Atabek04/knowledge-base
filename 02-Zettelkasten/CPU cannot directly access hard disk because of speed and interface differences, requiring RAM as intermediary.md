---
created: 2026-01-12
tags: [linux/memory]
---

The CPU cannot access the hard disk directly due to hardware architecture, speed mismatches, and addressing differences.

RAM acts as the necessary intermediary between CPU and disk.

## Hardware architecture limitation

The CPU has a **direct electrical connection** to RAM integrated on the motherboard.

The hard disk is an **external device** connected via SATA or NVMe cable.

The CPU can only execute instructions from local memory addresses, not from remote devices.

## Speed mismatch

The CPU operates at **nanosecond** speeds (billionths of a second).

Hard disks operate at **millisecond** speeds (thousandths of a second).

This represents a 10 million times speed difference — the CPU would wait forever if it accessed disk directly.

## Memory-mapped execution

The CPU expects code and data at specific **memory addresses** like 0x1000 or 0x2000.

Hard disks use **sectors and blocks** instead of memory addresses.

The CPU cannot understand the disk's block structure directly.

## How RAM bridges the gap

**CPU requests data** — the CPU asks the OS for file X.

**OS loads disk to RAM** — the OS copies data from disk into RAM at specific memory addresses.

**CPU accesses RAM** — the CPU performs instant read/write operations at those RAM addresses.

**RAM translates** — RAM converts disk blocks into addressable memory that the CPU understands.

## Links

- [[RAM provides fast temporary storage while hard disk provides large persistent storage]]
- [[Buffers store data during transfers between components with speed mismatches]]
- [[Memory swapping extends RAM by moving unused data to hard disk when RAM is full]]
- [[Linux MOC]]
