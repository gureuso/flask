# -*- coding: utf-8 -*-
from redis import Redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from apps.controllers import app
from config import Config

# db
db = SQLAlchemy(app)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config.fromAppMode())
    db.init_app(app)
    return app

# redis
redis_session = Redis(host=Config.REDIS_HOST, password=Config.REDIS_PASSWD)
