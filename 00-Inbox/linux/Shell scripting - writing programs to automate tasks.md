
> **Shell scripting** - writing program in a shell program in a shell language (bash, sh, zsh) to automate tasks.
---
### Why

- automate repetitive commands
- chain multiple tools together
- run scheduled jobs (cron)

---
### Example

```bash
#!/bin/bash
# Simple backup script

backup_dir="/backups"
mkdir -p $backup_dir
tar -czf $backup_dir/backup_$(date +%Y%m%d).tar.gz /home/user/data
echo "Backup completed"
```

