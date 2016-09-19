from flask import Flask, Blueprint
from celery import Celery
import logging as loger
from app.views import view

loger.basicConfig(filename='main.log', level=loger.DEBUG)

app = Flask(__name__)

celery_app = Celery(app)

app.config.from_object('config')

app.register_blueprint(view.mod)
