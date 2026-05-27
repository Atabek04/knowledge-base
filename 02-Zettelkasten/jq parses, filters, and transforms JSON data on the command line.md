---
created: 2026-05-14
aliases: [jq]
tags: [linux, cli-tools, jq, json]
---

`jq` is a CLI JSON processor. It pretty-prints, **extracts fields**, filters arrays, transforms structure, and produces new JSON. Think of it as `sed`/`awk`/`grep` for JSON — but structure-aware instead of line-based.

## Why use jq?

API responses come as JSON. Grep can't reliably parse nested structures. `jq` reads JSON, runs a filter expression, and outputs JSON (or raw text). Universal partner of `curl`.

---

What is the identity filter?

`.` — outputs the input unchanged. Most common use: `curl ... | jq` to pretty-print a response.

---

How do you extract a field?

`.field` for top-level, `.user.name` to descend, `.users[0]` for array index, `.users[]` for all elements.

---

What does `-r` do?

Outputs **raw** strings — strips surrounding quotes. Needed when piping a string value into another command: `curl ... | jq -r '.token'`.

---

How do you filter an array?

`map(select(condition))` keeps matching elements. Example: `.users | map(select(.active == true))` → only active users.

---

How do you build new objects?

`{newKey: .oldKey}`. Example: `.users | map({id, name: .full_name})` — reshape each user.

## Common patterns

```bash
# Pretty-print
curl -s https://api.github.com/users/torvalds | jq

# Extract one field (raw string)
curl -s api/login | jq -r '.access_token'

# Nested path
jq '.data.user.email' response.json

# Array index / slice
jq '.items[0]'           # first
jq '.items[-1]'          # last
jq '.items[2:5]'         # slice

# Iterate all elements
jq '.users[] | .email'

# Filter
jq '.users | map(select(.age >= 18))'

# Multiple fields
jq '{name, email}' user.json
jq '.users[] | {id, name}' response.json

# Length / keys / type
jq 'length'
jq 'keys'
jq '. | type'

# Sort and unique
jq '.tags | unique | sort'

# Group by
jq 'group_by(.category)'

# Conditional
jq 'if .active then "yes" else "no" end'

# String interpolation
jq -r '.users[] | "\(.id): \(.name)"'

# Use a shell variable as filter arg
jq --arg uid "$USER_ID" '.users[] | select(.id == $uid)' data.json

# In-place edit via temp file (jq has no -i)
jq '.version = "2.0"' config.json > tmp && mv tmp config.json

# Read multiple files
jq -s '.[0].users + .[1].users' a.json b.json   # combine arrays
```

## Useful flags

| Flag | Purpose |
|------|---------|
| `-r` | raw string output (no quotes) |
| `-c` | compact (no pretty-print) |
| `-s` | slurp inputs into one array |
| `-n` | null input (build JSON from scratch) |
| `-R` | raw input (read lines as strings) |
| `--arg name value` | pass shell string into filter |
| `--argjson name json` | pass JSON value into filter |
| `-e` | exit non-zero if result is null/false |

## Read more

- [[curl transfers data to and from servers over many protocols]]
- [[grep searches files for lines matching text patterns using regular expressions]]
- [[Pipe operator chains Linux commands by connecting stdout of one to stdin of another]]
- [[Linux MOC]]
