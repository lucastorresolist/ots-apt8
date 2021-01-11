from Back.dao_txt.dao_categories import save_category, list_categories

def save_cat(name: str, description: str) -> None:
    save_category(name, description)

def list_cat() -> list:
    list_c = list_categories()
    return list_c
