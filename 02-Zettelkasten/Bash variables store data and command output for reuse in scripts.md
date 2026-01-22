---
created: 2026-01-21
tags: [linux, bash, scripting, variables]
---

Bash variables store data values (strings, numbers, command output) for reuse throughout scripts. Variables are created with `variable_name=value` syntax and referenced with `$variable_name` or `${variable_name}`. They're fundamental for storing configuration, results, and arguments in shell scripts.

## How do you create a variable in Bash?

Use the syntax `variable_name=value` with **no spaces around the equal sign**. Example: `name="John"`, `age=30`, `count=0`.

---

How do you retrieve the value of a variable?

Use `$variable_name` or `${variable_name}`. The curly braces are optional but recommended for clarity, especially when concatenating: `echo "Name: ${name}"`

---

How do you store command output in a variable?

Use **command substitution** with `$()`: `variable=$(command)`. Example: `today=$(date +%Y-%m-%d)` or `errors=$(grep "error" logs.txt)`

---

What is the difference between $variable_name and ${variable_name}?

They're functionally identical, but `${variable_name}` is more explicit and avoids issues with concatenation. For example, `echo $name_suffix` looks for a variable called "name_suffix", but `echo ${name}_suffix` prints the value of "name" followed by "_suffix".

---

Can you store multi-line output in a variable?

Yes, command substitution preserves all output. Example: `file_list=$(ls -1 /home)` stores the entire directory listing. Use `"${variable}"` with quotes to preserve line breaks and spaces.

---

What special variables does Bash provide?

**$0** (script name), **$#** (number of parameters), **$@** (all parameters as separate values), **$?** (exit status of last command), **$HOME** (user home directory), **$PATH** (command search paths).

---

## Variable Examples

```bash
# Create variables
name="Alice"
age=30
balance=1500.50

# Use variables
echo "Name: $name"
echo "Age: $age"
echo "Balance: $balance"

# Store command output
current_date=$(date +%Y-%m-%d)
user_count=$(wc -l < /etc/passwd)
files=$(ls /home)

# String concatenation
greeting="Hello, ${name}!"
echo $greeting

# Arithmetic
count=5
count=$((count + 1))
echo $count  # Output: 6

# Using special variables
echo "Script: $0"
echo "Total args: $#"
echo "All args: $@"

# Conditional variable use
username="${1:-defaultuser}"  # Use $1 or "defaultuser" if empty
```

## Variable Naming Conventions

```bash
# Good practices
my_var="value"           # lowercase with underscores
CONSTANT_VALUE="fixed"   # UPPERCASE for constants
temp_file="/tmp/data"    # descriptive names

# Avoid
myVar="value"            # camelCase not preferred in bash
1var="value"             # can't start with number
my-var="value"           # hyphens not allowed
```

## Scope and Unset

```bash
# Define local variable in function
function my_function() {
    local local_var="only in function"
    global_var="visible outside"
}

# Unset a variable
unset variable_name

# Check if variable is set
if [ -z "$variable" ]; then
    echo "Variable is empty or unset"
fi

if [ -n "$variable" ]; then
    echo "Variable has a value"
fi
```

## Related Notes

- [[Bash positional parameters access command-line arguments as numbered variables]]
- [[Bash read command captures user input from stdin during script execution]]
- [[Bash if statements execute commands conditionally using test operators for comparison]]
- [[Shell scripts automate Linux tasks by combining multiple commands in a text file]]

## Flashcards

?
How do you create a Bash variable?

`variable_name=value` with **no spaces** around the `=`

---

?
How do you reference a variable's value?

Use `$variable_name` or `${variable_name}`

---

?
How do you store command output in a variable?

Use command substitution: `variable=$(command)`

---

?
What's the difference between `$var` and `${var}`?

They're equivalent, but `${var}` is clearer and avoids concatenation issues.

---

?
How do you get the number of arguments passed to a script?

Use the special variable `$#`

---

?
How do you get all arguments passed to a script?

Use `$@` (all as separate) or `$*` (all as single string)

---

?
What does $0 represent?

The **script name** itself.

---

?
How do you store multi-line command output?

Command substitution automatically preserves lines: `output=$(cat file.txt)`

---

?
Can variables be empty?

Yes, `empty_var=""` creates an empty variable. Use `[ -z "$var" ]` to test if empty.
