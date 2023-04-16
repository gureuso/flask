# -*- coding: utf-8 -*-
import click
import unittest2
from flask_migrate import Migrate


from apps.controllers.router import app
from apps.database.session import db
from config import Config

migrate = Migrate(app, db)


@app.cli.command('test')
def test():
    """test code"""
    loader = unittest2.TestLoader()
    start_dir = '{0}/apps'.format(Config.ROOT_DIR)
    suite = loader.discover(start_dir)

    runner = unittest2.TextTestRunner()
    r = runner.run(suite)

    if r.wasSuccessful():
        print('success')
    else:
        print('fail')
        exit(1)
