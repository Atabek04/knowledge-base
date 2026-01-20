---
created: 2026-01-20
tags: [linux/permissions]
---

**Linux file permissions** operate at two distinct levels: **user-level permissions** for individual ownership and **group-level permissions** for team-based access sharing.

**User-Level Permissions**
- Apply to a **single specific file owner**
- Only the **file owner** can read, write, or execute the file (except for root)
- Example: If user John owns `/home/john/secrets.txt`, only John can read or modify it
- No other regular user can access that file
- Provides **fine-grained control** for personal files and sensitive data

**Group-Level Permissions**
- Apply to **all members of a defined group** equally
- Multiple users can be added to the same group
- All group members inherit the **same permissions** on resources the group can access
- Example: If `developers` group has read permission on `/var/www/`, all members of that group can read website files
- Avoids listing individual users one by one

**Why Both Exist**
- **User permissions** — Enable individual ownership and privacy for personal files
- **Group permissions** — Enable **team collaboration** by sharing access across multiple people without duplicating permission entries

On Linux systems, these two permission levels work together: you might own certain files personally (user-level permissions) while being part of groups that grant you access to shared resources (group-level permissions). This two-tier system balances individual control with efficient team access management.

## Links

- [[Linux MOC]] — Linux operating system fundamentals
- [[Separate user accounts enable accountability through audit logs and granular permission control]]
- [[Every Linux user must have exactly one primary group but can have multiple secondary groups]]
