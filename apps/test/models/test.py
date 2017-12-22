# -*- coding: utf-8 -*-
import unittest2
from apps.models.database import init_db, db_session

from apps.models.tests import Test
from run import app


class TestDatabase(unittest2.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        init_db()

    def tearDown(self):
        Test.query.filter_by(message='test01').delete()
        db_session.commit()

    def test_connect_db(self):
        t = Test('test01')
        db_session.add(t)
        db_session.commit()

        rows = Test.query.filter_by(message='test01').all()
        self.assertEqual(len(rows), 1)


if __name__ == '__main__':
    unittest2.main()
