# -*- coding: utf-8 -*-
from redis import Redis

from config import Config
from apps.controllers.router import db

cache = Redis(host=Config.REDIS_HOST, password=Config.REDIS_PASSWD)
