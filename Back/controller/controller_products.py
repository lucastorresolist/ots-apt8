from Back.dao_txt.dao_products import save_product, list_products

def save_prod(name: str, description: str, price: float) -> None:
    save_product(name, description, price)

def list_prod() -> list:
    list_pro = list_products()
    return list_pro
