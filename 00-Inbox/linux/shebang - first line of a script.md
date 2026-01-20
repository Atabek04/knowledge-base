
### Why it's called `shebang`

Because of the first 2 characters: `#!`
- `#` - in musical notation, also called sharp
- `!` - also called *bang*
- Shebang became a shortening of sharp-bang

### What's the `shebang`

`shebang` is the first line of a script:
`#!<interpreter_path>`

Tells the OS which program should exec the script.

### Purpose

Allows running scripts directly, without specifying interpreter:

```bash
./script.sh
```

Without `shebang`, you'd need:

```bash
python3 script.py

bash script.sh
```

### Examples:

```bash
#!/bin/bash
# Shell script
```

```bash
#!/usr/bin/python3
# Python script
```

```bash
#!/usr/bin/env python3
# Python (finds python3 in PATH)
```

```bash
#!/usr/bin/perl
# Perl script
```

```bash
#!/usr/bin/env node
# Node.js script
```