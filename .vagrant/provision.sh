#!/bin/bash
echo Starting provisioning...

echo Installing python-pip
apt-get install python-pip -y > /dev/null

echo Installing project requirements
cd /var/www
pip install -q -U -r requirements.txt
