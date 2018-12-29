# -*- coding: utf-8 -*-
import flask_migrate
import flask_script
import unittest2
from alembic.util.exc import CommandError

from apps.common.database import db
from apps.controllers import app
from config import Config

migrate = flask_migrate.Migrate(app, db)
manager = flask_script.Manager(app, with_default_commands=False)
manager.add_command('db', flask_migrate.MigrateCommand)


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
    """init db tables & migration"""
    import apps.models.tests

    try:
        flask_migrate.init()
    except CommandError:
        flask_migrate.downgrade(revision='base')

    db.drop_all()
    db.create_all()
    flask_migrate.upgrade()
