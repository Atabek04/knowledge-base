---
created: 2026-01-12
tags: [linux/interface]
---

The Linux terminal prompt displays critical information: who you are, where you are, and your privilege level.

## Prompt format

```
username@hostname:current_directory$
```

**Examples:**
```
john@laptop:~$
alice@server01:/var/log$
root@db-prod:/home#
```

## Each component explained

| Part | Meaning | Example values |
|------|---------|----------------|
| **username** | Who you are logged in as | `john`, `alice`, `root` |
| **@** | Separator (means "at") | — |
| **hostname** | Computer/server name | `laptop`, `server01`, `db-prod` |
| **:** | Separator | — |
| **directory** | Where you are in filesystem | `~`, `/tmp`, `/var/log` |
| **$ or #** | Privilege level | `$` (user), `#` (root) |

## Understanding tilde (~)

The **tilde** is a shortcut for the user's home directory.

| User | `~` means |
|------|-----------|
| `john` | `/home/john/` |
| `alice` | `/home/alice/` |
| `root` | `/root/` |

## Why hostname matters

When managing multiple servers, the hostname tells you WHERE you are.

**Example scenario managing 3 servers:**

```
john@web-server:~$      ← You're on web server (safe to restart)
john@db-prod:/var/log#  ← You're on production database (CAREFUL!)
john@backup-01:~$       ← You're on backup server
```

Without hostname display, you risk running commands on the wrong server, potentially deleting production data or restarting critical services.

## User privilege: $ vs #

| Symbol | User type | Caution level |
|--------|-----------|---------------|
| **$** | Regular user | Limited permissions, safe |
| **#** | Root user | Full access, DANGEROUS |

**Example:**
```
john@laptop:~$    ← Regular user, safe to experiment
john@laptop:~#    ← Root user, one mistake breaks the system
```

## Links

- [[GUI and CLI are applications that mediate between users and kernel through system calls]]
- [[Linux root filesystem uses a hierarchical tree structure with standardized directories for different purposes]]
- [[Linux MOC]]
