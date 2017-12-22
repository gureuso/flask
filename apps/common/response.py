# -*- coding: utf-8 -*-
import json
from flask import make_response

from config import Config


def ok(data=None, code=20000):
    res = json.dumps({
        "data": data or {},
        "code": code,
    })
    return makeResponse(res, code)


def error(code):
    res = json.dumps({
        "code": code,
        "message": Config.ERROR_CODE[code],
    })
    return makeResponse(res, code)


def makeResponse(data, code):
    statusCode = code / 100
    resp = make_response(data, statusCode)
    resp.headers['Content-Type'] = 'application/json'
    return resp
