from Back.controller.controller_base import ControllerBase
from Back.dao_db.dao_logs import DaoLog


class ControllerLog(ControllerBase):
    def __init__(self) -> None:
        self.__dao = DaoLog()
        super().__init__(self.__dao)
