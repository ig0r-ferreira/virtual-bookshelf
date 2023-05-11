import pathlib

from dotenv import load_dotenv
from flask import Flask

load_dotenv()


def init_app(app: Flask, **config) -> None:
    pathlib.Path(app.instance_path).mkdir(exist_ok=True)
    app.config['DATABASE_URI'] = 'sqlite:///instance/bookshelf.db'
    app.config.from_prefixed_env()
    if config:
        app.config.from_mapping(config)
