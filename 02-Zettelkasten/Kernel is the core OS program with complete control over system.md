---
created: 2026-01-06
tags: [linux/fundamentals]
---

The **kernel** is the core program of an operating system with complete control over all system resources.

It is the first program loaded after the bootloader and remains in memory until system shutdown.

The kernel never terminates during normal system operation—it stays resident in **protected memory** that user programs cannot access or modify.

This ensures the kernel can always respond to **system calls** and hardware interrupts.

## How users interact with kernel

The kernel is invisible to users.

You interact with it through programs like shell, terminal, and applications that make **system calls** to request kernel services.

The kernel has exclusive access to hardware and mediates all access from user programs.

## Main responsibilities

**Process Management** — creates, schedules, and terminates processes.

The kernel decides which process runs on CPU at any moment using the **scheduler**.

**Memory Management** — allocates and deallocates RAM to processes.

Protects processes from accessing each other's memory and manages virtual memory using disk.

**Device Management** — communicates with hardware like disk, network, and keyboard through **device drivers**.

Programs cannot talk to hardware directly—they must request the kernel to do it.

**System Call Handling** — provides the interface through which user programs request kernel services.

Operations like reading files, writing to network, or allocating memory all go through system calls.

![[kernel-diagram.png]]

![[kernel-responsibilities.png]]

## Enforcement and isolation

The kernel enforces these responsibilities strictly.

A buggy application cannot crash other applications or access their data—the kernel isolates them.

This is the fundamental difference between modern operating systems and early computers where programs had direct hardware access.

## Links

- [[User Space and Kernel Space represent two CPU privilege modes]]
- [[System calls provide the bridge from user programs to kernel services]]
- [[CPU mode switch transitions from User Mode to Kernel Mode during syscalls]]
- [[VMs & Containers MOC]]
- [[Linux MOC]]
