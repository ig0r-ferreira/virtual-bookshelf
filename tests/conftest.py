import pytest
from flask import Flask
from flask.testing import FlaskClient

from virtual_bookshelf import create_app
from virtual_bookshelf.database import Session, create_tables
from virtual_bookshelf.database.models import Book


def books() -> list[Book]:
    return [
        Book(title='Book 1', author='Author 1', rating=8.0),
        Book(title='Book 2', author='Author 2', rating=5.0),
        Book(title='Book 3', author='Author 3', rating=10.0),
    ]


@pytest.fixture
def app() -> Flask:
    app_ = create_app({'TESTING': True, 'DATABASE_URI': 'sqlite://'})

    with app_.app_context():
        create_tables()
        Session.add_all(books())
        Session.commit()

    return app_


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()
