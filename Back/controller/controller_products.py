from Back.controller.controller_base import ControllerBase
from Back.dao_db.dao_products import DaoProduct


class ControllerProduct(ControllerBase):
    def __init__(self) -> None:
        self.__dao = DaoProduct()
        super().__init__(self.__dao)
