---
created: 2026-05-14
aliases: [find]
tags: [linux, cli-tools, find, filesystem]
---

`find` recursively walks a directory tree and matches files by name, type, size, modification time, permissions, or any combination. Unlike `grep` (searches **inside** files), `find` searches **for** files.

## Why use find?

Locate files when you don't remember the path. Bulk-operate on matches via `-exec` or `-delete`. Filter by attributes (size > 100MB, modified last 7 days, owned by user).

---

What is the basic syntax?

`find <path> <expression>`. Example: `find . -name "*.log"` searches current directory recursively for `.log` files.

---

What does `-name` do?

Matches files by name with glob patterns. Case-sensitive. Use `-iname` for case-insensitive.

---

What does `-type` do?

Filters by file type: `f` regular file, `d` directory, `l` symlink, `s` socket.

---

What does `-exec` do?

Runs a command on each match. `{}` is the matched file, `\;` ends the command: `find . -name "*.tmp" -exec rm {} \;`.

## Common flags

| Flag | Purpose |
|------|---------|
| `-name "*.ext"` | match filename (glob) |
| `-iname` | case-insensitive name |
| `-type f\|d\|l` | file / directory / symlink |
| `-size +100M` | larger than 100MB (`-` for smaller) |
| `-mtime -7` | modified within 7 days |
| `-mmin -60` | modified within 60 minutes |
| `-maxdepth N` | limit recursion depth |
| `-not` / `!` | negate expression |
| `-delete` | delete matches |
| `-exec cmd {} \;` | run command per match |
| `-exec cmd {} +` | batch matches into one command |

## Common examples

```bash
# Find by name
find . -name "*.java"
find /var/log -iname "error*"

# Only directories
find . -type d -name "target"

# Large files
find / -type f -size +500M 2>/dev/null

# Recently modified
find . -mtime -1            # last 24h
find . -mmin -30            # last 30 min

# Delete matches
find . -name "*.tmp" -delete

# Run command per match
find . -name "*.sh" -exec chmod +x {} \;

# Combine: empty .log files older than 30 days
find /var/log -name "*.log" -size 0 -mtime +30 -delete

# Exclude a directory
find . -path ./node_modules -prune -o -name "*.js" -print
```

## Read more

- [[grep searches files for lines matching text patterns using regular expressions]]
- [[ls command displays files with options for hidden files and detailed format]]
- [[Linux MOC]]
