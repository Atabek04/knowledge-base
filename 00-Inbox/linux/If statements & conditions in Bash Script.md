
### Basic Syntax

```bash
if [ condition ]; then
	# commands if true
elif [ condition ]; then
	# commands if second condition true
else
	# commands if all false
fi
```

### Test operators

```bash
# String comparisons
[ "$var" = "value" ]      # Equal
[ "$var" != "value" ]     # Not equal
[ -z "$var" ]             # Empty string
[ -n "$var" ]             # Not empty

# Numeric comparisons
[ $num -eq 5 ]            # Equal
[ $num -ne 5 ]            # Not equal
[ $num -lt 5 ]            # Less than
[ $num -gt 5 ]            # Greater than
[ $num -le 5 ]            # Less or equal
[ $num -ge 5 ]            # Greater or equal

# File tests
[ -f file.txt ]           # File exists
[ -d /path ]              # Directory exists
[ -r file.txt ]           # Readable
[ -w file.txt ]           # Writable
[ -x script.sh ]          # Executable
```

### Example

```bash
# Simple if
if [ $age -ge 18 ]; then
  echo "Adult"
fi

# If-else
if [ -f "$file" ]; then
  echo "File exists"
else
  echo "File not found"
fi

# If-elif-else
if [ $score -ge 90 ]; then
  echo "A"
elif [ $score -ge 80 ]; then
  echo "B"
else
  echo "C"
fi

# Multiple conditions
if [ $age -ge 18 ] && [ $score -ge 80 ]; then
  echo "Qualified"
fi

# Logical operators
[ $x -eq 1 ] && [ $y -eq 2 ]     # AND
[ $x -eq 1 ] || [ $y -eq 2 ]     # OR
```