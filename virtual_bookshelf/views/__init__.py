from flask import Flask

from .routes import bp


def init_app(app: Flask) -> Flask:
    app.register_blueprint(bp)
    app.add_url_rule('/', endpoint='index')
    return app
