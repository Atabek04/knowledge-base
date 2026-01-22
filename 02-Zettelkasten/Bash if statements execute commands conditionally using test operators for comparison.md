---
created: 2026-01-21
tags: [linux, bash, scripting, conditionals, control-flow]
---

Bash `if` statements execute commands conditionally based on test expressions. They use test operators like `-eq` for numeric comparison, `=` for string equality, and `-f` for file existence checks. If statements can include `elif` for additional conditions and `else` for fallback commands.

## What is the basic if statement syntax?

```bash
if [ condition ]; then
    # commands if true
fi
```

The condition is tested using `[ ]` (test command), then executes commands between `then` and `fi` if true.

---

How do you add an else clause?

Use `else` before the fallback commands:
```bash
if [ condition ]; then
    # commands if true
else
    # commands if false
fi
```

---

How do you test multiple conditions?

Use logical operators: `&&` (AND) and `||` (OR):
- `[ $age -ge 18 ] && [ $score -ge 80 ]` — both must be true
- `[ $x -eq 1 ] || [ $y -eq 2 ]` — either can be true

---

What is the difference between -eq and =?

`-eq` is for **numeric** comparison (`[ $num -eq 5 ]`), while `=` is for **string** comparison (`[ "$str" = "value" ]`).

---

What does [ -f filename ] test?

Tests if a file **exists** and is a regular file. Returns true if the file exists, false otherwise.

---

What does [ -d directory ] test?

Tests if a **directory** exists. Returns true if the path is a valid directory, false if it doesn't exist or is not a directory.

---

What are the common file test operators?

`-f` (file exists), `-d` (directory exists), `-r` (readable), `-w` (writable), `-x` (executable), `-s` (file has size > 0), `-e` (path exists).

---

## String Test Operators

| Operator | Meaning |
|----------|---------|
| `=` | Equal |
| `!=` | Not equal |
| `-z` | Empty string |
| `-n` | Not empty |

## Numeric Test Operators

| Operator | Meaning |
|----------|---------|
| `-eq` | Equal |
| `-ne` | Not equal |
| `-lt` | Less than |
| `-gt` | Greater than |
| `-le` | Less or equal |
| `-ge` | Greater or equal |

## File Test Operators

| Operator | Meaning |
|----------|---------|
| `-f` | File exists |
| `-d` | Directory exists |
| `-r` | Readable |
| `-w` | Writable |
| `-x` | Executable |
| `-s` | File has content |
| `-e` | Path exists (file or dir) |

## Examples

```bash
# Simple age check
if [ $age -ge 18 ]; then
    echo "Adult"
fi

# File existence check
if [ -f "$file" ]; then
    echo "File exists"
else
    echo "File not found"
fi

# String comparison
if [ "$username" = "admin" ]; then
    echo "Admin access"
elif [ "$username" = "user" ]; then
    echo "Regular user"
else
    echo "Unknown user"
fi

# Multiple conditions
if [ $attempts -lt 3 ] && [ -f "$config" ]; then
    echo "Attempt $attempts with config"
fi

# OR condition
if [ "$action" = "start" ] || [ "$action" = "begin" ]; then
    echo "Starting..."
fi

# Check if variable is empty
if [ -z "$1" ]; then
    echo "Error: argument required"
    exit 1
fi

# Check if file is readable
if [ -r "$filename" ]; then
    content=$(cat "$filename")
    echo "Read: $content"
else
    echo "Cannot read file"
fi

# Directory check
if [ -d "/backup" ]; then
    echo "Backup directory exists"
else
    mkdir -p "/backup"
fi
```

## [[[ ]] vs [ ]

```bash
# Old style (POSIX compatible)
if [ $num -eq 5 ]; then
    echo "test command"
fi

# Bash extended test (more features, no quoting needed)
if [[ $var == pattern* ]]; then
    echo "Pattern matching"
fi

# Arithmetic test
if (( $num > 5 )); then
    echo "Arithmetic comparison"
fi
```

## Related Notes

- [[Bash variables store data and command output for reuse in scripts]]
- [[Bash positional parameters access command-line arguments as numbered variables]]
- [[Bash loops iterate over lists with for or repeat while conditions are true]]
- [[Bash functions encapsulate reusable code blocks that accept parameters and return exit codes]]
- [[Shell scripts automate Linux tasks by combining multiple commands in a text file]]

## Flashcards

?
What is the basic if statement syntax in Bash?

`if [ condition ]; then ... fi`

---

?
What operator tests if a file exists?

`[ -f filename ]`

---

?
What operator tests if a directory exists?

`[ -d directory ]`

---

?
What does -eq do?

Tests **numeric equality** (is equal to).

---

?
What does = do?

Tests **string equality** (is equal to).

---

?
What does -ne do?

Tests **numeric inequality** (is NOT equal to).

---

?
What does -z do?

Tests if a string is **empty**.

---

?
How do you use AND in an if statement?

`[ condition1 ] && [ condition2 ]`

---

?
How do you use OR in an if statement?

`[ condition1 ] || [ condition2 ]`

---

?
What does -r test?

If a file is **readable** (has read permission).

---

?
What does -x test?

If a file is **executable** (has execute permission).
