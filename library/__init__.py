from flask import Flask, request, Blueprint
from .books.controller import books
from .extension import db
from .model import Students, Books, Author, Category, Borrows
import os

def create_db(app):
    if not os.path.exists("library/library.db"):
        with app.app_context():
            db.create_all()
            print("Created DB!")

def create_app(config_file="config.py"):
    app = Flask(__name__)

    #Load configuration first
    app.config.from_pyfile(config_file)
    # Create database
    db.init_app(app)
    # Create database if not exist
    create_db(app)
    # Register blueprint
    app.register_blueprint(books)
    return app
