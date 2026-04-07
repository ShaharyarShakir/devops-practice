# Download the static binary (check releases page for latest version)
```bash
curl -L https://github.com/containers/podman/releases/download/v5.7.1/podman-remote-static-linux_amd64.tar.gz -o /tmp/podman.tar.gz
```
# Extract and install
```bash
tar -xzf /tmp/podman.tar.gz -C /tmp
sudo mv /tmp/bin/podman-remote-static-linux_amd64 /usr/local/bin/podman
sudo chmod +x /usr/local/bin/podman
```
# Clean up
```bash
rm /tmp/podman.tar.gz
```

# Setting Up the Connection

```bash
podman system connection add --default podman-machine-default-root \
  unix:///mnt/wsl/podman-sockets/podman-machine-default/podman-root.sock
```
# Fixing Permissions
```bash
sudo usermod --append --groups 10 $(whoami)
```
# Verify everything works:
```bash
podman version
podman ps
```
