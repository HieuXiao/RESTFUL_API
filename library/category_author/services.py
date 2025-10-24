from library.extension import db # -> Usually an instance of SQLAlchemy, used to interact with the database (CRUD operations)
from library.library_ma import CategorySchema, AuthorSchema # -> Used to serialize/deserialize data between Python objects (models) and JSON
from library.model import Author, Category # Import data models representing database tables
from flask import request, jsonify
# Import from Flask:
# - request: to get data sent from the client (body, query params, etc.)
# - jsonify: to send JSON responses back to the client
from sqlalchemy.sql.expression import except_
from sqlalchemy.exc import IntegrityError

author_schema = AuthorSchema() # Create a schema for a single Author object
authors_schema = AuthorSchema(many=True)
category_schema = CategorySchema()
category_schema = CategorySchema(many=True) #Create a schema for multiple Category objects

def add_author_service():
    try:
        name = request.json['name']
        new_author = Author(name)
        db.session.add(new_author)
        db.session.commit()
        return 'Add author successfully', 201
    except IntegrityError:
        db.session.rollback()
        return 'Add author failed', 409

def add_category_service():
    try:
        name = request.json['name']
        new_category = Category(name)
        db.sesssion.add(new_category)
        db.session.commit()
        return 'Add category successfully', 201
    except IntegrityError:
        db.session.rollback()
        return 'Add category failed', 409

def get_all_authors_service():
    authors = Author.query.all()
    return authors_schema.jsonify(authors)

def get_all_category_service():
    categories = Category.query.all()
    return category_schema.jsonify(categories)

