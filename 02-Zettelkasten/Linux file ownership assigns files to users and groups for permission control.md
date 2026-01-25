---
created: 2026-01-21
tags: [linux, permissions, ownership, file-management]
---

Linux file ownership assigns each file and directory to a **user** (owner) and a **group**. The owner is typically the user who created the file, and ownership can be changed using `chown` and `chgrp` commands. Ownership works together with permissions to control access.

## Who is the owner of a file?

By default, the user who created the file becomes its **owner**. The owner can be viewed in the ls output, and only the owner or root can change ownership.

---

What are the two types of ownership in Linux?

**User ownership** (the owner) and **group ownership** (the group the file belongs to). Both are shown in the ls -l output.

---

How do you view the current ownership of a file?

Use `ls -l filename` which displays the owner in the third column and group in the fourth column. Example: `-rw-r--r-- 1 user group 1024 Jan 20 10:30 file.txt`

---

How do you change both user and group ownership at once?

Use `chown user:group filename`. For example: `sudo chown tom:admin test.txt` changes the owner to tom and group to admin.

---

How do you change only the user ownership without affecting the group?

Use `chown username filename` without the colon and group name. For example: `chown newuser file.txt`

---

How do you change only the group ownership?

Use `chgrp groupname filename`. For example: `chgrp admin file.txt` changes only the group without affecting the user owner.

---

## Command Reference

```bash
# View ownership
ls -l file.txt

# Change user and group
chown user:group file.txt

# Change user only
chown user file.txt

# Change group only
chgrp group file.txt

# Change recursively (files and directories)
chown -R user:group directory/

# Change ownership with verbose output
chown -v user:group file.txt
```

## Example Output

```bash
-rw-r--r-- 1 alice developers 1024 Jan 20 10:30 project.txt
           │ └─ user (owner)
           │    └─ group (ownership)
```

## Related Notes

- [[Linux file permissions control read, write, and execute access for owner, group, and others]]
- [[Linux has three user categories - superuser, user account, and service account]]
- [[Linux permission management operates at user level and group level]]
- [[ls command displays files with options for hidden files and detailed format]]

## Flashcards

?
What is file ownership?

**File ownership** assigns each file to a **user** (owner) and a **group** for access control.

---

?
Who is the default owner of a newly created file?

The **user** who created the file.

---

?
What does this command do: chown user:group file.txt

Changes both the **user owner** and **group owner** of the file.

---

?
What does this command do: chown user file.txt

Changes only the **user owner**, leaving the group unchanged.

---

?
What command changes only the group ownership?

`chgrp groupname filename`

---

?
How do you recursively change ownership of all files in a directory?

Use the `-R` flag: `chown -R user:group directory/`

---

?
Can a non-root user change ownership of their own files?

No, only the **owner** or **root** can change ownership. Regular users cannot change ownership using chown.

---

?
What does the third column show in ls -l output?

The **owner** (user) of the file.
