from Back.controller.controller_base import ControllerBase
from Back.dao_db.dao_sellers import SellerDao


class SellerController(ControllerBase):
    def __init__(self)-> None:
        self.__dao = SellerDao()
        super().__init__(self.__dao)
        