from flask import Flask
from flask_bootstrap import Bootstrap5

from virtual_bookshelf import database, views

bootstrap = Bootstrap5()


def create_app() -> Flask:
    app = Flask(__name__)

    database.init_app(app)
    views.init_app(app)
    bootstrap.init_app(app)

    return app
