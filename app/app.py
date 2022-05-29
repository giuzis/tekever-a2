from flask import Flask
from app.api import blueprintAPI


def init_app(testing=False):
    app = Flask("app_name")
    app.config.from_object('app.settings')

    if testing is True:
        app.config["TESTING"] = True

    register_blueprints(app)

    return app


def register_blueprints(app):
    """register all name space for application"""
    app.register_blueprint(blueprintAPI)