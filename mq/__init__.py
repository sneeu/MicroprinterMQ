from flask import Flask
import settings


app = Flask('mq')
app.config.from_object('mq.settings')


import views
