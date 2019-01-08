# -*- coding: utf-8 -*-
import flask_script
import unittest2

from apps.common.commands.db.manager import manager as db_manager
from apps.controllers.route import app
from config import Config

manager = flask_script.Manager(app, with_default_commands=False)
manager.add_command("db", db_manager)


@manager.command
def test():
    """test code"""
    loader = unittest2.TestLoader()
    start_dir = '{0}/apps'.format(Config.ROOT_DIR)
    suite = loader.discover(start_dir)

    runner = unittest2.TextTestRunner()
    runner.run(suite)


@manager.option('-h', '--host', dest='host', default=Config.APP_HOST)
@manager.option('-p', '--port', dest='port', default=Config.APP_PORT)
def runserver(host, port):
    """run flask server"""
    app.run(host=host, port=int(port))
