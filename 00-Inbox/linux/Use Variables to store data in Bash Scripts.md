
### Creating Variables

```bash
variable_name=value

name="John"
age=30
count=0
```

> ⚠️Note: there must be NO spaces around the equal sign

---
### Retrieving Variables

```bash
$variable_name
${variable_name}

echo $name
echo ${age}
```

Use {} for clarity, especially with concatenation:

```bash
echo "Name: ${name}"    # Clearer than $name
```

---

### Store command output in variable

```bash
variable=$(command)

today=$(date +%Y-%m-%d)
echo $today             # Output: 2026-01-20

# Store grep result
errors=$(grep "error" logs.txt)
echo $errors

# Store file list
files=$(ls -1 /home)
echo $files
```