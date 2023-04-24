from http import HTTPStatus

from flask import Flask
from flask.testing import FlaskClient

from virtual_bookshelf.database import Session
from virtual_bookshelf.database.models import Book


def test_access_homepage_should_return_http_code_200(
    client: FlaskClient,
) -> None:
    response = client.get('/')
    response_content = response.get_data(as_text=True)

    assert response.status_code == HTTPStatus.OK
    assert 'My Virtual Bookshelf' in response_content
    assert 'Book 1' in response_content
    assert 'Book 2' in response_content
    assert 'Book 3' in response_content


def test_access_add_book_page_should_return_http_code_200(
    client: FlaskClient,
) -> None:
    response = client.get('/add')
    response_content = response.get_data(as_text=True)

    assert response.status_code == HTTPStatus.OK
    assert 'Add new book' in response_content


def test_add_book_should_return_http_code_302_and_return_to_homepage(
    app: Flask,
    client: FlaskClient,
) -> None:
    response = client.post(
        '/add',
        data={
            'book-title': 'Book 4',
            'book-author': 'Author 4',
            'book-rating': 7.5,
        },
    )

    assert response.status_code == HTTPStatus.FOUND
    assert response.headers['Location'] == '/'

    with app.app_context():
        book = Session.get(Book, 4)

    assert book is not None
    assert book.title == 'Book 4'
    assert book.author == 'Author 4'
    assert book.rating == 7.5


def test_add_an_existing_book_should_return_an_error_message(
    client: FlaskClient,
) -> None:
    response = client.post(
        '/add',
        data={
            'book-title': 'Book 2',
            'book-author': 'Author 2',
            'book-rating': 3.0,
        },
    )
    response_content = response.get_data(as_text=True)

    assert response.status_code == HTTPStatus.OK
    assert (
        'Error: Book &#39;Book 2&#39; is already registered.'
        in response_content
    )


def test_delete_book_should_return_http_code_302_and_return_to_homepage(
    app: Flask,
    client: FlaskClient,
) -> None:
    response = client.get('/delete/1')

    assert response.status_code == HTTPStatus.FOUND
    assert response.headers['Location'] == '/'
    with app.app_context():
        assert Session.get(Book, 1) is None


def test_access_edit_book_page_should_return_http_code_200(
    client: FlaskClient,
) -> None:
    response = client.get('/edit/1')
    response_content = response.get_data(as_text=True)

    assert response.status_code == HTTPStatus.OK
    assert 'Edit book data' in response_content


def test_edit_book_page_should_return_http_code_302_and_return_to_homepage(
    app: Flask,
    client: FlaskClient,
) -> None:
    id = 2
    response = client.post(f'/edit/{id}', data={'book-rating': 0})

    assert response.status_code == HTTPStatus.FOUND
    assert response.headers['Location'] == '/'
    with app.app_context():
        assert (book := Session.get(Book, id)) and book.rating == 0
