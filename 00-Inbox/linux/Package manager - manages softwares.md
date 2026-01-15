
Downloads, installs or updates software from repo
Ensures the integrity and authenticity of the package
Manages and resolved all required dependencies
Knows where to put all files in Linux file system
Easy upgrading of the software

---

Each Linux distro has its own Package Manager.

<mark style="background: #BBFABBA6;">Debain family</mark> (Ubuntu, Mint etc.) uses :luc_arrow_right_circle: `APT` (Advanced Package Tool) or `APT-GET`

<mark style="background: #BBFABBA6;">Red had family</mark> (RHEL, CentOS, Fedora) uses :luc_arrow_right_circle: `YUM` 

---

**Search software:**

```bash
apt search <package_name>

sudo apt search openjdk
```

---

**Install package:**

```bash
sudo apt install openjdk-17-jre-headless
```

---

**Remove package:**

```bash
sudo apt remove openjdk-17-jre-headless
```

---
