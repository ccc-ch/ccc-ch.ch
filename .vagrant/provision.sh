#!/bin/bash
echo Starting provisioning...

echo Installing system packages
apt-get install python-pip ruby nodejs npm -y > /dev/null

echo Installing project requirements
cd /var/www
pip install -q -U -r requirements.txt
#cd /var/www/site
#npm install
