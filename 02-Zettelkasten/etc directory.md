---
created: 2026-01-20
tags: [linux/configuration]
---
**Linux system configuration**, including user accounts, groups, and passwords, is stored in **plain text files** located under the `/etc/` directory. This design choice provides transparency and flexibility.

**Primary Configuration Files**

**`/etc/passwd`** — User account information
- Contains one line per user account
- Records username, numeric user ID, primary group ID, home directory, and login shell
- Readable by all users (it's "passwd" not "password")
- Does NOT contain actual passwords (those are hashed and stored elsewhere)

**`/etc/shadow`** — Password hashes
- Contains **hashed passwords** for all users
- Only readable by root user (provides security)
- Stores password expiration and aging information

**`/etc/group`** — Group definitions
- Defines all system groups and their members
- Maps group names to numeric group IDs
- Lists secondary group membership

**Advantages of Plain Text Storage**
- **Easy to read** — System administrators can quickly understand configurations
- **Script-friendly** — Text files can be parsed by shell scripts and tools
- **Tool-independent** — No database or special software needed to edit
- **Portable** — Files can be easily backed up, copied, or migrated

**Important Security Note**: While plain text provides transparency, `/etc/shadow` is restricted to root-only access to protect password hashes. This separation allows regular users to look up directory information (usernames, home directories) while keeping authentication data secure.

## Links

- [[Linux MOC]] — Linux operating system fundamentals
- [[User management commands like useradd and usermod safely modify system user configuration]]
- [[LDAP and FreeIPA provide centralized authentication for Linux similar to Active Directory on Windows]]
