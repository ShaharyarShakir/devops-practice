# 📘 Ansible CLI & Ad-Hoc Commands
### 🔧 What is an Ad-Hoc Command?
- Ansible ad-hoc commands allow you to perform simple, quick tasks without writing a playbook, such as installing a package, restarting a service, or copying a file.

### 🧪 Inventory Sample (inventory.ini)
```
[web]
192.168.56.101
192.168.56.102
```
```
[db]
192.168.56.103
```
- Use this with -i inventory.ini in all commands below.

### ✅ Common Ad-Hoc Commands
- 1. 🔍 Ping All Hosts
```
ansible all -m ping -i inventory.ini
```
- 2. 💾 Gather Facts
``` 
ansible all -m setup -i inventory.ini
```
- 3. 📦 Install a Package
```
ansible all -m package -a "name=nginx state=present" -b -i inventory.ini
```
- 4. ❌ Remove a Package
```
ansible all -m package -a "name=nginx state=absent" -b -i inventory.ini
```
- 5. 🧑 Add a User
```
ansible all -m user -a "name=devuser shell=/bin/bash" -b -i inventory.ini
```
- 6. 👥 Add a Group
```
ansible all -m group -a "name=developers state=present" -b -i inventory.ini
```
- 7. ➕ Add User to Group
```
ansible all -m user -a "name=devuser groups=developers append=yes" -b -i inventory.ini
```
- 8. 🔥 Open Firewall Port (RedHat)
```
ansible all -m firewalld -a "port=80/tcp permanent=yes state=enabled" -b -i inventory.ini
```
- 9. 📁 Copy a File
```
ansible all -m copy -a "src=./index.html dest=/var/www/html/index.html" -b -i inventory.ini
```
- 10. 📄 Create an Empty File
ansible all -m file -a "path=/tmp/sample.log state=touch mode=0644" -b -i inventory.ini
- 11. 🖥️ Run a Shell Script
```
ansible all -m script -a "./scripts/setup.sh" -b -i inventory.ini
```
- 12. ❌ Kill a Process
```
ansible all -m shell -a "pkill nginx" -b -i inventory.ini
```
### ⚙️ Useful Ansible CLI Options
- Option	Description
- -m	Specify the module to use (e.g. ping, copy, shell)
- -a	Pass arguments to the module
- -i	Specify inventory file
- -b	Run as sudo (become)
- --check	Run in dry-run mode (no changes made)
- --diff	Show file changes when copying/editing files

### 🧠 Tips
- Always use -b if root access is required.

- Use --limit to run commands on a subset of hosts:

```
ansible web -m ping -i inventory.ini --limit 192.168.56.101
```
- Use ansible-doc <module> to explore module options:
```
ansible-doc copy
```
