
APT stores only verified packages
It may not store some apps that you need
For example browsers, IDE, messengers etc.

You have some other alternatives:
1. Ubuntu Software Center (uses `snap` under the hood)
2. Snap Package Manager
	- also called 'snappy'
	- it's software packaging and deployment system
3. Add repo to official list of repos
	- `add-apt-repository`
	- repo will be added to `/etc/apt/soruces.list`

---

### Differences between Snap and APT

Snap:
- Self-contained: all needed dependencies contained in the package
	- larger installation size
- More like universal for different distros
- auto updates

APT:
- dependencies are split and they're shared.
	- smaller installation size
- Only for `.deb` Linux distros
- manual update

---

### PPA - Personal Package Archive

PPAs are provided by the community
Used for private repos also

> NO guarantee of quality or security