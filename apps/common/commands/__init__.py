# -*- coding: utf-8 -*-
import unittest2
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from apps.common.commands.init import manager as initManager
from apps.common.database import db
from apps.controllers import app
from config import Config

migrate = Migrate(app, db)
manager = Manager(app, with_default_commands=False)
manager.add_command('db', MigrateCommand)
manager.add_command('init', initManager)


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
