---
created: 2026-05-14
aliases: [heredoc, here document, cat << EOF]
tags: [linux, cli-tools, bash, heredoc]
---

A **heredoc** (here document) is shell syntax that feeds a block of multi-line text directly into a command's stdin. Written as `<<DELIMITER ... DELIMITER`. The delimiter is any chosen word — `EOF` is convention, not magic.

## Why use heredoc?

Embed multi-line content in scripts: config files, SQL queries, JSON payloads, email bodies, prompts. Cleaner than chained `echo` calls. Variable expansion still works unless you quote the delimiter.

---

What is the basic syntax?

```bash
cat << EOF > file.txt
line 1
line 2
EOF
```

Everything between `<< EOF` and the closing `EOF` becomes stdin.

---

What does quoting the delimiter do?

`<< 'EOF'` (quoted) **disables** variable and command substitution — content is treated literally. Unquoted `<< EOF` expands `$VAR` and `$(cmd)`.

---

What does `<<-` do?

Strips **leading tab characters** from each line, letting you indent the heredoc for readability without breaking the content. Only tabs are stripped, not spaces.

---

What is a here-string `<<<`?

Single-line variant. `cmd <<< "string"` feeds one string as stdin. Example: `grep foo <<< "$variable"`.

## Common patterns

```bash
# Write a config file
cat << EOF > nginx.conf
server {
  listen 80;
  server_name $HOSTNAME;
}
EOF

# Literal content (no expansion)
cat << 'EOF' > script.sh
echo "$USER is literal here"
EOF

# Pipe SQL to psql
psql mydb << EOF
SELECT count(*) FROM users;
EOF

# JSON payload to curl
curl -X POST https://api.example.com -d @- << EOF
{"name": "$NAME", "active": true}
EOF

# Indented heredoc with <<-
if true; then
    cat <<- EOF
	leading tabs stripped
	but spaces preserved
	EOF
fi

# Here-string
grep "error" <<< "$log_line"
```

## Read more

- [[cat concatenates files and prints contents to stdout]]
- [[Bash variables store data and command output for reuse in scripts]]
- [[Output redirection operators write command output to files in Linux]]
- [[Linux MOC]]
