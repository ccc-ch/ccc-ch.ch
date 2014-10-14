Website of CCC Swiss association based on [Pelican Static Site Generator](http://blog.getpelican.com/)

# Depencies

[vagrant](http://www.vagrantup.com/) is requierd to initialize the development VM

# Installation

1. ``git clone https://github.com/peponi/ccc-ch.ch.git``
2. ``cd ccc-ch.ch``
3. ``vagrant up``
4. ``vagrant ssh``
5. ``cd /var/www/site/; ./develop_server.sh start``
6. open http://10.14.10.5:8000