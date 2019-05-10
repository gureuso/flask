# -*- coding: utf-8 -*-
import redis
from pymongo import MongoClient
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


from config import Config


engine = create_engine(Config.database_url())
db_session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

mongo_client = MongoClient(Config.database_url('mongodb'))
mongo_session = mongo_client[Config.DB_NAME]

redis_session = redis.Redis(host=Config.REDIS_HOST, password=Config.REDIS_PASSWD)
