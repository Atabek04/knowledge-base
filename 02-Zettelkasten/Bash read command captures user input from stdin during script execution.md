---
created: 2026-01-21
tags: [linux, bash, scripting, input, read-command]
---

The `read` command captures user input from **stdin** and stores it in a variable during script execution. It's the primary way to make scripts interactive by prompting users for data. The `-p` flag displays a prompt, and the `-s` flag hides input (useful for passwords).

## What does the read command do?

The `read` command pauses script execution and waits for the user to type input, then stores it in a specified variable. Basic syntax: `read variable_name`

---

How do you display a prompt with read?

Use the `-p` flag: `read -p "Enter your name: " name`. The prompt appears immediately and the cursor waits on the same line.

---

How do you read multiple values into separate variables?

Use: `read -p "Enter first and last name: " first last`. The input is split on whitespace and stored in multiple variables.

---

How do you read a password silently without echoing characters?

Use the `-s` flag: `read -sp "Enter password: " password`. The `-s` flag suppresses echo (silent), and add `echo ""` after to print a newline.

---

What is the difference between read and read -r?

`read` processes backslashes as escape characters and strips leading/trailing whitespace. `read -r` (raw mode) preserves backslashes literally. Use `-r` when you need exact input.

---

How do you provide a default value if the user presses Enter without input?

Use the parameter expansion: `read -p "Enter name [John]: " name; name=${name:-John}`. This uses "John" if the variable is empty.

---

## Common read Flags

| Flag | Purpose |
|------|---------|
| `-p prompt` | Display prompt text |
| `-s` | Silent mode (hide input, for passwords) |
| `-r` | Raw mode (preserve backslashes) |
| `-t seconds` | Timeout (stop waiting after N seconds) |
| `-n num` | Read only N characters |
| `-e` | Use readline for editing (like command line) |

## Examples

```bash
# Simple read
echo "Enter your age:"
read age
echo "You are $age years old"

# Read with prompt
read -p "Enter username: " username
echo "Hello, $username"

# Read password silently
read -sp "Enter password: " password
echo ""  # New line after silent input
echo "Password stored"

# Read multiple values
read -p "Enter first and last name: " first last
echo "Hello $first $last"

# Read with default
read -p "Enter name [John]: " name
name=${name:-John}
echo "Name: $name"

# Read with timeout (5 seconds)
read -t 5 -p "Enter value (5 sec timeout): " value

# Read exactly 1 character
read -n 1 -p "Continue? (y/n): " response

# Read from file into variable
read -p "Filename: " filename
if read -r line < "$filename"; then
    echo "First line: $line"
fi

# Read entire line including spaces
read -p "Enter your address: " address
echo "Address: $address"
```

## Interactive Script Example

```bash
#!/bin/bash
# Interactive user info collection

read -p "Enter your name: " name
read -p "Enter your age: " age
read -p "Enter your email: " email

# Confirm before proceeding
echo "You entered:"
echo "  Name: $name"
echo "  Age: $age"
echo "  Email: $email"

read -p "Is this correct? (y/n): " confirm

if [ "$confirm" = "y" ]; then
    echo "Saving user data..."
    # Process data
else
    echo "Please try again"
    exit 1
fi
```

## Login Script Example

```bash
#!/bin/bash
# Simple login simulation

read -p "Username: " username
read -sp "Password: " password
echo ""

if [ "$username" = "admin" ] && [ "$password" = "secret123" ]; then
    echo "Login successful!"
else
    echo "Invalid credentials"
    exit 1
fi
```

## Related Notes

- [[Bash variables store data and command output for reuse in scripts]]
- [[Bash positional parameters access command-line arguments as numbered variables]]
- [[Bash if statements execute commands conditionally using test operators for comparison]]
- [[Every program has 3 built-in streams - stdin, stdout, stderr]]
- [[Shell scripts automate Linux tasks by combining multiple commands in a text file]]

## Flashcards

?
What does the read command do?

Captures **user input** from **stdin** and stores it in a variable.

---

?
How do you display a prompt with read?

Use the `-p` flag: `read -p "Enter value: " variable`

---

?
How do you hide input (for passwords)?

Use the `-s` flag: `read -sp "Enter password: " password`

---

?
How do you read multiple values into separate variables?

`read -p "Enter two values: " var1 var2`

---

?
What does -r do with read?

Preserves backslashes and special characters (**raw mode**).

---

?
How do you set a timeout for read?

Use the `-t` flag: `read -t 5 -p "Enter value: " var`

---

?
How do you read only 1 character?

`read -n 1 -p "Continue? (y/n): " response`

---

?
How do you provide a default value if user presses Enter?

`read -p "Name [John]: " name; name=${name:-John}`
