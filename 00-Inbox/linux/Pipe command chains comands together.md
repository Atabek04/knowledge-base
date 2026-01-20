
#### What it is

**Pipe command `|`** - connects output of one command to input of another.

Chains command together to process data step by step.

---
#### Usage

```bash
command1 | command2 | command3
```

Output from `command1` becomes input to `command2`, etc.

----
#### Examples

```bash
# Search for specific lines, then count them
cat file.txt | grep "error" | wc -l

# List files, sort by name, view with pager
ls -l | sort | less

# Find processes containing "java", show only names
ps aux | grep java | awk '{print $1}'

# Count unique users
cat /etc/passwd | cut -d: -f1 | sort | uniq | wc -l
```

- `cat` — Display file contents
- `grep` — Search for text patterns in files
- `wc` — Count lines, words, characters
- `wc -l` — Count lines only
- `sort` — Sort lines alphabetically
- `less` — Paginate file viewing
- `ps` — List running processes
- `ps aux` — List all processes with full details
- `awk` — Extract/process text by columns or patterns
- `cut` — Extract specific columns from text
- `uniq` — Remove or count duplicate consecutive lines