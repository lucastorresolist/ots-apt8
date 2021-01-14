from Back.models.model_products import Product
from Back.dao_db.connection import Connection


def save_product(product: Product) -> None:
    with Connection() as conn:
        cursor = conn.cursor()
        sql = f"INSERT INTO products (name, description, price) values ('{product.name}','{product.description}', '{product.price}')"
        cursor.execute(sql)
        conn.commit()


def list_products():
    list_products = []
    with Connection() as conn:
        cursor = conn.cursor()
        sql = "SELECT id, name, description, price FROM products"
        cursor.execute(sql)
        result = cursor.fetchall()
        for item in result:
            produto = Product(item[1], item[2], item[3], item[0])
            list_products.append(produto)
    return list_products


def list_product_byId(id: int) -> Product:
    product = None
    with Connection() as conn:
        cursor = conn.cursor()
        sql = f"SELECT id, name, description, price FROM products WHERE id = {id};"
        cursor.execute(sql)
        result = cursor.fetchall()
        if result:
            for item in result:
                product = Product(item[1], item[2], item[3], item[0])
    return product


def delete_product(id: int) -> bool:
    try:
        with Connection() as conn:
            cursor = conn.cursor()
            sql = f"DELETE FROM products WHERE id = {id};"
            cursor.execute(sql)
        return True
    except Exception as e:
        return False


def update_product(product: Product) -> bool:
    try:
        with Connection() as conn:
            cursor = conn.cursor()
            sql = f"UPDATE products SET name = '{product.name}', description = '{product.description}', \
            price = '{product.price}' WHERE id = {product.id};"
            cursor.execute(sql)
        return True
    except Exception as e:
        return False
