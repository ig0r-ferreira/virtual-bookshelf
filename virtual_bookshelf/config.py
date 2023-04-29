from dotenv import load_dotenv
from flask import Flask

load_dotenv()


def init_app(app: Flask, **config) -> None:
    app.config.from_prefixed_env()
    if config:
        app.config.from_mapping(config)
