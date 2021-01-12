from Back.models.products import Product
from Back.models.log import Log
from Back.dao_db.dao_products import save_product, list_products
from Back.controller.controller_logs import save_l


def save_prod(product: Product) -> None:
    save_product(product)
    log = Log("Saved", "Product")
    save_l(log)

def list_prod() -> list:
    list_pro = list_products()
    log = Log("Listed", "Products")
    save_l(log)
    return list_pro
