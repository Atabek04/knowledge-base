---
created: 2026-01-12
tags: [moc]
---

Operating system fundamentals, Linux kernel architecture, Unix/Linux history, and system management concepts.

## Part 1 — OS Fundamentals

### Core Concepts

- [[Kernel is the core OS program with complete control over system|Kernel: core OS program with total control]]
- [[Operating system mediates between applications and hardware for security and abstraction|OS mediates between apps and hardware]]
- [[Operating system prevents direct hardware access for security, abstraction, and resource coordination|Why the OS blocks direct hardware access]]
- [[Applications communicate with operating system through system calls|Apps reach the kernel via system calls]]

### User Interface

- [[GUI and CLI are applications that mediate between users and kernel through system calls|GUI and CLI both mediate via system calls]]
- [[Linux terminal prompt shows username, hostname, current directory, and user privilege level|Prompt: user, host, dir, privilege level]]
- [[Shell interprets user commands and translates them into system calls for the kernel|Shell translates commands into system calls]]
- [[Every program has 3 built-in streams - stdin, stdout, stderr|Three streams: stdin, stdout, stderr]]

## Part 2 — Linux History & Philosophy

### Unix Origins

- [[Unix is a foundational operating system created in 1969 that influenced modern operating system design|Unix (1969): foundation of modern OSes]]
- [[Berkeley Software Distribution became open source when Unix source code was leaked|BSD went open source after a Unix leak]]
- [[POSIX is a standard specification that ensures operating system compatibility and portability|POSIX standardizes OS interfaces for portability]]

### Linux Creation

- [[Linus Torvalds created Linux in 1991 as an open-source alternative to proprietary Minix|Torvalds created Linux (1991) vs Minix]]
- [[Linux is the kernel while Linux distributions package the kernel with tools and utilities|Linux = kernel; distros add tools]]

## Part 3 — System Architecture

### Process Management

- [[Process is an instance of a program in execution with isolated memory space and resources|Process: a running program with isolated memory]]
- [[Context switch allows one CPU core to execute multiple processes by rapidly switching between them|Context switch: one core runs many processes]]

### Memory Management

- [[RAM provides fast temporary storage while hard disk provides large persistent storage|RAM: fast/temporary; disk: large/persistent]]
- [[CPU cannot directly access hard disk because of speed and interface differences, requiring RAM as intermediary|CPU can't reach disk directly; RAM bridges]]
- [[Memory swapping extends RAM by moving unused data to hard disk when RAM is full|Swapping extends RAM onto disk]]

### Filesystem

- [[Linux root filesystem uses a hierarchical tree structure with standardized directories for different purposes|Root filesystem: standardized directory tree (FHS)]]

### Task Scheduling

- [[Cron runs commands on a schedule defined by a five-field time expression|Cron — a daemon that matches wall-clock time against five-field job lines]]

## Part 3.5 — Command-Line Tools & Shell Scripting

### Command-Line Utilities

- [[ls command displays files with options for hidden files and detailed format|ls lists files (hidden, detailed)]]
- [[grep searches files for lines matching text patterns using regular expressions|grep matches lines by regex]]
- [[sed performs stream editing for find-and-replace on text|sed: stream find-and-replace]]
- [[find searches filesystem for files by name, type, or attributes|find locates files by name/type/attribute]]
- [[cat concatenates files and prints contents to stdout|cat dumps or merges files]]
- [[Heredoc passes multi-line text as stdin using cat and EOF marker|Heredoc: multi-line stdin via an EOF marker]]
- [[test command checks file properties and compares values in shell|test: file/string/integer checks ([ ... ])]]
- [[less command displays files one screen at a time with navigation and search|less: paged file viewing with search]]
- [[Pipe operator chains Linux commands by connecting stdout of one to stdin of another|Pipe chains stdout → stdin]]
- [[Output redirection operators write command output to files in Linux|Redirection writes output to files]]
- [[2 greater than ampersand 1 redirects stderr to the same place as stdout|2>&1 merges stderr into stdout]]

### Network & JSON CLI Tools

- [[curl transfers data to and from servers over many protocols|curl: transfer data over many protocols]]
- [[jq parses, filters, and transforms JSON data on the command line|jq: parse/filter/transform JSON in the shell]]

### Shell Scripting Fundamentals

- [[Shell scripts automate Linux tasks by combining multiple commands in a text file|Shell scripts automate command sequences]]
- [[Shebang tells the operating system which interpreter should execute a script|Shebang picks the script's interpreter]]
- [[Bash variables store data and command output for reuse in scripts|Bash variables store data and command output]]
- [[Bash positional parameters access command-line arguments as numbered variables|Positional parameters: numbered script args]]
- [[Bash read command captures user input from stdin during script execution|read captures user input from stdin]]
- [[Bash if statements execute commands conditionally using test operators for comparison|Bash if: conditional execution via test]]
- [[Bash loops iterate over lists with for or repeat while conditions are true|Bash loops: for over lists, while on condition]]
- [[Bash functions encapsulate reusable code blocks that accept parameters and return exit codes|Bash functions: reusable blocks with exit codes]]

## Part 4 — Package Management

### Package Concepts

- [[Software packages bundle application files and metadata into compressed archives for distribution|Packages bundle files + metadata in an archive]]
- [[Package managers automate software installation by resolving dependencies and managing file locations|Package managers resolve deps and place files]]
- [[Linux distributions use different package managers - APT for Debian family and YUM for RedHat family|APT (Debian) vs YUM (RedHat)]]
- [[Software repositories are centralized storage locations where package managers fetch packages from|Repositories: where packages are fetched from]]

### Package Manager Tools

- [[apt is more user-friendly than apt-get with progress bars and organized commands|apt is friendlier than apt-get]]
- [[Snap packages are self-contained with bundled dependencies while APT packages share dependencies|Snap bundles deps; APT shares them]]
- [[PPAs provide community-maintained package repositories with no quality or security guarantees|PPAs: community repos, no guarantees]]

## Part 5 — User Management & Permissions

### User Categories

- [[Linux has three user categories - superuser, user account, and service account|Three user types: superuser, user, service]]
- [[Separate user accounts enable accountability through audit logs and granular permission control|Separate accounts enable accountability]]

### Permission Systems

- [[Linux file ownership assigns files to users and groups for permission control|File ownership: user + group]]
- [[Linux file permissions control read, write, and execute access for owner, group, and others|Permissions: rwx for owner/group/others]]
- [[Linux permission management operates at user level and group level|Permissions at user and group level]]
- [[Every Linux user must have exactly one primary group but can have multiple secondary groups|One primary group, many secondary groups]]

### System Configuration

- [[etc directory|/etc: system configuration directory]]
- [[User management commands like useradd and usermod safely modify system user configuration|useradd / usermod modify user config safely]]
- [[LDAP and FreeIPA provide centralized authentication for Linux similar to Active Directory on Windows|LDAP / FreeIPA: centralized auth (like AD)]]

## Related MOCs

- [[VMs & Containers MOC]] — virtualization, containers, kernel namespaces, cgroups
- [[Networking MOC]] — network protocols and communication

## Practice

(Flashcards to be added)

## External Resources

- [Linux man pages](https://man7.org/)
- [Linux Kernel Documentation](https://www.kernel.org/doc/)
- [The Linux Command Line](https://linuxcommand.org/)
