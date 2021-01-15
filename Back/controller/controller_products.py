from Back.controller.controller_logs import ControllerLog
from Back.controller.controller_base import ControllerBase
from Back.dao_db.dao_products import DaoProduct


class ControllerProduct(ControllerBase):
    def __init__(self, log: object = None) -> None:
        self.__dao = DaoProduct()
        super().__init__(self.__dao)
        ControllerLog().create(log)
