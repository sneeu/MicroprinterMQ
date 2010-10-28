from google.appengine.ext import db


class Message(db.Model):
    content = db.TextProperty(required=True)
    seen = db.BooleanProperty(default=False)
    when = db.DateTimeProperty(auto_now_add=True)
