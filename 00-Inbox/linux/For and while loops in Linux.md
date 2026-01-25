
## For Loop
### Syntax

```bash
for variable in list
do
	# commands here
done
```

### Examples

```bash
for file in *.txt
do
	mv "$file" "${file%.txt}.md"
done
```

These coverts all `.txt` files to `.md`
Each filename gets stored in `$file`, one by one.

---

```bash
for server in prod-1 prod-2 prod-3
do
	echo "checking ${server}..."
	ssh ${server} "uptime"
done
```

Less repetition, easier to add new servers.

---

```bash
for i in {1..10}
do
	mkdir "backup-$i"
done
```

Creates 10 directories: backup-1, ... backup-10

---

## While Loop

### Syntax

```bash
while [ condition ]
do
	# commands here
done
```

### Example

```bash
attempts=0
while [ $attempts -lt 3 ]
do
	if curl -s https://api.example.com > /dev/null
	then
		echo "API is up"
		break
	fi
	attempts=$((attempts + 1))
	sleep 2
done
```