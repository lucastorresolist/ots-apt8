from .base_controller import BaseController
from ..dao_db.products_dao import ProductDao


class ProductController(BaseController):
    def __init__(self) -> None:
        self.__dao = ProductDao()
        super().__init__(self.__dao)
