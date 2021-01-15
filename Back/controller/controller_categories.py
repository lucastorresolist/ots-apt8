from Back.controller.controller_base import ControllerBase
from Back.dao_db.dao_categories import DaoCategory


class ControllerCategory(ControllerBase):
    def __init__(self) -> None:
        self.__dao = DaoCategory()
        super().__init__(self.__dao)
