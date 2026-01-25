
### Syntax

```bash
read variable_name
```

### With Prompt:

```bash
read -p "Enter your name: " name
echo "Hello, $name"
```

### Examples

```bash
#!/bin/bash

# Simple read
echo "Enter your age:"
read age
echo "You are $age years old"

# Read with prompt (-p flag)
read -p "Enter username: " username
read -p "Enter password: " password

# Read multiple values
read -p "Enter first and last name: " first last
echo "Hello $first $last"

# Read entire line (including spaces)
read -p "Enter your address: " address

# Read with default value
read -p "Enter name [John]: " name
name=${name:-John}  # Use "John" if empty
echo "Name: $name"

# Silent input (for passwords)
read -sp "Enter password: " password
echo ""  # New line after input
```