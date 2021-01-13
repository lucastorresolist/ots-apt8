from Back.controller.controller_logs import save_l
from Back.dao_db.dao_categories import delete_category, list_category_byId, save_category, list_categories, update_category
from Back.models.model_logs import Log
from Back.models.model_categories import Category


def save_cat(category: Category) -> None:
    save_category(category)
    log = Log("Saved", "Category")
    save_l(log)


def list_cat() -> list:
    list_c = list_categories()
    log = Log("Listed", "Category")
    save_l(log)
    return list_c


def list_cat_byId(id: int) -> Category:
    category = list_category_byId(id)
    return category


def delete_cat(id: int) -> bool:
    try:
        if delete_category(id):
            return True
        return False
    except Exception as e:
        return False


def update_cat(category: Category) -> bool:
    try:
        if update_category(category):
            return True
        return False
    except Exception as e:
        return False
