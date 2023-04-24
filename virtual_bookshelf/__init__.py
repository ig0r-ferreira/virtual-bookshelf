from typing import Any

from dotenv import load_dotenv
from flask import Flask
from flask_bootstrap import Bootstrap5

from virtual_bookshelf import database, views

bootstrap = Bootstrap5()
load_dotenv()


def create_app(config: dict[str, Any] = dict()) -> Flask:
    app = Flask(__name__)
    app.config.from_prefixed_env()
    if config:
        app.config.from_mapping(config)

    database.init_app(app)
    views.init_app(app)
    bootstrap.init_app(app)

    return app
