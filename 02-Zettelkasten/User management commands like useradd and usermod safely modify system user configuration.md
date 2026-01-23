---
created: 2026-01-20
tags: [linux/user-management]
---

**User management commands** provide safe, automated methods for creating, modifying, and deleting user accounts without risking system corruption from manual editing.

**Why Not Edit `/etc/passwd` Directly?**
- Manual editing is **error-prone** — a single syntax error breaks the authentication system
- **Multiple files must stay synchronized** — changes to `/etc/passwd` must match updates to `/etc/shadow` and `/etc/group`
- Dedicated commands handle this synchronization automatically and safely

**Common User Management Operations**

**Add New User**
```bash
sudo useradd username              # minimal user creation
sudo useradd -m -s /bin/bash username  # with home dir and shell
sudo adduser username              # interactive (Debian/Ubuntu)
```

**Set or Change Password**
```bash
sudo passwd username
```

**Modify User Properties**
```bash
sudo usermod -aG groupname username  # add secondary group
sudo usermod -g groupname username   # change primary group
sudo usermod -s /bin/zsh username    # change login shell
```

**Delete User**
```bash
sudo userdel username      # keep home directory
sudo userdel -r username   # remove home directory too
```

**Group Management**
```bash
sudo groupadd groupname     # create group
sudo groupdel groupname     # delete group
groups username             # list user's groups
```

These commands abstract away the complexity of `/etc/` file management. They ensure all related files stay synchronized and prevent typos that could make the system unbootable or locked out.

## Links

- [[Linux MOC]] — Linux operating system fundamentals
- [[etc directory]]
- [[Every Linux user must have exactly one primary group but can have multiple secondary groups]]
