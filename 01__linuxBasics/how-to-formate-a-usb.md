 # How to format a usb or broken usb

 ###  Wipe the beginning of the disk (clean old partition data)

 ```
 sudo dd if=/dev/zero of=/dev/sda bs=1M count=100
 ```

### 2. Create a New Partition Table and Partition

```
sudo fdisk /dev/sda
```

### Format the New Partition

```
sudo mkfs.vfat -F 32 /dev/sda1
```


