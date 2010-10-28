import flask
import simplejson

from mq import app
from models import Message


@app.route('/messages')
def messages():
    messages = list(Message.all().filter('seen', False))
    for m in messages:
        m.seen = True
        m.save()
    return flask.Response('\n\n'.join([m.content for m in messages]),
        mimetype='text/plain')


@app.route('/messages/create', methods=('GET', 'POST', ))
def message_create():
    if flask.request.method == 'POST':
        Message(content=flask.request.form['content']).put()
        return flask.jsonify(created=1)

    return flask.render_template('message_create.html')
