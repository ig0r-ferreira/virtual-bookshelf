from flask import Flask
from flask_bootstrap import Bootstrap5

from virtual_bookshelf import database, views

app = Flask(__name__)
bootstrap = Bootstrap5(app)
database.init_app(app)
views.init_app(app)
