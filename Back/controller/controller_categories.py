from Back.models.model_categories import Category
from Back.dao_txt.dao_categories import save_category, list_categories


def save_cat(category: Category) -> None:
    save_category(category)


def list_cat() -> list:
    list_c = list_categories()
    return list_c
