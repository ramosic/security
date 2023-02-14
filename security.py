#!/usr/bin/env python3
# Author: Christer Karlsen
# Email: chris@ramosicked.com
# Project: security
# Copyright (c) 2023, Christer Karlsen
# License: MIT License
#
import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode('utf-8')

# Update the package manager
run_command("sudo apt-get update")

# Upgrade the system packages
run_command("sudo apt-get upgrade -y")

# Install the firewall (UFW)
run_command("sudo apt-get install ufw -y")

# Enable the firewall
run_command("sudo ufw enable")

# Allow SSH traffic
run_command("sudo ufw allow ssh")

# Deny all incoming traffic by default
run_command("sudo ufw default deny incoming")

# Allow all outgoing traffic
run_command("sudo ufw default allow outgoing")

# Check the firewall status
firewall_status = run_command("sudo ufw status")
print("Firewall status:", firewall_status)

# Update the SSH configuration
sshd_config = """
# SSH security configuration

# Disable root login
PermitRootLogin no

# Disable password authentication
PasswordAuthentication no

# Use only key-based authentication
PubkeyAuthentication yes

# Specify the SSH port
Port 22
"""
with open("/etc/ssh/sshd_config", "w") as file:
    file.write(sshd_config)

# Restart the SSH service
run_command("sudo systemctl restart ssh")

