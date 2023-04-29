from flask import Flask
from flask_bootstrap import Bootstrap5

from virtual_bookshelf import config, database, views

bootstrap = Bootstrap5()


def create_app(**kwargs) -> Flask:
    app = Flask(__name__)

    config.init_app(app, **kwargs)
    database.init_app(app)
    views.init_app(app)
    bootstrap.init_app(app)

    return app
