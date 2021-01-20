from .base_dao import BaseDao
from Back.models.categories_model import Category


class CategoryDao(BaseDao):
    def __init__(self):
        super().__init__(Category)

