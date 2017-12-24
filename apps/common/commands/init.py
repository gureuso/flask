# -*- coding: utf-8 -*-
import flask_migrate
from alembic.util.exc import CommandError
from flask_script import Manager

from apps.common.database import db as dbSession

manager = Manager(usage="Perform init operations")


@manager.command
def db():
    """init db tables & migration"""
    import apps.models.tests

    try:
        flask_migrate.init()
    except CommandError:
        flask_migrate.downgrade(revision='base')

    dbSession.drop_all()
    dbSession.create_all()
    flask_migrate.upgrade()
