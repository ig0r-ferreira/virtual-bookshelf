from decimal import Decimal
from http import HTTPStatus

import pytest
from flask.testing import FlaskClient

from virtual_bookshelf.database import Session
from virtual_bookshelf.database.models import Book


def test_access_homepage_should_return_http_code_200(
    client: FlaskClient,
) -> None:
    response = client.get('/')
    data = response.get_data(as_text=True)

    assert response.status_code == HTTPStatus.OK
    assert 'My Virtual Bookshelf' in data
    assert 'Book 1' in data
    assert 'Book 2' in data
    assert 'Book 3' in data


def test_access_add_book_page_should_return_http_code_200(
    client: FlaskClient,
) -> None:
    response = client.get('/add')
    data = response.get_data(as_text=True)

    assert response.status_code == HTTPStatus.OK
    assert 'Add new book' in data


def test_add_book_should_return_http_code_302_and_return_to_homepage(
    client: FlaskClient,
) -> None:
    response = client.post(
        '/add',
        data={
            'book_title': 'Book 4',
            'book_author': 'Author 4',
            'book_rating': 5.7,
        },
    )
    assert response.status_code == HTTPStatus.FOUND
    assert response.headers['Location'] == '/'

    with client.application.app_context():
        book = Session.get(Book, 4)

    assert book is not None
    assert book.title == 'Book 4'
    assert book.author == 'Author 4'
    assert book.rating == Decimal('5.7')


@pytest.mark.parametrize(
    'book_data',
    [
        {
            'book_title': 'Best Book',
            'book_author': 'Best Author',
            'book_rating': 10.1,
        },
        {
            'book_title': 'Worst Book',
            'book_author': 'Worst Author',
            'book_rating': -1,
        },
    ],
)
def test_add_book_with_rating_outside_the_range_of_0_to_10_should_return_an_error(
    client: FlaskClient, book_data: dict
) -> None:
    response = client.post(
        '/add',
        data=book_data,
    )
    data = response.get_data(as_text=True)
    assert response.status_code == HTTPStatus.OK
    assert 'Number must be between 0 and 10.' in data


def test_add_an_existing_book_should_return_an_error_message(
    client: FlaskClient,
) -> None:
    response = client.post(
        '/add',
        data={
            'book_title': 'Book 2',
            'book_author': 'Author 2',
            'book_rating': 3.0,
        },
    )
    data = response.get_data(as_text=True)

    assert response.status_code == HTTPStatus.OK
    assert 'Error: Book &#39;Book 2&#39; is already registered.' in data


@pytest.mark.parametrize('id', [1, 2, 3])
def test_delete_book_should_return_http_code_302_and_return_to_homepage(
    id: int,
    client: FlaskClient,
) -> None:
    response = client.get(f'/delete/{id}')

    assert response.status_code == HTTPStatus.FOUND
    assert response.headers['Location'] == '/'
    with client.application.app_context():
        assert Session.get(Book, id) is None


def test_access_edit_book_page_should_return_http_code_200(
    client: FlaskClient,
) -> None:
    response = client.get('/edit/1')
    data = response.get_data(as_text=True)

    assert response.status_code == HTTPStatus.OK
    assert 'Edit book data' in data


def test_edit_book_page_should_return_http_code_302_and_return_to_homepage(
    client: FlaskClient,
) -> None:
    id = 2
    response = client.post(f'/edit/{id}', data={'book_rating': 0})

    assert response.status_code == HTTPStatus.FOUND
    assert response.headers['Location'] == '/'

    with client.application.app_context():
        book = Session.get(Book, id)
        assert book is not None and book.rating == Decimal('0.0')


def test_edit_a_non_existent_book_should_return_error_404(
    client: FlaskClient,
) -> None:
    response = client.get('/edit/9')

    assert response.status_code == HTTPStatus.NOT_FOUND
