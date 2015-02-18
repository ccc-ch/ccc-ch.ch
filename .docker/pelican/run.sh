#!/bin/bash

cd /var/www/site

MYUID=`stat -c "%u" .`
id $MYUID > /dev/null 2> /dev/null || useradd -u $MYUID -d /var/www temporary
MYUSER=`getent passwd "$MYUID" | cut -d: -f1`

sudo -u $MYUSER ./develop_server.sh start $@
while true; do
       sleep 1000
done
