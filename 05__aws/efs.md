# EFS

- Elastic File System
- can mount for multiples instances

### Uses

- containers
- servers
- machine learning

## how to mount

- create a security group using nfs as type
- add the web server security group as a value
- create EFS instance
- install amazon-efs-utils on ec2
- file-system-id:/ efs-mount-point efs \_netdev,noresvport,tls,accesspoint=access-point-id 0 0
- edit this according to creditentionals
- add this in /etc/fstab
- test it using mount -a
- add it using mount -fav
- before adding firts backup the folder
- add the files test it

