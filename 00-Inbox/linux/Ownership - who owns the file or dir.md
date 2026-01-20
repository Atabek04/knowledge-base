
> Owner is the user, who created the file.

Ownership can be applied for two things:
1. File 
2. Directory

```bash
-rw-r--r-- 1 user group 1024 Jan 20 10:30 file.txt
```

---

### Changing ownership

```bash
chown <username>:<group> <filename>

sudo chown tom:admin test.txt
```

#### To change only user ownership

```bash
chown <username> <filename>
```

#### To change only group ownership

```bash
chgrp <group> <filename>
```