import psycopg2
_host = 'pgsql08-farm15.uni5.net'
_user = 'topskills13'
_password = 'olist123'
_database = 'topskills13'
connection_string = f"host={_host} user={_user} dbname={_database} password={_password}"

def save_category(name:str, description:str) -> None:
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    sql = f"INSERT INTO categories (name, description) values ('{name}','{description}')"
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


def list_categories():
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    sql = "select name, description from categories"
    cursor.execute(sql)
    list_categories = cursor.fetchall()
    return list_categories
