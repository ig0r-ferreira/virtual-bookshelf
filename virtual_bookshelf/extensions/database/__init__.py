import click
from flask import Flask
from sqlalchemy import create_engine, delete, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import scoped_session, sessionmaker

from .models import Base

Session = scoped_session(sessionmaker(autoflush=False))


def init_db() -> None:
    Base.metadata.drop_all(Session.get_bind())
    Base.metadata.create_all(Session.get_bind())


def init_app(app: Flask) -> None:
    engine = create_engine(app.config['DATABASE_URI'])
    Session.configure(bind=engine)

    @app.teardown_appcontext
    def remove_session(exception=None) -> None:
        Session.remove()

    @click.command('init-db')
    def init_db_command():
        """Clear the existing data and create new tables."""
        init_db()
        click.echo('Initialized the database.')

    app.cli.add_command(init_db_command)
