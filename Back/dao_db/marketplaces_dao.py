from .base_dao import BaseDao
from Back.models.marketplaces_model import Marketplace


class MarketplaceDao(BaseDao):
    def __init__(self):
        super().__init__(Marketplace)

    def entity(self):
        return f'Marketplace'
