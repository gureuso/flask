# -*- coding: utf-8 -*-
import flask
import json

from config import Config


class Response(object):
    @classmethod
    def ok(cls, data=None, code=20000):
        res = json.dumps({
            "data": data or {},
            "code": code
        })
        return cls.make_response(res, code)

    @classmethod
    def error(cls, code, message=None):
        if not message:
            message = Config.ERROR_CODE[code]

        res = json.dumps({
            "code": code,
            "message": message
        })
        return cls.make_response(res, code)

    @staticmethod
    def make_response(data, code):
        statusCode = code / 100
        resp = flask.make_response(data, statusCode)
        resp.headers['Content-Type'] = 'application/json'
        return resp
