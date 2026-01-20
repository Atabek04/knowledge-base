
`ls -a` - prints all files and folders
	doesn't ignore entries starting with `.`

`ls -l` - will use long listing format, which will include:

  1. Permissions 
     (10 chars: file type + `rwx` for owner/group/others)
  2. Hard links count
  3. Owner (user)
  4. Owner group
  5. Size (bytes)
  6. Modification date
  7. Modification time
  8. Filename

  Example:
```bash
-rw-r--r-- 1 user group 1024 Jan 20 10:30 file.txt
```
