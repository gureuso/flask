# -*- coding: utf-8 -*-
from apps.controllers.router import app
from apps.common.commands.manager import manager
from config import Config

application = app

activate_this = '{0}/venv/bin/activate_this.py'.format(Config.ROOT_DIR)
execfile(activate_this, dict(__file__=activate_this))


if __name__ == '__main__':
    manager.run()
