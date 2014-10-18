Website of CCC Swiss association based on [Pelican Static Site Generator](http://blog.getpelican.com/)

|environment | URL|
|---|---|
|stage|[ccc-ch.ch](http://ccc-ch.ch/)|
|live|[ccc.dbrgn.ch](http://ccc.dbrgn.ch/)|

# Depencies

* [Virtualbox](https://www.virtualbox.org/) is required to run with Vagrant
* [Vagrant](http://www.vagrantup.com/) is requierd to initialize the development VM

# Installation

1. ``git clone https://github.com/peponi/ccc-ch.ch.git``
2. ``cd ccc-ch.ch``
3. ``vagrant up``
4. ``vagrant ssh``
5. ``cd /var/www/site/; ./develop_server.sh start``
6. open http://10.14.10.5:8000

# Todo Vagrant

* in der vagrant provision muss noch  ...
 * ein start script in die VM kopiert werden für den develop_server
 * npm installiert werden
 * 'npm install' im /var/www/ccc-ch.ch order ausgeführt werden
 * ein startscript für 'grunt watch' in die VM kopiert werden

# Todo CCC-CH Site