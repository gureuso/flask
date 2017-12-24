# -*- coding: utf-8 -*-
from apps.common.commands import manager
from apps.common.database import db
from apps.controllers import app
from config import Config


@app.teardown_request
def shutdown_session(exception=None):
    db.session.remove()


application = app

activate_this = '{0}/venv/bin/activate_this.py'.format(Config.ROOT_DIR)
execfile(activate_this, dict(__file__=activate_this))

if __name__ == "__main__":
    manager.run()
