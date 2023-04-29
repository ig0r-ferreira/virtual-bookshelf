import click
from flask import Flask
from sqlalchemy import create_engine, delete, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import scoped_session, sessionmaker

from .models import Base

Session = scoped_session(sessionmaker(autoflush=False))


def create_tables() -> None:
    """Creates all tables in the database."""
    Base.metadata.create_all(Session.get_bind())


def init_app(app: Flask) -> None:
    engine = create_engine(app.config['DATABASE_URI'])
    Session.configure(bind=engine)

    @app.teardown_appcontext
    def remove_session(exception=None) -> None:
        Session.remove()

    app.cli.add_command(click.command(create_tables))
