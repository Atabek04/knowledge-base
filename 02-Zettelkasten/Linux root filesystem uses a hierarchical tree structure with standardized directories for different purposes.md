---
created: 2026-01-12
tags: [linux/filesystem]
---

Linux uses the **Filesystem Hierarchy Standard (FHS)** which defines a standardized directory layout.

Each directory serves a specific purpose, making the system organized across all Linux distributions.

## Main directories

| Directory | Name means | Purpose |
|-----------|-----------|---------|
| `/bin` | Binary | Essential user commands (`ls`, `cat`, `grep`) |
| `/sbin` | System Binary | System administration commands (`fsck`, `mount`) |
| `/etc` | Et Cetera | System configuration files (`passwd`, `hosts`) |
| `/home` | Home | User home directories (`/home/john/`) |
| `/root` | Root user | Root user's home directory |
| `/tmp` | Temporary | Temporary files (auto-cleaned) |
| `/var` | Variable | Variable/changing data (logs, cache) |
| `/usr` | User programs | User applications and libraries |
| `/lib` | Library | Shared code libraries (`libc.so.6`) |
| `/boot` | Boot files | Kernel and bootloader |
| `/dev` | Device | Hardware device interfaces (`/dev/sda`) |
| `/proc` | Process | Process and kernel info (virtual) |
| `/sys` | System | System and hardware info (virtual) |
| `/opt` | Optional | Optional third-party software |
| `/srv` | Service | Service data (web server files) |

## Directory categories

**Essential for boot:**
- `/boot` — kernel files
- `/etc` — system configuration
- `/lib` — shared libraries

**User/program data:**
- `/home` — user files
- `/usr` — installed programs
- `/opt` — third-party software

**System runtime:**
- `/var` — logs, caches, databases
- `/tmp` — temporary workspace

**Virtual (kernel interface):**
- `/proc` — process information
- `/sys` — hardware/driver information
- `/dev` — device files

## Key insight

Every directory has a specific purpose revealed by its name.

This organization keeps the system consistent across all Linux distributions.

## Links

- [[Kernel is the core OS program with complete control over system]]
- [[Linux is the kernel while Linux distributions package the kernel with tools and utilities]]
- [[Linux MOC]]
