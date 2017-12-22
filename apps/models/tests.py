# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String

from apps.common.database import Base


class Test(Base):
    __tablename__ = 'tests'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    message = Column(String(120))

    def __init__(self, message=None):
        self.message = message

    def __repr__(self):
        return '<Test {0}>'.format(self.message)
