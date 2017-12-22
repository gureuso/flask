# -*- coding: utf-8 -*-
from flask import Blueprint, abort, render_template

from apps.common.response import ok

app = Blueprint('test', __name__)


@app.route('/ping', methods=['get'])
def ping():
    return ok('pong')


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
