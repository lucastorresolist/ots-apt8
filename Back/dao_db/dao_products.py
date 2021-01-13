from .connection import *
from Back.models.model_products import Product


def save_product(product: Product) -> None:
    with psycopg2.connect(credentials()) as conn:
        cursor = conn.cursor()
        sql = f"INSERT INTO products (name, description, price) values ('{product.name}','{product.description}', '{product.price}')"
        cursor.execute(sql)
        conn.commit()


def list_products():
    with psycopg2.connect(credentials()) as conn:
        cursor = conn.cursor()
        sql = "SELECT id, name, description, price FROM products"
        cursor.execute(sql)
        result = cursor.fetchall()
        list_products = []
        for item in result:
            produto = Product(item[1], item[2], item[3], item[0])
            list_products.append(produto)
    return list_products
