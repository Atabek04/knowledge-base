---
created: 2025-12-12
tags:
  - topic/subtopic
sr-due:
sr-interval:
sr-ease:
---
## <mark style="background: #ADCCFFA6;">What's the Socket?</mark>

Socket is just a **software construct**.
	It's not a protocol
	It's just an **OS object** for apps **to access the network**

**<mark style="background: #BBFABBA6;">Protocols</mark>** such as `HTTP`, `TCP`, `IP` are just **<mark style="background: #BBFABBA6;">rules for communication</mark>**

Now **<mark style="background: #FFF3A3A6;">Socket</mark>** in the other hand, **<mark style="background: #FFF3A3A6;">tool to use those protocols</mark>**.
	It's **OS provided programming interface**
	It's a **system-level interface** to access TCP/UDP

---
## <mark style="background: #ADCCFFA6;">How Socket works?</mark>

As we said earlier, Socket is just interface.
The OS implements it.
You never write socket implementation.

Specifically:
- **Linux**: Implements sockets in the kernel
- **Windows**: Implements sockets in the kernel (called Winsock)
- **macOS**: Implements sockets in the kernel (BSD-based)

### Is there any specification for sockets?

Most OSes follow the **POSIX socket standard** (aka **BSD sockets**)

This standard defines:
- **Function names**: `socket()`, `connect()`, `send()`, `recv()`, `close()`
- **How they behave**
- **What parameters they take**

### <mark style="background: #BBFABBA6;">Analogy with Electrical Socket (wall outlets)</mark>

#### Electrical Socket:

- Builders install the outlet (implementation)
- You plug your device into it (use the interface)
- You don't connect directly to wires in the wall
- You don't build the outlet yourself

#### Network Socket:

- OS implements the socket (implementation)
- Your code creates/uses sockets (use the interface)
- You don't access TCP/IP directly in kernel
- You don't implement the socket yourself


---
## <mark style="background: #ADCCFFA6;">Why not to use TCP directly? Why Socket needed?</mark>

**You simply cannot use TCP directly.**

> TCP is implemented in the OS kernel (or network hardware)
 
Your app source code cannot directly access kernel networking code

**<mark style="background: #ABF7F7A6;">Socket is the bridge</mark>**

```
Your Java Code (user space)
        ↕
Socket API ← This is the only way to access networking
        ↕
TCP/UDP (kernel space)
```

----
## <mark style="background: #ADCCFFA6;">Can't we use HTTP, instead of Socket?</mark>

**HTTP itself uses sockets underneath!**

**HTTP is built on top of sockets.** 
You can't escape sockets - they're the fundamental interface to networking.

---
## <mark style="background: #ADCCFFA6;">What protocols are built on top of the TCP sockets</mark>

- **HTTP protocol**
- **WebSocket protocol**
- **FTP protocol**
- **SMTP protocol**
- etc.

---
Learn more:
[[OSI model describes how network communication works]]