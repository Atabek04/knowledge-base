---
created: 2026-01-20
tags: [linux/package-management]
---

Software **packages** are compressed archives that bundle all files required by an application, along with metadata about dependencies and installation instructions.

Most applications depend on other libraries and tools to function properly. For example, a Node.js application requires the **Node.js runtime** to execute. When you install software on Linux, all dependencies must be installed first, which can be complex since they aren't always bundled into a single archive.

Traditional software installation is complicated because application files are scattered across different directories: executables go to `/bin`, libraries to `/lib`, configuration to `/etc`, and so on. This fragmentation makes **uninstallation** difficult, as you must remember and remove all files from multiple locations.

**Software packages** solve this problem by:
- Bundling all application files into a single compressed archive
- Including metadata about dependencies and installation instructions
- Automating file distribution to correct system directories
- Enabling clean removal of all related files

## Links

- [[Linux MOC]] — Linux operating system fundamentals
- [[Package managers automate software installation by resolving dependencies and managing file locations]]
