# -*- coding: utf-8 -*-
import os


# app config
class Config(object):
    APP_MODE_PRODUCTION = 'production'
    APP_MODE_DEVELOPMENT = 'development'
    APP_MODE_TESTING = 'testing'

    ROOT_DIR = os.getcwd()
    STATIC_DIR = '{0}/static'.format(ROOT_DIR)
    TEMPLATES_DIR = '{0}/templates'.format(ROOT_DIR)
    ERROR_CODE = {
        40300: 'Forbidden',
        40400: 'Not Found',
        41000: 'Gone',
        50000: 'Internal Server Error',
    }

    APP_MODE = os.getenv('APP_MODE', APP_MODE_DEVELOPMENT)
    APP_HOST = os.getenv('APP_HOST', 'localhost')
    APP_PORT = int(os.getenv('APP_PORT', 5000))
    MYSQL_USER_NAME = os.getenv('MYSQL_USER_NAME', 'root')
    MYSQL_USER_PASSWD = os.getenv('MYSQL_USER_PASSWD', 'asdf1234')
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_DB_NAME = os.getenv('MYSQL_DB_NAME', 'flask')
    REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
    REDIS_PASSWD = os.getenv('REDIS_PASSWD')

    @staticmethod
    def databaseUrls():
        return 'mysql://{0}:{1}@{2}/{3}'.format(Config.MYSQL_USER_NAME,
                                                Config.MYSQL_USER_PASSWD,
                                                Config.MYSQL_HOST,
                                                Config.MYSQL_DB_NAME)

    @staticmethod
    def fromAppMode():
        mode = {
            Config.APP_MODE_PRODUCTION: 'config.ProductionConfig',
            Config.APP_MODE_DEVELOPMENT: 'config.DevelopmentConfig',
            Config.APP_MODE_TESTING: 'config.TestingConfig',
        }
        return mode.get(Config.APP_MODE, mode[Config.APP_MODE_DEVELOPMENT])


# flask config
class FlaskConfig(object):
    SECRET_KEY = os.urandom(24).encode('hex')
    SQLALCHEMY_DATABASE_URI = Config.databaseUrls()
    # https://stackoverflow.com/questions/33738467/how-do-i-know-if-i-can-disable-sqlalchemy-track-modifications
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    TESTING = False


class ProductionConfig(FlaskConfig):
    DEBUG = False


class DevelopmentConfig(FlaskConfig):
    SQLALCHEMY_ECHO = True
    DEBUG = True
    TESTING = True


class TestingConfig(FlaskConfig):
    TESTING = True
