# -*- coding: utf-8 -*-
import flask_script
import unittest2

from apps.common.database import db
from apps.controllers import app
from config import Config

manager = flask_script.Manager(app, with_default_commands=False)


@manager.command
def test():
    """test code"""
    loader = unittest2.TestLoader()
    start_dir = '{0}/apps'.format(Config.ROOT_DIR)
    suite = loader.discover(start_dir)

    runner = unittest2.TextTestRunner()
    runner.run(suite)


@manager.command
def runserver():
    """run flask server"""
    app.run(host=Config.APP_HOST, port=Config.APP_PORT)


@manager.command
def init():
    """init db tables"""
    import apps.models.tests

    db.drop_all()
    db.create_all()
