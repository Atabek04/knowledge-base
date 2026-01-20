---
created: 2026-01-20
tags: [linux/package-management]
---

**Package managers** are system tools that automate software installation by handling dependency resolution, verifying package integrity, and placing files in appropriate system directories.

A **package manager** performs several critical functions:
- **Downloads and installs** software from centralized repositories
- **Resolves dependencies** automatically, ensuring all required libraries are installed first
- **Verifies authenticity and integrity** of packages before installation
- **Knows file system conventions** and places files in correct directories (`/bin`, `/lib`, `/etc`, etc.)
- **Enables easy upgrades** by tracking installed versions
- **Facilitates clean removal** by remembering which files were installed

Each **Linux distribution** has its own package manager tailored to its ecosystem. This diversity arose because different distributions have different philosophies about package structure and system management.

Without a package manager, installing software requires manually downloading all dependencies, extracting files to correct locations, and updating system configuration—a tedious and error-prone process that package managers completely automate.

## Links

- [[Linux MOC]] — Linux operating system fundamentals
- [[Software packages bundle application files and metadata into compressed archives for distribution]]
- [[Linux distributions use different package managers - APT for Debian family and YUM for RedHat family]]
