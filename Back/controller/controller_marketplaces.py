from Back.models.model_marketplaces import Marketplace
from Back.models.model_logs import Log
from Back.dao_db.dao_marketplaces import (
    save_mkplace,
    list_mkplaces,
    get_by_id,
    update_mktplace,
    delete_mktplace
)


def save_mkp(marketplace: Marketplace) -> None:
    save_mkplace(marketplace)
    log = Log("Saved", "Marketplace")


def list_mkp() -> list:
    list_mkp = list_mkplaces()
    log = Log("Listed", "Marketplaces")

    return list_mkp


def get_mkp_by_id(id: int) -> Marketplace:
    marketplace = get_by_id(id)
    return marketplace


def update_mkp(marketplace: Marketplace) -> None:
    update_mktplace(marketplace)
    log = Log("Update", "Marketplace")


def delete_mkp(id: int) -> None:
    delete_mktplace(id)
    log = Log("Delete", "Marketplace")
