# -*- coding: utf-8 -*-
from flask import Blueprint, send_from_directory

from apps.common.response import Response
from config import Config

app = Blueprint('index', __name__)


@app.route('/', methods=['get'])
def index():
    return Response.ok('Index')


@app.route('favicon.ico')
def favicon():
    return send_from_directory(Config.STATIC_DIR, 'favicon.ico', mimetype='image/vnd.microsoft.icon')
