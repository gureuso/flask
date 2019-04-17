# -*- coding: utf-8 -*-
import unittest2
import redis

from apps.common.database import db_session, redis_session
from apps.controllers.router import app
from apps.models.tests import Test


class TestDatabase(unittest2.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        Test.query.filter_by(message='test01').delete()
        db_session.commit()

    def test_connect_db(self):
        t = Test('test01')
        db_session.add(t)
        db_session.commit()

        rows = Test.query.filter_by(message='test01').all()
        self.assertEqual(len(rows), 1)

    def test_connect_redis(self):
        try:
            client_list = redis_session.client_list()
            self.assertIsNot(client_list, [])
        except redis.exceptions.ConnectionError as e:
            print(e)


if __name__ == '__main__':
    unittest2.main()
