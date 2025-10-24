from .extension import ma
from .model import Books, Category, Author

class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Books
        load_instance = True
        include_fk = True   # để hiển thị khóa ngoại (author_id, category_id)

class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category
        load_instance = True

class AuthorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Author
        load_instance = True
