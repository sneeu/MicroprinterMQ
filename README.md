MicroprinterMQ
==============

A [Google App Engine][gae] application for storing messages to be pulled by my [Arduino Microprinter][microprinter].

I wouldn't use this without adding some sort of password protection, to avoid your microprinter being spammed.

This project requires [Flask][flask] in the project directory:

    wget -q -O - http://github.com/mitsuhiko/flask/tarball/0.6 | tar xz
    mv mitsuhiko-flask-5cadd9d/flask .

    wget -q -O - http://pypi.python.org/packages/source/W/Werkzeug/Werkzeug-0.6.2.tar.gz | tar xz
    mv Werkzeug-0.6.2/werkzeug .

    wget -q -O - http://pypi.python.org/packages/source/J/Jinja2/Jinja2-2.5.tar.gz | tar xz
    mv Jinja2-2.5/jinja2 .

    wget -q -O - http://pypi.python.org/packages/source/s/simplejson/simplejson-2.1.1.tar.gz | tar xz
    mv simplejson-2.1.1/simplejson .

    rm -rf mitsuhiko-flask-5cadd9d Werkzeug-0.6.2 Jinja2-2.5 simplejson-2.1.1


[gae]: http://code.google.com/appengine/
[microprinter]: http://sneeu.com/projects/
[flask]: http://flask.pocoo.org/
