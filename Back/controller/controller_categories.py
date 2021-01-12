from Back.dao_db.dao_categories import save_category, list_categories
from Back.models.categories import Category


def save_cat(category: Category) -> None:
    save_category(category)


def list_cat() -> list:
    list_c = list_categories()
    return list_c
