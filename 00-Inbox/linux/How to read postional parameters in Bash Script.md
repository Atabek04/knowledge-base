
```bash
# $0 = script name
# $1 = first parameter
# $2 = second parameter
# etc.

# Example script: script.sh
./script.sh arg1 arg2 arg3
```

### Parameter Variables

```bash
echo $0          # Output: ./script.sh
echo $1          # Output: arg1
echo $2          # Output: arg2
echo $#          # Output: 3 (total parameters)
echo $@          # Output: arg1 arg2 arg3 (all params)
echo $*          # Output: arg1 arg2 arg3 (all as string)
```

### Example

```bash
#!/bin/bash
# backup.sh <source> <destination>

source=$1
destination=$2

if [ -z "$source" ]; then
  echo "Usage: backup.sh <source> <destination>"
  exit 1
fi

cp -r "$source" "$destination"
echo "Backup completed: $source -> $destination"
```

```bash
./backup.sh /home/user /backups/user
```