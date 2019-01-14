# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from redis import Redis

from config import Config

# db
engine = create_engine(Config.database_urls(), convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

# redis
redis_session = Redis(host=Config.REDIS_HOST, password=Config.REDIS_PASSWD)
