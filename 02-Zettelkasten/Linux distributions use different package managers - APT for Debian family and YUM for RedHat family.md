---
created: 2026-01-20
tags: [linux/package-management]
---

Different **Linux distributions** use different **package managers** because they have different design philosophies and package formats. The two dominant families each have their own package management systems.

**Debian Family Distributions** (Ubuntu, Linux Mint, etc.) use:
- **APT** (Advanced Package Tool) — modern, user-friendly package manager
- **apt-get** — older command-line interface for APT (still functional but less user-friendly)
- Uses `.deb` package format

**Red Hat Family Distributions** (RHEL, CentOS, Fedora, etc.) use:
- **YUM** (Yellowdog Updater, Modified) — package manager for older systems
- **DNF** (Dandified YUM) — newer replacement for YUM on modern Red Hat systems
- Uses `.rpm` package format

This diversity exists because the distributions evolved independently and developed different technical approaches to package management. Understanding your distribution's package manager is essential for system administration, as the commands and workflows differ between families.

## Links

- [[Linux MOC]] — Linux operating system fundamentals
- [[Package managers automate software installation by resolving dependencies and managing file locations]]
- [[apt is more user-friendly than apt-get with progress bars and organized commands]]
