from Back.models.model_categories import Category
from Back.dao_db.connection import *


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


def list_category_byId(id: int) -> Category:
    category = None
    with psycopg2.connect(credentials()) as conn:
        cursor = conn.cursor()
        sql = f"SELECT id, name, description FROM categories WHERE id = {id};"
        cursor.execute(sql)
        result = cursor.fetchall()
        if result:
            for item in result:
                category = Category(item[1], item[2], item[0])
    return category


def delete_category(id: int) -> bool:
    try:
        with psycopg2.connect(credentials()) as conn:
            cursor = conn.cursor()
            sql = f"DELETE FROM categories WHERE id = {id};"
            cursor.execute(sql)
        return True
    except Exception as e:
        return False


def update_category(category: Category) -> bool:
    try:
        with psycopg2.connect(credentials()) as conn:
            cursor = conn.cursor()
            sql = f"UPDATE categories SET name = '{category.name}', description = '{category.description}' \
            WHERE id = {category.id};"
            cursor.execute(sql)
        return True
    except Exception as e:
        return False
