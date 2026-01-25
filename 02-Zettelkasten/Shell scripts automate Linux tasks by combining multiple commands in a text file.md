---
created: 2026-01-21
tags: [linux, bash, shell-scripting, automation]
---

Shell scripts are text files containing sequences of shell commands that automate repetitive tasks and complex operations. Scripts combine simple commands into larger workflows, following the Unix philosophy of composing small tools to solve complex problems.

Shell scripts run in the shell interpreter (bash, sh, zsh) and can access all command-line utilities, making them powerful for system administration and automation.

## What is shell scripting used for?

Shell scripts automate **repetitive tasks** (backups, log rotation), **chain multiple tools together** (pipe commands), **run scheduled jobs** (using cron), and **perform complex system operations** that would be tedious to type manually each time.

---

What are the key advantages of shell scripts over typing commands manually?

Scripts provide **repeatability** (run anytime), **consistency** (same steps every time), **documentation** (readable commands), **scheduled execution** (cron jobs), and **complex logic** (conditions, loops).

---

What three elements should every shell script contain?

**Shebang** (`#!/bin/bash`) on the first line to specify the interpreter, **executable permission** (`chmod +x`) to allow direct execution, and **meaningful commands** that perform the desired task.

---

Can you run a shell script without execute permission?

Yes, but you must explicitly call the interpreter: `bash script.sh`. With execute permission, you can run directly: `./script.sh`. Execute permission requires the shebang.

---

What is the difference between writing a shell script and running individual commands?

Individual commands are one-off operations in the terminal, while scripts are **reusable programs** that can be run repeatedly, scheduled, and shared with others.

---

## Basic Script Structure

```bash
#!/bin/bash
# Shell script comment

# Variables
var_name="value"

# Commands
echo "Starting backup..."
backup_dir="/backups"
mkdir -p $backup_dir

# Logic
if [ -d $backup_dir ]; then
    tar -czf $backup_dir/backup_$(date +%Y%m%d).tar.gz /home/user/data
    echo "Backup completed"
else
    echo "Backup directory not found"
fi
```

## Common Script Patterns

```bash
# Simple backup
#!/bin/bash
tar -czf backup_$(date +%Y%m%d).tar.gz /data

# Loop through files
for file in *.txt; do
    echo "Processing $file"
    # do something with $file
done

# Conditional execution
if [ -f config.txt ]; then
    source config.txt
else
    echo "Config file not found"
fi

# Function definition
backup_files() {
    local src=$1
    local dest=$2
    tar -czf "$dest/backup.tar.gz" "$src"
}

# Error handling
command || { echo "Error: command failed"; exit 1; }
```

## Related Notes

- [[Shebang tells the operating system which interpreter should execute a script]]
- [[Bash variables store data and command output for reuse in scripts]]
- [[Bash positional parameters access command-line arguments as numbered variables]]
- [[Bash if statements execute commands conditionally using test operators for comparison]]
- [[Bash loops iterate over lists with for or repeat while conditions are true]]
- [[Bash functions encapsulate reusable code blocks that accept parameters and return exit codes]]
- [[Shell interprets user commands and translates them into system calls for the kernel]]

## Flashcards

?
What is a shell script?

A text file containing **shell commands** that can be run as a program to **automate tasks**.

---

?
What are three main uses for shell scripts?

**Automate** repetitive tasks, **chain** commands together, **schedule** jobs with cron, and **perform** complex operations.

---

?
What must be the first line of a shell script?

The **shebang** (`#!/bin/bash` or similar) to tell the OS which interpreter to use.

---

?
How do you make a shell script executable?

Use `chmod +x script.sh` to add execute permission.

---

?
What happens if you run a shell script without execute permission?

You must explicitly call the interpreter: `bash script.sh` instead of `./script.sh`

---

?
What is the advantage of shell scripts over typing commands manually?

Scripts are **repeatable**, **consistent**, **documented**, can be **scheduled**, and support **complex logic**.

---

?
What can shell scripts access?

All **command-line utilities**, **environment variables**, **file system**, and **system resources**.
