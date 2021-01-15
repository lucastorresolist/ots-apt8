from Back.controller.controller_base import ControllerBase
from Back.dao_db.dao_marketplaces import MarketplaceDao


class MarketplaceController(ControllerBase):
    def __init__(self)-> None:
        self.__dao = MarketplaceDao()
        super().__init__(self.__dao)
