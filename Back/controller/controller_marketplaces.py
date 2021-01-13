from Back.models.model_marketplaces import Marketplace
from Back.models.model_logs import Log
from Back.dao_db.dao_marketplaces import save_mkplace, list_mkplaces
from Back.controller.controller_logs import save_l


def save_mkp(marketplace:Marketplace) -> None:
    save_mkplace(marketplace)
    log = Log("Saved", "Marketplace")
    save_l(log)

def list_mkp() -> list:
    list_mkp = list_mkplaces()
    log = Log("Listed", "Marketplaces")
    save_l(log)
    return list_mkp
