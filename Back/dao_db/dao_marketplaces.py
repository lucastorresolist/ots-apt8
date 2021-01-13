from .connection import *
from Back.models.model_marketplaces import Marketplace


def save_mkplace(marketplace:Marketplace) -> None:
    with psycopg2.connect(credentials()) as conn:
        cursor = conn.cursor()
        sql = f"INSERT INTO marketplaces (name, description) values ('{marketplace.name}','{marketplace.description}')"
        cursor.execute(sql)
        conn.commit()

def list_mkplaces():
    marketplaces = []
    with psycopg2.connect(credentials()) as conn:
        cursor = conn.cursor()
        sql = "select name, description, id from marketplaces"
        cursor.execute(sql)
        result = cursor.fetchall()
        for item in result:
            marketplace = Marketplace(item[0], item[1], item[2])
            marketplaces.append(marketplace)
    return marketplaces
