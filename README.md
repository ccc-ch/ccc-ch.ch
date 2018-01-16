# ccc-ch.ch

Website of CCC Swiss association.


## Dependencies

The CCC-CH website is implemented with the help of Python and the [Pelican
Static Site Generator][pelican]. Content is written in [Markdown][markdown].


## Development setup

### Manual setup

You can set up the development environment locally. Then you need the following
tools:

* Python 2 or 3
* Virtualenv

First, create a virtualenv:

    $ virtualenv VENV
    $ . VENV/bin/activate

Then install the dependencies:

    $ pip install -U -r requirements.txt

Now start the development server:

    $ ./develop_server.sh start

The web server is now running on `http://localhost:8000`.


## Markdown use

You can use the online [Markdown Editor][markdown-editor] to write articles and
protocols.


## Deployment

If you have a user account on the ccc-ch.ch Server, first make sure that the
correct umask is set in your `~/.profile` file:

    umask 022

Then you can deploy the website via rsync:

    $ LANG=de_CH.UTF8 make rsync_upload


[pelican]: http://blog.getpelican.com/
[markdown]: https://daringfireball.net/projects/markdown/syntax
[markdown-editor]: http://jbt.github.io/markdown-editor/
