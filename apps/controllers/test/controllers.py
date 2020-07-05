# -*- coding: utf-8 -*-
import requests
from flask import Blueprint, abort, render_template, request

from apps.common.response import ok, error
from apps.database.models import Test

app = Blueprint('test', __name__, url_prefix='/test')


@app.route('/ping', methods=['get'])
def ping():
    return ok('pong')


@app.route('/proxy', methods=['get', 'post'])
def proxy():
    args = request.args
    form = request.form
    url = args.get('url')

    if not url:
        return error(50000)

    if request.method == 'GET':
        res = requests.get(url=url)
    else:
        res = requests.post(url=url, data=form)

    return ok(dict(url=res.url, data=res.text, code=res.status_code))


@app.route('/db', methods=['get'])
def db():
    test = Test.query.first()
    if test:
        message = test.message
    else:
        message = None
    return ok({'message': message})


@app.route('/403', methods=['get'])
def forbidden():
    return abort(403)


@app.route('/404', methods=['get'])
def page_not_found():
    return abort(404)


@app.route('/410', methods=['get'])
def gone():
    return abort(410)


@app.route('/500', methods=['get'])
def internal_server_error():
    return abort(500)


@app.route('/html', methods=['get'])
def html():
    return render_template('test/html.html', name=html.__name__)
