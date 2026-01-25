---
created: 2026-01-21
tags: [linux, permissions, file-management, chmod]
---

Linux file permissions control **read**, **write**, and **execute** access for three categories: **owner** (user), **group**, and **others**. Permissions are displayed as a 10-character string in `ls -l` output and can be modified using symbolic (`chmod u+x`) or numeric (`chmod 755`) modes.

Permissions work together with ownership to enforce security and prevent unauthorized access to files and directories.

## What are the three permission types?

**Read (r)** allows viewing file contents or listing directory contents, **Write (w)** allows modifying file contents or creating/deleting files in a directory, **Execute (x)** allows running a file as a program or entering a directory to access its contents.

---

What are the three categories that permissions apply to?

**Owner (u)** — the file owner, **Group (g)** — members of the file's group, **Others (o)** — everyone else.

---

What does the first character in the 10-character permission string represent?

The first character represents the **file type**: `-` for regular file, `d` for directory, `c` for character device, `l` for symbolic link.

---

How do you set execute permission on a file using symbolic mode?

Use `chmod +x filename` to add execute permission for all categories, or `chmod u+x filename` for owner only. You can combine: `chmod u+x,g+x filename`.

---

How do you set permissions using numeric mode?

Use `chmod [3 digits] filename` where each digit is calculated: `r` (read) = 4, `w` (write) = 2, `x` (execute) = 1. Example: `chmod 755` means owner gets 7 (4+2+1=rwx), group gets 5 (4+1=r-x), others get 5 (r-x).

---

Why does the execute permission matter for directories?

**Execute permission on a directory** allows entering and listing its contents. Without execute, users cannot `cd` into the directory or access files inside even if they have read permission.

---

What is the difference between chmod symbols u, g, o, and a?

**u** (user/owner), **g** (group), **o** (others), **a** (all three categories). Use combinations like `u+x,g+x` or simply `+x` for all.

---

## Permission Conversion Reference

| Symbolic | Numeric | Permissions |
|----------|---------|------------|
| `---` | 0 | No permissions |
| `--x` | 1 | Execute only |
| `-w-` | 2 | Write only |
| `-wx` | 3 | Write + Execute |
| `r--` | 4 | Read only |
| `r-x` | 5 | Read + Execute |
| `rw-` | 6 | Read + Write |
| `rwx` | 7 | Read + Write + Execute |

## Common Examples

```bash
# Add execute permission to owner
chmod u+x script.sh

# Set to rwx for owner, r-x for group and others (755)
chmod 755 file.sh

# Set to rw- for owner and group, no access for others (660)
chmod 660 file.txt

# Remove all permissions then add specific ones
chmod u=rwx,g=rx,o=r file.txt

# Recursively set permissions on directory
chmod -R 755 directory/

# Show only file permissions without other info
stat -c %a file.txt

# Change multiple files
chmod 644 *.txt
```

## Permission Examples Explained

```bash
-rwxr-xr--  (755) — Owner: full access, Group: read+exec, Others: read only
-rw-rw----  (660) — Owner: read+write, Group: read+write, Others: none
-r--r--r--  (444) — All: read-only
-rwx------  (700) — Owner: full access, Group: none, Others: none
drwxr-xr-x (755) — Directory: owner full, group+others can enter/list
```

## Important Notes

- By default, newly created files do NOT have execute permission (for security)
- Shell scripts and binaries need execute permission to run
- Directories need execute permission to enter (even with read permission)
- Only owner or root can change permissions on files you own
- The `umask` setting controls default permissions for new files

## Related Notes

- [[Linux file ownership assigns files to users and groups for permission control]]
- [[Bash functions encapsulate reusable code blocks that accept parameters and return exit codes]]
- [[Shebang tells the operating system which interpreter should execute a script]]

## Flashcards

?
What do the three permission types mean?

**Read (r)** — view contents, **Write (w)** — modify contents, **Execute (x)** — run as program/enter directory.

---

?
What are the three categories permissions apply to?

**Owner (u)** — file owner, **Group (g)** — group members, **Others (o)** — everyone else.

---

?
How do you add execute permission to a file?

`chmod +x filename` or `chmod u+x filename` for owner only.

---

?
What does chmod 755 mean?

Owner: 7 (rwx), Group: 5 (r-x), Others: 5 (r-x).

---

?
What does chmod 644 mean?

Owner: 6 (rw-), Group: 4 (r--), Others: 4 (r--).

---

?
How do you set permissions using symbolic notation?

`chmod u=rwx,g=rx,o=r file.txt` or `chmod u+x file.txt` to add permission.

---

?
What does the = operator do in chmod?

**Replaces** all permissions for that category (unlike + which adds).

---

?
Why do directories need execute permission?

To **enter** the directory and access its contents, even if you have read permission.

---

?
How do you recursively apply permissions to a directory and all contents?

`chmod -R 755 directory/`
