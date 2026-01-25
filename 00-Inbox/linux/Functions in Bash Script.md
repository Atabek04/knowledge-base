
### Why Functions

- **Better overview** when they're **named descriptively**
- Reuse code
- Enable you to break down the overall functionality of a script into smaller logical code blocks

### Syntax

```bash
function_name() {
	# commands here
	return value
}

# or with function keyword

function function_name {
	# commands here
}
```

> ⚠️ Functions must be defined before you call them.

---
### Examples

```bash
greet() {
	echo "Hello, $1"
}

greet "Alice"
greet "Bob"
```

`$1` mean the first argument passed to the function.

---

```bash
file_exists() {
	if [ -f "$1"]
	then
		echo "File $1 exists"
		return 0
	else
		echo "File $1 not found"
		return 1
	fi
}

file_exists "/etc/passwd"

if [ $? eq 0 ]
then
	echo "Check passed"
fi
```

> `$?` hold the return code of the last command
> `0` means true, `1` failure.

>Quotes prevent word splitting
>
>**Without quotes:**
>If `$file` is `my document.txt`, bash splits it at the space.
>Bash tries to copy `my` and `document.txt` separately
>fails ☣️
>
>**With quotes:**
>`cp "$file" /backup`
>Bash treats `my document.txt` as one thing
>works ✔️