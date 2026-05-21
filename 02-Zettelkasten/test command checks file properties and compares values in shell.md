---
created: 2026-05-14
aliases: [test, test -f, "[ ]"]
tags: [linux, cli-tools, bash, test, conditionals]
---

`test` evaluates a condition and exits with status `0` (true) or `1` (false). Shell scripts read this exit code in `if`, `&&`, `||`. The brackets `[ expr ]` are an alias for `test expr` — same command, prettier syntax.

## Why use test?

Conditional logic in scripts: does this file exist? is this variable empty? are two strings equal? Pre-flight checks before running commands that would fail loudly otherwise.

---

What does `test -f path` check?

Returns true if `path` exists **and** is a regular file (not a directory, not a symlink target missing, not a device).

---

What is the difference between `-e`, `-f`, and `-d`?

`-e` exists (any type). `-f` exists and is a **regular file**. `-d` exists and is a **directory**.

---

What is the bracket form?

`[ -f file.txt ]` is identical to `test -f file.txt`. Spaces inside brackets are **required**. Bash also has `[[ ... ]]` which is a shell keyword with more features (regex `=~`, no word splitting).

---

How is test used in if statements?

```bash
if [ -f config.yml ]; then
  echo "found"
fi
```

The `if` runs the body when test exits 0.

## Common file tests

| Flag | True when |
|------|-----------|
| `-e path` | path exists |
| `-f path` | regular file |
| `-d path` | directory |
| `-L path` | symlink |
| `-s path` | file exists and size > 0 |
| `-r` / `-w` / `-x` | readable / writable / executable |
| `-z str` | string is empty |
| `-n str` | string is non-empty |
| `str1 = str2` | strings equal |
| `int1 -eq int2` | integers equal (`-ne -lt -le -gt -ge`) |
| `f1 -nt f2` | f1 newer than f2 |

## Common examples

```bash
# Guard a script
[ -f .env ] || { echo ".env missing"; exit 1; }

# Create dir if absent
[ -d logs ] || mkdir logs

# Check command-line arg
if [ -z "$1" ]; then
  echo "usage: $0 <file>"; exit 1
fi

# Compare numbers
if [ "$count" -gt 100 ]; then
  echo "too many"
fi

# Bash [[ ]] with regex
if [[ "$email" =~ ^[a-z]+@[a-z]+\.[a-z]+$ ]]; then
  echo "valid"
fi
```

## Read more

- [[Bash if statements execute commands conditionally using test operators for comparison]]
- [[Bash variables store data and command output for reuse in scripts]]
- [[Linux MOC]]
