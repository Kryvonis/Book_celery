from flask import Flask, Blueprint
from app.views import view
from celery import Celery

app = Flask(__name__)

celery_app = Celery(app)

app.config.from_object('config')

app.register_blueprint(view.mod)
