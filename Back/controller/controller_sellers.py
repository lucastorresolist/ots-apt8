from Back.models.seller import Seller
from Back.models.log import Log
from Back.dao_db.dao_sellers import save_seller, list_sellers
from Back.controller.controller_logs import save_l


def save_sell(seller:Seller) -> None:
    save_seller(seller)
    log = Log("Saved", "Seller")
    save_l(log)

def list_sell() -> list:
    list_sel = list_sellers()
    log = Log("Listed", "Sellers")
    save_l(log)
    return list_sel
