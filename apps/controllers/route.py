# -*- coding: utf-8 -*-
from flask import Flask

from apps.common.response import error
from apps.controllers.index.controllers import app as index_app
from apps.controllers.test.controllers import app as test_app
from config import Config

app = Flask(__name__, template_folder=Config.TEMPLATES_DIR)
app.config.from_object(Config.from_app_mode())
app.register_blueprint(index_app, url_prefix='/')
app.register_blueprint(test_app, url_prefix='/test')


@app.errorhandler(403)
def forbidden(err):
    return error(40300)


@app.errorhandler(404)
def page_not_found(err):
    return error(40400)


@app.errorhandler(410)
def gone(err):
    return error(41000)


@app.errorhandler(500)
def internal_server_error(err):
    return error(50000)
