TARGET DECK: Tech-KB::Linux::Permissions
Tags: linux permissions
**Related:** [[Linux MOC]]

START
Coding Questions
What is file ownership in Linux?
Back: **File ownership** assigns each file to a **user** (owner) and a **group** for access control.
Tags: linux permissions
END

START
Coding Questions
Who is the default owner of a newly created file?
Back: The **user** who created the file.
Tags: linux permissions
END

START
Coding Questions
What does `chown user:group file.txt` do?
Back: Changes both the **user owner** and **group owner** of the file simultaneously.
Tags: linux permissions
END

START
Coding Questions
What does `chown user file.txt` do?
Back: Changes only the **user owner**, leaving the group unchanged.
Tags: linux permissions
END

START
Coding Questions
What command changes only the group ownership of a file?
Back: `chgrp groupname filename`
Tags: linux permissions
END

START
Coding Questions
How do you recursively change ownership of all files in a directory?
Back: Use the `-R` flag: `chown -R user:group directory/`
Tags: linux permissions
END

START
Coding Questions
Can a non-root user change file ownership with chown?
Back: No — only the **owner** or **root** can change ownership. Regular users cannot transfer file ownership.
Tags: linux permissions
END

START
Coding Questions
What does the third column in `ls -l` output represent?
Back: The **owner** (user) of the file.
Tags: linux permissions
END

START
Coding Questions
What are the three Linux permission types and what does each allow?
Back:
- **Read (r)** — view file contents / list directory contents
- **Write (w)** — modify file contents / create or delete files in directory
- **Execute (x)** — run file as program / enter a directory
Tags: linux permissions
END

START
Coding Questions
What are the three permission categories in Linux?
Back: **Owner (u)** — file owner, **Group (g)** — group members, **Others (o)** — everyone else.
Tags: linux permissions
END

START
Coding Questions
What does the first character in the 10-character permission string represent?
Back: The **file type**: `-` regular file, `d` directory, `c` character device, `l` symbolic link.
Tags: linux permissions
END

START
Coding Questions
How do you add execute permission to a file for all categories?
Back: `chmod +x filename` — adds execute for owner, group, and others.
Tags: linux permissions
END

START
Coding Questions
What does `chmod 755 file.sh` mean?
Back:
- Owner: **7** = rwx (read + write + execute)
- Group: **5** = r-x (read + execute)
- Others: **5** = r-x (read + execute)
Tags: linux permissions
END

START
Coding Questions
What does `chmod 644 file.txt` mean?
Back:
- Owner: **6** = rw- (read + write)
- Group: **4** = r-- (read only)
- Others: **4** = r-- (read only)
Tags: linux permissions
END

START
Coding Questions
What does the `=` operator do in chmod symbolic notation?
Back: **Replaces** all permissions for that category (unlike `+` which adds). Example: `chmod u=rwx,g=rx,o=r file.txt`
Tags: linux permissions
END

START
Coding Questions
Why do directories need execute permission?
Back: To **enter** the directory (`cd`) and access its contents — even if you have read permission, you can't enter without execute.
Tags: linux permissions
END

START
Coding Questions
How do you recursively apply permissions to a directory and all its contents?
Back: `chmod -R 755 directory/`
Tags: linux permissions
END

START
Coding Questions
What is the numeric permission value for each permission bit?
Back:
- `r` (read) = **4**
- `w` (write) = **2**
- `x` (execute) = **1**
- no permission = **0**

Add them: `rwx` = 4+2+1 = **7**, `rw-` = 4+2 = **6**, `r-x` = 4+1 = **5**
Tags: linux permissions
END

START
Coding Questions
What are the two levels of Linux permission management?
Back: **User-level** (individual ownership — controls a single file owner's access) and **group-level** (team access — all group members share the same permissions on a resource).
Tags: linux permissions
END

START
Coding Questions
Why does Linux have group-level permissions?
Back: To enable **team collaboration** — multiple users can be added to a group and all inherit the same permissions, without listing individuals one by one.
Tags: linux permissions
END
