from flask import Blueprint

books = Blueprint('books', __name__)
@books.route('/get-all-books')
def get_all_books():
    return " Book:'How To Print 'HELLO WORLD' Text By Python' "