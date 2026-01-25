
```bash
command > file      # Overwrite file
command >> file     # Append to file
```

```bash
# Save grep results to file
grep "error" logs.txt > errors.txt

# Append output
echo "new line" >> errors.txt

# Save multiple commands
cat file1.txt | grep "pattern" > results.txt

# Pipe and redirect
ps aux | grep java > processes.txt

# Redirect stderr (errors)
command 2> errors.log

# Redirect both stdout and stderr
command > output.txt 2>&1
```

---
#### Common redirect symbols

| Symbol | Use Case                      |
| ------ | ----------------------------- |
| `>`    | Redirect `stdout` (overwrite) |
| `>>`   | Redirect `stdout` (append)    |
| `2>`   | Redirect `stderr` (overwrite) |
| `2>>`  | Redirect `stderr` (overwrite) |
| `&>`   | Redirect `stdout` + `stderr`  |

---

Read more:
- [[Every program has 3 built-in streams - stdin, stdout, stderr]]