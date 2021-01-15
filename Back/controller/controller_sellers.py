from Back.controller.controller_base import BaseController
from Back.dao_db.dao_sellers import SellerDao
from Back.controller.controller_logs import ControllerLog


class SellerController(BaseController):
    def __init__(self, log:object = None)-> None:
        self.__dao = SellerDao()
        super().__init__(self.__dao)
        ControllerLog().create(log)
