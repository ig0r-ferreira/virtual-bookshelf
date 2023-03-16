import os

import click
from dotenv import load_dotenv
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from virtual_bookshelf.models import Base

load_dotenv()

DATABASE_URL: str = os.getenv('SQLALCHEMY_DATABASE_URI', '')
engine = create_engine(DATABASE_URL)
Session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)


@click.command('create-tables')
def create_tables() -> None:
    Base.metadata.create_all(engine)


def close_db(e=None) -> None:
    Session.remove()


def init_app(app: Flask) -> None:
    app.teardown_appcontext(close_db)
    app.cli.add_command(create_tables)
