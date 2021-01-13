from Back.models.model_products import Product
from Back.dao_txt.dao_products import save_product, list_products


def save_prod(product: Product) -> None:
    save_product(product)


def list_prod() -> list:
    list_pro = list_products()
    return list_pro
