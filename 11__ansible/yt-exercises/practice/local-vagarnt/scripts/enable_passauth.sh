#!/bin/bash
set -e

echo "[INFO] Enabling SSH PasswordAuthentication..."
sudo sed -i 's/^#\?PasswordAuthentication .*/PasswordAuthentication yes/' /etc/ssh/sshd_config
sudo sed -i 's/^#\?PermitRootLogin .*/PermitRootLogin yes/' /etc/ssh/sshd_config

# Restart SSH service
sudo systemctl restart sshd || sudo systemctl restart ssh

# Set password for vagrant user (in case you want to test with password)
echo "vagrant:vagrant" | sudo chpasswd

echo "[DONE] SSH PasswordAuthentication enabled."

