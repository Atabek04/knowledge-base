
Linux also has centralized functionality, like AD on Windows.

Linux has similar functionality:
- LDAP (Lightweight Directory Access Protocol) - centralized user database
- FreeIPA - like AD for Linux (LDAP + Kerberos)

---
#### Traditional Linux Multi-User

For single machines (like uni-labs), Linux is simpler:

Local accounts stored in `/etc/passwd` and `/etc/shadow`
Each user gets a home dir `/home/username`

When a user logs in, they access their `/home/username` folder.
Files stay on that local PC **only**.

---
#### Network Home Directories

Universities often mount NFS (Network File System):
Your `/home/username `is actually a network share from file server
Works like Windows Redirected Folders - files live on server, accessed remotely.