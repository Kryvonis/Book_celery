from flask import Flask, Blueprint
import logging as loger
from celery import Celery

app = Flask(__name__)
celery_app = Celery(app)

from app.views import view

loger.basicConfig(filename='main.log', level=loger.DEBUG)

app.config.from_object('config')

app.register_blueprint(view.mod)
