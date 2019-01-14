# -*- coding: utf-8 -*-
import importlib
import os

from config import Config


class BlueprintRegister(object):
    def __init__(self, app):
        self.app = app
        self.directories = []
        self.root_path = '{}/apps/controllers'.format(Config.ROOT_DIR)
        self.register_blueprint()

    def register_blueprint(self):
        self.find_dir(self.root_path)
        for dir_path in self.directories:
            dir_path = dir_path[1:]

            module_path = 'apps.controllers.{}.controllers'.format(dir_path.replace('/', '.'))
            module = importlib.import_module(module_path)

            if dir_path == 'index':
                dir_path = ''
            self.app.register_blueprint(module.app, url_prefix='/{}'.format(dir_path))

    def find_dir(self, path):
        files = os.listdir(path)
        for file_name in files:
            isdir = os.path.isdir('{}/{}'.format(path, file_name))
            if isdir:
                dir_path = '{}/{}'.format(path, file_name)
                self.directories.append(dir_path.replace(self.root_path, ''))
                self.find_dir(dir_path)
