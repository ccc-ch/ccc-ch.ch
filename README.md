Website of CCC Swiss association.

|environment | URL|
|---|---|
|stage|[ccc.dbrgn.ch](http://ccc.dbrgn.ch/)|
|live|[ccc-ch.ch](http://ccc-ch.ch/)|


# Dependencies

The CCC-CH website is implemented with the help of Python and the [Pelican
Static Site Generator][pelican]. Content is written in [Markdown][markdown]
syntax and CSS is created using the [SASS][sass] preprocessor.


# Development Setup

## Development VM using Vagrant + Virtualbox

With [Virtualbox][virtualbox] and [Vagrant][vagrant] you can easily set up and
provision a complete development VM.

To initialize the VM:

  $ vagrant up --provider virtualbox

To SSH into the VM:

  $ vagrant ssh

To start the development server:

  $ cd /var/www/site/
  $ ./develop_server.sh start

Then open `http://10.14.10.5:8000` on your local machine. You can edit the files
directly on the local file system, the files are synced with the VM.

To stop the VM:

  $ vagrant halt

And to destroy it:

  $ vagrant destroy

## Development VM using Vagrant + Docker

If you're all hip and bleeding edge, you can also use [Docker][docker] together
with [Vagrant][vagrant]. It's actually really cool and simple to set up a dev
system:

  $ vagrant up --provider docker

Now you have a lightweight docker container running in the background serving
the ccc-ch.ch site on `http://localhost:8000`!

You cannot SSH into it, but you can 

To stop the container:

  $ vagrant halt

And to destroy it:

  $ vagrant destroy

## Manual setup

You can also set up the development environment locally. Then you need the
following tools:

* Python 2
* Virtualenv

First, create a virtualenv:

  $ virtualenv -p $(which python2) VENV
  $ . VENV/bin/activate

Then install the dependencies:

  $ pip install -U -r requirements.txt

Now start the development server:

  $ cd site
  $ ./develop_server.sh start

The web server is now running on `http://localhost:8000`.


# Markdown use

You can use the online [Markdown Editor][markdown-editor] and the
[Guidelines](#) to write articles and protocols.


# TODO

## Todo Vagrant

* in der vagrant provision muss noch  ...
 * ein start script in die VM kopiert werden für den develop_server
 * npm installiert werden
 * 'npm install' im /var/www/ccc-ch.ch order ausgeführt werden
 * ein startscript für 'grunt watch' in die VM kopiert werden

## Todo CCC-CH Site

* neues logo
* farbschema gemeinsam auswählen
* im moment ist das grid wie flolg aufgeteilt 
 * |1 spalte|9 spalten|2 spalten|
 * der letzte 2 spalten block ist für das pelican include "extras" vorgesehen
 * wird das überhaupt verwendet werden? wenn nicht kommt die spalte weg, sähe besser aus


[pelican]: http://blog.getpelican.com/
[virtualbox]: https://www.virtualbox.org/
[vagrant]: http://www.vagrantup.com/
[docker]: https://www.docker.com/
[sass]: http://sass-lang.com/
[markdown]: https://daringfireball.net/projects/markdown/syntax
[markdown-editor]: http://jbt.github.io/markdown-editor/
