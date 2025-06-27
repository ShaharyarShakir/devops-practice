# Linux Commands

## How to add users and groups

id => show id of users

sudo adduser in debian

sudo useradd in other distros

sudo groupadd

su <username> to change user

cat /etc/passwd to check users

cat /etc/group to check groups

sudo gpasswd -a <username> <groupname>

sudo gpasswd -M <username>,<username> to add mutiple users

usermod -aG groupname username

sudo usermod -aG docker $USER

sudo userdel username

sudo chown <username> <nameofthefile>

sudo chgrp <groupname> <nameofthefile>

## zipping files

zip

tar -cvzf <name.tar.gz> <name of file> =>

c => compress

v => verbose

z => zip

f => files

## unzipping

unzip

tar -xcvf

x => extract

## copying file from server to local

scp -i "private key.pem" <name of the file> <server location>:/home/username/

rsync => to sync common folder btw local and server

rsync <source file path> <destination folder using ssh to client>

# SSH using password

you can add different clients in the host using

```
vim /etc/hosts
```

#### add new users

use useradd command to add <new user>
use passwd to give new user the password

then add the user to

```
visudo
```

then add the user with the root

```
<user name> ALL=(ALL) NOPASSWD: ALL
```

then on the main user shh into the client

```
ssh <user name>@<hostname>
```

# SSH using using ssh-keygen

generate the key using the command

```
ssh-keygen
```

it will give you a public and a private key

copy the key into the client using

```
ssh-copy-id <user name>@<hostname>
```

then you can directly run the command without any password

# Sending file btw different clients

we can use scp to send file to different client connected to us by:

```
scp -i <file/dir name> <client user name>@<hostname>:/<destination folder>

```

# Resyncing the shared folder

we can resync different folders by using rsync

```
Local:  rsync [OPTION...] SRC... [DEST]
```

or

```
rsync -e "ssh -i / src" -avz /path/to/file "path to dest":/save/path
```

# AWK - Programming language

works on structures file to find patterns

awk is used to print data from a formatted file

```
awk '{print <line number $1,$2>}' <name of the file>
```

to print specific number of lines

```
awk 'NR >= 1 && NR <= 10 {print NR, $1,$2,$3}' app.log
```

to print a range of a occurrence

```
 awk '$2 >= '08:51:01' && $2 <= '08:59:00' {print $2}' app.log
```

to print the count of occurrence

```
awk '/INFO/ {count++} END {print count}' app.log
```

# SED - streamline editor

work on any file to find patterns

search line by line

print pattern using sed

```
sed -n '/INFO/p' <name of file>
```

n => number

p => pattern

can also be used to replace to the value

```
sed 's/<name>/<name to replace>/g' <name of file>
```

s => string

g => global

to print number of line of a word

```
sed -n -e '/INFO/='  app.log

```

with the word itself

```
sed -n -e '/INFO/=' -e '/INFO/p'  app.log
```

-e => edit

= => number of line

to replace a a value from a range

```
sed '1,15  s/INFO/LOG/g; 1,10p; 11q' app.log
```

# GREP - global regular expression pattern

for case sensitive

```
grep <pattern name> <file name>
```

for case insensitive

```
grep -i <pattern name> <file name>
```

-c => for count

# DISk partition using - fdisk

to list the disk

```
fdisk -l
```

to create the partition

```
fdisk  /dev/<name of the disk>
```

then you will be prompted

# Formatting the disk using mkfs

show the types of formate available

```
mkfs
```

you can select one type

```
mkfs.btrfs /dev/<name>
```

# Mounting the volume

how to mount

```
mount /path/to/volume /path/to/dir
```

#### permanent mount

open the file

```
vim /etc/fstab
```

in fstab

add partition path as first column

volume path dir path format type options dump code && fscd code

```
/dev/name     /var/www/html/images    ext4        defaults                  0 0
```

0 0 => no dumping, no file extension

then

```
mount -a
```

to mount the files

# Unmountig the dir

how to unmount

```
umount /path/to/dir
```

# How to change shell

to change run command

```
chsh - /path/to/shell
```

shells are available in

```
cat /etc/shells
```

- sudo !! - re-run previous command with 'sudo' prepended
- ctrl-k, ctrl-u, ctrl-w, ctrl-y - cutting and pasting text in the command line
- practical kill/yank example
- use 'less +F' to view logfiles, instead of 'tail' (ctrl-c, shift-f, q to quit)
- ctrl-x-e - continue editing your current shell line in a text editor (uses $EDITOR)
- alt-. - paste previous command's argument (useful for running multiple commands on the same resource)
- reset - resets/unborks your terminal

# if images doesn't show up

- go to

```
vim /etc/selinux/config
```

- the disabled the enforcing path
- use this command to check which process taking if umount not works

```
lsof /path/to/dir
```
# add user to a group
- usermod -aG <groupname> <username>
