# How to install qemu with vert-manager


### Check how many virtual threads are available

```
egrep -c '(vmx|svm)' /proc/cpuinfo
```


### Install Dependencies 

```
sudo pacman -S qemu virt-manager virt-viewer dnsmasq vde2 bridge-utils openbsd-netcat ebtables iptables libguestfs
```
### enable libvertd

```
sudo systemctl enable --now libvirtd
```

### add libverth to root user
```
sudo usermod -aG libvirt $USER
```
### restart the manager

```
sudo systemctl restart libvirtd
```

