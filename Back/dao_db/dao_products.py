from Back.models.model_products import Product
from .base_dao import BaseDao


class DaoProduct(BaseDao):

    def create(self, model: Product) -> None:
        script = f"INSERT INTO products (name, description, price) values ('{model.name}','{model.description}', '{model.price}')"
        return super().execute(script)

    def read_all(self):
        list_products = []
        script = "SELECT id, name, description, price FROM products"
        result = super().read(script)
        for item in result:
            produto = Product(item[1], item[2], item[3], item[0])
            list_products.append(produto)
        return list_products

    def read_by_id(self, id: int) -> Product:
        product = None
        script = f"SELECT id, name, description, price FROM products WHERE id = {id};"
        result = super().read(script)
        if result:
            for item in result:
                product = Product(item[1], item[2], item[3], item[0])
        return product

    def delete(self, id: int) -> bool:
        try:
            script = f"DELETE FROM products WHERE id = {id};"
            super().execute(script)
            return True
        except Exception as e:
            return False

    def update(self, model: Product) -> bool:
        try:
            script = f"UPDATE products SET name = '{model.name}', description = '{model.description}', \
                price = '{model.price}' WHERE id = {model.id};"
            super().execute(script)
            return True
        except Exception as e:
            return False

    def entity(self):
        return 'Products'
