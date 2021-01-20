from sqlalchemy.orm import sessionmaker
from Back.models.products_model import Product
from .base_dao import BaseDao


class ProductDao(BaseDao):
    def __init__(self):
        super().__init__(Product)

    def entity(self):
            return f'Product'
