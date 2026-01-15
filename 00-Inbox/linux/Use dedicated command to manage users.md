
### Why Not Edit Directly

> Use dedicated commands to manage users
> instead of editing access control files in `/etc/`

Manual editing is error-prone.
One typo breaks auth system.

Multiple files must stay synchronized
Commands handle this automatically and safely.

---
### Common User Management Commands
#### Add new user

```bash
sudo useradd username  # minimal
sudo useradd -m -s /bin/bash username  # w/ home dir and shell
sudo adduser username  # interactive (debain/Ubuntu)
```

---
#### Set / Change password

```bash
sudo passwd username
```

---
#### Modify user

```bash
sudo usermod -aG groupname username # add a secondary group
sudo usermod -g groupname username # change primary group
sudo usermod -s /bin/zsh username # change shell
```

---
#### Delete user

```bash
sudo userdel username  # keep home dir
sudo userdel -r username  # remove home dir too
```

---
#### Group Management

```bash
sudo groupadd groupname  # create group
sudo groupdel groupname  # delete group
groups username  # show user's groups
```