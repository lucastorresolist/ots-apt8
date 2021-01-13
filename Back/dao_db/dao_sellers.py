from .connection import *
from Back.models.model_sellers import Seller


def save_seller(seller:Seller) -> None:
    with psycopg2.connect(credentials()) as conn:
        cursor = conn.cursor()
        sql = f"INSERT INTO sellers (name, phone, email) values ('{seller.name}','{seller.phone}','{seller.email}')"
        cursor.execute(sql)
        conn.commit()

def list_sellers():
    sellers = []
    with psycopg2.connect(credentials()) as conn:
        cursor = conn.cursor()
        sql = "select name, phone, email, id from sellers"
        cursor.execute(sql)
        result = cursor.fetchall()
        for item in result:
            seller = Seller(item[0], item[1], item[2], item[3])
            sellers.append(seller)
    return sellers
