# Readme.txt
# This file contains various entitities that explains how the Compute instances were setup
# How the RDP was installed
# How the connection was created with git from remote
# First how to ensure that the Ubuntu that you are running is also able to do the RDP
1  clear
2  sudo apt-get update
3  sudo DEBIAN_FRONTEND=noninteractive apt-get -y install xfce4
4  sudo apt install xfce4-session
5  sudo apt-get -y install xrdp
6  sudo systemctl enable xrdp
7  echo xfce4-session >~/.xsession
8  sudo service xrdp restart
9  sudo passwd azureuser


# Next copy this file to the newly created folder. 
