
In many companies and unis you can login to any PC with your creds.

---
#### How it works

Admins set up `Active Directory (AD)`
<mark style="background: #BBFABBA6;">AD is a central server</mark> that stores all user accounts.

Each PC joins the domain
Checks creds against AD when you login

That's why your username works on any domain-joined PC

---
#### Where files are stored

1. <mark style="background: #BBFABBA6;">Roaming profiles</mark>
	
	Files (from `home` folder) are copied from server to local PC at login
	You work on local copies during your session	
	At logout, changes are copied back to server
	
2. <mark style="background: #BBFABBA6;">Redirected folders</mark>
	
	Files stay on server permanently
	PC access them directly over network in real-time
	No copying - you're reading/writing to server constantly
	
3. <mark style="background: #BBFABBA6;">Local profiles</mark>
	
	Files stay on local PC only
	You get fresh empty profiles on each different PC 