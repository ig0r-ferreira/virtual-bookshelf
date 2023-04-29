from flask import Flask

from virtual_bookshelf import config, views
from virtual_bookshelf.extensions import appearance, database


def create_app(**kwargs) -> Flask:
    app = Flask(__name__)

    config.init_app(app, **kwargs)
    database.init_app(app)
    views.init_app(app)
    appearance.init_app(app)

    return app
