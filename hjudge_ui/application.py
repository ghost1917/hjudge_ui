import logging

from flask import Flask


class Application(object):
    def __init__(self, decorators):
        self.decorators = decorators
        self.app = Flask(__name__, static_url_path='')

    def create(self):
        self.app.logger.addHandler(logging.StreamHandler())
        self.app.logger.setLevel(logging.DEBUG)
        self.app.config.from_object(__name__)

        for decorator in self.decorators:
            decorator(self.app)
        return self.app

