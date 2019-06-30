# -*- coding: utf-8 -*-
from apps.controllers.router import app
from apps.database.session import db


def get_model(model):
    if app.testing:
        return model.test_model
    return model


class Test(db.Model):
    __tablename__ = 'tests'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.String(120))

    def __init__(self, message=None):
        self.message = message

    def __repr__(self):
        return '<Test {0}>'.format(self.id)
