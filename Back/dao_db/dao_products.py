from Back.models.products import Product
import psycopg2
_host = 'pgsql08-farm15.uni5.net'
_user = 'topskills13'
_password = 'olist123'
_database = 'topskills13'
connection_string = f"host={_host} user={_user} dbname={_database} password={_password}"


def save_product(product: Product) -> None:
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    sql = f"INSERT INTO products (name, description, price) values ('{product.name}','{product.description}', '{product.price}')"
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


def list_products():
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    sql = "SELECT id, name, description, price FROM products"
    cursor.execute(sql)
    result = cursor.fetchall()
    list_products = []
    for item in result:
        produto = Product(item[1], item[2], item[3], item[0])
        list_products.append(produto)
    return list_products
