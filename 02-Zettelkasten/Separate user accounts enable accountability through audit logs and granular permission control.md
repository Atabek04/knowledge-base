---
created: 2026-01-20
tags: [linux/user-management]
---

Creating **separate user accounts** rather than sharing a single account is essential for **accountability** and **granular permission management** on multi-user systems.

**Accountability and Auditing**
- Each user has a **unique login identity** independent of other users
- System **audit logs** record which user executed each command and when
- If something breaks or behaves incorrectly, logs reveal exactly who performed that action
- This **attribution** is critical for:
  - **Security investigation** — identifying unauthorized access or malicious behavior
  - **Debugging** — understanding who made changes when troubleshooting issues
  - **Compliance** — satisfying regulatory requirements for access tracking
  - **Performance tuning** — identifying which user's processes consume resources

**Granular Permission Control**
- Different users can have **different permission levels** based on their role
- Example system permissions distribution:
  - **Junior developers** — read-only access to production systems
  - **Senior developers** — permission to deploy code and restart services
  - **DevOps team** — full system access for infrastructure management
  - **Database administrator** — access only to database systems

With a **shared user account**, everyone has identical permissions regardless of role or responsibility. This creates security vulnerabilities: a junior developer could accidentally (or maliciously) delete production data or a service account compromise could grant unlimited access to sensitive systems.

**Separate accounts** enable organizations to implement the **principle of least privilege**—each user gets exactly the permissions they need, no more.

## Links

- [[Linux MOC]] — Linux operating system fundamentals
- [[Linux has three user categories - superuser, user account, and service account]]
- [[Linux permission management operates at user level and group level]]
