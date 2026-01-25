---
created: 2026-01-21
tags: [linux, cli-tools, filesystem, ls-command]
---

The `ls` command lists files and directories in the filesystem. The `-a` flag shows hidden files (starting with `.`), and the `-l` flag displays detailed information including permissions, ownership, size, and modification time.

The long format is essential for understanding file properties and is one of the most commonly used command variations in daily Linux work.

## What does the -a flag do with the ls command?

The `-a` flag tells `ls` to include **all** files, including those starting with `.` (dot files). By default, `ls` hides these files because they typically contain configuration data.

---

What information does the -l flag show in ls output?

The `-l` flag uses long listing format showing: (1) **permissions** (10 chars: file type + rwx for owner/group/others), (2) **hard links** count, (3) **owner** (user), (4) **owner group**, (5) **size** in bytes, (6) **modification date**, (7) **modification time**, (8) **filename**.

---

What does the first character in the permissions block represent?

The first character represents the **file type**: `-` for regular file, `d` for directory, `c` for character device, `l` for symbolic link.

---

How would you show all files with detailed information including hidden files?

Use `ls -al` (or `ls -la`). This combines the `-a` flag to show hidden files with the `-l` flag to display detailed information.

---

## Example Output

```bash
-rw-r--r-- 1 user group 1024 Jan 20 10:30 file.txt
│││││││││ │      │    │   │   │  │  │  │
│││││││││ │      │    │   │   │  │  │  └─ Filename
│││││││││ │      │    │   │   │  │  └───── Time
│││││││││ │      │    │   │   │  └──────── Date
│││││││││ │      │    │   │   └─────────── Size (bytes)
│││││││││ │      │    │   └──────────────── Group
│││││││││ │      │    └───────────────────── Owner
│││││││││ │      └────────────────────────── Hard links
│││││││││ └────────────────────────────────── File type + rwx blocks
```

Common output example with hidden files:
```bash
drwxr-xr-x  2 user group 4096 Jan 20 10:30 .config
-rw-r--r--  1 user group 1024 Jan 20 10:30 .bashrc
-rw-r--r--  1 user group 2048 Jan 20 10:30 file.txt
```

## Related Notes

- [[Every program has 3 built-in streams - stdin, stdout, stderr]]
- [[Linux root filesystem uses a hierarchical tree structure with standardized directories for different purposes]]
- [[Linux file ownership assigns files to users and groups for permission control]]
- [[Linux file permissions control read, write, and execute access for owner, group, and others]]

## Flashcards

?
What does ls -a do?

Shows **all** files including hidden files starting with `.`

---

?
What does ls -l do?

Displays **long format** with permissions, owner, group, size, date, time, and filename.

---

?
How do you combine both -a and -l flags?

Use `ls -al` (or `ls -la`) to show all files in long format.

---

?
What does the first character in ls -l output represent?

The **file type**: `-` (regular file), `d` (directory), `c` (character device), `l` (symbolic link).

---

?
Name four pieces of information shown in ls -l output.

**Permissions**, **owner**, **group**, **size**, **modification date/time**, **filename**.

---

?
What directory typically starts with a dot and is used for configuration?

The `.config` directory (or other dot directories like `.bashrc`, `.ssh`).
