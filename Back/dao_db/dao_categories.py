from .connection import *
from Back.models.model_categories import Category


def save_category(category: Category) -> None:
    with psycopg2.connect(credentials()) as conn:
        cursor = conn.cursor()
        sql = f"INSERT INTO categories (name, description) values ('{category.name}','{category.description}')"
        cursor.execute(sql)
        conn.commit()


def list_categories():
    list_categories = []
    with psycopg2.connect(credentials()) as conn:
        cursor = conn.cursor()
        sql = "select id, name, description from categories"
        cursor.execute(sql)
        result = cursor.fetchall()
        for item in result:
            category = Category(item[1], item[2], item[0])
            list_categories.append(category)
    return list_categories
