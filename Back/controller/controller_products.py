from Back.models.model_products import Product
from Back.models.model_logs import Log
from Back.dao_db.dao_products import list_product_byId, save_product, list_products, update_product, delete_product
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


def list_prod_byId(id: int) -> Product:
    product = list_product_byId(id)
    return product


def delete_prod(id: int) -> bool:
    try:
        if delete_product(id):
            log = Log("Delete", "Products")
            save_l(log)
            return True
        return False
    except Exception as e:
        return False


def update_pro(product: Product) -> bool:
    try:
        if update_product(product):
            log = Log("Update", "Products")
            save_l(log)
            return True
        return False
    except Exception as e:
        return False
