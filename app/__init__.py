from flask import Flask, Blueprint


from config import config


def create_app():
    app = Flask(__name__)


    from .converter import base
    app.register_blueprint(base)

    return app
