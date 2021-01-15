from Back.controller.controller_logs import ControllerLog
from Back.controller.controller_base import ControllerBase
from Back.dao_db.dao_categories import DaoCategory


class ControllerCategory(ControllerBase):
    def __init__(self, log: object = None) -> None:
        self.__dao = DaoCategory()
        super().__init__(self.__dao)
        if log:
            ControllerLog().create(log)
