# Basics

### Check Firewall Status

```bash
sudo ufw status
```

```bash
sudo ufw status verbose
```

### Allow Traffic

- Allow SSH (VERY important)

```bash
sudo ufw allow ssh
# same as: sudo ufw allow 22
```

### Allow a port

```bash
sudo ufw allow 80 # HTTP
```

```bash
sudo ufw allow 443 # HTTPS
```

```bash
sudo ufw allow 8080
```

### Allow a port with protocol

```basbh
sudo ufw allow 53/udp
```

```bash
sudo ufw allow 21/tcp
```

### Allow a port from a specific IP

```bash
sudo ufw allow from 192.168.1.10 to any port 22
```

### Deny or Reject Traffic

```bash
sudo ufw deny 23 # deny telnet
```

```bash
sudo ufw reject 25 # actively reject instead of silently drop
```

### Delete Rules

```bash
sudo ufw delete allow 80
```

```bash
sudo ufw delete deny 23
```

### Delete by numbered rule:

```bash
sudo ufw status numbered
```

```bash
sudo ufw delete <rule-number>
```

### Disable / Reset UFW

```bash
sudo ufw disable
```

```bash
sudo ufw reset
```

### Set Default Policies

#### Recommended defaults:

```bash
sudo ufw default deny incoming
```

```bash
sudo ufw default allow outgoing
```
