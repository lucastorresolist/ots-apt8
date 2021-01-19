from Back.controller.base_controller import BaseController
from Back.dao_db.dao_categories import DaoCategory


class ControllerCategory(BaseController):
    def __init__(self) -> None:
        self.__dao = DaoCategory()
        super().__init__(self.__dao)
