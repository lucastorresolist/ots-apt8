from .connection import *
from Back.models.model_marketplaces import Marketplace


def save_mkplace(marketplace:Marketplace) -> None:
    with psycopg2.connect(credentials()) as conn:
        cursor = conn.cursor()
        sql = f"INSERT INTO marketplaces (name, description) VALUES ('{marketplace.name}','{marketplace.description}');"
        cursor.execute(sql)
        conn.commit()

def list_mkplaces() -> list:
    marketplaces = []
    with psycopg2.connect(credentials()) as conn:
        cursor = conn.cursor()
        sql = "SELECT name, description, id FROM marketplaces;"
        cursor.execute(sql)
        result = cursor.fetchall()
        for item in result:
            marketplace = Marketplace(item[0], item[1], item[2])
            marketplaces.append(marketplace)
    return marketplaces

def get_by_id(id:int) -> int:
    with psycopg2.connect(credentials()) as conn:
        cursor = conn.cursor()
        sql = f"SELECT name, description, id FROM marketplaces WHERE id = {id};"
        cursor.execute(sql)
        result = cursor.fetchone()
        marketplace = Marketplace(result[0], result[1], result[2])
    return marketplace

def update_mktplace(marketplace:Marketplace) -> None:
    with psycopg2.connect(credentials()) as conn:
        cursor = conn.cursor()
        sql = f"""
                UPDATE marketplaces SET 
                name = '{marketplace.name}', description = '{marketplace.description}'
                WHERE id = {marketplace.id};
                """
        cursor.execute(sql)
        conn.commit()

def delete_mktplace(id:int) -> None:
    with psycopg2.connect(credentials()) as conn:
        cursor = conn.cursor()
        sql = f"DELETE FROM marketplaces WHERE id = {id};"
        cursor.execute(sql)
        conn.commit()
