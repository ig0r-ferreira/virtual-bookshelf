from decimal import Decimal

import pytest
from flask import Flask
from flask.testing import FlaskClient, FlaskCliRunner

from virtual_bookshelf import create_app
from virtual_bookshelf.extensions.database import Session, init_db
from virtual_bookshelf.extensions.database.models import Book


def books() -> list[Book]:
    return [
        Book(title='Book 1', author='Author 1', rating=Decimal('8.0')),
        Book(title='Book 2', author='Author 2', rating=Decimal('5.7')),
        Book(title='Book 3', author='Author 3', rating=Decimal('10.0')),
    ]


@pytest.fixture
def app() -> Flask:
    app_ = create_app(
        TESTING=True,
        DATABASE_URI='sqlite://',
        WTF_CSRF_ENABLED=False,
    )

    with app_.app_context():
        init_db()
        Session.add_all(books())
        Session.commit()

    return app_


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()


@pytest.fixture
def cli_runner(app: Flask) -> FlaskCliRunner:
    return app.test_cli_runner()
