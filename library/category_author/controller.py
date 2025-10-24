from flask import Blueprint, request
from library.model import Author
from library.extension import db
from .services import (get_all_authors_service, get_all_category_service, add_author_service, add_category_service)

auth_cate = Blueprint('auth_cate', __name__)

# Get All Authors
@auth_cate.route('/author-management/author', methods=['GET'])
def get_all_author():
    return get_all_authors_service()

# Get All Categories
@auth_cate.route('/category-management/category', methods=['GET'])
def get_all_category():
    return get_all_category_service()

# Add Author
@auth_cate.route('/author-management/author', methods=['POST'])
def add_author():
    return add_author_service()

# Add Category
@auth_cate.route('/category-management/category', methods=['POST'])
def add_category():
    return add_category_service()