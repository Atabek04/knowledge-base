---
created: 2026-01-21
tags: [linux, bash, scripting, functions, code-reuse]
---

Bash functions encapsulate reusable blocks of code with meaningful names. Functions accept parameters (like positional parameters `$1`, `$2`) and return exit codes (`0` for success, non-zero for failure) via the `return` statement. They must be defined before being called.

Functions follow the Unix philosophy of breaking complex scripts into smaller, focused, reusable components.

## What is the basic function syntax?

```bash
function_name() {
    # commands here
    return value
}
```

Or with the `function` keyword:
```bash
function function_name {
    # commands here
}
```

---

How do functions receive parameters?

Functions use the same positional parameters as scripts: `$1` for the first argument, `$2` for the second, etc. Also `$#` for total count and `$@` for all arguments.

---

How do you call a function with arguments?

Simply use the function name followed by arguments: `greet "Alice"` passes "Alice" as `$1` to the greet function.

---

What does the return statement do in a function?

The `return` statement sets the **exit code** of the function. `0` means success, any non-zero value means failure. Access it with `$?` after calling the function.

---

What is the difference between return and echo output?

`return` sets the exit code for success/failure checking, while `echo` sends text to stdout. Functions can both return a code (`return 1`) and output text (`echo "result"`).

---

Why is quoting important when using $1 in functions?

Without quotes, `$1` can be split if it contains spaces. Example: `cp $file backup` fails if $file is "my document.txt", but `cp "$file" backup` treats it as one item. **Always quote variables**.

---

Can functions modify variables outside their scope?

Yes, unless declared `local`. Variables in functions are global by default. Use `local var=value` to limit scope to the function.

---

## Function Examples

```bash
# Simple greeting function
greet() {
    echo "Hello, $1"
}

greet "Alice"     # Output: Hello, Alice
greet "Bob"       # Output: Hello, Bob

# Function with multiple parameters
add() {
    local sum=$(($$1 + $2))
    echo $sum
}

result=$(add 5 10)
echo "Sum: $result"

# Function with return code
file_exists() {
    if [ -f "$1" ]; then
        echo "File $1 exists"
        return 0
    else
        echo "File $1 not found"
        return 1
    fi
}

# Check return code
file_exists "/etc/passwd"
if [ $? -eq 0 ]; then
    echo "Check passed"
fi

# Function with local variables
backup_files() {
    local source=$1
    local dest=$2
    local timestamp=$(date +%Y%m%d_%H%M%S)

    tar -czf "$dest/backup_${timestamp}.tar.gz" "$source"
    echo "Backup created: $dest/backup_${timestamp}.tar.gz"
}

backup_files "/home/user" "/backups"

# Function with error handling
process_file() {
    local file=$1

    if [ ! -f "$file" ]; then
        echo "Error: file not found: $file" >&2
        return 1
    fi

    # Process file
    wc -l "$file"
    return 0
}

# Usage with error checking
process_file "data.txt" || echo "Failed to process"
```

## Advanced Examples

```bash
# Function that processes multiple files
process_all() {
    for file in "$@"; do
        echo "Processing: $file"
        # do something with $file
    done
}

process_all file1.txt file2.txt file3.txt

# Function with default parameters
greet_with_default() {
    local name=${1:-"Guest"}
    echo "Hello, $name"
}

greet_with_default              # Hello, Guest
greet_with_default "Alice"      # Hello, Alice

# Recursive function
factorial() {
    local n=$1
    if [ $n -le 1 ]; then
        echo 1
    else
        local prev=$(factorial $((n - 1)))
        echo $((n * prev))
    fi
}

result=$(factorial 5)
echo "5! = $result"

# Function with output capture
get_system_info() {
    local uptime=$(uptime)
    local user=$(whoami)
    echo "User: $user, Uptime: $uptime"
}

info=$(get_system_info)
echo "$info"
```

## Best Practices

```bash
# GOOD: Clear naming
backup_database() {
    # ...
}

validate_email() {
    # ...
}

# GOOD: Local variables
my_function() {
    local temp_var="value"  # Local to function
    global_var="value"      # Global variable
}

# GOOD: Quote parameters
copy_file() {
    cp "$1" "$2"  # Quotes prevent word splitting
}

# GOOD: Error handling
safe_delete() {
    if [ -f "$1" ]; then
        rm "$1"
        return 0
    else
        echo "Error: file not found" >&2
        return 1
    fi
}

# BAD: Unquoted parameters
copy_file() {
    cp $1 $2  # Will fail with spaces in filename
}
```

## Related Notes

- [[Bash variables store data and command output for reuse in scripts]]
- [[Bash positional parameters access command-line arguments as numbered variables]]
- [[Bash if statements execute commands conditionally using test operators for comparison]]
- [[Bash loops iterate over lists with for or repeat while conditions are true]]
- [[Shell scripts automate Linux tasks by combining multiple commands in a text file]]

## Flashcards

?
What is the basic function syntax?

`function_name() { commands here; }`

---

?
How do functions receive arguments?

Via positional parameters: `$1`, `$2`, `$#`, `$@`

---

?
How do you call a function with arguments?

`function_name arg1 arg2`

---

?
What does the return statement do?

Sets the **exit code**: `0` for success, non-zero for failure.

---

?
How do you check a function's return code?

Use `$?` immediately after calling: `my_function; if [ $? -eq 0 ]; then ...`

---

?
What does echo output compared to return?

**echo** outputs text to stdout, **return** sets the exit code only.

---

?
What does the local keyword do?

Limits a variable's scope to the **function only**.

---

?
Why should you always quote variables in functions?

To prevent **word splitting** if the variable contains spaces: `"$1"` not `$1`

---

?
Can functions modify global variables?

Yes, unless declared `local`. Global variables are accessible and modifiable by default.

---

?
Must function definitions come before calls?

Yes, functions must be **defined before they're called** in the script.
