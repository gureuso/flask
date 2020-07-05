# -*- coding: utf-8 -*-
from apps.database.session import db
from config import JsonConfig


def get_model(model):
    if JsonConfig.get_data('TESTING'):
        return model.test_model
    return model


class TestMixin:
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.String(120))

    def __init__(self, message=None):
        self.message = message

    def __repr__(self):
        return '<Test {0}>'.format(self.id)


class TestTestModel(TestMixin, db.Model):
    __tablename__ = 'test_tests'
    __table_args__ = {'extend_existing': True}


class TestModel(TestMixin, db.Model):
    __tablename__ = 'tests'
    __table_args__ = {'extend_existing': True}

    test_model = TestTestModel

Test = get_model(TestModel)
