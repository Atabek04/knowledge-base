---
created: 2026-01-20
tags: [linux/user-management]
---

**Linux user system** distinguishes between three categories of user accounts, each serving different purposes and with different permission levels.

**Superuser (Root)**
- Has **unrestricted permissions** to all system resources
- Can only be accessed through explicit elevation:
  - `su -` — switches to root user session
  - `sudo -i` — opens root shell
  - `sudo command` — executes specific command as root
- Reserved for administrative tasks requiring complete system control

**User Account**
- Regular account created for individuals to log in
- Each user gets their own isolated **home directory** (e.g., `/home/ayub`)
- Limited permissions: users cannot modify system files or other users' files
- Used for daily work, development, and general application access

**Service Account**
- Special accounts created to run specific system **services** and applications
- Relevant primarily on **Linux servers** where background services run continuously
- Each service typically gets its own dedicated user account (e.g., `mysql` user runs MySQL database)
- **Security best practice**: Services run with their own user rather than as root
  - If the service is compromised, attacker has limited permissions
  - Limits damage from potential security vulnerabilities

On a typical Linux server, multiple **regular users** and **service users** coexist. A single machine might have system administrators, developers, database services, web servers, and other services each operating with appropriate permission levels.

## Links

- [[Linux MOC]] — Linux operating system fundamentals
- [[Separate user accounts enable accountability through audit logs and granular permission control]]
