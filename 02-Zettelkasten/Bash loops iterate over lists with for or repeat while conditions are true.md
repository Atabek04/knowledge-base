---
created: 2026-01-21
tags: [linux, bash, scripting, loops, control-flow]
---

Bash loops automate repetition of commands. The **for** loop iterates over a list (files, numbers, strings), and the **while** loop repeats while a condition is true. Loops support `break` to exit early and `continue` to skip to the next iteration.

## How do for loops work in Bash?

For loops iterate over each item in a list, storing the current item in a variable. Basic syntax:
```bash
for variable in list; do
    # commands using $variable
done
```

---

What is a typical use case for for loops?

Processing multiple files: `for file in *.txt; do mv "$file" "${file%.txt}.md"; done` or iterating over servers: `for server in prod-1 prod-2 prod-3; do ssh $server "uptime"; done`

---

How does a while loop work?

A while loop repeats as long as a condition is true. It checks the condition at the start of each iteration:
```bash
while [ condition ]; do
    # commands
done
```

---

How do you create a numeric range in a for loop?

Use brace expansion: `for i in {1..10}; do echo "Number: $i"; done` creates numbers 1 through 10.

---

How do you exit a loop early?

Use the `break` statement to exit the current loop immediately: `[ $i -eq 5 ] && break`

---

How do you skip to the next iteration?

Use the `continue` statement to skip remaining commands and move to the next iteration: `[ $i -eq 3 ] && continue`

---

How do you create an infinite loop that must be broken manually?

Use `while true; do ... done` or `for (( ;; )); do ... done`. The loop continues until `break` is called.

---

## For Loop Examples

```bash
# Loop over files in current directory
for file in *.txt; do
    echo "Processing: $file"
    cat "$file"
done

# Loop over a list of values
for server in prod-1 prod-2 prod-3; do
    echo "Checking ${server}..."
    ssh ${server} "uptime"
done

# Create numbered directories
for i in {1..10}; do
    mkdir "backup-$i"
done

# Loop with C-style syntax
for ((i=1; i<=10; i++)); do
    echo "Number: $i"
done

# Loop over command output
for user in $(cat /etc/passwd | cut -d: -f1); do
    echo "User: $user"
done

# Nested loops
for i in 1 2 3; do
    for j in a b c; do
        echo "$i-$j"
    done
done
```

## While Loop Examples

```bash
# Simple counter
count=0
while [ $count -lt 5 ]; do
    echo "Count: $count"
    count=$((count + 1))
done

# Read lines from file
while IFS= read -r line; do
    echo "Line: $line"
done < /path/to/file

# Retry with timeout
attempts=0
while [ $attempts -lt 3 ]; do
    if curl -s https://api.example.com > /dev/null; then
        echo "API is up"
        break
    fi
    attempts=$((attempts + 1))
    sleep 2
done

# Infinite loop (must break manually)
while true; do
    read -p "Enter command (q to quit): " cmd
    if [ "$cmd" = "q" ]; then
        break
    fi
    echo "You entered: $cmd"
done

# Process user input until done
while read -p "Enter name (or 'done' to exit): " name; do
    if [ "$name" = "done" ]; then
        break
    fi
    echo "Hello, $name"
done
```

## Loop Control Statements

```bash
# break — exit current loop
for i in {1..10}; do
    if [ $i -eq 5 ]; then
        break
    fi
    echo $i
done

# continue — skip to next iteration
for i in {1..10}; do
    if [ $i -eq 5 ]; then
        continue  # Skip 5
    fi
    echo $i
done

# Use with conditions
while [ $true ]; do
    read -p "Enter y or n: " response
    [ "$response" = "y" ] && break
    [ "$response" = "n" ] && continue
done
```

## Related Notes

- [[Bash if statements execute commands conditionally using test operators for comparison]]
- [[Bash variables store data and command output for reuse in scripts]]
- [[Bash functions encapsulate reusable code blocks that accept parameters and return exit codes]]
- [[Shell scripts automate Linux tasks by combining multiple commands in a text file]]

## Flashcards

?
What is the basic for loop syntax?

`for variable in list; do ... done`

---

?
What is the basic while loop syntax?

`while [ condition ]; do ... done`

---

?
How do you create a for loop with numbers 1-10?

`for i in {1..10}; do echo $i; done`

---

?
How do you loop over all .txt files in a directory?

`for file in *.txt; do ... done`

---

?
What does the break statement do?

**Exits** the current loop immediately.

---

?
What does the continue statement do?

**Skips** remaining commands and goes to the next iteration.

---

?
How do you create an infinite loop?

`while true; do ... done` (must use `break` to exit)

---

?
How do you loop with a C-style syntax?

`for ((i=1; i<=10; i++)); do ... done`

---

?
How do you read lines from a file in a loop?

`while IFS= read -r line; do ... done < filename`
