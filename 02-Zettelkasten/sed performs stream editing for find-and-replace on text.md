---
created: 2026-05-14
aliases: [sed]
tags: [linux, cli-tools, text-processing, sed]
---

`sed` (**s**tream **ed**itor) reads text line by line and applies edit commands. Used for **find-and-replace**, deletion, insertion, and extraction without opening an editor. Non-interactive — perfect for scripts and pipelines.

## Why use sed?

Editing files programmatically. Replace strings across many files, strip lines matching a pattern, transform output mid-pipeline. Faster than opening Vim for one-off changes.

---

What is the basic substitute syntax?

`sed 's/old/new/'` replaces **first** occurrence per line. Add `g` flag for all: `sed 's/old/new/g'`.

---

What does the `-i` flag do?

Edits the file **in place** instead of printing to stdout. Use `sed -i 's/foo/bar/g' file.txt`. GNU sed accepts `-i` directly; BSD/macOS sed needs `-i ''`.

---

What does the `-n` flag do?

**Suppresses** default printing. Used with `p` command to print only matched lines: `sed -n '/pattern/p' file`.

---

What does the `-E` flag do?

Enables **extended regex** — no backslash escaping for `+`, `?`, `()`, `|`. Example: `sed -E 's/(foo|bar)/X/g'`.

## Common flags

| Flag | Purpose |
|------|---------|
| `-i` | edit file in place |
| `-i.bak` | in-place with backup `.bak` |
| `-n` | suppress auto-print |
| `-E` | extended regex |
| `-e` | multiple commands: `sed -e 'cmd1' -e 'cmd2'` |

## Common examples

```bash
# Replace all occurrences
sed 's/foo/bar/g' file.txt

# Replace in place with backup
sed -i.bak 's/old/new/g' config.yml

# Delete lines matching pattern
sed '/^#/d' file.txt          # delete comment lines
sed '/^$/d' file.txt          # delete empty lines

# Print specific lines
sed -n '5,10p' file.txt       # lines 5–10
sed -n '/ERROR/p' app.log     # only matching lines

# Multiple substitutions
sed -e 's/foo/x/g' -e 's/bar/y/g' file.txt

# Use different delimiter when string has /
sed 's|/usr/local|/opt|g' file.txt
```

## Read more

- [[grep searches files for lines matching text patterns using regular expressions]]
- [[Pipe operator chains Linux commands by connecting stdout of one to stdin of another]]
- [[Linux MOC]]
