from Back.controller.controller_base import BaseController
from Back.dao_db.dao_marketplaces import MarketplaceDao
from Back.controller.controller_logs import ControllerLog


class MarketplaceController(BaseController):
    def __init__(self, log:object = None)-> None:
        self.__dao = MarketplaceDao()
        super().__init__(self.__dao)
        ControllerLog().create(log)

        