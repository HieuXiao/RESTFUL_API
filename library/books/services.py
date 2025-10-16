from library.extension import db
from library.library_ma import BookSchema
from library.model import Books
from flask import request, jsonify

book_schema = BookSchema()
books_schema = BookSchema(many=True)


def add_book_service():
    data = request.json
    if (data and ('name' in data) and ('page_count' in data)
            and ('author_id' in data) and ('category_id' in data)):
        name = data['name']
        page_count = data['page_count']
        author_id = data['author_id']
        category_id = data['category_id']
        try:
            new_book = Books(name, page_count, author_id, category_id)
            db.session.add(new_book)
            db.session.commit()
            return 'Add new book successfully', 201
        except IndentationError:
            db.session.rollback()
            return "Can't add new book", 400
    else:
        return 'Request error', 400


def get_book_by_id_service(id):
    book = Books.query.get(id)
    if book:
        return book_schema.jsonify(book)
    else:
        return 'Book not found', 404


def get_all_books_service():
    books = Books.query.all()
    if books:
        return books_schema.jsonify(books)
    else:
        return 'No book found', 404


def update_book_by_id_service(id):
    book = Books.query.get(id)
    data = request.json
    if book:
        if data and 'page_count' in data:
            try:
                book.page_count = data['page_count']
                db.session.commit()
                return 'Update book successfully', 200
            except IndentationError:
                db.session.rollback()
                return "Can't update book", 400
    else:
        return 'Book not found', 404


def delete_book_by_id_service(id):
    book = Books.query.get(id)
    if book:
        try:
            db.session.delete(book)
            db.session.commit()
            return 'Delete book successfully', 200
        except IndentationError:
            db.session.rollback()
            return "Can't delete book", 400
    else:
        return 'Book not found', 404
