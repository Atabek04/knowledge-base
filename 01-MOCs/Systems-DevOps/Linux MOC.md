---
created: 2026-01-12
tags: [moc]
---

Operating system fundamentals, Linux kernel architecture, Unix/Linux history, and system management concepts.

## Part 1 — OS Fundamentals

### Core Concepts

- [[Kernel is the core OS program with complete control over system]] — first program after bootloader, manages all resources
- [[Operating system mediates between applications and hardware for security and abstraction]] — prevents direct hardware access
- [[Operating system prevents direct hardware access for security, abstraction, and resource coordination]] — reasons for OS mediation
- [[Applications communicate with operating system through system calls]] — the bridge between user programs and kernel

### User Interface

- [[GUI and CLI are applications that mediate between users and kernel through system calls]] — graphical vs command-line interfaces
- [[Linux terminal prompt shows username, hostname, current directory, and user privilege level]] — understanding the prompt format
- [[Shell interprets user commands and translates them into system calls for the kernel]] — shell as intermediary between user and kernel
- [[Every program has 3 built-in streams - stdin, stdout, stderr]] — standard input/output/error streams

## Part 2 — Linux History & Philosophy

### Unix Origins

- [[Unix is a foundational operating system created in 1969 that influenced modern operating system design]] — Bell Labs creation and Unix philosophy
- [[Berkeley Software Distribution became open source when Unix source code was leaked]] — BSD variants and history
- [[POSIX is a standard specification that ensures operating system compatibility and portability]] — standardizing Unix interfaces

### Linux Creation

- [[Linus Torvalds created Linux in 1991 as an open-source alternative to proprietary Minix]] — birth of Linux kernel
- [[Linux is the kernel while Linux distributions package the kernel with tools and utilities]] — kernel vs complete OS

## Part 3 — System Architecture

### Process Management

- [[Process is an instance of a program in execution with isolated memory space and resources]] — what processes are
- [[Context switch allows one CPU core to execute multiple processes by rapidly switching between them]] — how multitasking works

### Memory Management

- [[RAM provides fast temporary storage while hard disk provides large persistent storage]] — complementary roles
- [[CPU cannot directly access hard disk because of speed and interface differences, requiring RAM as intermediary]] — why RAM is necessary
- [[Memory swapping extends RAM by moving unused data to hard disk when RAM is full]] — extending RAM capacity

### Filesystem

- [[Linux root filesystem uses a hierarchical tree structure with standardized directories for different purposes]] — FHS directory layout

## Part 3.5 — Command-Line Tools & Shell Scripting

### Command-Line Utilities

- [[ls command displays files with options for hidden files and detailed format]] — listing files with options
- [[grep searches files for lines matching text patterns using regular expressions]] — text pattern matching and filtering
- [[less command displays files one screen at a time with navigation and search]] — pager for efficient file viewing
- [[Pipe operator chains Linux commands by connecting stdout of one to stdin of another]] — command composition and data flow
- [[Output redirection operators write command output to files in Linux]] — redirecting stdout and stderr

### Shell Scripting Fundamentals

- [[Shell scripts automate Linux tasks by combining multiple commands in a text file]] — automation and task composition
- [[Shebang tells the operating system which interpreter should execute a script]] — script execution headers
- [[Bash variables store data and command output for reuse in scripts]] — variables and command substitution
- [[Bash positional parameters access command-line arguments as numbered variables]] — handling script arguments
- [[Bash read command captures user input from stdin during script execution]] — interactive user input
- [[Bash if statements execute commands conditionally using test operators for comparison]] — conditional execution
- [[Bash loops iterate over lists with for or repeat while conditions are true]] — iteration and repetition
- [[Bash functions encapsulate reusable code blocks that accept parameters and return exit codes]] — code modularity and reuse

## Part 4 — Package Management

### Package Concepts

- [[Software packages bundle application files and metadata into compressed archives for distribution]] — what packages are
- [[Package managers automate software installation by resolving dependencies and managing file locations]] — role of package managers
- [[Linux distributions use different package managers - APT for Debian family and YUM for RedHat family]] — distribution-specific tools
- [[Software repositories are centralized storage locations where package managers fetch packages from]] — where packages come from

### Package Manager Tools

- [[apt is more user-friendly than apt-get with progress bars and organized commands]] — modern APT interface
- [[Snap packages are self-contained with bundled dependencies while APT packages share dependencies]] — alternative packaging systems
- [[PPAs provide community-maintained package repositories with no quality or security guarantees]] — extending package sources

## Part 5 — User Management & Permissions

### User Categories

- [[Linux has three user categories - superuser, user account, and service account]] — role-based user types
- [[Separate user accounts enable accountability through audit logs and granular permission control]] — multi-user benefits

### Permission Systems

- [[Linux file ownership assigns files to users and groups for permission control]] — user and group ownership
- [[Linux file permissions control read, write, and execute access for owner, group, and others]] — rwx permissions and chmod
- [[Linux permission management operates at user level and group level]] — two-tier permission model
- [[Every Linux user must have exactly one primary group but can have multiple secondary groups]] — group membership rules

### System Configuration

- [[Linux stores user configuration in plain text files under /etc directory]] — where user data lives
- [[User management commands like useradd and usermod safely modify system user configuration]] — command-line user administration
- [[LDAP and FreeIPA provide centralized authentication for Linux similar to Active Directory on Windows]] — enterprise authentication

## Related MOCs

- [[VMs & Containers MOC]] — virtualization, containers, kernel namespaces, cgroups
- [[Networking MOC]] — network protocols and communication

## Practice

(Flashcards to be added)

## External Resources

- [Linux man pages](https://man7.org/)
- [Linux Kernel Documentation](https://www.kernel.org/doc/)
- [The Linux Command Line](https://linuxcommand.org/)
