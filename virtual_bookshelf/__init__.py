from flask import Flask, redirect, render_template, request, url_for
from flask_bootstrap import Bootstrap5
from werkzeug.wrappers import Response

app = Flask(__name__)
bootstrap = Bootstrap5(app)


@app.route('/')
def home() -> str:
    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add_book() -> str | Response:
    if request.method == 'POST':
        return redirect(url_for('home'))

    return render_template('add.html')
