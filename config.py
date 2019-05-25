# -*- coding: utf-8 -*-
import os


# app config
class Config(object):
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    STATIC_DIR = '{0}/static'.format(ROOT_DIR)
    TEMPLATES_DIR = '{0}/templates'.format(ROOT_DIR)
    ERROR_CODE = {
        40000: 'Bad Request',
        41000: 'Gone',
        40300: 'Forbidden',
        40400: 'Not Found',
        50000: 'Internal Server Error',
    }

    APP_MODE_PRODUCTION = 'production'
    APP_MODE_DEVELOPMENT = 'development'
    APP_MODE_TESTING = 'testing'

    APP_MODE = os.getenv('APP_MODE', APP_MODE_PRODUCTION)
    APP_VENV = os.getenv('APP_VENV', 1)
    APP_HOST = os.getenv('APP_HOST', '0.0.0.0')
    APP_PORT = int(os.getenv('APP_PORT', 80))

    DB_USER_NAME = os.getenv('DB_USER_NAME') or os.getenv('RDS_USERNAME') or 'root'
    DB_USER_PASSWD = os.getenv('DB_USER_PASSWD') or os.getenv('RDS_PASSWORD') or 'asdf1234'
    DB_HOST = os.getenv('DB_HOST') or os.getenv('RDS_HOSTNAME') or 'localhost'
    DB_NAME = os.getenv('DB_NAME') or os.getenv('RDS_DB_NAME') or 'flask'

    REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
    REDIS_PASSWD = os.getenv('REDIS_PASSWD')

    @staticmethod
    def from_app_mode():
        mode = {
            Config.APP_MODE_PRODUCTION: 'config.ProductionConfig',
            Config.APP_MODE_DEVELOPMENT: 'config.DevelopmentConfig',
            Config.APP_MODE_TESTING: 'config.TestingConfig',
        }
        return mode.get(Config.APP_MODE, mode[Config.APP_MODE_DEVELOPMENT])

    @staticmethod
    def database_url(dialect='mysql'):
        if dialect == 'mongodb':
            return '{}://{}:{}@{}'.format(dialect, Config.DB_USER_NAME, Config.DB_USER_PASSWD, Config.DB_HOST)

        return '{}://{}:{}@{}/{}?charset=utf8'.format(dialect, Config.DB_USER_NAME, Config.DB_USER_PASSWD,
                                                      Config.DB_HOST, Config.DB_NAME)


# flask config
class FlaskConfig(object):
    SECRET_KEY = os.urandom(24).hex()
    SQLALCHEMY_DATABASE_URI = Config.database_url()
    # https://stackoverflow.com/questions/33738467/how-do-i-know-if-i-can-disable-sqlalchemy-track-modifications
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    TESTING = False


class ProductionConfig(FlaskConfig):
    pass


class DevelopmentConfig(FlaskConfig):
    SQLALCHEMY_ECHO = True
    DEBUG = True
    TESTING = True


class TestingConfig(FlaskConfig):
    TESTING = True
