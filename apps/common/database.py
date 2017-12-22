# -*- coding: utf-8 -*-
from redis import Redis
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from config import Config

# db
engine = create_engine(Config.databaseUrls())
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import apps.models.tests
    Base.metadata.create_all(bind=engine)


# redis
redis_session = Redis(host=Config.REDIS_HOST, password=Config.REDIS_PASSWD)
