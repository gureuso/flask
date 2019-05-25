# -*- coding: utf-8 -*-
from apps.controllers.router import app
from apps.common.commands.manager import manager
from config import Config

application = app

if Config.APP_VENV == 'true':
    activate_this = '{0}/venv/bin/activate_this.py'.format(Config.ROOT_DIR)
    exec(open(activate_this).read())

if __name__ == '__main__':
    manager.run()
