import psycopg2
_host = 'pgsql08-farm15.uni5.net'
_user = 'topskills13'
_password = 'olist123'
_database = 'topskills13'
connection_string = f"host={_host} user={_user} dbname={_database} password={_password}"

def save_product(name:str, description:str, price:str) -> None:
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    sql = f"INSERT INTO products (name, description, price) values ('{name}','{description}', '{price}')"
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

def list_products():
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    sql = "select name, description, price from product"
    cursor.execute(sql)
    list_products = cursor.fetchall()
    return list_products