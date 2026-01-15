---
created: 2026-01-12
tags: [linux/interface]
---

**GUI** (Graphical User Interface) and **CLI** (Command Line Interface) are both applications, not kernel components.

They mediate between users and the kernel by translating user actions into system calls.

## What they are

**GUI** — visual interface with windows, buttons, and icons operated by mouse and keyboard.

Examples include GNOME, KDE, and Windows Explorer.

**CLI** — text-based interface operated by typing commands with keyboard only.

Examples include Bash shell and Terminal.

## How they communicate with kernel

```
User action → Application (GUI/CLI) → System call → Kernel → Hardware
```

**GUI example:** User clicks "Delete" button → GUI application calls `unlink()` system call → kernel deletes the file.

**CLI example:** User types `rm file` command → shell calls `unlink()` system call → kernel deletes the file.

Both interfaces perform identical operations at the kernel level — they just present different user experiences.

## Key differences

| Aspect | GUI | CLI |
|--------|-----|-----|
| Interface | Visual, graphical | Text-based commands |
| Speed | Slower (mouse movements) | Faster (keyboard shortcuts) |
| Resource use | High (rendering graphics) | Minimal |
| Learning curve | Intuitive | Steep |

## Server vs desktop usage

**Desktop OS** — includes GUI which consumes more RAM and CPU for rendering.

**Server OS** — typically CLI only via SSH for minimal overhead and maximum performance.

Servers skip the GUI to dedicate resources to actual server work like web serving and databases.

## Links

- [[Applications communicate with operating system through system calls]]
- [[Kernel is the core OS program with complete control over system]]
- [[Linux terminal prompt shows username, hostname, current directory, and user privilege level]]
- [[Linux MOC]]
