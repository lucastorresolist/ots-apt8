from Back.controller.base_controller import BaseController
from Back.dao_db.sellers_dao import SellerDao


class SellerController(BaseController):
    def __init__(self)-> None:
        self.__dao = SellerDao()
        super().__init__(self.__dao)
        