from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask.typing import ResponseReturnValue

from virtual_bookshelf.database import IntegrityError, Session, delete, select
from virtual_bookshelf.database.models import Book

bp = Blueprint('bookshelf', __name__)


@bp.route('/')
def index() -> str:
    all_books = Session.scalars(select(Book)).all()
    return render_template('index.html', all_books=all_books)


@bp.route('/add', methods=['GET', 'POST'])
def add_book() -> ResponseReturnValue:
    if request.method == 'POST':
        book_title = request.form['book-title']
        book = Book(
            title=book_title,
            author=request.form['book-author'],
            rating=float(request.form['rating']),
        )
        Session.add(book)
        try:
            Session.commit()
        except IntegrityError:
            flash(f'Book {book_title!a} is already registered.', 'error')
        else:
            return redirect(url_for('index'))

    return render_template('add.html')


@bp.route('/delete/<int:id>')
def delete_book(id: int) -> ResponseReturnValue:
    book = Session.get(Book, id)
    Session.delete(book)
    Session.commit()
    return redirect(url_for('index'))


@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_book(id: int) -> ResponseReturnValue:
    book = Session.get(Book, id)
    if request.method == 'POST' and book:
        book.rating = float(request.form['rating'])
        Session.commit()
        return redirect(url_for('index'))

    return render_template('edit.html', book=book)
