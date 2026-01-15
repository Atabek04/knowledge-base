---
created: 2026-01-12
tags: [linux/fundamentals]
---

**Linux** refers specifically to the kernel created by Linus Torvalds.

A **Linux distribution** (distro) is a complete operating system that packages the Linux kernel with tools, utilities, and applications.

## Linux kernel

**Created by:** Linus Torvalds in 1991.

**What it does:** Manages CPU, memory, disk, and network devices. Schedules processes and allocates resources.

**Size:** Approximately 30 million lines of code.

**License:** Open source under GPL.

**What it is NOT:** Not a complete operating system, not an application — just the core manager.

## Linux distribution

A complete OS that includes multiple components:

```
Distribution = Linux kernel + utilities + tools + package manager + shell + desktop + apps
```

**Components:**

**Kernel** — Linux (same across most distros).

**Package manager** — APT (Ubuntu), YUM (CentOS), DNF (Fedora).

**Shell** — Bash command interpreter.

**System utilities** — file tools, network tools, permission management.

**Libraries** — shared code like glibc.

**Desktop environment** — GNOME, KDE, Cinnamon (optional GUI).

**Applications** — text editor, file manager, browser.

## Common distributions

| Distribution | Package Manager | Base | Use case |
|--------------|-----------------|------|----------|
| Ubuntu | APT | Debian | Desktop/Server, beginner-friendly |
| Linux Mint | APT | Debian | Desktop, lightweight |
| CentOS | YUM | RedHat | Enterprise, servers |
| Fedora | DNF | RedHat | Cutting-edge, developers |
| Arch | Pacman | Independent | Minimal, advanced users |

Different distributions share the same Linux kernel but differ in package managers, tools, and philosophy.

## Analogy

**Linux kernel** = car engine (same in all cars).

**Ubuntu distribution** = Toyota car (engine + steering + dashboard + features).

**CentOS distribution** = Honda car (same engine, different features).

Different cars, same engine.

## Links

- [[Kernel is the core OS program with complete control over system]]
- [[Linus Torvalds created Linux in 1991 as an open-source alternative to proprietary Minix]]
- [[Unix is a foundational operating system created in 1969 that influenced modern operating system design]]
- [[Linux MOC]]
