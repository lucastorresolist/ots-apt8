from Back.models.categories import Category
import psycopg2
_host = 'pgsql08-farm15.uni5.net'
_user = 'topskills13'
_password = 'olist123'
_database = 'topskills13'
connection_string = f"host={_host} user={_user} dbname={_database} password={_password}"


def save_category(category: Category) -> None:
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    sql = f"INSERT INTO categories (name, description) values ('{category.name}','{category.description}')"
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


def list_categories():
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    sql = "select id, name, description from categories"
    cursor.execute(sql)
    result = cursor.fetchall()
    list_categories = []
    for item in result:
        category = Category(item[1], item[2], item[0])
        list_categories.append(category)
    return list_categories
