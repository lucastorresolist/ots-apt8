from Back.models.model_categories import Category
from Back.models.log import Log
from Back.dao_db.dao_categories import save_category, list_categories
from Back.controller.controller_logs import save_l


def save_cat(category: Category) -> None:
    save_category(category)
    log = Log("Saved", "Category")
    save_l(log)

def list_cat() -> list:
    list_c = list_categories()
    log = Log("Listed", "Category")
    save_l(log)
    return list_c
