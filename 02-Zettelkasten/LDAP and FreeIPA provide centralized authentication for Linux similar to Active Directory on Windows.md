---
created: 2026-01-20
tags: [linux/authentication]
---

**Linux systems** can use **centralized authentication services** similar to **Windows Active Directory**, enabling users to log into any machine with a single credential and accessing network-based home directories.

**Traditional Local Linux Authentication**
- **Local accounts** stored in `/etc/passwd` and `/etc/shadow` on each machine
- Each user gets a **home directory** (`/home/username`) on that specific PC
- Files exist **only on that machine** — not shared across systems
- Suitable for single-user workstations or isolated lab environments

**Centralized Linux Authentication**

**LDAP** (**Lightweight Directory Access Protocol**)
- Centralized **user database** stored on a network server
- All machines query LDAP when users attempt login
- Usernames work on **any LDAP-connected system**

**FreeIPA**
- Complete **identity management solution** for Linux environments
- Combines **LDAP** (user directory) with **Kerberos** (secure authentication)
- Comparable to **Windows Active Directory** but designed for Linux
- Manages users, groups, permissions, and security policies

**Network Home Directories**
- Organizations often use **NFS** (Network File System) with centralized authentication
- User's `/home/username` is actually a **network share** from a file server
- Similar to **Windows Redirected Folders** — files live on server, accessed over network
- Users' files and settings follow them to **any connected machine**

**Enterprise Use Case**
Many companies and universities implement centralized authentication so employees/students can log into any workstation with their credentials. Files sync automatically, applications remember preferences, and administrators manage permissions centrally rather than on each individual machine.

## Links

- [[Linux MOC]] — Linux operating system fundamentals
- [[etc directory]]
- [[Separate user accounts enable accountability through audit logs and granular permission control]]
