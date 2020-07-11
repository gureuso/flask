# -*- coding: utf-8 -*-
import unittest2

from apps.database.session import cache
from apps.controllers.router import app
from apps.database.models import Test


class TestDatabase(unittest2.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_connect_db(self):
        rows = Test.query.filter_by(message='test01').all()
        self.assertEqual(len(rows), 0)

    def test_connect_redis(self):
        client_list = cache.client_list()
        self.assertIsNot(client_list, [])


if __name__ == '__main__':
    unittest2.main()
