#!/usr/bin/env python3
# Author: Christer Karlsen
# Email: chris@ramosicked.com
# Project: security
# Copyright (c) 2023, Christer Karlsen
# License: MIT License
#
#!/usr/bin/env python3

import os
from tqdm import tqdm

# update and upgrade the system
os.system('sudo apt update')
os.system('sudo apt upgrade')

# lock down SSH
os.system('sudo sed -i "s/#PermitRootLogin prohibit-password/PermitRootLogin no/g" /etc/ssh/sshd_config')
os.system('sudo sed -i "s/PasswordAuthentication yes/PasswordAuthentication no/g" /etc/ssh/sshd_config')
os.system('sudo systemctl restart sshd')

# enable firewall and allow SSH
os.system('sudo ufw enable')
os.system('sudo ufw default deny incoming')
os.system('sudo ufw default allow outgoing')
os.system('sudo ufw allow ssh')

# install fail2ban and enable it
os.system('sudo apt install fail2ban')
os.system('sudo systemctl enable fail2ban')

# other suggested tasks
# install and configure an antivirus program like ClamAV
os.system('sudo apt install clamav')
os.system('sudo freshclam')

# install and configure a web application firewall like ModSecurity
os.system('sudo apt install libapache2-mod-security2')
os.system('sudo mv /etc/modsecurity/modsecurity.conf-recommended /etc/modsecurity/modsecurity.conf')
os.system('sudo systemctl restart apache2')

# disable unnecessary services and daemons
os.system('sudo systemctl stop bluetooth')
os.system('sudo systemctl disable bluetooth')
os.system('sudo systemctl stop cups')
os.system('sudo systemctl disable cups')

# install and configure a backup solution
os.system('sudo apt install rsync')
os.system('sudo mkdir /backup')
os.system('sudo chown -R $USER:$USER /backup')
os.system('sudo chmod -R 700 /backup')

# add progress bar
tasks = ['update and upgrade the system', 'lock down SSH', 'enable firewall and allow SSH', 'install fail2ban and enable it', 'install and configure an antivirus program like ClamAV', 'install and configure a web application firewall like ModSecurity', 'disable unnecessary services and daemons', 'install and configure a backup solution']
for task in tqdm(tasks):
    print(task)


