# -*- coding: utf-8 -*-
import flask_script

from apps.common.database import db

manager = flask_script.Manager(usage="Perform database operations")


@manager.command
def init():
    """init db tables"""
    import apps.models.tests

    db.drop_all()
    db.create_all()
