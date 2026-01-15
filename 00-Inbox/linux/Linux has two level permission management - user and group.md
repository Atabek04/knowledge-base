
## User-level Permission

Apply to <mark style="background: #BBFABBA6;">only one specific user</mark>.

File owner can read/write/execute
No one else get these permissions (except root)

Example: John owns `/home/john/secrests.txt` - only John read it.

---
## Group-level Permission

Apply to <mark style="background: #BBFABBA6;">all members of a group</mark>

Multiple users added to same group.
Group permissions apply to everyone in that group

Example: `developers` group can read `/var/www/` - all members of that group get access.

---

## Why Both Exist

- User permissions: 
	Fine control for individual ownership.
- Group permissions: 
	Share access across the team without listing everyone one by one.