# -*- coding: utf-8 -*-
import redis
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import Config


def database_urls():
    return 'mysql://{0}:{1}@{2}/{3}'.format(Config.MYSQL_USER_NAME,
                                            Config.MYSQL_USER_PASSWD,
                                            Config.MYSQL_HOST,
                                            Config.MYSQL_DB_NAME)


engine = create_engine(database_urls())
db_session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

redis_session = redis.Redis(host=Config.REDIS_HOST, password=Config.REDIS_PASSWD)
