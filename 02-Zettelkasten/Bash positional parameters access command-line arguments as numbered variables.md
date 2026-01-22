---
created: 2026-01-21
tags: [linux, bash, scripting, parameters, arguments]
---

Bash positional parameters are special variables that store command-line arguments passed to a script. They're numbered starting with `$1` for the first argument, `$2` for the second, and so on. `$0` contains the script name itself, and `$#` contains the total count of arguments.

## What are positional parameters?

**Positional parameters** are special variables that hold arguments passed to a script. When you run `./script.sh arg1 arg2 arg3`, the arguments become: `$0` (script name), `$1` (arg1), `$2` (arg2), `$3` (arg3).

---

What does $# represent?

`$#` represents the **total number** of positional parameters (excluding the script name). If you run `./script.sh a b c`, then `$#` equals 3.

---

What is the difference between $@ and $*?

`$@` expands to all arguments as **separate** items (properly quoted), while `$*` expands to all arguments as a **single** string. In loops, `$@` is usually better for handling arguments with spaces.

---

What is $0 used for?

`$0` contains the **script name** itself. Useful for usage messages: `echo "Usage: $0 <filename>"` or to determine the script's location.

---

How do you check if a required argument was provided?

Use the `-z` test to check if a variable is empty: `if [ -z "$1" ]; then echo "Error: missing argument"; exit 1; fi`

---

Can you reassign positional parameters?

Technically yes with `set`, but it's rarely done. Better practice is to assign them to regular variables at the start: `source=$1; destination=$2`

---

## Common Positional Parameter Examples

```bash
#!/bin/bash
# Script: backup.sh <source> <destination>

# Assign to variables for clarity
source=$1
destination=$2

# Check if arguments provided
if [ -z "$source" ] || [ -z "$destination" ]; then
    echo "Usage: $0 <source> <destination>"
    exit 1
fi

# Use the variables
echo "Backing up: $source"
echo "To: $destination"
cp -r "$source" "$destination"
```

## Usage with Loops

```bash
#!/bin/bash
# Process multiple files

if [ $# -eq 0 ]; then
    echo "Usage: $0 <file1> <file2> ..."
    exit 1
fi

# Loop through all arguments
for file in "$@"; do
    echo "Processing: $file"
    # process each file
done

# Alternative: index-based loop
for ((i=1; i<=$#; i++)); do
    echo "Arg $i: ${!i}"
done
```

## All Positional Parameter Variables

| Variable | Meaning |
|----------|---------|
| `$0` | Script name |
| `$1` | First argument |
| `$2` | Second argument |
| `$#` | Total number of arguments |
| `$@` | All arguments (expanded separately) |
| `$*` | All arguments (as single string) |

## Practical Script Example

```bash
#!/bin/bash
# file_counter.sh - count files with specified extension

if [ $# -lt 1 ]; then
    echo "Usage: $0 <directory> [extension]"
    echo "Example: $0 /home txt"
    exit 1
fi

directory=$1
extension=${2:-*}  # Default to all files if no extension

count=$(find "$directory" -name "*.$extension" -type f | wc -l)
echo "Found $count files with extension .$extension"
```

## Related Notes

- [[Bash variables store data and command output for reuse in scripts]]
- [[Bash read command captures user input from stdin during script execution]]
- [[Bash if statements execute commands conditionally using test operators for comparison]]
- [[Shell scripts automate Linux tasks by combining multiple commands in a text file]]

## Flashcards

?
What does $1 represent?

The **first command-line argument** passed to the script.

---

?
What does $# represent?

The **total number** of positional parameters (arguments).

---

?
What does $0 contain?

The **script name** itself.

---

?
If you run ./script.sh file1.txt file2.txt, what is $#?

`2` (two arguments were passed)

---

?
What is the difference between $@ and $*?

`$@` expands arguments **separately** (better for spaces), `$*` expands as **single string**.

---

?
How do you check if the first argument was provided?

`if [ -z "$1" ]; then echo "missing"; fi`

---

?
How would you loop through all arguments?

`for arg in "$@"; do echo "$arg"; done`

---

?
What does this line do: source=$1

Assigns the **first argument** to a variable named `source` for easier use.
