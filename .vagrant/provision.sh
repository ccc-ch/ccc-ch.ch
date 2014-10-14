#!/bin/bash

echo starting provision ...

echo install python-pip

apt-get install python-pip -y > /dev/null

echo install project requirements

cd /var/www
pip install -r requirements.txt > /dev/null

#echo install apache2

#apt-get install apache2 > /dev/null

#cp .vagrant/configs/localhost /etc/apache2/sites-available/

#a2ensite localhost
#service apache2 reload

#cd site/; ./develop_server.sh start 8080