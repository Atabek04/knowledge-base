---
created: 2026-01-20
tags: [linux/package-management]
---

A **software repository** is a centralized server or storage location that contains thousands of pre-packaged applications ready for installation by a **package manager**.

**Repositories** serve as the source from which package managers download software. When you run `sudo apt install packagename`, your package manager queries repositories to find, download, and install that package along with its dependencies.

Before installing or upgrading packages through a package manager, you should always update your local **package index** with the command `sudo apt update`. This command:
- Pulls the latest package information from configured repositories
- Updates your local database (the **package index**) with available packages and their versions
- Ensures the package manager knows about the latest versions and security updates

If you skip this step, your package manager may try to install outdated versions or fail to find recently added packages. The package index essentially acts as a local cache of the repository's contents, allowing quick lookups without querying the remote servers for every operation.

## Links

- [[Linux MOC]] — Linux operating system fundamentals
- [[Package managers automate software installation by resolving dependencies and managing file locations]]
