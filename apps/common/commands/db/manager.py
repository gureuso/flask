# -*- coding: utf-8 -*-
import flask_script

from apps.common.database import init_db

manager = flask_script.Manager(usage="Perform database operations")


@manager.command
def init():
    """init db tables"""
    import apps.models.tests

    init_db()
