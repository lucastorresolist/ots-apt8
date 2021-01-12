from Back.models.marketplace import Marketplace
from Back.dao_db.dao_marketplaces import save_mkplace, list_mkplaces


def save_mkp(marketplace:Marketplace) -> None:
    save_mkplace(marketplace)

def list_mkp() -> list:
    list_mkp = list_mkplaces()
    return list_mkp
