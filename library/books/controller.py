from flask import Blueprint

from .services import add_book_service

books = Blueprint('books', __name__)

@books.route('/get-all-books')
def get_all_books():
    return " Book:'How To Print 'HELLO WORLD' Text By Python' "

# METHOD: Add a new book
@books.route('/book-management/book', methods=['POST'])
def add_book():
    return add_book_service()