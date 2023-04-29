from decimal import Decimal

from flask import Blueprint, abort, flash, redirect, render_template, url_for
from flask.typing import ResponseReturnValue

from virtual_bookshelf.extensions.database import (
    IntegrityError,
    Session,
    select,
)
from virtual_bookshelf.extensions.database.models import Book
from virtual_bookshelf.extensions.forms import AddBook, EditBook

bp = Blueprint('bookshelf', __name__)


def _convert_to_decimal(value: Decimal | None) -> Decimal:
    if value is None:
        return Decimal('NaN')

    return value


@bp.route('/')
def index() -> str:
    all_books = Session.scalars(select(Book)).all()
    return render_template('index.html', all_books=all_books)


@bp.route('/add', methods=['GET', 'POST'])
def add_book() -> ResponseReturnValue:
    form = AddBook()

    if form.validate_on_submit():
        book_title = form.book_title.data
        book = Book(
            title=book_title,
            author=form.book_author.data,
            rating=_convert_to_decimal(form.book_rating.data),
        )
        try:
            Session.add(book)
            Session.commit()
        except IntegrityError:
            flash(f'Book {book_title!a} is already registered.', 'danger')
        else:
            return redirect(url_for('index'))

    return render_template('add.html', form=form)


@bp.route('/delete/<int:id>')
def delete_book(id: int) -> ResponseReturnValue:
    book = Session.get(Book, id)
    Session.delete(book)
    Session.commit()
    return redirect(url_for('index'))


@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_book(id: int) -> ResponseReturnValue:
    book = Session.get(Book, id)
    if not book:
        abort(404)

    form = EditBook(
        data={'book_title': book.title, 'book_author': book.author}
    )

    if form.validate_on_submit():
        book.rating = _convert_to_decimal(form.book_rating.data)
        Session.commit()
        return redirect(url_for('index'))

    return render_template('edit.html', form=form, book=book)
