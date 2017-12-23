# -*- coding: utf-8 -*-
import unittest2
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from apps.common.database import db, create_app
from apps.controllers import app
from config import Config


@app.teardown_request
def shutdown_session(exception=None):
    db.session.remove()


application = app

activate_this = '{0}/venv/bin/activate_this.py'.format(Config.ROOT_DIR)
execfile(activate_this, dict(__file__=activate_this))

# command
migrate = Migrate(app, db)
manager = Manager(app, with_default_commands=False)
manager.add_command('db', MigrateCommand)


@manager.command
def initdb():
    """init db tables"""
    import apps.models.tests
    db.engine.execute("DROP TABLE alembic_version")
    db.drop_all()
    db.create_all()


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

if __name__ == "__main__":
    manager.run()
