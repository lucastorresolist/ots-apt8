from Back.controller.base_controller import BaseController
from Back.dao_db.dao_products import DaoProduct


class ControllerProduct(BaseController):
    def __init__(self) -> None:
        self.__dao = DaoProduct()
        super().__init__(self.__dao)
