---
created: 2025-12-12
tags:
  - networking
  - networking/osi-model
  - networking/protocols
sr-due: 2026-01-06
sr-interval: 1
sr-ease: 230
---
### OSI model has 7 layers to explain communication

#### Layer 7: <mark style="background: #FFF3A3A6;">Application</mark>

The Application Layers **provides protocols to the end-clients**.
End-clients use those protocols, to **communicate with the application**.

> Applications themselves aren't part of the layer.
> It's all about using protocols, to use application.

Example of those protocols are: HTTP/HTTPS, SMTP, FTP, DNS etc.

---
#### Layer 6: <mark style="background: #FFF3A3A6;">Presentation</mark>

The Presentation Layer is busy with **presenting data** to:
- :luc_upload: <mark style="background: #ABF7F7A6;">Application Layer</mark>: gets clean and **readable data**
- :luc_download: <mark style="background: #ABF7F7A6;">Session Layer</mark>: gets encoded/compressed **raw data**.

##### Main functions:

1. <mark style="background: #FFF3A3A6;">Translation (Encoding)</mark>:
	converts data between **different formats** (text :luc_arrow_left_right: binary) 
	**character encoding** conversions (ASCII :luc_arrow_left_right: EBCDIC)

2. <mark style="background: #FFF3A3A6;">Encryption / Decryption</mark>:
	secures data (**SSL/TSL** happens here conceptually)

3. <mark style="background: #FFF3A3A6;">Compression / Decompression</mark>:
	done for efficient transmission

4. <mark style="background: #FFF3A3A6;">Data formatting</mark>:
	structures data (JSON, XML, images as JPG/PNG)

> <mark style="background: #FF5582A6;">Note</mark>: :luc_pencil: 
> In modern TCP, this layer often merged with Application Layer.

---
#### Layer 5: <mark style="background: #FFF3A3A6;">Session</mark>

Session Layers **manages *the sessions***.

**Session** - is an ongoing connection between two applications (any program/process that uses the network).
It can persist across multiple connection.

> <mark style="background: #FF5582A6;">Note</mark>: :luc_pencil: 
> **One connection** is **NOT** the same as **one request-response**
> One session can have multiple request-response and TCP connections.

##### Main functions:

1. <mark style="background: #ABF7F7A6;">Session Establishment</mark>
	- **Who** gonna **talk first**
	- What **protocol** are we gonna use
	- **Authentication**
	- Sets up 'pathway'
	- Applications agree: "We're in a session now"
	- **Assigns session ID**, **maintains state**

2. <mark style="background: #ABF7F7A6;">Synchronization & Checkpointing</mark>
	- Long data transfers may fail midway
		- without checkpoints :luc_arrow_big_right: restart from the scratch
	- It uses `Sync points` :luc_arrow_big_right: **markers in the data stream**
	- Session gonna track those points
		- In case of fail, will say "we only received up to there"
		- Then last data from last checkpoint will be **resumed**

3. <mark style="background: #ABF7F7A6;">Dialog Control</mark>
	- **Who can transmit when**
	- <mark style="background: #FFF3A3A6;">Modes</mark> :
		- **<mark style="background: #BBFABBA6;">Simplex</mark>**
			- **One direction only** (rare)
			- Example: keyboard :luc_arrow_right: computer
		- **<mark style="background: #BBFABBA6;">Half-Duplex</mark>**
			- **Both directions**, but **NOT simultaneously**
			- Example: **Walkie-talkie** :luc_radio: - press button to talk, release to listen
			- Session enforces 'turns'
		- **<mark style="background: #BBFABBA6;">Full-Duplex</mark>**
			- **Both directions simultaneously**
			- Example: Phone call - both talk and listen at once
			- Session layer allows concurrent flow

	<mark style="background: #FF5582A6;">Note</mark>: :luc_pencil: 
	HTTP Request-Response can be half-duplex and full-duplex, depends on perspective
	- **Transport layer (TCP) itself `full-duplex`**
		- cause it allows simultaneous send/receive
	- but, **Application layer** behavior of 
		- `HTTP/1.1` :luc_arrow_right: is more like **`half-duplex`**
		- `HTTP/2` :luc_arrow_right: `full-duplex`

> <mark style="background: #FF5582A6;">Note</mark>: :luc_pencil: 
> 
> Session Layer does NOT modify the data itself.
> 
> It only:
> - manages connection
> - organizes the data flow
> - add sync points
> - controls dialogue
>
> Session Layer passes already compressed, encrypted, formatted data 
> to Transport Layer, without any changes. 

---
#### Layer 4: <mark style="background: #FFF3A3A6;">Transport</mark>

Transport Layer prepares data for transfer
- Breaks data into segments
- Adds port numbers and sequence numbers
- Handles end-to-end delivery logistics.

> Does NOT transfer data between devices.
> 
> Data stays on the same host.
> Not actual network transmission yet

**Key protocols**: TCP, UDP

##### Main functions:

1. <mark style="background: #ABF7F7A6;">End-to-End Connection</mark>

	- Communication directly between applications (not just devices)
		- because one device may have many apps
		- transport layer provides end-to-end connection, literally by using app's port
	- Uses port numbers to identify specific apps
	- Example:
		- **Your laptop** (device: IP = 192.168.1.5)
			- Chrome browser (app: port 50234)
			- Zoom (app: port 50236)
		- **Server** (device: IP = 93.184.216.34)
			- Web server (app: port 443)
			- Email server (app: port 25)
	- <mark style="background: #ADCCFFA6;">Transport Layer itself only deals with ports. </mark>
	- <mark style="background: #ABF7F7A6;">The IP addresses get added later when the segment moves down to the Network Layer (Layer 3)</mark>

###### Session vs End-to-End connection

| Session Layer                | Transport Layer             |
| ---------------------------- | --------------------------- |
| Logical dialogue/session     | Physical connection pathway |
| Manages "conversation state" | Ensures actual delivery     |
| Synchronization & recovery   | Reliability & ordering      |
| Can survive connection drops | IS the connection           |

2. <mark style="background: #ABF7F7A6;">Segmentation & Reassembly</mark>
	Read more: [[Segment is a chunk of data in Transport Layer]]

3. <mark style="background: #ABF7F7A6;">Flow Control & Buffer Overflow Prevention</mark>

	- Buffer :luc_arrow_big_right: temporary memory storage for incoming data
	- Overflow :luc_arrow_big_right: data arrives faster that receiver can process
	- Result = buffer fills up :luc_arrow_right_circle: data gets dropped :luc_arrow_right_circle: loss

	**How to prevent that ?**
	
	by **Window Size** mechanism (inside TCP)
	- Receiver tells sender, how much data he can handle
	- Sender adjust speed accordingly

---
#### Layer 3: <mark style="background: #FFF3A3A6;">Network</mark>

Network Layer handles routing and forwarding of data packets between different networks
	If devices talking in the same network, no need for this layer

The actual data transmission happens in this layer
	Packets physically leave your device and travel to the destination

**Key protocols**: IP, ICMP, IGMP, IPsec

See also: [[Packet is Segment with IP address]]

##### Main functions:

1. <mark style="background: #ABF7F7A6;">Logical Addressing</mark>

	- Network Layer assigns and uses **IP addresses** to identify **source** and **destiny**
		- Every packet gets tagged with sender and receiver IP address
		- Your ISP gives one public IP to your router
			- Your router translates private IPs of devices to that one public IP

2. <mark style="background: #ABF7F7A6;">Routing</mark>
	- Network Layer determines the best path to transfer data between routers
	- Routers analyze network topology and select optimal routes.

---
#### Layer 2: <mark style="background: #FFF3A3A6;">Data Link</mark>

- Data Link Layer receives Packets from Network Layer.
- <mark style="background: #ABF7F7A6;">Wraps those Packets with MAC <b>Header</b> and <b>Trailer</b></mark>
	- Now that wrapped data is called **Frame**

Additional MAC address is added
	By that you can send packets to the correct device on the same LAN.

For that we use physical device called Switch.
	Learn more about Switch: 
	[[Switch physical device that connects multiple devices on a single LAN]]

**Data Link Layer is similar to Network Layer** 
- In Network Layer you transport packets across the networks
- Whereas in Data Link Layer you transport frames to devices in the same network

Read more:
[[MAC address burned into network card]]
[[Frame is a Packet with MAC header and trailer]]
[[Frame Check Sequence (FCS) inside trailer detects corruped data]]

---
#### Layer 1: <mark style="background: #FFF3A3A6;">Physical</mark>

- Receives raw data, from the payload of the frame
- Converts those digital bits (0s and 1s) into physical signals

Read more: [[Raw bits encoding for different types of signals]]

---

![[OSI model 7 layers.png]]