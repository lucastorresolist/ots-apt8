from Back.models.model_sellers import Seller
from Back.models.model_logs import Log
from Back.dao_db.dao_sellers import (
    save_seller,
    list_sellers,
    get_by_id,
    update_seller,
    delete_seller
)


def save_sell(seller: Seller) -> None:
    save_seller(seller)
    log = Log("Saved", "Seller")


def list_sell() -> list:
    list_sel = list_sellers()
    log = Log("Listed", "Sellers")
    return list_sel


def get_seller_by_id(id: int) -> Seller:
    seller = get_by_id(id)
    return seller


def update_sell(seller: Seller) -> None:
    update_seller(seller)
    log = Log("Update", "Seller")


def delete_sell(id: int) -> None:
    delete_seller(id)
    log = Log("Delete", "Seller")
