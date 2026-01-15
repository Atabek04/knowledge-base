
### Superuser (Root)

Root user - unrestricted permissions
For admin tasks:
- login as root (`su -` or `sudo -i`)
- execute as root with `sudo`

---
### User Account

Regular user we create to log in
Each user has its own file system inside `/home` (e.g. `/home/ayub`)

---
### Service Account

Relevant for Linux Server Distros
Those servers to run different services like DB, app etc.

In one machine, you may have multiple regular users and service users.

> Each service will get its own user
> e.g. `mysql` user will start `mysql` application
> best practice for security

> <mark style="background: #FF5582A6;">DON'T RUN WITH ROOT USER!</mark>