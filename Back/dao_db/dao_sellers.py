from .connection import *
from Back.models.model_sellers import Seller


def save_seller(seller:Seller) -> None:
    with psycopg2.connect(credentials()) as conn:
        cursor = conn.cursor()
        sql = f"INSERT INTO sellers (name, phone, email) VALUES ('{seller.name}','{seller.phone}','{seller.email}');"
        cursor.execute(sql)
        conn.commit()

def list_sellers() -> list:
    sellers = []
    with psycopg2.connect(credentials()) as conn:
        cursor = conn.cursor()
        sql = "SELECT name, phone, email, id FROM sellers;"
        cursor.execute(sql)
        result = cursor.fetchall()
        for item in result:
            seller = Seller(item[0], item[1], item[2], item[3])
            sellers.append(seller)
    return sellers

def get_by_id(id:int) -> Seller:
    with psycopg2.connect(credentials()) as conn:
        cursor = conn.cursor()
        sql = f"SELECT name, phone, email, id FROM sellers WHERE id = {id};"
        cursor.execute(sql)
        result = cursor.fetchone()
        seller = Seller(result[0], result[1], result[2], result[3])
    return seller

def update_seller(seller:Seller) -> None:
    with psycopg2.connect(credentials()) as conn:
        cursor = conn.cursor()
        sql = f"""
                UPDATE sellers SET 
                name = '{seller.name}', phone = '{seller.phone}', email = '{seller.email}'
                WHERE id = {seller.id};
                """
        cursor.execute(sql)
        conn.commit()

def delete_seller(id:int) -> None:
    with psycopg2.connect(credentials()) as conn:
        cursor = conn.cursor()
        sql = f"DELETE FROM sellers WHERE id = {id};"
        cursor.execute(sql)
        conn.commit()
