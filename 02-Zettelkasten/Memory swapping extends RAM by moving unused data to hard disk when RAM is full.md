---
created: 2026-01-12
tags: [linux/memory]
---

**Swap space** is a reserved area on the hard disk that extends RAM capacity by storing overflow data.

When RAM fills up, the OS moves unused data to disk to free memory for active processes.

## How memory swapping works

**OS identifies idle pages** — memory that hasn't been used recently.

**Writes to swap** — copies that data from RAM to disk swap space.

**Frees RAM** — marks that RAM space as available for new data.

**Marks as "swapped"** — remembers where the data lives on disk.

## When swapped data is needed

**Page fault occurs** — the CPU tries to access memory that's been swapped out.

**OS loads from swap** — reads the data from disk back into RAM.

**Swaps other data** — may push different data to swap to maintain RAM availability.

## Timeline example

```
Time 0s:  RAM: [App A: 3GB] [App B: 2GB] [App C: 2GB] — 7GB/8GB used
Time 5s:  Open video editor (needs 3GB)
          OS swaps App C (2GB) to disk
          RAM: [App A: 3GB] [App B: 2GB] [Video: 3GB]
Time 10s: Switch back to App C
          Page fault → OS loads App C from swap (10ms delay)
```

## Performance cost

| Operation | Speed |
|-----------|-------|
| RAM access | 1 nanosecond |
| Swap access | 10 milliseconds |
| **Slowdown** | **10 million times slower** |

**Excessive swapping** leads to **system thrashing**.

The disk constantly reads and writes while the CPU waits for data.

The computer feels frozen because most time is spent on disk I/O instead of computation.

## When swapping occurs

Too many applications open simultaneously.

Available RAM is less than total process memory demand.

The OS has no choice but to use slower disk storage.

**Solution:** Close applications or add more physical RAM.

## Links

- [[RAM provides fast temporary storage while hard disk provides large persistent storage]]
- [[CPU cannot directly access hard disk because of speed and interface differences, requiring RAM as intermediary]]
- [[Linux MOC]]
