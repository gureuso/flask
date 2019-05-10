# -*- coding: utf-8 -*-
import unittest2
import redis

from apps.common.database import redis_session, mongo_client
from apps.controllers.router import app
from apps.models.tests import Test


class TestDatabase(unittest2.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_connect_db(self):
        try:
            rows = Test.query.filter_by(message='test01').all()
            self.assertEqual(len(rows), 0)
        except:
            print('mysql connection error')

    def test_connect_mongodb(self):
        try:
            mongo_client.admin.command('ismaster')
        except:
            print('mongodb connection error')

    def test_connect_redis(self):
        try:
            client_list = redis_session.client_list()
            self.assertIsNot(client_list, [])
        except redis.exceptions.ConnectionError as e:
            print(e)


if __name__ == '__main__':
    unittest2.main()
