from flask import Flask, redirect, render_template, request, url_for
from flask_bootstrap import Bootstrap5
from sqlalchemy import delete, select
from werkzeug.wrappers import Response

from virtual_bookshelf import database
from virtual_bookshelf.database import Session
from virtual_bookshelf.models import Book

app = Flask(__name__)
bootstrap = Bootstrap5(app)
database.init_app(app)


@app.route('/')
def home() -> str:
    all_books = Session.scalars(select(Book)).all()
    return render_template('index.html', all_books=all_books)


@app.route('/add', methods=['GET', 'POST'])
def add_book() -> str | Response:
    if request.method == 'POST':
        book = Book(
            title=request.form['book-name'],
            author=request.form['book-author'],
            rating=float(request.form['rating']),
        )
        Session.add(book)
        Session.commit()
        return redirect(url_for('home'))

    return render_template('add.html')


@app.route('/delete-all')
def delete_all() -> Response:
    Session.execute(delete(Book))
    Session.commit()
    return redirect(url_for('home'))


@app.route('/delete/<int:id>')
def delete_book(id: str) -> Response:
    book = Session.get(Book, id)
    Session.delete(book)
    Session.commit()
    return redirect(url_for('home'))
