# -*- coding: utf-8 -*-
from redis import Redis
from flask_sqlalchemy import SQLAlchemy

from config import Config

# db
db = SQLAlchemy()


# redis
redis_session = Redis(host=Config.REDIS_HOST, password=Config.REDIS_PASSWD)
