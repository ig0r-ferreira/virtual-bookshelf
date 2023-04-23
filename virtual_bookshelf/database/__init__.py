from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from .models import Base

Session = scoped_session(sessionmaker(autoflush=False))


def init_app(app: Flask) -> None:
    engine = create_engine(app.config['DB_URI'])
    Session.configure(bind=engine)

    @app.teardown_appcontext
    def remove_session(exception=None) -> None:
        Session.remove()

    @app.cli.command('create-tables')
    def create_tables() -> None:
        """Creates all tables in the database."""
        Base.metadata.create_all(engine)
