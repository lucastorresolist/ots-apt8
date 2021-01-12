from Back.models.seller import Seller
from Back.dao_db.dao_sellers import save_seller, list_sellers


def save_sell(seller:Seller) -> None:
    save_seller(seller)

def list_sell() -> list:
    list_sel = list_sellers()
    return list_sel
