#!/bin/bash

echo starting provision ...

echo install python-pip

sudo apt-get install python-pip -y > /dev/null

echo install project requirements

cd /var/www
sudo pip install -r requirements.txt > /dev/null

echo install apache2

sudo apt-get install apache2 > /dev/null

sudo cp .vagrant/configs/localhost /etc/apache2/sites-available/

#a2ensite localhost
sudo service apache2 reload

cd /var/www/site/

sudo ./develop_server.sh start 