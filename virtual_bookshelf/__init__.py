from flask import Flask, redirect, render_template, request, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Float, Integer, String, select
from sqlalchemy.orm import Mapped, mapped_column
from werkzeug.wrappers import Response

app = Flask(__name__)
app.config.from_prefixed_env()
bootstrap = Bootstrap5(app)
db = SQLAlchemy(app)


@app.cli.command('create-db')
def create_db() -> None:
    db.create_all()


@app.cli.command('drop-db')
def drop_db() -> None:
    db.drop_all()


class Book(db.Model):   # type: ignore[name-defined]
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True)
    author: Mapped[str] = mapped_column(String(250))
    rating: Mapped[float] = mapped_column(Float(precision=1))


@app.route('/')
def home() -> str:
    all_books = db.session.execute(select(Book)).scalars()
    return render_template('index.html', all_books=all_books)


@app.route('/add', methods=['GET', 'POST'])
def add_book() -> str | Response:
    if request.method == 'POST':
        book = Book(
            title=request.form['book-name'],
            author=request.form['book-author'],
            rating=request.form['rating'],
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('add.html')
